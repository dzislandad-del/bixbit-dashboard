#!/usr/bin/env python3
"""backlinks-monitor.py — ежемесячный мониторинг ссылок (DataForSEO Backlinks).

- summary для bixbit.io и конкурентов: rank (0–100), backlinks, referring (main) domains,
  broken backlinks, spam score, dofollow/nofollow;
- для bixbit.io: новые ссылающиеся домены (first_seen за --days) и потерянные (lost_date за --days);
- diff с прошлым снимком: Δ по каждой метрике.
bixbitusa.io — партнёрский домен: не считается ни нашим, ни конкурентом.

Примеры:
  ./scripts/backlinks-monitor.py --dry-run
  ./scripts/backlinks-monitor.py --out data/backlinks/backlinks-2026-09-28.json
"""
import argparse, base64, datetime as dt, glob, json, os, sys, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, ROOT, load_env  # noqa: E402

API = "https://api.dataforseo.com/v3/backlinks/"
COMPETITORS = ["braiins.com", "vnish-firmware.com", "epicblockchain.io", "emcd.io", "luxor.tech",
               "awesomeminer.com", "hiveon.com", "minerstat.com"]
SUMMARY_FIELDS = ["rank", "backlinks", "referring_domains", "referring_main_domains", "referring_domains_nofollow",
                  "broken_backlinks", "broken_pages", "backlinks_spam_score", "referring_ips"]


def call(auth, endpoint, task):
    req = urllib.request.Request(API + endpoint, data=json.dumps([task]).encode(),
                                 headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120, context=CTX) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        return None, 0, f"HTTP {e.code}"
    t = (d.get("tasks") or [{}])[0]
    if t.get("status_code") != 20000:
        return None, t.get("cost") or 0, f"{t.get('status_code')} {t.get('status_message')}"
    return (t.get("result") or [None])[0], t.get("cost") or 0, None


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--target", default="bixbit.io")
    p.add_argument("--competitors", default=",".join(COMPETITORS))
    p.add_argument("--days", type=int, default=31, help="окно для новых/потерянных доменов")
    p.add_argument("--out")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    comps = [c.strip() for c in a.competitors.split(",") if c.strip() and "bixbitusa" not in c]
    print(f"цель {a.target} · конкуренты: {', '.join(comps)} · окно {a.days} дн")
    if a.dry_run:
        print(f"Запросов: {1 + len(comps)} summary + 2 списка ≈ $0.1–0.3 (точная цена — из ответа API)")
        return
    if not a.out:
        sys.exit("укажи --out или --dry-run")
    env = load_env(a.env)
    if not env.get("DATAFORSEO_LOGIN") or not env.get("DATAFORSEO_PASSWORD"):
        print("DataForSEO: пропущено — DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD не заданы")
        return
    auth = base64.b64encode(f"{env['DATAFORSEO_LOGIN']}:{env['DATAFORSEO_PASSWORD']}".encode()).decode()
    since = (dt.datetime.utcnow() - dt.timedelta(days=a.days)).strftime("%Y-%m-%d 00:00:00 +00:00")
    cost, summaries, errors = 0.0, {}, {}

    for tgt in [a.target] + comps:
        res, c, err = call(auth, "summary/live", {"target": tgt, "include_subdomains": True, "rank_scale": "one_hundred",
                                                  "exclude_internal_backlinks": True})
        cost += c
        if err:
            errors[tgt] = err; print(f"  {tgt}: ОШИБКА {err}"); continue
        summaries[tgt] = {f: res.get(f) for f in SUMMARY_FIELDS}
        s = summaries[tgt]
        print(f"  {tgt:22} rank {s['rank']:>3} · RD {s['referring_main_domains']:>6} · BL {s['backlinks']:>8} · broken {s['broken_backlinks']}"
              f" · spam {s['backlinks_spam_score']}")

    def rd_list(status, flt, order):
        res, c, err = call(auth, "referring_domains/live", {
            "target": a.target, "backlinks_status_type": status, "filters": flt, "order_by": [order], "limit": 200,
            "rank_scale": "one_hundred", "exclude_internal_backlinks": True})
        items = [{"domain": i["domain"], "rank": i.get("rank"), "backlinks": i.get("backlinks"),
                  "first_seen": (i.get("first_seen") or "")[:10], "lost_date": (i.get("lost_date") or "")[:10],
                  "spam_score": i.get("backlinks_spam_score"), "nofollow_only": i.get("referring_domains_nofollow") == i.get("referring_domains")}
                 for i in ((res or {}).get("items") or []) if "bixbitusa" not in i.get("domain", "")]
        return items, c, err

    new, c1, e1 = rd_list("live", ["first_seen", ">", since], "first_seen,desc")
    lost, c2, e2 = rd_list("lost", ["lost_date", ">", since], "lost_date,desc")
    cost += c1 + c2
    for e, name in ((e1, "new"), (e2, "lost")):
        if e:
            errors[f"{a.target}:{name}"] = e

    prev = [f for f in sorted(glob.glob(os.path.join(ROOT, "data/backlinks/backlinks-*.json")))
            if os.path.abspath(f) != os.path.abspath(a.out)]
    deltas = {}
    if prev:
        ps = json.load(open(prev[-1]))["summaries"]
        for tgt, s in summaries.items():
            if tgt in ps:
                deltas[tgt] = {f: (s[f] - ps[tgt][f]) if isinstance(s.get(f), (int, float)) and isinstance(ps[tgt].get(f), (int, float)) else None
                               for f in SUMMARY_FIELDS}
    doc = {"meta": {"collected_on": dt.date.today().isoformat(), "target": a.target, "window_days": a.days, "since": since[:10],
                    "compared_to": os.path.relpath(prev[-1], ROOT) if prev else None, "cost_usd": round(cost, 4),
                    "note": "rank по шкале 0–100 (DataForSEO rank, не Ahrefs DR)"},
           "summaries": summaries, "deltas": deltas, "new_referring_domains": new, "lost_referring_domains": lost, "errors": errors}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(doc, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"\n{a.target}: новых доменов за {a.days} дн: {len(new)} · потерянных: {len(lost)} · ${cost:.4f} -> {os.path.relpath(os.path.abspath(a.out), ROOT)}")
    for x in new[:10]:
        print(f"   + {x['domain']:35} rank {x['rank']} · {x['first_seen']} · spam {x['spam_score']}")
    for x in lost[:10]:
        print(f"   - {x['domain']:35} rank {x['rank']} · lost {x['lost_date']}")


if __name__ == "__main__":
    main()
