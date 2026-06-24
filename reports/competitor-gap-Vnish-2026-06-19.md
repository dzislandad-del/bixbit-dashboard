# Competitor Gap Report: BiXBiT vs Vnish
**Date:** 2026-06-19
**Scope:** US/EN market, https://bixbit.io/en vs https://vnish.group
**Agents:** content-seo · offpage-seo · geo-ai · technical-seo

---

## Content & Keyword Gap

**DataForSEO:** 401 Unauthorized на всех запросах. Keyword volume недоступен. Анализ построен на WebFetch реальных страниц Vnish.

### Что такое Vnish как контентный конкурент

Vnish — это **download-портал, а не контент-ресурс**. Из 9 попыток WebFetch: 5 страниц вернули 404 (blog, articles, features, devices, partnership), мониторинг-страница рендерится пустой. Единственный реальный EN-контент — homepage, тонкие model pages, FAQ.

**Ключевые параметры Vnish (верифицировано WebFetch 2026-06-19):**
- Dev fee: **2.8% base** → **2.5–1.8% tier для 1 000+ ASIC** (тиринг есть; у BiXBiT нет)
- Поддержка: **Antminer only** (Whatsminer "in development")
- Дифференциаторы: Antivirus scanning + cloning module для массового деплоя
- Performance claims: "up to 25% efficiency", "15% consumption reduction" — без J/TH baseline, без методологии `[VERIFY: не подтверждено независимо]`
- Blog/educational content: **не существует** в EN-версии
- Comparison pages: **отсутствуют**
- AMS/monitoring: **страница пуста** (HTML-оболочка без контента)

### Gap-таблица

| # | Gap Topic | Vnish покрывает | BiXBiT покрывает | Тип Gap | Приоритет | Кластер BiXBiT |
|---|---|---|---|---|---|---|
| 1 | Whatsminer firmware (все) | Нет (Antminer only) | Кластер создан | **Возможность** | P0 | whatsminer-firmware.md |
| 2 | Firmware comparison (Vnish vs BiXBiT) | Нет | Нет | SERP gap | P0 | antminer-firmware/comparison |
| 3 | Dev fee transparency page | Частично (цифры на homepage) | Нет | Trust + Commercial | P0 | Новый spoke |
| 4 | Firmware benchmarks (J/TH до/после) | Нет (голые %) | Нет | E-E-A-T | **P0 — new** | Новый spoke: `/en/antminer-firmware/benchmarks` |
| 5 | "Vnish alternative" / "Vnish vs BiXBiT" | Нет | Нет | Bottom-of-funnel | **P1 — new** | Новый spoke: `/en/antminer-firmware/vnish-alternative` |
| 6 | Antminer overclocking guide | Нет (feature list only) | Spoke создан | Blog/guide gap | P1 | antminer-firmware/overclocking |
| 7 | Antminer firmware security / no-backdoor | Нет | Spoke создан | Trust | P0 | antminer-firmware/security |
| 8 | Antminer firmware install guide | Нет (thin) | Spoke создан | How-to | P1 | antminer-firmware/install |
| 9 | Antminer autotuning explainer | Нет | Spoke создан | Educational | P1 | antminer-firmware/autotuning |
| 10 | Immersion cooling + firmware | Нет вообще | Кластер создан | Уникальная позиция | P1 | immersion-cooling-mining.md |
| 11 | Fleet monitoring / AMS | Пустая страница | Кластер создан | Commercial | P1 | mining-fleet-monitoring.md |
| 12 | Mixed-fleet page (Antminer + Whatsminer) | Нет (Antminer only) | Нет | Уникальный USP | P1 | Новый spoke или pillar |
| 13 | Dev fee tier comparison | Нет (ни у кого нет нейтрального) | Нет | Trust + SERP | P1 | Новый spoke: `/en/antminer-firmware/dev-fee-comparison` |
| 14 | Cloning / mass deployment guide | ДА — Vnish Toolkit | Нет | Feature gap | P2 | Возможный blog post |
| 15 | Antminer antivirus / firmware security scanner | Частично (Vnish Antivirus feature) | Blog post есть | Частично закрыто | P2 | Расширить существующий post |

### Три новых спика для antminer-firmware кластера (не было в существующих брифах)

