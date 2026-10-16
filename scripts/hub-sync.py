#!/usr/bin/env python3
"""hub-sync.py — собирает данные для онлайн-приложения команды (BiXBiT SEO Hub).

Готовит папку .hub-build/:
  docs/<path>          — документы проекта (reports/, content/, docs/, ключевые data/*.md)
  docs-index.json      — список документов: path, title, section, ext, size, mtime
  metrics.json         — KPI и алерты (как «Обзор» в SEO Workspace + активные P0/P1 из алертов)
  publish-files.json   — список путей для публикации (для Artifact files + root=.hub-build)

Публикует Claude: Artifact(file_path=reports/team-hub.html, root=.hub-build, files=[...])
и ArtifactData set metrics/current ← .hub-build/metrics.json.

Пример:  ./scripts/hub-sync.py
"""
import datetime as dt, glob, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "app"))
import server  # noqa: E402  (status() — те же KPI, что в SEO Workspace)

BUILD = os.path.join(ROOT, ".hub-build")
INCLUDE = ["reports/**/*.md", "reports/**/*.html", "content/**/*.md", "content/**/*.csv", "content/**/*.txt",
           "content/**/*.html", "docs/**/*.md", "data/site-structure.md", "data/rank-tracking/keywords.md",
           "data/blog-audit-*.csv", "data/yandex/reachability-*.md"]
EXCLUDE = re.compile(r"(^reports/team-hub\.html$|/\.|\.env|service-account|/img/"
                     r"|2026-06-1[0-9]"                       # июньские отчёты: частично ложные (WebFetch), см. agent-knowledge
                     r"|^content/dev-task-p0\.md$|^content/seo-fixes/"   # устаревшие задания
                     r"|group-[ab]-alt\.csv$|meta-docs\.csv$"       # дубли alt-all.csv / meta-docs.md
                     r"|docs-bixbit-io-tags-alt\.html$)")           # опубликовано отдельной страницей
MAX_BYTES = 8_000_000
# Карточка KPI → документ-пояснение в хабе (последний по дате файл из шаблона)
CARD_DOCS = {"Яндекс": "data/yandex/reachability-*.md", "Позиции": "reports/rank-tracking-*.md",
             "Краул": "reports/crawl-*.md", "Google: клики": "reports/full-report-*.html",
             "AI Overview": "reports/competitor-gap-summary-*.md", "Ссылки": "reports/competitor-gap-summary-*.md"}
CMD_FIELDS = ("id", "group", "title", "desc", "cost", "confirm", "external", "needs_urls", "long")
SECTIONS = [("reports/runs/", "Отчёты запусков"), ("reports/sub/", "Отчёты агентов"), ("reports/", "Отчёты"), ("content/briefs/", "Брифы"),
            ("content/clusters/", "Кластеры"), ("content/documentation/", "Документация"), ("content/es/", "ES"),
            ("content/outreach/", "Линкбилдинг"), ("content/geo/", "GEO / AI"), ("content/page-optimize/", "Оптимизация страниц"),
            ("content/notes/", "Заметки"), ("content/", "Контент и планы"), ("docs/", "База знаний"), ("data/", "Данные")]


def title_of(path, text):
    if path.endswith(".md"):
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            return re.sub(r"[`*_]", "", m.group(1)).strip()[:140]
    if path.endswith(".html"):
        m = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
        if m:
            return " ".join(m.group(1).split())[:140]
    return os.path.basename(path)


def main():
    if os.path.isdir(BUILD):
        shutil.rmtree(BUILD)
    os.makedirs(BUILD)
    files = set()
    for pat in INCLUDE:
        for f in glob.glob(os.path.join(ROOT, pat), recursive=True):
            rel = os.path.relpath(f, ROOT)
            if os.path.isfile(f) and not EXCLUDE.search(rel) and os.path.getsize(f) <= MAX_BYTES:
                files.add(rel)
    index, publish = [], []
    for rel in sorted(files):
        src = os.path.join(ROOT, rel)
        dst = os.path.join(BUILD, "docs", rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        text = open(src, encoding="utf-8", errors="replace").read(20000)
        st = os.stat(src)
        index.append({"path": rel, "title": title_of(rel, text), "ext": os.path.splitext(rel)[1].lower(),
                      "section": next(n for p, n in SECTIONS if rel.startswith(p)) if any(rel.startswith(p) for p, _ in SECTIONS) else "Прочее",
                      "size": st.st_size, "mtime": dt.datetime.fromtimestamp(st.st_mtime).isoformat(timespec="minutes")})
        publish.append("docs/" + rel)

    st = server.status()
    alerts = []
    state = server.jload(os.path.join(ROOT, "data/alerts/state.json")) or {"active": {}}
    for k, v in state.get("active", {}).items():
        if v.get("sev") in ("P0", "P1"):
            alerts.append({"level": v["sev"], "title": v["title"], "detail": ""})
    for a in st["alerts"]:  # добавить то, чего нет в состоянии алертов
        if not any(a["text"].endswith(x["title"].split(": ", 1)[-1]) for x in alerts):
            alerts.append({"level": a["level"].upper(), "title": a["text"], "detail": ""})
    now = dt.datetime.now()
    def card_doc(k):
        for prefix, pat in CARD_DOCS.items():
            if k.startswith(prefix):
                hits = sorted(x for x in files if glob.fnmatch.fnmatch(x, pat))
                return hits[-1] if hits else None
    cards = []
    for c in st["cards"]:
        card = {k: c[k] for k in ("k", "v", "sub", "date")} | ({"bad": True} if c.get("bad") else {})
        if card_doc(c["k"]):
            card["doc"] = card_doc(c["k"])
        cards.append(card)
    metrics = {"asof": now.strftime("%d.%m.%Y %H:%M"), "synced_at": now.isoformat(timespec="minutes"),
               "alerts": alerts,
               "cards": cards,
               "docs_count": len(index)}
    json.dump(index, open(os.path.join(BUILD, "docs-index.json"), "w"), ensure_ascii=False)
    json.dump(metrics, open(os.path.join(BUILD, "metrics.json"), "w"), ensure_ascii=False, indent=1)
    commands = [{k: c[k] for k in CMD_FIELDS if c.get(k) not in (None, False)} for c in server.COMMANDS]
    for c in commands:  # последний отчёт запуска (есть в хабе)
        rep = server.last_report(c["id"])
        if rep and rep in files:
            c["last_report"] = rep
    json.dump(commands, open(os.path.join(BUILD, "commands.json"), "w"), ensure_ascii=False)
    publish.insert(0, "commands.json")
    publish.insert(0, "docs-index.json")
    json.dump(publish, open(os.path.join(BUILD, "publish-files.json"), "w"), ensure_ascii=False)
    total = sum(os.path.getsize(os.path.join(BUILD, p)) for p in publish)
    print(f"документов: {len(index)} · файлов к публикации: {len(publish)} · {total / 1e6:.1f} MB · алертов: {len(alerts)} · KPI: {len(metrics['cards'])}")
    if len(publish) > 250 or total > 60e6:
        print("ВНИМАНИЕ: превышен лимит публикации (255 файлов / 64 MB) — сузьте INCLUDE")


if __name__ == "__main__":
    main()
