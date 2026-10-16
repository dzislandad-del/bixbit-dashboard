#!/usr/bin/env python3
"""alerts.py — алерты по сайту bixbit.io в Telegram.

Что проверяет:
  живьём:   ключевые URL отвечают 200 (и не редиректят в никуда), robots.txt не закрывает сайт,
            sitemap.xml доступен, время ответа;
  по data/: Яндекс.Вебмастер (FATAL/CRITICAL, падение числа страниц в поиске), индексация Google
            (URL Inspection: не PASS, чужой canonical), снимок страниц (noindex, canonical, статус),
            позиции (выпадение P0-ключей из топ-20, просадка ≥ 5), краул (рост ошибок),
            AI Overview (потеря цитаты), ссылки (потеря доменов с rank ≥ 20).

Шлёт только НОВЫЕ проблемы и «решено» для ушедших (состояние — data/alerts/state.json).
P0/P1 — сразу; P2 — только в сводке (--digest).

.env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID (можно несколько через запятую).

Примеры:
  ./scripts/alerts.py --get-chat-id          # после того как написали боту /start
  ./scripts/alerts.py --test                 # тестовое сообщение
  ./scripts/alerts.py --dry-run              # показать, что было бы отправлено
  ./scripts/alerts.py                        # проверить и отправить новые алерты
  ./scripts/alerts.py --digest               # + сводка состояния, даже если нового нет
  ./scripts/alerts.py --always               # ручная проверка: итог приходит всегда (ежедневный запуск — без флага)
"""
import argparse, datetime as dt, glob, html, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, ROOT, load_env, yandex_expected  # noqa: E402

STATE = os.path.join(ROOT, "data/alerts/state.json")
LIVE_URLS = ["https://bixbit.io/", "https://bixbit.io/en", "https://bixbit.io/ru", "https://bixbit.io/en/firmwares",
             "https://bixbit.io/en/firmwares/antminer", "https://bixbit.io/en/ams", "https://bixbit.io/ru/firmwares"]
UA = "Mozilla/5.0 (compatible; BiXBiT-SEO-alerts/1.0)"
ICON = {"P0": "🔴", "P1": "🟠", "P2": "🟡"}


def latest(pattern, n=1):
    files = sorted(f for f in glob.glob(os.path.join(ROOT, pattern)) if re.search(r"\d{4}-\d{2}-\d{2}", f))
    return files[-n:] if n > 1 else (files[-1] if files else None)


def jload(p):
    try:
        return json.load(open(p))
    except Exception:
        return None


def age_days(p):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", p or "")
    return (dt.date.today() - dt.date.fromisoformat(m.group(1))).days if m else 999


def fetch(url, timeout=25):
    t0 = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=timeout, context=CTX) as r:
            return r.status, r.read(200_000).decode("utf-8", "replace"), round(time.time() - t0, 1), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", round(time.time() - t0, 1), url
    except Exception as e:
        return 0, str(getattr(e, "reason", e)), round(time.time() - t0, 1), url


# ---------------- правила ----------------

