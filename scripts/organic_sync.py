#!/usr/bin/env python3
"""organic_sync.py — органика из Google Search Console + GA4 → дашборд (Supabase).

Для квартала (по умолчанию — текущий) по каждой языковой версии сайта
(RU = /ru…, ES = /es…, EN = всё остальное на bixbit.io) пишет в
payload.periods["from|to"].organic[lang]:
  google  — показы/клики (GSC), время на сайте, отказы, конверсии (GA4, Organic Search / google)
  итоги   — google + yandex (yandex — ручной ввод в дашборде, не трогаем)
  pages   — топ-10 страниц по кликам: показы, клики, позиция (GSC) + время/отказы/конверсии (GA4)

Остальные данные дашборда (реклама, другие периоды, history, positions) не меняются.

Примеры:
  ./scripts/organic_sync.py                      # текущий квартал
  ./scripts/organic_sync.py --quarter 2026-Q1    # прошлый квартал (только если он пустой)
  ./scripts/organic_sync.py --quarter 2026-Q3 --overwrite
  ./scripts/organic_sync.py --dry-run            # посчитать и показать, ничего не записывать

Секреты: GOOGLE_APPLICATION_CREDENTIALS, GSC_SITE_URL, GA4_PROPERTY_ID (.env или окружение),
SUPABASE_URL, SUPABASE_ANON_KEY (окружение).
"""
import argparse, datetime as dt, json, os, sys, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, google_token, load_env  # noqa: E402

TABLE, ROW = "dashboard_state", "bixbit"
LANGS = ("ru", "en", "es")
GSC_LAG_DAYS = 3


# ── helpers ──────────────────────────────────────────────────────────────────
def lang_of(url):
    path = urllib.parse.urlparse(url).path if "://" in url else url
    path = "/" + path.lstrip("/")
    for lg in ("ru", "es"):
        if path == f"/{lg}" or path.startswith(f"/{lg}/"):
            return lg
    return "en"


def norm_path(url):
    path = urllib.parse.urlparse(url).path if "://" in url else url.split("?")[0]
    path = "/" + path.strip("/")
    return path


def fmt_time(sec):
    sec = int(round(sec or 0))
    return f"{sec // 60}:{sec % 60:02d}"


def parse_time(t):
    if isinstance(t, (int, float)):
        return float(t)
    p = str(t or "0").split(":")
    try:
        return int(p[0]) * 60 + int(p[1]) if len(p) == 2 else float(p[0])
    except ValueError:
        return 0.0


def num(v):
    try:
        return float(v or 0)
    except (TypeError, ValueError):
        return 0.0


def quarter_bounds(spec, today):
    if spec:
        y, q = spec.upper().split("-Q")
        y, q = int(y), int(q)
    else:
        y, q = today.year, (today.month - 1) // 3 + 1
    start = dt.date(y, 3 * (q - 1) + 1, 1)
    end = dt.date(y + (q == 4), (3 * q) % 12 + 1, 1) - dt.timedelta(days=1)
    return start, end


def http_json(req, what):
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            body = r.read()
            return json.loads(body) if body else None
    except urllib.error.HTTPError as e:
        sys.exit(f"{what} error {e.code}: {e.read().decode(errors='replace')[:300]}")


