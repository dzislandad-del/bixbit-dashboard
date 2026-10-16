#!/usr/bin/env python3
"""ga4-query.py — выгрузка GA4 Data API (runReport) в JSON.

Service account из .env (GOOGLE_APPLICATION_CREDENTIALS, GA4_PROPERTY_ID).

Пресеты (--preset):
  organic-landing  органические сессии/вовлечённость/конверсии по посадочным (по умолчанию)
  channels         сессии и конверсии по каналам
  countries        органика по странам
Или свои --dimensions / --metrics (имена GA4 API).

Примеры:
  ./scripts/ga4-query.py --days 28 --out data/ga4-organic-landing-2026-09-28.json
  ./scripts/ga4-query.py --preset channels --days 28
"""
import argparse, datetime as dt, json, os, sys, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, google_token, load_env  # noqa: E402

ORGANIC = {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}}
PRESETS = {
    "organic-landing": (["landingPagePlusQueryString"], ["sessions", "engagedSessions", "engagementRate",
                                                         "keyEvents", "totalUsers"], ORGANIC),
    "channels": (["sessionDefaultChannelGroup"], ["sessions", "engagedSessions", "keyEvents", "totalUsers"], None),
    "countries": (["country"], ["sessions", "engagedSessions", "keyEvents"], ORGANIC),
}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--preset", choices=PRESETS, default="organic-landing")
    p.add_argument("--dimensions"); p.add_argument("--metrics")
    p.add_argument("--days", type=int, default=28, help="окно до вчера")
    p.add_argument("--start"); p.add_argument("--end")
    p.add_argument("--limit", type=int, default=10000)
    p.add_argument("--out")
    a = p.parse_args()

    env = load_env(a.env)
    prop, sa = env.get("GA4_PROPERTY_ID"), env.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not prop or not sa:
        sys.exit("GA4_PROPERTY_ID / GOOGLE_APPLICATION_CREDENTIALS не заданы в .env")

    dims, mets, flt = PRESETS[a.preset]
    if a.dimensions:
        dims, flt = a.dimensions.split(","), None
    if a.metrics:
        mets = a.metrics.split(",")
    end = a.end or (dt.date.today() - dt.timedelta(days=1)).isoformat()
    start = a.start or (dt.date.fromisoformat(end) - dt.timedelta(days=a.days - 1)).isoformat()

    body = {"dateRanges": [{"startDate": start, "endDate": end}],
            "dimensions": [{"name": d} for d in dims], "metrics": [{"name": m} for m in mets],
            "orderBys": [{"metric": {"metricName": mets[0]}, "desc": True}], "limit": a.limit}
    if flt:
        body["dimensionFilter"] = flt
    token = google_token(sa, ["https://www.googleapis.com/auth/analytics.readonly"])
    req = urllib.request.Request(f"https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport",
                                 data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"GA4 API error {e.code}: {e.read().decode(errors='replace')[:300]}")

    rows = []
    for r in d.get("rows", []):
        row = {k: v["value"] for k, v in zip(dims, r["dimensionValues"])}
        for m, v in zip(mets, r["metricValues"]):
            row[m] = float(v["value"]) if "." in v["value"] else int(v["value"])
        rows.append(row)
    out = {"meta": {"property": prop, "start": start, "end": end, "preset": a.preset if not a.dimensions else None,
                    "dimensions": dims, "metrics": mets, "filter": flt, "rows": len(rows),
                    "row_count_total": d.get("rowCount"), "pulled_at": dt.datetime.now().isoformat(timespec="seconds")},
           "rows": rows}
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        json.dump(out, open(a.out, "w"), indent=1, ensure_ascii=False)
    tot = {m: sum(r[m] for r in rows) for m in mets if isinstance(rows[0][m] if rows else 0, int)}
    print(f"GA4 {prop} {start}..{end} {','.join(dims)} rows={len(rows)} "
          + " ".join(f"{k}={v}" for k, v in tot.items()) + (f" -> {a.out}" if a.out else ""))


if __name__ == "__main__":
    main()
