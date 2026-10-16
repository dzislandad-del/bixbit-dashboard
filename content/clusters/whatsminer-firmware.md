# Topic Cluster: Whatsminer Firmware
**Site:** https://bixbit.io/en
**Cluster owner:** Content & SEO
**Last updated:** 2026-09-25 (volumes and priorities recalculated from DataForSEO)
**Data note:** Volumes come from DataForSEO Google Ads search_volume, KD from DataForSEO Labs (United States / en), as of 2026-09-25. `n/d` means Google Ads returned no volume (fewer than ~10 searches/mo). The recalculation and the before/after table are in `reports/cluster-repriorization-2026-09-25.md`.

---

## Architecture v2 (2026-09-25): authoritative

> This section **replaces** the Hub/Spoke lists and the production order below. Spokes are no longer separate URLs: they become H2 sections on existing live pages. A new URL is created only for a standalone search intent. Rationale and the full table for all clusters: `reports/content-architecture-2026-09-25.md`. Links: `content/internal-linking.md` → «Architecture v2 — Linking Matrix». The old sections are kept below as **reference material for writers** (keywords, outlines, FAQs); their URLs no longer apply.

| URL | Type | Page priority | Sections from briefs (section priority) | What gets added |
|---|---|---|---|---|
| `/en/firmwares/whatsminer-all-series` | existing | **P0** | `whatsminer-firmware-pillar` → Main page content (hub) (P0)<br>`whatsminer-custom-firmware` → H2 Why third-party Whatsminer firmware (P2)<br>`whatsminer-overclocking-firmware` → H2 Tuning modes → overclocking (P2)<br>`whatsminer-undervolting` → H2 Tuning modes → undervolting (P2)<br>`whatsminer-autotuning` → H2 Tuning modes → autotuning (P2) | H2 sections: why third-party Whatsminer firmware (the category explainer); a series overview linking to m2x/m3x/m5x/m6x; tuning modes; FAQ; SoftwareApplication schema. Rule: don't remove 'whatsminer firmware' from -m3x until the hub is in the top 5 [VERIFY that the page is indexed; lastmod 2024-11] |
| `/en/firmwares` | existing | **P0** | — (no cluster briefs) | A canonical opening passage (Antminer + Whatsminer + AMS, one sentence reused in schema and llms.txt); a summary block on the transparent dev fee [VERIFY] linking to /en/firmwares/dev-fee; a supported-models table [VERIFY]; a real FAQPage in place of the empty mainEntity; links to comparison and dev-fee |
| `/en/firmwares/dev-fee` | **new** | **P0** | `whatsminer-firmware-security` → Whatsminer section of the dev-fee page (P1) | A new page: what a dev fee is and how it's charged; BiXBiT's fee by series [VERIFY: 2.8% / 2% M2x]; TCO calculation (efficiency gain minus fee), no 'lowest fee' claim; security (no backdoor, how to check) [VERIFY]; FAQ. Standalone intent: pricing and trust question, GEO 'lowest dev fee' (ePIC 4/5, BiXBiT 0/5) |
| `/en/firmwares/comparison` | **new** | **P0** | `whatsminer-firmware-comparison` → Whatsminer column/section of the comparison page (P1) | A new page: an HTML comparison table (fee, models, autotuning, Whatsminer support, monitoring) with every competitor figure [VERIFY]; decision framework; FAQ. Standalone intent: commercial comparison and GEO comparison prompts, plus competitor brand demand (braiins os 210, vnish firmware 140) |
| `/en/firmwares/whatsminer-series-m3x` | existing | **P1** | `whatsminer-m30s-firmware` → Page content (M3x series) (P1) | H2 sections: M30S/M30S+/M30S++ modes table [VERIFY]; efficiency and tuning for the M3x; FAQ. Keep the current ranking and add a link to the hub |
| `/en/firmwares/whatsminer-series-m5x` | existing | **P1** | `whatsminer-m50-firmware` → Page content (M5x); the M60 part goes to /en/firmwares/whatsminer-series-m6x (P1) | H2 sections: M50/M50S/M53 modes [VERIFY]; immersion/hydro notes; FAQ |
| `/en/firmwares/whatsminer-series-m6x` | existing | **P1** | `whatsminer-m50-firmware` → M60 part (P1) | H2 sections: M60/M60S/M63 modes [VERIFY]; immersion and hydro profiles; FAQ |
| `/en/documentation/user-guide-for-whatsminer-asic` | existing | **P2** | `whatsminer-firmware-install` → H2 Install custom firmware (P2)<br>`whatsminer-firmware-update` → H2 Update and rollback (P2) | Sections: install custom firmware, update, rollback; a link to the hub |
| `/en/firmwares/whatsminer-series-m2x` | existing | **P2** | — (no cluster briefs) | Dev fee fact (2% on M2x [VERIFY]) and a link to the hub. Nothing else |

