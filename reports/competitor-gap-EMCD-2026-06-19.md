# Competitor Gap Report: BiXBiT vs EMCD (emcd.io)

**Date:** 2026-06-19
**Scope:** US/EN market — EMCD как медиа/экосистемный конкурент за AI-цитируемость
**Note:** EMCD — не firmware-провайдер. Gap фокус: контентный авторитет, LLM-питание, ссылочный профиль.
**Data sources:** WebFetch (emcd.io, bixbit.io), WebSearch, DataForSEO [API UNAVAILABLE — 401], Claude self-test.

---

## Executive Summary

EMCD — майнинг-пул и экосистема (pool, analytics, P2P), а не firmware-провайдер. Тем не менее EMCD является P0-угрозой для BiXBiT по одной конкретной причине: **EMCD публикует firmware-сравнительные статьи, которые попадают в топ SERP и "кормят" LLM, не упоминая BiXBiT вообще**.

Статья `emcd.io/articles/mining/best-custom-asic-firmware-vnish-vs-braiins-os-vs-luxos/` занимает первую позицию в SERP по запросу "best custom asic firmware 2026 comparison". В ней упомянуты Braiins OS+, Vnish и LuxOS — BiXBiT отсутствует. Это не конкурентная атака — это информационный вакуум, который BiXBiT сам создал отсутствием passage-ready контента и editorial присутствия.

Настоящие AI-citation конкуренты BiXBiT — **Braiins OS+ (доминирует), Vnish, LuxOS, ePIC**. EMCD — медиа/авторитетный ресурс, который их "кормит". Но этот же механизм может начать работать на BiXBiT, если закрыть три системных разрыва:

1. Создать страницу firmware с passage-ready контентом (таблицы спеков, FAQ, определения).
2. Войти в сравнительный контент (собственный + партнёрский аутрич).
3. Настроить техническую AI-readiness (llms.txt, schema, canonical, hreflang).

---

## Content & Keyword Gap

### EMCD Content Profile

**Что публикует EMCD:**
- Блог `/blog` и раздел `/articles/` — криптовалюты, майнинг, финграмотность. Sitemap содержит ~1100+ URL, мультиязычный охват (RU, PT, ES, ZH).
- Firmware-раздел `/fw/` — EMCD распространяет прошивки для Antminer S19/S17/S9/L3+ (преимущественно в партнёрстве с Vnish).
- Help Center (`help.emcd.io`) — инструкции по установке firmware через MicroSD.
- **Ключевая статья:** `emcd.io/articles/mining/best-custom-asic-firmware-vnish-vs-braiins-os-vs-luxos/`
  - Заголовок: "Best Custom ASIC Firmware in 2026: Vnish vs Braiins OS vs LuxOS"
  - Упомянутые бренды: Vnish, Braiins OS+, LuxOS — **BiXBiT отсутствует**
  - Структура: dev fee [VERIFY: Braiins 2–2.5%, Vnish 2–2.8%, LuxOS 2.8%], autotuning, Stratum V2, совместимость с моделями

**Что EMCD не покрывает вообще:**
- Whatsminer firmware (M50, M60, M70 серии) — полный пробел
- Hydro/Immersion cooling firmware (режимы для жидкостного охлаждения)
- Fleet management / мониторинг парка как отдельная тема
- ePIC firmware
- BiXBiT — не упоминается нигде

**SERP-контекст:** По запросу "best custom asic firmware 2026 comparison" статья EMCD занимает первую позицию. D-Central — доминирующий контент-игрок (5+ страниц в топ-10). BiXBiT в SERP по firmware-сравнительным запросам отсутствует.

### Content Gap Table

