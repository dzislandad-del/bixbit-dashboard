"""run_report.py — отчёт о запуске команды понятным языком (Markdown).

Вызывается после каждого запуска из SEO Workspace (app/server.py) и из очереди хаба (run-command.py).
Читает файлы, которые записала команда (`--out …` в шагах), и stdout. Пишет
reports/runs/<дата>-<команда>.md (повторный запуск в тот же день перезаписывает отчёт).
Только факты из выгрузок — никаких выводов, которых нет в данных.
"""
import csv, datetime as dt, glob, gzip, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = "reports/runs"

STATUS_RU = {"done": "выполнено", "warn": "выполнено, есть замечания", "error": "ошибка", "ok": "выполнено"}
YANDEX_RU = {
    "CONNECT_FAILED": "робот не может подключиться к сайту", "NO_ROBOTS_TXT": "робот не видит robots.txt",
    "NO_SITEMAPS": "нет файлов Sitemap", "ERRORS_IN_SITEMAPS": "ошибки в Sitemap", "SOFT_404": "страницы-«мягкие 404»",
    "DOCUMENTS_MISSING_TITLE": "страницы без title", "DOCUMENTS_MISSING_DESCRIPTION": "страницы без description",
    "SLOW_AVG_RESPONSE_TIME": "медленный ответ сервера", "MAIN_PAGE_REDIRECTS": "главная страница редиректит",
    "THREATS": "угрозы безопасности", "BIG_FAVICON_ABSENT": "нет крупного favicon", "INSIGNIFICANT_CGI_PARAMETER": "незначащие GET-параметры",
    "ERROR_IN_ROBOTS_TXT": "ошибки в robots.txt", "NOT_IN_SPRAV": "компании нет в Яндекс.Бизнесе", "DUPLICATE_PAGES": "дубли страниц",
    "NOT_MOBILE_FRIENDLY": "не адаптировано для мобильных", "DISALLOWED_IN_ROBOTS": "сайт закрыт в robots.txt",
    "DNS_ERROR": "ошибка DNS", "SSL_CERTIFICATE_ERROR": "ошибка SSL-сертификата", "HOST_DATA_OUTDATED": "данные о сайте устарели",
}
SEV_RU = {"FATAL": "фатальная", "CRITICAL": "критичная", "POSSIBLE_PROBLEM": "возможная проблема", "RECOMMENDATION": "рекомендация"}
CRAWL_RU = {
    "error_pages": "страницы с ошибкой (4xx/5xx)", "broken_links": "битые внутренние ссылки", "external_broken": "битые внешние ссылки",
    "redirects": "редиректы", "links_to_redirects": "ссылки на редиректы", "title_missing": "нет title", "title_duplicates": "дубли title",
    "title_length": "title вне нормы по длине", "description_duplicates": "дубли description", "description_length": "description вне нормы по длине",
    "h1_problems": "проблемы с H1", "images_missing_alt": "картинки без ALT", "jsonld_errors": "ошибки JSON-LD", "faqpage_empty": "пустой FAQPage",
    "noindex": "страницы с noindex", "canonical_other": "canonical на другую страницу", "orphans": "страницы-сироты (нет входящих ссылок)",
    "not_in_sitemap": "индексируемые страницы вне sitemap", "sitemap_bad": "плохие URL в sitemap", "sitemap_duplicates": "дубли в sitemap",
    "deep_pages": "глубокие страницы (4+ клика)", "money_pages_inlinks": "входящие ссылки на коммерческие страницы",
}


def n(x):
    try:
        return f"{int(round(float(x))):,}".replace(",", " ")
    except (TypeError, ValueError):
        return str(x)


def pct(x, d=1):
    return f"{float(x) * 100:.{d}f}%"


def jl(path):
    try:
        return json.load(open(os.path.join(ROOT, path), encoding="utf-8"))
    except Exception:
        return None


def table(head, rows):
    if not rows:
        return ""
    esc = lambda v: str(v).replace("|", "\\|").replace("\n", " ")
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(esc(v) for v in r) + " |" for r in rows]) + "\n"


def outs(lines):
    """Файлы, которые команда записала: аргумент --out из строк «$ …»."""
    res = []
    for ln in lines:
        if ln.startswith("$ ") and "--out" in ln:
            parts = ln[2:].split()
            i = parts.index("--out")
            if i + 1 < len(parts):
                res.append(parts[i + 1])
    return res


def stdout(lines):
    return [ln for ln in lines if ln.strip() and not ln.startswith("$ ") and not ln.startswith("[код выхода")]


def path_short(u):
    return re.sub(r"^https?://(www\.)?bixbit\.io", "", u) or "/"


# ---------- по командам: каждая возвращает (коротко[], что_сделать[], подробности_md) ----------

def r_index_check(o, lines, urls):
    d = jl(o[0]) if o else None
    if not d:
        return [], [], ""
    s, m = d["summary"], d["meta"]
    short = [f"В индексе Google {s['pass']} из {m['urls']} ключевых страниц."]
    if s.get("canonical_mismatch"):
        short.append(f"У {s['canonical_mismatch']} страниц Google выбрал другой canonical, не тот, что указан на странице.")
    ch = d.get("changes") or []
    short.append(f"Изменений со вчера: {len(ch)}." if m.get("compared_to") else "Сравнить не с чем — это первая проверка.")
    bad = [u for u in d["urls"] if u.get("verdict") != "PASS" or u.get("canonical_mismatch")]
    todo = [f"Разобраться со страницей {path_short(u['url'])}: {u.get('coverage_state') or u.get('verdict')}." for u in bad[:10]]
    det = ""
    if ch:
        det += "### Изменения\n" + "\n".join(f"- {c if isinstance(c, str) else json.dumps(c, ensure_ascii=False)}" for c in ch[:30]) + "\n\n"
    if bad:
        det += "### Страницы с проблемами\n" + table(["Страница", "Статус", "Canonical Google"], [[path_short(u["url"]), u.get("coverage_state") or u.get("verdict"), path_short(u.get("google_canonical") or "—")] for u in bad]) + "\n"
    det += "### Все проверенные страницы\n" + table(["Страница", "Статус в Google", "Последний обход"], [[path_short(u["url"]), u.get("coverage_state") or u.get("verdict"), (u.get("last_crawl") or "—")[:10]] for u in d["urls"]])
    return short, todo, det


