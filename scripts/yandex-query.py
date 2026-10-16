#!/usr/bin/env python3
"""yandex-query.py — Яндекс.Вебмастер API v4: выгрузка данных и переобход.

Токен: YANDEX_WEBMASTER_TOKEN в .env (OAuth, права webmaster:hostinfo; для переобхода
и добавления сайтов — webmaster:verify). Токен нигде не печатается.

Отчёты (--report):
  hosts        сайты аккаунта: host_id, подтверждён ли, главное зеркало
  summary      ИКС, страниц в поиске / исключено, число проблем по уровням
  diagnostics  проблемы сайта (FATAL / CRITICAL / POSSIBLE_PROBLEM / RECOMMENDATION)
  queries      популярные запросы: показы, клики, ср. позиция показа/клика (до 500)
  indexing     история обхода: HTTP 2xx/3xx/4xx/5xx по датам
  insearch     история числа страниц в поиске
  sitemaps     sitemap-файлы, известные Вебмастеру, и их ошибки
  links        внешние ссылки (примеры) + история их числа
  recrawl      квота на переобход (с --submit и --urls — отправка URL на переобход)

Примеры:
  ./scripts/yandex-query.py --report hosts
  ./scripts/yandex-query.py --report summary
  ./scripts/yandex-query.py --report queries --days 28 --out data/yandex-queries-2026-09-30.json
  ./scripts/yandex-query.py --report recrawl                       # только квота
  ./scripts/yandex-query.py --report recrawl --urls https://bixbit.io/ru/firmwares --submit
"""
import argparse, datetime as dt, json, os, sys, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, ROOT, load_env  # noqa: E402

API = "https://api.webmaster.yandex.net/v4"


class YW:
    def __init__(self, token):
        self.token = token

    def req(self, path, params=None, body=None):
        url = API + path + ("?" + urllib.parse.urlencode(params, doseq=True) if params else "")
        r = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None,
                                   method="POST" if body is not None else "GET",
                                   headers={"Authorization": f"OAuth {self.token}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(r, timeout=60, context=CTX) as resp:
                raw = resp.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:300].replace(self.token, "***")
            sys.exit(f"Yandex Webmaster API {e.code} {path.split('/hosts/')[-1]}: {msg}")
        except urllib.error.URLError as e:
            sys.exit(f"Yandex Webmaster API: сеть — {e.reason}")