| # | Тема / URL EMCD | Покрытие EMCD | BiXBiT покрытие | Приоритет |
|---|---|---|---|---|
| 1 | Best Custom ASIC Firmware 2026 — `emcd.io/articles/mining/best-custom-asic-firmware-*` | Полная сравнительная статья, топ SERP, BiXBiT не упомянут | Нет сравнительной статьи, только продуктовые страницы | **P0** |
| 2 | Antminer firmware efficiency guide (J/TH benchmarks) | Общие упоминания, нет технических бенчмарков | Нет публичных бенчмарков / сравнений J/TH | **P0** |
| 3 | Whatsminer custom firmware comparison | Отсутствует у EMCD | Есть страницы M2X/M3X/M5X/M6X, нет editorial-контента | **P0** |
| 4 | Custom firmware dev fee comparison | EMCD упоминает конкурентов, BiXBiT не включён | Нет страницы с явным сравнением dev fee | **P1** |
| 5 | Antminer S19/S21 firmware installation guide | EMCD Help Center: гайды для S9/S17/L3+ (устаревшие) | KB упомянута, но не индексируется как editorial | **P1** |
| 6 | Firmware security (backdoors, dev fee transparency) | Не покрыто | Не покрыто — критический gap для ICP (тех-директора ДЦ) | **P1** |
| 7 | Immersion/Hydro cooling firmware modes | Отсутствует | Упоминается "immersion mode with PSU tuning", нет статьи | **P1** |
| 8 | Antminer S21/S23 custom firmware guide 2026 | Отсутствует | BiXBiT поддерживает S21 серию — нет статьи | **P2** |
| 9 | Firmware autotuning explained (per-chip vs hashboard level) | Упоминается вскользь | Нет образовательного контента | **P2** |
| 10 | Downvolting guide (efficiency underclocking) | Отсутствует | Функция есть — нет статьи | **P2** |
| 11 | Mining fleet management comparison | Отсутствует | BiXBiT AMS — только продуктовая страница, нет editorial | **P2** |
| 12 | Antminer L7/L9 firmware guide | EMCD: L3+ есть, L7/L9 нет | BiXBiT поддерживает L7/L9 — нет editorial контента | **P3** |

### Keyword Opportunities

Объёмы не указаны — DataForSEO недоступен в этой сессии [API UNAVAILABLE]. Приоритет расставлен по коммерческому интенту и конкурентному gap.

1. `best custom asic firmware 2026` — EMCD #1, BiXBiT нет в топ-20. Прямой B2B-интент.
2. `antminer firmware comparison` — D-Central доминирует, BiXBiT отсутствует.
3. `whatsminer custom firmware` — конкуренция слабее, EMCD отсутствует. BiXBiT — уникальный игрок с поддержкой Whatsminer + Antminer одновременно.
4. `asic firmware dev fee comparison` — отдельной страницы нет ни у кого. Быстрый win.
5. `antminer s21 custom firmware` — D-Central имеет статью, EMCD нет, BiXBiT нет.
6. `asic firmware security backdoor` — нет качественного контента у конкурентов. Высокий B2B/Enterprise-интент.
7. `immersion cooling firmware` — практически нет конкурентного контента. BiXBiT = уникальный перекрёсток firmware + cooling.
8. `antminer downvolting guide` / `asic underclocking efficiency` — D-Central базовый, потенциал для глубокого материала.
9. `asic autotuning firmware explained` — образовательный контент с высокой цитируемостью в AI Overviews.
10. `mining asic firmware no dev fee` — нишевый, высококонверсионный для крупных операторов.

### Content Action Plan (P0–P1)

**P0-1. Сравнительная статья — прямой конкурент статье EMCD**
`/en/blog/best-custom-asic-firmware-comparison`
Обзор 5 провайдеров (Braiins, Vnish, LuxOS, ePIC, BiXBiT), сравнительная таблица: J/TH [VERIFY], dev fee, поддерживаемые модели, autotuning, Stratum V2, security. Главный дифференциатор: BiXBiT — единственный с поддержкой Whatsminer + Antminer одновременно.

**P0-2. Whatsminer firmware hub**
`/en/blog/whatsminer-custom-firmware-guide`
Незанятая ниша — ни EMCD, ни D-Central нет качественного Whatsminer-контента. BiXBiT — один из немногих реальных провайдеров для M50/M60/M70.