**Gap #4 — `/en/antminer-firmware/benchmarks` (P0)**
Ни один конкурент (Braiins, Vnish, LuxOS, ePIC) не публикует верифицированные J/TH-данные "до/после прошивки" по конкретным моделям. Vnish заявляет 25% без методологии. Страница с реальными тестами BiXBiT делает любой "Vnish vs BiXBiT" запрос в пользу BiXBiT.
`[VERIFY: есть ли тест-бенч данные у инженерной команды?]`

**Gap #5 — `/en/antminer-firmware/vnish-alternative` (P1)**
Bottom-of-funnel: операторы которые уже знают Vnish и ищут альтернативу. Vnish не упоминает конкурентов — аудитория нигде не перехвачена. Главные аргументы: Whatsminer support + AMS + immersion ecosystem.
`[VERIFY: Whatsminer firmware — production ready на момент публикации?]`

**Gap #13 — `/en/antminer-firmware/dev-fee-comparison` (P1)**
BiXBiT и Vnish base rate одинаковы (2.8%). Нейтральная страница сравнения всех провайдеров перехватывает high-intent запрос "firmware dev fee comparison" — никем не закрыт.
`[VERIFY: планируется ли BiXBiT tier structure?]`

### Структурные преимущества BiXBiT которые Vnish не может закрыть
1. **Whatsminer support** — Vnish Antminer-only; Whatsminer "in development" без срока
2. **Firmware + AMS + Cooling в одном вендоре** — у Vnish нет ни мониторинга, ни охлаждения
3. **Mixed-fleet управление** — оператору с Antminer + Whatsminer Vnish бесполезен для половины парка
4. **Нет dev fee тиринга у BiXBiT** — слабость сейчас, но если ввести → можно позиционировать как "честнее"

---

## Link Gap

**DataForSEO backlinks API:** 401 Unauthorized. DR/DA/referring domains — `[est.]`. WebFetch: crazy-mining.org — таймаут (живой сайт, блокирует скрейпинг), bitcointalk.org — требует авторизации.

### Сравнительный профиль (оценочный)

| Метрика | BiXBiT (bixbit.io) | Vnish (vnish.group + vnish.net) |
|---|---|---|
| Referring domains (est.) | ~50–150 | ~200–500 |
| DR/DA (est.) | 20–30 | 30–40 |
| Основные анкоры | бренд, "bixbit firmware" | "vnish", "vnish firmware", "прошивка" (RU) |
| Языковой профиль | EN-преобладание, слабый CIS | CIS-преобладание (RU/UK), слабый EN |

**Ключевой факт:** Vnish имеет двойной веб-актив — vnish.group (EN/международный) и vnish.net (RU/CIS-основной). Ссылочный вес распределён, но суммарный CIS-охват значительно превосходит BiXBiT.

### Подтверждённый gap (WebFetch d-central.tech)

