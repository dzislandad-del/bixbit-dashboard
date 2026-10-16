# Topic Cluster: Mining Fleet Monitoring / ASIC Fleet Management
**Site:** https://bixbit.io/en
**Product:** BiXBiT AMS (Advanced Monitoring System)
**Created:** 2026-06-19
**Status:** Planned — no supporting editorial content exists yet. Mention rate in Claude/ChatGPT = 0%.

---

## Architecture v2 (2026-09-25): authoritative

> This section **replaces** the Hub/Spoke lists and the production order below. Spokes are no longer separate URLs: they become H2 sections on existing live pages. A new URL is created only for a standalone search intent. Rationale and the full table for all clusters: `reports/content-architecture-2026-09-25.md`. Links: `content/internal-linking.md` → «Architecture v2 — Linking Matrix». The old sections are kept below as **reference material for writers** (keywords, outlines, FAQs); their URLs no longer apply.

| URL | Type | Page priority | Sections from briefs (section priority) | What gets added |
|---|---|---|---|---|
| `/en/ams` | existing | **P0** | `mining-fleet-monitoring-pillar` → Main page content (pillar) (P0)<br>`antminer-monitoring-software` → H2 Antminer monitoring and dashboard (P1)<br>`mining-fleet-dashboard` → H2 Antminer monitoring and dashboard (dashboard part) (P2)<br>`whatsminer-monitoring-software` → H2 Whatsminer monitoring (mixed fleet) (P1)<br>`mining-farm-alerts-automation` → H2 Alerts and automation (P2)<br>`mining-farm-power-monitoring` → H2 Per-unit power monitoring (P2)<br>`mining-hosting-monitoring` → H2 Multi-client for hosting providers (P2)<br>`asic-fleet-management` → H2 Fleet management at scale (P2) | H2 sections: Antminer + Whatsminer in one dashboard (a mixed fleet); Antminer monitoring and dashboard; Whatsminer monitoring; alerts and automation (remote reboot [VERIFY]); per-unit power monitoring [VERIFY]; multi-client for hosting providers [VERIFY]; fleet management at scale; the firmware link; SoftwareApplication schema + the existing FAQ. Secondary keyword: mining software (260) |
| `/en/ams/comparison` | **new** | **P1** | `mining-farm-monitoring-software` → H2 How to choose monitoring software (P1)<br>`ams-vs-minerstat` → H2 AMS vs Minerstat (P1)<br>`ams-vs-braiins-manager` → H2 AMS vs Braiins Manager (P2)<br>`ams-vs-luxor-commander` → H2 AMS vs Luxor Commander (P2) | A new page: how to choose monitoring software (criteria); a comparison table with every competitor figure [VERIFY]; an 'alternatives' section (minerstat alternative 10, minerstat vs 10). Standalone intent: choosing and comparing vendors, GEO best-of-list queries |

**Production order:** `/en/ams` (P0) → `/en/ams/comparison` (P1)

---
## DataForSEO Status

**Updated 2026-09-25.**
- **Sources:** volumes from DataForSEO Google Ads search_volume, KD from DataForSEO Labs, BiXBiT positions from Labs ranked_keywords (United States / en). `n/d` = fewer than ~10/mo. Before/after table: `reports/cluster-repriorization-2026-09-25.md`.
- **Demand is minimal.** Of 26 seed keywords, 4 have measurable volume (10/mo each); the rest are n/d.
- **Real demand sits in adjacent queries:**
  - `asic monitor`: 70/mo, KD 0, **BiXBiT #7** (`/en/ams`)
  - `mining software`: 260/mo, CPC $39.51, KD 30. Broad, but commercial.
  - `antminer dashboard`: 30/mo, KD 12
  - `minerstat alternative`: 10, KD 24