def pick_host(hosts, want):
    """host_id bixbit.io: предпочтительно https, подтверждённый; bixbitusa.io — партнёры, не берём."""
    cands = [h for h in hosts if want in h.get("ascii_host_url", "") and "bixbitusa" not in h.get("ascii_host_url", "")]
    cands.sort(key=lambda h: (not h.get("verified"), not h["ascii_host_url"].startswith("https")))
    return cands[0] if cands else None


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--report", default="hosts",
                   choices=["hosts", "summary", "diagnostics", "queries", "indexing", "insearch", "sitemaps", "links", "recrawl"])
    p.add_argument("--host", default="bixbit.io", help="домен для выбора host_id (напр. bixbit.tech после переезда)")
    p.add_argument("--days", type=int, default=28)
    p.add_argument("--urls", help="через запятую — для --report recrawl --submit")
    p.add_argument("--submit", action="store_true", help="реально отправить URL на переобход")
    p.add_argument("--out")
    a = p.parse_args()

    tok = load_env(a.env).get("YANDEX_WEBMASTER_TOKEN")
    if not tok or tok.startswith("your_"):
        sys.exit("YANDEX_WEBMASTER_TOKEN не задан в .env")
    yw = YW(tok)
    uid = yw.req("/user")["user_id"]
    hosts = yw.req(f"/user/{uid}/hosts").get("hosts", [])
    if a.report == "hosts":
        data = hosts
        for h in hosts:
            print(f"  {h['host_id']:40} verified={h.get('verified')} main_mirror={(h.get('main_mirror') or {}).get('ascii_host_url', '—')}")
    else:
        h = pick_host(hosts, a.host)
        if not h:
            sys.exit(f"{a.host} не найден среди сайтов Вебмастера — добавьте и подтвердите сайт (webmaster.yandex.ru)")
        if not h.get("verified"):
            sys.exit(f"{h['ascii_host_url']} добавлен, но не подтверждён — данные недоступны")
        base = f"/user/{uid}/hosts/{urllib.parse.quote(h['host_id'], safe='')}"
        end = dt.date.today()
        start = end - dt.timedelta(days=a.days)
        dr = {"date_from": start.isoformat() + "T00:00:00+03:00", "date_to": end.isoformat() + "T00:00:00+03:00"}
        if a.report == "summary":
            data = yw.req(base + "/summary")
            print(f"  {h['ascii_host_url']}: ИКС {data.get('sqi')} · в поиске {data.get('searchable_pages_count')}"
                  f" · исключено {data.get('excluded_pages_count')} · проблемы {data.get('site_problems')}")
        elif a.report == "diagnostics":
            data = yw.req(base + "/diagnostics")
            for k, v in sorted((data.get("problems") or {}).items(), key=lambda x: x[1].get("severity", "")):
                if v.get("state") == "PRESENT":
                    print(f"  {v.get('severity'):16} {k}")
        elif a.report == "queries":
            data = yw.req(base + "/search-queries/popular", {
                "order_by": "TOTAL_SHOWS", "limit": 500, **dr,
                "query_indicator": ["TOTAL_SHOWS", "TOTAL_CLICKS", "AVG_SHOW_POSITION", "AVG_CLICK_POSITION"]})
            qs = data.get("queries", [])
            sh = sum(q["indicators"].get("TOTAL_SHOWS", 0) or 0 for q in qs)
            cl = sum(q["indicators"].get("TOTAL_CLICKS", 0) or 0 for q in qs)
            print(f"  запросов {len(qs)} · показы {sh:.0f} · клики {cl:.0f} ({start}..{end})")
            for q in qs[:15]:
                i = q["indicators"]
                print(f"   {q['query_text'][:55]:55} показы {i.get('TOTAL_SHOWS', 0):>6.0f} клики {i.get('TOTAL_CLICKS', 0):>4.0f} поз {i.get('AVG_SHOW_POSITION') or 0:.1f}")
        elif a.report == "indexing":
            data = yw.req(base + "/indexing/history", dr)
            for k, v in (data.get("indicators") or {}).items():
                print(f"  {k:10} посл. значение {v[-1]['value'] if v else '—'}")
        elif a.report == "insearch":
            data = yw.req(base + "/search-urls/in-search/history", dr)
            hist = data.get("history", [])
            print(f"  страниц в поиске: {hist[0]['value'] if hist else '—'} → {hist[-1]['value'] if hist else '—'}")
        elif a.report == "sitemaps":
            data = yw.req(base + "/sitemaps")
            for s in data.get("sitemaps", []):
                print(f"  {s.get('sitemap_url')} urls={s.get('urls_count')} errors={s.get('errors_count')} last={s.get('last_access_date')}")
        elif a.report == "links":
            data = {"samples": yw.req(base + "/links/external/samples", {"offset": 0, "limit": 100}),
                    "history": yw.req(base + "/links/external/history", {"indicator": "LINKS_TOTAL_COUNT"})}
            print(f"  внешних ссылок (пример): {data['samples'].get('count')}")
        elif a.report == "recrawl":
            q = yw.req(base + "/recrawl/quota")
            data = {"quota": q, "submitted": []}
            print(f"  квота переобхода: {q.get('quota_remainder')} из {q.get('daily_quota')} на сегодня")
            urls = [u.strip() for u in (a.urls or "").split(",") if u.strip()]
            if urls and not a.submit:
                print(f"  dry run: {len(urls)} URL не отправлены (добавьте --submit)")
            for u in (urls if a.submit else []):
                r = yw.req(base + "/recrawl/queue", body={"url": u})
                data["submitted"].append({"url": u, "task_id": r.get("task_id"), "quota_remainder": r.get("quota_remainder")})
                print(f"  → {u}: task {r.get('task_id')}, осталось {r.get('quota_remainder')}")
        data = {"host": h, "report": a.report, "window": [start.isoformat(), end.isoformat()], "data": data}
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        json.dump({"pulled_at": dt.datetime.now().isoformat(timespec="seconds"), **(data if isinstance(data, dict) else {"data": data})},
                  open(a.out, "w"), indent=1, ensure_ascii=False)
        print(f"  -> {os.path.relpath(os.path.abspath(a.out), ROOT)}")


if __name__ == "__main__":
    main()
