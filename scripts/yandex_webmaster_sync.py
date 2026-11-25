#!/usr/bin/env python3
"""yandex_webmaster_sync.py — Яндекс.Вебмастер → дашборд (Supabase).

bixbit.tech — зеркало bixbit.io. Яндекс отдаёт статистику главному зеркалу, а bixbit.io
в РФ заблокирован, поэтому по умолчанию берутся ОБА сайта и суммируются (запросы — по тексту).
Двойного счёта нет: показы приписываются только одному из склеенных зеркал.

Для квартала (по умолчанию — текущий) пишет в payload.periods["from|to"].organic:
  yandex_wm        — по всему сайту: показы, клики, CTR, ср. позиция (история по дням),
                     ИКС, страниц в поиске / исключено, проблемы сайта, топ-500 запросов с позициями
  ru/en/es.yandex  — показы, клики и ср. позиция Яндекса по языку. Вебмастер не отдаёт
                     статистику по страницам, поэтому язык определяется по языку запроса
                     (кириллица → RU, испанские слова/символы → ES, остальное → EN), а итоги
                     сайта делятся пропорционально. Время, отказы и конверсии Яндекса
                     (Метрика) остаются ручными.
Итоги по языку пересчитываются: Google + Яндекс.

Примеры:
  ./scripts/yandex_webmaster_sync.py                      # текущий квартал
  ./scripts/yandex_webmaster_sync.py --quarter 2026-Q3
  ./scripts/yandex_webmaster_sync.py --hosts bixbit.io     # только один сайт
  ./scripts/yandex_webmaster_sync.py --dry-run

Секреты: YANDEX_WEBMASTER_TOKEN (OAuth, право webmaster:hostinfo), SUPABASE_URL, SUPABASE_ANON_KEY.
"""
import argparse, datetime as dt, json, os, re, sys, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, load_env  # noqa: E402
from organic_sync import LANGS, merge_totals, quarter_bounds, sb_load, sb_save  # noqa: E402

API = "https://api.webmaster.yandex.net/v4"
ES_WORDS = re.compile(r"\b(de|para|que|como|precio|precios|comprar|minero|mineros|minería|mineria|venta|en|el|la|los|las|con|por)\b")


class YW:
    def __init__(self, token):
        self.token = token

    def get(self, path, params=None):
        url = API + path + ("?" + urllib.parse.urlencode(params, doseq=True) if params else "")
        r = urllib.request.Request(url, headers={"Authorization": f"OAuth {self.token}"})
        try:
            with urllib.request.urlopen(r, timeout=60, context=CTX) as resp:
                raw = resp.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:300].replace(self.token, "***")
            hint = " — токен недействителен или истёк: выпустите новый на oauth.yandex.ru" if e.code in (401, 403) else ""
            sys.exit(f"Yandex Webmaster API {e.code} {path.split('/hosts/')[-1]}: {msg}{hint}")
        except urllib.error.URLError as e:
            sys.exit(f"Yandex Webmaster API: сеть — {e.reason}")


def q_lang(text):
    t = (text or "").lower()
    if re.search(r"[а-яё]", t):
        return "ru"
    if re.search(r"[ñ¿¡áéíóú]", t) or ES_WORDS.search(t):
        return "es"
    return "en"


def pick_host(hosts, want):
    c = [h for h in hosts if want in h.get("ascii_host_url", "") and "bixbitusa" not in h.get("ascii_host_url", "")]
    c.sort(key=lambda h: (not h.get("verified"), not h["ascii_host_url"].startswith("https")))
    return c[0] if c else None


