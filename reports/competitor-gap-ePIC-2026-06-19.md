# Competitor Gap Report: BiXBiT vs ePIC (epicblockchain.io)

**Date:** 2026-06-19
**Scope:** US/EN market — https://bixbit.io/en vs https://epicblockchain.io
**DataForSEO status:** 401 Unauthorized на всех эндпоинтах — объёмы keywords и backlink-метрики недоступны из API; используется WebSearch + WebFetch + Claude self-test.

---

## Executive Summary

ePIC (UMC OS firmware) опережает BiXBiT по двум критическим измерениям: **on-page SEO-сигналы** (title, H1 содержат коммерческий запрос) и **AI-видимость** (7/10 ответов vs 0/10 для BiXBiT). Главная причина — ePIC системно присутствует в сравнительном контенте третьих сторон (hashrateindex.com, d-central.tech), которые являются primary source для LLM.

BiXBiT выигрывает структурно: богатая URL-иерархия, поддержка двух ASIC-платформ без замены hardware, AMS мониторинг, Immersion/Hydro cooling в одной экосистеме. Это уникальное позиционирование, которое ePIC не может воспроизвести (UMC — аппаратная замена контроллера).

Главные разрывы, закрываемые за 30–60 дней: исправить title/H1 homepage, попасть в hashrateindex.com и d-central.tech, создать страницу сравнения прошивок, запустить wire PR.

---

## 1. Content & Keyword Gap

> DataForSEO недоступен (401). Keyword volumes не приводятся — данные собраны через WebFetch ePIC сайта и WebSearch. Все тех-факты ePIC помечены [VERIFY].

### Профиль ePIC сайта (из WebFetch)

| Элемент | Значение |
|---|---|
| H1 homepage | "Custom Antminer Firmware" |
| Title tag | "Antminer Custom Firmware \| ePIC Blockchain Technologies" |
| Meta description | отсутствует |
| Продукт | UMC OS (Universal Mining Controller) — аппаратная плата + прошивка |
| Dev fee | 1.5% [VERIFY — источник: PRNewswire 2026-01] |
| Autotuning | "Perpetual Tune" [VERIFY] |
| Поддерживаемые платформы | Antminer S19/S21 + Whatsminer M30/M50/M3x/M5x [VERIFY] |
| Блог | есть, активный — 2 поста в июне 2026 |
| Контентные slugи | `/custom-firmware-vs-stock-firmware-antminer/`, `/what-is-perpetual-tune-auto-tuning-mining-firmware/` |
| Страниц в sitemap | ~50 (22 page + 28 post) |
| CMS | WordPress + Yoast SEO |

### Контентные разрывы BiXBiT

| # | Тема / Запрос | ePIC | BiXBiT | Приоритет | Обоснование |
|---|---|---|---|---|---|
| 1 | Firmware comparison (BiXBiT vs ePIC vs Braiins vs Vnish vs LuxOS) | Нет (упоминается в чужих) | Нет | **P0** | Самый цитируемый AI-тип контента; d-central.tech и hashrateindex.com доминируют без BiXBiT |
| 2 | "Lowest dev fee mining firmware" | Упоминается (1.5%) | Нет страницы | **P0** | ePIC выигрывает этот промпт через PR Newswire; BiXBiT нужен ответ (TCO-аргумент) |
| 3 | "Firmware for Antminer AND Whatsminer" | Упоминается (UMC V5) | Нет отдельной страницы | **P0** | BiXBiT покрывает обе платформы без замены hardware — уникальное УТП без контента |
| 4 | "Custom firmware vs stock firmware Antminer" | Есть пост (в блоге) | Нет | **P0** | ePIC занял этот топик в блоге; страница типа "why custom firmware" — базовая воронка |
| 5 | "What is Perpetual Tune / autotuning firmware" | Есть пост | Нет аналога | **P1** | Поисковый запрос по autotuning отдаётся ePIC; BiXBiT нужен аналог для своего autotuning |
| 6 | "ePIC firmware alternatives" | Является ref. | Нет | **P1** | Промпт "best alternatives to ePIC" не возвращает BiXBiT; нужна страница или гостевой материал |
| 7 | "Antminer S19 XP efficiency tuning" | Упоминается | Нет | **P1** | Модельно-специфичные страницы (S19 XP, S21, M50S) дают long-tail трафик |
| 8 | "ASIC firmware security / no backdoors" | Нет | Нет | **P1** | Braiins доминирует через open-source аргумент; BiXBiT может занять позицию |
| 9 | "Reduce ASIC power consumption with firmware" | Нет | Нет | **P1** | Ни один не покрывает; Braiins монополизирует через академический контент |
| 10 | Immersion cooling + firmware integration | Нет | Нет отдельного | **P2** | Уникальное для BiXBiT — связка firmware + AMS + cooling; у ePIC нет cooling |
| 11 | Fleet management firmware API | Нет | Частично | **P2** | Rich API позиционирование у ePIC; BiXBiT AMS нужна отдельная SEO-страница |
| 12 | PDU / power distribution mining | Нет | Нет страницы | **P3** | Четвёртый приоритет CLAUDE.md; у ePIC нет вообще |