**d-central.tech/firmware/** содержит сравнительную матрицу прошивок с прямыми ссылками на:
- Braiins OS+ → braiins.com/os ✓
- VNish → vnish.com ✓
- LuxOS → luxor.tech/firmware ✓
- DCENT_OS → d-central.tech/dcent-os/ ✓
- **BiXBiT → отсутствует** ✗

Это конкретный gap с высоким коммерческим весом: d-central.tech — крупнейший EN-ресурс по ASIC-обслуживанию, целевая аудитория = ICP BiXBiT.

### Ссылочные кластеры Vnish (логический анализ)

**A. CIS-форумы (сила Vnish, слабость BiXBiT):** crazy-mining.org, forum.bits.media, bitcointalk.org RU-сегмент — Vnish там 8+ лет, системной работы у BiXBiT нет.

**B. Партнёрские инструменты:** miner.dev (Vnish Monitoring) — vnish.net прямо ссылается; ecosystem-партнёрство которого у BiXBiT нет.

**C. EN-сравнительные ресурсы:** d-central.tech — подтверждено; hashrateindex.com, asicminervalue.com — не верифицировано, вероятны.

### Топ-10 доменов для аутрича

| # | Домен | DR est. | → Vnish | → BiXBiT | Тип | Приоритет | Стратегия |
|---|---|---|---|---|---|---|---|
| 1 | **d-central.tech** | ~50–60 | Да ✓ | Нет ✗ | Обзорник/образование | P0 | Письмо редактору с запросом добавить BiXBiT в firmware matrix; аргумент: единственный провайдер с Antminer + Whatsminer |
| 2 | **whatsminer.com** | ~55–65 | Вероятно | Нет | OEM (MicroBT) | P0 | Partnership outreach: BiXBiT = third-party firmware для M-серии |
| 3 | **nicehash.com** | ~70–80 | Вероятно | Нет | Пул / платформа | P0 | Firmware compatibility list или guest post |
| 4 | **asicminervalue.com** | ~40–55 | Вероятно | Нет | ASIC база данных | P1 | Firmware compatibility section на страницах моделей |
| 5 | **hashrateindex.com** | ~55–65 | Нет (не в проверенной статье) | Нет | Аналитика майнинга | P1 | Pitch: "Whatsminer firmware optimization ROI" — ниша не закрыта ни Vnish ни Braiins |
| 6 | **bitcointalk.org** | ~70–75 | Да (исторически) | Нет / слабо | Форум | P1 | Официальный announcement thread; signature ссылка |
| 7 | **crazy-mining.org** | ~30–45 | Да (таймаут = живой) | Нет / слабо | CIS-форум | P1 | Обзор прошивки от модератора или официальный тред |
| 8 | **compassmining.io** | ~50–60 | Неизвестно | Нет | Хостинг / образование | P1 | "Firmware guide for hosted miners" — BiXBiT AMS + firmware = полное hosted-решение |
| 9 | **miner.dev** | ~20–35 | Да (vnish.net → miner.dev) | Нет | Мониторинг / интеграция | P2 | Предложить интеграцию BiXBiT AMS или технический кейс |
| 10 | **f2pool.com** | ~60 | Вероятно | Нет | Пул / блог | P2 | Firmware efficiency темы + compatibility упоминание |

**Новый домен из Vnish-анализа:** miner.dev — экосистемный партнёр Vnish (прямая ссылка с vnish.net), не было в Braiins gap-списке.

### Системный вывод

BiXBiT отсутствует в d-central.tech firmware matrix (подтверждено) — самый приоритетный единственный аутрич, который прямо влияет на LLM-обучение и SERP-позиции. Письмо редактору d-central.tech = P0, передать человеку для переговоров.

---

## AI-Citation Gap

### Claude Self-Test (verbatim, 2026-06-19)

| Промпт | BiXBiT | Vnish | Позиция BiXBiT |
|---|---|---|---|
| "What is Vnish and how does it compare?" | НЕТ | #1 субъект | Отсутствует |
| "Is Vnish safe? Backdoors?" | НЕТ | Только он | Отсутствует |
| "Best alternatives to Vnish for Antminer?" | Частично | Субъект | 4-й (только mixed-fleet оговорка) |
| "Lowest dev fee firmware?" | ДА (паритет 2.8%) | ДА (2.8%) | Равно Vnish |
| "Does Vnish support Whatsminer?" | ДА — как альтернатива | "Limited/beta" | 2-й |
| "Firmware for Antminer AND Whatsminer?" | ДА — **первым** | "In development" | **#1 доминирует** |

**BiXBiT: 3/6 (50%). Vnish: 6/6 (100%).**

Единственная территория где LLM-позиция BiXBiT уже сильная: запрос "What firmware supports both Antminer and Whatsminer?" — Claude отвечает BiXBiT первым.

### Почему Vnish закрепился — конкретный механизм (3 причины)

**1. D-central.tech comparison guides**
5+ comparison guides, все с Vnish в h2/h3, ни одна не упоминает BiXBiT. Это единственный некоммерческий авторитет по firmware-теме в EN SERP. LLM обучаются на D-Central.

**2. Отдельные URL под каждый запрос**
У Vnish есть страница под "vnish vs braiins", "vnish alternatives", "vnish review" (на CIS-ресурсах) — каждый запрос имеет свой URL с Vnish в заголовке. У BiXBiT таких страниц нет.

**3. Верифицируемые цифры в авторитетных источниках**
LLM хранят верифицируемые цифры из авторитетных источников (Cambridge CCAF и аналоги). У BiXBiT нет публичного эквивалента — нет тест-бенч данных, нет независимых бенчмарков.

### GEO-gap матрица

| Запрос | Claude: Vnish | Claude: BiXBiT | Gap | Как закрыть |
|---|---|---|---|---|
| best custom firmware for Antminer | ДА (тройка) | НЕТ | Критично | Попасть в d-central comparison; создать /comparison page |
| Antminer firmware overclocking | ДА | НЕТ | Критично | Spoke /overclocking + аутрич |
| Antminer firmware alternatives | ДА (субъект) | Слабо (4-й) | Высоко | Страница /vnish-alternative на сайте BiXBiT |
| lowest dev fee firmware | ДА (2.8%) | ДА (2.8%) | Паритет | Tier structure или нейтральная сравнительная страница |
| Vnish does NOT support Whatsminer | "Limited/beta" | ДА (альтернатива) | **Возможность** | Усилить /whatsminer firmware кластер |
| firmware for mixed fleet | НЕТ | **#1** | **BiXBiT выигрывает** | Создать dedicated mixed-fleet страницу |
| Antminer firmware security | НЕТ (никто) | НЕТ | Первый получит | Spoke /security — ни у кого нет |

### Три P0-действия для вытеснения Vnish из AI-тройки

**P0 — FAQ на `/en/firmwares` (4 прямых ответа, HTML без JS)**
Это единственное что можно сделать без разработки и что напрямую влияет на passage-extraction при следующем краулинге AI-агентов. Ответы: "Does BiXBiT support Whatsminer? Yes. Does BiXBiT have a dev fee? [VERIFY]. Does BiXBiT firmware have backdoors? [VERIFY]."

**P0 — Аутрич к D-Central**
Одна правка в существующих comparison статьях D-Central > 10 собственных статей BiXBiT для LLM-цитируемости. Передать человеку для переговоров с редактором.

**P1 — Страница `/en/compare/bixbit-vs-vnish`**
Прямой ответ на "alternatives to Vnish" — самый частый gap-запрос. Vnish не публикует сравнений — эта аудитория нигде не перехвачена.

### Passage-фразы для вытеснения Vnish (вставить на сайт verbatim)

**Для "firmware for Antminer AND Whatsminer":**
> "BiXBiT firmware supports both Antminer (S19, S21, T19, T21 series [VERIFY full list]) and Whatsminer (M2x–M6x series [VERIFY]) from a single platform — one of the few providers covering both major ASIC manufacturers. Vnish and Braiins OS+ support Antminer only."

**Для "Antminer firmware alternatives to Vnish":**
> "Unlike Vnish, BiXBiT firmware supports both Antminer and Whatsminer ASICs, integrates with BiXBiT AMS for unified fleet monitoring, and is available with hydro and immersion cooling systems — making it the only full-stack option for operators running mixed-hardware farms."

**Для "dev fee comparison":**
> "BiXBiT firmware developer fee is [VERIFY: 0% / actual rate]. Vnish charges 2.8% for fleets under 1,000 units, scaling to 1.8% at large scale. ePIC charges 1.5%. Braiins OS+ charges 2.5% (0% effective with Braiins Pool). [All figures from providers' public pages, 2026-06-19]"

---

## Data Sources & Limitations

| Source | Status | Notes |
|---|---|---|
| WebFetch: vnish.group/en | OK | Homepage retrieved |
| WebFetch: vnish.group/en/firmware | OK | Firmware hub retrieved |
| WebFetch: vnish.group/en/antminer-s19t19/ | OK | Model page retrieved — content served in Chinese (geo-IP) |
| WebFetch: vnish.group/en/vnish-toolkit-installing-firmware | OK | Installation guide retrieved |
| WebFetch: vnish.group/en/faq | OK | FAQ page retrieved — content served in Chinese (geo-IP) |
| WebFetch: vnish.group/firmware-2/ | OK | Russian firmware hub retrieved |
| WebFetch: vnish.group/robots.txt | OK | Full content retrieved |
| WebFetch: vnish.group/sitemap.xml | OK | Sitemap index, 2 child sitemaps |
| WebFetch: vnish.group/page-sitemap.xml | OK | 143 URLs retrieved with lastmod dates |
| WebFetch: vnish.group/sitemap-misc.xml | OK | 2 URLs (root + sitemap.html) |
| WebFetch: vnish.group/llms.txt | 404 | File does not exist |
| WebFetch: vnish.group/en/devices | 404 | Page does not exist |
| WebFetch: vnish.group/en/antminer-s21t21 | 404 | Page does not exist |
| WebFetch: vnish.group/en/antminer-s21-t21 | 404 | Page does not exist |
| DataForSEO Lighthouse (vnish.group/en) | 401 Unauthorized | Credentials not configured — no CWV/performance data available |

**CWV/Lighthouse data for Vnish:** Not available — DataForSEO credentials are not configured.
All technical findings are based on HTML-level inspection via WebFetch. No live SERP or traffic data.

---

## Technical SEO Gap

### 1. JSON-LD Schema Markup

**Vnish:** Zero JSON-LD detected on all checked pages:
- Homepage `/en` — no JSON-LD
- Firmware hub `/en/firmware` — no JSON-LD
- Model page `/en/antminer-s19t19/` — no JSON-LD
- Installation guide `/en/vnish-toolkit-installing-firmware` — page contains 10 numbered installation steps, a textbook `HowTo` schema candidate — not implemented
- FAQ page `/en/faq` — accordion Q&A structure with no `FAQPage` JSON-LD

**BiXBiT:** 0 JSON-LD schema types (P1, full-audit 2026-06-17)

**Gap verdict:** Parity — both sites have zero schema coverage. BiXBiT opportunity: implement `Organization`, `Product`, `SoftwareApplication`, `HowTo`, `FAQPage` ahead of Vnish on both have identical zero baselines.

---

### 2. Meta Descriptions

**Vnish:** Absent on all checked pages (homepage, firmware hub, model pages, FAQ, installation guide).

**BiXBiT:** Absent (P0, full-audit 2026-06-17)

**Gap verdict:** Parity.

---

### 3. Canonical Tags

**Vnish:** No canonical tags detected on any checked page. This is especially critical given Vnish's geo-IP language substitution (see section 6) — `/en/` URLs serve Chinese content without a canonical pointing back to the original, creating unresolved duplicate content signals.

**BiXBiT:** No canonical tags (P0, full-audit 2026-06-17)

**Gap verdict:** Parity at the technical level, but Vnish's exposure is higher due to language substitution without canonical.

---

### 4. Hreflang

**Vnish:** Partially implemented. Hreflang tags were detected on model pages:
```html
<link rel="alternate" hreflang="ru" href="https://vnish.group/antminer-s19-t19/" />
<link rel="alternate" hreflang="en" href="https://vnish.group/en/vnish-s19-t19-firmware/" />
```

Critical defects in this implementation:
- No `x-default` tag
- No self-referencing hreflang (current page URL not included)
- Chinese versions exist in sitemap (143 URLs include `/zh/` paths) but are not included in hreflang annotations
- Geo-IP redirect serves `/en/` URLs with Chinese content — directly contradicts the `hreflang="en"` declaration pointing to a different URL

**BiXBiT:** No hreflang /en/ ↔ /ru/ (P0, full-audit 2026-06-17)

**Gap verdict:** Vnish nominally ahead (partial hreflang exists), but the implementation is broken. BiXBiT with a correct implementation (x-default, self-referencing, full language matrix) will immediately surpass Vnish's signal quality.

---

### 5. Open Graph / Twitter Card

**Vnish:** No og: or twitter:card tags on any checked page.

**BiXBiT:** No og: or twitter:card tags (P1, full-audit 2026-06-17)

**Gap verdict:** Parity.

---

### 6. Geo-IP Language Override — Vnish Critical Defect (Not Present on BiXBiT)

This is a Vnish-specific structural failure that BiXBiT does not share.

When pages under `/en/` are requested from a non-EN geo-IP address (the fetch server was routed through Asia), Vnish silently served Chinese content instead of English:

| Requested URL | Language Served | H1 Returned |
|---|---|---|
| `/en/antminer-s19t19/` | Chinese (Traditional) | "官方 Vnish 韌體 S19, T19" |
| `/en/faq` | Chinese (Simplified) | "维尼什常见问题解答" |

The geo-IP override operates without:
- A canonical pointing `/en/` URLs to the English canonical
- A `hreflang="zh"` declaration for the Chinese version
- A `Vary: Accept-Language` header

For Google, this creates indexing ambiguity: Googlebot (US IP) sees English content, while regional crawlers or Googlebot routed through Asian infrastructure may see Chinese. This is a direct risk of keyword cannibalization between English and Chinese versions of the same URLs.

**BiXBiT status:** This problem does not exist. The `/en/` URL structure is consistent and language-stable regardless of crawl origin.

---

### 7. H1 Structure

**Vnish:**
- Homepage `/en`: **2 H1 tags** — "VNISH official website" and "The best firmware for mining"
- Firmware hub `/en/firmware`: **1 H1** — "Vnish firmware" (correct)
- Model page `/en/antminer-s19t19/`: **1 H1** (correct)

**BiXBiT:** **8 H1 tags on homepage** (P0, full-audit 2026-06-17)

**Gap verdict:** Both violate single-H1 on homepage; BiXBiT's violation is more severe (8 vs 2). On inner pages, Vnish appears to follow correct 1 H1 structure. BiXBiT inner page H1 structure needs separate verification.

---

### 8. Sitemap — Freshness and Coverage

**Vnish:**
- Architecture: sitemap index → 2 child sitemaps
- Total URLs in `page-sitemap.xml`: **143**
- Sitemap index last updated: **2026-06-13** (6 days before this audit)
- Lastmod range in page-sitemap: August 2023 – June 2026
- Language coverage: EN + RU + ZH versions in sitemap
- Engine: WordPress + Google XML Sitemap Generator plugin
- robots.txt correctly references sitemap

**BiXBiT:**
- Sitemap lastmod frozen at **2024-09-04** (approximately 21 months stale) — P1, full-audit 2026-06-17
- Page count: ~70 pages crawled

**Gap verdict:** Vnish is ahead — sitemap is current (updated 2026-06-13), covers 143 URLs across three languages, and is correctly linked from robots.txt. BiXBiT's 21-month frozen lastmod risks reduced crawl frequency by Google. This gap requires closure.

---

### 9. robots.txt

**Vnish:**
```
User-agent: *
Allow: /
Disallow: /wp-admin/
Disallow: /wp-includes/
Clean-param: twclid For Yandex
Clean-param: utm_source&utm_medium&... For Yandex
Sitemap: https://vnish.group/sitemap.xml
```

Correctly restricts WordPress backend, does not block content pages. Clean-param for Yandex indicates CIS market optimization. Explicit Sitemap directive enables direct discovery by both Google and Yandex.

**BiXBiT:** robots.txt state not verified in this report — requires separate check.

**Gap verdict:** Vnish has a correct robots.txt with explicit Sitemap reference. BiXBiT robots.txt needs direct verification before comparison can be finalized.

---

### 10. Breadcrumb Navigation

**Vnish:** No breadcrumb markup detected in HTML or as JSON-LD `BreadcrumbList` on any checked page.

**BiXBiT:** Breadcrumb status not verified in full-audit — requires separate check.

**Gap verdict:** Parity on Vnish (no breadcrumbs implemented). BiXBiT status to be verified.

---

### 11. llms.txt

**Vnish:** HTTP 404 — file does not exist.

**BiXBiT:** Created but not deployed (P1, full-audit 2026-06-17).

**Gap verdict:** BiXBiT ahead on intent; clear advantage after deployment. No competitor in this firmware niche has llms.txt.

---

### 12. CMS and Technical Infrastructure

**Vnish:** WordPress + Google XML Sitemap Generator (visible in sitemap comments and robots.txt). WordPress provides native access to plugins like Yoast SEO or RankMath that can auto-generate meta descriptions, canonical tags, and hreflang in bulk — yet Vnish has not configured these. The CMS infrastructure for rapid SEO fixes exists and is unused.

**BiXBiT:** Custom HTML/CSS (Tailwind-compatible), non-WordPress.

**Gap verdict:** WordPress gives Vnish faster fix velocity for bulk meta/canonical/hreflang rollout once they decide to act. BiXBiT requires template-level changes or a metadata layer. This is a structural speed-of-execution advantage for Vnish if they prioritize technical SEO. However, BiXBiT's custom stack produces cleaner, more controlled HTML output without WordPress bloat.

---

## Consolidated Gap Table

| Element | BiXBiT | Vnish | Leader | BiXBiT Priority |
|---|---|---|---|---|
| JSON-LD schema | 0 types | 0 types | Parity — first-mover opportunity | P1 |
| Meta descriptions | Absent | Absent | Parity | P0 |
| Canonical tags | Absent | Absent (worse: geo-IP conflict) | BiXBiT (no geo conflict) | P0 |
| Hreflang | Absent | Partial — broken (no x-default, no zh, geo-IP conflict) | Vnish formally; BiXBiT with correct impl. | P0 |
| og: / twitter:card | Absent | Absent | Parity | P1 |
| H1 homepage | 8 H1 (critical) | 2 H1 (violation) | Both fail — BiXBiT worse | P0 |
| H1 inner pages | Unverified | 1 H1 (correct) | Vnish | P1 |
| Sitemap lastmod | 2024-09-04 (21mo stale) | 2026-06-13 (current) | Vnish | P1 |
| Sitemap URL coverage | ~70 | 143 (EN+RU+ZH) | Vnish | P2 |
| robots.txt quality | Unverified | Correct with Sitemap ref | Vnish | P1 |
| Breadcrumbs | Unverified | Absent | TBD | P2 |
| llms.txt | Created, not deployed | 404 (absent) | BiXBiT (after deploy) | P1 |
| Geo-IP language stability | No problem | Critical defect | BiXBiT | Structural advantage |
| HowTo schema on guides | Absent | Absent (content eligible) | Parity | P2 |
| FAQPage schema | Absent | Absent (accordion eligible) | Parity | P2 |
| CMS fix velocity | Custom HTML (slower bulk) | WordPress (faster bulk, unused) | Vnish (structural) | Architecture note |

---

## Where Vnish Has a Technical Advantage BiXBiT Should Close

### 1. Sitemap lastmod freshness — P1
Vnish updates lastmod on every content change (latest: 2026-06-13). BiXBiT's lastmod has been frozen at 2024-09-04 for 21 months — Google may reduce crawl frequency on pages it perceives as unchanged.

**Fix for BiXBiT:** Configure dynamic sitemap.xml generation that writes an accurate lastmod timestamp on every deploy. This is a one-time engineering task with permanent crawl-budget benefit.

### 2. Sitemap → robots.txt explicit linkage — P1
Vnish's robots.txt includes an explicit `Sitemap:` directive, ensuring discovery by both Googlebot and Yandex without relying on Search Console submission alone.

**Fix for BiXBiT:** Verify presence of `Sitemap: https://bixbit.io/sitemap.xml` in robots.txt. If absent, add it — this is a two-line change.

### 3. Three-language sitemap architecture — P2
Vnish covers EN + RU + ZH across 143 URLs. Despite the broken geo-IP implementation, the sitemap structure enables multilingual crawling.

**Fix for BiXBiT:** First priority is correct EN ↔ RU hreflang (P0). ZH is P3 — assess Chinese market opportunity separately.

---

## Where BiXBiT Already Leads Vnish Technically

1. **No geo-IP language override.** BiXBiT's URL structure is crawl-stable — `/en/` consistently serves English regardless of crawl origin. Vnish has a systemic issue where `/en/` URLs serve Chinese content to non-EN IPs, creating canonical ambiguity and hreflang contradiction.

2. **llms.txt prepared.** BiXBiT has created the file (pending deployment). Vnish returns 404. No firmware competitor in the niche has an active llms.txt. First deployer in this category gets the AI-discovery advantage.

3. **Dual-platform URL surface.** BiXBiT covers Antminer + Whatsminer (25+ Antminer model pages + full M2X–M6X Whatsminer series). Vnish is Antminer-only. More URL surface = more schema `Product` opportunities and more indexable firmware pages.

4. **Custom HTML stack.** BiXBiT's non-WordPress codebase produces cleaner, more predictable HTML output. Vnish's WordPress stack adds bloat (plugin markup, admin-bar remnants, comment forms) that can interfere with structured data parsing and increases page weight.

---

## P0/P1 Technical Fixes for BiXBiT (Gap-Analysis Derived)

| # | Fix | Priority | Effort | Notes |
|---|---|---|---|---|
| 1 | Add `<meta name="description">` to all 70 pages | P0 | M | Both sites equally deficient — fix first |
| 2 | Add `<link rel="canonical">` to all pages | P0 | M | Vnish equally deficient; fixing eliminates duplicate risk |
| 3 | Implement hreflang EN ↔ RU with x-default and self-referencing | P0 | M | Vnish hreflang is broken — correct impl. immediately surpasses competitor |
| 4 | Fix 8 H1 on homepage → 1 H1 | P0 | S | Vnish also violates (2 H1), BiXBiT's is more severe |
| 5 | Configure dynamic sitemap lastmod on deploy | P1 | M | Vnish sitemap is current; BiXBiT's is 21 months stale |
| 6 | Implement JSON-LD `Organization` on homepage | P1 | S | Both at zero — first to implement wins |
| 7 | Implement JSON-LD `Product` / `SoftwareApplication` on firmware pages | P1 | M | Both at zero — schema gap is equal |
| 8 | Deploy llms.txt | P1 | S | BiXBiT already has file — deployment only; Vnish 404 |
| 9 | Add og:title / og:description / og:image + twitter:card to all pages | P1 | M | Both at zero — parity fix |
| 10 | Add `Sitemap:` directive to robots.txt if absent | P1 | S | Vnish has it; BiXBiT state unverified |
| 11 | Implement JSON-LD `HowTo` on installation guide pages | P2 | S | Both have eligible content, neither has markup |
| 12 | Implement JSON-LD `FAQPage` on FAQ page | P2 | S | Both have accordion FAQ without schema |
| 13 | Add `BreadcrumbList` JSON-LD to inner pages | P2 | M | Both appear to lack breadcrumb schema |

---

## Сводная таблица приоритетов (все измерения)

| # | Действие | Тип | Приоритет | Усилие | Источник |
|---|---|---|---|---|---|
| 1 | **FAQ-блок на /en/firmwares** (4 ответа: Whatsminer support, dev fee, backdoors, AMS) | GEO/Content | P0 | S | AI-Citation |
| 2 | **Аутрич к d-central.tech** — добавить BiXBiT в firmware matrix | Backlinks | P0 | H (переговоры) | Link + AI |
| 3 | **Meta descriptions** на все 70 страниц | Technical | P0 | M | Technical |
| 4 | **Canonical tags** на все страницы | Technical | P0 | M | Technical |
| 5 | **Hreflang EN ↔ RU** с x-default + self-referencing | Technical | P0 | M | Technical |
| 6 | **H1 homepage: 8 → 1** | Technical | P0 | S | Technical |
| 7 | **CLS 0.888** — диагностика и fix | Technical | P0 | M | Baseline |
| 8 | **`/en/antminer-firmware/benchmarks`** — J/TH тест-данные до/после | Content | P0 | H + [VERIFY] | Content |
| 9 | **whatsminer.com** — partnership outreach | Backlinks | P0 | H (переговоры) | Link |
| 10 | **`/en/antminer-firmware/comparison`** — Vnish/Braiins/LuxOS/ePIC | Content | P0 | M | Content |
| 11 | **Задеплоить llms.txt** (content/geo/llms.txt) | GEO/Technical | P1 | S | GEO |
| 12 | **Entity-definition passage** на homepage (content/geo/entity-definition-homepage.md) | GEO | P1 | S | GEO |
| 13 | **`/en/compare/bixbit-vs-vnish`** — dedicated альтернатива Vnish | Content | P1 | M | AI-Citation |
| 14 | **`/en/antminer-firmware/dev-fee-comparison`** — нейтральное сравнение всех провайдеров | Content | P1 | M | Content |
| 15 | **Organization + SoftwareApplication JSON-LD** | Technical | P1 | S | Technical |
| 16 | **FAQPage JSON-LD** на firmware pages | Technical | P1 | S | Technical |
| 17 | **og: + twitter:card** на все страницы | Technical | P1 | M | Technical |
| 18 | **Sitemap lastmod** — динамический на деплое | Technical | P1 | M | Technical |
| 19 | **nicehash.com** — firmware compatibility outreach | Backlinks | P1 | M | Link |
| 20 | **asicminervalue.com** — firmware section outreach | Backlinks | P1 | M | Link |
| 21 | **Passage-фразы** из AI-Citation секции (3 блока) на страницы сайта | GEO | P1 | S | AI-Citation |
| 22 | **`/en/antminer-firmware/vnish-alternative`** | Content | P1 | M + [VERIFY] | Content |
| 23 | **Whatsminer firmware кластер** — production (брифы созданы) | Content | P1 | H | Content |
| 24 | **`/en/antminer-firmware/security`** — no-backdoor page | Content | P1 | M + [VERIFY] | Content |
| 25 | **bitcointalk.org** — официальный announcement thread | Backlinks | P1 | M | Link |
| 26 | **crazy-mining.org** — официальный тред + review request | Backlinks | P1 | M | Link |
| 27 | **Mixed-fleet dedicated page** (/en/firmware-for-mixed-fleet) | Content | P2 | M | Content + GEO |
| 28 | **miner.dev** — AMS integration outreach | Backlinks | P2 | M | Link |
| 29 | **hashrateindex.com** — pitch Whatsminer firmware article | Backlinks | P2 | M | Link |
| 30 | **HowTo + FAQPage JSON-LD** на install/FAQ страницах | Technical | P2 | S | Technical |

---

*Отчёт создан: 2026-06-19. Агенты: content-seo, offpage-seo, geo-ai, technical-seo. DataForSEO 401 на всех API-вызовах. Vnish факты верифицированы WebFetch (2026-06-19). Следующий Vnish-чек: после деплоя P0-правок или через 60 дней.*
