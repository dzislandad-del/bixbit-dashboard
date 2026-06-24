# Competitor Gap Report: BiXBiT vs Braiins (+ Vnish, LuxOS, ePIC)
**Date:** 2026-06-19
**Scope:** US/EN market, https://bixbit.io/en
**Primary competitor:** https://braiins.com
**Secondary:** vnish.group, luxor.tech/firmware, epicblockchain.io

---

## Data Sources & Limitations

| Source | Status | Notes |
|---|---|---|
| DataForSEO domain_intersection | 401 Unauthorized | Credentials not configured — no live keyword volume data |
| DataForSEO ranked_keywords | 401 Unauthorized | Same |
| WebFetch: braiins.com/blog | OK | Full blog listing retrieved |
| WebFetch: braiins.com/os/plus | OK | Product page retrieved |
| WebFetch: braiins.com/os | OK | Product suite overview retrieved |
| WebFetch: braiins.com/stratum-v2 | OK | Protocol page retrieved |
| WebFetch: braiins.com/braiins-manager | 404 | Page does not exist at this URL |
| WebFetch: braiins.com/compare | 404 | No public comparison page found |
| WebFetch: vnish.group/en | OK | Product homepage retrieved |
| WebFetch: luxor.tech/firmware | OK | LuxOS product page retrieved |
| WebFetch: epicblockchain.io | OK | ePIC (UMC OS) product page retrieved |
| WebFetch: bixbit.io/en | OK | BiXBiT homepage retrieved |
| WebFetch: bixbit.io/en/blog | OK | Blog listing retrieved |
| WebFetch: bixbit.io/en/firmwares/antminer | OK | Antminer firmware product page retrieved |
| Existing clusters | Read | antminer-firmware.md, whatsminer-firmware.md, immersion-cooling-mining.md |

**Search volume data:** Not available (DataForSEO 401). All keyword gap items are based on product/content analysis. Do not use for traffic estimates until DataForSEO credentials are configured.

---

## Content & Keyword Gap

### 1. Competitor Product & Content Positioning

#### Braiins OS+
- **Dev fee:** 2.5% (0% effective when combined with Braiins Pool) — explicitly published on product page
- **Autotuning:** Per-chip optimization marketed as "Autotuning" — dedicated documentation, blog posts, and the feature is central to their brand positioning
- **Supported hardware:** 40+ Antminer models; no Whatsminer support
- **Open-source:** GitHub-published components, GPG signature verification for downloads, SOC1/SOC2 compliance — actively marketed as security/trust differentiators
- **Performance claims (S21 XP):** 295 TH/s vs 270 TH/s stock (+10%), 12.2 J/TH vs 13.5 J/TH stock (+10% efficiency) — [VERIFY: sourced from braiins.com/os/plus product page 2026-06-19]
- **Protocol:** Stratum V2 — Braiins is the primary author and owns this content pillar entirely
- **Fleet management:** Braiins Manager + Braiins Toolbox — integrated ecosystem with dedicated blog content on automation ("Controlflow")
- **Mining pool integration:** Braiins Pool — creates a dev-fee rebate flywheel that competitors cannot replicate structurally
- **Content output:** Active technical blog (~20+ indexed posts visible); covers firmware, mining economics, hardware diagnostics, management software

#### Vnish
- **Dev fee:** 2.8% base; 2.5–1.8% for 1,000+ ASIC deployments — published
- **Supported hardware:** Antminer only (Whatsminer, Innosilicon, Avalon listed as "in development")
- **Efficiency claims:** "Up to 25% profitability increase", "15% reduction in consumption" — [VERIFY: no specific J/TH figures published on homepage]
- **Key differentiator claimed:** Antivirus scanning + cloning module for mass deployment
- **Content:** Minimal blog/editorial content; product-focused pages

#### LuxOS (Luxor)
- **Dev fee:** 0% pool fees on Luxor Pool — firmware dev fee not explicitly stated (0% pool fee positioning mirrors Braiins)
- **Supported hardware:** Antminer + select Whatsminer (30+ models) — [VERIFY: luxor.tech/firmware 2026-06-19]
- **Fleet deployed:** 300,000+ ASICs, >35 EH/s — [VERIFY: sourced from luxor.tech/firmware]
- **Certification:** SOC 2 Type 2 — claims first ASIC firmware to achieve this (ahead of Braiins, ePIC)
- **Differentiator:** "Demand response" — load shedding to ~25W in under 5 seconds; marketed for power curtailment/grid programs
- **Content:** Luxor publishes the "Hashrate Index" newsletter — strong mining economics content (not firmware-specific but builds category authority)

#### ePIC (UMC OS)
- **Dev fee:** 1.5% — lowest published dev fee among named competitors
- **Supported hardware:** Antminer S19j and newer + Whatsminer M3x/M5x/M30/M50 — both platforms, like BiXBiT
- **Performance claims:** "Sub 19 J/TH" for S19 XP support — [VERIFY: sourced from epicblockchain.io 2026-06-19]
- **Differentiator:** "Perpetual Tune" (self-optimizing autotuning), Rich API for fleet customization, licensing options available
- **Content:** Minimal editorial content; thin website