def r_yandex(o, lines, urls):
    short, todo, det = [], [], ""
    for p in o:
        d = jl(p)
        if not d:
            continue
        host = (d.get("host") or {}).get("ascii_host_url", "")
        if d.get("report") == "diagnostics":
            import seo_common
            exp = seo_common.yandex_expected(d)
            probs = [(k, v) for k, v in (d["data"].get("problems") or {}).items() if v.get("state") == "PRESENT"]
            real = [(k, v) for k, v in probs if k not in exp]
            crit = [k for k, v in real if v["severity"] in ("FATAL", "CRITICAL")]
            short.append(f"Диагностика {host}: " + (f"критичных проблем {len(crit)} — " + ", ".join(YANDEX_RU.get(k, k) for k in crit) + "." if crit else "критичных проблем нет."))
            if exp & {k for k, _ in probs}:
                short.append("Ошибки подключения к bixbit.io ожидаемы: сайт заблокирован в РФ, российская аудитория ходит на bixbit.tech.")
            todo += [f"Яндекс: {YANDEX_RU.get(k, k)} ({SEV_RU.get(v['severity'], v['severity'])})." for k, v in real if v["severity"] in ("FATAL", "CRITICAL", "POSSIBLE_PROBLEM")]
            det += "### Проблемы в Вебмастере\n" + (table(["Проблема", "Уровень", "Примечание"], [[YANDEX_RU.get(k, k), SEV_RU.get(v["severity"], v["severity"]), "ожидаемо (блокировка РФ)" if k in exp else ""] for k, v in probs]) or "Нет активных проблем.\n") + "\n"
        elif d.get("report") == "insearch":
            h = d["data"].get("history") or []
            if h:
                short.append(f"Страниц в поиске Яндекса: {n(h[-1]['value'])} (в начале периода {n(h[0]['value'])}, минимум {n(min(x['value'] for x in h))}).")
                det += "### Страниц в поиске по дням\n" + table(["Дата", "Страниц"], [[x["date"][:10], n(x["value"])] for x in h]) + "\n"
        elif d.get("report") == "summary":
            s = d["data"]
            short.append(f"ИКС {s.get('sqi')}; страниц в поиске по сводке: {n(s.get('searchable_pages_count'))}, исключено: {n(s.get('excluded_pages_count'))}.")
        elif d.get("report") == "queries":
            q = sorted(d["data"].get("queries") or [], key=lambda x: -(x["indicators"].get("TOTAL_SHOWS") or 0))
            shows = sum(x["indicators"].get("TOTAL_SHOWS") or 0 for x in q)
            clicks = sum(x["indicators"].get("TOTAL_CLICKS") or 0 for x in q)
            short.append(f"Запросов в Яндексе: {n(len(q))}, показов {n(shows)}, кликов {n(clicks)} ({d['data'].get('date_from')} — {d['data'].get('date_to')}).")
            det += "### Топ-15 запросов по показам\n" + table(["Запрос", "Показы", "Клики", "Позиция"], [[x["query_text"], n(x["indicators"].get("TOTAL_SHOWS")), n(x["indicators"].get("TOTAL_CLICKS")), f"{x['indicators'].get('AVG_SHOW_POSITION') or 0:.1f}"] for x in q[:15]]) + "\n"
        elif d.get("report") == "indexing":
            ind = d["data"].get("indicators") or {}
            tot = {k: sum(x["value"] for x in v) for k, v in ind.items()}
            short.append("Обход роботом Яндекса: " + ", ".join(f"{k.replace('HTTP_', '')} — {n(v)}" for k, v in tot.items()) + ".")
    return short, todo, det


def r_gsc(o, lines, urls):
    short, det, zero_pages = [], "", []
    for p in o:
        d = jl(p)
        if not d:
            continue
        rows, m = d.get("rows") or [], d["meta"]
        dims = ",".join(m.get("dimensions") or [])
        period = f"{m.get('start')} — {m.get('end')}"
        if dims == "country":
            c, i = sum(r["clicks"] for r in rows), sum(r["impressions"] for r in rows)
            short.append(f"Google за {period}: {n(c)} кликов, {n(i)} показов, CTR {pct(c / i if i else 0, 2)}.")
            top = sorted(rows, key=lambda r: -r["clicks"])[:8]
            det += "### Клики по странам\n" + table(["Страна", "Клики", "Показы", "CTR", "Позиция"], [[r["country"].upper(), n(r["clicks"]), n(r["impressions"]), pct(r["ctr"], 2), f"{r['position']:.1f}"] for r in top]) + "\n"
            us = next((r for r in rows if r["country"] == "usa"), None)
            if us:
                short.append(f"США: {n(us['clicks'])} кликов, {n(us['impressions'])} показов, CTR {pct(us['ctr'], 2)}.")
        elif dims == "page":
            top = sorted(rows, key=lambda r: -r["clicks"])[:10]
            det += "### Топ-10 страниц по кликам\n" + table(["Страница", "Клики", "Показы", "Позиция"], [[path_short(r["page"]), n(r["clicks"]), n(r["impressions"]), f"{r['position']:.1f}"] for r in top]) + "\n"
            zero = [r for r in rows if r["clicks"] == 0 and r["impressions"] >= 500 and r["position"] <= 10]
            if zero:
                short.append(f"Страниц в топ-10 с 500+ показами и нулём кликов: {len(zero)} — кандидаты на новые title/description.")
                zero_pages[:] = [f"{path_short(r['page'])} — {n(r['impressions'])} показов, позиция {r['position']:.1f}" for r in sorted(zero, key=lambda r: -r["impressions"])[:8]]
        elif dims == "query":
            top = sorted(rows, key=lambda r: -r["clicks"])[:10]
            det += "### Топ-10 запросов (все страны)\n" + table(["Запрос", "Клики", "Показы", "Позиция"], [[r["query"], n(r["clicks"]), n(r["impressions"]), f"{r['position']:.1f}"] for r in top]) + "\n"
        elif dims == "query,page":
            top = sorted(rows, key=lambda r: -r["impressions"])[:10]
            det += "### США: топ-10 запросов по показам\n" + table(["Запрос", "Страница", "Клики", "Показы", "Позиция"], [[r["query"], path_short(r["page"]), n(r["clicks"]), n(r["impressions"]), f"{r['position']:.1f}"] for r in top]) + "\n"
    todo = [f"Переписать title/description: {z}." for z in zero_pages]
    return short, todo, det + "Примечание: разрез по запросам не включает анонимизированные запросы, поэтому итоги считаются по странам.\n"