def rng(d1, d2):
    return {"date_from": f"{d1.isoformat()}T00:00:00+03:00", "date_to": f"{d2.isoformat()}T23:59:59+03:00"}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--quarter")
    p.add_argument("--hosts", default=os.environ.get("YANDEX_WM_HOSTS") or "bixbit.io,bixbit.tech",
                   help="сайты Вебмастера через запятую (зеркала суммируются)")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    env = load_env(a.env) if os.path.exists(a.env) else {}
    env.update({k: v for k, v in os.environ.items() if k.startswith(("YANDEX_", "SUPABASE_"))})
    need = ["YANDEX_WEBMASTER_TOKEN"] + ([] if a.dry_run else ["SUPABASE_URL", "SUPABASE_ANON_KEY"])
    missing = [k for k in need if not env.get(k)]
    if missing:
        sys.exit("Не заданы: " + ", ".join(missing))

    today = dt.date.today()
    q_start, q_end = quarter_bounds(a.quarter, today)
    end = min(q_end, today - dt.timedelta(days=1))
    if end < q_start:
        print("Квартал ещё не начался — пропуск"); return
    pkey = f"{q_start.isoformat()}|{q_end.isoformat()}"

    yw = YW(env["YANDEX_WEBMASTER_TOKEN"])
    uid = yw.get("/user")["user_id"]
    hosts = yw.get(f"/user/{uid}/hosts").get("hosts", [])
    picked = []
    for want in [x.strip() for x in a.hosts.split(",") if x.strip()]:
        h = pick_host(hosts, want)
        if not h:
            print(f"  ! {want}: нет в Вебмастере — пропуск"); continue
        if not h.get("verified"):
            print(f"  ! {h['ascii_host_url']}: не подтверждён — пропуск"); continue
        if h["host_id"] not in [x["host_id"] for x in picked]:
            picked.append(h)
    if not picked:
        sys.exit("Ни один сайт из списка не найден/не подтверждён. В Вебмастере: " +
                 ", ".join(f"{x.get('ascii_host_url', '?')}{'' if x.get('verified') else ' (не подтв.)'}" for x in hosts))

    byday, qmap, per_host = {}, {}, []
    sqi, searchable, excluded, problems = None, 0, 0, {}
    for h in picked:
        base = f"/user/{uid}/hosts/{urllib.parse.quote(h['host_id'], safe='')}"
        sm = yw.get(base + "/summary")
        hist = yw.get(base + "/search-queries/all/history", {
            "query_indicator": ["TOTAL_SHOWS", "TOTAL_CLICKS", "AVG_SHOW_POSITION"], **rng(q_start, end)}).get("indicators", {})
        hs = hc = 0
        tmp = {}
        for ind, key in (("TOTAL_SHOWS", "shows"), ("TOTAL_CLICKS", "clicks"), ("AVG_SHOW_POSITION", "pos")):
            for pt in hist.get(ind, []) or []:
                tmp.setdefault(pt["date"][:10], {})[key] = pt.get("value") or 0
        for d, v in tmp.items():
            x = byday.setdefault(d, {"date": d, "shows": 0, "clicks": 0, "_pw": 0.0})
            x["shows"] += v.get("shows", 0); x["clicks"] += v.get("clicks", 0)
            x["_pw"] += (v.get("pos") or 0) * v.get("shows", 0)
            hs += v.get("shows", 0); hc += v.get("clicks", 0)
        pq = yw.get(base + "/search-queries/popular", {
            "order_by": "TOTAL_SHOWS", "limit": 500, **rng(q_start, end),
            "query_indicator": ["TOTAL_SHOWS", "TOTAL_CLICKS", "AVG_SHOW_POSITION", "AVG_CLICK_POSITION"]}).get("queries", [])
        for q in pq:
            i, t = q.get("indicators", {}), q.get("query_text", "")
            x = qmap.setdefault(t.lower(), {"q": t, "lang": q_lang(t), "shows": 0, "clicks": 0, "_pw": 0.0, "_cw": 0.0})
            sh, cl = i.get("TOTAL_SHOWS") or 0, i.get("TOTAL_CLICKS") or 0
            x["shows"] += sh; x["clicks"] += cl
            x["_pw"] += (i.get("AVG_SHOW_POSITION") or 0) * sh; x["_cw"] += (i.get("AVG_CLICK_POSITION") or 0) * cl
        if sm.get("sqi") is not None:
            sqi = max(sqi or 0, sm["sqi"])
        searchable += sm.get("searchable_pages_count") or 0
        excluded += sm.get("excluded_pages_count") or 0
        for k, v in (sm.get("site_problems") or {}).items():
            if v:
                problems[k] = problems.get(k, 0) + v
        mm = (h.get("main_mirror") or {}).get("ascii_host_url")
        per_host.append({"host": h["ascii_host_url"], "main_mirror": mm, "shows": int(hs), "clicks": int(hc),
                         "sqi": sm.get("sqi"), "searchable": sm.get("searchable_pages_count"),
                         "excluded": sm.get("excluded_pages_count")})
        print(f"  {h['ascii_host_url']}{' (зеркало → ' + mm + ')' if mm else ''}: показы {int(hs)}, клики {int(hc)}, "
              f"ИКС {sm.get('sqi')}, в поиске {sm.get('searchable_pages_count')}, запросов {len(pq)}")

    days = []
    for d in sorted(byday):
        x = byday[d]
        days.append({"date": d, "shows": int(x["shows"]), "clicks": int(x["clicks"]),
                     "pos": round(x["_pw"] / x["shows"], 1) if x["shows"] else None})
    shows = sum(x["shows"] for x in days)
    clicks = sum(x["clicks"] for x in days)
    avg_pos = round(sum(byday[d]["_pw"] for d in byday) / shows, 1) if shows else None
    queries = []
    for x in sorted(qmap.values(), key=lambda v: -v["shows"])[:500]:
        queries.append({"q": x["q"], "lang": x["lang"], "shows": int(x["shows"]), "clicks": int(x["clicks"]),
                        "pos": round(x["_pw"] / x["shows"], 1) if x["shows"] and x["_pw"] else None,
                        "clickPos": round(x["_cw"] / x["clicks"], 1) if x["clicks"] and x["_cw"] else None})

    # доли языков по топ-запросам → оценка показов/кликов сайта по языкам
    share = {lg: {"shows": 0, "clicks": 0, "pw": 0.0} for lg in LANGS}
    for q in queries:
        s_ = share[q["lang"]]; s_["shows"] += q["shows"]; s_["clicks"] += q["clicks"]
        s_["pw"] += (q["pos"] or 0) * q["shows"]
    ts = sum(x["shows"] for x in share.values()) or 1
    tc = sum(x["clicks"] for x in share.values()) or 1
    per_lang = {lg: {"impressions": round(shows * share[lg]["shows"] / ts), "clicks": round(clicks * share[lg]["clicks"] / tc),
                     "position": round(share[lg]["pw"] / share[lg]["shows"], 1) if share[lg]["shows"] else None}
                for lg in LANGS}

    wm = {"host": " + ".join(x["host"] for x in per_host), "hosts": per_host, "from": q_start.isoformat(), "to": end.isoformat(),
          "shows": int(shows), "clicks": int(clicks), "ctr": round(clicks / shows * 100, 2) if shows else 0,
          "avg_pos": avg_pos, "sqi": sqi, "searchable": searchable,
          "excluded": excluded, "problems": problems,
          "history": days, "queries": queries,
          "lang_method": "по языку запроса (топ-500), итоги сайта распределены пропорционально",
          "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}

    print(f"Яндекс.Вебмастер {wm['host']} {q_start}..{end} (сумма): показы {wm['shows']}, клики {wm['clicks']}, "
          f"CTR {wm['ctr']}%, ср. позиция {avg_pos}, ИКС {wm['sqi']}, в поиске {wm['searchable']}, исключено {wm['excluded']}")
    for lg in LANGS:
        x = per_lang[lg]
        print(f"  {lg.upper()} (оценка): показы {x['impressions']}, клики {x['clicks']}, позиция {x['position']}")
    if a.dry_run:
        print("dry-run: в Supabase ничего не записано"); return

    payload = sb_load(env["SUPABASE_URL"], env["SUPABASE_ANON_KEY"])
    org = payload.setdefault("periods", {}).setdefault(pkey, {}).setdefault("organic", {})
    org["yandex_wm"] = wm
    for lg in LANGS:
        cur = org.setdefault(lg, {})
        y = cur.get("yandex") or {}
        y.update({"impressions": per_lang[lg]["impressions"], "clicks": per_lang[lg]["clicks"],
                  "position": per_lang[lg]["position"], "source": "webmaster", "estimated": True})
        cur["yandex"] = y
        cur.update(merge_totals(cur.get("google") or {}, y))
    sb_save(env["SUPABASE_URL"], env["SUPABASE_ANON_KEY"], payload)
    print(f"✓ Записано в Supabase: periods[{pkey}].organic.yandex_wm + Яндекс по языкам")


if __name__ == "__main__":
    main()
