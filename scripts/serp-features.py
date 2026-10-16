#!/usr/bin/env python3
"""serp-features.py — еженедельный съём AI Overview / Featured Snippet / PAA (DataForSEO).

По ключам из rank-tracking baseline (или --keywords) делает live/advanced SERP (depth 10,
load_async_ai_overview=true) и записывает:
  - есть ли AI Overview, цитируется ли в нём bixbit.io, какие домены цитируются;
  - кто держит Featured Snippet (и не мы ли);
  - есть ли People Also Ask, есть ли мы в раскрытых ответах;
  - органическая позиция bixbit.io в топ-10.
Diff с прошлым съёмом: потеря/получение цитаты в AIO и сниппета.
Стоимость печатается из ответа API.

Примеры:
  ./scripts/serp-features.py --dry-run
  ./scripts/serp-features.py --out data/serp-features/serp-features-2026-09-28.json
  ./scripts/serp-features.py --keywords "antminer firmware,immersion cooling" --out /tmp/sf.json
"""
import argparse, base64, datetime as dt, glob, json, os, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, ROOT, load_env  # noqa: E402

ENDPOINT = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"
OWN = ("bixbit.io",)  # bixbitusa.io — партнёры, не учитываем
COMPETITORS = ("braiins", "vnish", "vni.sh", "epicblockchain", "emcd", "hiveon", "awesomeminer", "minerstat",
               "luxor", "liquidstack", "engineeredfluids", "submer", "d-central")


def own(domain):
    d = (domain or "").lower()
    return d in OWN or d.endswith(".bixbit.io")


def domains_in(node, out):
    """Все (domain, url) внутри элемента (references, links, expanded_element…)."""
    if isinstance(node, list):
        for n in node:
            domains_in(n, out)
    elif isinstance(node, dict):
        if node.get("domain"):
            out.append((node["domain"].lower(), node.get("url")))
        for v in node.values():
            if isinstance(v, (dict, list)):
                domains_in(v, out)
    return out


def fetch(auth, kw, location, lang):
    body = json.dumps([{"keyword": kw, "location_name": location, "language_code": lang, "depth": 10,
                        "load_async_ai_overview": True, "people_also_ask_click_depth": 1}]).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120, context=CTX) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        return {"status_code": e.code, "items": [], "cost": 0, "item_types": []}
    except urllib.error.URLError as e:
        return {"status_code": 0, "items": [], "cost": 0, "item_types": [], "error": str(e.reason)}
    t = (d.get("tasks") or [{}])[0]
    res = (t.get("result") or [{}])[0] or {}
    return {"status_code": t.get("status_code"), "items": res.get("items") or [], "cost": t.get("cost") or 0,
            "item_types": res.get("item_types") or []}


