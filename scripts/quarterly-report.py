#!/usr/bin/env python3
"""quarterly-report.py — квартальный SEO-отчёт (HTML) с графиками, таблицами и сравнением с прошлым кварталом.

Данные: Google Search Console (по дням, страны, страницы, запросы, позиции отслеживаемых ключей),
GA4 (каналы), Bing (показы/клики по дням), снимки из data/ за квартал: AI Overview (serp-features),
позиции DataForSEO, индексация ключевых страниц, ссылки, краул.
Графики — встроенный SVG (без скриптов), отчёт открывается в браузере и в хабе команды.

Примеры:
  ./scripts/quarterly-report.py                         # последний завершённый квартал
  ./scripts/quarterly-report.py --quarter 2026Q3
  ./scripts/quarterly-report.py --quarter 2026Q4 --to-date   # текущий квартал на сегодня vs тот же период прошлого
  ./scripts/quarterly-report.py --quarter 2026Q3 --formats html,pdf,xlsx,md   # + PDF, Excel, Markdown
Выход: reports/quarterly-<год>-Q<n>.html (+ .pdf/.xlsx/.md), сырые выгрузки — data/quarterly/<год>-Q<n>/.
"""
import argparse, datetime as dt, glob, html, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import ROOT  # noqa: E402

MONTHS = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
ROMAN = ["I", "II", "III", "IV"]
CUR, PREV = "#d1127d", "#9a909c"


# ---------- периоды ----------

def quarter_bounds(year, q):
    start = dt.date(year, 3 * (q - 1) + 1, 1)
    end = (dt.date(year + (q == 4), (3 * q) % 12 + 1, 1) - dt.timedelta(days=1))
    return start, end


def prev_quarter(year, q):
    return (year - 1, 4) if q == 1 else (year, q - 1)


def esc(x):
    return html.escape(str(x))


def n(x, d=0):
    if x is None:
        return "—"
    return f"{x:,.{d}f}".replace(",", " ")


def dlt(cur, prev, kind="n", inverse=False):
    """Δ в процентах (или п.п./позиции) с цветом: зелёный — лучше, красный — хуже."""
    if cur is None or prev in (None, 0):
        return '<span class="d0">нет данных за прошлый квартал</span>' if prev in (None, 0) else ""
    diff = cur - prev
    good = (diff < 0) if inverse else (diff > 0)
    cls = "d0" if abs(diff) < 1e-9 else ("dp" if good else "dn")
    if kind == "pp":
        txt = f"{diff:+.2f} п.п."
    elif kind == "pos":
        txt = f"{diff:+.1f}"
    else:
        txt = f"{diff / prev * 100:+.0f}%"
    return f'<span class="{cls}">{"▲" if diff > 0 else "▼" if diff < 0 else "="} {txt}</span>'


# ---------- выгрузки ----------

def run(cmd):
    p = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print("  " + (p.stdout.strip().splitlines() or ["(нет вывода)"])[-1][:160])
    return p.returncode == 0


def gsc(cache, tag, start, end, dims, extra=()):
    path = os.path.join(cache, f"gsc-{tag}-{dims.replace(',', '_')}.json")
    if not os.path.exists(path):
        run(["./scripts/gsc-query.py", "--start", start.isoformat(), "--end", end.isoformat(), "--dimensions", dims, "--out", path, *extra])
    try:
        return json.load(open(path))["rows"]
    except Exception:
        return None


def ga4(cache, tag, start, end):
    path = os.path.join(cache, f"ga4-{tag}-channels.json")
    if not os.path.exists(path):
        run(["./scripts/ga4-query.py", "--preset", "channels", "--start", start.isoformat(), "--end", end.isoformat(), "--out", path])
    try:
        return json.load(open(path))["rows"]
    except Exception:
        return None


def bing_daily(cache):
    path = os.path.join(cache, "bing-traffic.json")
    if not os.path.exists(path):
        run(["./scripts/bing-query.py", "--report", "traffic", "--out", path])
    try:
        return {r["Date"][:10]: r for r in json.load(open(path))["data"]}
    except Exception:
        return None