def checks():
    A = []  # (id, severity, title, detail)

    # 1. живая доступность
    for u in LIVE_URLS:
        st, body, sec, final = fetch(u)
        if st != 200:
            A.append((f"down:{u}", "P0", f"Страница не отвечает 200: {u}", f"код {st or 'нет ответа'} {body[:80] if st == 0 else ''}".strip()))
        elif sec > 10:
            A.append((f"slow:{u}", "P2", f"Медленный ответ: {u}", f"{sec} с"))
        if st == 200 and u.rstrip("/") in ("https://bixbit.io/en", "https://bixbit.io/ru") and re.search(r'<meta[^>]+name="robots"[^>]+noindex', body, re.I):
            A.append((f"noindex:{u}", "P0", f"На {u} стоит noindex", "meta robots"))
    st, body, _, _ = fetch("https://bixbit.io/robots.txt")
    if st != 200:
        A.append(("robots:down", "P1", "robots.txt не отвечает 200", f"код {st}"))
    else:
        blocks = re.split(r"(?im)^user-agent:", body)
        for b in blocks[1:]:
            agent = b.splitlines()[0].strip()
            if agent in ("*", "Googlebot", "Yandex", "YandexBot") and re.search(r"(?im)^disallow:\s*/\s*$", b):
                A.append((f"robots:block:{agent}", "P0", f"robots.txt закрывает весь сайт для {agent}", "Disallow: /"))
    st, _, _, _ = fetch("https://bixbit.io/sitemap.xml")
    if st != 200:
        A.append(("sitemap:down", "P1", "sitemap.xml не отвечает 200", f"код {st}"))

    # 2. Яндекс.Вебмастер
    p = latest("data/yandex/yandex-diagnostics-*.json")
    d = jload(p) if p and age_days(p) <= 3 else None
    if d:
        expected = yandex_expected(d)
        for k, v in (d.get("data", {}).get("problems") or {}).items():
            if v.get("state") == "PRESENT" and v.get("severity") in ("FATAL", "CRITICAL") and k not in expected:
                A.append((f"yandex:{k}", "P0" if v["severity"] == "FATAL" else "P1", f"Яндекс.Вебмастер: {v['severity']} {k}",
                          "робот не может подключиться к сайту" if k == "CONNECT_FAILED" else "см. раздел «Диагностика»"))
    p = latest("data/yandex/yandex-insearch-*.json")
    d = jload(p) if p and age_days(p) <= 3 else None
    if d:
        h = [x["value"] for x in d.get("data", {}).get("history") or []]
        if len(h) >= 2 and max(h) > 100 and h[-1] < 0.7 * max(h):
            A.append(("yandex:insearch-drop", "P0", "Яндекс: резкое падение страниц в поиске", f"{max(h)} → {h[-1]}"))

    # 2a. Sitemap ↔ GSC и новые страницы (sitemap-monitor.py, еженедельно)
    p = latest("data/sitemap/sitemap-*.json")
    d = jload(p) if p and age_days(p) <= 8 else None
    if d:
        sm = d.get("summary", {})
        if sm.get("removed", 0) >= 20:
            A.append(("sitemap:removed", "P1", f"Из sitemap пропало {sm['removed']} URL", "проверить, не удалены ли страницы по ошибке"))
        if sm.get("fetch_errors"):
            A.append(("sitemap:fetch", "P1", "Sitemap не загружается полностью", f"ошибок: {sm['fetch_errors']}"))
        for g in (d.get("gsc") or {}).get("sitemaps", []):
            if g.get("errors"):
                A.append((f"sitemap:gsc:{g['path']}", "P2", f"Ошибки sitemap в GSC: {g['path'].replace('https://bixbit.io', '')}", f"ошибок {g['errors']}"))
        bad_new = [x for x in d.get("new_inspected", []) if x.get("verdict") not in ("PASS", None)]
        if bad_new:
            A.append(("sitemap:new-not-indexed", "P2", f"Новые страницы не в индексе Google: {len(bad_new)}",
                      ", ".join(x["url"].replace("https://bixbit.io", "") for x in bad_new[:3])))

    # 2b. Изменения на сайте между краулами (site-diff.py, ежемесячно)
    p = latest("data/site-diff/site-diff-*.json")
    d = jload(p) if p and age_days(p) <= 35 else None
    if d:
        sm, ch = d.get("summary", {}), d.get("changes", {})
        if sm.get("gone_pages", 0) >= 10:
            A.append(("site:gone", "P1", f"С сайта пропало {sm['gone_pages']} страниц с прошлого краула", "см. отчёт «Изменения на всём сайте»"))
        idx_lost = [x for x in ch.get("noindex", []) if x.get("new") is True]
        if idx_lost:
            A.append(("site:noindex", "P0", f"На {len(idx_lost)} страницах появился noindex", ", ".join(x["url"].replace("https://bixbit.io", "") for x in idx_lost[:3])))

    # 3. Индексация Google (URL Inspection)
    p = latest("data/index-check/index-*.json")
    d = jload(p) if p and age_days(p) <= 3 else None
    if d:
        for u in d.get("urls", []):
            if u.get("error"):
                continue
            if u.get("verdict") not in ("PASS", None):
                A.append((f"gindex:{u['url']}", "P1", f"Google: страница не в индексе — {u['url']}", f"{u.get('coverage_state')}"))
            if u.get("canonical_mismatch"):
                A.append((f"gcanon:{u['url']}", "P1", f"Google выбрал другой canonical — {u['url']}", f"{u.get('google_canonical')}"))

    # 4. Снимок страниц: критичные изменения
    p = latest("data/page-snapshot-*.json")
    d = jload(p) if p and age_days(p) <= 8 else None
    if d:
        for c in d.get("changes", []):
            if c["field"] in ("status", "robots", "x_robots_tag", "canonical"):
                now = str(c["now"])
                sev = "P0" if "noindex" in now.lower() or (c["field"] == "status" and now not in ("200",)) else "P1"
                A.append((f"snap:{c['url']}:{c['field']}", sev, f"Изменился {c['field']}: {c['url']}", f"{str(c['was'])[:60]} → {now[:60]}"))

    # 5. Позиции
    p = latest("data/rank-tracking/rank-*.json")
    d = jload(p) if p and age_days(p) <= 35 else None
    if d:
        for k in d.get("keywords", []):
            bp, np_ = k.get("baseline_position"), k.get("position")
            if k.get("priority") == "P0" and bp and bp <= 20 and (not np_ or np_ > 20) and "volatile" not in k.get("flags", []):
                A.append((f"rank-out:{k['keyword']}", "P1", f"Ключ P0 выпал из топ-20: «{k['keyword']}»", f"было {bp} → {np_ or 'нет в топ-100'}"))
            elif bp and np_ and np_ - bp >= 5:
                A.append((f"rank-drop:{k['keyword']}", "P2", f"Просадка позиции: «{k['keyword']}»", f"{bp} → {np_}"))

    # 6. Краул: рост ошибок
    ps = latest("data/crawl-*/summary.json", 2)
    if isinstance(ps, list) and len(ps) == 2:
        a, b = jload(ps[0]), jload(ps[1])
        if a and b:
            ea, eb = a["issues"].get("error_pages", 0), b["issues"].get("error_pages", 0)
            if eb > ea * 1.2 and eb - ea >= 10:
                A.append(("crawl:errors-up", "P1", "Краул: выросло число страниц с ошибками", f"{ea} → {eb}"))

    # 7. AI Overview: потеря цитаты
    p = latest("data/serp-features/serp-features-*.json")
    d = jload(p) if p and age_days(p) <= 8 else None
    if d:
        for c in d.get("changes", []):
            if c["field"] == "aio_cites_bixbit" and c["was"] and not c["now"]:
                A.append((f"aio-lost:{c['keyword']}", "P2", f"AI Overview перестал цитировать bixbit: «{c['keyword']}»", ""))

    # 8. Ссылки: потеря сильных доменов
    p = latest("data/backlinks/backlinks-*.json")
    d = jload(p) if p and age_days(p) <= 35 else None
    if d:
        for x in d.get("lost_referring_domains", []):
            if (x.get("rank") or 0) >= 20:
                A.append((f"link-lost:{x['domain']}", "P2", f"Потеряна ссылка с сильного домена: {x['domain']}", f"rank {x['rank']}, {x.get('lost_date')}"))
    return A


