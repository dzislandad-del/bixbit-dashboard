#!/usr/bin/env python3
"""index-check.py — ежедневная проверка индексации ключевых URL (read-only).

1. GSC URL Inspection API: verdict, coverageState, indexingState, robots, lastCrawlTime,
   pageFetchState, googleCanonical vs userCanonical (квота 2000 URL/день на ресурс).
2. Проверка на malware/phishing/unwanted software:
   - Google Web Risk API (uris.search) — ключ WEB_RISK_API_KEY. Для коммерческого использования
     это правильный API; бесплатно до 100 000 запросов/мес (нам нужно ~30/день).
   - запасной вариант: Safe Browsing v4 — только если явно задан SAFE_BROWSING_API_KEY;
     по условиям Google только для некоммерческого использования и помечен deprecated.
3. Diff с прошлым запуском: изменения verdict/coverage/canonical → алерты.

Примеры:
  ./scripts/index-check.py --out data/index-check/index-2026-09-28.json
  ./scripts/index-check.py --urls https://bixbit.io/en/ams --out /tmp/i.json
Список URL по умолчанию — data/tracked-pages.txt (только HTML).
"""
import argparse, datetime as dt, glob, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, ROOT, google_token, load_env  # noqa: E402

INSPECT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
SAFE = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
WATCH = ["verdict", "coverage_state", "indexing_state", "robots_txt_state", "page_fetch_state", "google_canonical"]