def r_ga4(o, lines, urls):
    short, det = [], ""
    for p in o:
        d = jl(p)
        if not d:
            continue
        rows, m = d.get("rows") or [], d["meta"]
        if m.get("preset") == "channels":
            s = sum(r["sessions"] for r in rows)
            short.append(f"GA4 за {m['start']} — {m['end']}: {n(s)} сессий.")
            org = next((r for r in rows if r["sessionDefaultChannelGroup"] == "Organic Search"), None)
            if org:
                short.append(f"Органика: {n(org['sessions'])} сессий ({pct(org['sessions'] / s if s else 0)}), ключевых событий {n(org['keyEvents'])}.")
            ai = next((r for r in rows if "AI" in r["sessionDefaultChannelGroup"]), None)
            if ai:
                short.append(f"Переходы из AI-ассистентов: {n(ai['sessions'])} сессий.")
            det += "### Сессии по каналам\n" + table(["Канал", "Сессии", "Вовлечённые", "Ключевые события", "Пользователи"], [[r["sessionDefaultChannelGroup"], n(r["sessions"]), n(r["engagedSessions"]), n(r["keyEvents"]), n(r["totalUsers"])] for r in sorted(rows, key=lambda r: -r["sessions"])]) + "\n"
        elif m.get("preset") == "organic-landing":
            top = sorted(rows, key=lambda r: -r["sessions"])[:10]
            det += "### Органика: топ-10 страниц входа\n" + table(["Страница", "Сессии", "Вовлечённость", "Ключевые события"], [[r["landingPagePlusQueryString"][:90], n(r["sessions"]), pct(r["engagementRate"], 0), n(r["keyEvents"])] for r in top]) + "\n"
    return short, [], det


def r_bing(o, lines, urls):
    short, det = [], ""
    for p in o:
        d = jl(p)
        if not d:
            continue
        rows = d.get("data") or []
        if d["meta"]["report"] == "queries":
            agg = {}
            for r in rows:
                a = agg.setdefault(r["Query"], [0, 0])
                a[0] += r["Clicks"]; a[1] += r["Impressions"]
            c, i = sum(v[0] for v in agg.values()), sum(v[1] for v in agg.values())
            short.append(f"Bing: {n(len(agg))} запросов, {n(c)} кликов, {n(i)} показов за доступный период.")
            top = sorted(agg.items(), key=lambda x: -x[1][1])[:10]
            det += "### Bing: топ-10 запросов по показам\n" + table(["Запрос", "Клики", "Показы"], [[q, n(v[0]), n(v[1])] for q, v in top]) + "\n"
        elif d["meta"]["report"] == "crawl" and rows:
            rows = sorted(rows, key=lambda r: r.get("Date", ""))
            last, month = rows[-1], rows[-31] if len(rows) > 30 else rows[0]
            short.append(f"Bing обошёл страниц за последний день ({last.get('Date', '')[:10]}): {n(last['CrawledPages'])}, ошибок обхода: {n(last['CrawlErrors'])}.")
            if last.get("InIndex"):
                short.append(f"Страниц в индексе Bing: {n(last['InIndex'])} (месяц назад {n(month.get('InIndex'))}).")
            det += "### Обход Bing, последние 10 дней\n" + table(["Дата", "Обойдено", "Ошибок", "В индексе"], [[r.get("Date", "")[:10], n(r["CrawledPages"]), n(r["CrawlErrors"]), n(r.get("InIndex"))] for r in rows[-10:]]) + "\n"
    return short, [], det


FIELD_RU = {"title": "Title", "meta_description": "Description", "h1": "H1", "h1_count": "кол-во H1", "canonical": "Canonical",
            "robots": "meta robots", "x_robots_tag": "X-Robots-Tag", "status": "код ответа", "final_url": "редирект",
            "hreflang": "hreflang", "jsonld_types": "разметка JSON-LD", "jsonld_errors": "ошибки JSON-LD",
            "faqpage_empty": "пустой FAQPage", "org_description_hash": "описание Organization", "text": "текст",
            "h2": "H2", "h3": "H3", "alt": "ALT картинок", "html_bytes (>30%)": "вес HTML", "(new url)": "новая страница в списке",
            "(dropped from list)": "убрана из списка"}


def short_val(v, k=120):
    if isinstance(v, (list, dict)):
        v = json.dumps(v, ensure_ascii=False)
    v = "—" if v in (None, "", "None") else str(v)
    return v if len(v) <= k else v[:k] + "…"


