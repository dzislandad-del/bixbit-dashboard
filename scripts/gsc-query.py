#!/usr/bin/env python3
"""gsc-query.py — выгрузка Search Console searchAnalytics в JSON.

Авторизация: service account из .env (GOOGLE_APPLICATION_CREDENTIALS, GSC_SITE_URL)
через scripts/seo_common.py. Секреты не печатаются.

Примеры:
  ./scripts/gsc-query.py --days 28 --dimensions query,page --country usa \
      --out data/gsc-queries-us-2026-09-28.json
  ./scripts/gsc-query.py --start 2026-08-01 --end 2026-08-31 --dimensions page

Зависимости: python3 (stdlib), openssl.
"""
import argparse, datetime as dt, json, os, sys
import urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ROOT, load_env, google_token  # noqa: E402












def query(token, site, body):
    url = ("https://www.googleapis.com/webmasters/v3/sites/"
           f"{urllib.parse.quote(site, safe='')}/searchAnalytics/query")
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors="replace")[:300]
        sys.exit(f"GSC API error {e.code}: {msg}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=os.path.join(ROOT, ".env"))
    p.add_argument("--days", type=int, default=28, help="окно, если не заданы --start/--end (конец = сегодня-3, лаг GSC)")
    p.add_argument("--start"); p.add_argument("--end")
    p.add_argument("--dimensions", default="query,page", help="query,page,country,device,date")
    p.add_argument("--country", help="ISO-3166 alpha-3, напр. usa")
    p.add_argument("--page-contains", help="фильтр page contains, напр. /en/")
    p.add_argument("--search-type", default="web")
    p.add_argument("--row-limit", type=int, default=25000)
    p.add_argument("--out", help="путь для JSON; без него — сводка в stdout")
    a = p.parse_args()

    env = load_env(a.env)
    site = env.get("GSC_SITE_URL")
    if not site or not env.get("GOOGLE_APPLICATION_CREDENTIALS"):
        sys.exit("GSC_SITE_URL / GOOGLE_APPLICATION_CREDENTIALS не заданы в .env")

    end = a.end or (dt.date.today() - dt.timedelta(days=3)).isoformat()
    start = a.start or (dt.date.fromisoformat(end) - dt.timedelta(days=a.days - 1)).isoformat()
    filters = []
    if a.country:
        filters.append({"dimension": "country", "operator": "equals", "expression": a.country})
    if a.page_contains:
        filters.append({"dimension": "page", "operator": "contains", "expression": a.page_contains})

    token = google_token(env["GOOGLE_APPLICATION_CREDENTIALS"], ["https://www.googleapis.com/auth/webmasters.readonly"])
    dims = [d for d in a.dimensions.split(",") if d]
    rows, start_row = [], 0
    while True:
        body = {"startDate": start, "endDate": end, "dimensions": dims, "type": a.search_type,
                "rowLimit": min(a.row_limit - len(rows), 25000), "startRow": start_row,
                "dataState": "final"}
        if filters:
            body["dimensionFilterGroups"] = [{"filters": filters}]
        batch = query(token, site, body).get("rows", [])
        rows += batch
        start_row += len(batch)
        if len(batch) < 25000 or len(rows) >= a.row_limit:
            break

    out = {"meta": {"site": site, "start": start, "end": end, "dimensions": dims,
                    "filters": filters, "search_type": a.search_type,
                    "rows": len(rows), "pulled_at": dt.datetime.now().isoformat(timespec="seconds")},
           "rows": [dict(zip(dims, r["keys"]), clicks=r["clicks"], impressions=r["impressions"],
                         ctr=round(r["ctr"], 4), position=round(r["position"], 1)) for r in rows]}
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        json.dump(out, open(a.out, "w"), indent=1, ensure_ascii=False)
    m = out["meta"]
    print(f"GSC {m['site']} {m['start']}..{m['end']} dims={','.join(dims)} rows={m['rows']}"
          f" clicks={sum(r['clicks'] for r in out['rows'])} impressions={sum(r['impressions'] for r in out['rows'])}"
          + (f" -> {a.out}" if a.out else ""))


if __name__ == "__main__":
    main()
