#!/usr/bin/env python3
"""bing-query.py — выгрузка Bing Webmaster Tools API в JSON.

Ключ берётся из .env (BING_WEBMASTER_API_KEY) и нигде не печатается
(в сообщениях об ошибках он заменяется на ***).

Отчёты (--report):
  sites     GetUserSites            — подтверждённые сайты аккаунта
  queries   GetQueryStats           — запросы: показы, клики, ср. позиция (по неделям)
  pages     GetPageStats            — страницы: показы, клики, ср. позиция
  traffic   GetRankAndTrafficStats  — показы/клики по дням
  crawl     GetCrawlStats           — краул: страницы, ошибки, блокировки
  links     GetLinkCounts           — входящие ссылки по страницам сайта

Примеры:
  ./scripts/bing-query.py --report sites
  ./scripts/bing-query.py --report queries --out data/bing-queries-2026-09-28.json
"""
import argparse, datetime as dt, json, os, re, sys, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ROOT, load_env  # noqa: E402
BASE = "https://ssl.bing.com/webmaster/api.svc/json/"
REPORTS = {"sites": "GetUserSites", "queries": "GetQueryStats", "pages": "GetPageStats",
           "traffic": "GetRankAndTrafficStats", "crawl": "GetCrawlStats", "links": "GetLinkCounts"}








def call(key, method, **params):
    q = urllib.parse.urlencode({"apikey": key, **params})
    try:
        with urllib.request.urlopen(f"{BASE}{method}?{q}", timeout=60, context=CTX) as r:
            return json.load(r).get("d")
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors="replace")[:300].replace(key, "***")
        sys.exit(f"Bing API {method} error {e.code}: {msg}")
    except urllib.error.URLError as e:
        sys.exit(f"Bing API {method}: network error {e.reason}")


def fix_dates(o):
    # Bing отдаёт даты как "/Date(1695686400000-0700)/" → ISO
    if isinstance(o, dict):
        return {k: fix_dates(v) for k, v in o.items()}
    if isinstance(o, list):
        return [fix_dates(v) for v in o]
    if isinstance(o, str):
        m = re.fullmatch(r"/Date\((-?\d+)([+-]\d{4})?\)/", o)
        if m:
            return dt.datetime.fromtimestamp(int(m.group(1)) / 1000, dt.timezone.utc).date().isoformat()
    return o


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=os.path.join(ROOT, ".env"))
    p.add_argument("--report", choices=REPORTS, default="sites")
    p.add_argument("--site", help="siteUrl как в Bing (по умолчанию — найденный bixbit.io)")
    p.add_argument("--out", help="путь для JSON; без него — сводка в stdout")
    a = p.parse_args()

    key = load_env(a.env).get("BING_WEBMASTER_API_KEY")
    if not key or key.startswith("your_"):
        sys.exit("BING_WEBMASTER_API_KEY не задан в .env")

    sites = call(key, "GetUserSites") or []
    if a.report == "sites":
        data = fix_dates(sites)
    else:
        site = a.site or next((s["Url"] for s in sites if "bixbit.io" in s.get("Url", "")
                               and "bixbitusa" not in s.get("Url", "")), None)
        if not site:
            sys.exit("bixbit.io не найден среди сайтов Bing Webmaster — добавь/импортируй его из GSC")
        params = {"siteUrl": site}
        if a.report == "links":
            params["page"] = 0
        data = fix_dates(call(key, REPORTS[a.report], **params))

    rows = data if isinstance(data, list) else (data or {}).get("Links", data)
    out = {"meta": {"report": a.report, "method": REPORTS[a.report], "site": a.site or None,
                    "rows": len(rows) if isinstance(rows, list) else None,
                    "pulled_at": dt.datetime.now().isoformat(timespec="seconds")}, "data": data}
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        json.dump(out, open(a.out, "w"), indent=1, ensure_ascii=False)
    if a.report == "sites":
        for s in sites:
            print(f"  {s.get('Url')}  verified={s.get('IsVerified')}")
    print(f"Bing {REPORTS[a.report]}: rows={out['meta']['rows']}" + (f" -> {a.out}" if a.out else ""))


if __name__ == "__main__":
    main()