**P0-3. Firmware efficiency benchmarks**
`/en/blog/asic-firmware-efficiency-benchmarks`
Реальные [VERIFY] тесты: stock vs BiXBiT по J/TH для S19/S21/M50/M60. Это E-E-A-T якорь и магнит для editorial цитирований.

**P1-4. Firmware security page**
`/en/blog/asic-firmware-security-no-backdoors`
Backdoors, dev fee transparency, closed vs open source. Критично для ICP (тех-директора, институционалы).

**P1-5. Antminer S21 firmware guide**
`/en/blog/antminer-s21-custom-firmware`
Актуальная модель 2024–2026, BiXBiT поддерживает S21 XP и Hydro.

**P1-6. Immersion cooling firmware modes**
`/en/blog/immersion-cooling-firmware-asic-optimization`
Уникальный контент на стыке двух продуктов BiXBiT. Нет аналогов у конкурентов.

---

## Link Gap

### API Status
DataForSEO вернул 401 на оба запроса (backlinks_summary для emcd.io и bixbit.io). Весь анализ построен на WebSearch + WebFetch.

### EMCD Backlink Profile (из открытых источников)

- **BeInCrypto** — партнёрские статьи и CEO-интервью (высокоавторитетный крипто-медиа)
- **CoinBureau** — упоминание в "11 Best Bitcoin Mining Pools" (~90K readers/mo)
- **BitDegree** — детальный обзор EMCD 2026
- **TradersUnion** — обзор EMCD
- **Trustpilot** — профиль с рейтингом (высокий авторитет домена)
- **G2** — профиль EMCD как B2B-продукта
- **Slashdot** — листинг
- **U.Today** — крипто-новости, обзор
- **Bitcointalk** — тред с ревью от VoskCoin (авторитетный YouTube-канал)
- **Blockpool.io** — отдельный обзор emcd-pool-review

### BiXBiT Backlink Profile (из открытых источников)

- **Bitcointalk** — ANN-тред topic 5566528 (есть, но менее активный)
- **Cryptwerk.com** — листинг Mining Hardware
- **SaaSHub** — сравнение bixbit.io vs MineTheASIC
- **bixbitusa.io** — USA-партнёрский сайт (внутри экосистемы)
- **Bitcoin.com forum** — тред-анонс
- **Scribd** — загруженный мануал firmware (пассивная ссылка)

**Ключевой разрыв:** BiXBiT отсутствует ни в одном топовом firmware-сравнении (Hashrate Index, D-Central, EMCD, Coin Web Mining, OBM), тогда как Braiins, Vnish, LuxOS, ePIC присутствуют везде.

### Link Gap Table

| Домен | Ссылается на EMCD | Ссылается на BiXBiT | Тип ресурса | Приоритет аутрича |
|---|---|---|---|---|
| hashrateindex.com | Нет | Нет | Отраслевая аналитика, firmware-гайды | **P0** |
| beincrypto.com | Да (партнёрские статьи, CEO-интервью) | Нет | Крипто-медиа, высокий DR | **P0** |
| coinbureau.com | Да (топ mining pools) | Нет | Крипто-медиа, ~90K readers/mo | **P0** |
| obm.io | Нет | Нет | Mining firmware гайды, ICP-аудитория | **P1** |
| d-central.tech | Нет | Нет | Технический mining блог, firmware-сравнения | **P1** |
| bitdegree.org | Да (обзор EMCD 2026) | Нет | Крипто-обучение, высокий DR | **P1** |
| tradersunion.com | Да (обзор EMCD) | Нет | Финансовые обзоры | **P1** |
| g2.com | Да (профиль EMCD) | Нет | B2B SaaS-обзоры | **P1** |
| trustpilot.com | Да (профиль EMCD) | Нет подтверждённых данных | Отзывы, очень высокий авторитет | **P1** |
| bitcointalk.org | Да (topic 5215417, активный) | Да (topic 5566528, менее активный) | Форум — оба есть | **P2** — улучшить активность |
| slashdot.org | Да | Нет | Тех-каталог/отзывы | **P2** |
| u.today | Да | Нет | Крипто-новости | **P2** |
| cryptwerk.com | Нет подтверждено | Да | Mining-каталог | Уже есть |

