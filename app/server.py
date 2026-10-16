#!/usr/bin/env python3
"""SEO Workspace — локальное веб-приложение для bixbit-seo.

Запуск:  python3 app/server.py   →   http://127.0.0.1:8765
Слушает только 127.0.0.1. Показывает файлы из reports/, content/, docs/, data/,
запускает только скрипты из белого списка COMMANDS (без shell), .env не читает.
Платные (DataForSEO) и «отправляющие наружу» команды требуют подтверждения в UI.
"""
import datetime as dt, glob, json, mimetypes, os, re, shutil, subprocess, sys, threading, time, urllib.parse, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from seo_common import yandex_expected  # noqa: E402
import run_report  # noqa: E402
BROWSE = ["reports", "content", "docs", "data"]
TEXT_EXT = {".md", ".html", ".csv", ".json", ".txt", ".yml", ".yaml"}
SKIP_DIRS = {"img", "raw", "__pycache__", "node_modules"}
EXPORT_DIR = os.path.expanduser("~/Documents/BiXBiT SEO")
NOTES_DIR = os.path.join(ROOT, "content", "notes")
PORT = int(os.environ.get("SEO_WORKSPACE_PORT", "8765"))
URL_RE = re.compile(r"^https://(bixbit\.io|docs\.bixbit\.io|bixbit\.tech)(/[^\s,]*)?$")


def today():
    return dt.date.today().isoformat()


def latest(pattern):
    files = sorted(f for f in glob.glob(os.path.join(ROOT, pattern)) if re.search(r"\d{4}-\d{2}-\d{2}", f))
    return files[-1] if files else None


