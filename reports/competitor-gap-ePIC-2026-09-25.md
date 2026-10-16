# Competitor Gap: BiXBiT vs ePIC (epicblockchain.io)

**Дата:** 2026-09-25 · **Рынок:** US / EN · **Предыдущий отчёт:** `competitor-gap-ePIC-2026-06-19.md` (тогда DataForSEO был недоступен, поэтому использовались WebSearch и self-test)

**Источники:** DataForSEO Labs (ranked_keywords, domain_intersection, domain_rank_overview), Backlinks (summary, referring_domains, anchors), AI Optimization (ChatGPT / Perplexity / Claude / Gemini / AI Overview / LLM mentions), On-Page (Lighthouse, instant_pages).
**Недоступно:** PageSpeed API (ошибка 500), CrUX (403), поэтому полевых CWV нет. Moz и Bing не подключены (нет ключей). Часть SERP-запросов упала с ошибками `40101`/`40106`.

Подробности по каждому направлению лежат в `reports/sub/competitor-gap-ePIC-{content,backlinks,geo,tech}-2026-09-25.md`.

---

## Executive Summary

Июньский вывод «ePIC опережает BiXBiT» **реальными данными не подтвердился**:

| Измерение | BiXBiT | ePIC | Лидер |
|---|---|---|---|
| Органика US (ключи / ETV) | 162 / 115 | 10 / 14.6 (весь топ-20 брендовый) | **BiXBiT** |
| Ссылающиеся домены (main) | 885 | 170 | BiXBiT по объёму |
| Качество ссылок (spam score / доля dofollow / гео) | 44 / ~44% / TR, RU, UA | 13 / ~65% / US, CA | **ePIC** |
| AI-упоминания (50 ответов, измерено) | 13/50 | 7/50 | **BiXBiT** |
| ChatGPT (ответы про firmware) | 0/8 | 3/8 | **ePIC** |
| Запрос «lowest dev fee» в LLM | 0/5 | 4/5 | **ePIC** |
| Скорость firmware-страницы (lab LCP) | 42 с, 23.8 MB | 9 с, 2.0 MB | **ePIC** |
| TTFB / LCP главной | ~40 мс / 2.75 с | 2.3 с / 51.5 с | **BiXBiT** |

ePIC выигрывает по трём направлениям: **нарратив dev fee**, **качество ссылочного профиля** и **ChatGPT**. BiXBiT выигрывает по органике, Whatsminer, охлаждению, AI-упоминаниям в целом и скорости сервера.

---

## 1. Content / keyword gap

| Ключ | Vol (US) | ePIC | BiXBiT | Приоритет | Действие |
|---|---|---|---|---|---|
| firmware dev fee | нет данных | 4 (пресс-релиз о dev fee 1.5% `[VERIFY]`) | — | **P0** | Страница `/en/antminer-firmware/dev-fee` (или `/en/firmwares/dev-fee`), аргумент через TCO, а не «самая низкая комиссия» |
| antminer custom firmware | 10 | 7 (гайд по установке) | 5 | P1 | Сделать отдельную страницу-гайд по установке |
| antminer autotuning | нет данных | SERP упал | — | P1 | Повторить сбор |
| brand: epic miner / epic mining / blockminer | 90 / 90 / 210 | 2 / 9 / 23 | — | P2 | Страница «BiXBiT vs ePIC» |
| epic umc (+100% YoY) | 20 | — | — | P2 | Сравнение: полностью программная прошивка против замены контроллера |

**Где выигрывает BiXBiT:** whatsminer firmware (20/mo, позиция 3), whatsminer custom firmware (позиции 2 / 6 / 16), asic monitor (70, позиция 7), immersion cooling mining (14 против 30 у ePIC), mineral oil for immersion cooling (позиция 1), «antminer mineral oil» ×3 (позиция 2). Всего 13 cooling-ключей в топ-20. По охлаждению, AMS и PDU у ePIC **ноль** позиций.

**Найдена ошибка в наших брифах:** в брифах Antminer и Whatsminer в `content/` написано «no dev fee». Подтверждённый dev fee — 2.8% (2% на M2x) `[VERIFY]`. **Исправить до публикации (P0).**

## 2. Link gap

119 доменов ссылаются на ePIC, но не на BiXBiT (множества сравнивались локально, потому что фильтр в API `domain_intersection` не сработал).

| Домен | Rank | Тип | P | Угол аутрича |
|---|---|---|---|---|
| altairtech.io | 118 | ASIC-реселлер | P0 | Партнёрский листинг |
| lightspeedhosting.com | 109 | Майнинг-хостинг | P0 | Кейс или гостевой пост |
| miningdisrupt.com | 55 | Конференция | P0 | Слот спикера (платные ссылки только с `rel="sponsored"`) |
| criptonoticias.com | — | LatAm-медиа (ES) | P0 | PR-питч |
| tokenradar.io | 84 | Обзоры | P1 | Попасть в обзоры «best ASIC firmware» |
| hashrateindex.com | — | Данные / медиа (принадлежит Luxor) | P1 | Предложить данные (шансы низкие) |
| kernelpanicpodcast.com, ungovernablemisfits.com | — | Подкасты | P1 | Гостевой эфир |
| blocktribune.com, nobsbitcoin.com | — | Новости | P1 | Новостной питч |

