#!/usr/bin/env python3
"""sitemap-monitor.py — новые/удалённые страницы и соответствие sitemap ↔ Google Search Console.

1. Скачивает sitemap (индекс и все вложенные файлы): URL + lastmod.
2. Сравнивает с прошлым снимком data/sitemap/sitemap-*.json → новые, удалённые URL, изменённый lastmod.
3. GSC Sitemaps API: что Google знает о каждом файле sitemap (когда скачан, ошибки, предупреждения, отправлено URL).
4. GSC Search Analytics (страницы, N дней): какие URL из sitemap не получают ни одного показа,
   какие страницы с показами отсутствуют в sitemap.
5. URL Inspection для новых URL (до --inspect шт.): попали ли они в индекс.

Примеры:
  ./scripts/sitemap-monitor.py --out data/sitemap/sitemap-2026-10-16.json
  ./scripts/sitemap-monitor.py --out data/sitemap/sitemap-2026-10-16.json --inspect 0 --days 28
"""
import argparse, datetime as dt, glob, json, os, re, sys, time
import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, ROOT, google_token, load_env  # noqa: E402

UA = "Mozilla/5.0 (compatible; BiXBiT-SEO-sitemap/1.0; +https://bixbit.io)"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
INSPECT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return r.read()


def api(url, token, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            return 200, json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode(errors="replace"))
        except Exception:
            return e.code, {}


def norm(u):
    """Нормализация для сравнения: https, без www, без завершающего / (кроме корня), без #."""
    u = u.strip().split("#")[0]
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"^https://www\.", "https://", u)
    if u.count("/") > 3 and u.endswith("/"):
        u = u[:-1]
    return u


def fetch_sitemap(root):
    urls, files, errors, seen = {}, [], [], set()
    queue = [root]
    while queue:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        try:
            tree = ET.fromstring(get(sm).strip())
        except Exception as e:
            errors.append({"sitemap": sm, "error": f"{type(e).__name__}: {e}"[:200]})
            continue
        if tree.tag == NS + "sitemapindex":
            for s in tree.findall(NS + "sitemap"):
                loc = (s.findtext(NS + "loc") or "").strip()
                if loc:
                    queue.append(loc)
            continue
        n = 0
        for u in tree.findall(NS + "url"):
            loc = (u.findtext(NS + "loc") or "").strip()
            if loc:
                urls[norm(loc)] = {"loc": loc, "lastmod": (u.findtext(NS + "lastmod") or "").strip() or None, "sitemap": sm}
                n += 1
        files.append({"sitemap": sm, "urls": n})
    return urls, files, errors


