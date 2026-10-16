# Контент-план блога BiXBiT (EN + RU): октябрь 2026 – июнь 2027

**Создан:** 2026-09-28 · **Обновлён:** 2026-10-10 (см. §0.1) · **Владелец:** content-seo · **Статус:** черновик. Слаги, объединения, noindex и приоритет RU утверждает команда (§6).
**Стык с `content/content-plan.md`:** тот план ведёт коммерческие страницы архитектуры v2 (17 URL). Этот ведёт только блог (`/en/blog/post/*`, `/ru/blog/post/*`). Два поста уже стоят в content-plan и здесь **не дублируются**: рефреш `immersion-liquid-choosing-the-right-one-for-mining` (W8) и `how-does-immersion-cooling-work` (W9). Раздел «Вне плана» из content-plan (нерелевантный трафик блога) разобран в §1.3 этого документа.
**Обновлять:** раз в месяц (skill `blog-plan`) после `/rank-check` и свежего GSC.

**Источники (только они, объёмы не придуманы):**
- Краул: `data/crawl-2026-09-28/pages.json`, `links.csv.gz`, `reports/crawl-2026-09-28.md`. В краул попали 106 EN-постов и 733 RU-поста.
- GSC: `data/gsc-blog-pages-90d-2026-09-28.json` (06-28..09-25), `data/gsc-pages-2026-09-28.json` (08-29..09-25), `data/gsc-blog-queries-pages-2026-09-28.json`, `data/gsc-queries-pages-all-2026-09-28.json`.
- GA4 (органика, 08-31..09-27): `data/ga4-organic-landing-2026-09-28.json`. Bing (2025-10..2026-09): `data/bing-pages-2026-09-28.json`.
- Каннибализация: `data/cannibalization/cannibal-2026-09-28.json`. AIO, featured snippets и PAA по 30 отслеживаемым ключам: `data/serp-features/serp-features-2026-09-28.json`.
- DataForSEO: `data/dfs-blog-topics-2026-09-28.json` (Labs suggestions + Trends, US/en и KZ/ru); `data/dfs-ru-briefs-2026-09-28.json` (KZ/ru, прокси СНГ); **новый** `data/dfs-blog-plan-volumes-us-2026-09-28.json` (Google Ads US, 50 ключей, $0.09, 2026-09-28).
- Разбор каждого поста с метриками и рекомендацией: **`data/blog-audit-2026-09-28.csv`** (865 строк, колонки `recommendation` / `supports_page` / `plan_id`).

> **Как читать объёмы.** Число — Google Ads US в месяц, если не указано другое. «10» — порог, то есть 0–15. **n/d** — Google Ads не отдаёт данных. RU-объём — прокси по Казахстану (KZ/ru): Россию Labs не поддерживает, поэтому для RU главный сигнал — показы GSC. «GSC i/c/pos» — показы / клики / средняя позиция.

---

## 0. Главное

1. **В блоге много трафика, но почти всё не по теме ICP.** EN за 90 дней: 132.7k показов и 271 клик. Из них 30.7% показов приходится на 11 нерелевантных постов: ERC-20 wallets, ETH PoS, ETC, Ravencoin, GPU. В RU 43% показов собирают 129 нерелевантных постов (крипто-карты, «какую криптовалюту купить», обменники).
2. **Блог почти не передаёт вес продвигаемым страницам.** Ссылки на `/en/firmwares/antminer`, `/en/ams`, immersion и hydro стоят только в меню и подвале. Контекстных ссылок из текста мало:
   - на `/en/firmwares/antminer` — **0**;
   - на `/en/firmwares/whatsminer-all-series` — 0 (хаб вообще сирота);
   - на `/en/products/pdu` — 0;
   - на `/en/ams` — 7 постов, на `immersion-systems` — 8.
   Зато из 30 постов стоят ссылки в тексте на legacy-страницы прошивок, которые закрыты noindex (`/firmwares/asic-s19`, `asic-s9-s9j-s9i` и т.п.).
3. **Featured snippets в нашей нише почти не встречаются, AIO — везде.** По 30 отслеживаемым ключам: AI Overview в 28, featured snippet в 0, PAA в 17. Поэтому формат «под сниппет» здесь означает passage для AIO и PAA:
   - ответ в 40–60 слов под H2-вопросом;
   - таблица;
   - нумерованные шаги.
   Доказательство, что это работает: Google уже показывает jump-links на H2 поста про mineral oil (`#Silicone oil` 489 показов, поз. 5.1; `#Synthetic oil` 463, поз. 5.2).
4. **Посты про прошивку Whatsminer AIO цитирует, а в органике они слабы.** По `whatsminer custom firmware` AI Overview ссылается на 2 EN-поста (`firmware-for-whatsminer-overclocking-…`, `installing-the-updated-version-…`). В органике эти же посты стоят на позициях 40–60 по «whatsminer firmware *» и делят показы с `-m2x`/`-m3x`. Поэтому: **эти два URL не сносим**, а обновляем и направляем с них ссылки на хаб. Объединяем только слабые посты.
5. **Нагрузка — допущение:** EN — 4 ед./мес (в декабре 3), RU — 3 ед./мес. RU-часть зависит от решения по RU-рынку и от возможного переезда `/ru` → `bixbit.tech` (§6, вопросы 1–2).

### 0.1 Обновление 2026-10-10 (фокус: октябрь–декабрь 2026)

**Новые данные:** краул `data/crawl-2026-10-10/` (1859 URL, из них 1742 HTML со статусом 200; 841 пост блога против 839 на 09-28); GSC 28 дн (09-10..10-07) — `data/gsc-blog-pages-28d-2026-10-10.json`, `data/gsc-blog-queries-pages-2026-10-10.json`, `data/gsc-queries-pages-all-2026-10-10.json`; GA4 органика (09-12..10-09) — `data/ga4-organic-landing-2026-10-10.json`; каннибализация — `data/cannibalization/cannibal-2026-10-10.json`; DataForSEO (Trends US 12 мес + Labs suggestions US/KZ, ≈$0.05) — `data/dfs-blog-2026-10-10.json`; разбивка RU-постов Whatsminer по странам — `data/gsc-ru-whatsminer-posts-country-2026-10-10.json`. Ahrefs не авторизован — не использовался.

1. **Выполнение плана: 0 из 8 октябрьских строк.** По краулу у целевых постов EN-OCT-1…4 и RU-OCT-1…4 title, H1 и объём текста не менялись, 301 не появились. До конца месяца осталось три недели: если мощности не хватает, в первую очередь делать P0 — EN-OCT-1, EN-OCT-2, RU-OCT-1/2, а EN-OCT-3/4 сдвинуть на неделю.
2. **Опубликовано вне плана (2 поста):** `asic-and-pool-what-to-check-before-connecting` (EN, 1 688 слов) и `asic-i-pul-chto-proverit-pered-podklyucheniem` (RU). Это материал совместно с Kryptex Pool. Schema `Article` + `Person` на месте. EN-версия ставит в тексте ссылки на `/en/firmwares` и `/en/ams` — хорошо. **RU-версия ссылается в тексте на `bixbit.tech/ru/firmwares` и `bixbit.tech/ru/ams`, а не на `/ru/...`** — это решение команды (связано с §6, вопрос 2), пометка для человека.
3. **Блог в целом (GSC 28 дн):** RU — 312 кликов / 39.0k показов; EN — 92 / 23.2k. GA4: блог — 290 из 3 212 органических сессий (9%). Лидеры по кликам по-прежнему нерелевантны (ERC-20, криптокарты, обменник) — вопросы §6 № 3–4 остаются главным блокером чистки.
4. **Перестановки по данным:**
   - **EN-FEB-4 → EN-NOV-4 (P0):** пост про контейнеры. Спрос на `mining container` / `crypto mining container` сезонный: Ads US — окт 2025 **1 300**, ноя 1 000, дек 720, авг 2026 **20**. Окно — октябрь–ноябрь. Пост сейчас каннибализирует `/en/products/container` (crypto mining shipping container: пост поз. 49.6 против товара 18.0) — переводим в информационный формат. Бриф: `content/briefs/blog/bitcoin-mining-container-guide.md`.
   - **EN-NOV-4 → EN-FEB-4:** пост про ASIC-вирус (P1; ему всё равно нужна опубликованная `/en/firmwares/dev-fee`).
   - **RU-DEC-3 → RU-NOV-3 (P0 RU):** `bitmain-vypustil-modeli-antminer-s19-…` вырос — 20 кл. / 3 102 показа / поз. 8.5 за 28 дн (было 8 / 1 961). Сейчас это самый кликабельный RU-пост наравне с `anons-proshivki-dlya-whatsminer`.
   - **RU-NOV-3 → RU-DEC-3:** объединение постов про вирус (P2).
   Нагрузка по месяцам не изменилась: EN 4/4/3, RU 3.5/3/3.