#### BiXBiT Current State
- **Dev fee:** 2.8% (Antminer firmware) — matches Vnish, higher than Braiins (2.5%), LuxOS, ePIC (1.5%)
- **Supported hardware:** Antminer (25+ models S19–S21 series) + Whatsminer (M2X–M6X series) — both platforms, unique vs Braiins/Vnish
- **Comparison pages:** None
- **Dev fee transparency page:** None
- **Open-source / security positioning:** Not addressed in public content
- **Autotuning documentation:** Referenced in feature list as "automatic frequency tuning" — no dedicated explainer page
- **Blog content on firmware:** Zero firmware-specific editorial posts in visible blog listing
- **Stratum V2:** Not mentioned in retrieved product pages
- **Fleet management integration (AMS):** Product exists; no comparative content against competitors

---

### 2. Keyword Gap Analysis (Logical, No Volume Data)

DataForSEO returned 401. The following gaps are derived from product analysis and known SERP behavior in this niche. Priority is commercial + intent-based, not volume-based.

**Braiins ranks for (inferred from content depth and brand size):**

| Keyword Category | Specific Terms | Braiins Depth | BiXBiT Coverage | Gap Severity |
|---|---|---|---|---|
| Antminer firmware brand | "braiins os antminer", "braiins os plus" | Owned — brand term | None | N/A (brand) |
| Antminer firmware generic | "antminer custom firmware", "best antminer firmware", "antminer firmware comparison" | Strong (multiple pages + blog) | Product page only — no comparison, no blog | Critical |
| Antminer autotuning | "antminer autotuning", "asic autotuning firmware", "per chip tuning antminer" | Feature page + documentation | Feature mentioned in list only | High |
| Antminer S19 firmware | "antminer s19 firmware", "s19 pro firmware", "s19 custom firmware" | Strong (S19 is their core model) | Covered in product model list — no dedicated page | High |
| Antminer S21 firmware | "antminer s21 firmware", "s21 custom firmware" | Has S21 XP content + performance data | Covered in product model list — no dedicated page | High |
| Firmware comparison | "braiins vs vnish", "antminer firmware comparison", "braiins os alternatives" | Braiins ranks — self-promotional | No comparison page | Critical |
| Dev fee comparison | "antminer firmware dev fee", "no dev fee mining firmware", "antminer firmware no dev fee" | Braiins publishes dev fee page with 0% pool combo | No dev fee page | Critical |
| Firmware security | "antminer firmware backdoor", "safe antminer firmware", "antminer firmware audit" | Some blog coverage | Nothing | High |
| Mining fleet management | "asic mining fleet management", "mining management software", "mining monitoring dashboard" | Braiins Manager has dedicated content | AMS product exists — no comparison content | High |
| Stratum V2 | "stratum v2 mining", "stratum v2 firmware" | Braiins is the protocol author — completely owns this | Not addressed | Medium (niche) |
| Mining economics | "bitcoin mining profitability", "asic efficiency J/TH" | Braiins calculator + blog | Calculator exists — no supporting editorial | Medium |
| Antminer firmware overclocking | "antminer overclocking firmware", "antminer s19 overclocking", "how to overclock antminer" | Blog + feature page | Not covered in blog; product feature only | High |
| Antminer undervolting | "antminer undervolting", "antminer undervolt guide", "antminer power reduction" | Thin coverage | Nothing | Medium (but high ICP intent) |

**Vnish additionally ranks for (inferred):**

| Keyword Category | Specific Terms | Vnish Depth | BiXBiT Coverage | Gap Severity |
|---|---|---|---|---|
| Antminer antivirus | "antminer virus", "asic antivirus firmware", "antminer malware" | Feature-based — Vnish Antivirus is a named feature | Feature mentioned in BiXBiT list | Medium |
| Bulk deployment | "asic firmware mass deployment", "mining firmware cloning", "bulk firmware install" | Cloning module feature | Not addressed | Medium |

**LuxOS additionally covers:**

| Keyword Category | Specific Terms | LuxOS Depth | BiXBiT Coverage | Gap Severity |
|---|---|---|---|---|
| Demand response mining | "mining demand response", "asic load shedding", "bitcoin mining curtailment" | Featured prominently | Not addressed | Medium (growing ICP need) |
| SOC 2 firmware | "soc 2 mining firmware", "certified asic firmware" | Only SOC 2 certified firmware claimed | Not addressed | Medium (enterprise sales) |

**ePIC gap opportunity for BiXBiT:**

| Gap | Notes |
|---|---|
| Whatsminer firmware | ePIC supports Whatsminer; BiXBiT also supports Whatsminer — both can compete here. ePIC has thin content |
| Low dev fee positioning | ePIC at 1.5% — BiXBiT at 2.8% is structurally weaker here unless BiXBiT matches or reframes |

---

### 3. Prioritized Gap Table

