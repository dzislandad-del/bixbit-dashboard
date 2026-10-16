# Content SEO Audit — bixbit.io/en
**Date:** 2026-09-16
**Scope:** Full-site content coverage vs. CLAUDE.md §3 priorities, cluster-hub-and-spoke gap analysis, E-E-A-T, PDU page completeness.
**Auditor:** Content & Clusters agent
**Inputs used:** `data/site-structure.md` (rewritten 2026-09-16), `reports/sub/technical-seo-2026-09-16.md`, all files in `content/briefs/` and `content/clusters/` (dated 2026-06-18/19), `content/page-optimize/{homepage,ams,firmwares,firmwares-hub,firmwares-antminer}.md` (referenced, not duplicated), plus live WebFetch spot-checks of `/en/blog`, `sitemap-blog.xml`, `/en/about`, one blog post, one documentation article, `/en/products/pdu`, `/en/asics-cooling/immersion-systems`, `/en/asics-cooling/hydro-systems`, `/en/firmwares/whatsminer-series-m6x`, `/en/firmwares/antminer`.

**Data gaps (honest accounting):** DataForSEO and GSC/GA4 were not connected this session — no search volume, ranking, click, or impression data anywhere in this report. All findings below are structural/qualitative (what exists, what's missing, what's inconsistent), never invented traffic/volume numbers. Blog-topic and cooling/PDU page-content findings are based on WebFetch sampling (1 blog post, 2 cooling sub-pages, 1 firmware series page, 1 documentation article, the blog index, and the sitemap) — not an exhaustive crawl of all ~400 blog URLs or all firmware/documentation pages; treat percentages/impressions as directional, not census data.

---

## 0. Headline finding — the "no dev fee" differentiator baked into two P0 briefs is factually wrong

`content/briefs/antminer-firmware-pillar.md` and `content/briefs/whatsminer-firmware-pillar.md` (both June 2026) build their core trust/security differentiator around **"No dev fee — zero hidden hashrate redirection; operator retains 100% of mining output,"** and both draft an explicit FAQ answer: *"Does BiXBiT firmware charge a dev fee? A: No."* (with a `[VERIFY]` tag attached, but framed as the expected answer).