def r_snapshot(o, lines, urls):
    d = jl(o[0]) if o else None
    if not d:
        return [], [], ""
    pages = d["pages"]
    short = [f"Снято {len(pages)} ключевых страниц."]
    bad = [p for p in pages if p.get("status") != 200]
    nod = [p for p in pages if not p.get("meta_description")]
    noindex = [p for p in pages if "noindex" in (p.get("robots") or "") + (p.get("x_robots_tag") or "")]
    if bad:
        short.append(f"Не отвечают 200: {len(bad)}.")
    if nod:
        short.append(f"Без meta description: {len(nod)}.")
    if noindex:
        short.append(f"С noindex: {len(noindex)}.")
    ch = d.get("changes")
    since = (d.get("meta", {}).get("compared_to") or "").replace("data/page-snapshot-", "").replace(".json", "")
    if ch is None:
        short.append("Сравнивать не с чем — это первый снимок.")
    elif not ch:
        short.append(f"С прошлого снимка ({since}) на страницах ничего не изменилось.")
    else:
        by = {}
        for c in ch:
            by[FIELD_RU.get(c["field"], c["field"])] = by.get(FIELD_RU.get(c["field"], c["field"]), 0) + 1
        short.append(f"С прошлого снимка ({since}) изменений: {len(ch)} — " + ", ".join(f"{k} {v}" for k, v in by.items()) + ".")
    todo = [f"Проверить {path_short(p['url'])}: код {p.get('status')}." for p in bad] + [f"Снять noindex или убедиться, что он нужен: {path_short(p['url'])}." for p in noindex]
    crit = [c for c in (ch or []) if c["field"] in ("status", "robots", "x_robots_tag", "canonical", "final_url", "faqpage_empty", "jsonld_errors")]
    todo += [f"Проверить изменение «{FIELD_RU.get(c['field'], c['field'])}» на {path_short(c['url'])}: {short_val(c['was'], 60)} → {short_val(c['now'], 60)}." for c in crit[:6]]
    det = ""
    if ch:
        simple = [c for c in ch if c["field"] not in ("text", "alt", "h2", "h3")]
        if simple:
            det += "### Изменения тегов\n" + table(["Страница", "Что", "Было", "Стало"], [[path_short(c["url"]), FIELD_RU.get(c["field"], c["field"]), short_val(c["was"]), short_val(c["now"])] for c in simple]) + "\n"
        for c in [c for c in ch if c["field"] == "text"][:10]:
            det += f"### Текст: {path_short(c['url'])} ({c['was']} → {c['now']})\n"
            det += "".join(f"- ➕ {short_val(b, 300)}\n" for b in c.get("added", [])[:8])
            det += "".join(f"- ➖ {short_val(b, 300)}\n" for b in c.get("removed", [])[:8]) + "\n"
        hx = [c for c in ch if c["field"] in ("h2", "h3")]
        if hx:
            det += "### Подзаголовки\n" + table(["Страница", "Уровень", "Убраны", "Добавлены"], [[path_short(c["url"]), c["field"].upper(), short_val(c["was"]), short_val(c["now"])] for c in hx]) + "\n"
        alts = [c for c in ch if c["field"] == "alt"]
        if alts:
            rows = []
            for c in alts:
                for k in sorted(set(c["was"]) | set(c["now"])):
                    rows.append([path_short(c["url"]), k, short_val(c["was"].get(k), 80), short_val(c["now"].get(k), 80)])
            det += "### ALT картинок\n" + table(["Страница", "Картинка", "Было", "Стало"], rows[:60]) + "\n"
    det += "### Страницы\n" + table(["Страница", "Код", "Title (длина)", "Description", "Слов", "Время ответа"], [[path_short(p["url"]), p.get("status"), p.get("title_len"), "есть" if p.get("meta_description") else "нет", p.get("main_words", "—"), f"{p.get('response_ms')} мс"] for p in pages])
    return short, todo, det


def r_sitemap(o, lines, urls):
    d = jl(o[0]) if o else None
    if not d:
        return [], [], ""
    s, g = d["summary"], d.get("gsc") or {}
    short = [f"В sitemap {n(s['urls'])} URL в {s['sitemap_files']} файлах" + (f", ошибок загрузки {s['fetch_errors']}" if s["fetch_errors"] else "") + "."]
    if d["meta"].get("compared_to"):
        short.append(f"С прошлой проверки: новых страниц {s['new']}, удалено {s['removed']}, обновлён lastmod у {s['lastmod_changed']}.")
    else:
        short.append("Это первая проверка — новые страницы начнут отслеживаться со следующего запуска.")
    todo, det = [], ""
    if g.get("checked"):
        short.append(f"GSC ({g['window']}): из sitemap не получили ни одного показа {n(g['sitemap_without_impressions'])} URL; "
                     f"страниц с показами, которых нет в sitemap, — {n(g['gsc_not_in_sitemap'])}.")
        for sm in g.get("sitemaps", []):
            if sm["errors"] or sm["warnings"]:
                todo.append(f"Sitemap в GSC {sm['path']}: ошибок {sm['errors']}, предупреждений {sm['warnings']} — исправить или удалить из GSC.")
        if g["gsc_not_in_sitemap"]:
            todo.append(f"Добавить в sitemap страницы с показами, которых там нет ({g['gsc_not_in_sitemap']}), или проверить, что они не дубли.")
        det += "### Sitemap в Google Search Console\n" + table(["Файл", "Скачан Google", "URL", "Ошибки", "Предупреждения"], [[sm["path"].replace("https://bixbit.io", ""), (sm["last_downloaded"] or "—")[:10], sm["submitted"], sm["errors"], sm["warnings"]] for sm in g.get("sitemaps", [])]) + "\n"
        det += "### URL из sitemap без показов — по разделам\n" + table(["Раздел", "URL"], list(g.get("sitemap_without_impressions_by_section", {}).items())[:20]) + "\n"
        det += "### Страницы с показами вне sitemap (топ-20)\n" + table(["Страница", "Показы", "Клики"], [[path_short(x["url"]), n(x["impressions"]), n(x["clicks"])] for x in g.get("gsc_not_in_sitemap_top", [])[:20]]) + "\n"
    if d.get("new_urls"):
        insp = {x["url"]: x for x in d.get("new_inspected", [])}
        det += "### Новые страницы\n" + table(["Страница", "Статус в Google"], [[path_short(u), (insp.get(u) or {}).get("coverage_state") or "не проверялась"] for u in d["new_urls"][:50]]) + "\n"
        todo += [f"Новая страница не в индексе Google: {path_short(x['url'])} ({x.get('coverage_state')})." for x in d.get("new_inspected", []) if x.get("verdict") not in ("PASS", None)][:8]
    if d.get("removed_urls"):
        det += "### Удалены из sitemap\n" + "".join(f"- {path_short(u)}\n" for u in d["removed_urls"][:50]) + "\n"
    return short, todo, det