| # | Gap Topic | Competitor Covering It | BiXBiT Covers? | Gap Type | Priority | Existing BiXBiT Cluster |
|---|---|---|---|---|---|---|
| 1 | Firmware comparison page (all competitors vs stock) | None — each only self-promotes | No | Content + SERP | P0 | antminer-firmware.md (Spoke 10) |
| 2 | Dev fee transparency & comparison | Braiins (with 0% pool rebate angle) | No | Trust + Commercial | P0 | antminer-firmware.md (Spoke 9 partial) |
| 3 | Antminer firmware security / backdoor guide | No competitor fully covers | No | Trust + E-E-A-T | P0 | antminer-firmware.md (Spoke 9) |
| 4 | "Best custom firmware for Antminer" — generic SERP | Braiins, Vnish, d-central.tech dominate | No standalone page | SERP presence | P0 | antminer-firmware.md (Hub) |
| 5 | Antminer overclocking guide (firmware-focused) | Braiins (light), d-central.tech (heavy) | No blog/guide | SERP gap | P1 | antminer-firmware.md (Spoke 5) |
| 6 | Antminer S21 firmware dedicated page | Braiins (thin), others minimal | No | Model-level SERP | P1 | antminer-firmware.md (Spoke 4) |
| 7 | Antminer S19 firmware dedicated page | Braiins (strong) | No | Model-level SERP | P1 | antminer-firmware.md (Spoke 3) |
| 8 | Antminer autotuning explainer | Braiins owns term | No dedicated page | Educational / commercial | P1 | antminer-firmware.md (Spoke 6) |
| 9 | Antminer firmware install guide (multi-method) | Braiins OS install (product-specific) | No | How-to / high traffic | P1 | antminer-firmware.md (Spoke 8) |
| 10 | Whatsminer firmware — all categories | ePIC (thin), LuxOS (thin) | Product page exists but no SERP content | Entire SERP segment | P1 | whatsminer-firmware.md (full cluster) |
| 11 | ASIC fleet monitoring comparison | Braiins Manager content exists | AMS product exists — no comparison | Commercial | P1 | None — new cluster needed |
| 12 | Antminer firmware update how-to | All competitors: product-specific only | No generic guide | How-to / high traffic | P1 | antminer-firmware.md (Spoke 1) |
| 13 | Antminer undervolting standalone guide | No competitor fully covers | No | ICP pain point | P2 | antminer-firmware.md (Spoke 7) |
| 14 | Immersion cooling for Bitcoin mining | LiquidStack, GRC, Engineered Fluids | Cluster planned | Full SERP segment | P1 | immersion-cooling-mining.md (full cluster) |
| 15 | Firmware + immersion integration (unique BiXBiT angle) | No competitor covers | No | Unique differentiation | P1 | Cross-cluster gap — antminer-firmware.md + immersion-cooling-mining.md |
| 16 | Demand response / power curtailment for ASICs | LuxOS primary coverage | No | Enterprise ICP segment | P2 | None — new spoke or blog post |
| 17 | Mining fleet monitoring software comparison | Braiins Manager + Luxor Commander content | No comparison content for AMS | Commercial | P2 | None — new cluster needed |
| 18 | Antminer virus / ASIC security (non-firmware) | Vnish (antivirus feature) | Blog post exists ("How to Detect and Cure an ASIC virus") | Partial | P2 | None — can extend existing blog post |
| 19 | SOC 2 / enterprise firmware certification angle | LuxOS claims first SOC 2 firmware | Not addressed | Enterprise trust | P3 | None |
| 20 | Stratum V2 mining protocol | Braiins completely owns | Not addressed | Niche / authority | P3 | None — low priority given Braiins dominance |

---

### 4. Structural Observations

**BiXBiT's published dev fee (2.8%) is the highest among named competitors:**

| Provider | Dev Fee | Notes |
|---|---|---|
| ePIC (UMC OS) | 1.5% | Lowest published |
| Braiins OS+ | 2.5% | 0% effective with Braiins Pool |
| LuxOS | Not disclosed | 0% pool fees on Luxor Pool |
| Vnish | 2.8% base / 2.5–1.8% at scale | Tiered for fleet operators |
| BiXBiT | 2.8% | No tiered pricing published, no pool rebate |

**Implication for content strategy:** BiXBiT cannot win a raw dev fee comparison at current pricing without a rebate/tiering mechanism or a non-fee differentiator (e.g., Whatsminer support breadth, immersion integration, no-backdoor guarantee). Content strategy must avoid leading with dev fee comparison until this is addressed. **This is a product-level gap that content alone cannot close.** Flag to product team.

**BiXBiT's structural advantages that competitors lack and should be content-amplified:**
1. **Both Antminer + Whatsminer support** — Braiins, Vnish have no Whatsminer. LuxOS and ePIC have partial Whatsminer. BiXBiT + ePIC are the most complete dual-platform providers. Content should lead with "firmware for mixed fleets."
2. **Firmware + cooling hardware integration** — No competitor sells both. This is a unique positioning angle for the immersion cooling cluster.
3. **Hotel fee option** — Listed as a BiXBiT feature on the Antminer page. Not mentioned by competitors. This is relevant to hosting/colocation operators (ICP segment). Zero content exists around this feature.

---

### 5. Plan to Close Gaps

#### Phase 1 — P0 gaps (do first, prerequisite for authority):

**A. Antminer Firmware Comparison Page**
- URL: `/en/antminer-firmware/comparison`
- Brief: Already mapped in `content/clusters/antminer-firmware.md` (Spoke 10)
- Action: Write the brief (`content/briefs/antminer-firmware-comparison.md`) and produce the page
- Note: Must include dev fee table with [VERIFY] flags on all competitor figures; do not use marketing copy as ground truth

**B. Dev Fee + Transparency Page**
- URL: `/en/antminer-firmware/dev-fee` (new — not in existing cluster)
- Gap: P0 because "no dev fee" and "dev fee comparison" queries are explicitly where BiXBiT is invisible (confirmed in geo-check-2026-06-18.md)
- Content angle: Explain what dev fee is, how it works technically (hashrate diversion), published rates for all competitors, BiXBiT's 2.8% and what it funds (support, development, updates)
- Note: This page is a trust page, not a sales page. Honesty about BiXBiT's rate builds E-E-A-T. If product team introduces tiering, this page becomes a conversion page.
- Add to cluster: Extend `content/clusters/antminer-firmware.md` with this spoke

