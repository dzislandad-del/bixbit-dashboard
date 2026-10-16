# Проверить источники данных — 10.10.2026

> Запуск 10.10.2026 15:27 · длительность 0.6 мин · результат: **выполнено**

## Коротко

- GSC: работает — https://bixbit.io/, права: siteFullUser
- GA4: работает — property 320129421, sessions за 7 дней: 69564
- PageSpeed: работает — https://bixbit.io/en mobile perf=34, поле CrUX: SLOW
- CrUX: работает — https://bixbit.io PHONE LCP p75=3779ms
- Moz: не настроен — MOZ_API_TOKEN (или legacy MOZ_ACCESS_ID / MOZ_SECRET_KEY) не задан в .env
- Bing: работает — сайтов: 1, bixbit.io: verified
- Yandex: работает — сайтов: 2, bixbit.io: verified
- Итого: OK=6 WARN=0 FAIL=0 SKIP=1

## Технический лог (последние строки)

```
Проверка коннекторов — 2026-10-10 15:27
Service account: bixbit-seo-bot@bixbit-seo.iam.gserviceaccount.com
[OK]    GSC        200  https://bixbit.io/, права: siteFullUser
[OK]    GA4        200  property 320129421, sessions за 7 дней: 69564
[OK]    PageSpeed  200  https://bixbit.io/en mobile perf=34, поле CrUX: SLOW
[OK]    CrUX       200  https://bixbit.io PHONE LCP p75=3779ms
[SKIP]  Moz        -    MOZ_API_TOKEN (или legacy MOZ_ACCESS_ID / MOZ_SECRET_KEY) не задан в .env
[OK]    Bing       200  сайтов: 1, bixbit.io: verified
[OK]    Yandex     200  сайтов: 2, bixbit.io: verified
Итого: OK=6 WARN=0 FAIL=0 SKIP=1
```
