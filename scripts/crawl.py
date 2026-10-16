#!/usr/bin/env python3
"""crawl.py — краулер bixbit.io (замена Screaming Frog для регулярных задач).

Обходит сайт с главной и из sitemap, уважает robots.txt, пишет по каждой странице
статус, цепочку редиректов, head-элементы, JSON-LD, изображения/ALT и все ссылки,
затем считает проблемы:
  - 4xx/5xx и битые внутренние ссылки (с источником и анкором);
  - редиректы, цепочки, внутренние ссылки на редиректы (для карты редиректов);
  - noindex, canonical на другой URL, пустые/дубли title/description/H1, длины;
  - изображения без ALT (по локалям);
  - сироты (в sitemap, но без входящих ссылок), индексируемые страницы вне sitemap,
    URL из sitemap с не-200/noindex/чужим canonical;
  - глубина клика и число входящих ссылок (аудит перелинковки), ссылки блог → продвигаемые.

Результат: data/crawl-YYYY-MM-DD/
  pages.json         — страница: все поля
  links.csv.gz       — рёбра: source, target, anchor, nofollow, target_status
  issues/*.csv       — по одному CSV на тип проблемы
  summary.json       — счётчики + топ-проблемы (для отчётов и drift)

Примеры:
  ./scripts/crawl.py                              # весь сайт, до 5000 URL
  ./scripts/crawl.py --max-pages 200 --out /tmp/crawl-test
  ./scripts/crawl.py --check-external             # + статусы внешних ссылок (HEAD)
"""
import argparse, collections, csv, datetime as dt, gzip, json, os, re, sys, threading, time
import urllib.error, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ROOT  # noqa: E402

UA = "Mozilla/5.0 (compatible; BiXBiT-SEO-crawler/1.0; +https://bixbit.io)"
SKIP_EXT = re.compile(r"\.(jpe?g|png|gif|webp|avif|svg|ico|pdf|zip|rar|7z|gz|tar|bin|img|mp4|webm|mp3|woff2?|ttf|eot|css|js|json|xml|txt)$", re.I)
TRACKING = re.compile(r"^(utm_|gclid|gbraid|wbraid|fbclid|yclid|gad_source|_ga|mc_)", re.I)
# Продвигаемые разделы — для отчёта «блог → money pages»
MONEY = ("/firmwares", "/ams", "/asics-cooling", "/products")


# ---------- HTTP ---------------------------------------------------------------

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **kw):
        return None


OPENER = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=CTX))


def fetch(url, method="GET", timeout=45):
    """Один запрос без следования редиректам. -> (status, headers, body, ms, error)"""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.8"})
    t0 = time.time()
    try:
        with OPENER.open(req, timeout=timeout) as r:
            body = r.read() if method == "GET" else b""
            return r.status, r.headers, body, int((time.time() - t0) * 1000), None
    except urllib.error.HTTPError as e:
        body = b""
        if method == "GET" and e.code >= 400:
            try:
                body = e.read()
            except Exception:
                pass
        return e.code, e.headers, body, int((time.time() - t0) * 1000), None
    except Exception as e:  # сеть, таймаут, TLS
        return 0, {}, b"", int((time.time() - t0) * 1000), str(getattr(e, "reason", e))[:200]


def fetch_follow(url, max_hops=10):
    """Следует редиректам вручную, возвращает финальный ответ и цепочку."""
    chain, cur = [], url
    for _ in range(max_hops):
        status, headers, body, ms, err = fetch(cur)
        if status in (301, 302, 303, 307, 308):
            loc = headers.get("Location")
            if not loc:
                break
            nxt = urllib.parse.urljoin(cur, loc)
            chain.append({"url": cur, "status": status, "to": nxt})
            if nxt in [c["url"] for c in chain]:
                return {"status": status, "headers": headers, "body": b"", "ms": ms, "error": "redirect loop", "chain": chain, "final": nxt}
            cur = nxt
            continue
        return {"status": status, "headers": headers, "body": body, "ms": ms, "error": err, "chain": chain, "final": cur}
    return {"status": 0, "headers": {}, "body": b"", "ms": 0, "error": "too many redirects", "chain": chain, "final": cur}


