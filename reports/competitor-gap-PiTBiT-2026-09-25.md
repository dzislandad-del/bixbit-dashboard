# Competitor Gap: BiXBiT vs PiTBiT (pitbitecosystem.com + pitbit.online)

**Дата:** 2026-09-25
**Рынки:** US/EN, KZ/RU, UA/RU. Россия и Беларусь недоступны в DataForSEO (ошибка 40501).
**Предыдущий отчёт:** `competitor-gap-PiTBiT-2026-06-19.md` (без DataForSEO)
**Тип конкурента:** прямой конкурент в прошивках для Antminer и Elphapex и в облачном мониторинге. Рынок — СНГ. Whatsminer, охлаждения и PDU нет `[VERIFY]`.

**Источники:**
- DataForSEO Labs, Keywords Data, SERP (KZ/ru)
- DataForSEO Backlinks: 9 запросов, все успешны
- DataForSEO AI Optimization: 84 ответа LLM, из них 64 переиспользованы из прогонов ePIC и EMCD, плюс LLM Mentions
- DataForSEO On-Page: Lighthouse, instant_pages, raw HTML
- WebFetch: 4 страницы

**Недоступно:**
- PageSpeed (500), CrUX (403), Moz, Bing
- Российская выдача, то есть домашний рынок PiTBiT. Следующий шаг — GSC по `/ru`.

Подробности: `reports/sub/competitor-gap-PiTBiT-{content,backlinks,geo,tech}-2026-09-25.md`.

---

## Executive Summary

| Измерение | BiXBiT | PiTBiT | Лидер |
|---|---|---|---|
| Органика US | 162 кл. / ETV 115 | 4 ключа на оба домена, 0 в топ-20 | **BiXBiT** |
| Органика KZ/ru | 6 ключей + выдача: «прошивка whatsminer» #1, «мониторинг асиков» #3 | 0 ключей; YouTube-видео #1 по «прошивка s19» | BiXBiT, но PiTBiT силён в видео |
| Индексируемость EN | ОК | EN закрыт: `noindex` конфликтует с `index`, в sitemap нет `/en/` | **BiXBiT** |
| Страницы прошивки по моделям (ru) | Хаб; 7 старых страниц моделей закрыты noindex | 26 индексируемых страниц моделей | **PiTBiT** |
| Ссылающиеся домены (main) | 885 | 47 + 49; около 15 реальных, все RU | **BiXBiT** |
| AI-упоминания без бренда в промпте | 28/84 (33%) | 1/84 | **BiXBiT** |
| Запрос с брендом («pitbit или vnish») | BiXBiT предложен как альтернатива в 1/8 | Отвечают по собственным страницам PiTBiT | PiTBiT |
| Каналы вне Google | — | YouTube 39.7K, Telegram, Avito | **PiTBiT** |

**Вывод.** PiTBiT почти не присутствует в Google и LLM. Реальных угроз три:
1. **Факты PiTBiT попадают в ответы о BiXBiT.** Claude приписал BiXBiT dev fee PiTBiT 2.75% и его модельный ряд, сославшись на altcoinlog.com. В этой статье раздел PITBIT стоит сразу перед разделом Bixbit.
2. **Видео в выдаче по моделям** («прошивка s19»).
3. **Страницы по отдельным моделям** на русском сайте.

**Июнь → сентябрь:**
- Опровергнуто: «оба бренда одинаково слабы в AI». BiXBiT упоминается в 28 раз чаще.
- Опровергнуто: altcoinlog и ultramining как доноры PiTBiT. У BiXBiT там уже есть ссылки.
- Подтверждено: top-mining.ru и cryptodesk.ru.

---

## 1. Content / keyword gap

| Запрос (KZ/ru, live SERP) | Vol | PiTBiT | BiXBiT | P | Действие |
|---|---|---|---|---|---|
| прошивка antminer | 10 | — | — | **P0** | В топ-20 нет ни одного вендора, только YouTube, форумы, reddit и зеркала. Сделать /ru-хаб Antminer |
| прошивка s19 / s21 | 10 / н/д | Видео на YouTube #1 | — | P1 | /ru-страницы моделей S19 и S21 с таблицей режимов `[VERIFY]` плюс видео |
| программы для мониторинга асиков | н/д | — | — | P1 | Сравнительная /ru-страница; такой формат уже стоит на #4 |
| мониторинг асиков | 10 | — | **#3** (`/ru/ams`) | P2 | Добавить запрос в title `/ru/ams` |
| прошивка whatsminer | 10 | — | **#1, #6, #12** + видео-блок | P2 | Добавить CTA на страницу документации |
| bixbit прошивка отзывы (подсказка Google) | н/д | — | — | P1 | Страница с отзывами и кейсами |
| bitmain warranty check (US) | 110 | #29 (`/en/warranty/`) | — | P3 | Вне ICP |

Брендовый спрос в KZ: BiXBiT (bixbit + биксбит) — 30 в месяц, PiTBiT — 20.

## 2. Link gap

| Домен | Тип | P | Угол | Cross-gap |
|---|---|---|---|---|
| top-mining.ru | СНГ-медиа, рейтинги | **P0** | Карточка бренда и место в рейтинге «Топ-6 прошивок» | EMCD + PiTBiT |
| rushash.ru | Майнинг-хостинг | **P0** | Партнёрский блок, передать BD | EMCD + PiTBiT |
| trustmining.ru | Каталог | **P0** | Профиль компании `[VERIFY: бесплатно ли]` | — |
| dc-mining.ru | Хостинг, газовые площадки | P1 | Совместный продукт, передать BD | — |
| cryptodesk.ru | Блог магазина ASIC | P1 | Обзор прошивки и AMS | — |
| hidix.ru | Медиа | P1 | Гостевой туториал `[VERIFY: модели и цифры]` | — |
| crypto-emergency.com | Медиа, Blockchain Life Dubai | P1 | Пресс-кит `[VERIFY: участвует ли BiXBiT]` | — |
| kernelpanicpodcast.com | Подкаст | P1 | Гость-инженер. **Сначала проверить вручную:** spam score 70 | ePIC + EMCD + PiTBiT |