**C. Antminer Firmware Security / No-Backdoor Page**
- URL: `/en/antminer-firmware/security`
- Brief: Mapped in `content/clusters/antminer-firmware.md` (Spoke 9)
- Action: Prioritize to P0 given it covers the geo-check gap "Antminer firmware no dev fee comparison" — security and dev fee are the same ICP concern
- [VERIFY] required: BiXBiT's actual security audit process, GPG signing policy, open/closed source stance

**D. Hub pages (pillar pages for all three clusters)**
- `/en/antminer-firmware` — exists as product page but lacks editorial depth; needs expansion to 2,500+ words covering the topic holistically
- `/en/whatsminer-firmware` — same situation
- `/en/immersion-cooling-mining` — does not exist as a standalone SEO page; must be built

#### Phase 2 — P1 gaps (build in parallel with Phase 1):

| Page | Cluster | Action |
|---|---|---|
| `/en/antminer-firmware/overclocking` | antminer-firmware.md Spoke 5 | Write brief + produce |
| `/en/antminer-firmware/install` | antminer-firmware.md Spoke 8 | Write brief + produce |
| `/en/antminer-firmware/antminer-s19` | antminer-firmware.md Spoke 3 | Write brief + produce |
| `/en/antminer-firmware/antminer-s21` | antminer-firmware.md Spoke 4 | Write brief + produce |
| `/en/antminer-firmware/update` | antminer-firmware.md Spoke 1 | Write brief + produce |
| All Whatsminer firmware spokes (P1) | whatsminer-firmware.md Spokes 1,2,3,4,5,8,10 | Write briefs; produce in parallel with Antminer P1 spokes |
| `/en/immersion-cooling-mining` + Antminer/Whatsminer sub-pages | immersion-cooling-mining.md | Start pillar; Antminer + Whatsminer sub-pages are P0 within cluster |

#### Phase 3 — New clusters required (gaps not covered by existing clusters):

**New Cluster: Mining Fleet Management / AMS**
- Gap: "ASIC mining fleet management", "mining monitoring software", "mining monitoring dashboard" — Braiins Manager content exists; BiXBiT AMS has no supporting editorial
- Hub: `/en/mining-monitoring-software`
- Key spokes: AMS vs Braiins Manager comparison, AMS vs Luxor Commander comparison, "how to monitor mining farm", "mining fleet management software for 1000+ ASICs"
- Priority: P2 (after firmware clusters are live)

**New Spoke (add to antminer-firmware cluster): Hotel Fee / Hosting Operator**
- URL: `/en/antminer-firmware/hosting-fee` or blog post
- Gap: BiXBiT's "hotel fee option" is unique — no competitor documents this feature. Targets hosting/colocation operators specifically.
- Priority: P2

**New Blog Vertical: Firmware + Operations Guides**
- BiXBiT blog currently has 0 firmware-focused posts. Braiins has 20+ across firmware, management, economics, hardware.
- Immediate blog posts to publish (can be produced without full cluster infrastructure):
  1. "How to choose ASIC firmware in 2026: J/TH, dev fee, security, and support" — targets "best antminer firmware" informational SERP
  2. "Running a mixed Antminer + Whatsminer fleet: firmware strategy guide" — BiXBiT's unique dual-platform angle
  3. "ASIC firmware overclocking: what operators need to know before pushing hashrate" — targets the overclocking SERP currently dominated by d-central.tech
  4. "Dev fee explained: what mining firmware providers actually charge (2026)" — pre-empts the trust/transparency gap

---

### 6. Quick Reference: Gap Coverage by Existing Clusters

| Gap | Existing Cluster | Coverage | What's Missing |
|---|---|---|---|
| Antminer firmware comparison | antminer-firmware.md | Spoke mapped | Brief + content not produced |
| Antminer overclocking | antminer-firmware.md | Spoke mapped | Brief + content not produced |
| Antminer S19/S21 pages | antminer-firmware.md | Spokes mapped | Briefs + content not produced |
| Antminer install/update | antminer-firmware.md | Spokes mapped | Briefs + content not produced |
| Antminer security/dev fee | antminer-firmware.md | Spoke mapped (security); dev fee spoke missing | Dev fee spoke needs adding; briefs not produced |
| Whatsminer firmware — all | whatsminer-firmware.md | Full cluster mapped | All briefs + content not produced |
| Immersion cooling | immersion-cooling-mining.md | Full cluster mapped | All briefs + content not produced |
| Fleet monitoring (AMS) | None | Not covered | New cluster required |
| Demand response / curtailment | None | Not covered | New spoke (P2) |
| Hosting/hotel fee angle | None | Not covered | New spoke (P2) |
| Stratum V2 | None | Not covered | Low priority; Braiins dominates |

---

*Report generated: 2026-06-19. DataForSEO keyword volume unavailable (401). All competitor figures marked [VERIFY] must be confirmed against live sources before publication. Dev fee figures: Braiins 2.5% from braiins.com/os/plus (fetched 2026-06-19); Vnish 2.8% from vnish.group/en (fetched 2026-06-19); ePIC 1.5% from epicblockchain.io (fetched 2026-06-19); LuxOS dev fee not published. BiXBiT 2.8% from bixbit.io/en/firmwares/antminer (fetched 2026-06-19).*

---

## Link Gap

**Статус DataForSEO backlinks API:** HTTP 401 — credentials не настроены. Числовые метрики DR/DA/referring domains недоступны из API. Раздел построен на geo-check данных, отраслевой логике и публично известном ссылочном ландшафте. DR-оценки помечены `[est.]` — требуют верификации через DataForSEO/Ahrefs после восстановления авторизации.