- **Strategy:** the pillar `/en/ams` is P0 (a quick win from #7 into the top 3). Most spokes drop to P1/P2. The cluster's value is in GEO: AI answers about monitoring software (see `reports/sub/competitor-gap-*-geo-2026-09-25.md`), not organic volume.
- **The status line above is out of date:** BiXBiT does rank for `asic monitor`, and the real URL is `/en/ams`, not `/en/monitoring`.

---

## Strategic Rationale

BiXBiT AMS exists as a product page (`/en/monitoring`) with zero editorial support. Competitors — Braiins Manager, Luxor Commander, Minerstat — dominate SERP and AI citations for "ASIC fleet monitoring" and "mining farm management software." BiXBiT AMS's primary differentiator is **multi-vendor support**: it monitors both Antminer and Whatsminer from a single dashboard, integrated with BiXBiT firmware. Braiins Manager does not support Whatsminer; this is the clearest content gap to exploit.

The cluster creates topical authority around AMS, drives organic traffic from operators comparing platforms, and feeds the AI citation surface (GEO) where BiXBiT is currently invisible.

---

## Competitive Content Gaps

| Gap | Competitor Weakness | BiXBiT Angle |
|---|---|---|
| Whatsminer monitoring | Braiins Manager does not support Whatsminer [VERIFY: confirm current Braiins Manager model coverage] | AMS supports Antminer + Whatsminer in one dashboard |
| Mixed-fleet monitoring | No single-vendor solution covers both platforms well | BiXBiT firmware + AMS = unified stack for mixed fleets |
| Mid-scale enterprise (100–5,000 ASIC) | Most content targets either hobbyist or 100k+ hyperscale | AMS designed for this underserved segment |
| Hosting/colocation operator use case | Poorly covered across all competitors | Dedicated spoke page for hosting operators |
| Firmware + monitoring integration | Separate products at Braiins/Luxor/Minerstat | BiXBiT unique: same vendor for firmware + monitoring |
| Alert automation depth | Generic coverage | Dedicated spoke: alerting logic, escalation, remote reboot |

---

## Seed Keywords (volumes: DataForSEO Google Ads, US/en, 2026-09-25)

| Keyword | Est. Intent | Vol (US, 2026-09) | Notes |
|---|---|---|---|
| mining fleet monitoring | Commercial | n/d (<10) | Primary seed |
| ASIC fleet management software | Commercial | n/d (<10) | High commercial intent |
| bitcoin miner monitoring software | Commercial | n/d (<10) | Broad, competitive |
| mining farm management software | Commercial | 10 | Core cluster keyword |
| ASIC monitoring dashboard | Commercial | n/d (<10) | Feature-level intent |
| mining farm remote monitoring | Informational/Commercial | n/d (<10) | Use-case intent |
| antminer monitoring software | Commercial | 10 | Spoke keyword |
| whatsminer monitoring software | Commercial | n/d (<10) | Spoke keyword — Braiins gap |
| mining fleet management platform | Commercial | n/d (<10) | Platform comparison intent |
| bitcoin mining management system | Commercial | n/d (<10) | Enterprise framing |
| mining hardware monitoring | Informational | n/d (<10) | Top-of-funnel |
| ASIC farm dashboard | Informational/Commercial | n/d (<10) | Feature-level |
| mining farm alerts | Informational | n/d (<10) | Spoke keyword |
| remote ASIC reboot | Informational/Commercial | n/d (<10) | Feature-specific |
| mining farm uptime monitoring | Commercial | n/d (<10) | SLA-focused intent |
| bitcoin mining fleet management | Commercial | n/d (<10) | Enterprise intent |
| ASIC fleet monitoring software | Commercial | n/d (<10) | Primary target |
| mining pool monitoring | Informational | 10 | Adjacent — different intent |
| Braiins Manager alternative | Commercial | n/d (<10) | High-value comparison intent |
| Luxor Commander alternative | Commercial | n/d (<10) | High-value comparison intent |
| Minerstat alternative | Commercial | 10, KD 24 | High-value comparison intent |
| mining monitoring software | Commercial | 10, KD 38 | Pillar keyword |
| ASIC fleet control | Commercial | n/d (<10) | Secondary |
| mining farm power monitoring | Informational/Commercial | n/d (<10) | Spoke: power telemetry |
| per unit ASIC telemetry | Informational | n/d (<10) | Long-tail, specific |
| bitcoin miner hashrate monitoring | Informational | n/d (<10) | Feature-level |

---

## Hub-and-Spoke Architecture *(superseded by Architecture v2; reference material)*

### Hub (Pillar Page)

| Attribute | Value |
|---|---|
| Slug | `/en/ams` (existing product page) or `/en/monitoring` |
| Title | AMS: ASIC Fleet Monitoring Software for Mining Operations |
| Primary keyword | "mining fleet monitoring software" |
| Intent | Commercial / navigational |
| Schema | SoftwareApplication + FAQPage |
| Priority | **P0** (was P0). `asic monitor` 70/mo, KD 0, BiXBiT #7; test `mining software` 260/mo (CPC $39.51) as a secondary keyword |
| Word count | 2,000–2,500 |

### Spoke Pages

| # | Slug | Title (working) | Primary Keyword | Intent | Priority | Competitor Gap |
|---|---|---|---|---|---|---|
| S1 | `/en/ams/vs-braiins-manager` | AMS vs Braiins Manager: ASIC Fleet Monitoring Compared | "AMS vs Braiins Manager" / "Braiins Manager alternative" | Commercial | P2 (was P0) | Braiins supports Antminer only |
| S2 | `/en/ams/vs-luxor-commander` | AMS vs Luxor Commander: Mining Fleet Management Compared | "Luxor Commander alternative" / "LuxOS monitoring" | Commercial | P2 (was P1) | Luxor = LuxOS-only ecosystem |
| S3 | `/en/ams/vs-minerstat` | AMS vs Minerstat: Which ASIC Monitoring Platform is Right for You? | "Minerstat alternative" / "Minerstat vs" | Commercial | P1 | Minerstat = no firmware integration |
| S4 | `/en/ams/mining-farm-monitoring-software` | Mining Farm Monitoring Software: How to Choose (2025 Guide) | "mining farm monitoring software" / "bitcoin miner monitoring software" | Informational | P1 (was P0) | Generic educational — all competitors thin here |
| S5 | `/en/ams/asic-fleet-management` | ASIC Fleet Management: A Technical Guide for Farm Operators | "ASIC fleet management" / "ASIC fleet management software" | Informational | P2 (was P0) | Deep technical content missing from all competitors |
| S6 | `/en/ams/antminer-monitoring-software` | Antminer Monitoring Software: AMS Integration Guide | "Antminer monitoring software" / "Antminer dashboard" | Commercial | P1 (was P0) | Ties to existing Antminer firmware cluster |
| S7 | `/en/ams/whatsminer-monitoring-software` | Whatsminer Monitoring Software: What to Use When Braiins Won't | "Whatsminer monitoring software" / "Whatsminer management software" | Commercial | P1 (was P0) | Braiins Manager does not support Whatsminer — direct gap |
| S8 | `/en/ams/mining-farm-alerts-automation` | Mining Farm Alerts and Automation: Reducing Downtime at Scale | "mining farm alerts" / "ASIC alert automation" / "remote ASIC reboot" | Informational/Commercial | P2 (was P1) | Feature depth missing from Minerstat/Braiins content |
| S9 | `/en/ams/mining-hosting-monitoring` | ASIC Monitoring for Mining Hosting Operators: Multi-Client Fleet Management | "mining hosting monitoring" / "colocation ASIC management" | Commercial | P2 (was P1) | No competitor targets hosting operators specifically |
| S10 | `/en/ams/mining-farm-power-monitoring` | Mining Farm Power Monitoring: Per-Unit Consumption Tracking | "mining farm power monitoring" / "ASIC power consumption monitoring" | Informational/Commercial | P2 | Underserved across all competitors |
| S11 | `/en/ams/mining-fleet-dashboard` | ASIC Fleet Dashboard: What Enterprise Mining Operators Need | "ASIC monitoring dashboard" / "mining fleet dashboard" | Informational | P2 | Feature-education content gap |

---

## Intent Classification Summary

| Intent | Pages | Notes |
|---|---|---|
| Commercial | Hub, S1, S2, S3, S6, S7, S9 | Comparison / evaluation stage — highest conversion proximity |
| Informational | S4, S5, S8, S10, S11 | Top-of-funnel — build topical authority, feed AI citations |
| Transactional | Hub (CTA section) | Demo request / contact — handled within pillar, not separate page |

---

## Cross-Cluster Links (AMS ↔ Firmware Clusters) *(superseded by `content/internal-linking.md` → Architecture v2)*

| AMS Page | Links To | Rationale |
|---|---|---|
| Hub `/en/ams` | `/en/antminer-firmware` | Firmware + AMS = integrated product stack |
| Hub `/en/ams` | `/en/whatsminer-firmware` | Mixed-fleet unified management |
| S6 `/en/ams/antminer-monitoring-software` | `/en/antminer-firmware` (pillar) | Direct product integration |
| S6 `/en/ams/antminer-monitoring-software` | `/en/antminer-firmware/autotuning` | AMS surfaces autotuning results |
| S7 `/en/ams/whatsminer-monitoring-software` | `/en/whatsminer-firmware` (pillar) | Direct product integration |
| S7 `/en/ams/whatsminer-monitoring-software` | `/en/whatsminer-firmware/autotuning` | AMS surfaces autotuning results |
| S1 `/en/ams/vs-braiins-manager` | `/en/antminer-firmware/comparison` | Comparison context: firmware AND monitoring |
| S8 `/en/ams/mining-farm-alerts-automation` | `/en/antminer-firmware/overclocking` | Alert use case: overclocked units |
| S8 `/en/ams/mining-farm-alerts-automation` | `/en/whatsminer-firmware/overclocking` | Alert use case: overclocked Whatsminer |
| S10 `/en/ams/mining-farm-power-monitoring` | `/en/antminer-firmware/undervolting` | Power monitoring + undervolting workflow |
| S10 `/en/ams/mining-farm-power-monitoring` | `/en/whatsminer-firmware/undervolting` | Power monitoring + undervolting workflow |

---

## Schema Map

| Page Type | Recommended Schema |
|---|---|
| Hub (AMS product page) | `SoftwareApplication` + `FAQPage` |
| Comparison pages (S1, S2, S3) | `FAQPage` + `Article` (no `Product` — avoid false Product schema on comparison) |
| Educational guides (S4, S5, S8, S10, S11) | `TechArticle` + `FAQPage` |
| Integration guides (S6, S7) | `TechArticle` + `HowTo` + `FAQPage` |
| Hosting use case (S9) | `TechArticle` + `FAQPage` |

---

## Production Priority *(superseded by Architecture v2; reference material)*

*Recalculated 2026-09-25 from DataForSEO US data. The previous waves are kept in git history.*

| Page | Was | Now | Vol (US, 2026-09) |
|---|---|---|---|
| Hub `/en/ams` | P0 | **P0** | `asic monitor` 70 (#7), `mining software` 260, `mining monitoring software` 10 |
| S6 Antminer monitoring (+ S11 dashboard as a section) | P0 | **P1** | 50 (`antminer dashboard` 30, KD 12) |
| S4 mining farm monitoring software | P0 | **P1** | 20 |
| S7 Whatsminer monitoring | P0 | **P1** | n/d, but it's the differentiator (Antminer + Whatsminer) and matters for GEO |
| S3 AMS vs Minerstat | P1 | **P1** | 20 (`minerstat alternative` 10, KD 24; `minerstat vs` 10) |
| S1 AMS vs Braiins Manager | P0 | **P2** | n/d |
| S5 ASIC fleet management | P0 | **P2** | n/d |
| S2 AMS vs Luxor Commander | P1 | **P2** | n/d |
| S8 Alerts & automation | P1 | **P2** | n/d |
| S9 Hosting monitoring | P1 | **P2** | n/d; a sales/BD asset rather than SEO |
| S10 Power monitoring | P2 | **P2** | n/d |
| S11 Fleet dashboard | P2 | **P2** | n/d; section of S6 |

| Wave | Pages |
|---|---|
| Wave 1 (immediate) | Hub `/en/ams` (quick win #7 → top 3) |
| Wave 2 (4–6 weeks) | S6 (+S11), S4, S7, S3 |
| Wave 3 (8–12 weeks) | S1, S5, S2, S8, S9, S10, only if GSC shows impressions |

---

## [VERIFY] Blockers

Before publishing any page in this cluster, the following must be verified with product/engineering:

1. `[VERIFY: AMS — complete list of supported ASIC models (Antminer series: S19, S21, S19 Pro, S19j, S21 XP etc.; Whatsminer series: M30S, M50, M56, M60, M63 etc.)]`
2. `[VERIFY: AMS — maximum fleet size supported (units per account, units per dashboard view)]`
3. `[VERIFY: AMS — real-time polling interval (seconds/minutes per unit refresh)]`
4. `[VERIFY: AMS — alert types available (hashrate drop, temperature threshold, offline, rejected shares, power spike)]`
5. `[VERIFY: AMS — remote reboot capability: yes/no, per-unit or batch]`
6. `[VERIFY: AMS — per-unit power consumption telemetry: yes/no, granularity]`
7. `[VERIFY: AMS — firmware update push via dashboard: yes/no]`
8. `[VERIFY: AMS — multi-client / sub-account support for hosting operators: yes/no]`
9. `[VERIFY: AMS — pricing model: free tier, per-unit fee, flat SaaS, bundled with firmware]`
10. `[VERIFY: AMS — API/webhook support for third-party integrations]`
11. `[VERIFY: Braiins Manager — confirm it does NOT support Whatsminer as of 2025 (critical competitive claim)]`
12. `[VERIFY: Luxor Commander — current supported ASIC models and fleet size limits from luxor.tech]`
13. `[VERIFY: Minerstat ASIC Hub — pricing tiers and supported hardware from minerstat.com]`
