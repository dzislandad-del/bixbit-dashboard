#!/usr/bin/env python3
"""run-command.py — выполнить команду из белого списка SEO Workspace (app/server.py COMMANDS).

Нужен для очереди запусков из BiXBiT SEO Hub: команда из хаба → /hub-sync → этот скрипт.
Список команд тот же, что в Workspace; произвольные команды не принимаются.
Платные (confirm/cost) и отправляющие наружу (external) запускать только после подтверждения владельца.

Примеры:
  ./scripts/run-command.py --list
  ./scripts/run-command.py index-check
  ./scripts/run-command.py reindex-dry --urls https://bixbit.io/en/firmwares
Лог: data/runs/<дата>-<id>.log; отчёт понятным языком: reports/runs/<дата>-<id>.md; в stdout — итог (JSON).
"""
import argparse, datetime as dt, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "app"))
import server  # noqa: E402
import run_report  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?")
    ap.add_argument("--urls", default="", help="URL через пробел или перевод строки (для команд переобхода)")
    ap.add_argument("--list", action="store_true", help="показать белый список")
    ap.add_argument("--tail", type=int, default=25, help="сколько последних строк вывода показать")
    a = ap.parse_args()
    if a.list or not a.cmd:
        for c in server.COMMANDS:
            flags = [f"${c['cost']}" if c.get("cost") else "", "подтверждение" if c.get("confirm") else "", "наружу" if c.get("external") else ""]
            print(f"{c['id']:15} {c['group']:22} {c['title']}  {' '.join(f for f in flags if f)}")
        return
    c = server.CMD.get(a.cmd)
    if not c:
        sys.exit(f"нет такой команды: {a.cmd} (см. --list)")
    urls = []
    if c.get("needs_urls"):
        import re
        urls = [x.strip() for x in re.split(r"[\s,]+", a.urls) if x.strip()]
        bad = [x for x in urls if not server.URL_RE.match(x)]
        if bad or not urls:
            sys.exit(f"URL не прошли проверку: {' '.join(bad) or 'пусто'}")
    today = dt.date.today().isoformat()
    snap = server.latest("data/page-snapshot-*.json") or ""
    os.makedirs(os.path.join(ROOT, "data/runs"), exist_ok=True)
    log_path = os.path.join(ROOT, "data/runs", f"{today}-{c['id']}.log")
    lines, rc, started = [], 0, dt.datetime.now().timestamp()
    for step in c["steps"]:
        argv = []
        for s in step:
            if s == "{urls}":
                argv.append(",".join(urls))
            else:
                argv.append(s.replace("{today}", today).replace("{latest_snapshot}", os.path.relpath(snap, ROOT) if snap else ""))
        lines.append("$ " + " ".join(argv))
        p = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        lines += p.stdout.splitlines()
        rc = p.returncode
        if rc and rc not in c.get("warn_codes", []):
            break
    status = "ok" if rc == 0 else ("warn" if rc in c.get("warn_codes", []) else "error")
    open(log_path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    report = run_report.build(c["id"], c["title"], "done" if status == "ok" else status, lines, started, dt.datetime.now().timestamp(), urls)
    print(json.dumps({"cmd": c["id"], "status": status, "rc": rc, "log": os.path.relpath(log_path, ROOT), "report": report,
                      "tail": "\n".join(lines[-a.tail:])}, ensure_ascii=False, indent=1))
    sys.exit(0 if status != "error" else 1)


if __name__ == "__main__":
    main()