def r_site_diff(o, lines, urls):
    f = sorted(glob.glob(os.path.join(ROOT, "data/site-diff/site-diff-*.json")))
    d = jl(os.path.relpath(f[-1], ROOT)) if f else None
    if not d:
        return [], [], ""
    s, m, c = d["summary"], d["meta"], d["changes"]
    short = [f"Сравнение краулов {m['old_date']} → {m['new_date']}: страниц {n(s['pages_old'])} → {n(s['pages_new'])}.",
             f"Новых страниц {s['new_pages']}, пропало {s['gone_pages']}, сменился код ответа у {s['status_changed']}."
             + (f" Ещё {s.get('gone_fetch_errors', 0)} страниц не ответили при краулинге (сбой загрузки, не удаление) и {s.get('gone_pagination', 0)} — пагинация и теги блога." if s.get("gone_fetch_errors") or s.get("gone_pagination") else ""),
             f"Изменились: title {s['title_changed']}, description {s['description_changed']}, H1 {s['h1_changed']}, canonical {s['canonical_changed']}, "
             f"noindex {s['noindex_changed']}, текст {s['text_changed']}, H2 {s['h2_changed']}, ALT {s['alt_changed']}, разметка {s['jsonld_changed']}."]
    if not s.get("text_compared"):
        short.append("Текст, H2 и ALT по значениям пока не сравнивались — в прошлом краулинге их не было; полное сравнение — со следующего краула.")
    todo = [f"Проверить, почему пропала страница {path_short(x['url'])} (сейчас: {x['now']})." for x in d["gone_pages"] if x.get("kind", "gone") == "gone"][:8]
    todo += [f"Новая страница {path_short(x['url'])}: " + ("нет в sitemap" if not x.get("in_sitemap") else "в sitemap") + (", noindex" if x.get("noindex") else "") + "." for x in d["new_pages"][:8]]
    todo += [f"Проверить смену noindex на {path_short(x['url'])}: {x['old']} → {x['new']}." for x in c.get("noindex", [])[:5]]
    det = ""
    if d["new_pages"]:
        det += "### Новые страницы\n" + table(["Страница", "Title", "В sitemap", "Входящих ссылок"], [[path_short(x["url"]), short_val(x["title"], 70), "да" if x["in_sitemap"] else "нет", x.get("inlinks")] for x in d["new_pages"][:50]]) + "\n"
    if d["gone_pages"]:
        kind_ru = {"gone": "удалена / ошибка", "fetch_error": "не ответила при краулинге", "pagination": "пагинация / теги"}
        det += "### Пропавшие страницы\n" + table(["Страница", "Title", "Сейчас", "Тип"], [[path_short(x["url"]), short_val(x["title"], 70), x["now"], kind_ru.get(x.get("kind", "gone"))] for x in d["gone_pages"][:50]]) + "\n"
    for k, lbl in (("title", "Title"), ("description", "Description"), ("h1", "H1"), ("canonical", "Canonical"), ("noindex", "noindex")):
        if c.get(k):
            det += f"### {lbl}\n" + table(["Страница", "Было", "Стало"], [[path_short(x["url"]), short_val(x["old"]), short_val(x["new"])] for x in c[k][:40]]) + "\n"
    if c.get("text"):
        det += "### Изменился текст\n" + table(["Страница", "Слов было", "Слов стало", "Δ"], [[path_short(x["url"]), x["words_old"], x["words_new"], x["delta"]] for x in sorted(c["text"], key=lambda x: -abs(x["delta"]))[:40]]) + "\n"
    if c.get("alt"):
        rows = []
        for x in c["alt"][:40]:
            for y in x.get("changed", []):
                rows.append([path_short(x["url"]), y["img"], short_val(y["old"], 60), short_val(y["new"], 60)])
            for y in x.get("added", []):
                rows.append([path_short(x["url"]), y["img"], "—", short_val(y["alt"], 60)])
            if "no_alt_old" in x:
                rows.append([path_short(x["url"]), "без ALT", x["no_alt_old"], x["no_alt_new"]])
        det += "### ALT картинок\n" + table(["Страница", "Картинка", "Было", "Стало"], rows[:60]) + "\n"
    return short, todo, det


def r_crawl(o, lines, urls):
    f = sorted(glob.glob(os.path.join(ROOT, "data/crawl-*/summary.json")))
    if not f:
        return [], [], ""
    s = json.load(open(f[-1], encoding="utf-8"))
    base = os.path.dirname(f[-1])
    codes = s.get("status_codes") or {}
    short = [f"Обойдено {n(s['pages_crawled'])} URL, из них HTML {n(s['html_pages'])}, индексируемых {n(s['indexable'])}.",
             "Коды ответа: " + ", ".join(f"{k} — {n(v)}" for k, v in sorted(codes.items())) + "."]
    counts = []
    for p in sorted(glob.glob(os.path.join(base, "issues", "*.csv"))):
        k = os.path.basename(p)[:-4]
        with open(p, encoding="utf-8") as fh:
            c = max(0, sum(1 for _ in fh) - 1)
        counts.append((k, c))
    main = [(k, c) for k, c in counts if c and k in ("error_pages", "broken_links", "faqpage_empty", "jsonld_errors", "title_missing", "orphans", "sitemap_bad")]
    todo = [f"{CRAWL_RU.get(k, k).capitalize()}: {n(c)} — список в data/{os.path.basename(base)}/issues/{k}.csv." for k, c in main]
    det = "### Все проверки\n" + table(["Проверка", "Найдено"], [[CRAWL_RU.get(k, k), n(c)] for k, c in counts])
    sd = sorted(glob.glob(os.path.join(ROOT, "data/site-diff/site-diff-*.json")))
    if sd and os.path.basename(sd[-1])[10:20] == os.path.basename(base)[6:]:
        s2, t2, d2 = r_site_diff(o, lines, urls)
        short += s2; todo += t2; det += "\n## Что изменилось на сайте\n\n" + d2
    return short, todo, det


def r_cannibal(o, lines, urls):
    d = jl(o[0]) if o else None
    if not d:
        return [], [], ""
    s = d["summary"]
    short = [f"Проверено запросов (от 20 показов): {n(s['queries_checked'])}.",
             f"Конфликты: {s['same_locale']} — внутри одного языка (главное), {s['cross_locale']} — между языковыми версиями, {s['brand']} — брендовые.",
             f"Новых конфликтов: {s.get('new', 0)}, ушло: {s.get('resolved', 0)}."]
    same = [c for c in d["conflicts"] if c["kind"] == "same_locale"][:10]
    todo = [f"«{c['query']}»: решить, какая страница главная — " + " vs ".join(path_short(p["page"]) for p in c["pages"][:2]) + "." for c in same[:5]]
    det = "### Топ-10 конфликтов внутри языка\n" + table(["Запрос", "Показы", "Страницы (доля показов, позиция)"], [[c["query"], n(c["impressions"]), "; ".join(f"{path_short(p['page'])} {pct(p.get('share', 0), 0)} p{p.get('position', 0):.0f}" for p in c["pages"][:3])] for c in same])
    if d.get("new_conflicts"):
        det += "\n### Новые конфликты\n" + "\n".join(f"- {q}" for q in d["new_conflicts"][:20]) + "\n"
    return short, todo, det


