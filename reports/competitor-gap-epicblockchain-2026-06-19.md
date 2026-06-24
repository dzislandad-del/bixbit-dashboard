# Competitor Gap Analysis: BiXBiT vs ePIC Blockchain — 2026-06-19

> Источники: WebFetch (epicblockchain.io, bixbit.io/en — live crawl), WebSearch (8 запросов),
> DataForSEO (API 401 — keyword volumes и backlinks недоступны; указано явно где применимо).
> Четыре агента: content-seo, offpage-seo, geo-ai, technical-seo.
> Тех-факты ePIC помечены [VERIFY].

---

## Обзор: кто такой ePIC Blockchain

**Продукт:** UMC OS (Universal Mining Controller OS) — кастомная прошивка для Antminer.
**H1 homepage:** "Custom Antminer Firmware"
**Позиционирование:** Firmware-only вендор (нет cooling, нет мониторинга).
**Dev fee:** 1.5% (снижен с 2.5% январь 2026, анонсирован как "market-leading") [VERIFY]
**Поддерживаемые модели [VERIFY]:** Antminer S19j и новее (S19x–S21x); Whatsminer M3x/M5x/M30/M50 (заявлено на homepage, не подтверждено FAQ)
**Ключевые фичи:** Perpetual Tune (autotuning в 3 режимах: Voltage Optimizer/Board Tune/Chip Tune), RigRunner (fleet deploy tool), ePIC Dashboard, Overdrive mode, AutoFan, Survival mode, API (GitHub)
**Перформанс-заявки [VERIFY]:** 10–25% improvement vs stock firmware; +5–15% hashrate; 200-unit fleet экономия ~$30,000/год при $0.07/kWh
**Блог:** Да — 28 постов, активен до июня 2026. Темы: autotuning explainers, firmware vs stock, install guides, version release notes.
**Сайт:** WordPress + Yoast SEO. ~51 страница, sitemap lastmod 2026-06-15 (свежий).

---

## I. CONTENT / KEYWORD GAP

### DataForSEO статус
API вернул HTTP 401 — все keyword volumes = null, данные не придуманы. Для получения объёмов: исправить DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD в `.env`, проверить наличие подписки на DataForSEO Labs.

### Ключевые запросы без объёмов (подтверждены через WebSearch как активные)

| Keyword | Volume | KD | Примечание |
|---------|--------|----|------------|
| epic firmware | null | null | not_available (401) |
| umc os firmware | null | null | not_available (401) |
| antminer firmware comparison | null | null | not_available (401) |
| whatsminer firmware | null | null | not_available (401) |
| asic firmware dev fee | null | null | not_available (401) |
| lowest dev fee asic firmware | null | null | not_available (401) |
| perpetual tune mining | null | null | not_available (401) |
| antminer autotuning firmware | null | null | not_available (401) |
| asic overclocking firmware | null | null | not_available (401) |
| mining firmware no dev fee | null | null | not_available (401) |
| antminer s19 efficiency firmware | null | null | not_available (401) |
| asic firmware fleet management | null | null | not_available (401) |

### SERP landscape (qualitative, WebSearch)
- "best antminer firmware 2026" — топ занят Braiins OS+, VNish, LuxOS, D-Central editorial. **Ни BiXBiT, ни ePIC в топе не обнаружены.**
- "antminer firmware comparison dev fee" — доминируют D-Central и VNish. ePIC упомянут вскользь, BiXBiT отсутствует.
- "whatsminer firmware" — BiXBiT появляется (модельные страницы). ePIC Whatsminer-контента нет.
- "UMC OS mining firmware" — ePIC владеет брендовым SERP (Yahoo Finance PR, собственный сайт).

### Content Gap Table