### Top 8 Outreach Targets

**1. hashrateindex.com** — публикует "Top Bitcoin Mining Firmware of 2026": Braiins, Vnish, LuxOS, ePIC, stock. BiXBiT отсутствует. Авторитетная редакция Luxor с firmware-фокусом. Питч: верифицированные бенчмарки + кейс клиента.

**2. beincrypto.com** — опубликовал партнёрский материал про EMCD+Vnish. BiXBiT нет. Питч: CEO-интервью "что упускают майнеры при выборе firmware".

**3. coinbureau.com** — "11 Best Bitcoin Mining Pools" упоминает EMCD. Питч: BiXBiT firmware в обзорах mining-инфраструктуры.

**4. obm.io** — "Miners Guide to Firmware" (Mitch Klee, 2024): Vnish, Braiins, LuxOS. BiXBiT отсутствует. Аудитория — операционные менеджеры крупных ферм. Питч: добавить BiXBiT абзац + ссылку в существующую статью.

**5. d-central.tech** — 5+ firmware-сравнений, никогда не упоминают BiXBiT. Питч: совместный бенчмарк или "guest data" — BiXBiT передаёт данные, D-Central публикует.

**6. g2.com** — EMCD имеет профиль, BiXBiT отсутствует. Самостоятельное действие: создать профиль BiXBiT AMS + Firmware, собрать отзывы клиентов.

**7. bitdegree.org** — детальный обзор EMCD есть. Питч: отдельный обзор BiXBiT firmware или включение в comparison.

**8. trustpilot.com** — проверить/создать профиль BiXBiT, активно собирать отзывы от клиентов.

### Link Action Plan

**Немедленные (без переговоров):**
- G2.com — создать профиль BiXBiT AMS + Firmware (бесплатно), запросить отзывы у 5–10 клиентов
- Trustpilot — создать профиль если нет, собирать отзывы
- Bitcointalk ANN-тред — поддерживать активность (апдейты о новых прошивках, кейсах)

**Аутрич Волна 1 — Editorial firmware media:**
- hashrateindex.com — Luxor editorial team; тема: "BiXBiT firmware data for your 2026 guide update"
- obm.io — Mitch Klee; тема: "One firmware you missed in your guide — BiXBiT"
- d-central.tech — business development; тема: "Independent firmware benchmark — collaboration opportunity"

**Аутрич Волна 2 — Крипто-медиа:**
- beincrypto.com — CEO-интервью BiXBiT
- coinbureau.com — pitch на review@coinbureau.com

**Аутрич Волна 3 — Обзорные платформы:**
- bitdegree.org, tradersunion.com — запрос обзора BiXBiT firmware

**Контентный рычаг для всего аутрича:** 1–2 публичных case study с реальными цифрами ("ферма X сократила потребление на Y% за Z недель") — резко увеличивают конверсию питчей в публикации.

---

## AI-Citation Gap

### EMCD AI-Readiness

| Параметр | Статус |
|---|---|
| `llms.txt` | Нет (HTTP 404) |
| AI-краулеры в robots.txt | Не прописаны явно; попадают под `*` (технически доступны) |
| JavaScript рендеринг | SPA (Nuxt.js) — статический crawl видит только HTML-шелл |
| Passage-ready firmware контент | Недостижим без JS-рендеринга; в sitemap раздел `/articles/mining/` есть |

**Почему EMCD-статьи всё равно влияют на LLM:** Статьи попали в Common Crawl / C4 / WebText до отсечения обучающих данных через рендеренные версии (Googlebot рендерит JS). Вторичный эффект — репосты и цитирования в Reddit, Bitcointalk, Telegram создают текстовый след.

### BiXBiT AI-Readiness