**Production order:** `/en/firmwares/whatsminer-all-series` (P0) → `/en/firmwares` (P0) → `/en/firmwares/dev-fee` (P0) → `/en/firmwares/comparison` (P0) → `/en/firmwares/whatsminer-series-m3x` (P1) → `/en/firmwares/whatsminer-series-m5x` (P1) → `/en/firmwares/whatsminer-series-m6x` (P1) → `/en/documentation/user-guide-for-whatsminer-asic` (P2) → `/en/firmwares/whatsminer-series-m2x` (P2)

---
## Data Availability

| Source | Status | Notes |
|---|---|---|
| DataForSEO Google Ads search_volume | OK (2026-09-25) | `data/dfs-search-volume-clusters-us-2026-09-25.json` |
| DataForSEO Labs bulk_keyword_difficulty | OK (2026-09-25) | `data/dfs-keyword-difficulty-clusters-us-2026-09-25.json` |
| DataForSEO Labs ranked_keywords (bixbit.io) | OK (2026-09-25) | `data/dfs-ranked-keywords-bixbit.io-2026-09-25.json` |
| GSC | Connector works (2026-09-25), not pulled | Next step: GSC impressions for the n/d queries |

**Key finding:** `whatsminer firmware` is 20/mo, CPC $32.03, KD 4, and BiXBiT already ranks **#3** with `/en/firmwares/whatsminer-series-m3x`. `whatsminer tool` (50/mo, KD 12) is at #16 with `/en/firmwares`. The rest are 10/mo or n/d. The segment is confirmed as uncontested: competitors have no Whatsminer rankings (competitor-gap 2026-09-25), and LLMs name BiXBiT for Whatsminer on 4 of 5 engines. The strategy therefore changes from capture to **defend and expand**. **Real URLs:** series pages already exist (`/en/firmwares/whatsminer-series-m2x/m3x/m5x/m6x`, `/whatsminer-all-series`). Optimize those; don't create new `/en/whatsminer-firmware/*` pages [VERIFY with the team].

---

## Cluster Overview

**Seed:** whatsminer firmware
**Pillar URL:** /en/whatsminer-firmware
**Cluster goal:** Own the "Whatsminer firmware" topic in US/EN Google SERPs. Establish BiXBiT as the authoritative third-party firmware provider for Whatsminer (MicroBT) operators — the alternative to stock MicroBT firmware, with no comparable third-party competitor currently dominating this SERP segment.

**Business rationale:** The Whatsminer M30S, M50, M60, and M60S series represent a large and growing share of industrial mining fleets. Operators running mixed Antminer/Whatsminer fleets need firmware solutions for both platforms. Unlike the Antminer segment where Braiins OS+, Vnish, LuxOS, and ePIC have substantial content, the Whatsminer third-party firmware SERP is comparatively underserved — a first-mover content opportunity. This cluster pairs with the existing Antminer firmware cluster to cover both dominant ASIC platforms.

**Platform distinction from Antminer cluster:** Whatsminer runs MicroBT hardware with a different chipset architecture, different management interface (WhatsMiner API / whatsminer web dashboard), different boot and flash procedure, and different stock firmware stack. Content must be platform-specific — do not repurpose or paraphrase Antminer content.

---

## Hub Page *(superseded by Architecture v2; reference material)*

| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware |
| H1 | Whatsminer Firmware: Custom Firmware for MicroBT Whatsminer ASICs |
| Intent | Commercial investigation |
| Priority | **P0** (was P0) — Keep, now as defense. whatsminer firmware 20/mo, CPC $32.03, KD 4; BiXBiT is #3 (/en/firmwares/whatsminer-series-m3x). There is no hub-level Whatsminer page, and competitors have no Whatsminer rankings. Build the hub on an existing URL (/en/firmwares/whatsminer-all-series) [VERIFY with the team]. |
| Schema | SoftwareApplication + FAQPage |
| Vol (US, 2026-09) | 40/mo (whatsminer firmware 20; whatsminer custom firmware 10; MicroBT firmware 10); BiXBiT: whatsminer firmware #3 |
| KD | whatsminer firmware 4; whatsminer custom firmware 50 |
| Target keywords | whatsminer firmware, whatsminer custom firmware, best whatsminer firmware, third-party whatsminer firmware, MicroBT firmware, whatsminer firmware comparison |