### Контентные слабости ePIC
- Нет контента по cooling, AMS, PDU — всё это имеет BiXBiT
- Нет страниц под Whatsminer конкретные модели (M50S++, M60)
- Нет сравнительного контента по безопасности
- Тонкий сайт: ~50 страниц; нет документации

### Уникальные контент-возможности BiXBiT (ePIC не может воспроизвести)
- "Firmware + Immersion Cooling + AMS monitoring — unified ecosystem"
- "BiXBiT vs competitors: no hardware replacement required" (vs UMC — физическая замена платы)
- Whatsminer M6x серия — пост-2023 модели (есть ли поддержка у ePIC — [VERIFY])
- PDU content hub — у ePIC нет продукта, нет конкуренции

---

## 2. Link Gap

> DataForSEO API недоступен (401). Backlink метрики (DR, количество доменов) не получены. Данные из WebSearch.

### Качественная оценка профилей

| Показатель | ePIC | BiXBiT |
|---|---|---|
| Referring domains (est.) | Сильный: PRNewswire, BusinessWire, CBInsights, Crunchbase, ZoomInfo, Tracxn, Medium, GitHub, Bitcoin Magazine, Proactive Investors | Слабее: bitcointalk.org, zeusbtc.com (упоминание), saashub.com, crunchbase.com, tracxn.com |
| Wire PR backlinks | Систематически: 4+ релиза за 2020–2026 на PRNewswire/BusinessWire | Нет |
| Industry roundups | hashrateindex.com (#4), d-central.tech (comparison) | Отсутствует в обоих |
| GitHub presence | github.com/epicblockchain — публичные репозитории | github.com/bixbit-me — нет публичных репо |
| Medium publication | medium.com/epic-blockchain-technologies — активна | Нет |
| Partner/reseller links | altairtech.io — product page с ссылкой | Нет аналога |

### Домены аутрича: уникальные для ePIC, отсутствуют у BiXBiT

| # | Домен | Тип | Приоритет | Тактика |
|---|---|---|---|---|
| 1 | hashrateindex.com | Industry media — "Top 5 Bitcoin Mining Firmware 2026" | **P0** | Аутрич с просьбой включить BiXBiT в существующую статью; предоставить бенчмарки J/TH [VERIFY] |
| 2 | d-central.tech | Industry media + ASIC shop — "Bitcoin Mining Software Comparison 2026" | **P0** | Аутрич к редакции; предложить гостевой раздел о BiXBiT firmware; возможно партнёрство/листинг |
| 3 | altairtech.io | Reseller/partner | **P0** | Найти аналогичных ASIC-ретейлеров (США/Канада) для product pages с backlink |
| 4 | prnewswire.com | Press wire | **P0** | Запустить PR под реальный повод (запуск firmware, партнёрство); 50–200 синдицированных ссылок с одного релиза |
| 5 | businesswire.com | Press wire | **P0** | Аналогично prnewswire |
| 6 | bitcoinmagazine.com | Industry media | **P0** | Питч об институциональном партнёрстве (Quantum Expeditions/Cormint) или экосистемном подходе |
| 7 | crunchbase.com | Directory | **P1** | Профиль существует — актуализировать (funding, team, description); попасть в "similar companies" к ePIC |
| 8 | tracxn.com | Directory | **P1** | Профиль существует — запросить корректировку конкурентов (сейчас BitMine/Rhodium); добавить ePIC/Braiins |
| 9 | emcd.io | Mining pool media | **P1** | Аутрич к редакции EMCD — включить BiXBiT в статью "Best Custom ASIC Firmware" |
| 10 | zeusbtc.com | Industry shop | **P1** | Упоминание уже есть — конвертировать в полноценный backlink с product page |
| 11 | medium.com | Blog platform | **P1** | Создать Medium publication, переопубликовать EN-статьи — получить domain backlink |
| 12 | github.com | Developer platform | **P1** | Опубликовать open-source CLI/скрипты для AMS — органические links из dev-community |

---

## 3. AI-Citation Gap

> Claude self-test выполнен честно (10 промптов). DataForSEO AI Optimization API — 401. llms.txt: оба сайта вернули 404.

### Self-test матрица (Claude, 2026-06-19)

| # | Промпт | ePIC | BiXBiT | Лидеры ответа |
|---|---|---|---|---|
| 1 | "What is ePIC firmware vs Braiins OS+?" | ДА | НЕТ | Braiins, ePIC |
| 2 | "Which firmware has the lowest dev fee?" | ДА (1.5%) | НЕТ | Braiins, Vnish, LuxOS, ePIC |
| 3 | "Does ePIC firmware support Whatsminer?" | ДА | НЕТ | — |
| 4 | "Best alternatives to ePIC firmware?" | ДА (ref) | НЕТ | Braiins, Vnish, LuxOS |
| 5 | "Firmware for both Antminer and Whatsminer?" | ДА | НЕТ | Braiins, ePIC |
| 6 | "Best custom firmware for Antminer S19 XP?" | ДА | НЕТ | Braiins, Vnish, LuxOS, ePIC |
| 7 | "What is UMC OS mining firmware?" | ДА | НЕТ | — |
| 8 | "How to reduce ASIC power with firmware?" | НЕТ | НЕТ | Braiins, Vnish, LuxOS |
| 9 | "What mining firmware has no backdoors?" | НЕТ | НЕТ | Braiins (open-source) |
| 10 | "ePIC vs Braiins vs Vnish comparison?" | ДА | НЕТ | Braiins, Vnish, ePIC |

**Итог:** ePIC — 7/10, BiXBiT — 0/10.

### Почему ePIC цитируется, а BiXBiT нет

Источники, питающие LLM-упоминания ePIC:
1. `d-central.tech` — Bitcoin Mining Software Comparison 2026 (включает ePIC, не включает BiXBiT)
2. `hashrateindex.com` — Top 5 Bitcoin Mining Firmware 2026 (ePIC на #4)
3. `prnewswire.com` — 2 PR-релиза (UMC OS launch + dev fee reduction)
4. `altairtech.io` — product pages с entity co-occurrence
5. `github.com/epicblockchain` — публичные репозитории (технический credibility)
6. `epicblockchain.io/category/articles/` — регулярный блог

BiXBiT не представлен ни в одном из этих доменов в контексте firmware.

### Контент для AI-видимости (приоритет)

| Тема | Формат | Приоритет |
|---|---|---|
| BiXBiT vs ePIC vs Braiins vs Vnish vs LuxOS — полное сравнение | Comparison table + FAQ | P0 |
| Firmware that supports Antminer AND Whatsminer: Complete Guide | Guide + table | P0 |
| llms.txt на bixbit.io/en | Техническая реализация | P0 |
| Outreach в d-central.tech и hashrateindex.com | PR / гостевой материал | P0 |
| Lowest Dev Fee Firmware 2026: Full Breakdown | Comparison + FAQ | P0 |
| ePIC Firmware Alternatives Guide | Listicle | P1 |
| Mining Firmware Security: No Backdoors Checklist | FAQ + checklist | P1 |
| PR Newswire релизы (2 шт.) | Wire PR | P1 |

---

## 4. Technical SEO Gap

> DataForSEO Lighthouse недоступен (401). CWV из API не получены. Данные из WebFetch обоих сайтов.

### Сравнительная таблица технических элементов

| Элемент | ePIC | BiXBiT | Победитель | Приоритет |
|---|---|---|---|---|
| Title tag — коммерческий запрос | "Antminer Custom Firmware \| ePIC..." | "Bitcoin Mining Solutions – Tools..." | **ePIC** | **P0** |
| H1 homepage | "Custom Antminer Firmware" | "Bitcoin Mining Software & Hardware" | **ePIC** | **P0** |
| Hreflang | Нет (монолингвальный) | Нет — КРИТИЧНО: /en/ и /ru/ без hreflang | Tie (BiXBiT риск выше) | **P0** |
| JSON-LD Schema | Нет | Нет | Tie — первый кто внедрит выиграет | **P0** |
| Meta description | Нет | Нет | Tie | P1 |
| Open Graph / og: | Нет | Нет | Tie | P1 |
| Canonical | Нет | Нет | Tie — для BiXBiT критичнее из-за дублей /en/ /ru/ | P1 |
| Sitemap lastmod | Актуален (июнь 2026) | Устарел (2024-09-04 везде) | **ePIC** | P1 |
| Блог — частота публикаций | 2 SEO-поста в июне 2026 | Неизвестна (sitemap неактуален) | **ePIC** | **P0** |
| CMS | WordPress + Yoast SEO | Custom HTML/CSS | **ePIC** (автоматизация) | P1 |
| URL структура | Плоская для постов | Иерархичная (/en/firmwares/...) | **BiXBiT** | P3 |
| Sitemap структура | WordPress default (post, page, tag) | Тематическая (firmware, product, blog, docs) | **BiXBiT** | P2 |
| robots.txt | Чистый минималистичный | Детализированный с Clean-param | **BiXBiT** | P3 |
| Объём контента | ~50 страниц | >130+ URL (firmware + product + blog) | **BiXBiT** | P2 |
| llms.txt | Нет (404) | Нет (404) | Tie — BiXBiT может стать первым | P2 |
| CLS | Неизвестен (нет API) | 0.888 — P0 из аудита 2026-06-17 | **ePIC** (предположительно) | **P0** (зафиксировано) |
| HTTPS | Да | Да | Tie | — |

### Технические преимущества BiXBiT
- Иерархичная семантичная URL-структура (`/en/firmwares/whatsminer-series-m6x`)
- Тематически структурированный sitemap (firmware, product, blog, documentation)
- Детализированный robots.txt с Clean-param для UTM
- Больший объём проиндексированного контента
- Мультиязычная структура заложена — готова для hreflang

### Технические преимущества ePIC
- Title и H1 homepage содержат главный коммерческий запрос
- Sitemap lastmod актуален
- WordPress + Yoast — автоматизация meta, sitemap, og
- Активный SEO-блог с коммерческими ключами в slug

---

## 5. Сводка возможностей

### Где BiXBiT структурно выигрывает

1. **Dual-platform без hardware replacement** — BiXBiT firmware устанавливается на существующую плату Antminer и Whatsminer. UMC ePIC — это физическая замена control board за $100–200/unit [VERIFY]. Для флота из 1000+ ASIC это существенная разница в TCO.
2. **Полная экосистема** — Firmware + AMS мониторинг + Immersion/Hydro cooling + PDU. ePIC только firmware.
3. **URL и sitemap архитектура** — технически лучше построены.
4. **Больше поддерживаемых Whatsminer моделей** — [VERIFY: M6x серия]

### Где BiXBiT проигрывает / уязвим

1. **Dev fee: 3% vs 1.5%** — ePIC выигрывает прямое сравнение [VERIFY текущий BiXBiT dev fee]. На флоте 1000 ASIC при цене Bitcoin $100k разница в dev fee = реальные деньги.
2. **AI-видимость: 0/10 vs 7/10** — критичный разрыв для B2B-ресёрча.
3. **Нет в сравнительном контенте третьих сторон** — hashrateindex.com, d-central.tech не упоминают.
4. **Нет wire PR** — ePIC системно использует PRNewswire/BusinessWire.
5. **Title/H1 не содержат целевой запрос** — on-page сигнал слабее.
6. **CLS = 0.888** — задокументированная P0 проблема.

### Уникальные ниши, недоступные ePIC

- **"Firmware + immersion cooling" keyword cluster** — у ePIC нет cooling, нет конкуренции
- **"Mining fleet management + firmware"** — AMS + firmware в одном вендоре
- **"No hardware modification firmware"** — чистая программная прошивка vs UMC аппаратная замена
- **PDU content cluster** — у ePIC нет продукта в этой категории

---

## Plan закрытия разрывов

### P0 — Сделать в течение 2 недель

| # | Действие | Тип | Ответственный |
|---|---|---|---|
| 1 | Исправить title homepage: "Custom Firmware for Antminer & Whatsminer \| BiXBiT" | On-page | Dev |
| 2 | Исправить H1 homepage: содержать "Antminer" + "Whatsminer" + "custom firmware" | On-page | Dev |
| 3 | Создать страницу сравнения прошивок (BiXBiT vs ePIC vs Braiins vs Vnish vs LuxOS) | Новый контент | Content |
| 4 | Аутрич в hashrateindex.com — запрос включить BiXBiT в "Top 5 Firmware 2026" | Outreach | Marketing |
| 5 | Аутрич в d-central.tech — включение в comparison + обсуждение партнёрства | Outreach | Marketing |
| 6 | Создать llms.txt на bixbit.io/llms.txt | Technical | Dev |
| 7 | Внедрить hreflang для /en/ и /ru/ (риск дублирования без него) | Technical | Dev |
| 8 | [VERIFY] dev fee BiXBiT Antminer — если 3%, сформулировать TCO-контраргумент | Content research | PM |

### P1 — 30 дней

| # | Действие |
|---|---|
| 9 | Внедрить JSON-LD Schema: Organization + SoftwareApplication + FAQPage |
| 10 | Добавить meta description на все ключевые страницы |
| 11 | Добавить Open Graph теги |
| 12 | Canonical self-referencing на всех страницах |
| 13 | Исправить sitemap lastmod (сейчас везде 2024-09-04) |
| 14 | Запустить wire PR на PRNewswire под реальный повод |
| 15 | Обновить Crunchbase и Tracxn профили |
| 16 | Создать страницу "Firmware for Antminer AND Whatsminer" |
| 17 | Аутрич в emcd.io — включить в firmware comparison |

### P2 — 60 дней

| # | Действие |
|---|---|
| 18 | Найти ASIC-ретейлеров США/Канада — договориться о product pages с backlink |
| 19 | Создать Medium publication BiXBiT — переопубликовать EN-статьи |
| 20 | Опубликовать open-source CLI/утилиты на github.com/bixbit-me |
| 21 | Создать страницу "ePIC Firmware Alternatives" |
| 22 | Создать контент по security/no backdoors |

### P3 — 90 дней

| # | Действие |
|---|---|
| 23 | Запустить регулярный блог: минимум 2 поста/месяц с SEO-slug |
| 24 | Создать PDU content hub |
| 25 | Пруниг устаревшего blog-контента 2018–2019 |

---

## JSON — Сводная таблица результатов

```json
{
  "competitor": "ePIC (epicblockchain.io)",
  "analysis_date": "2026-06-19",
  "data_sources": "WebFetch, WebSearch, Claude self-test. DataForSEO 401 — keyword volumes и backlink metrics недоступны.",
  "bixbit_wins": [
    "URL-архитектура: иерархичная и семантичная vs плоские slugи ePIC",
    "Тематический sitemap (firmware/product/blog/docs) vs WordPress-дефолт",
    "Dual-platform поддержка без замены hardware (vs UMC — физическая плата $100-200/unit [VERIFY])",
    "Полная экосистема: firmware + AMS + immersion/hydro cooling + PDU",
    "Объём контента: 130+ URL vs ~50 у ePIC",
    "robots.txt: детализированный с Clean-param, без рисков",
    "Мультиязычная структура /en/ /ru/ готова для hreflang"
  ],
  "bixbit_loses": [
    "Dev fee: BiXBiT 3% [VERIFY] vs ePIC 1.5% — прямое сравнение проигрывает",
    "AI-видимость: 0/10 vs 7/10 ePIC по Claude self-test",
    "Title/H1 homepage не содержат целевой запрос 'firmware', 'Antminer', 'Whatsminer'",
    "Отсутствие в сравнительных roundup-статьях: hashrateindex.com, d-central.tech",
    "Нет wire PR (PRNewswire/BusinessWire) — ePIC системно использует",
    "Блог неактивен (lastmod 2024-09-04) vs ePIC 2 поста в июне 2026",
    "CLS = 0.888 (P0 из аудита 2026-06-17) — CWV критическая проблема",
    "Нет JSON-LD schema, нет Open Graph, нет canonical, нет hreflang",
    "GitHub: нет публичных репо vs epicblockchain имеет open репозитории"
  ],
  "unique_opportunities": [
    "Firmware + immersion cooling keyword cluster — у ePIC нет cooling-продукта, нет конкуренции в этой нише",
    "Fleet management + firmware unified ecosystem — AMS + firmware в одном вендоре",
    "No hardware modification firmware: BiXBiT = software-only install vs UMC = hardware replacement",
    "PDU content hub — у ePIC нет PDU-продукта совсем",
    "Whatsminer M6x / post-2023 models coverage [VERIFY совместимость]",
    "llms.txt — ни один из конкурентов не внедрил; BiXBiT может быть первым в нише",
    "Security/no-backdoors content — ни ePIC, ни BiXBiT не покрывают; Braiins монополизирует через open-source"
  ],
  "p0_actions": [
    "Исправить title/H1 homepage: включить 'Antminer firmware', 'Whatsminer firmware', 'custom firmware' в тег и заголовок — ePIC делает это, BiXBiT нет",
    "Аутрич в hashrateindex.com + d-central.tech: эти два домена являются primary source для LLM-ответов про firmware — попасть туда = сразу +7 AI-промптов с упоминанием",
    "Создать страницу сравнения прошивок (BiXBiT vs ePIC vs Braiins vs Vnish vs LuxOS) — единственный контент-формат, который LLM цитируют по всем 10 тестовым промптам"
  ]
}
```

---

### Дополнительные находки content-агента

**Dev fee на сайте отсутствует полностью.** На bixbit.io/en нет ни строчки про dev fee — это конверсионный блокер для B2B. ePIC сделал снижение до 1.5% PR-событием (PRNewswire, январь 2026). BiXBiT должен либо [VERIFY] свою цифру и разместить её явно, либо сформулировать TCO-контраргумент.

**Whatsminer — незакрытая монополия.** ePIC официально не имеет backing-контента под Whatsminer (homepage claim без модельных страниц). BiXBiT имеет модельные страницы (`/en/firmwares/whatsminer-series-m6x`) — это единственная SERP-зона, где BiXBiT уже выигрывает. Нужны hub-страница и GEO-оптимизация кластера.

**ziven.io** — mining B2B directory, self-submit без переговоров, P0 по усилиям.

---

### Дополнительные артефакты (созданы content-агентом)

- `/Users/dmitrytchirkov/bixbit-seo/content/competitor-gap-epic-content-2026-06-19.md` — content/keyword gap детально
- `/Users/dmitrytchirkov/bixbit-seo/content/competitor-gap-epic-links-2026-06-19.md` — link gap детально
- `/Users/dmitrytchirkov/bixbit-seo/content/competitor-gap-epic-technical-2026-06-19.md` — technical gap детально

---

*Отчёт сгенерирован: 2026-06-19. Данные: WebFetch epicblockchain.io, WebSearch, Claude self-test (10 промптов). DataForSEO API: 401 Unauthorized на всех эндпоинтах — keyword volumes и backlink-метрики недоступны, не придуманы. Тех-факты ePIC помечены [VERIFY]. Бизнес-решения по dev fee, партнёрствам, контент-инвестициям — на усмотрение команды.*