| Topic | ePIC has | BiXBiT has | Priority | Rationale |
|-------|----------|-----------|----------|-----------|
| Autotuning explainer (что это, как работает) | ДА — "What Is Perpetual Tune" + алгоритмы (2 поста) | НЕТ | **P0** | ePIC активно строит brand equity на термине. BiXBiT имеет фичу [VERIFY] — нет ни страницы, ни поста |
| Dev fee transparency / сравнение | ДА — отдельный пост о снижении до 1.5%, FAQ-запись | НЕТ — dev fee не упомянут нигде на bixbit.io/en | **P0** | Dev fee — главный B2B-критерий покупки. Отсутствие — конверсионный блокер |
| Custom firmware vs stock firmware | ДА — пост с quantified claims | НЕТ | **P0** | Высокий коммерческий интент, D-Central тоже покрывает. BiXBiT отсутствует |
| Firmware comparison (vs Braiins/VNish/LuxOS) | ЧАСТИЧНО — 1 пост упоминает конкурентов | НЕТ | **P0** | "antminer firmware comparison" — ключевой кластер. Ни одной страницы у BiXBiT |
| Fleet management / bulk deploy | ДА — RigRunner + ePIC Dashboard описаны детально | ЧАСТИЧНО — AMS упомянут на homepage | **P1** | ICP (100–100k+ ASIC) ищет именно это |
| Per-model firmware landing pages | ЧАСТИЧНО — 1 пост S19 XP; нет отдельных страниц | ДА — 12 EN URL по моделям | **P1** | BiXBiT структурно выигрывает — страницы есть, но нужна оптимизация |
| Firmware API / developer docs | ДА — GitHub репо, упоминание на сайте | НЕТ — нет публичного API-контента на bixbit.io/en | **P1** | Institutional buyers нуждаются в API для интеграции |
| Firmware installation guides | ДА — MicroSD recovery, RigRunner guide (2026) | ЧАСТИЧНО — посты 2022–2023 (устаревшие) | **P1** | Устаревший контент теряет релевантность |
| Benchmark data (J/TH по моделям) | ЧАСТИЧНО — страница есть, J/TH цифры не опубликованы | НЕТ | **P1** | E-E-A-T: buyers хотят доказательства, не маркетинг |
| Whatsminer firmware (dedicated) | НЕТ — homepage claim, 0 страниц | ДА — модельные страницы + блог | **P2** | BiXBiT монополист в этой нише vs ePIC |
| Immersion cooling + firmware synergy | НЕТ (нет cooling продуктов) | ЧАСТИЧНО — cooling блог 2018–2021 (устаревший) | **P2** | Уникальный differentiator BiXBiT vs все firmware-конкуренты |
| Firmware security / no-backdoor | НЕТ | НЕТ | **P2** | B2B ICP требует это. Braiins владеет через open-source |
| Overclocking / underclocking guides | НЕТ | ЧАСТИЧНО — пост 2022 (устаревший) | **P2** | Открытая территория — ePIC тоже не покрывает |
| Firmware changelog series | ДА — release posts v1.8–v1.16 | ЧАСТИЧНО — нерегулярно | **P3** | Накапливает long-tail запросы и форумные ссылки |
| Mining profitability с firmware | Implied (калькулятор ROI) | НЕТ | **P3** | Риск compliance; низкий приоритет |

### ePIC Content Weaknesses (возможности BiXBiT)

1. **Нет мета-описаний ни на одной странице** — базовый SEO-провал, легко закрыть.
2. **Whatsminer — нулевой контент.** Только homepage claim. BiXBiT имеет модельные страницы — надо усилить.
3. **Benchmark data vague** — страница есть, J/TH-таблиц нет. First mover с verified tables выигрывает кластер.
4. **Нет immersion/hydro cooling.** У ePIC нет cooling продуктов. Firmware + immersion — незаполненная ниша.
5. **Blog только раскручивается** — 2 поста в июне 2026. BiXBiT может опередить по техническому depth.
6. **API на GitHub, не на сайте** — нет SEO-ценности для epicblockchain.io.
7. **Fleet management** слабо задокументирован в SEO-контенте (только FAQ).

---

## II. LINK GAP

### DataForSEO Backlinks статус
Endpoints (backlinks_summary, referring_domains, domain_intersection) вернули HTTP 401. Backlinks API требует отдельной подписки. Количественные метрики (DR, referring domains, backlinks count) недоступны. Анализ через открытые источники.

### Домены с ePIC, которых нет у BiXBiT

| Domain | Тип | Links ePIC | Links BiXBiT | Приоритет | Действие |
|--------|-----|-----------|-------------|----------|---------|
| hashrateindex.com | Mining research/media | ДА (топ-5 firmware 2026) | НЕТ | **P0** | Редакционный питч Colin Harper / editorial@luxor.tech |
| d-central.tech | Mining B2B media | ДА (mention) | НЕТ | **P0** | Аутрич support@d-central.tech, акцент на Whatsminer |
| ziven.io | Mining B2B directory | ДА | НЕТ | **P0** | Самостоятельный сабмит "Add a Company" — без переговоров |
| coindesk.com | Crypto tier-1 media | ДА (funding + Argo) | НЕТ | **P1** | Newsworthy PR event (партнёрство, продукт-анонс) |
| bitcoinmagazine.com | Bitcoin media | ДА (июль 2024) | НЕТ | **P1** | Угол: независимость от китайских вендоров, западная инфраструктура |
| einpresswire.com | Press wire | ДА | НЕТ | **P1** | Включить в PR-дистрибуцию следующего релиза |
| prnewswire.com | Press wire | ДА (янв 2026) | ЧАСТИЧНО | **P1** | Систематизировать релизы под firmware/cooling |
| altairtech.io | Hardware reseller | ДА (2 product pages) | НЕТ | **P1** | Найти западного реселлера BiXBiT с product page |
| aijourn.com | Tech media | ДА | НЕТ | **P2** | Включить в PR-рассылку |
| github.com/epicblockchain | Developer platform | ДА (rig-runner, etc.) | НЕТ (нет publich repo) | **P2** | Решение о публикации open-source инструментов |
| cbinsights.com | VC intelligence | ДА | НЕТ | **P3** | Создать профиль |
| owler.com | Company intelligence | ДА | НЕТ | **P3** | Создать профиль |