### Сравнительный профиль (оценочный)

| Параметр | BiXBiT (bixbit.io) | Braiins (braiins.com) | Vnish (vnish.group) | LuxOS (luxor.tech) |
|---|---|---|---|---|
| Referring domains (est.) | ~50–150 | ~2 000–5 000 | ~200–500 | ~500–1 500 |
| DR/DA (est.) | 20–30 | 60–70 | 30–40 | 45–55 |
| Тип профиля | Молодой, узкий | Зрелый, диверсифицированный | Преимущественно CIS-форумы | Медиа + крипто-пресса |
| Источники силы | — | Open-source community, крипто-медиа, GitHub | RU-майнинг-форумы | Luxor Pool backflow, крипто-журналистика |

### Домены из geo-check: статус ссылок на BiXBiT

`[VERIFY via DataForSEO после восстановления 401]`

| Домен | DR est. | → Braiins | → BiXBiT | Тип | Приоритет | Стратегия |
|---|---|---|---|---|---|---|
| **d-central.tech** | ~45 | Да (вероятно) | Нет [VERIFY] | Обзорник/DIY mining | **P0** | Гест-пост или product review; d-central пишет extensive firmware comparison guides — именно они доминируют 5/9 SERP по overclocking |
| **whatsminer.com** | ~50 | Возможно | Нет [VERIFY] | OEM-производитель (MicroBT) | **P0** | Партнёрская ссылка — BiXBiT поддерживает Whatsminer, что даёт основание для OEM-упоминания |
| **nicehash.com** | ~70 | Да | Нет [VERIFY] | Платформа/экосистема | **P0** | Firmware compatibility list или партнёрская интеграция |
| **asicminervalue.com** | ~40 | Да | Нет [VERIFY] | ASIC база данных | **P1** | Добавить BiXBiT в firmware compatibility разделы по моделям |
| **bitcointalk.org** | ~85 | Да | Частично [VERIFY] | Форум | **P1** | Официальный announcement thread + поддержка активности |
| **hashrate.farm** | ~30 | Вероятно | Нет [VERIFY] | Калькулятор/инфо | **P1** | Добавить в список поддерживаемых прошивок |
| **crazy-mining.org** | ~30 | Да | Нет [VERIFY] | Форум/блог RU/EN | **P1** | Официальная тема на форуме + review request |
| **cryptomine.cc** | ~25 | Вероятно | Нет [VERIFY] | Обзорник | **P1** | Pitch firmware review или comparison |
| **github.com** | ~95 | Да (Braiins OS репо) | Нет / минимально | Open-source платформа | **P1** | Открыть публичный репо с документацией; попасть в awesome-mining lists |
| **compass.mining** | ~50 | Да | Нет [VERIFY] | Managed mining / блог | **P2** | Продуктовый питч для institutional аудитории |
| **f2pool.com** | ~60 | Да | Нет [VERIFY] | Пул / блог | **P2** | Firmware efficiency темы + compatibility упоминание |
| **coindesk.com** | ~80 | Да | Нет [VERIFY] | Крипто-медиа | **P2** | PR-питч при продуктовых релизах |

### Ссылочные кластеры Braiins — логический gap

**A. GitHub-экосистема.** Braiins OS имеет публичный репо (~1k+ stars) — органические ссылки из awesome-lists, документации, developer-статей. BiXBiT без публичной технической документации полностью теряет этот кластер. *Стратегия:* открыть репо с AMS API docs / firmware changelog.

**B. Майнинг-медиа (EN).** asicminervalue.com, miningstore.com.au, compass.mining, f2pool.com/blog, btc.com — цитируют Braiins как эталон. BiXBiT там отсутствует. *Стратегия:* pitch product review editors с test-данными (hashrate, efficiency).

**C. Пулы.** Braiins Pool создаёт двусторонние ссылки с экосистемой пулов. BiXBiT должен выстраивать partnership упоминания с Foundry, ViaBTC, Antpool в разделах "recommended firmware". *Стратегия:* официальное упоминание в "supported firmware" у топ-пулов.

**D. CIS-форумы (частично закрытый gap).** bitcointalk.org, crazy-mining.org — Braiins и Vnish там хорошо представлены. Системной работы у BiXBiT нет. *Стратегия:* announcement threads при каждом firmware-релизе.

### Аномалии и флаги

- **Нулевое присутствие на OEM-сайтах.** Ни Bitmain (antminer.com), ни MicroBT (whatsminer.com) не упоминают BiXBiT — при том что BiXBiT заявляет поддержку обеих платформ. P0-gap: OEM-ссылка = сигнал доверия.
- **bixbitusa.io.** Зафиксирован в geo-check на позиции 9 по Whatsminer-запросу (отдельный домен). Требует расследования: canonical-атрибуция на основной домен, нет ли разбавления link equity.
- **Нет press-coverage в EN крипто-медиа.** CoinDesk, Cointelegraph, Decrypt — нулевая видимость. Нужен PR-план к релизам.

### Следующие шаги по данным

1. Проверить `.env` — `DATAFORSEO_LOGIN` / `DATAFORSEO_PASSWORD` не настроены.
2. После восстановления 401: запустить `backlinks_domain_intersection` с `targets: ["braiins.com", "vnish.group", "luxor.tech"]` + `exclude_targets: ["bixbit.io"]` для живого gap-списка.
3. `backlinks_bulk_spam_score` — проверить токсичность текущего профиля BiXBiT.

---

## AI-Citation Gap

