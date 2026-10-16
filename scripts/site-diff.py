#!/usr/bin/env python3
"""site-diff.py — что изменилось на всём сайте между двумя краулами (data/crawl-*/pages.json).

Новые и пропавшие страницы, смена кода ответа, title, description, H1, H2, canonical, noindex,
hreflang, попадание в sitemap, разметка JSON-LD, изменение основного текста (без шапки/меню/подвала),
ALT картинок. Текст, H2 и ALT сравниваются, если они есть в обоих краулах (краулер пишет их с 2026-10-16).

Примеры:
  ./scripts/site-diff.py                                   # два последних краула
  ./scripts/site-diff.py --old data/crawl-2026-09-28 --new data/crawl-2026-10-10 --out data/site-diff/site-diff-2026-10-10.json
"""
import argparse, datetime as dt, glob, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import ROOT  # noqa: E402

FIELDS = [("title", "title"), ("description", "description"), ("h1", "H1"), ("canonical", "canonical"),
          ("noindex", "noindex"), ("robots", "meta robots"), ("in_sitemap", "в sitemap"), ("html_lang", "lang")]


def load(d):
    j = json.load(open(os.path.join(d, "pages.json"), encoding="utf-8"))
    return j.get("meta", {}), {p["url"]: p for p in j["pages"]}


def clean(v):
    if isinstance(v, str):
        return " ".join(v.split())
    if isinstance(v, list):
        return [clean(x) for x in v]
    return v