5. **Сезонность (Trends US, 12 мес):** `antminer s21` и `whatsminer` поднимаются в ноябре–декабре и пикуют в апреле–мае; `immersion cooling` пикует в апреле–июне, сейчас на дне (10–15). Значит, EN-NOV-1 (S21) публиковать **до 9 ноября**; immersion-рефреши остаются в content-plan W8/W9 и в весеннем блоке.
6. **Аудитория RU-постов про прошивку Whatsminer — в основном Россия** (`anons-…` 100 из 151 показов, `ustanovka-…` 58 из 66), где `bixbit.io` заблокирован. Это аргумент к решению §6 № 1–2 (где публиковать RU-обновления). Блокировку не обходим.
7. **Новые брифы (2026-10-10):** `antminer-s21-series-explained.md` (EN-NOV-1), `bitcoin-mining-container-guide.md` (EN-NOV-4), `antminer-l7-specs-efficiency.md` (EN-OCT-4), `whatsminer-proshivka-ru-posts.md` (RU-OCT-1+2) — в `content/briefs/blog/`. Вместе с брифами от 09-28 закрыты все P0 октября–ноября, кроме EN-NOV-2 (Whatsminer lineup — после хаба W7).
8. **Спринт ссылок (§2.0) не начат:** контекстных ссылок из блога на `/en/firmwares/whatsminer-all-series`, `/ru/firmwares/whatsminer-all-series` и `/en/products/pdu` по-прежнему **0**.
9. **В отслеживаемых ключах нет** antminer s21, antminer l7 и контейнерных запросов (`data/rank-tracking/keywords.md`) — кандидаты на ротацию в брифах, утверждает человек.

---

## 1. Аудит блога (коротко)

### 1.1 Итоги по локалям

| | EN | RU |
|---|---|---|
| Постов в краул (HTML 200) | 106 | 733 |
| GSC 90 дн: клики / показы | 271 / 132 671 | 931 / 141 657 |
| GSC 28 дн: клики / показы | 99 / 27 669 | 305 / 48 127 |
| GA4 органика, 28 дн (сессии) | 109 | 201 |
| Bing, 12 мес (показы) | 6 906 | 122 |
| «Мёртвые» (<10 показов за 90 дн) | 18 (6 с нулём) | 404 (216 с нулём) |
| Посты с ≥1 контекстной ссылкой на коммерческую страницу | 56 из 105 | 85 из 732 |
| hreflang на постах | 0 | 0 |
| Ошибки JSON-LD | 4 | 5 |

**Тематика EN (показы за 90 дн):**
- обзоры ASIC — 20 постов / 44.5k;
- нерелевантное — 11 / 40.8k;
- охлаждение — 22 / 27.8k;
- прошивки — 8 / 7.6k;
- мониторинг — 2 / 0.4k;
- PDU — 0.

**Тематика RU:**
- нерелевантное — 129 / 60.7k;
- новости и прочее — 415 / 29.4k;
- ASIC — 112 / 28.4k;
- охлаждение — 24 / 11.1k (113 кликов);
- прошивки — 12 / 7.5k (109 кликов);
- мониторинг — 3;
- PDU — 1 (0 показов).

Классификация сделана по слагу, подробности — в CSV.

### 1.2 Топ релевантных постов (кандидаты на обновление и перелинковку)

| Пост | Лок. | GSC 90д i / c / pos | Прочее | Действие (ID плана) |
|---|---|---|---|---|
| `antminer-19-series-profitability-and-price-guide` | EN | 20 310 / 38 / 7.4 | Bing 2 894 / 45 кл.; ChatGPT цитирует копию поста на `bixbit.tech` | Обновление P0 (EN-OCT-1) |
| `bitmain-antminer-l7-review-specifications-price-payback` | EN | 8 553 / 8 / 7.6 | antminer l7 — 210/мес | Обновление (EN-OCT-4) |
| `how-does-immersion-cooling-work` | EN | 5 447 / 2 / 23.4 | — | **content-plan W9** |
| `immersion-liquid-choosing-the-right-one-for-mining` | EN | 4 693 / 26 / 13.0 | GA4 14 — топ блога | **content-plan W8** |
| `killers-of-the-mining-equipment-getting-rid-of-noise-and-dust` | EN | 4 453 / 8 / 9.1 | — | Обновление (EN-FEB-3) |
| `review-of-miners-2021-new-models-vs-old-ones-with-immersion-cooling` | EN | 4 324 / 4 / 11.7 | — | Обновление + объединение (EN-APR-4) |
| `firmware-for-whatsminer-overclocking-for-m2x-m3x-m5x-series` | EN | 2 166 / 2 / 41.6 | **цитируется в AIO** | Обновление, цель объединения (EN-NOV-3) |
| `installing-the-updated-version-of-whatsminer-firmware` | EN | 1 946 / 15 / 49.9 | **цитируется в AIO**; Bing 109 | Обновление P0 (EN-OCT-2) |
| `how-to-calculate-the-pue-of-a-datacenter` | EN | 1 733 / 1 / 37.9 | **Bing 2 788 / 16 кл.**; data center pue — 1 000/мес | Обновление (EN-OCT-3) |
| `antminer-s19-pro-vs-whatsminer-m30-…` | EN | 1 693 / 11 / 6.1 | — | Обновление (EN-DEC-2) |
| `immersionnaya-zhidkost-kakuyu-vybrat-dlya-mayninga-i-pochemu` | RU | 3 428 / 54 / 8.0 | GA4 11 | Обновление (RU-NOV-1) |
| `bitmain-vypustil-modeli-antminer-s19-i-antminer-s19-pro-…` | RU | 4 132 / 12 / 16.9 | есть дубли слага | Обновление (RU-NOV-3, перенесено из RU-DEC-3) |
| `proshivka-asic-antminer-l3-…` | RU | 1 861 / 15 / 9.3 | ссылка на noindex `asic-l3-plus` | Ссылки (RU-OCT-4) |
| `ohlazhdenie-mayning-fermy` | RU | 1 644 / 4 / 13.6 | лидер каннибал-группы §1.4 | Обновление P0 (RU-OCT-3) |
| `anons-proshivki-dlya-whatsminer` | RU | 1 261 / 36 / 16.3 | GA4 9, ошибка JSON-LD | Обновление P0 (RU-OCT-1) |
| `ustanovka-obnovlennoy-versii-proshivki-whatsminer` | RU | 581 / 30 / 8.5 | — | Обновление P0 (RU-OCT-2) |

**Спорный случай — пост про PUE.** В постановке задачи PUE назван нерелевантным. Данные говорят обратное:
- ICP включает техдиректоров дата-центров;
- спрос: `data center pue` 1 000/мес (CPC $7.17), `what is pue` 590, `pue calculation` 170;
- в Bing это второй по показам пост блога;
- по `data center pue` в GSC поз. 6.5.

Поэтому предлагаю не закрывать пост, а привязать его к immersion и hydro (EN-OCT-3). Решение за командой.

### 1.3 Нерелевантные и мёртвые посты: кандидаты (решает команда)

