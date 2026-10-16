# Проверить источники данных — 02.10.2026

> Запуск 02.10.2026 17:03 · длительность 0.5 мин · результат: **выполнено**

## Коротко

- GSC: работает — https://bixbit.io/, права: siteFullUser
- GA4: работает — property 320129421, sessions за 7 дней: 80645
- PageSpeed: работает — https://bixbit.io/en mobile perf=37, поле CrUX: SLOW
- CrUX: работает — https://bixbit.io PHONE LCP p75=3682ms
- Moz: не настроен — MOZ_API_TOKEN (или legacy MOZ_ACCESS_ID / MOZ_SECRET_KEY) не задан в .env
- Bing: работает — сайтов: 1, bixbit.io: verified
- Yandex: работает — сайтов: 2, bixbit.io: verified
- Итого: OK=6 WARN=0 FAIL=0 SKIP=1

## Технический лог (последние строки)

```
Проверка коннекторов — 2026-10-02 17:03
Service account: bixbit-seo-bot@bixbit-seo.iam.gserviceaccount.com
[OK]    GSC        200  https://bixbit.io/, права: siteFullUser
[OK]    GA4        200  property 320129421, sessions за 7 дней: 80645
[OK]    PageSpeed  200  https://bixbit.io/en mobile perf=37, поле CrUX: SLOW
[OK]    CrUX       200  https://bixbit.io PHONE LCP p75=3682ms
[SKIP]  Moz        -    MOZ_API_TOKEN (или legacy MOZ_ACCESS_ID / MOZ_SECRET_KEY) не задан в .env
[OK]    Bing       200  сайтов: 1, bixbit.io: verified
[OK]    Yandex     200  сайтов: 2, bixbit.io: verified
Итого: OK=6 WARN=0 FAIL=0 SKIP=1
```