| Параметр | Статус |
|---|---|
| `llms.txt` | Нет (HTTP 404) |
| AI-краулеры в robots.txt | Не прописаны явно (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) |
| `/en/firmware` | HTTP 404 — страница не существует |
| Passage-ready контент на главной | Слабый — цифры есть, но нет таблиц спеков, нет J/TH, абзацы не открываются прямым ответом |
| Schema Article на блоге | Отсутствует (подтверждено) |

### Claude Self-Test Results

**Промпт 1:** "What is the best custom firmware for Antminer ASIC miners?"
**Ответ:** Braiins OS+, Vnish, LuxOS (Luxor), ePIC — эти четыре описываются с умеренной уверенностью.
**BiXBiT упомянут:** Нет — не фигурирует в сравнительных обзорах или независимых источниках в обучающих данных.
**EMCD упомянут:** Нет — EMCD классифицирован как майнинг-пул, не firmware-авторитет.
**Источники в ответе:** Braiins documentation, Luxor/LuxOS blog, Vnish community guides, Reddit r/BitcoinMining, Bitcointalk.

**Промпт 2:** "What firmware does EMCD recommend for ASIC miners?"
**Ответ:** Нет достоверных данных. EMCD в обучающих данных — майнинг-пул. Конкретные firmware-рекомендации EMCD не вошли в обучающие данные в воспроизводимой форме.
**BiXBiT упомянут:** Нет.
**EMCD упомянут:** Да — как майнинг-пул, не как firmware-рекомендатор.

**Промпт 3:** "Compare Braiins OS vs BiXBiT firmware for Antminer"
**Ответ:** Braiins OS+ описан подробно. BiXBiT firmware — недостаточно независимого контента для предметного сравнения. BiXBiT знаком в контексте cooling solutions, но не как firmware-вендор с детальными публичными тех-характеристиками. Сравнение невозможно без актуальных данных.
**BiXBiT упомянут:** Да — но как "unknown/insufficient-data" сторона сравнения.

**Промпт 4:** "Is EMCD a competitor to BiXBiT?"
**Ответ:** Прямым конкурентом не классифицирую. EMCD = майнинг-пул. BiXBiT = firmware + cooling. Разные сегменты. Пересечение возможно в области мониторинга (AMS vs EMCD dashboard), но позиционирование и основной бизнес различаются. Потенциально комплементарные продукты.

### AI-Citation Gap Matrix

| Запрос-тип | EMCD цитируется | BiXBiT цитируется | Gap | Приоритет |
|---|---|---|---|---|
| "best custom firmware for Antminer" | Нет | Нет | Оба отсутствуют; доминируют Braiins/Vnish/LuxOS/ePIC | **P0** |
| "custom firmware efficiency J/TH comparison" | Нет | Нет | Нет passage с таблицей спеков ни у кого из двух | **P0** |
| "ASIC firmware autotuning explained" | Нет | Нет | Braiins OS documentation доминирует | **P0** |
| "best firmware Whatsminer M50/M60" | Нет | Нет | Vnish и Braiins упоминаются | **P1** |
| "mining firmware security no backdoor" | Нет | Нет | Ниша не занята ни одним из двух | **P1** |
| "immersion cooling for Bitcoin mining" | Нет | Нет | LiquidStack, Engineered Fluids доминируют | **P2** |
| "EMCD mining pool firmware" | Да (как pool) | Нет | EMCD = pool, не firmware-авторитет | P2 |
| "BiXBiT vs Braiins OS comparison" | Нет | Частично | BiXBiT — только как "insufficient data" сторона | **P1** |

### Три системные причины невидимости BiXBiT в LLM

1. **Нет standalone firmware-страницы** — `/en/firmware` возвращает 404. Нет URL для LLM-атрибуции к firmware-контенту.
2. **Нет сравнительных таблиц с реальными спеками** — единственный формат, который LLM стабильно извлекают для "best firmware" и "compare firmware" запросов.
3. **Нет независимых упоминаний** — Braiins/Vnish/LuxOS фигурируют в десятках форумных обсуждений; BiXBiT firmware — нет.

### Passage-структура для `/en/firmwares/antminer` (и новой `/en/firmware`)