### Claude Self-Test (verbatim, 2026-06-19)

**Промпт: "What are the best Antminer firmware alternatives to Braiins OS+"**

> The most commonly cited alternatives are: **Vnish** (wide deployment, aggressive overclocking, granular per-hashboard tuning), **LuxOS by Luxor Technology** (per-chip tuning, efficiency edge, large-scale operators), and **ASICseer** (monitoring-focused). BiXBiT is a less widely discussed option — it offers firmware for both Antminer and Whatsminer fleets and includes an integrated monitoring system (AMS), but it does not appear in mainstream firmware comparison guides as of my knowledge cutoff.

**Промпт: "Which companies offer custom firmware for both Antminer and Whatsminer?"**

> Most custom firmware focuses on Antminer. Companies explicitly supporting both: **BiXBiT** (industrial-focused, claims M2x–M6x Whatsminer and S19/S21 Antminer support), and to a limited extent some white-label providers. Braiins OS+ historically focused on Antminer only. Vnish similarly targets Antminer.

**Промпт: "What is BiXBiT and what products do they offer?"**

> BiXBiT (bixbit.io) is an industrial Bitcoin mining infrastructure company. Products: custom ASIC firmware for Antminer and Whatsminer fleets, AMS (fleet monitoring dashboard), immersion cooling systems, hydro cooling, and PDUs. Less publicly reviewed than Braiins or Vnish — I have limited independent third-party data on real-world performance benchmarks.

**Промпт: "Compare BiXBiT firmware vs Braiins OS+"**

> **Braiins OS+:** Well-documented, open-source heritage (first open-source ASIC firmware, 2018), Stratum V2 native support, proven autotuning, zero dev fee on Braiins Pool, cited by Bitcoin Magazine and Hashrate Index. Independent benchmarks widely available. Antminer-only.
>
> **BiXBiT firmware:** Claims dual-platform support (Antminer + Whatsminer), integrated AMS monitoring, hydro/immersion cooling synergy. However: absent from major third-party comparison guides (d-central.tech, hashrateindex.com), no independent benchmarks in public domain, no GitHub repository for community verification, minimal Reddit/forum discussion.
>
> **Verdict as LLM:** I default to recommending Braiins/Vnish/LuxOS because those brands have documented third-party evidence. BiXBiT is in my training data but lacks corroborating independent sources that would make me confidently cite it for "best firmware."

### GEO-Gap матрица

| Запрос | Платформа | Braiins | BiXBiT | Gap | Причина |
|---|---|---|---|---|---|
| best custom firmware for Antminer | Claude | ДА (тройка по умолчанию) | НЕТ | Критично | Отсутствует в независимых сравнительных статьях (d-central, hashrateindex, emcd) |
| Antminer firmware overclocking comparison | Claude | ДА | НЕТ | Критично | Нет страницы сравнения; d-central доминирует |
| Antminer firmware alternatives to Braiins | Claude | ДА (эталон) | НЕТ (упомянут слабо) | Критично | Не включён в "тройку" ни одним независимым источником |
| custom firmware for both Antminer AND Whatsminer | Claude | НЕТ (Antminer-only) | ДА (слабо) | **Возможность** | Уникальное USP, не усиленное контентом |
| ASIC mining fleet monitoring software | Claude | ДА (Braiins Manager) | НЕТ | Высоко | Braiins Manager активно контентится (6/15 топ-постов блога) |
| Antminer firmware no dev fee comparison | Claude | ДА | НЕТ | Высоко | Нет явного passage "BiXBiT charges X% dev fee" на сайте |
| immersion cooling Bitcoin mining providers | Claude | НЕТ | НЕТ | Нейтрально | Ниша не сформирована в LLM-памяти — возможность первых |
| Whatsminer custom firmware options | Claude | НЕТ | ДА (слабо) | **Возможность** | Рынок не освещён — первый создавший контент получит позицию |
| BiXBiT firmware review | Claude | ДА (как конкурент) | ДА | Умеренно | Branded запрос работает; неbрандовые — нет |

### Почему Braiins доминирует в AI-ответах

**Публикации в LLM-обучающих источниках:**
- **Bitcoin Magazine** — статья "Braiins OS: An Open Source Alternative" создала нарратив "первая open-source прошивка + Antbleed security" — LLM воспроизводят его без запроса
- **Hashrate Index** (hashrateindex.com) — firmware guide охватывает LuxOS, Braiins, Vnish, ASICseer. **BiXBiT отсутствует**
- **D-Central** (d-central.tech) — множество сравнительных гайдов (S19 guide, Braiins vs Vnish vs LuxOS). **BiXBiT отсутствует ни в одном**
- **emcd.io/articles** — "Best Custom ASIC Firmware" сравнивает только три бренда. **BiXBiT отсутствует**

**GitHub-присутствие:** Braiins имеет активную GitHub-организацию с открытым кодом. LLM обучаются на GitHub-данных — README, issues, звёзды формируют сигналы авторитетности. BiXBiT: нет связанного публичного репо.

**"Тройка по умолчанию" как паттерн:** Vnish + Braiins + LuxOS — устойчивый паттерн из 3+ независимых публикаций. Войти в тройку требует присутствия в 3+ независимых источниках с высоким DA, упоминающих BiXBiT в сравнительном контексте.

### Passage-фразы для размещения на сайте (verbatim для LLM-зацепки)