def is_page(p):
    return p and p.get("status") == 200 and "html" in (p.get("content_type") or "") and not p.get("redirect_chain")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--old"); ap.add_argument("--new"); ap.add_argument("--out")
    ap.add_argument("--min-text-change", type=float, default=0.0, help="порог изменения объёма текста (доля), 0 — любое изменение")
    a = ap.parse_args()
    crawls = sorted(d for d in glob.glob(os.path.join(ROOT, "data/crawl-????-??-??")) if os.path.exists(os.path.join(d, "pages.json")))
    new_dir = a.new or (crawls[-1] if crawls else None)
    old_dir = a.old or (crawls[-2] if len(crawls) > 1 else None)
    if not new_dir or not old_dir:
        sys.exit("нужно минимум два краула в data/crawl-YYYY-MM-DD (или --old/--new)")
    m_old, old = load(old_dir)
    m_new, new = load(new_dir)
    o_date, n_date = os.path.basename(old_dir.rstrip("/"))[6:], os.path.basename(new_dir.rstrip("/"))[6:]

    new_pages = sorted(u for u, p in new.items() if is_page(p) and not is_page(old.get(u)))
    gone = sorted(u for u, p in old.items() if is_page(p) and not is_page(new.get(u)))
    status = [{"url": u, "old": old[u].get("status"), "new": new[u].get("status")} for u in sorted(set(old) & set(new))
              if old[u].get("status") != new[u].get("status")]
    both = sorted(u for u in set(old) & set(new) if is_page(old[u]) and is_page(new[u]))

    changes = {k: [] for k, _ in FIELDS}
    changes.update({"text": [], "h2": [], "alt": [], "jsonld": [], "hreflang": []})
    has_text = any("text_hash" in p for p in old.values())
    for u in both:
        po, pn = old[u], new[u]
        for k, _ in FIELDS:
            vo, vn = clean(po.get(k)), clean(pn.get(k))
            if k == "h1":
                vo, vn = (vo or [None])[0], (vn or [None])[0]
            if vo != vn:
                changes[k].append({"url": u, "old": vo, "new": vn})
        if sorted(po.get("jsonld_types") or []) != sorted(pn.get("jsonld_types") or []) or po.get("faqpage_empty") != pn.get("faqpage_empty"):
            changes["jsonld"].append({"url": u, "old": po.get("jsonld_types"), "new": pn.get("jsonld_types"),
                                      "faq_empty_old": po.get("faqpage_empty"), "faq_empty_new": pn.get("faqpage_empty")})
        if len(po.get("hreflang") or []) != len(pn.get("hreflang") or []):
            changes["hreflang"].append({"url": u, "old": len(po.get("hreflang") or []), "new": len(pn.get("hreflang") or [])})
        if "text_hash" in po and "text_hash" in pn and po["text_hash"] != pn["text_hash"]:
            wo, wn = po.get("main_words") or 0, pn.get("main_words") or 0
            share = abs(wn - wo) / wo if wo else 1.0
            if share >= a.min_text_change:
                changes["text"].append({"url": u, "words_old": wo, "words_new": wn, "delta": wn - wo, "share": round(share, 3)})
        if "h2" in po and "h2" in pn and clean(po["h2"]) != clean(pn["h2"]):
            changes["h2"].append({"url": u, "added": [h for h in clean(pn["h2"]) if h not in clean(po["h2"])][:8],
                                  "removed": [h for h in clean(po["h2"]) if h not in clean(pn["h2"])][:8]})
        if "img_alts" in po and "img_alts" in pn:
            ao, an = po["img_alts"], pn["img_alts"]
            changed = [{"img": k, "old": ao[k], "new": an[k]} for k in an if k in ao and ao[k] != an[k]]
            added = [{"img": k, "alt": an[k]} for k in an if k not in ao]
            removed = [{"img": k, "alt": ao[k]} for k in ao if k not in an]
            if changed or added or removed:
                changes["alt"].append({"url": u, "changed": changed[:10], "added": added[:10], "removed": removed[:10]})
        else:
            no = len(po.get("images_no_alt") or []), len(pn.get("images_no_alt") or [])
            if no[0] != no[1]:
                changes["alt"].append({"url": u, "no_alt_old": no[0], "no_alt_new": no[1]})

    # пропавшие: настоящие (4xx/3xx/нет в краулинге) отдельно от сбоев загрузки (код 0) и пагинации/тегов
    def gone_kind(u):
        st = (new.get(u) or {}).get("status")
        if "?page=" in u or "/tags/" in u or "/tag/" in u:
            return "pagination"
        return "fetch_error" if st == 0 else "gone"
    gone_real = [u for u in gone if gone_kind(u) == "gone"]
    summary = {"pages_old": sum(1 for p in old.values() if is_page(p)), "pages_new": sum(1 for p in new.values() if is_page(p)),
               "new_pages": len(new_pages), "gone_pages": len(gone_real), "gone_fetch_errors": sum(1 for u in gone if gone_kind(u) == "fetch_error"),
               "gone_pagination": sum(1 for u in gone if gone_kind(u) == "pagination"), "status_changed": len(status),
               **{f"{k}_changed": len(v) for k, v in changes.items()}, "text_compared": has_text}
    out = {"meta": {"created_at": dt.datetime.now().isoformat(timespec="seconds"), "old": os.path.relpath(old_dir, ROOT),
                    "new": os.path.relpath(new_dir, ROOT), "old_date": o_date, "new_date": n_date},
           "summary": summary, "new_pages": [{"url": u, "title": new[u].get("title"), "in_sitemap": new[u].get("in_sitemap"),
                                              "noindex": new[u].get("noindex"), "inlinks": new[u].get("inlinks")} for u in new_pages],
           "gone_pages": [{"url": u, "title": old[u].get("title"), "now": (new.get(u) or {}).get("status", "нет в краулинге"), "kind": gone_kind(u)}
                          for u in sorted(gone, key=lambda u: ("gone", "fetch_error", "pagination").index(gone_kind(u)))],
           "status_changed": status, "changes": changes}
    path = a.out or os.path.join(ROOT, "data/site-diff", f"site-diff-{n_date}.json")
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=1)
    print(f"краул {o_date} → {n_date}: страниц {summary['pages_old']} → {summary['pages_new']}; "
          f"новых {len(new_pages)}, пропало {len(gone_real)} (+ сбоев загрузки {summary['gone_fetch_errors']}, пагинации/тегов {summary['gone_pagination']}), смена кода {len(status)}")
    print("изменения: " + ", ".join(f"{lbl} {len(changes[k])}" for k, lbl in FIELDS + [("text", "текст"), ("h2", "H2"), ("alt", "ALT"), ("jsonld", "JSON-LD"), ("hreflang", "hreflang")]))
    if not has_text:
        print("текст/H2/ALT по значениям не сравнивались: в старом краулинге их нет (сравнение будет со следующего краула)")
    print(f"-> {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    main()