# ---------- команды (белый список) --------------------------------------------
# steps: список argv; {today} подставляется; {urls} — проверенный список URL из формы
COMMANDS = [
    # Состояние
    dict(id="connectors", group="Состояние", title="Проверить источники данных", desc="GSC, GA4, PageSpeed, CrUX, Bing, Яндекс — статус подключения.",
         steps=[["./scripts/check-connectors.sh"]], cost=0, warn_codes=[1]),
    dict(id="index-check", group="Состояние", title="Индексация ключевых URL (Google)", desc="URL Inspection по 27 ключевым страницам + сравнение с прошлым днём.",
         steps=[["./scripts/index-check.py", "--out", "data/index-check/index-{today}.json"]], cost=0),
    dict(id="yandex-health", group="Состояние", title="Диагностика Яндекса", desc="Ошибки сайта в Вебмастере (FATAL/CRITICAL), страницы в поиске, сводка.",
         steps=[["./scripts/yandex-query.py", "--report", "diagnostics", "--out", "data/yandex/yandex-diagnostics-{today}.json"],
                ["./scripts/yandex-query.py", "--report", "insearch", "--days", "28", "--out", "data/yandex/yandex-insearch-{today}.json"],
                ["./scripts/yandex-query.py", "--report", "summary", "--out", "data/yandex/yandex-summary-{today}.json"]], cost=0),
    # Выгрузки
    dict(id="gsc", group="Выгрузки", title="Google Search Console, 28 дней", desc="Страны, страницы, запросы (все страны и US).",
         steps=[["./scripts/gsc-query.py", "--days", "28", "--dimensions", "country", "--out", "data/gsc-countries-{today}.json"],
                ["./scripts/gsc-query.py", "--days", "28", "--dimensions", "page", "--out", "data/gsc-pages-{today}.json"],
                ["./scripts/gsc-query.py", "--days", "28", "--dimensions", "query", "--out", "data/gsc-queries-all-{today}.json"],
                ["./scripts/gsc-query.py", "--days", "28", "--dimensions", "query,page", "--country", "usa", "--out", "data/gsc-queries-pages-us-{today}.json"]], cost=0),
    dict(id="ga4", group="Выгрузки", title="GA4: каналы и органика", desc="Сессии по каналам (включая AI Assistant) и органические посадочные.",
         steps=[["./scripts/ga4-query.py", "--preset", "channels", "--days", "28", "--out", "data/ga4-channels-{today}.json"],
                ["./scripts/ga4-query.py", "--preset", "organic-landing", "--days", "28", "--out", "data/ga4-organic-landing-{today}.json"]], cost=0),
    dict(id="bing", group="Выгрузки", title="Bing Webmaster", desc="Запросы и краул Bing.",
         steps=[["./scripts/bing-query.py", "--report", "queries", "--out", "data/bing-queries-{today}.json"],
                ["./scripts/bing-query.py", "--report", "crawl", "--out", "data/bing-crawl-{today}.json"]], cost=0),
    dict(id="yandex-queries", group="Выгрузки", title="Яндекс: запросы и обход", desc="Популярные запросы (28 дней) и история обхода.",
         steps=[["./scripts/yandex-query.py", "--report", "queries", "--days", "28", "--out", "data/yandex/yandex-queries-{today}.json"],
                ["./scripts/yandex-query.py", "--report", "indexing", "--days", "28", "--out", "data/yandex/yandex-indexing-{today}.json"]], cost=0),
    # Аудит
    dict(id="snapshot", group="Аудит", title="Снимок страниц (head, JSON-LD)", desc="Title, description, canonical, hreflang, schema 27 ключевых URL + diff с прошлым снимком.",
         steps=[["./scripts/page-snapshot.py", "--out", "data/page-snapshot-{today}.json"]], cost=0),
    dict(id="crawl", group="Аудит", title="Полный краул сайта", desc="~1 900 URL, 15–20 минут: 404, битые ссылки, редиректы, ALT, дубли, перелинковка.",
         steps=[["./scripts/crawl.py", "--check-external"]], cost=0, long=True),
    dict(id="cannibal", group="Аудит", title="Каннибализация", desc="Запросы, по которым показываются несколько страниц (GSC, 28 дней).",
         steps=[["./scripts/cannibalization.py", "--out", "data/cannibalization/cannibal-{today}.json"]], cost=0),
    dict(id="hreflang", group="Аудит", title="Проверка hreflang", desc="По последнему снимку страниц.",
         steps=[["./scripts/hreflang-check.py", "{latest_snapshot}", "--langs", "en,ru,es"]], cost=0, warn_codes=[1]),
    # Платные (DataForSEO)
    dict(id="serp-features", group="Позиции и AI (платно)", title="AI Overview / сниппеты", desc="Цитирует ли AIO bixbit по 30 ключам.",
         steps=[["./scripts/serp-features.py", "--out", "data/serp-features/serp-features-{today}.json"]], cost=0.10, confirm=True),
    dict(id="rank", group="Позиции и AI (платно)", title="Позиции по 30 ключам", desc="Google US, depth 100, дельты к baseline.",
         steps=[["./scripts/serp-rank.py", "--out", "data/rank-tracking/rank-{today}.json"]], cost=1.0, confirm=True),
    dict(id="backlinks", group="Позиции и AI (платно)", title="Ссылки: мы и конкуренты", desc="Rank, ссылающиеся домены, новые/потерянные за месяц.",
         steps=[["./scripts/backlinks-monitor.py", "--out", "data/backlinks/backlinks-{today}.json"]], cost=0.27, confirm=True),
    # Алерты
    dict(id="alerts-dry", group="Алерты", title="Проверить сайт (без отправки)", desc="Живая доступность, robots, Яндекс, индексация, noindex/canonical, позиции, краул — что ушло бы в Telegram.",
         steps=[["./scripts/alerts.py", "--dry-run"]], cost=0),
    dict(id="alerts", group="Алерты", title="Проверить и отправить в Telegram", desc="Новые P0/P1 и «решено»; если нового нет — короткий итог проверки.",
         steps=[["./scripts/alerts.py", "--always"]], cost=0, confirm=True, external=True),
    dict(id="alerts-digest", group="Алерты", title="Сводка в Telegram", desc="Все активные проблемы, включая P2.",
         steps=[["./scripts/alerts.py", "--digest"]], cost=0, confirm=True, external=True),
    # Переобход (отправка наружу)
    dict(id="reindex-dry", group="Переобход", title="Переобход: проверить квоты", desc="Bing/IndexNow и Яндекс — квоты и готовность, ничего не отправляет.",
         steps=[["./scripts/index-submit.py", "--urls", "{urls}"], ["./scripts/yandex-query.py", "--report", "recrawl"]], cost=0, needs_urls=True),
    dict(id="reindex", group="Переобход", title="Отправить URL на переобход", desc="Bing + IndexNow + Яндекс (квота 1 020/день). Для Google — ссылки на ручной запрос.",
         steps=[["./scripts/index-submit.py", "--urls", "{urls}", "--submit"],
                ["./scripts/yandex-query.py", "--report", "recrawl", "--urls", "{urls}", "--submit"]], cost=0, confirm=True, needs_urls=True, external=True),
]
CMD = {c["id"]: c for c in COMMANDS}
JOBS = {}
JOBS_LOCK = threading.Lock()


