#!/usr/bin/env python3
"""page-snapshot.py — снимок SEO-критичных элементов страниц по сырому HTML + diff.

WebFetch не видит <head>/<script>, поэтому drift снимаем здесь: статус, редиректы,
title, meta description, robots (meta + X-Robots-Tag), canonical, hreflang, H1, H2, H3,
ALT картинок, основной текст страницы (без шапки/меню/подвала, по абзацам),
JSON-LD (типы, ошибки парсинга, пустые FAQPage, хэш Organization.description),
вес HTML и время ответа. Diff показывает, какие абзацы текста добавлены/удалены и какие ALT изменились.

Примеры:
  ./scripts/page-snapshot.py --out data/page-snapshot-2026-09-28.json
  ./scripts/page-snapshot.py --out data/page-snapshot-2026-10-05.json --compare data/page-snapshot-2026-09-28.json
  ./scripts/page-snapshot.py --urls https://bixbit.io/en,https://bixbit.io/en/ams
"""
import argparse, datetime as dt, glob, hashlib, json, os, re, sys, time
import urllib.error, urllib.request
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ROOT  # noqa: E402

UA = "Mozilla/5.0 (compatible; BiXBiT-SEO-snapshot/1.0; +https://bixbit.io)"
# Поля, изменение которых — регрессия-кандидат (порядок = важность)
WATCH = ["status", "final_url", "robots", "x_robots_tag", "canonical", "title", "meta_description",
         "h1", "h1_count", "hreflang", "jsonld_types", "jsonld_errors", "faqpage_empty", "org_description_hash"]


BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "dt", "dd", "div", "section", "article",
         "blockquote", "figcaption", "br", "tr", "button", "summary", "label", "main"}