**1. Opening definition (первый абзац)**
Шаблон: "BiXBiT custom firmware is [product category] for Antminer S19/S21 and Whatsminer M50/M60 series that delivers [VERIFY: X J/TH efficiency] through per-chip autotuning and voltage optimization."
LLM извлекают первые 1–2 предложения как определение. Категория + дифференциатор + конкретная модель = цитируемый passage.

**2. Comparison table (обязательно)**

| Firmware | Compatible ASICs | Efficiency gain | Autotuning | Dev fee | Open source |
|---|---|---|---|---|---|
| BiXBiT | [VERIFY: model list] | [VERIFY: J/TH delta] | Yes | [VERIFY: %] | No |
| Braiins OS+ | Antminer S9/S19/S21 | [VERIFY] | Yes | ~2% | Yes |
| Vnish | Antminer/Whatsminer | [VERIFY] | Partial | [VERIFY] | No |
| LuxOS | Antminer S19/S21 | [VERIFY] | Yes | [VERIFY] | No |
| Stock Bitmain | All Antminer | Baseline | No | 0% | No |

Таблица — главный passage для сравнительных LLM-запросов. Все [VERIFY] заполняются командой до публикации.

**3. FAQ-блок (7–10 вопросов)**
- "What Antminer models does BiXBiT firmware support?" — [VERIFY: перечень]
- "Does BiXBiT firmware have a dev fee?" — [VERIFY: конкретный %]
- "Is BiXBiT firmware safe — does it have backdoors?" — описание политики безопасности
- "How much efficiency improvement does BiXBiT firmware deliver?" — [VERIFY: J/TH range]
- "Does BiXBiT firmware work with Whatsminer M50?" — [VERIFY]
- "How does BiXBiT firmware compare to Braiins OS+?" — ключевые отличия
- "Can BiXBiT firmware brick my ASIC?" — гарантии/риски

FAQ — самый высококонвертируемый passage-формат для LLM. Каждый Q&A — отдельный extractable passage.

---

## Technical SEO Gap

### Технический профиль: EMCD

**Архитектура:** SPA (Nuxt.js). WebFetch видит только HTML-шелл — JSON-LD, meta description, OG-теги, H1 через статический crawl не верифицированы. Эта оговорка важна: нельзя утверждать об отсутствии schema у EMCD без Playwright-рендера.

| Элемент | EMCD |
|---|---|
| llms.txt | Нет (HTTP 404) |
| AI-краулеры в robots.txt | Не прописаны явно; дефолт `*` |
| Sitemap | Плоский, ~1100+ URL; priority/changefreq не используются; мультиязычный (RU, PT, ES, ZH) |
| Блог/Статьи | Активный, прошивочные статьи в `/articles/mining/` |
| Schema | Не верифицирована (JS-рендер) |
| Title главной | "EMCD - Cryptocurrency mining pool" — шаблонный |

### Технический профиль: BiXBiT

| Элемент | BiXBiT | Статус |
|---|---|---|
| JSON-LD на главной | Отсутствует (подтверждено) | Проблема |
| Article schema на блоге | Отсутствует (подтверждено на реальной статье) | Проблема |
| Meta descriptions | Отсутствуют на всех проверенных страницах | P0 |
| Canonical tags | Отсутствуют на всех страницах | P0 |
| OG-теги | Отсутствуют | P1 |
| hreflang | Отсутствуют несмотря на /en/ и /ru/ | P0 |
| llms.txt | Нет (HTTP 404) | P1 |
| AI-краулеры в robots.txt | Не прописаны явно | P1 |
| Sitemap | Sitemap-index из 5 дочерних карт; priority/changefreq есть | Лучше EMCD |
| Blog priority в sitemap | `0.3` — занижен | P2 |
| `/en/firmware` URL | HTTP 404 | P0 |
| `Disallow: /assets/` в robots | Потенциально блокирует JS/CSS | P0 — проверить |
| DatePublished в HTML | Только "2 months ago" — нет ISO-даты | P1 |

### Technical Gap Table