# ---------- HTML ---------------------------------------------------------------

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.meta, self.links, self.h1, self.jsonld = None, {}, [], [], []
        self.anchors, self.images, self.lang = [], [], None
        self._stack, self._buf, self._a = [], "", None
        self.text_len, self._skip = 0, 0

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title" and self.title is None:
            self._stack.append("title"); self._buf = ""
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key:
                self.meta.setdefault(key, a.get("content", ""))
        elif tag == "link":
            self.links.append(a)
        elif tag == "h1":
            self._stack.append("h1"); self._buf = ""
        elif tag == "script":
            self._skip += 1
            if a.get("type", "").lower() == "application/ld+json":
                self._stack.append("ld"); self._buf = ""
        elif tag in ("style", "noscript", "template"):
            self._skip += 1
        elif tag == "a" and "href" in a:
            self._a = {"href": a["href"], "rel": a.get("rel", "").lower(), "text": ""}
        elif tag == "img":
            src = a.get("src") or a.get("data-src") or ""
            if src.startswith("data:"):
                src = src[:30] + "…(inline)"
            self.images.append({"src": src[:300], "alt": a.get("alt"), "has_alt": "alt" in a})

    def handle_endtag(self, tag):
        if tag == "title" and self._stack[-1:] == ["title"]:
            self.title = " ".join(self._buf.split()); self._stack.pop()
        elif tag == "h1" and self._stack[-1:] == ["h1"]:
            self.h1.append(" ".join(self._buf.split())); self._stack.pop()
        elif tag == "script":
            if self._stack[-1:] == ["ld"]:
                self.jsonld.append(self._buf); self._stack.pop()
            self._skip = max(0, self._skip - 1)
        elif tag in ("style", "noscript", "template"):
            self._skip = max(0, self._skip - 1)
        elif tag == "a" and self._a is not None:
            self._a["text"] = " ".join(self._a["text"].split())[:120]
            self.anchors.append(self._a); self._a = None

    def handle_data(self, data):
        if self._stack:
            self._buf += data
        if self._a is not None:
            self._a["text"] += data
        if not self._skip:
            self.text_len += len(data.split())


def ld_info(blocks):
    types, errors, faq_empty = [], 0, False

    def walk(n):
        nonlocal faq_empty
        if isinstance(n, list):
            for i in n:
                walk(i)
        elif isinstance(n, dict):
            t = n.get("@type")
            if t:
                types.extend(t if isinstance(t, list) else [t])
            if (t == "FAQPage" or (isinstance(t, list) and "FAQPage" in t)) and not n.get("mainEntity"):
                faq_empty = True
            for v in n.values():
                if isinstance(v, (dict, list)):
                    walk(v)
    for b in blocks:
        try:
            walk(json.loads(b))
        except json.JSONDecodeError:
            errors += 1
    return sorted(set(types)), errors, faq_empty


# ---------- URL helpers --------------------------------------------------------

def normalize(url):
    p = urllib.parse.urlsplit(url)
    if p.scheme not in ("http", "https"):
        return None
    q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True) if not TRACKING.match(k)]
    path = re.sub(r"/{2,}", "/", p.path or "/")
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower(), path, urllib.parse.urlencode(q), ""))


def locale(url):
    m = re.match(r"https?://[^/]+/(en|ru|es)(/|$)", url)
    return m.group(1) if m else "-"


def sitemap_urls(root):
    urls, seen = [], set()

    def load(u):
        if u in seen:
            return
        seen.add(u)
        r = fetch_follow(u)
        if r["status"] != 200:
            return
        x = r["body"].decode("utf-8", "replace")
        for loc in re.findall(r"<loc>\s*(.*?)\s*</loc>", x, re.S):
            loc = loc.strip()
            if "<sitemapindex" in x:
                load(loc)
            else:
                urls.append(loc)  # список, не set: нужны дубли; не нормализуем: хотим увидеть кривые URL (с пробелом) как есть
    load(root.rstrip("/") + "/sitemap.xml")
    return urls