**Риск (P1):** 391 домен BiXBiT со spam score ≥ 50 даёт ~57% всех бэклинков (кластеры .online/.website/.space/.site, .com.tr, .xyz). Всплески новых доменов были в 2025-09/10 и 2026-01. Рекомендация: ручной аудит и disavow только явного спама, решение за человеком. **Ничего не отклонено.**

## 3. AI-citation gap (измерено через DataForSEO)

| Источник, который кормит LLM | Упоминаний ePIC | BiXBiT | P |
|---|---|---|---|
| d-central.tech | 8 | нет (проверено 2 страницы сравнений) | **P0** |
| spark.money | 4 | нет (в сравнении у ePIC указано 1.5%) | P0 |
| prnewswire / einpresswire | пресс-релиз ePIC о dev fee | — | P1 (собственный пресс-релиз) |
| github.com | 3 | — | P2 |
| altairtech.io, hashrateindex.com | 2 / 2 | — | P1 (совпадает с link-gap) |

Главный пробел — **ChatGPT**: bixbit.io процитирован 0 раз из 11 ответов. ChatGPT цитирует `bixbit.tech`, из-за чего цитирования уходят с основного домена `[VERIFY: принадлежит ли домен BiXBiT → настроить 301 на bixbit.io]`.

## 4. Технический gap

| Фактор | BiXBiT | ePIC | P | Исправление |
|---|---|---|---|---|
| Вес `/en/firmwares/antminer` | 23.8 MB, LCP 42 с | 2.0 MB, LCP 9 с | **P0** | Перевести 8 картинок по 0.8–3.3 MB в AVIF/WebP с srcset, предзагрузить hero, lazy-load для остальных |
| Валидность HTML | Дублирующийся `<body>`, незакрытый тег (строки 45–46) | 0 ошибок | P1 | Исправить шаблон |
| og:image / Twitter Cards | Favicon, Twitter-тегов нет | Отдельные картинки для каждой страницы, `summary_large_image` | P1 | Сделать OG-картинки для каждой страницы |
| Schema | Блоки не связаны, `WebSite.url` = URL текущей страницы, на Antminer нет `SoftwareApplication` | Связанный `@graph` | P1 | Объединить `@graph` через `@id` |
| Sitemap | Без авто-lastmod, нет image sitemap | Авто-lastmod, 132 image-записи | P2 | Сделать генератор |
| HSTS / Best Practices | Нет / 0.73–0.77 | Есть / 0.92–1.00 | P2 | Добавить заголовок |
| llms.txt | 404 | 404 | P1 (шанс опередить) | Создать |

**BiXBiT впереди:** TTFB 40 мс против 2.3 с; LCP главной 2.75 с против 51.5 с; CLS 0.001 (июньское значение 0.888 не воспроизвелось, подтвердить полевыми данными); `SoftwareApplication` на Whatsminer; сайт на en и ru; 106 статей в EN-блоге против 34.

---

## 5. План закрытия

**Quick wins (≤ 2 недели)**
1. Исправить «no dev fee» в брифах `content/`. P0, 15 минут.
2. Сжать картинки на `/en/firmwares/antminer`. P0, самый заметный технический эффект.
3. В начале `/en/firmwares` дать одну каноническую фразу про поддержку Antminer и Whatsminer, плюс HTML-таблицу с dev fee и поддерживаемыми моделями `[VERIFY]`. Ту же фразу использовать в schema и llms.txt.
4. Создать llms.txt. Поправить пустую FAQ-schema и добавить FAQ про безопасность и бэкдоры.
5. Проверить `bixbit.tech` и `bixbitusa.io` (видны в выдаче и в LLM) и склеить их с основным доменом 301-редиректом.

**30–60 дней**
- Контент: страница про dev fee и TCO, сравнение прошивок с колонкой ePIC (hashrateindex стоит на 4-й позиции по «best asic firmware», BiXBiT на 18-й), страница «BiXBiT vs ePIC», гайд по установке. Перенести «immersion cooling mining» с блог-поста про жидкости на коммерческий пиллар.
- Ссылки и GEO: аутрич в d-central.tech, spark.money, altairtech.io, lightspeedhosting.com, tokenradar.io с фактшитом.
- Тех: HTML-шаблон, OG, связанный `@graph`, HSTS, sitemap.

**60–90 дней:** собственный wire-релиз, конференции (Mining Disrupt), подкасты, аудит спам-профиля.

## 6. [VERIFY] для человека
- dev fee ePIC 1.5% и Perpetual Tune (указаны в пресс-релизах и ответах LLM).
- Dev fee BiXBiT 2.8% / 2% M2x и версия прошивки 1.8.1.
- Принадлежность `bixbit.tech` и `bixbitusa.io`.
- Пост в EN-разделе с транслитерированным русским URL.