---

## Spoke Pages *(superseded by Architecture v2; reference material)*

### Spoke 1: Whatsminer Firmware Update
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/update |
| H1 | How to Update Whatsminer Firmware: Step-by-Step Guide |
| Intent | Informational (how-to) |
| Priority | **P2** (was P1) — Demoted. 10/mo, KD 42. Merge into the install page. |
| Schema | HowTo + FAQPage |
| Vol (US, 2026-09) | 10/mo (whatsminer firmware update 10) |
| Target keywords | whatsminer firmware update, how to update whatsminer firmware, whatsminer firmware upgrade, whatsminer firmware flash |
| Competitor gap | No third-party firmware vendor has a comprehensive update guide for Whatsminer. MicroBT's own documentation is terse and model-fragmented. This how-to is effectively uncontested. |

### Spoke 2: Whatsminer Custom Firmware
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/custom |
| H1 | Custom Firmware for Whatsminer: What It Is and Why Operators Switch |
| Intent | Informational (educational) |
| Priority | **P2** (was P1) — Demoted. 10/mo, KD 50. Fold into the pillar. |
| Schema | TechArticle + FAQPage |
| Vol (US, 2026-09) | 10/mo (whatsminer custom firmware 10) |
| Target keywords | whatsminer custom firmware, custom firmware whatsminer m30s, whatsminer third party firmware, MicroBT firmware mod, whatsminer firmware alternative |
| Competitor gap | No competitor publishes a neutral educational piece explaining the custom firmware category specifically for Whatsminer. All existing content is either stock MicroBT docs or Antminer-centric. |