def run_job(job):
    try:
        _run_steps(job)
    finally:
        if job["status"] == "running":
            job["status"], job["ended"] = "error", time.time()
        job["ended"] = job["ended"] or time.time()
        try:
            job["report"] = run_report.build(job["cmd"], job["title"], job["status"], job["lines"], job["started"], job["ended"], job.get("urls"))
            job["lines"].append(f"[отчёт: {job['report']}]")
        except Exception as e:  # отчёт не должен ронять приложение
            job["lines"].append(f"[отчёт не сформирован: {e}]")


def _run_steps(job):
    for step in job["steps"]:
        job["lines"].append("$ " + " ".join(step))
        try:
            p = subprocess.Popen(step, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        except OSError as e:
            job["lines"].append(f"не удалось запустить: {e}")
            job["status"], job["rc"] = "error", -1
            return
        job["proc"] = p
        for line in p.stdout:
            job["lines"].append(line.rstrip("\n"))
        rc = p.wait()
        job["lines"].append(f"[код выхода {rc}]")
        if rc != 0 and rc in job.get("warn_codes", ()):
            job["warned"] = True
            continue
        if rc != 0:
            job["status"], job["rc"] = "error", rc
            job["ended"] = time.time()
            return
    job["status"], job["rc"], job["ended"] = ("warn" if job.get("warned") else "done"), 0, time.time()


def start_job(cid, urls):
    c = CMD[cid]
    snap = latest("data/page-snapshot-*.json") or ""
    steps = []
    for s in c["steps"]:
        argv = []
        for a in s:
            if a == "{urls}":
                argv.append(",".join(urls))
            else:
                argv.append(a.replace("{today}", today()).replace("{latest_snapshot}", os.path.relpath(snap, ROOT) if snap else ""))
        steps.append(argv)
    job = {"id": uuid.uuid4().hex[:10], "cmd": cid, "title": c["title"], "steps": steps, "lines": [],
           "status": "running", "rc": None, "started": time.time(), "ended": None, "warn_codes": tuple(c.get("warn_codes", ())),
           "urls": urls, "report": None}
    with JOBS_LOCK:
        JOBS[job["id"]] = job
    threading.Thread(target=run_job, args=(job,), daemon=True).start()
    return job


# ---------- файлы ---------------------------------------------------------------

def safe_path(rel):
    if not rel:
        return None
    full = os.path.realpath(os.path.join(ROOT, rel))
    if os.path.basename(full).startswith(".env") or "service-account" in full:
        return None
    for d in BROWSE + ["content/notes"]:
        base = os.path.realpath(os.path.join(ROOT, d))
        if full == base or full.startswith(base + os.sep):
            return full
    return None


def tree():
    out = []
    for d in BROWSE:
        for dp, dns, fns in os.walk(os.path.join(ROOT, d)):
            dns[:] = sorted(x for x in dns if not x.startswith(".") and x not in SKIP_DIRS)
            for f in fns:
                ext = os.path.splitext(f)[1].lower()
                if f.startswith(".") or ext not in TEXT_EXT:
                    continue
                full = os.path.join(dp, f)
                st = os.stat(full)
                if d == "data" and st.st_size > 5_000_000:
                    continue
                out.append({"path": os.path.relpath(full, ROOT), "size": st.st_size, "mtime": st.st_mtime, "ext": ext})
    return out


def search(q, limit=60):
    q = q.lower().strip()
    if len(q) < 2:
        return []
    res = []
    for f in tree():
        if f["ext"] not in {".md", ".html", ".csv", ".txt"} or f["size"] > 2_000_000:
            continue
        try:
            text = open(os.path.join(ROOT, f["path"]), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        low = text.lower()
        i = low.find(q)
        in_name = q in f["path"].lower()
        if i < 0 and not in_name:
            continue
        snip = ""
        if i >= 0:
            s = re.sub(r"<[^>]+>", " ", text[max(0, i - 80): i + 120])
            snip = " ".join(s.split())
        res.append({"path": f["path"], "snippet": snip, "hits": low.count(q), "name_match": in_name})
    res.sort(key=lambda r: (not r["name_match"], -r["hits"]))
    return res[:limit]


# ---------- сводка ------------------------------------------------------------------

def jload(p):
    try:
        return json.load(open(p))
    except Exception:
        return None


def status():
    cards, alerts = [], []

    def date_of(p):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", p or "")
        return m.group(1) if m else None

    p = latest("data/index-check/index-*.json")
    d = jload(p) if p else None
    if d:
        s = d.get("summary", {})
        cards.append({"k": "Индексация Google", "v": f"{s.get('pass')}/{d['meta'].get('urls')}", "sub": "ключевых URL в индексе", "date": date_of(p), "src": os.path.relpath(p, ROOT)})
        if s.get("not_pass"):
            alerts.append({"level": "p1", "text": f"Google: {s['not_pass']} ключевых URL не в индексе или с чужим canonical", "src": os.path.relpath(p, ROOT)})
    p = latest("data/yandex/yandex-diagnostics-*.json")
    d = jload(p) if p else None
    if d:
        expected = yandex_expected(d)
        probs = {k: v for k, v in (d.get("data", {}).get("problems") or {}).items() if v.get("state") == "PRESENT"}
        fatal = [k for k, v in probs.items() if v.get("severity") in ("FATAL", "CRITICAL") and k not in expected]
        sub = ", ".join(fatal) or ("критичных нет (CONNECT_FAILED ожидаем: блокировка РФ)" if expected & set(probs) else "критичных нет")
        cards.append({"k": "Яндекс: ошибки", "v": str(len(fatal)), "sub": sub, "date": date_of(p), "src": os.path.relpath(p, ROOT), "bad": bool(fatal)})
        for k in fatal:
            alerts.append({"level": "p0", "text": f"Яндекс.Вебмастер: {probs[k]['severity']} {k}", "src": os.path.relpath(p, ROOT)})
    p = latest("data/yandex/yandex-insearch-*.json")
    d = jload(p) if p else None
    if d:
        h = d.get("data", {}).get("history") or []
        if h:
            cards.append({"k": "Яндекс: страниц в поиске", "v": f"{h[-1]['value']:,}".replace(",", " "), "sub": f"было {h[0]['value']:,}".replace(",", " ") + " в начале периода", "date": date_of(p), "src": os.path.relpath(p, ROOT)})
    p = latest("data/gsc-countries-*.json")
    d = jload(p) if p else None
    if d:
        rows = d.get("rows", [])
        clicks = sum(r["clicks"] for r in rows)
        usa = next((r for r in rows if r.get("country") == "usa"), None)
        cards.append({"k": "Google: клики за 28 дней", "v": f"{clicks:,}".replace(",", " "), "sub": f"США {usa['clicks']} · CTR {usa['ctr'] * 100:.2f}%" if usa else "", "date": date_of(p), "src": os.path.relpath(p, ROOT)})
    p = latest("data/serp-features/serp-features-*.json")
    d = jload(p) if p else None
    if d:
        s = d.get("summary", {})
        cards.append({"k": "AI Overview цитирует bixbit", "v": f"{s.get('aio_cites_bixbit')}/{s.get('with_aio')}", "sub": f"из {s.get('keywords')} ключей", "date": date_of(p), "src": os.path.relpath(p, ROOT)})
    p = latest("data/rank-tracking/rank-*.json") or latest("data/rank-tracking/baseline-*.json")
    d = jload(p) if p else None
    if d:
        ks = d.get("keywords", [])
        top10 = sum(1 for k in ks if k.get("position") and k["position"] <= 10)
        cards.append({"k": "Позиции Google US", "v": f"{top10}/{len(ks)}", "sub": "ключей в топ-10", "date": date_of(p), "src": os.path.relpath(p, ROOT)})
    p = latest("data/crawl-*/summary.json")
    d = jload(p) if p else None
    if d:
        iss = d.get("issues", {})
        cards.append({"k": "Краул: ошибки", "v": str(iss.get("error_pages", 0)), "sub": f"битых ссылок {iss.get('broken_links', 0)} · пустых FAQ {iss.get('faqpage_empty', 0)}", "date": date_of(p), "src": os.path.relpath(p, ROOT)})
    p = latest("data/backlinks/backlinks-*.json")
    d = jload(p) if p else None
    if d:
        s = d.get("summaries", {}).get("bixbit.io", {})
        cards.append({"k": "Ссылки (rank 0–100)", "v": str(s.get("rank")), "sub": f"{s.get('referring_main_domains')} ссылающихся доменов", "date": date_of(p), "src": os.path.relpath(p, ROOT)})
    return {"cards": cards, "alerts": alerts, "today": today()}


def last_report(cid):
    """Последний отчёт запуска команды: reports/runs/<дата>-<id>.md."""
    f = sorted(glob.glob(os.path.join(ROOT, "reports/runs", f"????-??-??-{cid}.md")))
    return os.path.relpath(f[-1], ROOT) if f else None


def claude_commands():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, ".claude/commands/*.md"))):
        t = open(f, encoding="utf-8").read()
        m = re.search(r"^description:\s*(.+)$", t, re.M)
        h = re.search(r'^argument-hint:\s*"?(.+?)"?$', t, re.M)
        out.append({"name": "/" + os.path.splitext(os.path.basename(f))[0], "desc": m.group(1).strip() if m else "", "hint": h.group(1) if h else ""})
    return out