def r_serp_features(o, lines, urls):
    d = jl(o[0]) if o else None
    if not d:
        return [], [], ""
    s = d["summary"]
    short = [f"AI Overview есть в {s['with_aio']} из {s['keywords']} запросов; bixbit цитируется в {s['aio_cites_bixbit']}.",
             f"Featured snippet: {s['with_featured_snippet']} (наших {s['fs_bixbit']}); «Люди также спрашивают»: {s['with_paa']} (наших {s['paa_bixbit']}).",
             "Чаще всего AI Overview цитирует: " + ", ".join(s.get("top_aio_domains", [])[:5]) + ".",
             f"Стоимость запуска: ${s.get('cost_usd')}."]
    miss = [k for k in d["keywords"] if k.get("ai_overview") and not k.get("aio_cites_bixbit")]
    todo = [f"Нет цитаты в AI Overview по {len(miss)} запросам — усилить блоки-ответы на целевых страницах (см. таблицу)."] if miss else []
    det = table(["Запрос", "AIO", "Цитирует bixbit", "Конкуренты в AIO"], [[k["keyword"], "да" if k.get("ai_overview") else "нет", "да" if k.get("aio_cites_bixbit") else "нет", ", ".join((k.get("aio_competitors") or [])[:3])] for k in d["keywords"]])
    return short, todo, det


def r_rank(o, lines, urls):
    d = jl(o[0]) if o else None
    if not d:
        return [], [], ""
    kw, m = d["keywords"], d["meta"]
    top3 = sum(1 for k in kw if k.get("position") and k["position"] <= 3)
    top10 = sum(1 for k in kw if k.get("position") and k["position"] <= 10)
    nf = sum(1 for k in kw if not k.get("position"))
    up = sorted([k for k in kw if (k.get("delta") or 0) > 0], key=lambda k: -k["delta"])
    down = sorted([k for k in kw if (k.get("delta") or 0) < 0], key=lambda k: k["delta"])
    short = [f"Google США: в топ-3 — {top3}, в топ-10 — {top10} из {len(kw)} запросов; не найдено в топ-100 — {nf}.",
             f"К базовой линии: выросли {len(up)}, упали {len(down)}.", f"Стоимость: ${m.get('cost_usd')}."]
    todo = [f"Разобрать падение «{k['keyword']}»: {k['baseline_position']} → {k['position']}." for k in down[:5]]
    det = table(["Запрос", "Позиция", "Было", "Δ", "Страница"], [[k["keyword"], k.get("position") or "—", k.get("baseline_position") or "—", (f"+{k['delta']}" if (k.get("delta") or 0) > 0 else k.get("delta")) if k.get("delta") is not None else "", path_short(k.get("ranking_url") or "—")] for k in sorted(kw, key=lambda k: k.get("position") or 999)])
    return short, todo, det


def r_backlinks(o, lines, urls):
    d = jl(o[0]) if o else None
    if not d:
        return [], [], ""
    s = d["summaries"]
    us = s.get("bixbit.io", {})
    short = [f"bixbit.io: рейтинг {us.get('rank')} из 100, {n(us.get('referring_domains'))} ссылающихся доменов, {n(us.get('backlinks'))} ссылок, спам-оценка {us.get('backlinks_spam_score')}.",
             f"За {d['meta']['window_days']} дней: новых доменов {len(d.get('new_referring_domains') or [])}, потеряно {len(d.get('lost_referring_domains') or [])}.",
             f"Стоимость: ${d['meta'].get('cost_usd')}."]
    lost = sorted(d.get("lost_referring_domains") or [], key=lambda x: -(x.get("rank") or 0))
    todo = [f"Проверить потерю ссылки с {x['domain']} (рейтинг {x['rank']})." for x in lost[:5] if (x.get("rank") or 0) >= 10]
    det = "### Мы и конкуренты\n" + table(["Домен", "Рейтинг", "Ссыл. домены", "Ссылки", "Спам"], [[k, v.get("rank"), n(v.get("referring_domains")), n(v.get("backlinks")), v.get("backlinks_spam_score")] for k, v in s.items()])
    if lost:
        det += "\n### Потерянные домены\n" + table(["Домен", "Рейтинг", "Ссылок", "Спам"], [[x["domain"], x["rank"], x["backlinks"], x["spam_score"]] for x in lost[:20]])
    return short, todo, det


def r_stdout(o, lines, urls):
    """Команды без файла-результата (коннекторы, hreflang, алерты, переобход): пересказ вывода."""
    out = stdout(lines)
    short, todo = [], []
    for ln in out:
        s = ln.strip()
        m = re.match(r"^\[(OK|WARN|FAIL|SKIP)\]\s+(\S+)\s+\S+\s+(.*)$", s)
        if m:
            short.append(f"{m.group(2)}: {'работает' if m.group(1) == 'OK' else {'WARN': 'есть замечание', 'FAIL': 'НЕ работает', 'SKIP': 'не настроен'}[m.group(1)]} — {m.group(3)}")
            if m.group(1) == "FAIL":
                todo.append(f"Починить подключение {m.group(2)}.")
            continue
        m = re.match(r"^(P[0-3])\s+(.*)$", s)
        if m:
            short.append(f"{m.group(1)}: {m.group(2)}")
            if m.group(1) in ("P0", "P1"):
                todo.append(m.group(2))
            continue
        if re.search(r"итого|найдено|отправлено|квота|осталось|ошибок|ok|готово", s, re.I) and len(short) < 25:
            short.append(s)
    if not short:
        short = [x.strip() for x in out[-8:]]
    sent = next((int(m.group(1)) for x in out for m in [re.search(r"сообщений отправлено:\s*(\d+)", x)] if m), None)
    if sent == 0:
        short.append("В Telegram ничего не отправлено: новых P0/P1 нет и ничего не решилось. P2 и уже известные проблемы приходят только в сводке.")
    elif sent:
        short.append(f"В Telegram отправлено сообщений: {sent}.")
    return short, todo, ""


