# Topic Cluster: Immersion Cooling Mining
**Site:** https://bixbit.io/en
**Cluster slug:** immersion-cooling-mining
**Created:** 2026-06-19
**Last updated:** 2026-09-25 (volumes and priorities recalculated from DataForSEO)
**DataForSEO status:** OK. Volumes from Google Ads search_volume, KD from Labs (United States / en), as of 2026-09-25. `n/d` = fewer than ~10/mo. Before/after table: `reports/cluster-repriorization-2026-09-25.md`.
**Priority:** P1 (CLAUDE.md §3, second after the ASIC firmware clusters). Confirmed: the cluster has the largest total demand, but mostly broad terms with low commercial value (CPC $2–4).

**Key finding (2026-09-25):**
- **Mining-specific queries are tiny.** `immersion cooling mining` is 20/mo (KD 0, BiXBiT #14 via a blog post); `immersion cooling antminer` and `antminer immersion cooling` are 20 each (KD 55).
- **Broad terms carry the volume.** `immersion cooling` is 1600/mo (KD 21, BiXBiT #32) and `immersion computer cooling` is 390 (KD 10, #15). These are wider than the ICP, so use them as a traffic source through the blog post `how-does-immersion-cooling-work`, with links to the commercial page.
- **BiXBiT already owns the mineral oil group.** `mineral oil for immersion cooling` (30) is #1; `antminer mineral oil`, `antminer in mineral oil` and `mineral oil antminer` (50 each) are #2; `mineral oil immersion cooling` (20) is #5. That's about 200/mo on `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining`, the largest owned block in the cluster.
- **Real URLs:** the commercial pages exist at `/en/asics-cooling/immersion-systems` and `/en/asics-cooling`. The slugs `/en/immersion-cooling-mining/*` below are working names [VERIFY with the team before creating them].

---

## Architecture v2 (2026-09-25): authoritative

> This section **replaces** the Hub/Spoke lists and the production order below. Spokes are no longer separate URLs: they become H2 sections on existing live pages. A new URL is created only for a standalone search intent. Rationale and the full table for all clusters: `reports/content-architecture-2026-09-25.md`. Links: `content/internal-linking.md` → «Architecture v2 — Linking Matrix». The old sections are kept below as **reference material for writers** (keywords, outlines, FAQs); their URLs no longer apply.

| URL | Type | Page priority | Sections from briefs (section priority) | What gets added |
|---|---|---|---|---|
| `/en/asics-cooling/immersion-systems` | existing | **P0** | `immersion-cooling-mining-pillar` → Main page content (pillar) (P0)<br>`immersion-cooling-antminer` → H2 Antminer and Whatsminer in immersion (P1)<br>`immersion-cooling-whatsminer` → H2 Antminer and Whatsminer in immersion (Whatsminer part) (P2)<br>`single-phase-immersion-cooling` → H2 Single-phase vs two-phase (P1)<br>`two-phase-immersion-cooling` → H2 Single-phase vs two-phase (two-phase part) (P2)<br>`immersion-cooling-vs-air-cooling` → H2 Immersion vs air (short version also on /en/asics-cooling) (P2)<br>`immersion-cooling-tank` → H2 Tanks and system components (P2)<br>`immersion-cooling-asic-setup` → H2 Deployment steps (P2)<br>`immersion-cooling-roi` → H2 ROI / TCO (link to /en/calc) (P2)<br>`immersion-cooling-data-center` → H2 Data center deployments (P2) | H2 sections: immersion for bitcoin mining (the pillar); Antminer and Whatsminer in immersion (models, firmware profiles [VERIFY]); single-phase vs two-phase; immersion vs air; tanks and system components; deployment steps; ROI/TCO (link to /en/calc, no profitability promises); data center deployments; FAQ; Product schema. Move 'immersion cooling mining' (#14 via a blog post) onto this page |
| `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` | existing | **P1** | `immersion-cooling-dielectric-fluid` → Refresh the existing post (P1) | Refresh: current fluid types table [VERIFY], mineral oil vs synthetic vs engineered fluids, an Antminer-in-mineral-oil section, updated date; a link to immersion-systems. This post already has its own URL, so no new page |
| `/en/blog/post/how-does-immersion-cooling-work` | existing | **P1** | — (no cluster briefs) | Refresh: definition, how it works, single/two-phase at a glance; a CTA link to immersion-systems |
| `/en/asics-cooling` | existing | **P2** | — (no cluster briefs) | A short immersion vs hydro vs air comparison block and links to immersion-systems / hydro-systems. Adding it to the sitemap is a separate technical task |

**Production order:** `/en/asics-cooling/immersion-systems` (P0) → `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` (P1) → `/en/blog/post/how-does-immersion-cooling-work` (P1) → `/en/asics-cooling` (P2)

---
## Cluster Purpose

Establish BiXBiT as a credible B2B vendor for industrial-scale immersion cooling infrastructure targeting operators running 100–100,000+ ASICs. Differentiate from pure hardware vendors (LiquidStack, GRC, Engineered Fluids) by leading with the firmware-cooling integration angle — BiXBiT is the only vendor in this SERP space that ships both immersion cooling hardware and custom firmware (Antminer + Whatsminer) designed to leverage immersion thermal headroom.

---

## Hub-and-Spoke Architecture *(superseded by Architecture v2; reference material)*

### Hub (Pillar Page)
| Attribute | Value |
|---|---|
| Slug | `/en/immersion-cooling-mining` |
| Primary keyword | `immersion cooling mining` |
| Secondary keywords | `ASIC immersion cooling`, `bitcoin miner immersion cooling`, `immersion cooled bitcoin miner`, `mining immersion cooling system` |
| Intent | Commercial investigation — operator evaluating whether to deploy immersion and which vendor/system to choose |
| Schema | `Product` + `FAQPage` |
| Word count target | 3,000–3,500 |
| Brief | `content/briefs/immersion-cooling-mining-pillar.md` |

### Spoke Pages

| # | Slug | Primary Keyword | Intent | Schema | Vol (US, 2026-09) | Priority (was → now) | Brief |
|---|---|---|---|---|---|---|---|
| 1 | `/en/immersion-cooling-mining/vs-air-cooling` | `immersion cooling vs air cooling mining` | Informational / comparison | `Article` + `FAQPage` | n/d for every keyword | P1 → **P2** | `immersion-cooling-vs-air-cooling.md` |
| 2 | `/en/immersion-cooling-mining/single-phase` | `single phase immersion cooling mining` | Informational / commercial | `Article` + `FAQPage` | 20 (`single phase vs two phase immersion cooling`, KD 40) | P1 → **P1**; merge with two-phase | `single-phase-immersion-cooling.md` |
| 3 | `/en/immersion-cooling-mining/two-phase` | `two phase immersion cooling mining` | Informational / commercial | `Article` + `FAQPage` | n/d | P2 → **P2**; section of #2 | `two-phase-immersion-cooling.md` |
| 4 | `/en/immersion-cooling-mining/dielectric-fluid` | `immersion cooling dielectric fluid` | Informational | `Article` + `FAQPage` | ~200 across the mineral oil group; BiXBiT #1–5 | P2 → **P1**; refresh the existing post | `immersion-cooling-dielectric-fluid.md` |
| 5 | `/en/immersion-cooling-mining/setup-guide` | `ASIC immersion cooling setup` | Informational / transactional | `HowTo` + `FAQPage` | n/d | P1 → **P2** | `immersion-cooling-asic-setup.md` |
| 6 | `/en/immersion-cooling-mining/roi` | `immersion cooling ROI mining` | Commercial investigation | `Article` + `FAQPage` | n/d | P1 → **P2** | `immersion-cooling-roi.md` |
| 7 | `/en/immersion-cooling-mining/data-center` | `immersion cooling data center mining` | Commercial investigation | `Article` + `FAQPage` | n/d | P2 → **P2** | `immersion-cooling-data-center.md` |
| 8 | `/en/immersion-cooling-mining/antminer` | `immersion cooling Antminer` | Commercial / transactional | `Product` + `FAQPage` | 40 (20+20, KD 55, CPC $2.12) | P0 → **P1** | `immersion-cooling-antminer.md` |
| 9 | `/en/immersion-cooling-mining/whatsminer` | `immersion cooling Whatsminer` | Commercial / transactional | `Product` + `FAQPage` | n/d | P0 → **P2**; section of #8 | `immersion-cooling-whatsminer.md` |
| 10 | `/en/immersion-cooling-mining/tank` | `mining immersion tank` | Commercial investigation | `Product` + `FAQPage` | 10 (`asic immersion cooling tank`) | P1 → **P2** | `immersion-cooling-tank.md` |
| 11 | `/en/immersion-cooling-mining/pue` | `immersion cooling PUE data center` | Informational | `Article` | n/d | P2 (deferred) | *(defer: low commercial value for BiXBiT's ICP at this stage)* |

**Total active briefs: 10** (PUE page deferred — low product tie-in for current BiXBiT product scope).

---

## Competitor Gap Analysis

### Who ranks in this SERP space
- **LiquidStack** — strong product pages, weak on ROI calculators and firmware integration content
- **Engineered Fluids** — deep technical content on dielectric fluids, weak on ASIC-specific setup and operator TCO
- **GRC (Green Revolution Cooling)** — strong on data center / enterprise angle, minimal Bitcoin mining specifics
- **DCX** — thin content overall, few guides
- **Braiins / Vnish / LuxOS** — firmware vendors with no immersion cooling content at all

### BiXBiT content gaps to exploit
1. **Firmware + immersion integration** — nobody covers "what firmware settings to use in immersion" as a dedicated page. BiXBiT is uniquely positioned here.
2. **Mid-scale ROI (100–5,000 ASIC)** — LiquidStack targets hyperscale (5,000+ ASIC); GRC targets enterprise IT. The 100–5,000 ASIC mining operator segment is underserved.
3. **Model-specific pages** (immersion cooling for Antminer S19/S21, Whatsminer M50/M60) — no competitor owns these SERP slots.
4. **Immersion tank buying guide** — informational with commercial intent; nobody does a thorough, brand-neutral guide that positions their own product.
5. **Single-phase vs two-phase decision guide** — existing content is generic; BiXBiT can anchor it to real mining operator decisions.

---

## Cross-Cluster Integration Points *(superseded by `content/internal-linking.md` → Architecture v2)*

### Immersion Cooling → Antminer Firmware Cluster
| Immersion Cooling Page | Target Firmware Page | Rationale |
|---|---|---|
| `/en/immersion-cooling-mining` (pillar) | `/en/antminer-firmware/overclocking` | Immersion unlocks sustained overclock |
| `/en/immersion-cooling-mining` (pillar) | `/en/antminer-firmware` | BiXBiT firmware optimized for immersion |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware` | Primary CTA — pair hardware with firmware |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware/overclocking` | Immersion-specific overclock profiles |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware/antminer-s19` | S19 immersion deployment |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware/antminer-s21` | S21 / S21 Hydro deployment |
| `/en/immersion-cooling-mining/setup-guide` | `/en/antminer-firmware/install` | Firmware install is part of immersion setup |
| `/en/immersion-cooling-mining/roi` | `/en/antminer-firmware/undervolting` | Efficiency gains compound ROI |

### Immersion Cooling → Whatsminer Firmware Cluster
| Immersion Cooling Page | Target Firmware Page | Rationale |
|---|---|---|
| `/en/immersion-cooling-mining` (pillar) | `/en/whatsminer-firmware/overclocking` | Immersion unlocks sustained Whatsminer overclock |
| `/en/immersion-cooling-mining` (pillar) | `/en/whatsminer-firmware` | BiXBiT Whatsminer firmware for immersion |
| `/en/immersion-cooling-mining/whatsminer` | `/en/whatsminer-firmware` | Primary CTA — pair hardware with firmware |
| `/en/immersion-cooling-mining/whatsminer` | `/en/whatsminer-firmware/overclocking` | Immersion-specific overclock profiles |
| `/en/immersion-cooling-mining/whatsminer` | `/en/whatsminer-firmware/whatsminer-m50` | M50/M60 immersion deployment |
| `/en/immersion-cooling-mining/setup-guide` | `/en/whatsminer-firmware/install` | Firmware install is part of immersion setup |
| `/en/immersion-cooling-mining/roi` | `/en/whatsminer-firmware/undervolting` | Efficiency gains compound ROI |

### Firmware Clusters → Immersion Cooling (already partially in internal-linking.md, extended here)
| Source Firmware Page | Target Immersion Page | Anchor Text |
|---|---|---|
| `/en/antminer-firmware/overclocking` | `/en/immersion-cooling-mining` | "immersion cooling for sustained overclocking" |
| `/en/antminer-firmware/undervolting` | `/en/immersion-cooling-mining` | "immersion cooling extends undervolt headroom" |
| `/en/antminer-firmware/custom` | `/en/immersion-cooling-mining` | "custom firmware for immersion deployments" |
| `/en/antminer-firmware/antminer-s21` | `/en/immersion-cooling-mining/antminer` | "immersion cooling for Antminer S21" |
| `/en/whatsminer-firmware/overclocking` | `/en/immersion-cooling-mining` | "immersion cooling for sustained Whatsminer overclocking" |
| `/en/whatsminer-firmware/undervolting` | `/en/immersion-cooling-mining` | "immersion cooling extends Whatsminer undervolt headroom" |
| `/en/whatsminer-firmware/whatsminer-m50` | `/en/immersion-cooling-mining/whatsminer` | "immersion cooling for Whatsminer M60" |

---

## Content Production Priority *(superseded by Architecture v2; reference material)*

*Recalculated 2026-09-25 from DataForSEO US data. The previous order (2026-06-19) is kept in git history.*

| Priority | Page | Rationale (2026-09-25 data) |
|---|---|---|
| P0 | Pillar on the existing `/en/asics-cooling/immersion-systems` | Move `immersion cooling mining` (20/mo, KD 0; BiXBiT #14 via a blog post) and `asic immersion cooling` (10, KD 0) onto the commercial page |
| P1 | Refresh the existing post `immersion-liquid-choosing-the-right-one-for-mining` (dielectric fluid brief) | ↑ from P2. Protect about 200/mo at #1–5 (the mineral oil group); link from it to the pillar |
| P1 | Refresh the existing post `how-does-immersion-cooling-work` | New item. `immersion computer cooling` 390 (#15), `what is immersion cooling` 90 (#19), `immersion cooling` 1600 (#32). Broad traffic, funneled to the pillar |
| P1 | `/antminer` (Whatsminer as a section) | ↓ from P0. 40/mo, KD 55, CPC $2.12 |
| P1 | `/single-phase` (plus the two-phase section) | 20/mo, KD 40 |
| P2 | `/vs-air-cooling`, `/roi`, `/setup-guide`, `/tank`, `/data-center`, `/whatsminer` | ↓. n/d or 10/mo. Build later, or as sections of the pillar |
