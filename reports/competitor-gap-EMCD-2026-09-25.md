# Competitor Gap: BiXBiT vs EMCD (emcd.io)

**Дата:** 2026-09-25 · **Рынки:** US/EN, KZ/RU. DataForSEO Labs не поддерживает Россию, поэтому СНГ представлен Казахстаном. · **Предыдущий отчёт:** `competitor-gap-EMCD-2026-06-19.md` (без DataForSEO)
**Тип конкурента:** EMCD — майнинг-пул и медиа, а не вендор прошивок. Конкурирует с BiXBiT за информационные запросы и за то, откуда LLM берут сведения о прошивках. Раздел `/fw/` у EMCD работает в партнёрстве с Vnish `[VERIFY]`.

**Источники:**
- DataForSEO Labs: US и KZ/ru; для Казахстана и России в Labs нет данных.
- DataForSEO Backlinks: топ-1000 из 2 649 доменов EMCD, плюс зонды.
- DataForSEO AI Optimization: 64 ответа LLM, из них 40 переиспользованы из прогона по ePIC.
- DataForSEO On-Page: Lighthouse, instant_pages, краул на 40 страниц.

**Недоступно:** PageSpeed (500), CrUX (403), Moz и Bing. curl запрещён, обходных путей не использовали. Через WebFetch пришёл только заголовок статьи EMCD.

Подробные отчёты по направлениям: `reports/sub/competitor-gap-EMCD-{content,backlinks,geo,tech}-2026-09-25.md`.

---

## Executive Summary

| Измерение | BiXBiT | EMCD | Лидер |
|---|---|---|---|
| Органика US (ключей / ETV) | 162 / 115 | 955 / 267 (из них 358 про майнинг) | EMCD по объёму |
| Прошивки / охлаждение / мониторинг в US | Whatsminer #3, asic monitor #7, immersion #1–2 | 2 firmware-ключа, оба ниже топ-30; охлаждения и мониторинга нет | **BiXBiT** |
| Общие ключи | Выше в 9 из 14 | 5 из 14 | **BiXBiT** |
| Ссылающиеся домены (main) / spam score | 885 / 44 | 2 649 / 35 | **EMCD** |
| Цитирование в LLM по сравнениям прошивок | Назван в 2 из 10 ответов, которые ссылаются на EMCD | emcd.io в 8 из 24 сравнительных ответов (33%) | **EMCD** |
| hreflang / языки | 2 шаблона / en, ru | Все страницы, x-default / 5 языков | **EMCD** |
| Производительность (TBT, CLS, TTFB) | 0.4–0.8 с / 0.001 / 40 мс | 5–8.5 с / 0.096 / 300–400 мс | **BiXBiT** |

**Вывод.** По коммерческим запросам EMCD не конкурент. Он опасен одной статьёй-сравнением: она «кормит» Perplexity, Claude и Gemini и не упоминает BiXBiT. Ещё EMCD сильнее на СНГ-рынке и в мультиязычной технической инфраструктуре.

**Июнь → сентябрь.** В июне писали, что эта статья EMCD стоит #1 в SERP. Это **не подтвердилось**: в Labs её нет, и на первой странице по «best custom asic firmware» её тоже нет. Но LLM её активно цитируют, то есть она опасна в GEO, а не в классическом SEO.

---

## 1. Content / keyword gap