**BiXBiT впереди:** в СНГ у BiXBiT есть bits.media (34 ссылки), miningclub.info, minecool.ru, forklog, habr, altcoinlog, ultramining. На английском — bitcointalk (177), b.tc, d-central.tech, prnewswire. **У PiTBiT англоязычных отраслевых доноров нет.**

## 3. AI-citation gap (измерено)

| Источник | Что с ним не так | P | Действие |
|---|---|---|---|
| altcoinlog.com | LLM путают разделы PITBIT и Bixbit, BiXBiT получает dev fee 2.75% и модели PiTBiT | **P0** | Попросить разделить разделы и обновить факты о BiXBiT |
| ultramining.com | Спонсорская статья о PiTBiT | P2 | — |
| YouTube («PITBIT V2 S21 Pro 300TH»), Telegram t.me/s/PitBitPro, LinkedIn | Называют только PiTBiT | P1 | Собственные видео и Telegram BiXBiT |
| crazy-mining.org, saashub | Ложные факты о BiXBiT: «-50% downvolt», «+80 TH/s» | P1 | Запросить исправления |
| top-mining.ru, cryptorussia.ru | Называют оба бренда | P2 | Исправить факты, не добавлять бренд заново |

**Ошибки о BiXBiT в ответах LLM на русском (для блока фактов, всё `[VERIFY]`):**
- «BiXBiT, Россия»
- «BiXBiT Prime firmware»
- Двухфазные иммерсионные профили
- «devfee 2,75% или единоразовая оплата» (это модель PiTBiT)
- «1.8–2.8% DevFee» (altcoinlog)
- Рекомендация по S21 со ссылкой на старый пост про S17

По запросу про облачный мониторинг BiXBiT назван в 0 ответах из 4. Perplexity пишет, что на bixbit.io это неочевидно.

## 4. Технический gap

| Фактор | BiXBiT | PiTBiT | P | Исправление |
|---|---|---|---|---|
| Страницы прошивки по моделям | Хаб; 7 старых страниц моделей закрыты noindex | 26 индексируемых страниц на ru | **P1** | Шаблон `/{en,ru}/firmwares/antminer/{model}`, только где есть уникальный контент; список моделей `[VERIFY]` |
| Organization schema | Базовая | legalName, foundingDate, address, contactPoint, sameAs | P2 | Заполнить поля, все значения `[VERIFY]` |
| Вес firmware-страницы | 23.8 MB, LCP 42 с | 6.5 MB, LCP 3.7 с | P0 (уже есть в плане ePIC) | Сжать изображения |

**BiXBiT впереди:**
- Индексация EN, meta, schema, hreflang (у PiTBiT hreflang нет)
- TTFB 37 мс против 253–1048 мс
- Производительность главной 0.87 против 0.44
- CLS

Разделение бренда на три домена (сайт, pitbit.online, pitbit.pro) — скорее минус для PiTBiT: страница приложения — логин на 21 слово без H1 и без ссылки на основной сайт.

---

## 5. План закрытия

**Quick wins (≤ 2 недели)**
1. **Блок фактов и llms.txt.** Добавить строку о ценовой модели: только dev fee, без единоразовой лицензии `[VERIFY]`. Указать официальные названия продуктов и страну. P0, общая задача с планами ePIC и EMCD.
2. **Аутрич в altcoinlog.** Попросить разделить разделы PITBIT и Bixbit и обновить факты. P0.
3. **Фраза на `/firmwares`** о том, что прошивка управляется через облачный мониторинг AMS. P0.
4. **Title `/ru/ams`** — добавить «мониторинг асиков». CTA на странице документации Whatsminer, которая стоит на #1.
5. **`launch.bixbitusa.io`** — связать с bixbit.io `[VERIFY: домен наш]`.

**30–60 дней**
- /ru-хаб Antminer под «прошивка antminer»: на первой странице выдачи нет ни одного вендора.
- Страницы моделей S19 и S21 на ru и en.
- /ru-сравнение программ мониторинга.
- Страница с отзывами и кейсами.
- Аутрич: top-mining.ru, rushash.ru, trustmining.ru, cryptodesk.ru, hidix.ru, листинги мониторинга (headframe.io, tcs-mining.ru, hashrate.ru, bitexpert.io).
- Исправить листинг на saashub.

**60–90 дней**
- Видео на русском по S19, S21 и T21.
- Telegram-канал.
- Партнёрства с хостингами в СНГ (rushash, dc-mining), через BD.
- Подключить GSC для измерения RU-выдачи.

## 6. [VERIFY] для человека
- Факты о PiTBiT: dev fee 2.75%, 28 моделей, 90k+ устройств, 6k+ клиентов (данные июня).
- Ценовая модель BiXBiT и есть ли единоразовая лицензия.
- Страна и юрлицо BiXBiT для Organization schema.
- Участвует ли BiXBiT в Blockchain Life.
- Список поддерживаемых моделей для страниц моделей.
- Принадлежит ли BiXBiT `launch.bixbitusa.io`.