| Группа | EN | RU | Рекомендация | Почему |
|---|---|---|---|---|
| **A. Похоже на инвест-советы** | 2: `mining-trading-or-holding-what-to-choose-for-capital-growth` (3 112 / 16), `top-10-major-cryptocurrencies-…-2020` | 12, напр. `kakuyu-kriptovalyutu-pokupat-…` (10 831 / 21, есть дубль слага), `mayning-treyding-ili-holding-…`, `pyat-luchshih-kriptovalyut-dlya-dolgosrochnyh-investiciy-…`, `bitkoin-osobenno-rastet-po-vyhodnym-…` (дубль слага) | **noindex или переписать** — первыми в очереди на решение | Противоречит бренд-правилу CLAUDE.md §4 (никаких инвест-советов) |
| **B. Не по ICP, но с трафиком** | 8: `popular-erc-20-compatible-wallets` (19 013 / 41; US 2 088 показов за 28 дн, 0 кликов), `what-will-happen-to-ethereum-mining-after-switching-to-pos` (12 422 / 3), `how-to-start-mining-ethereum-classic`, `how-to-mine-ravencoin`, `cmp-170hx-…`, PoS | 70, напр. криптокарты (4 643 / 57), криптообменник (4 119 / 34), суперкомпьютеры (6 644 / 35), биткоин-адрес, «программы для майнинга 2019» (6 807 / 1, поз. 48) | **Не вкладываться**, CTA на продукты не ставить. Прежде чем закрывать noindex, проверить бэклинки (DataForSEO backlinks, отдельная задача `offpage-seo`) | Размывают тематику сайта. Трафик на них не конвертируется: например, у ERC-20 в GA4 6 сессий |
| **C. Мёртвые** (<10 показов за 90 дн) | 17 | 394 | noindex, объединение или 410 **пакетом**, после проверки бэклинков и входящих внутренних ссылок | Трафика нет. Отдельно: 4 пары дублей слагов в RU (`…-harakteristiki-i-pribylnost` / `…-harakteristiki-pribylnost` и т.п.) → 301 на основной вариант |
| **D. Релевантные, но без контекстных ссылок** | 16 | 39 | «Спринт ссылок» (§2.0): 1–2 ссылки в тексте на продвигаемую страницу | Дешёвый способ передать вес хабам |

Список постов по группам — в `data/blog-audit-2026-09-28.csv`, фильтр по `recommendation`.

### 1.4 Каннибализирующие группы (GSC 28 дн, все страны)