def parse(kw, resp):
    items = resp["items"]
    aio = [i for i in items if i.get("type") == "ai_overview"]
    fs = [i for i in items if i.get("type") == "featured_snippet"]
    paa = [i for i in items if i.get("type") == "people_also_ask"]
    org = [i for i in items if i.get("type") == "organic"]
    aio_domains = sorted({d for d, _ in domains_in(aio, [])})
    paa_domains = sorted({d for d, _ in domains_in(paa, [])})
    own_org = [i for i in org if own(i.get("domain"))]
    return {
        "keyword": kw, "api_status": resp["status_code"], "item_types": resp["item_types"],
        "ai_overview": bool(aio), "aio_cites_bixbit": any(own(d) for d in aio_domains),
        "aio_cited_urls_bixbit": sorted({u for d, u in domains_in(aio, []) if own(d) and u}),
        "aio_domains": aio_domains[:30],
        "aio_competitors": [d for d in aio_domains if any(c in d for c in COMPETITORS)],
        "featured_snippet": bool(fs), "fs_domain": fs[0].get("domain") if fs else None, "fs_url": fs[0].get("url") if fs else None,
        "fs_is_bixbit": bool(fs and own(fs[0].get("domain"))),
        "paa": bool(paa), "paa_has_bixbit": any(own(d) for d in paa_domains),
        "organic_position": own_org[0]["rank_group"] if own_org else None,
        "organic_url": own_org[0]["url"] if own_org else None,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--baseline", default=(sorted(glob.glob(os.path.join(ROOT, "data/rank-tracking/baseline-*.json"))) or [None])[-1])
    p.add_argument("--keywords")
    p.add_argument("--location", default="United States")
    p.add_argument("--language", default="en")
    p.add_argument("--out")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    kws = [k.strip() for k in a.keywords.split(",")] if a.keywords else \
        [k["keyword"] for k in json.load(open(a.baseline))["keywords"]]
    print(f"{len(kws)} ключей · {a.location}/{a.language} · advanced depth 10 + AIO")
    if a.dry_run:
        print(f"Ожидаемая стоимость ≈ ${len(kws) * 0.004:.2f}–{len(kws) * 0.006:.2f} (SERP + доплата за AIO только где он есть)")
        return
    if not a.out:
        sys.exit("укажи --out или --dry-run")
    env = load_env(a.env)
    auth = base64.b64encode(f"{env['DATAFORSEO_LOGIN']}:{env['DATAFORSEO_PASSWORD']}".encode()).decode()

    rows, cost = [], 0.0
    for kw in kws:
        resp = fetch(auth, kw, a.location, a.language)
        if resp["status_code"] in (40101, 40106, 0):
            time.sleep(1); resp = fetch(auth, kw, a.location, a.language)
        cost += float(resp["cost"] or 0)
        r = parse(kw, resp)
        rows.append(r)
        print(f"  {kw:45} AIO={'Y' if r['ai_overview'] else '-'}{'★' if r['aio_cites_bixbit'] else ' '} "
              f"FS={(r['fs_domain'] or '-')[:22]:22}{'★' if r['fs_is_bixbit'] else ' '} PAA={'Y' if r['paa'] else '-'}"
              f"{'★' if r['paa_has_bixbit'] else ' '} org={r['organic_position'] or '—'}")

    prev = [f for f in sorted(glob.glob(os.path.join(ROOT, "data/serp-features/serp-features-*.json")))
            if os.path.abspath(f) != os.path.abspath(a.out)]
    changes = []
    if prev:
        pb = {r["keyword"]: r for r in json.load(open(prev[-1]))["keywords"]}
        for r in rows:
            o = pb.get(r["keyword"])
            if o:
                for f in ("ai_overview", "aio_cites_bixbit", "fs_is_bixbit", "fs_domain", "paa_has_bixbit"):
                    if o.get(f) != r.get(f):
                        changes.append({"keyword": r["keyword"], "field": f, "was": o.get(f), "now": r.get(f)})
    summ = {"keywords": len(rows), "with_aio": sum(r["ai_overview"] for r in rows),
            "aio_cites_bixbit": sum(r["aio_cites_bixbit"] for r in rows),
            "with_featured_snippet": sum(r["featured_snippet"] for r in rows), "fs_bixbit": sum(r["fs_is_bixbit"] for r in rows),
            "with_paa": sum(r["paa"] for r in rows), "paa_bixbit": sum(r["paa_has_bixbit"] for r in rows),
            "top_aio_domains": sorted({d for r in rows for d in r["aio_domains"]},
                                      key=lambda d: -sum(d in r["aio_domains"] for r in rows))[:15],
            "cost_usd": round(cost, 4)}
    doc = {"meta": {"collected_on": dt.date.today().isoformat(), "location": a.location, "language": a.language,
                    "compared_to": os.path.relpath(prev[-1], ROOT) if prev else None}, "summary": summ,
           "changes": changes, "keywords": rows}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(doc, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"\nAIO {summ['with_aio']}/{len(rows)} (цитирует нас: {summ['aio_cites_bixbit']}) · FS {summ['with_featured_snippet']} (наш: {summ['fs_bixbit']})"
          f" · PAA {summ['with_paa']} (мы: {summ['paa_bixbit']}) · изменений {len(changes)} · ${cost:.4f}")


if __name__ == "__main__":
    main()