Live WebFetch of `/en/firmwares/antminer` and `/en/firmwares/whatsminer-series-m6x` today confirms the opposite: BiXBiT firmware **does charge a developer fee — 2.8% of mined hashrate** (2% on the Whatsminer M2x series per `content/page-optimize/firmwares.md`, already independently confirmed by today's page-optimize pass), disclosed on-page under "Transparent Pricing" / "Usage Cost" after a 30-day trial. This is corroborated by the parallel `page-optimize` work done today (`firmwares.md`, `firmwares-antminer.md`, `firmwares-hub.md` all treat 2.8%/2% as confirmed on-page fact) and by `homepage.md`'s own open `[VERIFY: confirm dev fee = 0% before publishing]` flag, which this audit resolves — the answer is **not 0%.**

**Impact:** Both firmware pillar briefs' "no dev fee" positioning, FAQ Q1 answers, and E-E-A-T "trustworthiness" framing must be rewritten before any writer uses them — as drafted, they would ship a false, easily fact-checked claim to a technical B2B audience (the exact reputational risk CLAUDE.md §4 and §7 warn against). The competitive angle against Braiins OS+ (free/open-source) and Vnish/LuxOS (also fee-based) needs re-framing around **transparent, disclosed fee vs. undisclosed fees**, not "we charge nothing."

**Priority: P0. Effort: Low** (edit two brief files + flag to whoever eventually writes the live copy). This should happen before either brief is handed to a writer.

---

## 1. Cluster coverage vs. CLAUDE.md §3 priorities

| Priority | Cluster | Live pages found (site-structure.md) | Verdict |
|---|---|---|---|
| P1 | ASIC firmware (Antminer/Whatsminer, overclocking/underclocking/autotuning) | `/en/firmwares` (hub), `/en/firmwares/antminer` (hub only), 4 Whatsminer series pages, 7 legacy Antminer model pages (now noindexed) | **Hub-only.** No topic-based spoke content (overclocking/autotuning/undervolting/security/comparison as standalone pages) exists anywhere. See §2. |
| P2 | Immersion / Hydro cooling | `/en/asics-cooling` (hub) + `/en/asics-cooling/immersion-systems` + `/en/asics-cooling/hydro-systems` | **Best-covered cluster on the site.** Real product SKUs, PUE case-study data, deployment specs — see §2 and §4. Ironically this P2 cluster is more mature than the P1 firmware cluster. |
| P3 | Mining monitoring / AMS | `/en/ams` (hub, already optimized today) + `/en/ams/connect` (thin) | Hub is strong (per today's `ams.md` page-optimize); zero of 11 planned spoke pages exist. |
| P4 | PDU / power distribution | `/en/products/pdu` (single page, no sitemap presence — flagged P0 by technical-seo) | Single consolidated page with real spec table but no comparison/FAQ/spoke content. See §4. |
| — | Blog (content distribution) | ~400 URLs, actively publishing | **Volume does not equal relevance — see §1a.** |
| — | Documentation | 5 sitemap URLs + confirmed deeper nested structure (error-code sub-pages, PSU/network guides) not in any sitemap | Genuinely useful long-tail firmware/Whatsminer support content, but orphaned from search discovery (technical-seo already flagged hub absence; nested child pages are *also* absent, a new finding — see §1b). |

### 1a. Blog: ~400 URLs, but topic mix is diluted against CLAUDE.md priorities

This is the single largest structural change since June (blog went from "not found" to ~400 URLs), so it needs a real verdict, not just a headcount.

Sampled the blog index and sitemap slugs. Tag taxonomy in use: `BiXBiT, BITCOIN, MINING, CRYPTOCURRENCY, ASIC, TECHNOLOGIES, CRYPTO, IMMERSIONCOOLING, BLOCKCHAIN, Longread, FPGA, GPU, LEGISLATION, COMPANY, PERSON, NEWS, RATINGS, FINANCE, ECONOMY, HEATUTILIZATION, FIRMWARE, AI`.

Of the 6 most recent posts sampled (newest = 1 week old), **zero were tagged FIRMWARE**, one was tagged IMMERSIONCOOLING-adjacent ("Hydro ASIC 2026" under MINING), and four were company-news/conference/AI-infrastructure pieces (WDMS Bitmain, ISC High Performance, GITEX AI Central Asia, "crypto mining as AI infrastructure"). The "Popular Articles" widget surfaces two immersion-cooling posts, a security post ("How to Detect and Cure an ASIC virus"), and a 2018-era ASIC ratings post.

Sitemap slug sampling shows large categories of content clearly outside CLAUDE.md §3 priorities entirely: **cryptocurrency/altcoin price analysis, proof-of-stake explainers, regional mining-legislation news, general finance/economy content.** These exist under tags `CRYPTOCURRENCY, BLOCKCHAIN, LEGISLATION, FINANCE, ECONOMY, RATINGS` — none of which map to firmware, cooling, monitoring, or PDU.

**Verdict:** the blog is a general crypto-news/company-blog, not a topically-focused content-marketing engine for the four priority clusters. It is actively publishing (good cadence, real freshness signal), and cooling content does appear reasonably often, but **firmware — the #1 stated priority — is visibly under-represented in the recent cadence**, and a large fraction of the ~400 URLs (price/legislation/finance/altcoin news, thin 2018-era ratings posts) sit outside the ICP pain points this project is meant to serve (J/TH efficiency, uptime, firmware security, fleet monitoring). This is not a "delete the blog" finding — general crypto content has legitimate traffic/brand value — but it means **the blog cannot be counted as progress against the firmware/cooling/monitoring/PDU content plan**, and a content-calendar rebalancing toward FIRMWARE/IMMERSIONCOOLING/HEATUTILIZATION tags is a real opportunity, especially against Braiins/Vnish who publish more technical firmware content than event/PR posts.

**Priority: P2. Effort: Medium** (editorial calendar/tag-mix policy change, not a technical fix). Hand to a future content-plan pass: recommend a minimum-cadence quota (e.g., 1 in 3 posts tagged FIRMWARE or IMMERSIONCOOLING/HEATUTILIZATION) and a pruning/consolidation review of the 2018–2019-era thin posts already flagged by technical-seo (sitemap-blog.xml still lists them).

### 1b. Documentation hub has more real depth than the sitemap shows — new finding

WebFetch of `/en/documentation/error-codes-for-whatsminer-asic` shows it is itself a thin index page linking to deeper content not present in `sitemap-documentation.xml`'s 5 URLs — e.g. `/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1`, plus references to WhatsPower PSU guides, overclocking documentation, and network/pool-configuration pages. None of this nested tier appears to be in any sitemap (technical-seo only confirmed the 5 top-level documentation URLs).

**This is a real, if narrower, content asset that already exists and is orphaned from search discovery** — it's Whatsminer/MicroBT-specific technical support content (error codes, PSU wiring, overclocking setup) that maps directly onto the P1 firmware priority and P3 monitoring/AMS appendix content, but is invisible to Google beyond internal links. Hand to technical-seo for a proper crawl of the full documentation tree and sitemap inclusion; flagging here because it changes the "documentation = 5 thin articles" read from the site-structure file into "documentation = a real but undiscoverable knowledge base."

**Priority: P1. Effort: Low-Medium** (crawl + add to sitemap; no new content needed, just discoverability).

---

## 2. Cluster gaps: planned (June briefs) vs. published (September site-structure)

This is the direct progress check requested: of ~45 spoke/pillar URLs specified across the five June-dated pillar briefs (`antminer-firmware-pillar.md`, `whatsminer-firmware-pillar.md`, `immersion-cooling-mining-pillar.md`, `mining-fleet-monitoring-pillar.md`/AMS, `pdu-pillar.md`), **effectively zero were published as separate URLs in the planned URL scheme in the three months since.** More importantly, **the live site never adopted the briefs' proposed URL architecture at all** — it uses a completely different IA:

| Cluster | Brief's planned pillar URL | Live pillar URL | Planned spokes (10–11 each) | Spokes actually live |
|---|---|---|---|---|
| Antminer firmware | `/en/antminer-firmware` | `/en/firmwares/antminer` | update, custom, antminer-s19, antminer-s21, overclocking, autotuning, undervolting, install, security, comparison | **0 of 10.** (7 legacy per-model pages exist but were *demoted* to noindex+self-canonical during this period — the opposite direction from the brief, which wanted *more* granular spoke pages, not fewer.) |
| Whatsminer firmware | `/en/whatsminer-firmware` | `/en/firmwares/whatsminer-all-series` | update, custom, whatsminer-m30s, whatsminer-m50, overclocking, autotuning, undervolting, install, security, comparison | **0 of 10 by the brief's naming/topic split**, but 4 series-group pages exist (`whatsminer-series-m6x/m5x/m3x/m2x`) that partially cover feature ground under a different structure — spot-check of `-m6x` shows it already bundles autotuning, undervolting ("downvolting"), a 5-step install flow, and a 10+ question FAQ **into one page**, rather than the brief's one-topic-per-URL split. This is a legitimate alternate IA choice (denser hub pages vs. many thin spokes) but means the brief's spoke plan should be revised, not just "not done yet." |
| Immersion cooling | `/en/immersion-cooling-mining` | `/en/asics-cooling` (+ `/hydro-systems`, `/immersion-systems`) | vs-air-cooling, single-phase, two-phase, antminer, whatsminer, roi, setup-guide, tank, dielectric-fluid | **0 of 9** as separate URLs — but see §4: the live `/immersion-systems` and `/hydro-systems` pages already contain real PUE/case-study data that resolves several of the brief's `[VERIFY]` blockers (tank capacity, PUE, deployment scale, compatible models). The brief's IA (single "immersion-cooling-mining" pillar) doesn't match the live IA (parallel hydro/immersion sub-hubs under one cooling hub) — the brief needs restructuring, not just spoke production. |
| Monitoring / AMS | `/en/ams` (update existing page) | `/en/ams` | vs-braiins-manager, vs-luxor-commander, vs-minerstat, mining-farm-monitoring-software, asic-fleet-management, antminer-monitoring-software, whatsminer-monitoring-software, mining-farm-alerts-automation, mining-hosting-monitoring, mining-farm-power-monitoring, mining-fleet-dashboard | **0 of 11.** This is the only cluster where the brief's pillar URL matches the live URL exactly, and per today's separate `page-optimize/ams.md` pass the hub itself is the most schema-complete page on the site. Zero spokes exist — none of the three named competitor-comparison pages (`vs-braiins-manager`, `vs-luxor-commander`, `vs-minerstat`) are live, despite full comparison briefs already written and sitting in `content/briefs/`. |
| PDU | `/en/pdu` | `/en/products/pdu` | per-outlet-metering, remote-switching, overload-protection, ams-integration, sizing-asic-farm, vs-direct-wiring, vs-unmanaged-pdu, data-center-mining | **0 of 8** — single consolidated page instead. See §4 for detailed gap-fill assessment. |

**Net read:** in three months, the site's actual content investment went into (a) the blog (volume, mixed topical relevance — §1a), (b) the calculator/FAQ tools, (c) the documentation knowledge base, and (d) consolidating/pruning legacy Antminer model pages — **not** into publishing any of the ~45 spoke pages specified in the ready-to-use June briefs. The AMS competitor-comparison briefs (`ams-vs-braiins-manager.md`, `ams-vs-luxor-commander.md`, `ams-vs-minerstat.md`) are fully written, `[VERIFY]`-flagged, and sitting unused — these are the lowest-effort, highest-differentiation gap to close first since AMS's "supports Whatsminer, Braiins doesn't" claim is explicitly called out in the brief as the strongest available differentiator and nothing competing pages exist to capture that comparison search intent.

**Recommendation, not just observation:** rather than resuming the June briefs' spoke plan as-is, the plans need a one-time reconciliation pass against the real IA (`/en/firmwares/*`, `/en/asics-cooling/*`, `/en/products/pdu`, `/en/ams/*`) before any more writer time is spent — otherwise new content gets written against URLs that don't match how the site is actually organized today. `content/internal-linking.md` (June, 54KB) is built entirely against the old planned URL scheme (`/en/antminer-firmware`, `/en/pdu`, `/en/immersion-cooling-mining`) and is **not usable as-is** against the real site — it needs a full rebuild against confirmed live URLs, not incremental edits.

**Priority: P0 (the IA-mismatch itself, since it blocks all future spoke work) / P1 (each individual missing spoke). Effort: Low** to re-scope (this audit + a rewrite pass), **Medium-High** to actually produce ~40 spoke pages.

---

## 3. E-E-A-T signals — sitewide

**No named individual authorship exists anywhere on the site that was checked** — this is a consistent, sitewide gap, not a per-page oversight:

- **Blog posts:** WebFetch of a recent post (`hydro-asic-2026-ranking-models-for-largescale-mining-farms`) confirms a relative publish date ("1 month ago," no absolute date, no last-updated date) but **no author byline, name, or title** — "content is attributed to BiXBiT organization" only. No external citations/sources — all technical claims (specific TH/s, J/TH, W figures for Bitmain Antminer S23 Hyd variants) are stated as fact with zero sourcing, which is a real E-E-A-T weakness against Braiins (which publishes benchmark methodology) even where the specs themselves may be accurate.
- **Documentation:** same pattern — no author/engineer name on the error-codes page.
- **Firmware series page** (`/en/firmwares/whatsminer-series-m6x`): no byline; "content attributed to BiXBiT organization."
- **`/en/about`:** confirmed via WebFetch — **no named individuals, founders, or leadership at all.** It does contain real, usable E-E-A-T material that is *not* being surfaced elsewhere on the site: founding date (September 2016), a real company timeline (air-cooling → liquid formula April 2017 → prototype July 2017 → production April 2018 → software dept. Nov 2018 → AMS launched Sept 2022 → Poland/USA expansion Oct 2022), "7+ years of expertise in cooling computing equipment," and real office locations (HQ Poland; USA office in Burleson, TX; Europe/North America/South Asia presence). It references "qualified engineers" and a "dedicated design department" but **no names, headcounts, or credentials** — the page explicitly avoids naming individual leadership.

**Assessment against CLAUDE.md §4/E-E-A-T priorities:** the raw materials for E-E-A-T (a real 9-year operating history, named product SKUs, real deployment case studies with PUE/uptime numbers — see §4) exist on the site, but **zero of it is connected to a named human expert.** Every firmware/cooling/monitoring claim on every page type sampled is anonymous-organizational. This is a bigger structural E-E-A-T gap than "add author bios" — it means none of the June briefs' repeated `[VERIFY: identify internal author]` / `[VERIFY: assign real author name]` items can be resolved from anything currently live on the site; a named-author program (even 1–2 real engineers with a bio page, reused across firmware + cooling + documentation content) would be a new initiative, not a page fix.

**Priority: P1 (structural, blocks E-E-A-T on every brief). Effort: Medium** (needs a real person + sign-off from BiXBiT, not a content trick) — flag to whoever owns content operations; this agent cannot invent a byline per CLAUDE.md rule #2/§4.

---

## 4. PDU page vs. `content/briefs/pdu-pillar.md` — completeness assessment

`/en/products/pdu` is a real, single consolidated page (not the `/en/pdu` pillar+8-spokes structure the brief specifies). Content found via WebFetch:

**What the live page already covers (brief's `[VERIFY]` blockers now resolved by on-page copy):**
- Spec table: 3-phase + single-phase modes, input 380–480 VAC, max input current 450A (20-outlet config), output 380–480 VAC (3-phase) / 220–277 VAC (single-phase), outlet counts 6/12/16/20 (custom available), dimensions 1850×175×300mm, certifications CE/UL/Intertek.
- H3-level feature sections: SUM Design Concept, Active Energy Metering, Smart Alarming System, Intelligent Power Management, Flexible Configuration, Broad Application.
- This resolves several brief `[VERIFY]` items directly: form factor, outlet count, voltage/amperage range, certifications. **These no longer need `[VERIFY]` tags if reused — they are already published, presumably-vetted copy**, not agent-invented data. (Still flag "automatic circuit breaker" / "automatic hydraulic circuit breaker" H3 headings for a human to confirm meaning — unusual phrasing, possibly a translation artifact from the RU original.)

**What's still genuinely missing vs. the brief (real content gaps, not just [VERIFY] noise):**
- **No FAQ section on the page at all**, despite the brief specifying a 5-question FAQ block and despite a site-wide `/en/faq` page existing with unrelated content. No `FAQPage` schema either (already flagged by technical-seo).
- **No comparison content** — the brief's "Managed PDU vs. Direct Wiring vs. Unmanaged PDU" H2 does not exist in any form. This is the section most likely to help conversion (educates first-time PDU buyers) and is pure content-gap, not a spec-sourcing problem.
- **No AMS-integration deep-dive** — the brief wants a dedicated explanation of PDU telemetry flowing into the AMS dashboard (use cases: fault alerts, per-client billing, PUE inputs); the live page does not describe this beyond a general capability mention.
- **No sizing guidance, no persona-based sections** (farm operator vs. hosting provider vs. institutional vs. data-center), no spoke pages for per-outlet-metering/remote-switching/overload-protection/sizing/data-center as separate deep-dive URLs.
- Confirmed by technical-seo: zero sitemap presence and no `Product`/`SoftwareApplication` schema — this page is both content-incomplete and technically undiscoverable.

**Verdict:** the PDU page is a solid, spec-rich single-page product page — better than the brief's `[VERIFY]`-heavy draft assumed was possible — but it's missing the comparison/FAQ/persona content that would make it a true pillar, and it has zero spoke support. Given P4 priority ranking in CLAUDE.md, recommend **not** producing all 8 planned spokes; instead do a **single incremental content pass** adding FAQ + comparison table + AMS-integration paragraph to the existing page (fast, uses already-published specs, closes the highest-value gaps) before considering spoke expansion.

**Priority: P2 (in line with PDU's P4 overall priority, but the FAQ+schema fix is cheap and worth doing opportunistically). Effort: Low** for FAQ/comparison content add; **Medium** if full spoke expansion is pursued later.

---

## 5. Prioritized findings (P0–P3)

| # | Finding | URL(s) | Priority | Impact | Effort |
|---|---|---|---|---|---|
| 1 | Two P0 firmware briefs assert "no dev fee" as the core differentiator; live pages confirm a real 2.8%/2% dev fee — briefs would ship a false, fact-checkable claim | `content/briefs/antminer-firmware-pillar.md`, `content/briefs/whatsminer-firmware-pillar.md` (vs. live `/en/firmwares/antminer`, `/en/firmwares/whatsminer-series-m6x`) | **P0** | High (reputational risk with technical B2B audience) | Low (edit two brief files, reframe differentiator) |
| 2 | June briefs' planned URL architecture (`/en/antminer-firmware`, `/en/pdu`, `/en/immersion-cooling-mining`, etc.) does not match the real site IA (`/en/firmwares/*`, `/en/products/pdu`, `/en/asics-cooling/*`) — blocks all future spoke production and makes `content/internal-linking.md` unusable as-is | all 5 pillar briefs; `content/internal-linking.md` | **P0** | High (structural blocker) | Low to re-scope; Medium-High to rebuild linking matrix + rewrite briefs |
| 3 | AMS competitor-comparison briefs (vs-Braiins/vs-LuxOS/vs-Minerstat) are fully written and unused — lowest-effort, highest-differentiation content gap on the site | `content/briefs/ams-vs-braiins-manager.md`, `ams-vs-luxor-commander.md`, `ams-vs-minerstat.md` — zero live equivalents | **P1** | High (AMS's strongest claim — Whatsminer support Braiins lacks — is uncaptured) | Low (briefs already exist, just need writing + publishing) |
| 4 | Documentation hub has a real nested content tier (error-code sub-pages, PSU/overclocking guides) entirely absent from any sitemap — bigger orphaned-content problem than the 5-URL sitemap suggested | `/en/documentation/error-codes-for-whatsminer-asic/*` and siblings | **P1** | Medium-High (real content, zero discoverability) | Low-Medium (crawl + sitemap fix, hand to technical-seo) |
| 5 | Zero named-author E-E-A-T anywhere sitewide (blog, documentation, firmware pages, `/en/about`) despite real company history/timeline existing on `/en/about` that could support it | sitewide; `/en/about` | **P1** | Medium-High (structural E-E-A-T ceiling) | Medium (needs a real person/bio from BiXBiT, not content-only fix) |
| 6 | Blog (~400 URLs) is majority general crypto-news/finance/legislation content; firmware (P1 priority) is under-represented in recent cadence vs. company-news/conference posts | `/en/blog`, `sitemap-blog.xml` | **P2** | Medium (diffuses topical authority from stated priorities) | Medium (editorial calendar policy, not a one-off fix) |
| 7 | Whatsminer firmware brief's spoke plan (per-feature URLs) doesn't match the live per-series-group IA (`-m6x/-m5x/-m3x/-m2x`), which already bundles autotuning/undervolting/install/FAQ into denser pages | `/en/firmwares/whatsminer-series-m6x` (+3 siblings) vs. `whatsminer-firmware-pillar.md` | **P2** | Medium (brief needs restructuring, not blind execution) | Low (revise brief's IA assumption) |
| 8 | `/en/products/pdu` missing FAQ, FAQPage schema, comparison content, AMS-integration deep-dive — brief's spec-table gaps are already resolved by on-page copy, but these narrative sections are real gaps | `/en/products/pdu` | **P2** | Medium (P4-priority cluster, but cheap high-value add) | Low |
| 9 | Immersion-cooling brief's IA (single `/en/immersion-cooling-mining` pillar with 9 spokes) doesn't match live IA (`/en/asics-cooling` split into hydro/immersion sub-hubs) — brief needs restructuring; live pages already contain real PUE/case-study data resolving most `[VERIFY]` blockers | `content/briefs/immersion-cooling-mining-pillar.md` vs. `/en/asics-cooling/*` | **P2** | Medium | Low (revise brief using already-published specs as source) |
| 10 | 7 legacy Antminer model pages consolidated/noindexed since June — moves away from, not toward, the brief's plan for more granular model-specific spoke content (already flagged by technical-seo as `[VERIFY]` re: intent) | `/en/firmwares/asic-*` (7 URLs) | **P3** (content-strategy echo of a technical-seo P1 item) | Low-Medium | Low ([VERIFY] intent with dev/content owner before deciding whether to rebuild model-spoke content here or elsewhere) |

---

## Data Gaps (honest accounting)

- **DataForSEO / GSC / GA4:** not connected this session. No volume, ranking, click, or impression data used anywhere in this report — all findings are structural/content-based only, per task instructions.
- **Full blog crawl:** only the blog index, one post, and the sitemap slug sample were fetched. The topic-mix verdict in §1a is directional (sample-based), not a full 400-URL census — a proper content audit/pruning pass would need to sample far more broadly before any deletion/consolidation decisions.
- **Full documentation tree:** only the top-level hub and one child article were fetched; the deeper nested tier (error-code sub-pages, PSU guides, overclocking docs) was inferred from in-page links, not independently fetched/verified for content quality.
- **`/en/ams/connect`, `/en/about` full content, `/en/contacts`, `/en/sustainability`:** not re-fetched for content depth this pass beyond what's in site-structure.md (status-only) and the one `/en/about` WebFetch done here for E-E-A-T purposes.
- **Competitor content (Braiins/Vnish/LuxOS/ePIC) direct comparison:** not re-verified this pass; existing competitor-gap reports (`content/competitor-gap-epic-*-2026-06-19.md`) are 3 months old and not re-confirmed here.
- **Technical firmware specs quoted from live pages** (dev fee %, PDU voltage/amperage, cooling PUE/case-study numbers) are reported as **observed on already-published BiXBiT pages**, not verified against an internal source-of-truth or invented by this agent — per CLAUDE.md rule #2, treat them as "what the site currently says," and re-confirm with the product/content owner before reusing in new copy, since commercial terms (like dev fee %) can change without notice.

---

## [VERIFY] Items surfaced for human review

- `[VERIFY]` Reconcile the "no dev fee" positioning in `antminer-firmware-pillar.md` / `whatsminer-firmware-pillar.md` against the confirmed live 2.8%/2% dev fee — this is not a new unknown, it is a **resolved contradiction** that needs a brief rewrite, not a data lookup.
- `[VERIFY]` Whether BiXBiT wants to formally adopt a named-author/engineer-byline program for E-E-A-T — currently no named individual exists in any content sampled sitewide.
- `[VERIFY]` "Automatic hydraulic circuit breaker" phrasing on `/en/products/pdu` — confirm this is intended terminology and not a translation artifact.
- `[VERIFY]` Intent behind the 7 noindexed legacy Antminer pages (already flagged by technical-seo) — affects whether content-seo should plan new model-specific spoke content or consider that ground permanently ceded to the consolidated hub.
- `[VERIFY]` Whether the blog's editorial calendar should adopt a topic-mix quota favoring FIRMWARE/IMMERSIONCOOLING/HEATUTILIZATION tags over CRYPTOCURRENCY/FINANCE/LEGISLATION/RATINGS content, given CLAUDE.md's stated priority order.