# ---------------- Telegram ----------------

def tg_send(token, chat_ids, text):
    ok = True
    for cid in chat_ids:
        data = urllib.parse.urlencode({"chat_id": cid, "text": text[:4000], "parse_mode": "HTML", "disable_web_page_preview": "true"}).encode()
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=data), timeout=30, context=CTX) as r:
                ok &= json.load(r).get("ok", False)
        except urllib.error.HTTPError as e:
            print(f"Telegram {e.code}: {e.read().decode(errors='replace')[:200].replace(token, '***')}")
            ok = False
    return ok


def fmt(items, header):
    lines = [f"<b>{html.escape(header)}</b>"]
    for aid, sev, title, detail in items:
        lines.append(f"{ICON.get(sev, '•')} <b>{sev}</b> {html.escape(title)}" + (f"\n   <i>{html.escape(detail)}</i>" if detail else ""))
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--digest", action="store_true", help="прислать сводку, даже если нового нет (+ P2)")
    p.add_argument("--always", action="store_true", help="ручной запуск: если нового нет, всё равно прислать короткий итог")
    p.add_argument("--test", action="store_true")
    p.add_argument("--get-chat-id", action="store_true")
    a = p.parse_args()

    env = load_env(a.env)
    token = env.get("TELEGRAM_BOT_TOKEN", "")
    chats = [c.strip() for c in (env.get("TELEGRAM_CHAT_ID") or "").split(",") if c.strip()]
    need_tg = not a.dry_run
    if need_tg and (not token or token.startswith("your_")):
        sys.exit("TELEGRAM_BOT_TOKEN не задан в .env")

    if a.get_chat_id:
        with urllib.request.urlopen(f"https://api.telegram.org/bot{token}/getUpdates", timeout=30, context=CTX) as r:
            ups = json.load(r).get("result", [])
        seen = {}
        for u in ups:
            ch = (u.get("message") or u.get("channel_post") or u.get("my_chat_member") or {}).get("chat")
            if ch:
                seen[ch["id"]] = ch.get("title") or ch.get("username") or ch.get("first_name")
        if not seen:
            print("Сообщений нет: напишите боту /start (или добавьте его в группу и напишите там), затем повторите.")
        for cid, name in seen.items():
            print(f"chat_id {cid}  ({name})")
        return
    if need_tg and not chats:
        sys.exit("TELEGRAM_CHAT_ID не задан в .env — узнайте его: ./scripts/alerts.py --get-chat-id")

    if a.test:
        ok = tg_send(token, chats, "✅ <b>BiXBiT SEO alerts</b> подключены.\nБуду писать сюда о проблемах сайта bixbit.io: доступность, индексация Google и Яндекса, noindex/canonical, позиции, краул.")
        print("отправлено" if ok else "ошибка отправки")
        return

    found = checks()
    state = jload(STATE) or {"active": {}}
    active = state.get("active", {})
    now = dt.datetime.now().isoformat(timespec="minutes")
    cur = {x[0]: x for x in found}
    new = [x for x in found if x[0] not in active and x[1] in ("P0", "P1")]
    resolved = [k for k in active if k not in cur]
    msgs = []
    if new:
        msgs.append(fmt(sorted(new, key=lambda x: x[1]), f"bixbit.io — новые проблемы ({len(new)})"))
    if resolved:
        msgs.append("<b>✅ Решено</b>\n" + "\n".join(f"• {html.escape(active[k]['title'])}" for k in resolved))
    if a.digest:
        if found:
            msgs.append(fmt(sorted(found, key=lambda x: x[1]), f"Сводка bixbit.io на {dt.date.today():%d.%m}: активных проблем {len(found)}"))
        else:
            msgs.append(f"<b>Сводка bixbit.io на {dt.date.today():%d.%m}</b>\n✅ Проблем не найдено.")

    if a.always and not msgs:
        rest = sorted(found, key=lambda x: x[1])
        msgs.append(f"<b>Проверка bixbit.io {dt.datetime.now():%d.%m %H:%M}</b>\n✅ Новых проблем P0/P1 нет."
                    + (f"\nИзвестных проблем: {len(rest)}\n" + "\n".join(f"• {sev} {html.escape(title)}" for _, sev, title, _ in rest[:10]) if rest else "\nИзвестных проблем нет."))

    for aid, sev, title, detail in found:
        print(f"{sev} {title} {('— ' + detail) if detail else ''}")
    print(f"найдено {len(found)} · новых P0/P1 {len(new)} · решено {len(resolved)}")

    if a.dry_run:
        for m in msgs:
            print("\n--- сообщение ---\n" + re.sub(r"</?[bi]>", "", m))
        return
    sent = all(tg_send(token, chats, m) for m in msgs) if msgs else True
    if sent:  # состояние обновляем только если доставили, иначе повторим в следующий раз
        state["active"] = {k: {"sev": v[1], "title": v[2], "since": active.get(k, {}).get("since", now)} for k, v in cur.items()}
        state["last_run"] = now
        os.makedirs(os.path.dirname(STATE), exist_ok=True)
        json.dump(state, open(STATE, "w"), indent=1, ensure_ascii=False)
    print(f"сообщений отправлено: {len(msgs)}" if sent else "не удалось отправить — состояние не обновлено")


if __name__ == "__main__":
    main()