def section(u):
    p = urllib.parse.urlparse(u).path.strip("/").split("/")
    return "/".join(p[:2]) if p and p[0] else "/"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--sitemap", default="https://bixbit.io/sitemap.xml")
    p.add_argument("--days", type=int, default=28, help="окно GSC для поиска страниц без показов")
    p.add_argument("--inspect", type=int, default=20, help="сколько новых URL проверить через URL Inspection (0 — не проверять)")
    p.add_argument("--compare", default="latest", help="прошлый снимок ('latest' — последний в data/sitemap/, 'none')")
    p.add_argument("--out", required=True)
    a = p.parse_args()

    urls, files, errors = fetch_sitemap(a.sitemap)
    print(f"sitemap: файлов {len(files)}, URL {len(urls)}" + (f", ошибок {len(errors)}" if errors else ""))

    prev_path = None
    if a.compare == "latest":
        cands = sorted(f for f in glob.glob(os.path.join(ROOT, "data/sitemap/sitemap-????-??-??.json"))
                       if os.path.abspath(f) != os.path.abspath(a.out))
        prev_path = cands[-1] if cands else None
    elif a.compare != "none":
        prev_path = a.compare
    prev = json.load(open(prev_path)) if prev_path else None
    new_urls, removed, lastmod_changed = [], [], []
    if prev:
        pu = {x["url"]: x for x in prev.get("urls", [])}
        new_urls = sorted(u for u in urls if u not in pu)
        removed = sorted(u for u in pu if u not in urls)
        lastmod_changed = sorted(u for u in urls if u in pu and urls[u]["lastmod"] != pu[u].get("lastmod"))
        print(f"с {prev['meta']['taken_at'][:10]}: новых {len(new_urls)}, удалено {len(removed)}, изменён lastmod {len(lastmod_changed)}")

    env = load_env(a.env)
    site = env.get("GSC_SITE_URL")
    gsc = {"checked": False}
    inspected = []
    if site and env.get("GOOGLE_APPLICATION_CREDENTIALS"):
        token = google_token(env["GOOGLE_APPLICATION_CREDENTIALS"], ["https://www.googleapis.com/auth/webmasters.readonly"])
        enc = urllib.parse.quote(site, safe="")
        code, d = api(f"https://www.googleapis.com/webmasters/v3/sites/{enc}/sitemaps", token)
        sm_gsc = []
        if code == 200:
            for s in d.get("sitemap", []):
                c = {x.get("type"): x for x in s.get("contents", [])}.get("web", {})
                sm_gsc.append({"path": s.get("path"), "last_submitted": s.get("lastSubmitted"), "last_downloaded": s.get("lastDownloaded"),
                               "is_pending": s.get("isPending"), "errors": int(s.get("errors") or 0), "warnings": int(s.get("warnings") or 0),
                               "submitted": int(c.get("submitted") or 0)})
        end = dt.date.today() - dt.timedelta(days=3)
        start = end - dt.timedelta(days=a.days - 1)
        code2, d2 = api(f"https://www.googleapis.com/webmasters/v3/sites/{enc}/searchAnalytics/query", token,
                        {"startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": ["page"], "rowLimit": 25000, "type": "web"})
        pages = {}
        if code2 == 200:
            for r in d2.get("rows", []):
                pages[norm(r["keys"][0])] = {"clicks": r["clicks"], "impressions": r["impressions"]}
        no_impr = sorted(u for u in urls if u not in pages)
        not_in_sm = sorted(((u, v) for u, v in pages.items() if u not in urls and "?" not in u), key=lambda x: -x[1]["impressions"])
        by_sec = {}
        for u in no_impr:
            by_sec[section(u)] = by_sec.get(section(u), 0) + 1
        gsc = {"checked": code2 == 200, "window": f"{start}..{end}", "sitemaps": sm_gsc, "sitemaps_api": code,
               "pages_with_impressions": len(pages),
               "sitemap_without_impressions": len(no_impr),
               "sitemap_without_impressions_by_section": dict(sorted(by_sec.items(), key=lambda x: -x[1])),
               "sitemap_without_impressions_sample": no_impr[:300],
               "gsc_not_in_sitemap": len(not_in_sm),
               "gsc_not_in_sitemap_top": [{"url": u, **v} for u, v in not_in_sm[:100]]}
        print(f"GSC {start}..{end}: страниц с показами {len(pages)}; из sitemap без показов {len(no_impr)}; "
              f"с показами, но вне sitemap {len(not_in_sm)}")
        for s in sm_gsc:
            print(f"  GSC sitemap {s['path'].replace('https://bixbit.io', '')}: скачан {(s['last_downloaded'] or '—')[:10]}, "
                  f"URL {s['submitted']}, ошибок {s['errors']}, предупреждений {s['warnings']}")
        for u in new_urls[:a.inspect]:
            c, r = api(INSPECT, token, {"inspectionUrl": urls[u]["loc"], "siteUrl": site, "languageCode": "en-US"})
            ix = (r.get("inspectionResult") or {}).get("indexStatusResult", {}) if c == 200 else {}
            inspected.append({"url": u, "verdict": ix.get("verdict") if c == 200 else f"error {c}",
                              "coverage_state": ix.get("coverageState"), "last_crawl": ix.get("lastCrawlTime")})
            print(f"  новая: {ix.get('verdict') or c:8} {(ix.get('coverageState') or '')[:40]:40} {u.replace('https://bixbit.io', '')}")
            time.sleep(0.15)
    else:
        print("GSC: пропущено — нет GSC_SITE_URL / GOOGLE_APPLICATION_CREDENTIALS")

    out = {"meta": {"taken_at": dt.datetime.now().isoformat(timespec="seconds"), "sitemap": a.sitemap,
                    "compared_to": os.path.relpath(prev_path, ROOT) if prev_path else None},
           "summary": {"sitemap_files": len(files), "urls": len(urls), "fetch_errors": len(errors), "new": len(new_urls),
                       "removed": len(removed), "lastmod_changed": len(lastmod_changed),
                       "without_impressions": gsc.get("sitemap_without_impressions"), "gsc_not_in_sitemap": gsc.get("gsc_not_in_sitemap")},
           "files": files, "fetch_errors": errors, "new_urls": new_urls, "removed_urls": removed, "lastmod_changed": lastmod_changed[:500],
           "new_inspected": inspected, "gsc": gsc,
           "urls": [{"url": u, "lastmod": v["lastmod"], "sitemap": v["sitemap"]} for u, v in sorted(urls.items())]}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)
    print(f"-> {os.path.relpath(a.out, ROOT) if os.path.isabs(a.out) else a.out}")


if __name__ == "__main__":
    main()