def r_quarterly(o, lines, urls):
    out = stdout(lines)
    path = next((x.split("-> ", 1)[1].strip() for x in out if x.startswith("-> ")), None)
    head = next((x.strip() for x in out if "квартал" in x and " vs " in x), "")
    summ = next((x.strip() for x in out if x.startswith("Google: клики")), "")
    short = [x for x in (head, summ) if x]
    if path:
        short.append(f"Отчёт с графиками и таблицами: [{path}](../../{path}) — откройте его в «Документах».")
    return short, [], ""


# ---------- «Что изменилось с прошлого запуска» ----------

def prev_of(path):
    """Предыдущий файл той же серии: data/x-2026-10-16.json → последний data/x-YYYY-MM-DD.json раньше по дате."""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", path or "")
    if not m:
        return None
    pat = path.replace(m.group(1), "????-??-??")
    cands = sorted(f for f in glob.glob(os.path.join(ROOT, pat)) if re.search(r"\d{4}-\d{2}-\d{2}", f) and
                   re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(f)).group(1) < m.group(1))
    return os.path.relpath(cands[-1], ROOT) if cands else None


def delta(new, old, kind="n"):
    if old in (None, 0) or new is None:
        return f"{n(new) if kind == 'n' else new}"
    d = new - old
    rel = d / old * 100 if old else 0
    arrow = "▲" if d > 0 else ("▼" if d < 0 else "=")
    if kind == "pct":
        return f"{new:.2f}% ({arrow} {d:+.2f} п.п.)"
    return f"{n(new)} ({arrow} {'+' if d > 0 else ''}{n(d)}, {rel:+.0f}%)"


def date_of(path):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", path or "")
    return m.group(1) if m else "?"


def ch_gsc(o):
    rows = []
    for p in o:
        q = prev_of(p)
        if not q:
            continue
        a, b = jl(p), jl(q)
        dims = ",".join(a["meta"].get("dimensions") or [])
        if dims == "country":
            ca, ia = sum(r["clicks"] for r in a["rows"]), sum(r["impressions"] for r in a["rows"])
            cb, ib = sum(r["clicks"] for r in b["rows"]), sum(r["impressions"] for r in b["rows"])
            rows += [["Клики Google (28 дн.)", n(cb), delta(ca, cb)], ["Показы Google", n(ib), delta(ia, ib)],
                     ["CTR", f"{cb / ib * 100:.2f}%" if ib else "—", delta(ca / ia * 100 if ia else 0, cb / ib * 100 if ib else 0, "pct")]]
            us_a = next((r for r in a["rows"] if r["country"] == "usa"), None); us_b = next((r for r in b["rows"] if r["country"] == "usa"), None)
            if us_a and us_b:
                rows.append(["Клики США", n(us_b["clicks"]), delta(us_a["clicks"], us_b["clicks"])])
        elif dims == "page":
            pa = {r["page"]: r["clicks"] for r in a["rows"]}; pb = {r["page"]: r["clicks"] for r in b["rows"]}
            mv = sorted(((u, pa.get(u, 0) - pb.get(u, 0)) for u in set(pa) | set(pb)), key=lambda x: x[1])
            for u, d in mv[:3]:
                if d < 0:
                    rows.append([f"Просела: {path_short(u)}", n(pb.get(u, 0)), delta(pa.get(u, 0), pb.get(u, 0))])
            for u, d in mv[::-1][:3]:
                if d > 0:
                    rows.append([f"Выросла: {path_short(u)}", n(pb.get(u, 0)), delta(pa.get(u, 0), pb.get(u, 0))])
    return rows, (date_of(prev_of(o[0])) if o and prev_of(o[0]) else None)


def ch_ga4(o):
    rows = []
    for p in o:
        q = prev_of(p)
        if not q:
            continue
        a, b = jl(p), jl(q)
        if a["meta"].get("preset") == "channels":
            sa, sb = sum(r["sessions"] for r in a["rows"]), sum(r["sessions"] for r in b["rows"])
            rows.append(["Сессии GA4 (28 дн.)", n(sb), delta(sa, sb)])
            for ch in ("Organic Search", "Direct", "Referral"):
                ra = next((r["sessions"] for r in a["rows"] if r["sessionDefaultChannelGroup"] == ch), None)
                rb = next((r["sessions"] for r in b["rows"] if r["sessionDefaultChannelGroup"] == ch), None)
                if ra is not None and rb is not None:
                    rows.append([f"— {ch}", n(rb), delta(ra, rb)])
            ka, kb = sum(r["keyEvents"] for r in a["rows"]), sum(r["keyEvents"] for r in b["rows"])
            rows.append(["Ключевые события", n(kb), delta(ka, kb)])
    return rows, (date_of(prev_of(o[0])) if o and prev_of(o[0]) else None)


def ch_bing(o):
    rows = []
    for p in o:
        q = prev_of(p)
        if not q:
            continue
        a, b = jl(p), jl(q)
        if a["meta"]["report"] == "crawl":
            la = sorted(a["data"], key=lambda r: r.get("Date", ""))[-1]; lb = sorted(b["data"], key=lambda r: r.get("Date", ""))[-1]
            if la.get("InIndex") and lb.get("InIndex"):
                rows.append(["Страниц в индексе Bing", n(lb["InIndex"]), delta(la["InIndex"], lb["InIndex"])])
    return rows, (date_of(prev_of(o[0])) if o and prev_of(o[0]) else None)


def ch_serp(o):
    if not o or not prev_of(o[0]):
        return [], None
    a, b = jl(o[0])["summary"], jl(prev_of(o[0]))["summary"]
    return [["Запросов с AI Overview", b["with_aio"], delta(a["with_aio"], b["with_aio"])],
            ["AI Overview цитирует bixbit", b["aio_cites_bixbit"], delta(a["aio_cites_bixbit"], b["aio_cites_bixbit"])],
            ["Featured snippet у bixbit", b["fs_bixbit"], delta(a["fs_bixbit"], b["fs_bixbit"])]], date_of(prev_of(o[0]))