# ---------- crawl --------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--start", default="https://bixbit.io/")
    p.add_argument("--domains", default="bixbit.io,www.bixbit.io", help="хосты, которые обходим")
    p.add_argument("--max-pages", type=int, default=5000)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--delay", type=float, default=0.25, help="пауза на поток между запросами, с")
    p.add_argument("--check-external", action="store_true", help="HEAD-проверка внешних ссылок")
    p.add_argument("--out", help="папка результата (по умолчанию data/crawl-YYYY-MM-DD)")
    a = p.parse_args()

    today = dt.date.today().isoformat()
    out = a.out or os.path.join(ROOT, f"data/crawl-{today}")
    os.makedirs(os.path.join(out, "issues"), exist_ok=True)
    hosts = {h.strip() for h in a.domains.split(",")}
    start = normalize(a.start)

    rp = urllib.robotparser.RobotFileParser()
    r = fetch_follow(urllib.parse.urljoin(start, "/robots.txt"))
    rp.parse(r["body"].decode("utf-8", "replace").splitlines() if r["status"] == 200 else [])

    sm_raw = sitemap_urls(start)
    sm = {normalize(u) or u for u in sm_raw}
    print(f"robots.txt: {r['status']} · sitemap: {len(sm_raw)} URL · старт {start}", flush=True)

    pages, edges, blocked = {}, [], set()
    depth = {start: 0}
    queue = collections.deque([start] + sorted(u for u in sm if u != start))
    for u in sm:
        depth.setdefault(u, None)  # глубина по ссылкам посчитается позже
    queued = set(queue)
    lock = threading.Lock()

    def work(url):
        time.sleep(a.delay)
        res = fetch_follow(url)
        row = {"url": url, "status": res["status"], "error": res["error"], "ms": res["ms"],
               "redirect_chain": res["chain"], "final_url": res["final"] if res["chain"] else None,
               "locale": locale(url), "in_sitemap": url in sm}
        ctype = (res["headers"].get("Content-Type") or "") if res["headers"] else ""
        row["content_type"] = ctype.split(";")[0]
        row["x_robots_tag"] = res["headers"].get("X-Robots-Tag") if res["headers"] else None
        found = []
        if res["status"] == 200 and "html" in ctype and not res["chain"]:
            body = res["body"]
            row["bytes"] = len(body)
            pg = Page()
            try:
                pg.feed(body.decode("utf-8", "replace"))
            except Exception as e:
                row["parse_error"] = str(e)[:120]
            canon = [l.get("href") for l in pg.links if "canonical" in l.get("rel", "").lower().split()]
            types, ld_err, faq_empty = ld_info(pg.jsonld)
            robots = (pg.meta.get("robots") or "") + " " + (row["x_robots_tag"] or "")
            row.update({
                "title": pg.title, "title_len": len(pg.title or ""),
                "description": pg.meta.get("description"), "description_len": len(pg.meta.get("description") or ""),
                "h1": pg.h1[:3], "h1_count": len(pg.h1), "html_lang": pg.lang,
                "robots": pg.meta.get("robots"), "noindex": "noindex" in robots.lower(),
                "canonical": urllib.parse.urljoin(url, canon[0]) if canon else None, "canonical_count": len(canon),
                "hreflang": sorted(f"{l.get('hreflang')}={l.get('href')}" for l in pg.links
                                   if "alternate" in l.get("rel", "").lower() and l.get("hreflang")),
                "jsonld_types": types, "jsonld_errors": ld_err, "faqpage_empty": faq_empty,
                "words": pg.text_len, "images": len(pg.images),
                "images_no_alt": [i["src"] for i in pg.images if not i["has_alt"]][:50],
                "images_empty_alt": sum(1 for i in pg.images if i["has_alt"] and not (i["alt"] or "").strip()),
            })
            for an in pg.anchors:
                href = an["href"].strip()
                if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                    continue
                tgt = normalize(urllib.parse.urljoin(url, href))
                if tgt:
                    found.append((tgt, an["text"], "nofollow" in an["rel"]))
        return row, found

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {}
        while (queue or futs) and len(pages) < a.max_pages:
            while queue and len(futs) < a.workers * 2 and len(pages) + len(futs) < a.max_pages:
                u = queue.popleft()
                futs[ex.submit(work, u)] = u
            done = next(as_completed(futs))
            u = futs.pop(done)
            row, found = done.result()
            with lock:
                pages[u] = row
                fin = row.get("final_url")
                if fin:  # цель редиректа обходим, но не считаем её входящей ссылкой
                    fin = normalize(fin)
                    if fin and urllib.parse.urlsplit(fin).netloc in hosts and fin not in queued and rp.can_fetch(UA, fin):
                        queued.add(fin); queue.append(fin)
                for tgt, text, nofollow in found:
                    host = urllib.parse.urlsplit(tgt).netloc
                    internal = host in hosts
                    edges.append({"source": u, "target": tgt, "anchor": text, "nofollow": nofollow, "internal": internal})
                    if not internal or tgt in queued:
                        continue
                    if SKIP_EXT.search(urllib.parse.urlsplit(tgt).path):
                        continue
                    if not rp.can_fetch(UA, tgt):
                        blocked.add(tgt); continue
                    queued.add(tgt); queue.append(tgt)
                    if depth.get(u) is not None:
                        depth[tgt] = depth[u] + 1
                    else:
                        depth.setdefault(tgt, None)
                if len(pages) % 100 == 0:
                    print(f"  {len(pages)} стр. · очередь {len(queue)} · {int(time.time() - t0)} с", flush=True)
    truncated = bool(queue)

    # глубина клика — BFS по рёбрам от старта (не зависит от порядка обхода)
    adj = collections.defaultdict(set)
    for e in edges:
        if e["internal"]:
            adj[e["source"]].add(e["target"])
    for u, row in pages.items():  # редирект = переход без клика
        if row.get("final_url"):
            adj[u].add(normalize(row["final_url"]) or row["final_url"])
    depth = {start: 0}
    redirect_to = {u: (normalize(r["final_url"]) or r["final_url"]) for u, r in pages.items() if r.get("final_url")}
    dq = collections.deque([start])
    while dq:  # 0-1 BFS: редирект не добавляет клик
        x = dq.popleft()
        for y in adj.get(x, ()):
            w = 0 if redirect_to.get(x) == y else 1
            if y not in depth or depth[x] + w < depth[y]:
                depth[y] = depth[x] + w
                (dq.appendleft if w == 0 else dq.append)(y)

    # статусы внутренних целей, которых нет в pages (не обошли: robots/лимит/расширение)
    status_of = {u: r["status"] for u, r in pages.items()}
    inlinks = collections.Counter(e["target"] for e in edges if e["internal"] and e["source"] != e["target"])
    inlinks_follow = collections.Counter(e["target"] for e in edges if e["internal"] and not e["nofollow"] and e["source"] != e["target"])

    ext_status = {}
    if a.check_external:
        ext = sorted({e["target"] for e in edges if not e["internal"]})
        print(f"HEAD-проверка {len(ext)} внешних ссылок…", flush=True)

        def head(u):
            s, _, _, _, err = fetch(u, method="HEAD", timeout=20)
            if s in (405, 403, 0):
                s, _, _, _, err = fetch(u, timeout=20)
            return u, s, err
        with ThreadPoolExecutor(max_workers=8) as ex2:
            for u, s, err in ex2.map(head, ext):
                ext_status[u] = s

    for u, row in pages.items():
        row["depth"] = depth.get(u)
        row["inlinks"] = inlinks.get(u, 0)
        row["inlinks_follow"] = inlinks_follow.get(u, 0)
    for e in edges:
        e["target_status"] = status_of.get(e["target"], ext_status.get(e["target"]))

    # ---------- проблемы ----------
    html = [r for r in pages.values() if r.get("title") is not None or r.get("bytes")]
    indexable = [r for r in html if not r.get("noindex") and (not r.get("canonical") or r["canonical"] == r["url"])]
    I = collections.OrderedDict()
    I["error_pages"] = [{"url": r["url"], "status": r["status"], "error": r["error"], "inlinks": r["inlinks"], "in_sitemap": r["in_sitemap"]}
                        for r in pages.values() if r["status"] >= 400 or r["status"] == 0]
    I["broken_links"] = [{"source": e["source"], "target": e["target"], "status": e["target_status"], "anchor": e["anchor"]}
                         for e in edges if e["target_status"] is not None and (e["target_status"] >= 400 or e["target_status"] == 0)]
    I["redirects"] = [{"url": r["url"], "hops": len(r["redirect_chain"]), "final_url": r["final_url"],
                       "codes": ">".join(str(c["status"]) for c in r["redirect_chain"]), "inlinks": r["inlinks"], "in_sitemap": r["in_sitemap"]}
                      for r in pages.values() if r["redirect_chain"]]
    red = {r["url"]: r for r in I["redirects"]}
    I["links_to_redirects"] = [{"source": e["source"], "target": e["target"], "final_url": red[e["target"]]["final_url"],
                                "codes": red[e["target"]]["codes"], "anchor": e["anchor"]}
                               for e in edges if e["internal"] and e["target"] in red]
    I["noindex"] = [{"url": r["url"], "robots": r.get("robots"), "x_robots_tag": r.get("x_robots_tag"), "inlinks": r["inlinks"], "in_sitemap": r["in_sitemap"]}
                    for r in html if r.get("noindex")]
    I["canonical_other"] = [{"url": r["url"], "canonical": r["canonical"], "in_sitemap": r["in_sitemap"]}
                            for r in html if r.get("canonical") and r["canonical"] != r["url"]]
    I["canonical_missing"] = [{"url": r["url"]} for r in html if not r.get("canonical")]
    I["title_missing"] = [{"url": r["url"]} for r in indexable if not r.get("title")]
    I["title_length"] = [{"url": r["url"], "len": r["title_len"], "title": r["title"]} for r in indexable
                         if r.get("title") and not 30 <= r["title_len"] <= 65]
    I["description_missing"] = [{"url": r["url"]} for r in indexable if not r.get("description")]
    I["description_length"] = [{"url": r["url"], "len": r["description_len"]} for r in indexable
                               if r.get("description") and not 70 <= r["description_len"] <= 165]
    I["h1_problems"] = [{"url": r["url"], "h1_count": r["h1_count"], "h1": " | ".join(r["h1"])} for r in indexable
                        if r["h1_count"] != 1 or not (r["h1"] and r["h1"][0])]
    for field, key in (("title", "title_duplicates"), ("description", "description_duplicates")):
        g = collections.defaultdict(list)
        for r in indexable:
            if r.get(field):
                g[(r["locale"], r[field].strip().lower())].append(r["url"])
        I[key] = [{"locale": k[0], "value": k[1][:120], "count": len(v), "urls": " ".join(v[:20])} for k, v in g.items() if len(v) > 1]
    I["images_missing_alt"] = [{"url": r["url"], "locale": r["locale"], "no_alt": len(r["images_no_alt"]),
                                "empty_alt": r.get("images_empty_alt", 0), "images_total": r.get("images", 0),
                                "examples": " ".join(r["images_no_alt"][:10])}
                               for r in html if r.get("images_no_alt") or r.get("images_empty_alt")]
    I["faqpage_empty"] = [{"url": r["url"]} for r in html if r.get("faqpage_empty")]
    I["jsonld_errors"] = [{"url": r["url"], "errors": r["jsonld_errors"]} for r in html if r.get("jsonld_errors")]
    I["thin_content"] = [{"url": r["url"], "words": r["words"]} for r in indexable if r.get("words", 0) < 150]
    I["sitemap_bad"] = [{"url": u, "status": pages.get(normalize(u) or u, {}).get("status"),
                         "problem": ("space/invalid" if " " in u else
                                     "not crawled" if (normalize(u) or u) not in pages else
                                     "non-200" if pages[normalize(u) or u]["status"] != 200 else
                                     "noindex" if pages[normalize(u) or u].get("noindex") else
                                     "canonical elsewhere")}
                        for u in sorted(set(sm_raw))
                        if " " in u or (normalize(u) or u) not in pages or pages[normalize(u) or u]["status"] != 200
                        or pages[normalize(u) or u].get("noindex")
                        or (pages[normalize(u) or u].get("canonical") and pages[normalize(u) or u]["canonical"] != (normalize(u) or u))]
    I["sitemap_duplicates"] = [{"url": u, "count": c} for u, c in collections.Counter(sm_raw).items() if c > 1]
    I["not_in_sitemap"] = [{"url": r["url"], "locale": r["locale"], "inlinks": r["inlinks"]} for r in indexable if not r["in_sitemap"]]
    I["orphans"] = [{"url": r["url"], "locale": r["locale"]} for r in pages.values() if r["in_sitemap"] and r["inlinks"] == 0 and r["url"] != start]
    I["deep_pages"] = [{"url": r["url"], "depth": r["depth"]} for r in indexable if r["depth"] is None or r["depth"] > 3]
    blog_to_money = collections.Counter()
    for e in edges:
        if e["internal"] and "/blog/post/" in e["source"] and any(m in urllib.parse.urlsplit(e["target"]).path for m in MONEY):
            blog_to_money[e["target"]] += 1
    I["money_pages_inlinks"] = sorted(
        [{"url": r["url"], "inlinks": r["inlinks"], "inlinks_follow": r["inlinks_follow"], "from_blog": blog_to_money.get(r["url"], 0), "depth": r["depth"]}
         for r in indexable if any(m in urllib.parse.urlsplit(r["url"]).path for m in MONEY)],
        key=lambda x: x["inlinks"])
    if a.check_external:
        I["external_broken"] = [{"source": e["source"], "target": e["target"], "status": e["target_status"], "anchor": e["anchor"]}
                                for e in edges if not e["internal"] and e["target_status"] is not None
                                and (e["target_status"] >= 400 or e["target_status"] == 0)]

    # ---------- запись ----------
    json.dump({"meta": {"start": start, "crawled_at": dt.datetime.now().isoformat(timespec="seconds"),
                        "pages": len(pages), "truncated": truncated, "robots_blocked": len(blocked)},
               "pages": list(pages.values())}, open(os.path.join(out, "pages.json"), "w"), ensure_ascii=False)
    with gzip.open(os.path.join(out, "links.csv.gz"), "wt", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["source", "target", "anchor", "nofollow", "internal", "target_status"])
        w.writeheader(); w.writerows(edges)
    for name, rows in I.items():
        path = os.path.join(out, "issues", f"{name}.csv")
        if not rows:
            if os.path.exists(path):
                os.remove(path)
            continue
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
    by_status = collections.Counter(r["status"] for r in pages.values())
    by_locale = collections.Counter(r["locale"] for r in html)
    summary = {"crawled_at": dt.datetime.now().isoformat(timespec="seconds"), "start": start,
               "pages_crawled": len(pages), "html_pages": len(html), "indexable": len(indexable),
               "truncated_by_max_pages": truncated, "robots_blocked_links": len(blocked),
               "sitemap_urls": len(sm_raw), "internal_links": sum(1 for e in edges if e["internal"]),
               "external_links": sum(1 for e in edges if not e["internal"]),
               "status_codes": dict(sorted(by_status.items())), "html_by_locale": dict(by_locale),
               "issues": {k: len(v) for k, v in I.items()},
               "images_total": sum(r.get("images", 0) for r in html),
               "images_missing_alt_total": sum(len(r.get("images_no_alt", [])) for r in html),
               "images_empty_alt_total": sum(r.get("images_empty_alt", 0) for r in html),
               "duration_s": int(time.time() - t0)}
    json.dump(summary, open(os.path.join(out, "summary.json"), "w"), indent=1, ensure_ascii=False)

    print(f"\nГотово за {summary['duration_s']} с: {len(pages)} URL ({len(html)} HTML, {len(indexable)} индексируемых)"
          f"{' — ОБРЕЗАНО лимитом' if truncated else ''} -> {os.path.relpath(out, ROOT) if out.startswith(ROOT) else out}")
    print("Коды:", summary["status_codes"], "· локали:", summary["html_by_locale"])
    for k, v in summary["issues"].items():
        if v:
            print(f"  {k:24} {v}")


if __name__ == "__main__":
    main()