def post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            return 200, json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode(errors="replace"))
        except Exception:
            return e.code, {}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--list", default=os.path.join(ROOT, "data/tracked-pages.txt"))
    p.add_argument("--urls", help="через запятую; переопределяет --list")
    p.add_argument("--out", required=True)
    p.add_argument("--compare", default="latest")
    a = p.parse_args()

    env = load_env(a.env)
    site = env.get("GSC_SITE_URL")
    urls = [u.strip() for u in a.urls.split(",")] if a.urls else \
        [l.strip() for l in open(a.list) if l.strip() and not l.startswith("#")]
    urls = [u for u in urls if not re.search(r"\.(txt|xml)$", u)]

    token = google_token(env["GOOGLE_APPLICATION_CREDENTIALS"], ["https://www.googleapis.com/auth/webmasters.readonly"])
    rows = []
    for u in urls:
        code, d = post(INSPECT, {"inspectionUrl": u, "siteUrl": site, "languageCode": "en-US"},
                       {"Authorization": f"Bearer {token}"})
        if code != 200:
            rows.append({"url": u, "error": f"{code}: {(d.get('error') or {}).get('message', '')[:160]}"})
            print(f"  ERR {code} {u}")
            continue
        r = d.get("inspectionResult", {})
        ix = r.get("indexStatusResult", {})
        row = {"url": u, "verdict": ix.get("verdict"), "coverage_state": ix.get("coverageState"),
               "indexing_state": ix.get("indexingState"), "robots_txt_state": ix.get("robotsTxtState"),
               "page_fetch_state": ix.get("pageFetchState"), "last_crawl": ix.get("lastCrawlTime"),
               "crawled_as": ix.get("crawledAs"), "google_canonical": ix.get("googleCanonical"),
               "user_canonical": ix.get("userCanonical"),
               "canonical_mismatch": bool(ix.get("googleCanonical") and ix.get("userCanonical")
                                          and ix["googleCanonical"] != ix["userCanonical"]),
               "rich_results": (r.get("richResultsResult") or {}).get("verdict"),
               "rich_results_issues": [i.get("richResultType") for i in (r.get("richResultsResult") or {}).get("detectedItems", [])
                                       if any(it.get("issues") for it in i.get("items", []))],
               "inspection_link": r.get("inspectionResultLink")}
        rows.append(row)
        flag = " CANONICAL≠" if row["canonical_mismatch"] else ""
        print(f"  {row['verdict'] or '?':8} {(row['coverage_state'] or '')[:42]:42} {(row['last_crawl'] or '')[:10]} "
              f"{u.replace('https://bixbit.io', '')}{flag}")
        time.sleep(0.15)  # квота 600/мин

    # Web Risk (предпочтительно) или Safe Browsing v4 (запасной) — сайт целиком + ключевые URL
    check_urls = ["https://bixbit.io/"] + urls
    safe = {"checked": False}
    wr_key = env.get("WEB_RISK_API_KEY")
    sb_key = env.get("SAFE_BROWSING_API_KEY")  # только явный ключ: v4 — некоммерческий API, по умолчанию не используем
    if wr_key:
        matches, err = [], None
        for u in check_urls:
            q = urllib.parse.urlencode([("threatTypes", t) for t in ("MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE")]
                                       + [("uri", u), ("key", wr_key)])
            try:
                with urllib.request.urlopen(f"https://webrisk.googleapis.com/v1/uris:search?{q}", timeout=30, context=CTX) as r:
                    d = json.load(r)
                if d.get("threat"):
                    matches.append({"url": u, "threat": d["threat"]})
            except urllib.error.HTTPError as e:
                try:
                    j = json.loads(e.read().decode(errors="replace")).get("error", {})
                    reason = next((x.get("reason") for x in j.get("details", []) if x.get("reason")), j.get("status"))
                    err = f"{e.code} {reason}: {j.get('message', '')[:140]}"
                except Exception:
                    err = f"HTTP {e.code}"
                break
        safe = {"checked": err is None, "api": "web_risk", "urls": len(check_urls), "matches": matches}
        if err:
            safe["error"] = err
    elif sb_key:
        body = {"client": {"clientId": "bixbit-seo", "clientVersion": "1.0"},
                "threatInfo": {"threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
                               "platformTypes": ["ANY_PLATFORM"], "threatEntryTypes": ["URL"],
                               "threatEntries": [{"url": u} for u in check_urls[:400]]}}
        code, d = post(f"{SAFE}?key={sb_key}", body, {})
        if code == 200:
            safe = {"checked": True, "api": "safe_browsing_v4", "matches": d.get("matches", [])}
        else:
            reason = next((x.get("reason") for x in (d.get("error") or {}).get("details", []) if x.get("reason")), "")
            safe = {"checked": False, "api": "safe_browsing_v4", "error": f"{code} {reason}: {(d.get('error') or {}).get('message', '')[:140]}"}
    print(f"Угрозы ({safe.get('api', 'нет ключа')}): " + ("OK, не найдено" if safe.get("checked") and not safe.get("matches")
          else f"НАЙДЕНО {len(safe['matches'])}" if safe.get("matches") else ("не проверялось: " + safe["error"]) if safe.get("error") else "не проверялось (нет WEB_RISK_API_KEY; замена — уведомления GSC)"))

    prev_path = None
    if a.compare == "latest":
        prev = [f for f in sorted(glob.glob(os.path.join(ROOT, "data/index-check/index-*.json")))
                if os.path.abspath(f) != os.path.abspath(a.out)]
        prev_path = prev[-1] if prev else None
    elif a.compare != "none":
        prev_path = a.compare
    changes = []
    if prev_path:
        pb = {r["url"]: r for r in json.load(open(prev_path))["urls"]}
        for r in rows:
            o = pb.get(r["url"])
            if o:
                for f in WATCH:
                    if o.get(f) != r.get(f):
                        changes.append({"url": r["url"], "field": f, "was": o.get(f), "now": r.get(f)})
    alerts = [r for r in rows if r.get("verdict") not in ("PASS", None) or r.get("canonical_mismatch") or r.get("error")]
    doc = {"meta": {"checked_at": dt.datetime.now().isoformat(timespec="seconds"), "site": site, "urls": len(rows),
                    "compared_to": os.path.relpath(prev_path, ROOT) if prev_path else None},
           "summary": {"pass": sum(r.get("verdict") == "PASS" for r in rows), "not_pass": len(alerts),
                       "canonical_mismatch": sum(bool(r.get("canonical_mismatch")) for r in rows),
                       "safe_browsing_matches": len(safe.get("matches", [])) if safe.get("checked") else None},
           "safe_browsing": safe, "changes": changes, "urls": rows}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(doc, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"PASS {doc['summary']['pass']}/{len(rows)} · проблем {len(alerts)} · canonical≠ {doc['summary']['canonical_mismatch']}"
          f" · изменений {len(changes)} -> {os.path.relpath(os.path.abspath(a.out), ROOT)}")
    for c in changes:
        print(f"   Δ {c['url'].replace('https://bixbit.io', '')} {c['field']}: {c['was']} → {c['now']}")


if __name__ == "__main__":
    main()