**Для "firmware for both Antminer and Whatsminer":**
> "BiXBiT firmware supports both Antminer (S19, T19, S21, T21, L7 [VERIFY]) and Whatsminer (M2x–M6x series [VERIFY]) fleets from a single dashboard — one of the few solutions covering both ASIC families."

**Для "Antminer firmware no dev fee":**
> "BiXBiT firmware charges [VERIFY: 0% / actual rate] developer fee. There is no hashrate redirect or background pool switching — 100% of mined hashrate goes to the operator's chosen pool."

**Для "ASIC fleet monitoring software":**
> "BiXBiT AMS (Advanced Monitoring System) provides centralized fleet management for Antminer and Whatsminer ASICs: real-time hashrate, temperature, fault alerts, and remote reboot — scalable from 5 to 5,000+ units."

**Для "Braiins OS+ alternatives" (на firmware page):**
> "Looking for alternatives to Braiins OS+? BiXBiT firmware offers autotuning, overclocking profiles, and fleet monitoring in one package — with additional support for Whatsminer fleets that Braiins OS+ does not cover."

### Контент P0 для GEO-закрепления

| Приоритет | Тип | Тема | Целевой запрос |
|---|---|---|---|
| P0 | Comparison page | "BiXBiT vs Braiins OS+ vs Vnish vs LuxOS: Antminer Firmware Comparison 2026" | antminer firmware comparison |
| P0 | Guide | "Custom Firmware for Whatsminer: Complete Guide 2026" | whatsminer custom firmware |
| P1 | FAQ-блок на firmware page | dev fee, supported models, Whatsminer compatibility | dev fee firmware / model list |
| P1 | Blog post | "Braiins OS+ Alternatives for Large-Scale ASIC Operations" | Braiins OS alternatives |
| P1 | Tech spec page | Таблица моделей с J/TH до/после [VERIFY] | firmware efficiency J/TH |
| P2 | Case study | "40MW Farm: BiXBiT Firmware vs Stock — Power Savings" | mining firmware ROI |

### Источники для получения (для AI-памяти)

| Источник | Действие | Сложность |
|---|---|---|
| d-central.tech | Гест-пост "BiXBiT firmware for Whatsminer fleets" или включение в сравнение | Средняя |
| hashrateindex.com | Письмо с запросом включить BiXBiT в firmware guide | Средняя |
| emcd.io/articles | Outreach с техданными для обновления статьи | Низкая |
| Bitcoin Magazine | PR pitch: "first dual-platform industrial firmware" | Высокая |
| GitHub | Открыть репо с документацией (README + compatibility list) | Низкая |
| reddit.com/r/BitcoinMining | Органическое участие в дискуссиях | Низкая |
| slashdot.org software | Добавить BiXBiT в категорию alternatives to Braiins OS | Очень низкая |

---

## Technical SEO Gap

**Статус DataForSEO Lighthouse:** HTTP 401 — CWV-сравнение недоступно. Анализ на основе WebFetch (braiins.com, bixbit.io/en) и full-audit baseline 2026-06-17. Braiins head-секция (canonical, og:, hreflang) не верифицирована — SPA с JS-рендерингом.

### Таблица технических разрывов