### Структурные наблюдения по ссылкам

1. **Editorial mining media — главный gap.** hashrateindex.com + d-central.tech — два крупнейших B2B-ресурса по firmware. ePIC в обоих, BiXBiT ни в одном.
2. **ePIC использует PR wires системно.** Prnewswire + EIN Presswire = регулярный поток ссылок. BiXBiT нерегулярно.
3. **Reseller как донор.** altairtech.io ссылается с product pages — «partnership link building». BiXBiT нужен аналогичный западный реселлер.
4. **Нет developer footprint.** ePIC имеет GitHub org с публичными tools — developer-ссылки с высоким trust-сигналом.

---

## III. AI CITATION GAP (GEO)

### Инструменты
DataForSEO LLM Mentions API заблокирован (permission denied). Анализ через WebSearch proxy + прямой fetch страниц.

### Матрица AI-Citation Gap

| Промпт (B2B ICP) | ePIC в AI-источниках | BiXBiT | Gap |
|---|---|---|---|
| "best custom firmware antminer S19 S21" | ДА — через d-central.tech, coinwebmining.com | НЕТ | КРИТИЧЕСКИЙ |
| "asic firmware providers comparison" | ДА — d-central "Bitcoin Mining Software Comparison 2026" | НЕТ | КРИТИЧЕСКИЙ |
| "antminer firmware overclocking comparison" | ДА — упоминается в обзорах наряду с Braiins/VNish | НЕТ | КРИТИЧЕСКИЙ |
| "whatsminer custom firmware comparison" | НЕТ (ePIC не поддерживает Whatsminer) | ДА | BiXBiT выигрывает |
| "mining fleet monitoring software" | НЕТ | НЕТ | Оба отсутствуют |

**Счёт:** ePIC цитируется по 3/5 Antminer-запросам. BiXBiT — по 1/5 (только Whatsminer).

### Источники, которые "кормят" LLM-ответы

ePIC получает AI-упоминания через external citation trail, а не за счёт on-page качества:
- **d-central.tech** — главный AI-feeder для firmware-запросов. ePIC включён, BiXBiT нет.
- **github.com/epicblockchain** — 3 публичных репозитория (powerplay-antminer, rig-runner, umcos-antminer). LLM обучаются на GitHub.
- **altairtech.io** — дистрибьютор создаёт независимые упоминания.
- **businesswire.com** — пресс-релизы (Argo partnership) — авторитетный источник для AI.

BiXBiT упоминается преимущественно в: ANN-треде BitcoinTalk, topgold.forum (низкий DR), prweb.com (1 релиз Cormint), YouTube (firmware guide video), saashub.com (узкий comparison).

### AI-Readiness: ePIC vs BiXBiT