### Spoke 3: Whatsminer M30S Firmware
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/whatsminer-m30s |
| H1 | Whatsminer M30S Firmware: Custom Tuning and Efficiency Options |
| Intent | Commercial investigation |
| Priority | **P1** (was P1) — Keep. whatsminer m30s firmware 10/mo. Optimize the existing /en/firmwares/whatsminer-series-m3x (already #3 for whatsminer firmware); don't create a new URL. |
| Schema | TechArticle + FAQPage |
| Vol (US, 2026-09) | 10/mo (whatsminer m30s firmware 10) |
| Target keywords | whatsminer m30s firmware, whatsminer m30s pro firmware, whatsminer m30s++ firmware, m30s custom firmware, m30s firmware update |
| Competitor gap | M30S is the most widely deployed Whatsminer generation. No third-party vendor has a dedicated M30S firmware page. SERP is currently occupied by MicroBT support docs and mining forums. |

### Spoke 4: Whatsminer M50/M60 Firmware
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/whatsminer-m50 |
| H1 | Whatsminer M50 and M60 Firmware: Next-Gen MicroBT Custom Tuning |
| Intent | Commercial investigation |
| Priority | **P1** (was P1) — Keep. whatsminer m50 firmware 10/mo. Use the existing /en/firmwares/whatsminer-series-m5x and -m6x. |
| Schema | TechArticle + FAQPage |
| Vol (US, 2026-09) | 10/mo (whatsminer m50 firmware 10) |
| Target keywords | whatsminer m50 firmware, whatsminer m60 firmware, whatsminer m50s firmware, microbt m60s firmware, whatsminer gen6 firmware |
| Competitor gap | M50/M60 series are current-gen. Competitor content is nearly absent on these models. Early ownership opportunity mirrors the Antminer S21 opportunity in the other cluster. |

### Spoke 5: Whatsminer Overclocking Firmware
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/overclocking |
| H1 | Whatsminer Overclocking: Boost Hashrate with Custom Firmware |
| Intent | Informational / commercial |
| Priority | **P2** (was P1) — Demoted. 10/mo. Merge into a tuning-modes page. |
| Schema | TechArticle + HowTo |
| Vol (US, 2026-09) | 10/mo (whatsminer overclock firmware 10) |
| Target keywords | whatsminer overclocking, whatsminer overclock firmware, how to overclock whatsminer, whatsminer hashrate boost, MicroBT overclocking |
| Competitor gap | No competitor (Braiins, Vnish, LuxOS, ePIC) publishes Whatsminer-specific overclocking content. This SERP is served by Reddit threads and YouTube. |

### Spoke 6: Whatsminer Autotuning
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/autotuning |
| H1 | Whatsminer Autotuning: Per-Chip Optimization for MicroBT Hardware |
| Intent | Informational |
| Priority | **P2** (was P2) — Keep P2. Volume n/d. |
| Schema | TechArticle + FAQPage |
| Vol (US, 2026-09) | n/d (<10/mo for every keyword) |
| Target keywords | whatsminer autotuning, whatsminer auto tuning firmware, microbt autotuning, whatsminer per chip tuning, whatsminer efficiency autotuning |
| Competitor gap | MicroBT's stock firmware has some autotuning capability, but no vendor publishes a technical explainer of how per-chip autotuning differs on the Whatsminer chipset vs Antminer. Zero competitor content on this. |

### Spoke 7: Whatsminer Undervolting
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/undervolting |
| H1 | Whatsminer Undervolting: Lower Power Draw Without Losing Hashrate |
| Intent | Informational / commercial |
| Priority | **P2** (was P2) — Keep P2. Volume n/d. |
| Schema | TechArticle + HowTo |
| Vol (US, 2026-09) | n/d (<10/mo for every keyword) |
| Target keywords | whatsminer undervolting, whatsminer undervolt firmware, underclock whatsminer m30s, whatsminer power reduction, microbt undervolting firmware |
| Competitor gap | No dedicated Whatsminer undervolting guide exists in the market from any vendor. Electricity cost reduction is a universal ICP pain point. |

### Spoke 8: Whatsminer Firmware Installation Guide
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/install |
| H1 | How to Install Custom Firmware on Whatsminer: Complete Installation Guide |
| Intent | Informational (how-to) |
| Priority | **P2** (was P1) — Demoted. Volume n/d. A combined install + update page; documentation already exists in /en/documentation. |
| Schema | HowTo + FAQPage |
| Vol (US, 2026-09) | n/d (<10/mo for every keyword) |
| Target keywords | whatsminer firmware install, how to install whatsminer firmware, whatsminer firmware flash guide, whatsminer firmware sd card, whatsminer firmware recovery |
| Competitor gap | MicroBT documentation is minimal and version-fragmented. No competitor offers a comprehensive multi-method installation guide for Whatsminer. Mirrors the Antminer install spoke — equally high-value. |

### Spoke 9: Whatsminer Firmware Security
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/security |
| H1 | Whatsminer Firmware Security: Dev Fees, Backdoors, and What to Audit |
| Intent | Informational (trust-building) |
| Priority | **P1** (was P2) — Promoted. Merge into the shared dev-fee + security page (see antminer-firmware-security). GEO priority. |
| Schema | TechArticle + FAQPage |
| Vol (US, 2026-09) | n/d (<10/mo for every keyword) |
| Target keywords | whatsminer firmware security, whatsminer firmware backdoor, microbt firmware dev fee, safe whatsminer firmware, whatsminer firmware audit |
| Competitor gap | Identical gap to the Antminer security spoke — no competitor covers this. Critical for institutional operators running Whatsminer fleets. |

### Spoke 10: Whatsminer Firmware Comparison
| Field | Value |
|---|---|
| URL | /en/whatsminer-firmware/comparison |
| H1 | Whatsminer Firmware Comparison: BiXBiT vs Stock MicroBT Firmware and Alternatives |
| Intent | Commercial investigation |
| Priority | **P1** (was P1) — Keep. Volume n/d, but it is the only segment with no competitors; LLMs name BiXBiT for Whatsminer on 4 of 5 engines. Reinforce with a comparison table. |
| Schema | TechArticle + FAQPage |
| Vol (US, 2026-09) | n/d (<10/mo for every keyword) |
| Target keywords | whatsminer firmware comparison, best whatsminer custom firmware, whatsminer firmware alternatives, microbt custom firmware comparison, whatsminer third party firmware comparison |
| Competitor gap | No comparison page exists for Whatsminer firmware alternatives. Unlike the Antminer segment where Braiins/Vnish/LuxOS compete, BiXBiT may be among the very few third-party options — making a comparison page both a decision-stage capture tool and a market-positioning piece. |

---

## Competitor Content Gap Summary

| Gap | Priority (2026-09-25) | Who's weak | Opportunity |
|---|---|---|---|
| Generic Whatsminer firmware update how-to | P2 (was P1): 10/mo, merge into install | All competitors absent | Uncontested SERP |
| Whatsminer M30S model-specific firmware page | P1: 10/mo, existing `-m3x` page | All competitors absent | Largest installed base model |
| Whatsminer M50/M60 current-gen firmware | P1: 10/mo, existing `-m5x`/`-m6x` pages | All competitors absent | Early SERP ownership |
| Whatsminer overclocking guide | P2 (was P1): 10/mo | All competitors absent | Performance-focused operators |
| Whatsminer firmware security / dev fee audit | P1: GEO (dev fee) | No vendor covers this | Highest trust-building opportunity |
| Whatsminer firmware comparison | P1: n/d, GEO | Market essentially uncontested | Decision-stage capture |
| Whatsminer undervolting standalone guide | P2: n/d | No vendor covers this | Electricity cost pain point |
| Per-chip autotuning on MicroBT architecture | P2: n/d | No vendor covers this | Technical E-E-A-T depth |
| Custom firmware educational explainer (Whatsminer) | P2 (was P1): 10/mo, KD 50, section of hub | All vendors Antminer-focused | Category creation for Whatsminer |
| Whatsminer firmware install (multi-method) | P2 (was P1): n/d | Only MicroBT terse docs exist | How-to |

---

## Cross-Cluster Links: Whatsminer ↔ Antminer Firmware *(superseded by `content/internal-linking.md` → Architecture v2)*

These are the semantically justified intersection points between the two firmware clusters:

| Whatsminer Page | Links To Antminer Page | Anchor Text | Rationale |
|---|---|---|---|
| /en/whatsminer-firmware (pillar) | /en/antminer-firmware | "Antminer firmware" | Mixed-fleet operators run both platforms; link in "Supported Platforms" section |
| /en/whatsminer-firmware/comparison | /en/antminer-firmware/comparison | "Antminer firmware comparison" | Operators evaluating both platforms; end-of-page "Also see" section |
| /en/whatsminer-firmware/security | /en/antminer-firmware/security | "Antminer firmware security guide" | Security methodology is platform-agnostic; link in "Also applies to" section |
| /en/whatsminer-firmware/autotuning | /en/antminer-firmware/autotuning | "Antminer per-chip autotuning" | Technical comparison of autotuning on two different ASIC architectures |
| /en/whatsminer-firmware/install | /en/antminer-firmware/install | "Antminer firmware installation" | Fleet operators installing firmware on both platforms |
| /en/whatsminer-firmware/undervolting | /en/antminer-firmware/undervolting | "Antminer undervolting guide" | Cross-platform efficiency operators |
| /en/antminer-firmware (pillar) | /en/whatsminer-firmware | "Whatsminer firmware" | Antminer pillar should reference Whatsminer support for mixed-fleet operators |
| /en/antminer-firmware/comparison | /en/whatsminer-firmware/comparison | "Whatsminer firmware comparison" | Cross-reference in "Related comparisons" section |

---

## Schema Map by Page Type

| Page Type | Primary Schema | Secondary Schema | Rationale |
|---|---|---|---|
| Pillar (commercial) | SoftwareApplication | FAQPage | Product is a software application; FAQ captures PAA |
| How-to (update/install) | HowTo | FAQPage | Step-by-step content; HowTo gets rich results |
| Model-specific (M30S/M50) | TechArticle | FAQPage | Technical reference for specific hardware |
| Educational (custom firmware, autotuning) | TechArticle | FAQPage | Informational depth content |
| Comparison | TechArticle | FAQPage | Comparison articles map to TechArticle |
| Security | TechArticle | FAQPage | Expert security analysis; TechArticle signals E-E-A-T |
| Overclocking / Undervolting | TechArticle | HowTo | Mix of explainer + actionable steps |

---

## Priority Order for Production *(superseded by Architecture v2; reference material)*

*Recalculated 2026-09-25 from DataForSEO US data. The previous order (2026-06-19) was based on hypotheses and is kept in git history.*

1. **P0:** Whatsminer hub on the existing `/en/firmwares/whatsminer-all-series` (or a new hub; decide with the team [VERIFY]). Protect the #3 position for `whatsminer firmware` (CPC $32.03, KD 4). Add `whatsminer tool` (50/mo).
2. **P1:** M30S → `/en/firmwares/whatsminer-series-m3x` and M50/M60 → `-m5x`/`-m6x`. Optimize the existing series pages (10/mo each).
3. **P1:** comparison. Volume is n/d, but it's the only segment without competitors, so a comparison table cements the "only third-party Whatsminer vendor" position in LLM answers.
4. **P1:** security + dev fee (↑ from P2). A shared page with Antminer, see `antminer-firmware.md`.
5. **P2:** custom (10/mo, KD 50) becomes a section of the hub. Install and update (10/mo) become one page, with documentation already in `/en/documentation`.
6. **P2:** tuning modes, covering overclocking (10/mo), undervolting (n/d) and autotuning (n/d), as one page.
