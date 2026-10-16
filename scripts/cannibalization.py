#!/usr/bin/env python3
"""cannibalization.py — еженедельный отчёт «запрос → несколько страниц» по GSC.

Берёт выгрузку GSC query+page (или сам снимает её через gsc-query.py) и находит
запросы, по которым показы делят ≥ 2 страницы. Классы:
  - same_locale  — 2+ страницы одной локали (en/en): настоящая каннибализация;
  - cross_locale — страницы разных локалей (en/ru/es) на один запрос: сигнал проблем hreflang;
  - brand        — брендовые запросы (bixbit…): несколько страниц — норма (sitelinks), не алерт;
  - #якоря и ?параметры склеиваются с основным URL.
Сравнение с прошлым отчётом: новые и исчезнувшие конфликты.

Примеры:
  ./scripts/cannibalization.py --out data/cannibalization/cannibal-2026-09-28.json
  ./scripts/cannibalization.py --input data/gsc-queries-pages-us-2026-09-28.json --out /tmp/c.json
"""
import argparse, collections, csv, datetime as dt, glob, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import ROOT  # noqa: E402


BRAND = re.compile(r"bix\s?bit|биксбит|bixbite|bitbix|bixbix", re.I)


def loc(u):
    m = re.match(r"https?://[^/]+/(en|ru|es)(/|$)", u)
    return m.group(1) if m else "-"


def clean(u):
    return re.sub(r"[#?].*$", "", u)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", help="готовая выгрузка gsc-query.py (dims query,page); иначе снимем за --days")
    p.add_argument("--days", type=int, default=28)
    p.add_argument("--country", help="ISO alpha-3 (напр. usa); по умолчанию все страны")
    p.add_argument("--min-impressions", type=int, default=20, help="минимум показов у запроса")
    p.add_argument("--min-share", type=float, default=0.10, help="доля показов, чтобы страница считалась конкурентом")
    p.add_argument("--out", required=True)
    a = p.parse_args()

    src = a.input
    if not src:
        src = os.path.join(ROOT, f"data/gsc-queries-pages-{a.country or 'all'}-{dt.date.today().isoformat()}.json")
        cmd = [os.path.join(ROOT, "scripts/gsc-query.py"), "--days", str(a.days), "--dimensions", "query,page", "--out", src]
        if a.country:
            cmd += ["--country", a.country]
        subprocess.run(cmd, check=True)
    data = json.load(open(src))
    rows = data["rows"]

    by_q = collections.defaultdict(lambda: collections.defaultdict(lambda: {"impressions": 0, "clicks": 0, "pos_w": 0.0}))
    for r in rows:
        pg = by_q[r["query"]][clean(r["page"])]
        pg["impressions"] += r["impressions"]; pg["clicks"] += r["clicks"]; pg["pos_w"] += r["position"] * r["impressions"]

    conflicts = []
    for q, pages in by_q.items():
        tot = sum(v["impressions"] for v in pages.values())
        if tot < a.min_impressions:
            continue
        comp = [(u, v) for u, v in pages.items() if v["impressions"] / tot >= a.min_share]
        if len(comp) < 2:
            continue
        locs = {loc(u) for u, _ in comp}
        kind = "brand" if BRAND.search(q) else ("cross_locale" if len(locs) > 1 else "same_locale")
        comp.sort(key=lambda x: -x[1]["impressions"])
        conflicts.append({
            "query": q, "kind": kind, "impressions": tot, "clicks": sum(v["clicks"] for v in pages.values()),
            "pages": [{"page": u, "locale": loc(u), "impressions": v["impressions"], "clicks": v["clicks"],
                       "share": round(v["impressions"] / tot, 2), "position": round(v["pos_w"] / max(v["impressions"], 1), 1)}
                      for u, v in comp]})
    conflicts.sort(key=lambda c: -c["impressions"])

    # страница ↔ страница: какие пары конфликтуют чаще всего
    pairs = collections.Counter()
    for c in conflicts:
        if c["kind"] == "same_locale":
            ps = [x["page"] for x in c["pages"][:2]]
            pairs[tuple(sorted(ps))] += c["impressions"]

    prev = [f for f in sorted(glob.glob(os.path.join(ROOT, "data/cannibalization/cannibal-*.json")))
            if os.path.abspath(f) != os.path.abspath(a.out)]
    new, gone = [], []
    if prev:
        old = {c["query"] for c in json.load(open(prev[-1]))["conflicts"]}
        cur = {c["query"] for c in conflicts}
        new, gone = sorted(cur - old), sorted(old - cur)

    doc = {"meta": {"source": os.path.relpath(src, ROOT), "window": f"{data['meta']['start']}..{data['meta']['end']}",
                    "country": a.country or "all", "min_impressions": a.min_impressions, "min_share": a.min_share,
                    "compared_to": os.path.relpath(prev[-1], ROOT) if prev else None,
                    "note": "GSC query-разрез не включает анонимизированные запросы"},
           "summary": {"queries_checked": sum(1 for q in by_q if sum(v["impressions"] for v in by_q[q].values()) >= a.min_impressions),
                       "same_locale": sum(c["kind"] == "same_locale" for c in conflicts),
                       "cross_locale": sum(c["kind"] == "cross_locale" for c in conflicts),
                       "brand": sum(c["kind"] == "brand" for c in conflicts),
                       "new": len(new), "resolved": len(gone)},
           "top_page_pairs": [{"pages": list(k), "impressions": v} for k, v in pairs.most_common(25)],
           "new_conflicts": new, "resolved_conflicts": gone, "conflicts": conflicts}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(doc, open(a.out, "w"), indent=1, ensure_ascii=False)
    with open(os.path.splitext(a.out)[0] + ".csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["query", "kind", "impressions", "clicks", "page", "locale", "page_impr", "share", "position"])
        for c in conflicts:
            for x in c["pages"]:
                w.writerow([c["query"], c["kind"], c["impressions"], c["clicks"], x["page"], x["locale"], x["impressions"], x["share"], x["position"]])
    s = doc["summary"]
    print(f"{s['queries_checked']} запросов ≥{a.min_impressions} показов · same_locale {s['same_locale']} · cross_locale {s['cross_locale']}"
          f" · новых {s['new']} · ушло {s['resolved']} -> {os.path.relpath(os.path.abspath(a.out), ROOT)}")
    for c in [c for c in conflicts if c["kind"] == "same_locale"][:12]:
        print(f"  [{c['impressions']:>5}] {c['query'][:50]:50} " + " | ".join(
            f"{x['page'].replace('https://bixbit.io', '')} {int(x['share'] * 100)}% p{x['position']}" for x in c["pages"][:3]))


if __name__ == "__main__":
    main()