| Сигнал | ePIC | BiXBiT |
|--------|------|--------|
| llms.txt | НЕТ (404) | НЕТ (404) |
| FAQ секция | ДА (/support/faq/) | ДА (/en/firmwares#faq) |
| Opening definition "What is X?" | ЧАСТИЧНО | НЕТ — страница не отвечает на базовый промпт |
| Competitor comparison tables | НЕТ | НЕТ |
| Benchmark tables с J/TH | НЕТ | НЕТ |
| Schema markup | НЕТ | НЕТ |
| GitHub / open-source | ДА (3 репо) | НЕ обнаружен |
| Авторитетные comparison mentions | ДА (d-central, altairtech) | НЕТ (только saashub.com) |

**Вывод:** Оба сайта слабо оптимизированы под AI-citability. Преимущество ePIC — внешний citation trail, а не on-page структура.

---

## IV. TECHNICAL SEO GAP

### On-Page сравнение

| Элемент | ePIC | BiXBiT | Gap |
|---------|------|--------|-----|
| Title tag | Описательный, keyword-rich (JS-gated, static не подтверждён) | "BiXBiT Bitcoin Mining Solutions – Tools for Crypto Miners" | Оба OK; ePIC title более точечный под продукт |
| Meta description | Отсутствует | Отсутствует | Оба без — P1 |
| H1 homepage | "Custom Antminer Firmware" | "Bitcoin Mining Software & Hardware" | ePIC H1 точнее под ключ |
| Canonical | Отсутствует | Отсутствует | Оба без — P1 |
| Open Graph | Отсутствует | Отсутствует | Оба без — P2 |
| JSON-LD Schema | НЕТ (подтверждено на всех страницах) | НЕТ (подтверждено на всех страницах) | Первый внедривший — первый в rich results |
| CMS / платформа | WordPress + Yoast SEO | Custom (Tailwind) | Yoast даёт ePIC инфраструктуру meta/OG автоматически |
| Sitemap lastmod | 2026-06-15 (свежий) | 2024-09-04 (9 месяцев устарел) | ePIC выигрывает по crawl frequency сигналу — P0 |
| Robots.txt | Fully open | Частично ограничен + clean-param | BiXBiT сложнее и правильнее; clean-param — плюс |

### Sitemap Structure

| Параметр | ePIC | BiXBiT |
|----------|------|--------|
| Страниц (est.) | ~51 | ~230 EN |
| Blog posts | 27 | ~205 EN |
| Firmware pages | 1 (download page) | 12 model-specific EN URL |
| Product pages | 1 /product/ | 9 /en/products/* |
| EN/RU смешаны | Нет (EN only) | Да — без hreflang |
| Firmware sitemap | Нет | Да (sitemap-firmware.xml) |

### Schema Gap (оба на нуле — first-mover opportunity)

| Schema type | Приоритет | Почему важно |
|-------------|----------|--------------|
| FAQPage | P0 | Обе страницы имеют FAQ HTML — прямой путь к rich results и AI Overviews |
| Organization | P1 | Knowledge panel, sitelinks |
| SoftwareApplication | P1 | Rich results для firmware pages; ePIC тоже не внедрил |
| Product | P1 | Hardware cooling pages |
| BreadcrumbList | P2 | ePIC имеет HTML breadcrumbs; schema нет у обоих |
| Article | P2 | DatePublished/Modified для freshness signaling на 205 EN постах |
| HowTo | P2 | Installation guides |

### Performance
DataForSEO Lighthouse и SERP API недоступны (401). Из baseline 2026-06-17: **BiXBiT CLS = 0.888 (P0)**. ePIC CLS неизвестен.

---

## ПЛАН ЗАКРЫТИЯ РАЗРЫВОВ

### P0 — В течение 1 недели (наивысший impact)

| # | Действие | Зона | Ответственный |
|---|----------|------|--------------|
| P0.1 | FAQPage JSON-LD на /en/firmwares/antminer и /en/firmwares/whatsminer | Technical | Dev |
| P0.2 | Исправить sitemap lastmod — регенерация со свежими датами | Technical | Dev |
| P0.3 | Добавить opening definition на /en/firmwares — первый абзац отвечает "What is BiXBiT firmware?" [VERIFY спеки перед публикацией] | Content | Content lead |
| P0.4 | Зарегистрировать BiXBiT на ziven.io — self-submit без переговоров | Links | Marketing |
| P0.5 | Создать страницу/секцию dev fee — что за модель, какой %, сравнение [VERIFY точный % перед публикацией] | Content | Content lead + Product |

### P1 — В течение 30 дней

| # | Действие | Зона | Ответственный |
|---|----------|------|--------------|
| P1.1 | "Antminer Firmware Comparison" hub-страница — BiXBiT vs Braiins vs VNish vs LuxOS vs ePIC — таблица с dev fee, моделями, autotuning [VERIFY все цифры] | Content | Content lead |
| P1.2 | "What Is Autotuning in BiXBiT Firmware" — explainer-страница [VERIFY: название фичи, алгоритм, время tuning] | Content | Content lead + Product |
| P1.3 | Meta descriptions на всех /en/firmwares/* и /en/products/* (приоритет) | Technical | Dev/Content |
| P1.4 | Canonical tags site-wide (особенно EN/RU — риск дублей) | Technical | Dev |
| P1.5 | Open Graph теги site-wide | Technical | Dev |
| P1.6 | Organization JSON-LD на homepage | Technical | Dev |
| P1.7 | SoftwareApplication JSON-LD на всех 12 firmware pages [VERIFY цены/модели] | Technical | Dev |
| P1.8 | Аутрич к d-central.tech (support@d-central.tech) — включение в firmware comparison. Акцент: Whatsminer + AMS ecosystem | Links/Content | Marketing |
| P1.9 | Редакционный питч к hashrateindex.com — editorial@luxor.tech или Colin Harper LinkedIn | Links | Marketing |
| P1.10 | Создать /llms.txt — первый в нише среди firmware-вендоров | GEO | Dev |
| P1.11 | Аутрич к emcd.io, coinwebmining.com для включения в annual firmware reviews | Links/GEO | Marketing |

### P2 — В течение 60–90 дней

| # | Действие | Зона |
|---|----------|------|
| P2.1 | Hub-страница "Whatsminer Firmware" — BiXBiT монополист, ePIC не конкурирует | Content |
| P2.2 | Benchmark data page — J/TH по моделям до/после (verified first-party test data) [VERIFY все цифры] | Content |
| P2.3 | "BiXBiT Firmware + Immersion Cooling: The Stack No Competitor Offers" — pillar page | Content |
| P2.4 | "Firmware Security for Bitcoin Mining" — trust/E-E-A-T page [VERIFY audit status] | Content |
| P2.5 | BreadcrumbList + Article schema на blog posts | Technical |
| P2.6 | HowTo schema на installation guides | Technical |
| P2.7 | Refresh firmware installation guides (Antminer + Whatsminer 2025–2026) | Content |
| P2.8 | Аутрич к coindesk.com / bitcoinmagazine.com через newsworthy event | Links |
| P2.9 | Публичный GitHub репозиторий (changelog, compatibility list, tools) | GEO/Links |
| P2.10 | Проверить/решить вопрос bixbitusa.io (canonical или DMCA) | Technical |
| P2.11 | Разблокировать DataForSEO LLM Mentions API + Backlinks API для количественного анализа | Data |

### P3 — Backlog

| # | Действие |
|---|----------|
| P3.1 | Team/About pages для E-E-A-T (ePIC имеет /team/ и /about-us/) |
| P3.2 | Product schema на /en/products/* (cooling hardware) |
| P3.3 | Firmware changelog blog series — регулярные release notes |
| P3.4 | Проверить robots.txt: разрешены ли GPTBot, ClaudeBot, PerplexityBot |
| P3.5 | Профили на cbinsights.com, owler.com |
| P3.6 | Einpresswire.com включить в регулярный PR-дистрибуцию |

---

## КЛЮЧЕВЫЕ ДИФФЕРЕНЦИАТОРЫ BiXBiT vs ePIC (для контентной стратегии)

| Параметр | ePIC/UMC OS | BiXBiT | Как использовать |
|----------|-------------|--------|-----------------|
| Whatsminer support | НЕТ | ДА (M2X–M6X) | Атака по кластеру "Whatsminer firmware" — монополия |
| Antminer support | S19J+ / S21 | S19/T19/S21 и старше | Более широкий охват старого парка |
| Dev fee | 1.5% [VERIFY] | [VERIFY] | Сравнение — только с verified данными |
| Hardware controller | ДА (физическая плата UMC) | НЕТ (software only) | Разные сегменты — не конкурировать напрямую |
| Immersion cooling | НЕТ | ДА (linked ecosystem) | Ecosystem angle — уникален |
| Fleet monitoring (AMS) | Отдельный Dashboard | Интегрированный AMS | "All-in-one" для fleet operators |
| Autotuning | Да — Perpetual Tune [VERIFY] | [VERIFY: название, алгоритм] | Нужен контент немедленно |
| Quickstart recovery | НЕ заявлено | 3 мин vs 15–45 мин stock | Enterprise USP — включить в comparison |

---

## ДАННЫЕ ПО ИСТОЧНИКАМ

| Источник | Статус | Причина |
|----------|--------|---------|
| DataForSEO Labs (keyword overview) | 401 | Credentials или подписка |
| DataForSEO Backlinks API | 401 | Отдельная подписка |
| DataForSEO SERP API | 401 | Credentials или подписка |
| DataForSEO Lighthouse | 401 | Credentials или подписка |
| DataForSEO LLM Mentions | Permission denied | Требует явного разрешения |
| WebFetch (epicblockchain.io) | Доступен | Основной источник |
| WebFetch (bixbit.io/en) | Доступен | Основной источник |
| WebSearch | Доступен | SERP landscape + source analysis |
| BiXBiT CLS baseline | 0.888 | Из full-audit 2026-06-17 (P0) |