def ch_backlinks(o):
    if not o or not prev_of(o[0]):
        return [], None
    a, b = jl(o[0])["summaries"].get("bixbit.io", {}), jl(prev_of(o[0]))["summaries"].get("bixbit.io", {})
    return [["Рейтинг ссылок (0–100)", b.get("rank"), delta(a.get("rank"), b.get("rank"))],
            ["Ссылающихся доменов", n(b.get("referring_domains")), delta(a.get("referring_domains"), b.get("referring_domains"))],
            ["Обратных ссылок", n(b.get("backlinks")), delta(a.get("backlinks"), b.get("backlinks"))]], date_of(prev_of(o[0]))


def ch_index(o):
    if not o or not prev_of(o[0]):
        return [], None
    a, b = jl(o[0])["summary"], jl(prev_of(o[0]))["summary"]
    return [["Ключевых страниц в индексе", b["pass"], delta(a["pass"], b["pass"])],
            ["Чужой canonical у Google", b.get("canonical_mismatch", 0), delta(a.get("canonical_mismatch", 0), b.get("canonical_mismatch", 0))]], date_of(prev_of(o[0]))


def ch_cannibal(o):
    if not o or not prev_of(o[0]):
        return [], None
    a, b = jl(o[0])["summary"], jl(prev_of(o[0]))["summary"]
    return [["Конфликты внутри языка", b["same_locale"], delta(a["same_locale"], b["same_locale"])],
            ["Конфликты между языками", b["cross_locale"], delta(a["cross_locale"], b["cross_locale"])]], date_of(prev_of(o[0]))


def ch_crawl(o):
    f = sorted(glob.glob(os.path.join(ROOT, "data/crawl-????-??-??/summary.json")))
    if len(f) < 2:
        return [], None
    a, b = json.load(open(f[-1])), json.load(open(f[-2]))
    sa, sb = a.get("status_codes", {}), b.get("status_codes", {})
    return [["HTML-страниц", n(b["html_pages"]), delta(a["html_pages"], b["html_pages"])],
            ["Индексируемых", n(b["indexable"]), delta(a["indexable"], b["indexable"])],
            ["Ответов 404", n(sb.get("404", 0)), delta(sa.get("404", 0), sb.get("404", 0))]], os.path.basename(os.path.dirname(f[-2]))[6:]


def ch_sitemap(o):
    if not o or not prev_of(o[0]):
        return [], None
    a, b = jl(o[0])["summary"], jl(prev_of(o[0]))["summary"]
    rows = [["URL в sitemap", n(b["urls"]), delta(a["urls"], b["urls"])]]
    if a.get("without_impressions") is not None and b.get("without_impressions") is not None:
        rows.append(["URL из sitemap без показов", n(b["without_impressions"]), delta(a["without_impressions"], b["without_impressions"])])
    return rows, date_of(prev_of(o[0]))


CHANGES = {"gsc": ch_gsc, "ga4": ch_ga4, "bing": ch_bing, "serp-features": ch_serp, "backlinks": ch_backlinks,
           "index-check": ch_index, "cannibal": ch_cannibal, "crawl": ch_crawl, "sitemap": ch_sitemap}


FORMATTERS = {"index-check": r_index_check, "yandex-health": r_yandex, "yandex-queries": r_yandex, "gsc": r_gsc, "ga4": r_ga4,
              "bing": r_bing, "snapshot": r_snapshot, "crawl": r_crawl, "cannibal": r_cannibal, "serp-features": r_serp_features,
              "rank": r_rank, "backlinks": r_backlinks, "sitemap": r_sitemap, "site-diff": r_site_diff,
              "quarterly": r_quarterly, "quarterly-qtd": r_quarterly}


def build(cmd, title, status, lines, started=None, ended=None, urls=None):
    """Пишет reports/runs/<дата>-<cmd>.md и возвращает относительный путь."""
    import sys
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    started = started or dt.datetime.now().timestamp()
    day = dt.datetime.fromtimestamp(started)
    o = outs(lines)
    try:
        short, todo, det = FORMATTERS.get(cmd, r_stdout)(o, lines, urls or [])
    except Exception as e:  # отчёт не должен ронять запуск
        short, todo, det = [], [], f"Не удалось разобрать результат: `{type(e).__name__}: {e}`. Смотрите технический лог ниже.\n"
    if status == "error":
        short.insert(0, "Команда завершилась с ошибкой — данные ниже могут быть неполными или устаревшими.")
        err = [x for x in stdout(lines) if re.search(r"error|ошибк|traceback|failed|denied|403|401|500", x, re.I)]
        todo.insert(0, "Посмотреть ошибку в логе: " + (err[-1].strip()[:200] if err else "см. технический лог") + ".")
    dur = f"{(ended - started) / 60:.1f} мин" if ended and started else "—"
    md = [f"# {title} — {day:%d.%m.%Y}", "",
          f"> Запуск {day:%d.%m.%Y %H:%M} · длительность {dur} · результат: **{STATUS_RU.get(status, status)}**" + (f" · URL: {len(urls)}" if urls else ""), "",
          "## Коротко", ""] + [f"- {s}" for s in (short or ["Команда отработала, содержательных данных в выводе нет."])] + [""]
    if todo:
        md += ["## Что сделать", ""] + [f"{i}. {t}" for i, t in enumerate(todo[:12], 1)] + [""]
    if cmd in CHANGES:
        try:
            crow, since = CHANGES[cmd](o)
        except Exception as e:  # сравнение не должно ронять отчёт
            crow, since = [], f"ошибка сравнения: {type(e).__name__}"
        md += ["## Что изменилось с прошлого запуска", ""]
        if crow:
            md += [f"Сравнение с запуском от {since}.", "", table(["Показатель", "Было", "Стало"], crow), ""]
        else:
            md += ["Прошлого запуска для сравнения нет — сравнение появится со следующего." if not since or "ошибка" not in str(since) else str(since), ""]
    if det.strip():
        md += ["## Подробности", "", det.strip(), ""]
    if o:
        md += ["## Данные", ""] + [f"- `{p}`" for p in o] + [""]
    tail = stdout(lines)[-40:]
    if tail:
        md += ["## Технический лог (последние строки)", "", "```", *[x[:300] for x in tail], "```", ""]
    rel = f"{OUT_DIR}/{day:%Y-%m-%d}-{cmd}.md"
    os.makedirs(os.path.join(ROOT, OUT_DIR), exist_ok=True)
    open(os.path.join(ROOT, rel), "w", encoding="utf-8").write("\n".join(md))
    return rel