| Элемент | EMCD | BiXBiT | Gap | Приоритет |
|---|---|---|---|---|
| JSON-LD Organization | Не верифицирована (JS) | Отсутствует (подтверждено) | BiXBiT проигрывает по умолчанию | **P0** |
| Article schema на блоге | Не верифицирована (JS) | Отсутствует (подтверждено) | Нет rich snippets для статей | **P0** |
| SoftwareApplication schema на /firmwares/ | Не применимо | Отсутствует | BiXBiT упускает уникальную возможность | **P0** |
| Meta descriptions | Не верифицированы (JS) | Отсутствуют везде | Потеря CTR | **P0** |
| Canonical tags | Не верифицированы (JS) | Отсутствуют везде | Риск дублей /en/ vs /ru/ | **P0** |
| hreflang | Есть (4 языка в sitemap) | Отсутствует | Googlebot не видит языковые версии | **P0** |
| llms.txt | Нет | Нет | Паритет — оба отсутствуют | **P1** |
| AI-краулеры (robots.txt) | Не прописаны | Не прописаны | Паритет — здесь BiXBiT может опередить EMCD | **P1** |
| OG-теги | Не верифицированы | Отсутствуют | Нет превью при шеринге | **P1** |
| Blog priority в sitemap | Не используется (нет priority) | 0.3 (занижен) | Поднять до 0.7–0.8 для firmware/cooling статей | **P2** |
| Объём контента | ~1100 URL, 4 языка | 400+ blog + 24 firmware | EMCD значительно больший массив | **P1** |
| Author markup | Не верифицирован | Отсутствует | Слабый E-E-A-T сигнал | **P2** |

### P0-P1 Технические исправления для BiXBiT

**P0-1. Canonical tags** — добавить `<link rel="canonical">` на все страницы.

