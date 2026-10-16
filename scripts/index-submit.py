#!/usr/bin/env python3
"""index-submit.py — отправка изменённых URL на переобход (Bing + IndexNow).

По умолчанию — DRY RUN (только показывает квоты и что будет отправлено).
Реальная отправка — только с флагом --submit.

- Bing Webmaster SubmitUrlBatch (ключ BING_WEBMASTER_API_KEY), квота — GetUrlSubmissionQuota.
- IndexNow (api.indexnow.org → Bing, Yandex, Seznam, Naver и др.). Нужны:
  INDEXNOW_KEY в .env и файл https://bixbit.io/<INDEXNOW_KEY>.txt с этим ключом
  (выкладывает разработчик). Без файла IndexNow не отправляется.
- Google: API переобхода для обычных страниц НЕТ (Indexing API — только JobPosting/
  BroadcastEvent). Для Google скрипт печатает ссылки URL Inspection для ручного
  «Запросить индексирование».

Примеры:
  ./scripts/index-submit.py --urls https://bixbit.io/en/firmwares,https://bixbit.io/en/ams
  ./scripts/index-submit.py --file changed-urls.txt --submit
"""
import argparse, json, os, sys, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ENV_PATH, load_env  # noqa: E402

BING = "https://ssl.bing.com/webmaster/api.svc/json/"


def req(url, body=None, method=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method=method or ("POST" if data else "GET"),
                               headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(r, timeout=60, context=CTX) as resp:
            raw = resp.read().decode(errors="replace")
            return resp.status, (json.loads(raw) if raw.strip().startswith(("{", "[")) else raw)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="replace")[:300]
    except urllib.error.URLError as e:
        return 0, str(e.reason)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=ENV_PATH)
    p.add_argument("--urls", help="через запятую")
    p.add_argument("--file", help="файл со списком URL (по одному в строке)")
    p.add_argument("--site", default="https://bixbit.io/")
    p.add_argument("--submit", action="store_true", help="реально отправить (иначе dry run)")
    a = p.parse_args()

    urls = []
    if a.urls:
        urls += [u.strip() for u in a.urls.split(",") if u.strip()]
    if a.file:
        urls += [l.strip() for l in open(a.file) if l.strip() and not l.startswith("#")]
    urls = [u for u in dict.fromkeys(urls) if u.startswith(a.site.rstrip("/"))]
    env = load_env(a.env)
    bing_key, inkey = env.get("BING_WEBMASTER_API_KEY"), env.get("INDEXNOW_KEY")
    host = urllib.parse.urlsplit(a.site).netloc
    print(f"{len(urls)} URL · режим: {'ОТПРАВКА' if a.submit else 'dry run'}")

    # --- Bing
    if bing_key:
        q = urllib.parse.urlencode({"apikey": bing_key, "siteUrl": a.site})
        code, d = req(f"{BING}GetUrlSubmissionQuota?{q}")
        quota = (d or {}).get("d", {}) if isinstance(d, dict) else {}
        print(f"Bing квота: {quota.get('DailyQuota', '?')}/день, {quota.get('MonthlyQuota', '?')}/мес (HTTP {code})")
        if a.submit and urls:
            batch = urls[: int(quota.get("DailyQuota") or len(urls))]
            code, d = req(f"{BING}SubmitUrlBatch?{urllib.parse.urlencode({'apikey': bing_key})}",
                          {"siteUrl": a.site, "urlList": batch})
            print(f"Bing SubmitUrlBatch: HTTP {code} · отправлено {len(batch)}"
                  + ("" if code == 200 else f" · {str(d).replace(bing_key, '***')[:200]}"))
    else:
        print("Bing: BING_WEBMASTER_API_KEY не задан")

    # --- IndexNow
    if inkey:
        key_url = f"https://{host}/{inkey}.txt"
        code, body = req(key_url)
        ok = code == 200 and isinstance(body, str) and body.strip() == inkey
        print(f"IndexNow ключ-файл {key_url}: {'OK' if ok else f'НЕ НАЙДЕН/не совпадает (HTTP {code})'}")
        if a.submit and urls and ok:
            code, d = req("https://api.indexnow.org/indexnow",
                          {"host": host, "key": inkey, "keyLocation": key_url, "urlList": urls[:10000]})
            print(f"IndexNow: HTTP {code} (200/202 = принято) · {len(urls)} URL")
    else:
        print("IndexNow: INDEXNOW_KEY не задан (сгенерировать: python3 -c 'import secrets;print(secrets.token_hex(16))',"
              " положить в .env и выложить файл <key>.txt в корень сайта)")

    # --- Google (вручную)
    print("Google: API переобхода для обычных страниц нет — запросить вручную в GSC → Проверка URL:")
    for u in urls[:20]:
        print("   https://search.google.com/search-console/inspect?resource_id="
              + urllib.parse.quote(a.site, safe="") + "&id=" + urllib.parse.quote(u, safe=""))


if __name__ == "__main__":
    main()