# ---------- HTTP -------------------------------------------------------------------

class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body, ctype="application/json; charset=utf-8", extra=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False).encode()
        elif isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def host_ok(self):
        h = (self.headers.get("Host") or "").split(":")[0]
        return h in ("127.0.0.1", "localhost")

    def do_GET(self):
        if not self.host_ok():
            return self.send(403, {"error": "forbidden host"})
        u = urllib.parse.urlsplit(self.path)
        qs = urllib.parse.parse_qs(u.query)
        q1 = lambda k: (qs.get(k) or [""])[0]
        if u.path in ("/", "/index.html"):
            return self.send(200, open(os.path.join(APP, "index.html"), encoding="utf-8").read(), "text/html; charset=utf-8")
        if u.path == "/api/tree":
            return self.send(200, tree())
        if u.path == "/api/status":
            return self.send(200, status())
        if u.path == "/api/commands":
            return self.send(200, {"scripts": [{k: v for k, v in c.items() if k != "steps"} | {"steps": [" ".join(s) for s in c["steps"]], "last_report": last_report(c["id"])} for c in COMMANDS],
                                   "claude": claude_commands()})
        if u.path == "/api/search":
            return self.send(200, search(q1("q")))
        if u.path in ("/api/file", "/api/raw", "/api/download"):
            full = safe_path(q1("path"))
            if not full or not os.path.isfile(full):
                return self.send(404, {"error": "not found"})
            data = open(full, "rb").read()
            ctype = mimetypes.guess_type(full)[0] or "text/plain"
            if ctype.startswith("text/") or ctype in ("application/json",):
                ctype += "; charset=utf-8"
            extra = {}
            if u.path == "/api/download":
                extra["Content-Disposition"] = "attachment; filename*=UTF-8''" + urllib.parse.quote(os.path.basename(full))
            if u.path == "/api/raw":
                extra["Content-Security-Policy"] = "sandbox allow-scripts allow-popups"
            return self.send(200, data, ctype, extra)
        m = re.match(r"^/api/jobs/([0-9a-f]+)$", u.path)
        if m:
            j = JOBS.get(m.group(1))
            if not j:
                return self.send(404, {"error": "no job"})
            since = int(q1("since") or 0)
            return self.send(200, {k: j.get(k) for k in ("id", "cmd", "title", "status", "rc", "started", "ended", "report")} | {"lines": j["lines"][since:], "next": len(j["lines"])})
        if u.path == "/api/jobs":
            return self.send(200, [{k: j.get(k) for k in ("id", "cmd", "title", "status", "rc", "started", "ended", "report")} for j in sorted(JOBS.values(), key=lambda x: -x["started"])][:20])
        return self.send(404, {"error": "not found"})

    def do_POST(self):
        if not self.host_ok() or self.headers.get("X-Workspace") != "1":
            return self.send(403, {"error": "forbidden"})
        u = urllib.parse.urlsplit(self.path)
        n = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError:
            return self.send(400, {"error": "bad json"})
        if u.path == "/api/run":
            c = CMD.get(body.get("id"))
            if not c:
                return self.send(404, {"error": "unknown command"})
            if c.get("confirm") and body.get("confirmed") is not True:
                return self.send(409, {"error": "confirmation required"})
            urls = []
            if c.get("needs_urls"):
                urls = [x.strip() for x in re.split(r"[\s,]+", body.get("urls") or "") if x.strip()]
                bad = [x for x in urls if not URL_RE.match(x)]
                if not urls or bad:
                    return self.send(400, {"error": "нужны URL вида https://bixbit.io/... (через пробел или запятую)", "bad": bad})
            if any(j["cmd"] == c["id"] and j["status"] == "running" for j in JOBS.values()):
                return self.send(409, {"error": "эта команда уже выполняется"})
            return self.send(200, {"job": start_job(c["id"], urls)["id"]})
        if u.path == "/api/export":
            full = safe_path(body.get("path"))
            if not full or not os.path.isfile(full):
                return self.send(404, {"error": "not found"})
            os.makedirs(EXPORT_DIR, exist_ok=True)
            dst = os.path.join(EXPORT_DIR, os.path.basename(full))
            shutil.copy2(full, dst)
            return self.send(200, {"saved": dst})
        if u.path == "/api/reveal":
            full = safe_path(body.get("path"))
            if not full or not os.path.exists(full):
                return self.send(404, {"error": "not found"})
            subprocess.run(["open", "-R", full], check=False)
            return self.send(200, {"ok": True})
        if u.path == "/api/note":
            title = (body.get("title") or "").strip() or "Заметка"
            text = body.get("text") or ""
            slug = re.sub(r"[^\w\-]+", "-", title.lower(), flags=re.U).strip("-")[:60] or "note"
            os.makedirs(NOTES_DIR, exist_ok=True)
            path = os.path.join(NOTES_DIR, f"{today()}-{slug}.md")
            if os.path.exists(path) and not body.get("overwrite"):
                path = os.path.join(NOTES_DIR, f"{today()}-{slug}-{uuid.uuid4().hex[:4]}.md")
            open(path, "w", encoding="utf-8").write(f"# {title}\n\n{text.rstrip()}\n")
            return self.send(200, {"path": os.path.relpath(path, ROOT)})
        return self.send(404, {"error": "not found"})


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), H)
    print(f"SEO Workspace: http://127.0.0.1:{PORT}  (Ctrl+C — остановить)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