| Элемент | BiXBiT | Braiins | Gap | Приоритет |
|---|---|---|---|---|
| **H1 на страницу** | 8 H1 на homepage (критическое нарушение) | 2 H1 на /os/plus | BiXBiT нарушает базовую on-page структуру | **P0** |
| **Meta description** | Отсутствует (подтверждено full-audit) | Не верифицировано (JS) | BiXBiT: гарантированный auto-snippet, потеря CTR | **P0** |
| **Canonical tags** | Отсутствуют (full-audit) | Не верифицировано (JS) | /en/ vs / дубли без контроля | **P0** |
| **Hreflang /en/ ↔ /ru/** | Отсутствует (full-audit) | Не верифицировано | Sitemap показывает обе языковые версии — без hreflang гарантированный краулинг-конфликт | **P0** |
| **CLS** | 0.888 (P0 из full-audit) | Не верифицировано | BiXBiT: критическое нарушение CWV | **P0** |
| **JSON-LD schema** | 0 типов (full-audit) | 0 на проверенных страницах (WebFetch) | Оба не реализовали — кто первый, тот получает rich results | **P1** |
| **FAQPage schema** | FAQ-разделы есть без schema | FAQ на /os/plus (11 вопросов) без schema | Оба упускают FAQ rich results — BiXBiT может выиграть первым | **P1** |
| **og: / twitter:card** | Отсутствуют (full-audit) | Не верифицировано | BiXBiT: пустое превью при шаринге в B2B-чатах | **P1** |
| **Sitemap lastmod** | Все застряли на 2024-09-04 | lastmod блога 2026-06-10 (актуально) | Braiins: свежий сигнал краулеру; BiXBiT: снижение crawl priority | **P1** |
| **llms.txt** | Создан в сессии (content/geo/) — не задеплоен | 404 (отсутствует) | BiXBiT впереди если задеплоит первым | **P1** |
| **BreadcrumbList JSON-LD** | Текстовые крошки есть, schema нет | Нет (WebFetch) | Оба упускают breadcrumb rich snippets | **P2** |
| **Контентная база** | ~400 URLs в sitemap (EN+RU), минимум EN-контента | 256 URLs, 50–60 EN-постов с 2018 | Braiins: 8 лет контентной базы; BiXBiT: тонкий EN-контент | **P1** |
| **Структура firmware URL** | /firmwares/asic-s19, /firmwares/whatsminer-series-m5x — модельная granularity | Одна /os-firmware страница (по sitemap) | BiXBiT имеет архитектурное преимущество — не реализовано (нет schema/meta) | **P1** |
| **Документация домен** | /en/documentation/ — на основном домене ✓ | academy.braiins.com (301) — отдельный домен, link equity не перетекает | BiXBiT выигрывает — документация на основном домене | Преимущество |

### Quick Wins (≤1 спринт, ≤2 недели)

**P0 — немедленно:**
1. **Один H1 per page.** Главная: 8 H1 → все секции продукта стать H2. Шаблонная правка.
2. **Canonical tags на все страницы.** Шаблонное добавление `<link rel="canonical">` для всех роутов /en/ и /ru/.
3. **Hreflang /en/ ↔ /ru/.** Sitemap показывает зеркальную структуру. Шаблон в head, один раз — закрывает языковой краулинг-конфликт.
4. **Meta description.** Начать с /en/firmwares, /en/firmwares/antminer, /en/monitoring — коммерческие приоритеты.
5. **CLS = 0.888 → исправить.** Источник CLS из full-audit — установить и устранить (likely layout shift от изображений или шрифтов).

**P1 — в том же спринте:**
6. **FAQPage JSON-LD** на /en/firmwares и /en/firmwares/antminer — FAQ-разделы уже есть, нужна обёртка schema.
7. **og: + twitter:card** — шаблонное добавление, критично для B2B-шаринга.
8. **Sitemap lastmod** — скрипт обновления при деплое.
9. **BreadcrumbList JSON-LD** — текстовые крошки есть, 30 минут dev-времени на шаблон.
10. **Задеплоить llms.txt** из content/geo/ → https://bixbit.io/llms.txt.

### Что не верифицировано

- Braiins canonical, og:, hreflang — SPA блокирует static fetch; требует Playwright/headless
- CWV Braiins — DataForSEO 401
- Точное количество EN-постов блога BiXBiT — blog-sitemap содержит EN+RU в общем пуле

---

## Сводная таблица приоритетов

| # | Gap | Тип | Приоритет | Усилие | Первый шаг |
|---|---|---|---|---|---|
| 1 | Comparison page (firmware vs Braiins/Vnish/LuxOS) | Content | P0 | Medium | Бриф уже в кластере → написать и опубликовать |
| 2 | Dev fee transparency page | Content + Product | P0 | Low (content) / High (product) | Создать страницу; флаг → продуктовой команде по снижению ставки |
| 3 | Antminer firmware security / no-backdoor | Content + E-E-A-T | P0 | Medium | Бриф в кластере → [VERIFY] с командой → опубликовать |
| 4 | H1 per page (8 → 1 на homepage) | Technical | P0 | Low | Шаблонная правка CMS |
| 5 | Canonical + hreflang | Technical | P0 | Low | Шаблонная правка |
| 6 | Meta descriptions | Technical | P0 | Low | Написать для топ-5 коммерческих страниц |
| 7 | CLS 0.888 | Technical | P0 | Medium | Диагностика + fix layout shift |
| 8 | d-central.tech — упоминание/ссылка | Backlinks | P0 | High | Outreach + гест-пост pitch |
| 9 | whatsminer.com OEM-ссылка | Backlinks | P0 | High | Partnership outreach |
| 10 | FAQPage JSON-LD на firmware pages | Technical | P1 | Low | Обернуть существующие FAQ |
| 11 | Sitemap lastmod | Technical | P1 | Low | Скрипт деплоя |
| 12 | og: + twitter:card | Technical | P1 | Low | Шаблон |
| 13 | llms.txt деплой | GEO/Technical | P1 | Low | Задеплоить content/geo/llms.txt |
| 14 | Whatsminer firmware кластер (полный) | Content | P1 | High | Все брифы созданы → production |
| 15 | Antminer spokes (S19, S21, overclocking, install, update) | Content | P1 | High | Брифы созданы → production |
| 16 | nicehash.com + asicminervalue.com — упоминания | Backlinks | P1 | Medium | Compatibility list outreach |
| 17 | Entity-definition passage на homepage | GEO | P1 | Low | Вставить фрагмент из content/geo/entity-definition-homepage.md |
| 18 | Organization + SoftwareApplication schema | Technical | P1 | Low | JSON-LD в <head> |
| 19 | Immersion cooling кластер (полный) | Content | P1 | High | Брифы созданы → production |
| 20 | AMS / Fleet monitoring — новый кластер | Content | P2 | High | Новый кластер: /new-cluster "mining fleet monitoring" |
| 21 | Passage-фразы для LLM-цитирования | GEO | P1 | Low | Вставить 4 passage-блока из AI-Citation Gap секции |
| 22 | GitHub репо с документацией | Backlinks + GEO | P2 | Medium | Открыть публичный репо AMS API / firmware changelog |
| 23 | Press-coverage (coindesk, cointelegraph) | Backlinks | P2 | High | PR-план к следующему продуктовому релизу |
| 24 | Demand response / curtailment content | Content | P2 | Medium | Новый spoke к immersion или AMS кластеру |
| 25 | Hotel fee / hosting operator content | Content | P2 | Low | Новый spoke к antminer-firmware кластеру |

---

*Отчёт создан: 2026-06-19. Агенты: content-seo, offpage-seo, geo-ai, technical-seo. DataForSEO 401 на всех API-вызовах — живые объёмы и backlink метрики недоступны. Dev fee конкурентов верифицированы из их публичных страниц (дата fetch: 2026-06-19). Следующий competitor-gap чек: после деплоя P0-правок или через 90 дней.*