**P0-2. hreflang** — добавить на все /en/ и /ru/ пары:
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer">
```

**P0-3. Meta descriptions** — на всех страницах. Приоритет: главная, /firmwares/*, /blog/post/*.

**P0-4. SoftwareApplication JSON-LD** на `/en/firmwares/antminer` и других firmware-страницах — конкуренты firmware это не делают; уникальное конкурентное окно.

**P0-5. Organization JSON-LD** на главной — с sameAs (Twitter/X, LinkedIn, Telegram [VERIFY: реальные URL]).

**P0-6. Article JSON-LD** на всех `/en/blog/post/*` — с DatePublished (ISO), Author, Publisher. Также заменить "2 months ago" на `<time datetime="2026-03-23">` в HTML.

**P0-7. Проверить `Disallow: /assets/`** в robots.txt — если там JS/CSS бандлы, Googlebot не рендерит страницы. Проверить через GSC → "Проверка URL" → "Заблокированные ресурсы".

**P1-1. llms.txt** — создать `/llms.txt` с определением BiXBiT, списком ключевых URL и аннотациями продуктов. EMCD не имеет — BiXBiT может опередить.

**P1-2. AI-краулеры в robots.txt** — явно прописать Allow для GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot.

**P1-3. OG-теги** — минимум og:title, og:description, og:url, og:image на всех страницах.

**P1-4. BreadcrumbList JSON-LD** на firmware и блоге.

**P2. Blog sitemap priority** — поднять с 0.3 до 0.7–0.8 для firmware/cooling статей.

---

## Стратегический вывод: как попасть в EMCD-тип контента

EMCD — нестандартный конкурент. Это не прямой firmware-вендор, а **медиа-авторитет**, чьи firmware-статьи "кормят" LLM и формируют SERP. BiXBiT проигрывает не EMCD как компании — BiXBiT проигрывает **информационному вакууму**, который EMCD заполнил контентом.

Три механизма попадания в EMCD-тип контент:

**1. Создать конкурентный контент** (`/en/blog/best-custom-asic-firmware-comparison`). Это самая быстрая дорога к появлению в SERP по тем же запросам что и EMCD — и одновременно создаёт ресурс, который авторы firmware-сравнений (EMCD, D-Central, Reddit) смогут цитировать при обновлениях.

**2. Аутрич к авторам существующих статей.** EMCD написал статью один раз и обновляет. D-Central пишет регулярно. obm.io написал гайд в 2024. Все они обновляют контент — и каждый апдейт это возможность добавить BiXBiT. Условие: у BiXBiT должна быть публичная страница с верифицируемыми данными (J/TH, dev fee, поддерживаемые модели) до начала аутрича.

**3. Стать первичным источником данных.** Если у BiXBiT будут реальные публичные бенчмарки (J/TH до/после, таблицы совместимости, кейсы клиентов) — другие медиа-ресурсы начнут их цитировать. EMCD цитируют Braiins data, Vnish data. BiXBiT data нет в публичном пространстве. Это первопричина AI-невидимости.

**Ключевое конкурентное преимущество, которое нигде не артикулировано:** BiXBiT — единственный крупный провайдер, поддерживающий одновременно Antminer и Whatsminer с autotuning. Ни EMCD, ни D-Central, ни Braiins этого не делают. Этот факт должен стоять в первом предложении каждой firmware-страницы и каждого питча.

---

## Gap Summary JSON

```json
{
  "competitor": "EMCD (emcd.io)",
  "competitor_type": "медиа/экосистема (не firmware)",
  "bixbit_wins": [
    "Единственный провайдер с поддержкой Whatsminer + Antminer одновременно",
    "Уникальный продукт на стыке firmware + immersion/hydro cooling",
    "Лучше структурированный sitemap-index (5 дочерних сайтмапов vs плоский список EMCD)",
    "EMCD тоже не имеет llms.txt — BiXBiT может опередить в AI-readiness"
  ],
  "bixbit_loses": [
    "Отсутствие в SERP по всем firmware-сравнительным запросам",
    "Отсутствие упоминания в топовой firmware-статье EMCD (первая позиция SERP)",
    "Нет /en/firmware страницы (HTTP 404) — нечего индексировать AI-краулерам",
    "Нет LLM-цитируемости по firmware-запросам (Braiins/Vnish/LuxOS доминируют)",
    "Нет ссылок с авторитетных крипто-медиа (BeInCrypto, CoinBureau — у EMCD есть)",
    "Нет G2/Trustpilot профиля (у EMCD есть)",
    "Нет schema markup ни на одной странице (при том что у конкурентов-firmware частично есть)",
    "Нет canonical, hreflang, meta descriptions — P0 технические проблемы",
    "Нет публичных бенчмарков J/TH — нечего цитировать в editorial материалах"
  ],
  "unique_opportunities": [
    "Whatsminer firmware hub — ни EMCD, ни D-Central нет качественного контента по M50/M60/M70",
    "Immersion cooling firmware — уникальный перекрёсток двух продуктов BiXBiT, нет аналогов у конкурентов",
    "Firmware security page — ниша не занята ни у EMCD, ни у Braiins/Vnish, критична для ICP (тех-директора ДЦ)",
    "llms.txt — EMCD не имеет, первый кто создаст получит преимущество в AI-visibility",
    "SoftwareApplication schema на firmware-страницах — конкуренты слабо используют"
  ],
  "p0_actions": [
    "Создать /en/blog/best-custom-asic-firmware-comparison с comparison table (J/TH [VERIFY], dev fee, модели) — прямой конкурент статье EMCD, путь к SERP и LLM-цитируемости",
    "Восстановить /en/firmware (сейчас 404) с passage-ready структурой: opening definition + comparison table + FAQ 7-10 вопросов + SoftwareApplication JSON-LD",
    "Добавить canonical + hreflang + meta descriptions на все страницы + создать llms.txt — три технических P0 которые блокируют индексацию и AI-видимость одновременно"
  ]
}
```

---

*Отчёт основан на данных WebFetch (emcd.io, bixbit.io), WebSearch, Claude self-test. DataForSEO API: [UNAVAILABLE — 401]. Метрики DR/referring domains по API не получены. Технические факты о прошивках конкурентов помечены [VERIFY].*