# ── Google ───────────────────────────────────────────────────────────────────
def gsc_pages(token, site, start, end):
    url = ("https://www.googleapis.com/webmasters/v3/sites/"
           f"{urllib.parse.quote(site, safe='')}/searchAnalytics/query")
    rows, start_row = [], 0
    while True:
        body = {"startDate": start, "endDate": end, "dimensions": ["page"], "type": "web",
                "rowLimit": 25000, "startRow": start_row, "dataState": "final"}
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={
            "Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        batch = (http_json(req, "GSC API") or {}).get("rows", [])
        rows += batch
        start_row += len(batch)
        if len(batch) < 25000:
            break
    return [{"page": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"],
             "position": r["position"]} for r in rows]


def ga4_landing(token, prop, start, end):
    body = {"dateRanges": [{"startDate": start, "endDate": end}],
            "dimensions": [{"name": "landingPage"}],
            "metrics": [{"name": m} for m in ("sessions", "averageSessionDuration", "bounceRate", "keyEvents")],
            "dimensionFilter": {"andGroup": {"expressions": [
                {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}},
                {"filter": {"fieldName": "sessionSource", "stringFilter": {"value": "google"}}}]}},
            "limit": 100000}
    req = urllib.request.Request(f"https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport",
                                 data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    d = http_json(req, "GA4 API") or {}
    out = []
    for r in d.get("rows", []):
        lp = r["dimensionValues"][0]["value"]
        s, dur, br, ke = (float(v["value"]) for v in r["metricValues"])
        out.append({"page": lp, "sessions": s, "duration": dur, "bounce": br, "conversions": ke})
    return out


def build_organic(gsc, ga4):
    """→ {lang: {"google": {...}, "pages": [...]}}"""
    ga_by_path = {}
    for r in ga4:
        if r["page"] in ("(not set)", ""):
            continue
        a = ga_by_path.setdefault(norm_path(r["page"]), {"sessions": 0, "dur": 0, "bounce": 0, "conv": 0})
        a["sessions"] += r["sessions"]
        a["dur"] += r["duration"] * r["sessions"]
        a["bounce"] += r["bounce"] * r["sessions"]
        a["conv"] += r["conversions"]

    res = {}
    for lg in LANGS:
        g_rows = [r for r in gsc if lang_of(r["page"]) == lg]
        a_rows = {p: v for p, v in ga_by_path.items() if lang_of(p) == lg}
        sess = sum(v["sessions"] for v in a_rows.values())
        google = {
            "impressions": int(sum(r["impressions"] for r in g_rows)),
            "clicks": int(sum(r["clicks"] for r in g_rows)),
            "time_on_site": fmt_time(sum(v["dur"] for v in a_rows.values()) / sess if sess else 0),
            "bounce": round(sum(v["bounce"] for v in a_rows.values()) / sess * 100, 1) if sess else 0,
            "conversions": int(sum(v["conv"] for v in a_rows.values())),
        }
        pages = []
        for r in sorted(g_rows, key=lambda x: (-x["clicks"], -x["impressions"]))[:10]:
            a = a_rows.get(norm_path(r["page"]))
            pg = {"url": r["page"], "clicks": int(r["clicks"]), "impressions": int(r["impressions"]),
                  "pos": round(r["position"], 1)}
            if a and a["sessions"]:
                pg.update(avgTime=fmt_time(a["dur"] / a["sessions"]),
                          bounceRate=round(a["bounce"] / a["sessions"] * 100, 1),
                          conversions=int(a["conv"]))
            pages.append(pg)
        res[lg] = {"google": google, "pages": pages}
    return res


def merge_totals(google, yandex):
    srcs = [s for s in (google, yandex or {}) if num(s.get("impressions")) or num(s.get("clicks"))]
    tot = {k: int(sum(num(s.get(k)) for s in srcs)) for k in ("impressions", "clicks", "conversions")}
    w = sum(num(s.get("clicks")) or 1 for s in srcs) or 1
    tot["bounce"] = round(sum(num(s.get("bounce")) * (num(s.get("clicks")) or 1) for s in srcs) / w, 1) if srcs else 0
    tot["time_on_site"] = fmt_time(sum(parse_time(s.get("time_on_site")) * (num(s.get("clicks")) or 1) for s in srcs) / w) if srcs else "0:00"
    return tot


# ── Supabase ─────────────────────────────────────────────────────────────────
def sb_headers(key):
    return {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def sb_load(url, key):
    req = urllib.request.Request(f"{url}/rest/v1/{TABLE}?project=eq.{ROW}&select=payload", headers=sb_headers(key))
    rows = http_json(req, "Supabase load") or []
    if not rows or not rows[0].get("payload"):
        sys.exit(f'Supabase: строка "{ROW}" не найдена или пустая — запись отменена, чтобы не потерять данные')
    return rows[0]["payload"]


def sb_save(url, key, payload):
    body = json.dumps({"payload": payload, "updated_at": dt.datetime.now(dt.timezone.utc).isoformat()}).encode()
    req = urllib.request.Request(f"{url}/rest/v1/{TABLE}?project=eq.{ROW}", data=body, method="PATCH",
                                 headers={**sb_headers(key), "Prefer": "return=minimal"})
    http_json(req, "Supabase save")


def has_google_data(org):
    return any(num((org.get(lg) or {}).get("google", {}).get(k)) for lg in LANGS for k in ("impressions", "clicks"))


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--quarter", help="напр. 2026-Q1; по умолчанию текущий")
    p.add_argument("--overwrite", action="store_true", help="перезаписать Google-данные прошлого квартала, если они уже есть")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    env = load_env(a.env) if os.path.exists(a.env) else {}
    env.update({k: v for k, v in os.environ.items() if k.startswith(("GSC_", "GA4_", "GOOGLE_", "SUPABASE_"))})
    need = ["GOOGLE_APPLICATION_CREDENTIALS", "GSC_SITE_URL", "GA4_PROPERTY_ID"] + ([] if a.dry_run else ["SUPABASE_URL", "SUPABASE_ANON_KEY"])
    missing = [k for k in need if not env.get(k)]
    if missing:
        sys.exit("Не заданы: " + ", ".join(missing))

    today = dt.date.today()
    q_start, q_end = quarter_bounds(a.quarter, today)
    is_current = q_start <= today <= q_end
    gsc_end = min(q_end, today - dt.timedelta(days=GSC_LAG_DAYS))
    ga_end = min(q_end, today - dt.timedelta(days=1))
    if gsc_end < q_start:
        print(f"Квартал {q_start}..{q_end}: данных GSC ещё нет (лаг {GSC_LAG_DAYS} дня) — пропуск")
        return
    pkey = f"{q_start.isoformat()}|{q_end.isoformat()}"

    tok_gsc = google_token(env["GOOGLE_APPLICATION_CREDENTIALS"], ["https://www.googleapis.com/auth/webmasters.readonly"])
    tok_ga = google_token(env["GOOGLE_APPLICATION_CREDENTIALS"], ["https://www.googleapis.com/auth/analytics.readonly"])
    gsc = gsc_pages(tok_gsc, env["GSC_SITE_URL"], q_start.isoformat(), gsc_end.isoformat())
    ga4 = ga4_landing(tok_ga, env["GA4_PROPERTY_ID"], q_start.isoformat(), ga_end.isoformat())
    built = build_organic(gsc, ga4)

    print(f"Период {pkey}: GSC {q_start}..{gsc_end} ({len(gsc)} страниц), GA4 {q_start}..{ga_end} ({len(ga4)} строк)")
    for lg in LANGS:
        g = built[lg]["google"]
        print(f"  {lg.upper()}: показы {g['impressions']}, клики {g['clicks']}, время {g['time_on_site']}, "
              f"отказы {g['bounce']}%, конверсии {g['conversions']}, топ-страниц {len(built[lg]['pages'])}")
    if a.dry_run:
        print("dry-run: в Supabase ничего не записано")
        return

    payload = sb_load(env["SUPABASE_URL"], env["SUPABASE_ANON_KEY"])
    period = payload.setdefault("periods", {}).setdefault(pkey, {})
    org = period.setdefault("organic", {})
    if not is_current and has_google_data(org) and not a.overwrite:
        sys.exit(f"{pkey}: Google-данные органики уже есть — добавьте --overwrite, чтобы перезаписать")

    synced = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    for lg in LANGS:
        cur = org.setdefault(lg, {})
        cur["google"] = built[lg]["google"]
        cur.update(merge_totals(cur["google"], cur.get("yandex")))
        cur["pages"] = built[lg]["pages"]
        cur["synced"] = {"source": "gsc+ga4", "gsc_end": gsc_end.isoformat(), "ga4_end": ga_end.isoformat(), "at": synced}
    payload["lastUpdated"] = {**(payload.get("lastUpdated") or {}), "organic": synced}
    sb_save(env["SUPABASE_URL"], env["SUPABASE_ANON_KEY"], payload)
    print(f"✓ Записано в Supabase: periods[{pkey}].organic (ru/en/es)")


if __name__ == "__main__":
    main()