| # | Запросы (показы) | Кто делит | Решение |
|---|---|---|---|
| K1 | whatsminer firmware (1 489 по всем страницам), whatsminer m20s/m21s/m60/m63 firmware (130–230 каждый) | 3–4 EN-поста на поз. 40–60 против `-m2x` (#2), `-m3x`, `/en/firmwares`; хаб `-all-series` вне игры | EN-OCT-2: цитируемые в AIO посты обновить и направить на хаб. `announcement-of-whatsminer-firmware` → 301 на `installing-…` [команда]. `firmware-update-log-…` становится журналом изменений |
| K2 | whatsminer m3 overclock (186), how to overclock whatsminer m3 (51) | документация `…/6-miner-overclocking` (поз. 1.6–2.2) против 2 EN-постов | EN-NOV-3: в блоге остаётся один пост про условия и риски разгона, шаги — только в документации. Пост `how-to-overclock-whatsminer-asics-over-50` → 301 [команда] |
| K3 | asic immersion cooling (97), immersion cooling system for mining (59), mining immersion cooling (54), immersion cooling mining (30) | 3 EN-поста против `/en/products`, `/en/products/cell`; у `immersion-systems` 1 показ | Коммерческие запросы уходят пиллару (content-plan W7–W8). EN-DEC-3 снимает с поста `immersion-cooling-or-how-to-stop-wasting-money-on-air` коммерческие формулировки в title и H1 |
| K4 | crypto mining shipping container (189), bitcoin mining shipping container (105), shipping container mining (90) | `how-shipping-containers-change-…` (поз. 50–63) против `/en/products/container` (поз. 17–19) | EN-NOV-4 (перенесено из EN-FEB-4, сезонность): пост переводим в информационный формат, коммерческую формулировку отдаём товарной странице, ставим ссылку на неё |
| K5 | охлаждение майнинг ферм (246), охлаждение для майнинга (205), водяное охлаждение майнинг (169) | 3 RU-поста (`ohlazhdenie-mayning-fermy` поз. 8.5; `…vodoblokami…`; `immersionnoe-ohlazhdenie-ili-kak-ne-pustit…`) + `/ru/products` | RU-OCT-3: `ohlazhdenie-mayning-fermy` — главный пост группы. Пост про водоблоки остаётся про GPU. Пост `immersionnoe-…` — кандидат на 301 [команда] |
| K6 | прошивка вотсмайнер (72), прошивка для asic whatsminer серии m3x (64), прошивка whatsminer m31s/m61 | `anons-…`, `kak-obnovit-…`, `proshivka-dlya-whatsminer-razgon-…` против RU-документации и `/ru/firmwares/*` | RU-OCT-1/2: ссылки на `/ru/firmwares/whatsminer-all-series`. `kak-obnovit-proshivku-whatsminer` (поз. 59.8) → 301 на `ustanovka-…` [команда] |
| K7 | antminer s19 (184), s19 pro (135), bitmain antminer l7 (120), classic майнинг (146) | EN- и RU-посты в одной выдаче (cross-locale) | Корень проблемы — отсутствие hreflang. Лечится связкой переводов (§4, п. 9) и `content/hreflang-spec.md`, а не текстом |
| K8 | контейнер для майнинга (93), стойка для майнинга (102) | `kak-konteynery-dlya-mayninga-…` против `/ru/products/container`, `/ru/products/rack` | RU-DEC-2: из поста поставить ссылки на товары |
| K9 | как проверить асик на вирусы (12) | `virus-na-asike-…` + `asic-porazil-virus-…` | RU-DEC-3 (перенесено из RU-NOV-3): объединить посты |

### 1.5 Гигиена (не считается в нагрузку, октябрь; исполнители — dev и `technical-seo`)

| # | Задача | Масштаб |
|---|---|---|
| H1 | JSON-LD через сериализатор (`json_encode` / `JSON.stringify`), а не склейкой строк | 9 постов: en `announcement-of-whatsminer-firmware`, `firmware-update-log-for-whatsminer`, `save-unprofitable-asic-equipment`, `whats-the-most-profitable-miner-in-2025`; ru `anons-proshivki-dlya-whatsminer`, `centralizaciya-…`, `kak-spasti-ubytochnoe-…`, `obzor-asic-antminer-k7`, `samye-dohodnye-asic-majnery-…`. У двух EN-постов из-за ошибки Article вообще не распознаётся |
| H2 | 302 → 301 для двух постов про WhatsminerTool, убрать их из sitemap | см. `reports/crawl-2026-09-28.md` |
| H3 | Перенаправить ссылки из текста постов с legacy noindex-страниц на `/…/firmwares/antminer#s19` и т.п. (id якорей [VERIFY у dev]) | 30 ссылок: EN 5, RU 25 |
| H4 | Шаблон блога ставит ссылки на noindex `/…/firmwares/whatsminer-series-m7x` и 4 страницы `psu-whats-power-*/download` с каждого поста | `technical-seo` [VERIFY: намеренно ли] |
| H5 | Глубина до 22 кликов: пагинация и блок «похожие посты по рубрике» (прошивки / охлаждение / мониторинг / PDU) | `technical-seo` |
| H6 | EN-пост с русским слагом `kak-maynit-kriptovalyutu-i-pri-etom-vygodno-ispolzovat-teplo-1` — проверить язык, 301 или noindex | 1 пост |

---

## 2. План по месяцам

**Допущения по нагрузке** (пересчитать, когда будет известна реальная мощность):
- EN — **4 ед./мес**, в декабре 3 (праздники);
- RU — **3 ед./мес**.
- Единица (ед.) — одна новая статья (1 200–2 000 слов) либо одно существенное обновление или объединение.
- Спринт ссылок (§2.0) и гигиена (§1.5) в нагрузку не входят. Это работа редактора и dev по ~0.1 ед. на пост.
- [VERIFY] у инженеров занимает около недели, поэтому черновик и публикация статей с тех-фактами разнесены. Как в content-plan.
- RU-статьи — **адаптация, а не перевод**: свои RU-запросы из GSC, те же [VERIFY].

**Колонки:**
- **Тип:** новая / обновление / объединение (301 — только после решения команды).
- **Ключ + объём:** см. легенду в шапке.
- **Поддерживает:** продвигаемая страница из архитектуры v2.
- **Обязательные ссылки:** контекстные, в тексте. Анкоры описательные, один и тот же точный анкор — не больше чем на 2 страницах (правило v2). Ссылки на новые страницы ставить **только после их публикации**: dev-fee — конец октября (W4), comparison — середина ноября (W6), install-гайд — W10, `/en/ams/comparison` — W11.
- **AEO-формат:** под что верстаем passage. Featured snippet в нише почти не встречается (0 из 30), см. §0.
- Приоритеты — P0–P3.

### 2.0 Спринт ссылок (октябрь–декабрь, параллельно)

Посты из групп D и «ASIC review with traffic» в CSV (EN 16, RU 39) получают по 1–2 ссылки в тексте:
- прошивки → `/en/firmwares/antminer` (секция модели) или `/en/firmwares/whatsminer-all-series`;
- охлаждение → `/en/asics-cooling/immersion-systems` или `hydro-systems`;
- мониторинг → `/en/ams`;
- электропитание → `/en/products/pdu`.

Цели спринта: у хаба Whatsminer должно появиться ≥10 входящих ссылок из блога, у PDU — ≥3 (сейчас 0 и 0). Проверка — повторный краул (`./scripts/crawl.py`).

### Октябрь 2026 — аудит → обновление лидеров, приток ссылок на хаб Whatsminer

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-OCT-1 | `antminer-19-series-profitability-and-price-guide` → «Antminer S19 Series Guide: S19, S19 Pro & S19 XP Specs, Efficiency and What Drives Profitability» (бриф: `content/briefs/blog/antminer-s19-series-guide.md`) | EN | обновление | antminer s19 pro 590 · antminer s19 xp 170 · GSC antminer s19 pro profitability 64 / поз. 8 | `/en/firmwares/antminer#s19` | `/en/firmwares/antminer#s19` (вместо noindex `/en/firmwares/asic-s19`), `/en/calc`, `/en/ams`, `/en/firmwares/dev-fee` (после W4) | таблица моделей (TH/s, W, J/TH [VERIFY]); ответ в 40–60 слов «Which S19 model is most efficient?»; FAQ | **P0** |
| EN-OCT-2 | Посты про прошивку Whatsminer: обновить `installing-the-updated-version-of-whatsminer-firmware` и `firmware-update-log-for-whatsminer` (журнал изменений); `announcement-of-whatsminer-firmware` → 301 [команда] (бриф: `content/briefs/blog/whatsminer-firmware-posts-consolidation.md`) | EN | обновление + объединение | whatsminer firmware update 10 · GSC whatsminer firmware 1 489 по сайту | `/en/firmwares/whatsminer-all-series`, `-m2x`…`-m6x` | хаб `-all-series`, `-m3x`, `/en/documentation/user-guide-for-whatsminer-asic` | журнал версий таблицей (версия / дата / модели / изменения [VERIFY]); шаги установки коротко + ссылка на документацию | **P0** |
| EN-OCT-3 | `how-to-calculate-the-pue-of-a-datacenter`: PUE для майнинга и ДЦ, air vs hydro vs immersion (бриф: `content/briefs/blog/data-center-pue.md`) | EN | обновление | data center pue 1 000 (CPC $7.17) · what is pue 590 · pue calculation 170 | `/en/asics-cooling/immersion-systems`, `hydro-systems` | immersion-systems, hydro-systems, `/en/ams` (учёт мощности [VERIFY]) | формула в блоке-определении (≤50 слов); пример расчёта шагами; таблица диапазонов PUE по типам охлаждения [VERIFY, с источником] | P1 |
| EN-OCT-4 | `bitmain-antminer-l7-review-…`: характеристики и эффективность; обещания окупаемости («payback») убрать (бриф: `content/briefs/blog/antminer-l7-specs-efficiency.md`; вариант A/B — по ответу на §6 вопрос 8) | EN | обновление | antminer l7 210 · GSC antminer l7 overclock 26 / поз. 15 | `/en/firmwares/antminer` (L7 [VERIFY: поддержка и секция]) | `/en/firmwares/antminer`, `/en/calc` | таблица характеристик; FAQ «Can you overclock the L7?» [VERIFY] | P1 |
| RU-OCT-1 | `anons-proshivki-dlya-whatsminer`: актуализация, JSON-LD (H1) (бриф вместе с RU-OCT-2: `content/briefs/blog/whatsminer-proshivka-ru-posts.md`) | RU | обновление | прошивка whatsminer 10 (KZ) · GSC 1 261 / 36 кл. за 90 дн | `/ru/firmwares/whatsminer-all-series` | хаб `-all-series`, `/ru/firmwares/whatsminer-series-m3x`, RU-документация | список поддерживаемых серий [VERIFY]; FAQ | **P0** |
| RU-OCT-2 | `ustanovka-obnovlennoy-versii-proshivki-whatsminer` + `zhurnal-obnovleniy-…`; `kak-obnovit-proshivku-whatsminer` → 301 [команда] | RU | обновление + объединение | обновление прошивки whatsminer n/d (KZ) · GSC 581 / 30 кл., поз. 8.5 | `/ru/firmwares/whatsminer-all-series` | хаб, `/ru/documentation/rukovodstvo-polzovatelia-whatsminer-asic` | нумерованные шаги + ссылка на документацию | **P0** |
| RU-OCT-3 | `ohlazhdenie-mayning-fermy` → главный RU-пост про охлаждение: воздух / гидро / иммерсия (бриф: `content/briefs/blog/ohlazhdenie-mayning-fermy.md`) | RU | обновление (решение K5) | охлаждение майнинг фермы 10, охлаждение асиков 10 (KZ) · GSC охлаждение майнинг ферм 246 / поз. 8.5 / 0 кл.; для майнинга 205; водяное охлаждение 169 | `/ru/asics-cooling`, `/ru/asics-cooling/hydro-systems`, `/ru/asics-cooling/immersion-systems` | все три + `/ru/products/coolant` | таблица сравнения трёх способов; ответ «Какое охлаждение выбрать для майнинг-фермы» в 40–60 слов; FAQ | **P0** (RU) |
| RU-OCT-4 | Ссылки в RU-постах про прошивки Antminer (L3, L7, S17): с noindex-страниц → на `/ru/firmwares/antminer` (часть H3) | RU | обновление (0.5 ед.) | GSC: L3 1 861, L7 1 191, S17 1 111 показов за 90 дн | `/ru/firmwares/antminer` | `/ru/firmwares/antminer` | — | P1 |

**Октябрь, итог:** EN 4 ед. · RU 3.5 ед. + гигиена H1–H6 + старт спринта ссылок.

### Ноябрь 2026 — сезонный пик Antminer (Trends: ноябрь 37.2 против 9.3 в сентябре), хаб Whatsminer

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-NOV-1 | «Antminer S21 Series Explained: S21, S21 Pro, S21 XP and Hydro — Specs, Efficiency, Cooling Options» (бриф: `content/briefs/blog/antminer-s21-series-explained.md`; публикация до 9 ноября, до сезонного роста). **Не** брать в цель «antminer s21 firmware» — это запрос коммерческой страницы | EN | новая | antminer s21 1 000 · s21 pro 480 · s21 xp 320 (CPC $1.94–3.22) | `/en/firmwares/antminer#s21` | `/en/firmwares/antminer#s21`, `/en/asics-cooling/hydro-systems` (S21 Hydro), `/en/firmwares/comparison` (после W6) | таблица моделей [VERIFY: TH/s, W, J/TH, тип охлаждения]; «Which S21 model should you run?» — 40–60 слов; FAQ | **P0** |
| EN-NOV-2 | «Whatsminer Lineup Guide: M30S to M60S — Efficiency, Air vs Hydro Variants, Firmware Support». Публикация после обновления хаба (content-plan W7) | EN | новая | whatsminer m60s 110 · m30s 90 · m50s 70 · m50 70 · whatsminer 590 (широкий, не цель) | `/en/firmwares/whatsminer-all-series` + `-m3x`/`-m5x`/`-m6x` | хаб, все серийные страницы, `/en/asics-cooling/hydro-systems` | таблица «серия → модели → охлаждение → поддержка прошивкой [VERIFY]» | **P0** |
| EN-NOV-3 | Объединение постов про разгон Whatsminer: целевой — `firmware-for-whatsminer-overclocking-for-m2x-m3x-m5x-series` (цитируется в AIO); `how-to-overclock-whatsminer-asics-over-50` → 301 [команда]. Угол статьи — условия и риски (питание, охлаждение, лимиты); шаги — в документации | EN | объединение | whatsminer overclock 10 · GSC whatsminer m3 overclock 186 | `/en/firmwares/whatsminer-all-series#tuning` | хаб (секция tuning), `/en/documentation/user-guide-for-whatsminer-asic` (глава про разгон), `/en/asics-cooling/immersion-systems` | чек-лист перед разгоном; таблица «режим → что проверить» [VERIFY]. Цифру «over 50%» не повторять без [VERIFY] | P1 |
| EN-NOV-4 | **Перенесено из EN-FEB-4 (2026-10-10): сезонность.** `how-shipping-containers-change-the-cryptocurrency-mining-industry` (K4) → информационный гид «Bitcoin Mining Containers: Air vs Hydro vs Immersion, Site Requirements and a Planning Checklist» (бриф: `content/briefs/blog/bitcoin-mining-container-guide.md`). Коммерческий интент («for sale», «price») отдаём товарной странице. Публиковать вместе с рефрешем `/en/products/container` (`content/briefs/hardware-mining-container.md`) или после него | EN | обновление | mining container 390 · crypto mining container 390 (CPC $4.2–4.3) · crypto mining shipping container 170 — **пик октябрь–ноябрь** (Ads US: окт 2025 1 300, ноя 1 000, авг 2026 20; `data/dfs-blog-2026-10-10.json`) · GSC 28 дн: пост поз. 39, crypto mining shipping container — пост 49.6 против товара 18.0 | `/en/products/container` | `/en/products/container`, `/en/asics-cooling/hydro-systems`, `/en/asics-cooling/immersion-systems` | таблица «air / hydro / immersion container» [VERIFY]; чек-лист требований к площадке (питание, вода, фундамент) нумерованным списком; ответ «What is a bitcoin mining container?» в 40–60 слов; цену не называть — только факторы стоимости | **P0** |
| RU-NOV-1 | `immersionnaya-zhidkost-…`: зеркало EN-рефреша из content-plan W8 | RU | обновление | иммерсионная жидкость 20 (KZ) · GSC 197 / поз. 6.8 | `/ru/products/coolant`, `/ru/asics-cooling/immersion-systems` | обе | таблица типов жидкостей [VERIFY] | P1 |
| RU-NOV-2 | Адаптация EN-NOV-1: «Antminer S21: обзор серии — характеристики, эффективность, охлаждение» | RU | новая | n/d (KZ не измерено) | `/ru/firmwares/antminer` | `/ru/firmwares/antminer`, `/ru/asics-cooling/hydro-systems` | таблица моделей [VERIFY] | P1 |
| RU-NOV-3 | **Перенесено из RU-DEC-3 (2026-10-10): рост** — 28 дн: 20 кл. / 3 102 показа / поз. 8.5 (было 8 / 1 961). Пересекается с EN-OCT-1 по «antminer s19» (cross-locale: RU 190 показов, поз. 9.6 против EN 62, поз. 21.9). `bitmain-vypustil-modeli-antminer-s19-…`: характеристики и эффективность; 301 с дублей слага [команда] | RU | обновление | GSC 4 132 / 12 / поз. 16.9 за 90 дн | `/ru/firmwares/antminer#s19` | `/ru/firmwares/antminer`, `/ru/calc` | таблица моделей [VERIFY] | **P0** (RU) |

**Ноябрь, итог:** EN 4 · RU 3.

### Декабрь 2026 — после выхода comparison и пиллара immersion (нагрузка снижена)

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-DEC-1 | «J/TH Explained: How to Measure ASIC Efficiency at the Wall and Why It Matters More Than Hashrate» | EN | новая | j/th 50 · asic efficiency 10 · GSC mining efficiency firmware 13 / поз. 9.6 | `/en/firmwares` + `/en/firmwares/antminer#tuning` | `/en/firmwares`, `/en/firmwares/antminer#tuning`, `/en/ams` (мощность на устройство [VERIFY]), EN-NOV-1 | определение (≤50 слов) + формула; пример расчёта; таблица «что меняет J/TH» | P1 |
| EN-DEC-2 | `antminer-s19-pro-vs-whatsminer-m30-…`: сравнение эффективности без прогнозов прибыли | EN | обновление | antminer vs whatsminer 10 · GSC 1 693 / поз. 6.1 за 90 дн | `/en/firmwares/comparison` | comparison, `/en/firmwares/antminer#s19`, `-m3x` | таблица сравнения; вывод «когда какой» в 40–60 слов | P1 |
| EN-DEC-3 | `immersion-cooling-or-how-to-stop-wasting-money-on-air`: снять коммерческие формулировки (K3), угол — TCO и эксплуатация | EN | обновление | GSC mining immersion cooling 54 / поз. 11.3 | `/en/asics-cooling/immersion-systems` | immersion-systems (анкор ≠ анкору из C8/C9), `/en/calc` | таблица «air vs immersion: эксплуатационные факторы» [VERIFY]; без обещаний окупаемости | P1 |
| RU-DEC-1 | Адаптация EN-NOV-2: «Линейка Whatsminer: M30S – M60S» | RU | новая | n/d (KZ); GSC whatsminer m31s 66, whatsminer m3 96 (cross-locale) | `/ru/firmwares/whatsminer-all-series` | хаб, серийные RU-страницы | таблица серий [VERIFY] | P1 |
| RU-DEC-2 | `kak-konteynery-dlya-mayninga-…`: ссылки на товары (K8) | RU | обновление | GSC контейнер для майнинга 93, стойка для майнинга 102 | `/ru/products/container`, `/ru/products/rack` | обе | — | P2 |
| RU-DEC-3 | **Перенесено из RU-NOV-3 (2026-10-10).** Объединение K9: `virus-na-asike-kak-obnaruzhit-i-vylechit` ← `asic-porazil-virus-…` (301 [команда]) | RU | объединение | GSC как проверить асик на вирусы 12 / поз. 6.2 | `/ru/firmwares` (безопасность); RU dev-fee — когда появится | `/ru/firmwares`, `/ru/ams` | шаги проверки; FAQ | P2 |

**Декабрь, итог:** EN 3 · RU 3. На неделе 21 дек – 3 янв новых публикаций нет.

### Январь 2027 — годовые материалы и охлаждение

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-JAN-1 | «Hydro (Direct-to-Chip) vs Immersion Cooling for ASIC Mining». Углублённая версия короткого блока на `/en/asics-cooling` (архитектура v2, #17) | EN | новая | direct to chip cooling 590 (CPC $11.92, общий ДЦ-спрос) · direct-to-chip vs immersion cooling 30 · immersion cooling vs liquid cooling 20 | `/en/asics-cooling/hydro-systems`, `immersion-systems` | обе + `/en/asics-cooling`, EN-OCT-3 (PUE) | сравнительная таблица по 8–10 критериям [VERIFY]; ответ «Which is better for ASIC mining?» в 40–60 слов | P1 |
| EN-JAN-2 | «Whatsminer M70 / M79 Series: Specs and Cooling Variants» — если серия вышла и поддерживается [VERIFY]. `-m7x` сейчас noindex с title от M6x (`technical-seo`) | EN | новая | microbt whatsminer m79s 170 · whatsminer m79s 70 · whatsminer m70 50 (тренд +100% г/г) | `/en/firmwares/whatsminer-all-series` (потом `-m7x`) | хаб, EN-NOV-2 | таблица характеристик [VERIFY] | P1 |
| EN-JAN-3 | «Most Efficient ASIC Miners in 2027: J/TH Ranking» — рейтинг по эффективности, не по прибыли. `whats-the-most-profitable-miner-in-2025` → 301 [команда, слаг VERIFY] | EN | новая + объединение | best asic miner 110 · most profitable asic miner 70 (не цель) · GSC 652 показа у старого поста | `/en/firmwares`, `/en/calc` | `/en/firmwares`, `/en/firmwares/antminer`, хаб Whatsminer, EN-DEC-1 | ранжированная таблица (модель / J/TH / охлаждение [VERIFY, дата данных]) | P1 |
| EN-JAN-4 | «BiXBiT 2026 in Numbers» — продолжение `bixbit-2025-year-in-numbers` (1 863 / поз. 4.3) | EN | новая | бренд | `/en/firmwares`, `/en/ams`, `/en/asics-cooling` | все три | блок ключевых цифр [VERIFY у команды] — E-E-A-T | P2 |
| RU-JAN-1 | Адаптация EN-DEC-1: «J/TH: как считать эффективность асика» | RU | новая | n/d | `/ru/firmwares` | `/ru/firmwares`, `/ru/firmwares/antminer`, `/ru/ams` | определение + формула | P1 |
| RU-JAN-2 | Адаптация EN-JAN-1: «Гидро или иммерсия: что выбрать для майнинга» | RU | новая | GSC водяное охлаждение майнинг 169; гидроохлаждение асиков n/d (KZ) | `/ru/asics-cooling/hydro-systems`, `immersion-systems` | обе + RU-OCT-3 | таблица сравнения | P1 |
| RU-JAN-3 | RU-рейтинг эффективности 2027. `samye-dohodnye-asic-majnery-zhidkostnoe-ohlazhdenie` (1 189 показов, «топ асиков для майнинга» 387 / поз. 13, ошибка JSON-LD) → 301 [команда] | RU | новая + объединение | GSC топ асиков для майнинга 387 | `/ru/firmwares` | `/ru/firmwares`, `/ru/calc` | ранжированная таблица [VERIFY] | P1 |

### Февраль 2027 — мониторинг и PDU (самые слабые по ссылкам кластеры)

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-FEB-1 | «How to Monitor an ASIC Fleet: 10 Metrics That Predict Downtime». Отдельный интент how-to, не «software» (у `/en/ams` поз. 3–10 по asic monitoring software, её не трогаем) | EN | новая | asic monitoring 70 · how to monitor asic miners n/d · GSC how to monitor asic miners remotely 17 / поз. 10.3; how to monitor mining farm health? 11 / поз. 4.2 | `/en/ams` | `/en/ams`, `/en/ams/comparison`, EN-DEC-1 | нумерованный список метрик с порогами [VERIFY]; ответ на вопрос из GSC в 40–60 слов | P1 |
| EN-FEB-2 | «PDUs for Bitcoin Mining: Planning 240V and 3-Phase Power Distribution for ASIC Racks» | EN | новая | smart pdu 320 (CPC $3.61) · 240v pdu 90 · 3 phase pdu 90 · pdu for mining 20 · mining pdu 20 | `/en/products/pdu` (из блога сейчас 0 ссылок) | `/en/products/pdu`, `/en/ams` (мониторинг питания [VERIFY]), `/en/asics-cooling/hydro-systems` | формула расчёта нагрузки на ветку; таблица «сеть → тип PDU» [VERIFY у инженеров]; **юр.: без гарантий соответствия нормам (NEC и т.п.)** | P1 |
| EN-FEB-3 | `killers-of-the-mining-equipment-getting-rid-of-noise-and-dust` | EN | обновление | asic miner noise 10 · GSC mining rig noise reduction 19 / поз. 13 | `/en/asics-cooling/hydro-systems`, `immersion-systems` | обе | таблица «проблема → решение»; FAQ | P1 |
| EN-FEB-4 | **Перенесено из EN-NOV-4 (2026-10-10).** `how-to-detect-and-cure-an-asic-virus`: безопасность прошивки, признаки взлома, как проверить | EN | обновление | asic miner virus n/d · GSC how to remove bitcoin miner virus 15 / поз. 47 | `/en/firmwares/dev-fee` (секция безопасности) | `/en/firmwares/dev-fee`, `/en/ams` | нумерованные шаги проверки; FAQ «Can custom firmware contain a backdoor?» — только утверждения, подтверждённые инженерами [VERIFY] | P1 |
| RU-FEB-1 | Адаптация EN-FEB-1: «Как мониторить асики удалённо: метрики, которые предсказывают простой» | RU | новая | мониторинг асиков 10 (KZ) · GSC удалённый мониторинг асиков 12 / поз. 3.8 (на `/ru/ams`: цель статьи — how-to, не «программа») | `/ru/ams` | `/ru/ams` | нумерованный список | P1 |
| RU-FEB-2 | `obsluzhivanie-asic-uhod-i-diagnostika` (804 показа за 90 дн) | RU | обновление | GSC мониторинг асиков (показ поста) | `/ru/ams` | `/ru/ams`, RU-OCT-3 | чек-лист обслуживания | P1 |
| RU-FEB-3 | `besplatnoe-otoplenie-za-schet-mayninga-pribyl-v-pervyy-zhe-sezon`: новый title без обещания прибыли, угол — утилизация тепла | RU | обновление | GSC майнинг отопление 86 | `/ru/asics-cooling/hydro-systems` [VERIFY: поддерживает ли гидро рекуперацию тепла] | hydro-systems | — | P2 |

RU-версия поста про PDU **не планируется**, пока `/ru/products/pdu` отдаёт 404 (crawl P0-1).

### Март 2027 — подготовка к лету, E-E-A-T

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-MAR-1 | «Summer Derating: Undervolting Profiles for Hot-Climate ASIC Sites». Операционный угол, не дубль секции tuning | EN | новая | n/d (asic undervolting n/d, bitcoin mining curtailment n/d, ercot bitcoin mining n/d); GSC-сигнала нет | `/en/firmwares/antminer#tuning` | `/en/firmwares/antminer#tuning`, хаб Whatsminer, `/en/asics-cooling/immersion-systems` | таблица «температура на входе → профиль» [VERIFY] | P2 (только GEO; отложить, если GSC к марту не даст показов) |
| EN-MAR-2 | «Immersion Fluid Maintenance: Testing, Filtration and Top-Up Schedule» | EN | новая | n/d (immersion fluid maintenance, immersion cooling maintenance); смежный спрос: immersion cooling fluid 110 | `/en/products/coolant`, `immersion-systems` | обе + пост про mineral oil | нумерованный регламент [VERIFY] | P2 |
| EN-MAR-3 | `ams-bixbit-mining-management-case`: кейс с проверяемыми цифрами | EN | обновление | GSC 236 / поз. 6.4 | `/en/ams` | `/en/ams`, `/en/ams/comparison` | блок «Results» с цифрами [VERIFY у клиента и команды] | P1 |
| EN-MAR-4 | «How Hosting Providers Monitor Client Fleets and Report Uptime» | EN | новая | asic miner hosting 70 (**CPC $25.34**) · mining farm hosting 10 | `/en/ams` (мультиклиентский режим [VERIFY]) | `/en/ams`, `/en/products/pdu` | список «что включить в отчёт клиенту» | P1 |
| RU-MAR-1 | Адаптация EN-MAR-1 (лето в KZ и на юге) | RU | новая | n/d | `/ru/firmwares/antminer` | `/ru/firmwares/antminer`, хаб Whatsminer | таблица [VERIFY] | P2 |
| RU-MAR-2 | Адаптация EN-MAR-2 | RU | новая | иммерсионная ванна для асиков 10 (KZ) | `/ru/products/coolant` | coolant, immersion-systems | регламент | P2 |
| RU-MAR-3 | `ams-bixbit-mining-management-case-study` | RU | обновление | GSC 176 / поз. 39 | `/ru/ams` | `/ru/ams` | блок «Результаты» [VERIFY] | P1 |

### Апрель 2027 — сезон (Trends: immersion растёт с апреля по июнь)

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-APR-1 | «ASIC Operating Temperature Guide: Chip, Board and Inlet Limits for Antminer and Whatsminer» | EN | новая | asic miner temperature 10 · antminer temperature 10 | `/en/ams` (алерты [VERIFY]), `/en/asics-cooling` | `/en/ams`, `hydro-systems`, `immersion-systems` | таблица пределов по моделям [VERIFY по документации производителя] | P1 |
| EN-APR-2 | «What Is Hashprice? Definition, Formula and How Efficiency Changes Your Exposure» — только определение, без прогнозов | EN | новая | hashprice 590 | `/en/calc`, `/en/firmwares` | `/en/calc`, EN-DEC-1 | определение в 40–60 слов + формула | P2 (юр. и бренд: проверить, что нет инвест-советов) |
| EN-APR-3 | `5-reasons-to-switch-to-asic-immersion-cooling-in-summer` — сезонный рефреш | EN | обновление | GSC 119 показов | `immersion-systems` | immersion-systems, EN-APR-1 | список с тезисами по 40–60 слов | P2 |
| EN-APR-4 | `review-of-miners-2021-…`: «Older vs Newer ASICs in Immersion». `which-asic-to-buy-in-2019-…` → 301 [команда] | EN | обновление + объединение | GSC 4 324 / поз. 11.7 за 90 дн | `immersion-systems` | immersion-systems, EN-JAN-3 | таблица [VERIFY] | P2 |
| RU-APR-1 | Адаптация EN-APR-1: «Рабочая температура асика» | RU | новая | GSC рабочая температура асика 17 / поз. 5.5; температура для майнинга 47; btc tools температура плат 63 (документация) | `/ru/ams`, `/ru/asics-cooling` | `/ru/ams`, RU-OCT-3 | таблица пределов [VERIFY] | **P1** (у RU есть сигнал GSC) |
| RU-APR-2 | `5-prichin-letom-pereyti-na-immersionnoe-ohlazhdenie-asic` (225 / 7 кл.) | RU | обновление | GSC | `/ru/asics-cooling/immersion-systems` | immersion-systems | список | P2 |
| RU-APR-3 | Адаптация EN-MAR-4 (хостинг-провайдеры) | RU | новая | n/d | `/ru/ams` | `/ru/ams` | список | P2 |

### Май 2027 — пик Antminer (Trends: май 43.8, максимум года)

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-MAY-1 | «Antminer S19 vs S21: Retune or Replace? An Efficiency Comparison» — без обещаний прибыли | EN | новая | n/d (s19 vs s21 не измерено); смежные: antminer s21 1 000, s19 pro 590 | `/en/firmwares/antminer` | `#s19`, `#s21`, `/en/calc`, EN-OCT-1, EN-NOV-1 | таблица сравнения [VERIFY]; вывод в 40–60 слов | P1 |
| EN-MAY-2 | `full-review-of-microbt-whatsminer-m50-m50s-and-m53-…` | EN | обновление | whatsminer m50 70 · m50s 70 · GSC 1 749 / поз. 24.3 | `-m5x` | `-m5x`, хаб, `hydro-systems` (M53 Hydro) | таблица [VERIFY] | P1 |
| EN-MAY-3 | «Early Signs of Hashboard Failure in Your Monitoring Data» | EN | новая | antminer hashboard repair 10 | `/en/ams` | `/en/ams`, EN-FEB-1 | список «симптом → метрика → действие» [VERIFY] | P2 |
| EN-MAY-4 | Квартальный рефреш топ-постов: EN-OCT-1, EN-NOV-1, EN-NOV-2, EN-JAN-3 (даты, [VERIFY]-цифры, новые модели) | EN | обновление | — | как в исходных | — | — | P1 |
| RU-MAY-1 | Адаптация EN-MAY-1 | RU | новая | n/d | `/ru/firmwares/antminer` | `#s19`, `#s21` | таблица | P1 |
| RU-MAY-2 | Адаптация EN-MAY-3 | RU | новая | n/d | `/ru/ams` | `/ru/ams` | список | P2 |
| RU-MAY-3 | PDU (RU) — **только если** к маю есть `/ru/products/pdu`; иначе резерв под находки GSC | RU | новая / резерв | n/d | `/ru/products/pdu` | — | — | P3 |

### Июнь 2027 — лето и итоги полугодия

| ID | Тема / пост | Язык | Тип | Ключ + объём | Поддерживает | Обязательные ссылки | AEO-формат | P |
|---|---|---|---|---|---|---|---|---|
| EN-JUN-1 | «Summer Checklist for Air-Cooled Mining Farms: Preventing Thermal Downtime» | EN | новая | n/d | `hydro-systems`, `immersion-systems`, `/en/ams` | все три + EN-APR-1 | нумерованный чек-лист | P2 |
| EN-JUN-2 | Объединение ДЦ-постов: `datacenter-cooling-methods-everything-you-need-to-know` ← `data-centre-cooling-trends-2026` [команда] | EN | объединение | data center immersion cooling 590 (CPC $11.23) · immersion cooling for data centers 210 | `/en/asics-cooling` | `/en/asics-cooling`, EN-OCT-3, EN-JAN-1 | таблица методов | P2 |
| EN-JUN-3 | Итоги полугодия: сверка по GSC, пересборка плана на Q3 2027 | EN | — | — | — | — | — | P1 |
| EN-JUN-4 | Резерв: тема из новых GSC-запросов с показами без хорошей страницы | EN | новая | по данным | — | — | — | P2 |
| RU-JUN-1 | Адаптация EN-JUN-1 | RU | новая | n/d | `/ru/asics-cooling` | RU-OCT-3, RU-APR-1 | чек-лист | P2 |
| RU-JUN-2 | Итоги полугодия RU | RU | — | — | — | — | — | P1 |
| RU-JUN-3 | Резерв | RU | — | — | — | — | — | P3 |

### 2.1 Сводка

- **EN:** 35 ед. Из них 18 новых статей (включая резерв EN-JUN-4), остальное — обновления, объединения и итоги.
- **RU:** 27.5 ед. (28 позиций, RU-OCT-4 — пол-единицы). Все новые RU-статьи — адаптации EN.
- Каждая позиция плана (кроме итогов и резерва) ставит ссылку хотя бы на одну продвигаемую страницу: прошивки Antminer, хаб и серии Whatsminer, охлаждение, AMS, PDU. PDU в плане только EN-FEB-2 и EN-MAR-4, поэтому основной приток ссылок на `/en/products/pdu` даёт спринт (§2.0).

**Отслеживаемые ключи:** план вводит новые блоговые цели. Предлагаю добавить в `data/rank-tracking/keywords.md`: `antminer s21` → EN-NOV-1, `data center pue` → EN-OCT-3, `direct to chip vs immersion cooling` → EN-JAN-1, `smart pdu` → EN-FEB-2. Файл я не менял, ротацию утверждает человек. Объединения из K1/K2 не меняют URL ключей, которые уже отслеживаются.

---

## 3. Шаблон брифа статьи блога

Файл: `content/briefs/blog/<slug>.md`. Готовые брифы на октябрь: `antminer-s19-series-guide.md`, `whatsminer-firmware-posts-consolidation.md`, `data-center-pue.md`, `ohlazhdenie-mayning-fermy.md`.

```markdown
# Бриф: <рабочий заголовок>
**ID плана:** EN-XXX-N · **Язык:** EN / RU · **Тип:** новая / обновление / объединение · **Приоритет:** P0–P3
**URL:** существующий `/en/blog/post/<slug>` или новый слаг `[VERIFY у команды]` · **Пара hreflang:** `/ru/blog/post/<slug>` (или «нет»)
**Поддерживает (architecture v2):** `<продвигаемый URL#секция>`, чем именно пост ему помогает
**Автор / ревьюер:** <инженер BiXBiT, должность> / <кто проверяет [VERIFY]> · **Дата проверки фактов:** <YYYY-MM-DD>

## 1. Цель и интент
- Интент (informational / how-to / comparison / news). Чем пост отличается от продвигаемой страницы: какой запрос он **не** забирает у неё.
- Читатель (ICP): оператор фермы / техдиректор ДЦ / хостинг-провайдер. Какая у него боль.
- Действие после чтения: переход на <URL>.

## 2. Ключи (только из данных)
| Ключ | Объём (источник, дата) | GSC i/c/pos (окно) | Роль |
|---|---|---|---|
| основной | … | … | title/H1 |
| вторичные | … | … | H2 |
| не брать в цель (занят страницей X) | … | … | — |

## 3. Title / description / H1
- Title ≤ 60 симв., с основным ключом в начале; без «profitable», «ROI guaranteed», «no dev fee».
- Description ≤ 155 симв.
- H1 — один, отличается от title.

## 4. Структура (H2/H3) и AEO
- Первый абзац после H1: ответ на главный вопрос в 40–60 слов, без маркетинга. Это passage для AIO.
- H2 формулировать вопросом там, где есть PAA или вопросный запрос в GSC. Сразу под H2 — ответ в 1–2 предложения, затем детали.
- Таблица (если сравнение или характеристики): единицы в заголовке колонки (TH/s, W, J/TH, °C), дата данных, источник.
- Шаги — нумерованным списком (для how-to).
- FAQ: 4–6 вопросов из PAA или GSC; ответ ≤ 80 слов.

## 5. Сущности и термины
Модели, технологии, стандарты — то, что должно встретиться в тексте.

## 6. Факты на проверку [VERIFY]
Список всех цифр и утверждений: хешрейт, W, J/TH, °C, совместимость, функции AMS, dev fee («transparent dev fee [VERIFY: current rate with the team]»), данные конкурентов (с датой и источником).

## 7. Внутренние ссылки
| Куда | Анкор | Где в тексте | Обязательна? |
|---|---|---|---|
Правила: ≥ 2 контекстные ссылки на продвигаемые страницы и 1–2 на соседние посты. Нельзя ссылаться на noindex legacy-страницы, на 302 и на страницы, которые ещё не вышли.

## 8. Внешние источники (E-E-A-T)
Документация производителя, стандарты, собственные тесты BiXBiT (ссылка на протокол) [VERIFY].

## 9. Запреты
Никакой доходности и инвест-советов (сравнивать только J/TH и технику); не писать «no dev fee»; без юр-гарантий; партнёрский домен (agent-knowledge §2) не упоминать.

## 10. После публикации
Чек-лист §4. Что замерить через 28 дней: ключи и страница.
```

---

## 4. Чек-лист публикации (и обновления) поста

**До публикации**
1. [ ] Бриф утверждён. Для нового URL слаг согласован с командой. Для объединения есть решение команды и запись в §5.
2. [ ] Все `[VERIFY]` закрыты инженером. В тексте нет «no dev fee» / «zero fee» (только «transparent dev fee» с проверенной ставкой), обещаний прибыли и окупаемости, инвест-советов, упоминаний партнёрского домена (agent-knowledge §2).
3. [ ] Текст прогнан через `humanizer`, затем через skill `text-review`.
4. [ ] Title ≤ 60, description ≤ 155, один H1. У изображений есть alt (кроме декоративных).
5. [ ] **Перелинковка:**
   - ≥ 2 контекстные ссылки на продвигаемые страницы из строки плана и 1–2 на соседние посты;
   - анкоры описательные, один точный анкор — не больше чем на 2 страницах;
   - нет ссылок на noindex, 302 и 404;
   - ссылки на новые страницы (dev-fee, comparison, install, ams/comparison) — только после их выхода.
6. [ ] **Входящие ссылки:** ≥ 2 ссылки на новый пост из уже проиндексированных постов той же рубрики и из продвигаемой страницы, если это есть в матрице `content/internal-linking.md`. Пост виден из блока рубрики не глубже 3 кликов от главной блога.
7. [ ] **JSON-LD** генерируется сериализатором (`json_encode` / `JSON.stringify`), без склейки строк:
   - `BlogPosting` или `Article`: `headline`, `datePublished`, `dateModified`, `author` (Person с `jobTitle`), `publisher` (Organization);
   - `BreadcrumbList`;
   - `FAQPage` — только если FAQ виден на странице, и никогда пустой.
   Для Google FAQ и HowTo rich results на таком сайте почти не выводятся, разметка нужна для структуры и GEO. Проверка: `./scripts/page-snapshot.py --urls <url> --out data/page-snapshot-<date>.json --compare none` → `jsonld_errors = 0`.
8. [ ] **hreflang-пара EN/RU:** связь переводов в CMS (translation group). На обеих версиях — self + пара + `x-default` = en, по `content/hreflang-spec.md`. Проверка: `scripts/hreflang-check.py`. Если RU-версии нет, hreflang не ставить.
9. [ ] Canonical на себя, пост в sitemap с корректным `lastmod`.

**После публикации (в день деплоя)**
10. [ ] Переиндексация:
    - Bing и IndexNow: `./scripts/index-submit.py --urls https://bixbit.io/en/blog/post/<slug>,https://bixbit.io/ru/blog/post/<slug> --submit`. Сначала без `--submit` — dry run с квотой;
    - Google: вручную «Запросить индексирование» в GSC URL Inspection (скрипт печатает ссылки).
11. [ ] **Объединения:**
    - 301, не 302;
    - внутренние ссылки ведут сразу на итоговый URL (проверка по `data/crawl-*/links.csv.gz` после краула);
    - старый URL удалён из sitemap;
    - на переиндексацию отправлены итоговый URL и страницы, где менялись ссылки.
12. [ ] Строка в журнале §5: дата, URL, что сделано.
13. [ ] Через 28 дней: GSC по странице (`./scripts/gsc-query.py --days 28 --dimensions query,page --out …`) и сверка с метриками из CSV. Раз в месяц — `./scripts/serp-features.py` по ключам поста (AIO, PAA).

---

## 5. Журнал (заполнять при деплое)

| Дата | ID | URL | Что сделано (обновление / 301 / noindex / новая) | Замер через 28 дн |
|---|---|---|---|---|
| до 2026-10-10 | вне плана | `/en/blog/post/asic-and-pool-what-to-check-before-connecting` | новая (с Kryptex Pool); ссылки на `/en/firmwares`, `/en/ams` | ~2026-11-07 |
| до 2026-10-10 | вне плана | `/ru/blog/post/asic-i-pul-chto-proverit-pered-podklyucheniem` | новая; в тексте ссылки на `bixbit.tech/ru/*` [решение команды] | ~2026-11-07 |

---

## 6. Решения за командой

| # | Вопрос | Что блокирует |
|---|---|---|
| 1 | **Приоритет RU** (content-plan §5, вопрос 1). В RU-блоге 931 клик за 90 дн против 271 в EN, но CLAUDE.md ставит в приоритет EN | Все RU-строки |
| 2 | **Переезд `/ru` → `bixbit.tech`** (упомянут в `reports/crawl-2026-09-28.md`) [VERIFY]. Если он будет, RU-обновления делать после переезда с картой 301. Заодно решить судьбу копии S19-поста на `bixbit.tech`, которую цитирует ChatGPT (competitor-gap ePIC) | RU-план, GEO по EN-OCT-1 |
| 3 | **Группа A (похоже на инвест-советы):** noindex или переписать; EN 2, RU 12 | Бренд-риск; первое решение |
| 4 | **Группы B и C:** пакетный noindex или 410 после проверки бэклинков (`offpage-seo`, DataForSEO backlinks) | Размывание тематики |
| 5 | **Объединения с 301:** K1 (`announcement-…`), K2 (`…over-50`), K5 (`immersionnoe-…`), K6 (`kak-obnovit-…`), K9, EN-JAN-3, RU-JAN-3, EN-APR-4, EN-JUN-2, дубли RU-слагов | Соответствующие строки |
| 6 | **Пост про PUE:** оставляем как ДЦ-вход в кластер охлаждения (рекомендация) или считаем нерелевантным | EN-OCT-3 |
| 7 | **Авторы-инженеры** для подписи постов про прошивки и охлаждение, где лежат тесты (content-plan §5, вопрос 10) | E-E-A-T всех P0/P1 |
| 8 | **L7 и M7x:** поддерживает ли прошивка BiXBiT Antminer L7 и серию Whatsminer M7x (в меню есть «Antminer L7», `-m7x` стоит noindex) | EN-OCT-4, EN-JAN-2 |
| 9 | **Слаги новых постов** (EN-NOV-1, EN-NOV-2, EN-DEC-1, EN-JAN-1…3, EN-FEB-1/2, EN-MAR-2/4, EN-APR-1/2, EN-MAY-1/3, EN-JUN-1) | Публикация |
| 10 | **Ссылки из RU-блога на `bixbit.tech`** (новый пост `asic-i-pul-…` ведёт на `bixbit.tech/ru/firmwares`, `/ru/ams`): это осознанная политика для RU-аудитории или ошибка шаблона? | Спринт ссылок RU, RU-OCT-1/2 |
| 11 | **Рефреш `/en/products/container`** — когда выходит (бриф `content/briefs/hardware-mining-container.md`)? Пост EN-NOV-4 публикуем вместе с ним или после | EN-NOV-4 (окно спроса — октябрь–ноябрь) |