class Head(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.meta, self.links, self.h1, self.jsonld = None, {}, [], [], []
        self._in_title = self._in_h1 = self._in_ld = False
        self._buf = ""
        self.h2, self.h3, self.alts, self.blocks = [], [], {}, []
        self._hx, self._hbuf, self._skip, self._chrome, self._text = None, "", 0, 0, ""

    def _flush(self):
        t = " ".join(self._text.split())
        if len(t) >= 3 and not self._chrome:
            self.blocks.append(t[:1000])
        self._text = ""

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "title" and self.title is None:
            self._in_title, self._buf = True, ""
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key:
                self.meta.setdefault(key, a.get("content", ""))
        elif tag == "link":
            self.links.append(a)
        elif tag == "h1":
            self._in_h1, self._buf = True, ""
        elif tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self._in_ld, self._buf = True, ""
        if tag in ("h2", "h3"):
            self._hx, self._hbuf = tag, ""
        if tag in ("script", "style", "noscript", "template", "svg", "title"):
            self._skip += 1
        elif tag in ("header", "nav", "footer"):
            self._flush(); self._chrome += 1
        elif tag in BLOCK:
            self._flush()
        if tag == "img" and "alt" in a:
            src = (a.get("src") or a.get("data-src") or "").split("?")[0]
            # имя файла без хэша сборки (logo.f275c2433ea3fd12.svg → logo.svg), иначе каждый деплой = «новые» картинки
            key = ("inline" if src.startswith("data:") else re.sub(r"\.[0-9a-f]{8,}(?=\.)", "", src.rsplit("/", 1)[-1]))[:80] or "?"
            if not self._chrome:
                self.alts[key] = (a.get("alt") or "")[:200]

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self.title, self._in_title = " ".join(self._buf.split()), False
        elif tag == "h1" and self._in_h1:
            self.h1.append(" ".join(self._buf.split())); self._in_h1 = False
        elif tag == "script" and self._in_ld:
            self.jsonld.append(self._buf); self._in_ld = False
        if tag == self._hx:
            (self.h2 if tag == "h2" else self.h3).append(" ".join(self._hbuf.split())[:200]); self._hx = None
        if tag in ("script", "style", "noscript", "template", "svg", "title"):
            self._skip = max(0, self._skip - 1)
        elif tag in ("header", "nav", "footer"):
            self._flush(); self._chrome = max(0, self._chrome - 1)
        elif tag in BLOCK:
            self._flush()

    def handle_data(self, data):
        if self._in_title or self._in_h1 or self._in_ld:
            self._buf += data
        if self._hx:
            self._hbuf += data
        if not self._skip and not self._chrome:
            self._text += " " + data


def ld_types(node, out):
    if isinstance(node, list):
        for n in node:
            ld_types(n, out)
    elif isinstance(node, dict):
        t = node.get("@type")
        if t:
            out.extend(t if isinstance(t, list) else [t])
        for k in ("@graph", "mainEntity", "itemListElement"):
            if k in node:
                ld_types(node[k], out)


def find_type(node, name):
    if isinstance(node, list):
        for n in node:
            yield from find_type(n, name)
    elif isinstance(node, dict):
        t = node.get("@type")
        if t == name or (isinstance(t, list) and name in t):
            yield node
        for v in node.values():
            if isinstance(v, (dict, list)):
                yield from find_type(v, name)


def snapshot(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            status, final, headers, body = r.status, r.geturl(), r.headers, r.read()
    except urllib.error.HTTPError as e:
        status, final, headers, body = e.code, e.geturl(), e.headers, e.read()
    except urllib.error.URLError as e:
        return {"url": url, "status": 0, "error": str(e.reason)}
    row = {"url": url, "status": status, "final_url": final if final != url else None,
           "x_robots_tag": headers.get("X-Robots-Tag"), "content_type": headers.get("Content-Type"),
           "html_bytes": len(body), "response_ms": int((time.time() - t0) * 1000)}
    if "html" not in (headers.get("Content-Type") or ""):
        row["sha1"] = hashlib.sha1(body).hexdigest()
        return row
    p = Head()
    p.feed(body.decode("utf-8", errors="replace"))
    p._flush()
    blocks, total = [], 0
    for b in p.blocks:  # уникальные абзацы в порядке появления, до 40 000 символов
        if b not in blocks and total < 40000:
            blocks.append(b); total += len(b)
    canon = [l.get("href") for l in p.links if "canonical" in l.get("rel", "").lower().split()]
    hreflang = sorted(f"{l.get('hreflang')}={l.get('href')}" for l in p.links
                      if "alternate" in l.get("rel", "").lower() and l.get("hreflang"))
    types, errors, faq_empty, org_desc = [], 0, False, None
    for raw in p.jsonld:
        try:
            node = json.loads(raw)
        except json.JSONDecodeError:
            errors += 1
            continue
        ld_types(node, types)
        for faq in find_type(node, "FAQPage"):
            if not faq.get("mainEntity"):
                faq_empty = True
        for org in find_type(node, "Organization"):
            if org.get("description") and org_desc is None:
                org_desc = org["description"]
    row.update({"title": p.title, "title_len": len(p.title or ""),
                "meta_description": p.meta.get("description"), "robots": p.meta.get("robots"),
                "canonical": canon[0] if canon else None, "canonical_count": len(canon),
                "hreflang": hreflang, "h1": p.h1[0] if p.h1 else None, "h1_count": len(p.h1),
                "jsonld_types": sorted(set(types)), "jsonld_blocks": len(p.jsonld), "jsonld_errors": errors,
                "faqpage_empty": faq_empty,
                "org_description_hash": hashlib.sha1(org_desc.encode()).hexdigest()[:10] if org_desc else None,
                "org_description_start": (org_desc or "")[:80] or None,
                "h2": p.h2[:30], "h3": p.h3[:40], "img_alts": dict(list(p.alts.items())[:80]),
                "main_words": sum(len(b.split()) for b in blocks),
                "text_hash": hashlib.sha1("\n".join(blocks).encode()).hexdigest()[:16],
                "text_blocks": blocks})
    return row


def diff(prev, cur):
    pb = {r["url"]: r for r in prev["pages"]}
    changes = []
    for r in cur["pages"]:
        o = pb.get(r["url"])
        if not o:
            changes.append({"url": r["url"], "field": "(new url)", "was": None, "now": r.get("status")})
            continue
        for f in WATCH:
            if o.get(f) != r.get(f):
                changes.append({"url": r["url"], "field": f, "was": o.get(f), "now": r.get(f)})
        if o.get("text_hash") and r.get("text_hash") and o["text_hash"] != r["text_hash"]:
            ob, nb = o.get("text_blocks") or [], r.get("text_blocks") or []
            added, removed = [b for b in nb if b not in ob], [b for b in ob if b not in nb]
            if added or removed:
                changes.append({"url": r["url"], "field": "text", "was": f"{o.get('main_words')} слов", "now": f"{r.get('main_words')} слов",
                                "added": added[:15], "removed": removed[:15]})
        for f in ("h2", "h3"):
            if o.get(f) is not None and r.get(f) is not None and o[f] != r[f]:
                changes.append({"url": r["url"], "field": f, "was": [h for h in o[f] if h not in r[f]][:10],
                                "now": [h for h in r[f] if h not in o[f]][:10]})
        if o.get("img_alts") is not None and r.get("img_alts") is not None and o["img_alts"] != r["img_alts"]:
            ao, an = o["img_alts"], r["img_alts"]
            changes.append({"url": r["url"], "field": "alt",
                            "was": {k: ao[k] for k in ao if an.get(k) != ao[k]}, "now": {k: an[k] for k in an if ao.get(k) != an[k]}})
        if o.get("html_bytes") and r.get("html_bytes") and abs(r["html_bytes"] - o["html_bytes"]) / o["html_bytes"] > 0.3:
            changes.append({"url": r["url"], "field": "html_bytes (>30%)", "was": o["html_bytes"], "now": r["html_bytes"]})
    for u in set(pb) - {r["url"] for r in cur["pages"]}:
        changes.append({"url": u, "field": "(dropped from list)", "was": pb[u].get("status"), "now": None})
    return changes


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--list", default=os.path.join(ROOT, "data/tracked-pages.txt"))
    p.add_argument("--urls", help="через запятую; переопределяет --list")
    p.add_argument("--out", required=True)
    p.add_argument("--compare", default="latest", help="прошлый снимок для diff ('latest' = последний в data/, 'none' = без diff)")
    a = p.parse_args()

    urls = [u.strip() for u in a.urls.split(",")] if a.urls else \
        [l.strip() for l in open(a.list) if l.strip() and not l.startswith("#")]
    prev_path = a.compare
    if prev_path == "latest":
        prev = [f for f in sorted(glob.glob(os.path.join(ROOT, "data/page-snapshot-*.json")))
                if re.fullmatch(r"page-snapshot-\d{4}-\d{2}-\d{2}\.json", os.path.basename(f))
                and os.path.abspath(f) != os.path.abspath(a.out)]
        prev_path = prev[-1] if prev else None
    elif prev_path == "none":
        prev_path = None

    pages = []
    for u in urls:
        r = snapshot(u)
        pages.append(r)
        flags = [f for f, bad in (("NOINDEX", "noindex" in ((r.get("robots") or "") + (r.get("x_robots_tag") or "")).lower()),
                                  ("NO-CANONICAL", r.get("content_type", "").startswith("text/html") and not r.get("canonical")),
                                  ("EMPTY-FAQ", r.get("faqpage_empty")), ("LD-ERR", r.get("jsonld_errors")),
                                  ("H1x" + str(r.get("h1_count")), (r.get("h1_count") or 1) != 1 and r.get("title") is not None)) if bad]
        print(f"  {r['status']:>3} {u.replace('https://bixbit.io', ''):70} {r.get('html_bytes', 0) // 1024:>6} KB  {' '.join(flags)}")
    doc = {"meta": {"taken_at": dt.datetime.now().isoformat(timespec="seconds"), "urls": len(pages), "user_agent": UA},
           "pages": pages}
    if prev_path:
        doc["meta"]["compared_to"] = os.path.relpath(prev_path, ROOT)
        doc["changes"] = diff(json.load(open(prev_path)), doc)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(doc, open(a.out, "w"), indent=1, ensure_ascii=False)
    ch = doc.get("changes")
    print(f"{len(pages)} URL -> {os.path.relpath(os.path.abspath(a.out), ROOT)}"
          + (f" · изменений vs {doc['meta']['compared_to']}: {len(ch)}" if ch is not None else " · без сравнения"))
    for c in (ch or [])[:40]:
        print(f"   Δ {c['url'].replace('https://bixbit.io', '')} {c['field']}: {str(c['was'])[:60]!r} → {str(c['now'])[:60]!r}")


if __name__ == "__main__":
    main()