| Ключ | Vol | EMCD | BiXBiT | P | Что делать |
|---|---|---|---|---|---|
| asic miners profitability / asic miner profit / asic miner profitability / asic miners profit | 590 / 590 / 480 / 480 | 14 / 19 / 16 / 14 | — | P1 | Конкурировать: объяснить экономику через J/TH и TCO, дать калькулятор (`/en/calc`), **без обещаний доходности** |
| асики (KZ/ru) | 880 | 11 | — | P1 | Конкурировать через /ru-хаб |
| майнинг ферма (KZ/ru) | 590 | 25 | — | P1 | Конкурировать через /ru |
| bitmain firmware | 140 | 36 | 45 | P1 | Добавить синоним «Bitmain» на `/en/firmwares/antminer` |
| asic crypto mining | 590 | 18 | 36 | P2 | Обновить пост про asic evolution |
| miner efficiency (KD 6) | 50 | 37 | — | P1 | Страница J/TH и efficiency tuning |
| прошивка для асиков (KZ) | нет данных | — | — | **P0** | Первая страница выдачи слабая (форумы, YouTube, Avito). Сделать /ru-страницу и попросить operativa.ru (#3, упоминает прошивку BiXBiT для S9k в статье 2022 года) обновить статью и поставить ссылку |
| Antminer S9 | 590 | 16 | — | P3 | Только если S9 ещё поддерживается `[VERIFY]` |

**BiXBiT впереди:** antminer firmware (15 против 34), what is asic miner (16 против 49), whatsminer firmware (#3), asic monitor (#7), immersion и mineral oil (#1–2), immersion computer cooling (390, #15), стойки и контейнеры.

## 2. Link gap

| Домен | Тип | P | Угол | Cross-gap |
|---|---|---|---|---|
| criptonoticias.com | LatAm-медиа, ES | **P0** | PR-питч | ePIC + EMCD |
| miningdisrupt.com | Конференция | **P0** | Спикер, спонсорство (`rel=sponsored`) | ePIC + EMCD |
| bitcoinminingstock.io | Медиа | **P0** | Новостной питч | ePIC + EMCD |
| digitalcurrencyresearch.io | Исследования | **P0** | Данные, экспертный комментарий | ePIC + EMCD |
| asicminervalue.com | ASIC-каталог (rank 297) | P1 | Добавить в листинг | — |
| onlybestminers.com | Обзоры и магазин (238) | P1 | Обзор прошивки | — |
| miner.ae | Майнинг-сервис, ОАЭ | P1 | Партнёрство, передать BD | — |
| asicprices.com | Агрегатор цен, US | P1 | Листинг | — |
| beincrypto.com | Медиа | P1 | Экспертная колонка | — |
| kernelpanicpodcast.com, yesmining.io | Подкаст, хостинг | P1 | Гостевой эфир, партнёрство | ePIC + EMCD |

**Сам EMCD как цель.** Ссылки из статей EMCD нереалистичны: EMCD не ссылается ни на одного вендора прошивок. Реалистичны два пути: (1) попросить добавить BiXBiT в их статью-сравнение, это даёт GEO-эффект; (2) переговоры по `/fw/`, где сейчас Vnish. Оба пути идут через BD, не через SEO.

**Риск.** 18 общих «ссылающихся доменов» у BiXBiT и EMCD — это одна xyz-сеть (`link-legion-*.xyz`, `seo-anomaly-top-*.xyz`). Это кандидаты в disavow, **решение за человеком**.

**BiXBiT впереди:** на BiXBiT, но не на EMCD ссылаются minecool.ru, bigstarmining.com, kryptex.com, coindoo.com, newscrypto.net, uol.com.br, pdsdigital.com.py (Парагвай) и prnewswire. С bitcointalk у BiXBiT 177 ссылок, у EMCD 22; с irlbtc — 104 против 6.

## 3. AI-citation gap (измерено)

| URL EMCD, который цитируют LLM | Цитирований | BiXBiT в ответе | P |
|---|---|---|---|
| `/articles/mining/best-custom-asic-firmware-vnish-vs-braiins-os-vs-luxos/` | 8 из 10 | Почти никогда | **P0** |
| `/ru/articles/kriptovalyuta/kak-uvelichit-dohod-ot-majninga/` | 1 (Gemini: «EMCD официально партнёрится с VNISH») | — | P2 |
| `/monitoring/` и статья btc-tools | 1 | — | P3 |

Цитирование по движкам: Perplexity 4, Claude 3, Gemini 3, **ChatGPT 0/16**, Google AIO 0/11. BiXBiT силён в запросах на русском: запрос про S21 для СНГ назвал BiXBiT в 3 из 4 ответов, запрос на русском про прошивки — в 2 из 4 (со ссылкой на bixbit.io/ru).

**LLM искажают факты о BiXBiT:** «~2% dev fee», «30-day trial», «up to 40%», «русский разработчик». Всё это `[VERIFY]` → нужен канонический блок фактов и llms.txt.

## 4. Технический gap

| Фактор | BiXBiT | EMCD | P | Исправление |
|---|---|---|---|---|
| hreflang | 2 из 10+ шаблонов | Все страницы, x-default, взаимные ссылки | **P0** (открыт ещё с 09-16) | Добавить hreflang во все шаблоны |
| Связь переводов | Нет | Свой slug у каждого перевода, связаны через hreflang | P1 | Поле «translation of» в CMS |
| Языки | en, ru | en, ru, pt-BR, es, zh | P2 | ES и PT под LatAm, передать `international-seo` |
| Вес firmware-страницы | 23.8 MB, LCP 42 с | `/fw/` 6.9 MB, LCP 13 с | P0 (уже есть в плане ePIC) | Сжать изображения |

**Не копировать у EMCD:** даты не в ISO, нет `dateModified`, относительные URL в schema, нет JSON-LD на главной и `/fw/`, английский текст в разделах `/de/`, `/fr/`, `/id/`.

---

## 5. План закрытия

**Quick wins (≤ 2 недели)**
1. **Прочитать статью-сравнение EMCD вручную** (WebFetch отдал только заголовок), затем отправить питч с фактшитом и предложить добавить Whatsminer и BiXBiT. P0.
2. В первом абзаце firmware-страниц явно назвать Whatsminer. Claude повторяет за d-central, что Vnish — «единственная» прошивка для обоих брендов. P0.
3. Канонический блок фактов и llms.txt, чтобы LLM перестали искажать факты. Общая задача с планом ePIC.
4. Синоним «Bitmain» на Antminer-странице.

**30–60 дней**
- `/en/firmwares/comparison` + `/ru/`: прямой ответ на запросы вида «Vnish vs Braiins vs LuxOS», все спеки `[VERIFY]`. Общая задача с планом ePIC.
- /ru-кластер: «прошивка для асиков», «асики», «майнинг ферма», FAQ на русском с рабочей FAQPage-разметкой.
- Материал про экономику J/TH и TCO под запросы о доходности, без обещаний доходности.
- hreflang во все шаблоны.
- Аутрич в 4 cross-gap P0-домена и в operativa.ru, отдельный раздел BiXBiT на Kryptex.

**60–90 дней:** BD-переговоры по `/fw/` EMCD, локали ES и PT, аудит xyz-сети.

**Не делать:** конкурировать с EMCD в GPU, pool и altcoin-контенте (P3, вне ICP).

## 6. [VERIFY] для человека
- Партнёрство EMCD и Vnish.
- Что сейчас написано в статье-сравнении EMCD.
- Поддерживается ли S9.
- Факты о BiXBiT, которые искажают LLM: dev fee, trial, «+40%», страна разработчика.
- Dev fee конкурентов, указанные в статьях EMCD.