def snapshots(pattern, start, end):
    res = []
    for f in sorted(glob.glob(os.path.join(ROOT, pattern))):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(f))
        if m and start.isoformat() <= m.group(1) <= end.isoformat():
            try:
                res.append((m.group(1), json.load(open(f))))
            except Exception:
                pass
    return res


# ---------- SVG ----------

def line_chart(series, labels, height=220, width=760, fmt=lambda v: n(v), title=""):
    """series: [(название, [значения], цвет, пунктир?)]; labels — подписи по оси X."""
    vals = [v for _, s, _, _ in series for v in s if v is not None]
    if not vals:
        return '<p class="muted">Нет данных для графика.</p>'
    top = max(vals) * 1.12 or 1
    L, R, T, B = 56, 30, 14, 34
    w, h = width - L - R, height - T - B
    npts = max(len(s) for _, s, _, _ in series)
    x = lambda i: L + (w * i / max(1, npts - 1))
    y = lambda v: T + h - h * v / top
    out = [f'<svg viewBox="0 0 {width} {height}" class="chart" role="img">']
    for k in range(5):
        gv = top * k / 4
        out.append(f'<line x1="{L}" x2="{width - R}" y1="{y(gv):.1f}" y2="{y(gv):.1f}" class="grid"/>'
                   f'<text x="{L - 6}" y="{y(gv) + 4:.1f}" class="ax" text-anchor="end">{esc(fmt(gv))}</text>')
    step = max(1, npts // 7)
    for i in range(0, npts, step):
        if i < len(labels):
            out.append(f'<text x="{x(i):.1f}" y="{height - 10}" class="ax" text-anchor="middle">{esc(labels[i])}</text>')
    for name, s, color, dash in series:
        pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(s) if v is not None)
        out.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.4"'
                   + (' stroke-dasharray="5 4"' if dash else "") + ' stroke-linejoin="round"/>')
        for i, v in enumerate(s):
            if v is not None:
                out.append(f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="2.6" fill="{color}"><title>{esc(name)}: {esc(fmt(v))}</title></circle>')
    out.append("</svg>")
    leg = "".join(f'<span><i style="background:{c}{";opacity:.7" if d else ""}"></i>{esc(nm)}</span>' for nm, _, c, d in series)
    # скрытая таблица с данными графика — для выгрузки в Excel / Markdown
    data = (f'<table class="chartdata" data-title="{esc(title)}" hidden><tr><th>Период</th>' + "".join(f"<th>{esc(nm)}</th>" for nm, _, _, _ in series) + "</tr>"
            + "".join("<tr><td>" + esc(labels[i] if i < len(labels) else i + 1) + "</td>" + "".join(f"<td>{n(s[i]) if i < len(s) and s[i] is not None else ''}</td>" for _, s, _, _ in series) + "</tr>"
                      for i in range(max(len(s) for _, s, _, _ in series))) + "</table>")
    return f'<div class="legend">{leg}</div>' + "".join(out) + data


def bars(rows, cur_name, prev_name, width=760):
    """rows: [(подпись, прошлый, текущий)] — горизонтальные парные столбцы."""
    if not rows:
        return '<p class="muted">Нет данных.</p>'
    top = max(max(p or 0, c or 0) for _, p, c in rows) or 1
    L, bh, gap = 190, 11, 10
    height = len(rows) * (2 * bh + gap) + 10
    w = width - L - 70
    out = [f'<svg viewBox="0 0 {width} {height}" class="chart" role="img">']
    for i, (lbl, p, c) in enumerate(rows):
        y0 = 4 + i * (2 * bh + gap)
        out.append(f'<text x="{L - 8}" y="{y0 + bh + 4}" class="ax lbl" text-anchor="end">{esc(lbl[:30])}</text>')
        for j, (v, col) in enumerate(((p, PREV), (c, CUR))):
            bw = w * (v or 0) / top
            out.append(f'<rect x="{L}" y="{y0 + j * bh}" width="{max(bw, 1):.1f}" height="{bh - 1}" fill="{col}" rx="2">'
                       f'<title>{esc(prev_name if j == 0 else cur_name)}: {n(v)}</title></rect>'
                       f'<text x="{L + bw + 5:.1f}" y="{y0 + j * bh + bh - 2}" class="ax">{n(v)}</text>')
    out.append("</svg>")
    return f'<div class="legend"><span><i style="background:{PREV}"></i>{esc(prev_name)}</span><span><i style="background:{CUR}"></i>{esc(cur_name)}</span></div>' + "".join(out)


def table(head, rows, cls=""):
    return (f'<div class="tw"><table class="{cls}"><thead><tr>' + "".join(f"<th>{esc(h)}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


# ---------- расчёты ----------

def weekly(daily, start, end, key):
    """Суммы по неделям квартала (неделя 1 = первые 7 дней квартала)."""
    weeks = []
    d = start
    while d <= end:
        s = 0
        for i in range(7):
            day = d + dt.timedelta(days=i)
            if day > end:
                break
            s += (daily.get(day.isoformat()) or {}).get(key, 0)
        if (end - d).days + 1 < 4 and weeks:  # хвост квартала короче 4 дней — добавляем к последней неделе
            weeks[-1] += s
        else:
            weeks.append(s)
        d += dt.timedelta(days=7)
    return weeks


def totals(rows):
    if not rows:
        return None
    c = sum(r["clicks"] for r in rows); i = sum(r["impressions"] for r in rows)
    pos = sum(r["position"] * r["impressions"] for r in rows) / i if i else None
    return {"clicks": c, "impressions": i, "ctr": c / i * 100 if i else 0, "position": pos}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quarter", help="например 2026Q3; по умолчанию — последний завершённый")
    ap.add_argument("--to-date", action="store_true", help="текущий квартал на сегодня vs тот же отрезок прошлого квартала")
    ap.add_argument("--out")
    ap.add_argument("--refresh", action="store_true", help="перекачать выгрузки (иначе берутся из кэша data/quarterly/)")
    ap.add_argument("--formats", default="html", help="через запятую: html,pdf,xlsx,md (HTML создаётся всегда)")
    a = ap.parse_args()

    today = dt.date.today()
    if a.quarter:
        m = re.fullmatch(r"(\d{4})Q([1-4])", a.quarter.upper())
        if not m:
            sys.exit("--quarter в формате 2026Q3")
        year, q = int(m.group(1)), int(m.group(2))
    else:
        cy, cq = today.year, (today.month - 1) // 3 + 1
        year, q = (cy, cq) if a.to_date else prev_quarter(cy, cq)
    start, end = quarter_bounds(year, q)
    py, pq = prev_quarter(year, q)
    pstart, pend = quarter_bounds(py, pq)
    gsc_last = today - dt.timedelta(days=3)  # лаг данных GSC
    if a.to_date or end > gsc_last:
        end = min(end, gsc_last)
        pend = min(pend, pstart + (end - start))
    label = f"{ROMAN[q - 1]} квартал {year}"
    plabel = f"{ROMAN[pq - 1]} квартал {py}"
    period = f"{start:%d.%m.%Y} — {end:%d.%m.%Y}"
    pperiod = f"{pstart:%d.%m.%Y} — {pend:%d.%m.%Y}"
    cache = os.path.join(ROOT, "data/quarterly", f"{year}-Q{q}" + ("-to-date" if a.to_date else ""))
    if a.refresh and os.path.isdir(cache):
        for f in glob.glob(os.path.join(cache, "*.json")):
            os.remove(f)
    os.makedirs(cache, exist_ok=True)
    print(f"{label}: {period} vs {plabel}: {pperiod}")

    # --- Google ---
    print("GSC…")
    d_cur = {r["date"]: r for r in (gsc(cache, "cur", start, end, "date") or [])}
    d_prev = {r["date"]: r for r in (gsc(cache, "prev", pstart, pend, "date") or [])}
    t_cur, t_prev = totals(list(d_cur.values())), totals(list(d_prev.values()))
    c_cur = gsc(cache, "cur", start, end, "country") or []
    c_prev = gsc(cache, "prev", pstart, pend, "country") or []
    p_cur = gsc(cache, "cur", start, end, "page") or []
    p_prev = gsc(cache, "prev", pstart, pend, "page") or []
    q_cur = gsc(cache, "cur", start, end, "query") or []
    q_prev = gsc(cache, "prev", pstart, pend, "query") or []
    # --- GA4, Bing ---
    print("GA4…")
    g_cur, g_prev = ga4(cache, "cur", start, end), ga4(cache, "prev", pstart, pend)
    print("Bing…")
    bd = bing_daily(cache) or {}
    b_cur = {k: v for k, v in bd.items() if start.isoformat() <= k <= end.isoformat()}
    b_prev = {k: v for k, v in bd.items() if pstart.isoformat() <= k <= pend.isoformat()}
    bt = lambda d, k: sum(v.get(k, 0) for v in d.values()) if d else None

    # --- снимки за квартал ---
    serp = snapshots("data/serp-features/serp-features-*.json", start, end)
    serp_p = snapshots("data/serp-features/serp-features-*.json", pstart, pend)
    ranks = snapshots("data/rank-tracking/rank-*.json", start, end) + snapshots("data/rank-tracking/baseline-*.json", start, end)
    idx = snapshots("data/index-check/index-*.json", start, end)
    bl = snapshots("data/backlinks/backlinks-*.json", start, end)
    bl_p = snapshots("data/backlinks/backlinks-*.json", pstart, pend)
    crawls = [(os.path.basename(os.path.dirname(f))[6:], json.load(open(f))) for f in sorted(glob.glob(os.path.join(ROOT, "data/crawl-????-??-??/summary.json")))
              if start.isoformat() <= os.path.basename(os.path.dirname(f))[6:] <= end.isoformat()]
    tracked = []
    base = sorted(glob.glob(os.path.join(ROOT, "data/rank-tracking/baseline-*.json")))
    if base:
        tracked = [k["keyword"] for k in json.load(open(base[-1]))["keywords"]]

    # ---------- HTML ----------
    css = """
:root{--bg:#f7f5f8;--card:#fff;--line:#e3dce4;--text:#1d1820;--muted:#665c69;--accent:#d1127d;--ok:#1f8a55;--bad:#c23333}
@media (prefers-color-scheme:dark){:root{--bg:#151216;--card:#1e1a20;--line:#3a333d;--text:#f4f1f5;--muted:#b3a9b6;--ok:#3fbf7f;--bad:#ef5a5a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 Inter,system-ui,-apple-system,Segoe UI,sans-serif;padding:0 16px 60px}
.wrap{max-width:980px;margin:0 auto}h1,h2,h3{font-family:Onest,Inter,system-ui,sans-serif;line-height:1.2}
h1{font-size:28px;margin:28px 0 4px}h2{font-size:21px;margin:34px 0 8px;padding-top:6px;border-top:1px solid var(--line)}h3{font-size:16px;margin:20px 0 6px}
.muted,.note{color:var(--muted)}.note{font-size:13px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px;margin:16px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
.card .k{font-size:12.5px;color:var(--muted)}.card .v{font:700 24px/1.2 Onest,Inter,sans-serif;margin:4px 0}.card .s{font-size:12.5px;color:var(--muted)}
.dp{color:var(--ok);font-weight:600}.dn{color:var(--bad);font-weight:600}.d0{color:var(--muted)}
.chart{width:100%;height:auto;background:var(--card);border:1px solid var(--line);border-radius:12px;margin:4px 0 8px}
.chart .grid{stroke:var(--line);stroke-width:1}.chart .ax{fill:var(--muted);font-size:11px}.chart .lbl{fill:var(--text)}
.legend{display:flex;gap:16px;font-size:13px;color:var(--muted);margin:10px 0 2px}.legend i{display:inline-block;width:12px;height:4px;border-radius:2px;margin-right:6px;vertical-align:middle}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--card);margin:6px 0 10px}
table{border-collapse:collapse;width:100%;font-size:13.5px}th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:11.5px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}tr:last-child td{border-bottom:0}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
@media print{body{background:#fff}.chart,.card,.tw,.legend{break-inside:avoid}h2,h3,.legend{break-after:avoid}}
"""
    H = [f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         f'<title>SEO-отчёт BiXBiT — {esc(label)}</title>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@600;700&family=Inter:wght@400;600&display=swap">'
         f'<style>{css}</style></head><body><div class="wrap">',
         f'<h1>SEO-отчёт BiXBiT — {esc(label)}</h1>',
         f'<p class="muted">{esc(period)} · сравнение с: {esc(plabel)} ({esc(pperiod)}) · сформирован {today:%d.%m.%Y}</p>']

    # Ключевые цифры
    org = lambda rows: next((r["sessions"] for r in (rows or []) if r["sessionDefaultChannelGroup"] == "Organic Search"), None)
    cards = []
    if t_cur:
        cards += [("Клики из Google", n(t_cur["clicks"]), dlt(t_cur["clicks"], t_prev and t_prev["clicks"])),
                  ("Показы в Google", n(t_cur["impressions"]), dlt(t_cur["impressions"], t_prev and t_prev["impressions"])),
                  ("CTR Google", f'{t_cur["ctr"]:.2f}%', dlt(t_cur["ctr"], t_prev and t_prev["ctr"], "pp")),
                  ("Средняя позиция", n(t_cur["position"], 1), dlt(t_cur["position"], t_prev and t_prev["position"], "pos", inverse=True))]
    if org(g_cur) is not None:
        cards.append(("Органика GA4, сессии", n(org(g_cur)), dlt(org(g_cur), org(g_prev))))
    if b_cur:
        cards.append(("Клики из Bing", n(bt(b_cur, "Clicks")), dlt(bt(b_cur, "Clicks"), bt(b_prev, "Clicks"))))
    if serp:
        s = serp[-1][1]["summary"]
        cards.append(("AI Overview цитирует bixbit", f'{s["aio_cites_bixbit"]} из {s["with_aio"]}', f'<span class="d0">замер {serp[-1][0]}</span>'))
    if bl:
        s = bl[-1][1]["summaries"].get("bixbit.io", {})
        p = bl_p[-1][1]["summaries"].get("bixbit.io", {}) if bl_p else {}
        cards.append(("Ссылающихся доменов", n(s.get("referring_domains")), dlt(s.get("referring_domains"), p.get("referring_domains"))))
    H.append('<h2>Ключевые показатели</h2><div class="cards">' + "".join(
        f'<div class="card"><div class="k">{esc(k)}</div><div class="v">{v}</div><div class="s">{d}</div></div>' for k, v, d in cards) + "</div>")

    # Google: динамика
    H.append("<h2>Google: динамика по неделям</h2>")
    wk_lbl = [f"нед. {i + 1}" for i in range(len(weekly(d_cur, start, end, "clicks")))]
    H.append("<h3>Клики</h3>" + line_chart([(label, weekly(d_cur, start, end, "clicks"), CUR, False),
                                            (plabel, weekly(d_prev, pstart, pend, "clicks"), PREV, True)], wk_lbl, title="Google — клики по неделям"))
    H.append("<h3>Показы</h3>" + line_chart([(label, weekly(d_cur, start, end, "impressions"), CUR, False),
                                             (plabel, weekly(d_prev, pstart, pend, "impressions"), PREV, True)], wk_lbl, title="Google — показы по неделям"))
    H.append('<p class="note">Неделя 1 — первые 7 дней квартала; линии кварталов совмещены по номеру недели.</p>')

    # Страны
    cp = {r["country"]: r for r in c_prev}
    top_c = sorted(c_cur, key=lambda r: -r["clicks"])[:10]
    H.append("<h2>Google: страны</h2>" + bars([(r["country"].upper(), (cp.get(r["country"]) or {}).get("clicks", 0), r["clicks"]) for r in top_c], label, plabel))
    H.append(table(["Страна", "Клики", "Δ", "Показы", "CTR", "Позиция"],
                   [[esc(r["country"].upper()), n(r["clicks"]), dlt(r["clicks"], (cp.get(r["country"]) or {}).get("clicks")),
                     n(r["impressions"]), f'{r["ctr"] * 100:.2f}%', n(r["position"], 1)] for r in top_c]))

    # Страницы и запросы
    pp = {r["page"]: r for r in p_prev}
    top_p = sorted(p_cur, key=lambda r: -r["clicks"])[:15]
    short = lambda u: re.sub(r"^https?://(www\.)?bixbit\.io", "", u) or "/"
    H.append("<h2>Страницы: топ-15 по кликам</h2>" + table(["Страница", "Клики", "Было", "Δ", "Позиция"],
             [[esc(short(r["page"])[:80]), n(r["clicks"]), n((pp.get(r["page"]) or {}).get("clicks")), dlt(r["clicks"], (pp.get(r["page"]) or {}).get("clicks")), n(r["position"], 1)] for r in top_p]))
    qp = {r["query"]: r for r in q_prev}
    top_q = sorted(q_cur, key=lambda r: -r["clicks"])[:20]
    H.append("<h2>Запросы: топ-20 по кликам</h2>" + table(["Запрос", "Клики", "Было", "Δ", "Позиция", "Была"],
             [[esc(r["query"]), n(r["clicks"]), n((qp.get(r["query"]) or {}).get("clicks")), dlt(r["clicks"], (qp.get(r["query"]) or {}).get("clicks")),
               n(r["position"], 1), n((qp.get(r["query"]) or {}).get("position"), 1)] for r in top_q]))
    new_q = sorted((r for r in q_cur if r["query"] not in qp and r["impressions"] >= 50), key=lambda r: -r["impressions"])[:12]
    if new_q:
        H.append("<h3>Новые запросы квартала (не было в прошлом, от 50 показов)</h3>" + table(["Запрос", "Показы", "Клики", "Позиция"],
                 [[esc(r["query"]), n(r["impressions"]), n(r["clicks"]), n(r["position"], 1)] for r in new_q]))

    # Позиции
    H.append("<h2>Позиции по отслеживаемым запросам</h2>")
    if tracked:
        qc = {r["query"]: r for r in q_cur}
        rows, better, worse = [], 0, 0
        for k in tracked:
            c, p = qc.get(k), qp.get(k)
            if c and p:
                better += c["position"] < p["position"] - 0.5
                worse += c["position"] > p["position"] + 0.5
            rows.append([esc(k), n(p and p["position"], 1), n(c and c["position"], 1),
                         dlt(c and c["position"], p and p["position"], "pos", inverse=True) if c and p else '<span class="d0">—</span>',
                         n(c and c["impressions"]), n(c and c["clicks"])])
        H.append(f'<p>Средняя позиция в Google по данным Search Console (все страны): улучшилась по {better}, ухудшилась по {worse} из {len(tracked)} запросов.</p>')
        H.append(table(["Запрос", plabel, label, "Δ", "Показы", "Клики"], rows))
    if ranks:
        dte, r = sorted(ranks, key=lambda x: x[0])[-1]
        kw = r["keywords"]
        H.append(f'<h3>Google США, замер DataForSEO от {dte}</h3><p>В топ-3: {sum(1 for k in kw if k.get("position") and k["position"] <= 3)}, '
                 f'в топ-10: {sum(1 for k in kw if k.get("position") and k["position"] <= 10)} из {len(kw)}. '
                 'Замеров позиций США за прошлый квартал нет — сравнение по ним начнётся со следующего квартала.</p>')

    # AI-выдача
    H.append("<h2>AI-выдача: Google AI Overview</h2>")
    if serp:
        H.append(table(["Дата замера", "Запросов", "С AI Overview", "Цитирует bixbit", "Featured snippet bixbit", "«Люди также спрашивают»"],
                       [[d, s["summary"]["keywords"], s["summary"]["with_aio"], s["summary"]["aio_cites_bixbit"], s["summary"]["fs_bixbit"], s["summary"]["with_paa"]] for d, s in serp]))
        last = serp[-1][1]
        cited = [k["keyword"] for k in last["keywords"] if k.get("aio_cites_bixbit")]
        H.append(f'<p>В последнем замере AI Overview цитирует bixbit по запросам: {esc(", ".join(cited)) or "нет"}. '
                 f'Чаще всего цитируются: {esc(", ".join(last["summary"].get("top_aio_domains", [])[:6]))}.</p>')
        if not serp_p:
            H.append('<p class="note">Отслеживание AI Overview запущено в этом квартале — сравнения с прошлым нет. Ответы AI Overview нестабильны, выводы — по динамике нескольких замеров.</p>')
    else:
        H.append('<p class="muted">Замеров AI Overview за квартал нет.</p>')

    # GA4
    if g_cur:
        gp = {r["sessionDefaultChannelGroup"]: r for r in (g_prev or [])}
        top_g = sorted(g_cur, key=lambda r: -r["sessions"])[:8]
        H.append("<h2>Трафик сайта по каналам (GA4)</h2>" + bars([(r["sessionDefaultChannelGroup"], (gp.get(r["sessionDefaultChannelGroup"]) or {}).get("sessions", 0), r["sessions"]) for r in top_g], label, plabel))
        H.append(table(["Канал", "Сессии", "Δ", "Вовлечённые", "Ключевые события"],
                       [[esc(r["sessionDefaultChannelGroup"]), n(r["sessions"]), dlt(r["sessions"], (gp.get(r["sessionDefaultChannelGroup"]) or {}).get("sessions")),
                         n(r["engagedSessions"]), n(r["keyEvents"])] for r in top_g]))

    # Bing
    if b_cur:
        H.append("<h2>Bing</h2>")
        H.append(f'<p>Клики: {n(bt(b_cur, "Clicks"))} ({dlt(bt(b_cur, "Clicks"), bt(b_prev, "Clicks"))}), показы: {n(bt(b_cur, "Impressions"))} ({dlt(bt(b_cur, "Impressions"), bt(b_prev, "Impressions"))}).</p>')
        H.append(line_chart([(label, weekly(b_cur, start, end, "Clicks"), CUR, False), (plabel, weekly(b_prev, pstart, pend, "Clicks"), PREV, True)], wk_lbl, title="Bing — клики по неделям"))

    # Техническое состояние
    H.append("<h2>Техническое состояние</h2>")
    tech = []
    if idx:
        ok = [s["summary"]["pass"] for _, s in idx]; tot = [s["meta"]["urls"] for _, s in idx]
        tech.append(["Индексация ключевых страниц (Google)", f"{min(ok)}–{max(ok)} из {max(tot)} в индексе", f"{len(idx)} проверок за квартал"])
    for d, s in crawls:
        tech.append([f"Краул сайта {d}", f'{n(s["html_pages"])} HTML-страниц, индексируемых {n(s["indexable"])}', f'404: {n((s.get("status_codes") or {}).get("404", 0))}'])
    if bl:
        s = bl[-1][1]["summaries"].get("bixbit.io", {})
        tech.append([f"Ссылочный профиль {bl[-1][0]}", f'рейтинг {s.get("rank")}, доменов {n(s.get("referring_domains"))}', f'спам-оценка {s.get("backlinks_spam_score")}'])
    H.append(table(["Что", "Значение", "Комментарий"], tech) if tech else '<p class="muted">Снимков технического состояния за квартал нет.</p>')

    H.append("<h2>Методика</h2><ul class='note'>"
             "<li>Google — Search Console (данные «final», лаг 3 дня). Итоги по дням включают анонимизированные запросы, поэтому сумма по таблице запросов меньше итога.</li>"
             "<li>Средняя позиция — взвешена по показам. Позиции отслеживаемых запросов — средние по всем странам из Search Console.</li>"
             "<li>GA4 — каналы по умолчанию (sessionDefaultChannelGroup). Bing — Bing Webmaster Tools.</li>"
             "<li>AI Overview и позиции США — замеры DataForSEO (Google США, английский).</li>"
             f"<li>Сырые выгрузки отчёта — <code>{esc(os.path.relpath(cache, ROOT))}/</code>.</li></ul>")
    H.append("</div></body></html>")
    out = a.out or os.path.join(ROOT, "reports", f"quarterly-{year}-Q{q}" + ("-to-date" if a.to_date else "") + ".html")
    open(out, "w", encoding="utf-8").write("\n".join(H))
    extra = []
    fmts = [f for f in a.formats.split(",") if f.strip() and f.strip() != "html"]
    if fmts:
        import report_export
        for f in fmts:
            try:
                extra += report_export.export(out, [f])
            except Exception as e:  # один формат не должен ронять остальные
                print(f"формат {f}: не удалось — {e}")
    print(f"Google: клики {n(t_cur and t_cur['clicks'])} (было {n(t_prev and t_prev['clicks'])}), показы {n(t_cur and t_cur['impressions'])} "
          f"(было {n(t_prev and t_prev['impressions'])}); AI Overview замеров {len(serp)}; позиций DataForSEO {len(ranks)}")
    print(f"-> {os.path.relpath(out, ROOT)}")
    for f in extra:
        print(f"-> {os.path.relpath(f, ROOT)}")


if __name__ == "__main__":
    main()
