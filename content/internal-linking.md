# Internal Linking Matrix — Firmware + Immersion Cooling + Fleet Monitoring + Hardware Clusters
**Site:** https://bixbit.io/en
**Last updated:** 2026-09-28 (Hardware section added to Architecture v2); 2026-09-25 (Architecture v2 added; older matrices superseded)
**Clusters:** antminer-firmware, whatsminer-firmware, immersion-cooling-mining, mining-fleet-monitoring, hardware
**Scope:** All five clusters, cross-cluster links, and links to AMS, PDU, and homepage

---

## Architecture v2 — Linking Matrix (2026-09-25): authoritative

> **This section replaces the matrices below.** Architecture v2 has 17 URLs: 13 existing live pages extended with new H2 sections, plus 4 new pages for standalone intents. The old spokes (`/en/antminer-firmware/*`, `/en/whatsminer-firmware/*`, `/en/immersion-cooling-mining/*`, `/en/ams/<spoke>`) **are not being created**, so links to them must not go live. The sections below this one are kept only as anchor-text ideas. Plan and rationale: `reports/content-architecture-2026-09-25.md`.

### Rules for v2
- Links to a **section** of a long page use a fragment such as `/en/firmwares/antminer#s21`. Fragment ids are fixed when the page is built [VERIFY with dev].
- Each new page (comparison, dev-fee, the Antminer install guide, AMS comparison) gets **at least 3 incoming links** from existing pages at launch.
- Anchors must be descriptive, and the same exact anchor may appear on at most 2 pages. No "click here" or "learn more".
- The legacy noindex model pages (`/en/firmwares/asic-s19` and similar) link to the matching section of `/en/firmwares/antminer`, e.g. `#s19`.

### Firmware

| # | From | To | Anchor (example) | Placement | P |
|---|---|---|---|---|---|
| F1 | `/en` (homepage) | `/en/firmwares` | custom firmware for Antminer and Whatsminer | hero / product block | P0 |
| F2 | `/en/firmwares` | `/en/firmwares/antminer` | Antminer firmware | platforms block | P0 |
| F3 | `/en/firmwares` | `/en/firmwares/whatsminer-all-series` | Whatsminer firmware | platforms block | P0 |
| F4 | `/en/firmwares` | `/en/firmwares/comparison` | compare BiXBiT with Braiins OS+, Vnish, LuxOS and ePIC | after the opening passage | P0 |
| F5 | `/en/firmwares` | `/en/firmwares/dev-fee` | how the BiXBiT dev fee works | dev fee summary block | P0 |
| F6 | `/en/firmwares/antminer` | `/en/firmwares/comparison` | Antminer firmware comparison | "Why BiXBiT" section | P0 |
| F7 | `/en/firmwares/antminer` | `/en/firmwares/dev-fee` | dev fee and firmware security | FAQ / trust block | P0 |
| F8 | `/en/firmwares/antminer` | `/en/documentation/antminer-firmware-install` | step-by-step Antminer firmware installation | Install & update section | P1 |
| F9 | `/en/firmwares/antminer` | `/en/ams` | monitor your Antminer fleet in AMS | after the tuning modes section | P1 |
| F10 | `/en/firmwares/antminer#tuning` | `/en/asics-cooling/immersion-systems` | immersion cooling for sustained overclocking | tuning modes → overclocking | P1 |
| F11 | `/en/firmwares/antminer` | `/en/firmwares/whatsminer-all-series` | firmware for Whatsminer in mixed fleets | platforms / FAQ | P1 |
| F12 | `/en/firmwares/whatsminer-all-series` | `-m2x`, `-m3x`, `-m5x`, `-m6x` | Whatsminer M20 / M30 / M50 / M60 series firmware | series overview | P0 |
| F13 | `-m2x`, `-m3x`, `-m5x`, `-m6x` | `/en/firmwares/whatsminer-all-series` | BiXBiT firmware for all Whatsminer series | breadcrumbs + intro | P0 |
| F14 | `/en/firmwares/whatsminer-all-series` | `/en/firmwares/comparison` | Whatsminer firmware options compared | "Why BiXBiT" | P0 |
| F15 | `/en/firmwares/whatsminer-all-series` | `/en/firmwares/dev-fee` | Whatsminer firmware dev fee by series | trust block | P0 |
| F16 | `/en/firmwares/whatsminer-all-series` | `/en/ams` | one dashboard for Antminer and Whatsminer | mixed fleet section | P1 |
| F17 | `/en/firmwares/whatsminer-all-series` | `/en/documentation/user-guide-for-whatsminer-asic` | how to install firmware on Whatsminer | Install section | P2 |
| F18 | `-m5x`, `-m6x` | `/en/asics-cooling/immersion-systems` | immersion and hydro profiles for Whatsminer M50/M60 | modes section | P1 |
| F19 | `/en/firmwares/comparison` | `/en/firmwares/antminer`, `/en/firmwares/whatsminer-all-series` | BiXBiT firmware for Antminer / for Whatsminer | table CTA | P0 |
| F20 | `/en/firmwares/comparison` | `/en/firmwares/dev-fee` | how dev fees compare in practice | fee row / FAQ | P0 |
| F21 | `/en/firmwares/comparison` | `/en/ams/comparison` | monitoring software compared | "Beyond firmware" block | P1 |
| F22 | `/en/firmwares/dev-fee` | `/en/firmwares/comparison`, `/en/firmwares/antminer`, `/en/firmwares/whatsminer-all-series` | full firmware comparison; Antminer firmware; Whatsminer firmware | TCO section / CTA | P0 |
| F23 | `/en/documentation/antminer-firmware-install` | `/en/firmwares/antminer`, `/en/ams` | BiXBiT Antminer firmware; connect units to AMS | intro + final step | P1 |
| F24 | `/en/faq` | `/en/firmwares/dev-fee`, `/en/firmwares/comparison` | dev fee question; firmware comparison | answers | P1 |

### Cooling

| # | From | To | Anchor (example) | Placement | P |
|---|---|---|---|---|---|
| C1 | `/en` (homepage) | `/en/asics-cooling/immersion-systems` | immersion cooling systems for ASIC fleets | product block | P0 |
| C2 | `/en/asics-cooling` | `/en/asics-cooling/immersion-systems`, `/en/asics-cooling/hydro-systems` | immersion cooling; hydro cooling | comparison block | P0 |
| C3 | `/en/asics-cooling/immersion-systems` | `/en/firmwares/antminer#tuning`, `/en/firmwares/whatsminer-series-m6x` | firmware profiles for immersion; Whatsminer M60 in immersion | Antminer & Whatsminer section | P0 |
| C4 | `/en/asics-cooling/immersion-systems` | `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` | choosing a dielectric fluid (mineral oil vs synthetic) | tanks & components | P1 |
| C5 | `/en/asics-cooling/immersion-systems` | `/en/calc` | calculate payback for your fleet | ROI / TCO section | P1 |
| C6 | `/en/asics-cooling/immersion-systems` | `/en/ams` | monitor temperature and hashrate per unit | deployment steps | P1 |
| C7 | `/en/asics-cooling/immersion-systems` | `/en/asics-cooling/immersion-systems/ict-100`, `/en/asics-cooling/immersion-systems/ic-1000`, `/en/products/cell`, `/en/products/rack`, `/en/products/container`, `/en/products/container-1k`, `/en/products/coolant` (immersion products per `/en/products` catalog and model pages, 2026-09-28; legacy vs current line [VERIFY]) | product names | tanks & components | P1 |
| C8 | `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` | `/en/asics-cooling/immersion-systems` | industrial immersion cooling systems | intro + conclusion | P1 |
| C9 | `/en/blog/post/how-does-immersion-cooling-work` | `/en/asics-cooling/immersion-systems`, the mineral oil post | immersion cooling for bitcoin mining; which fluid to choose | after the definition + conclusion | P1 |
| C10 | `/en/asics-cooling/hydro-systems` | `/en/asics-cooling/immersion-systems` | hydro vs immersion | comparison block | P2 |

### AMS

| # | From | To | Anchor (example) | Placement | P |
|---|---|---|---|---|---|
| A1 | `/en` (homepage) | `/en/ams` | ASIC fleet monitoring (AMS) | product block | P0 |
| A2 | `/en/ams` | `/en/ams/comparison` | how AMS compares with Minerstat, Braiins Manager and Luxor Commander | after the features section | P1 |
| A3 | `/en/ams` | `/en/firmwares/antminer`, `/en/firmwares/whatsminer-all-series` | BiXBiT firmware for Antminer / Whatsminer | mixed fleet section | P0 |
| A4 | `/en/ams#alerts` | `/en/asics-cooling/immersion-systems` | temperature alerts in immersion deployments | alerts section | P2 |
| A5 | `/en/ams/comparison` | `/en/ams` | try BiXBiT AMS | table CTA | P1 |
| A6 | `/en/ams/comparison` | `/en/firmwares/comparison` | firmware comparison | "Firmware + monitoring" block | P1 |

### Incoming links to the new pages at launch (check)

| New page | Incoming links (minimum 3) |
|---|---|
| `/en/firmwares/comparison` | F4, F6, F14, F22, F24, A6 |
| `/en/firmwares/dev-fee` | F5, F7, F15, F20, F24 |
| `/en/documentation/antminer-firmware-install` | F8 + legacy noindex pages (`asic-s19`, …) + `/en/documentation` index [VERIFY] |
| `/en/ams/comparison` | A2, F21 + `/en/faq` [VERIFY] |

### Hardware (added 2026-09-28)

> Cluster: `content/clusters/hardware.md`; briefs `content/briefs/hardware-*.md`. Existing URLs only. Why this matters (crawl 2026-09-28): the 8 model pages under `/en/asics-cooling/{hydro,immersion}-systems/*` have **2 internal links each**, `/en/products/pdu` has 14 and 0 from the blog, while `/en/products/rack` has 618 and `/en/products/server` 607 (menu). Cooling rows C1–C10 above stay valid; H-rows add the product layer.
> Anchor split to avoid cannibalization: "hydro cooling system(s)" / "mining water cooling" → hydro sub-hub only; "hydro container" → `container-hydro`; "hydro rack" → `rack-hydro`; "mining container" → `container`; "immersion container" → `container-1k` or IC-1000; "immersion cooling fluid" / "dielectric coolant" → `coolant`; "immersion cooling tank" → `cell` (ICT-100 gets its model name).
> Product cards on sub-hubs must be plain crawlable `<a href>` links (template brief).

**Hub and sub-hubs → products**

| # | From | To | Anchor (example) | Placement | P |
|---|---|---|---|---|---|
| H1 | `/en/asics-cooling` | `/en/asics-cooling/hydro-systems`, `/en/asics-cooling/immersion-systems` | covered by C2 | comparison block | P0 |
| H2 | `/en/asics-cooling` | `/en/products/container`, `/en/products/container-1k`, `/en/products/container-hydro` | immersion mining containers; single-loop immersion container; hydro mining container | "Choose a cooling system" cards | P1 |
| H3 | `/en/asics-cooling` | `/en/products/rack`, `/en/products/rack-hydro`, `/en/products/cell`, `/en/products/coolant`, `/en/products/server`, `/en/products/pdu` | ASIC mining racks; water-cooled hydro racks; Cell immersion tank; dielectric immersion coolant; prefab data center cooling; smart PDUs for mining racks | "Choose a cooling system" cards | P1 |
| H4 | `/en/asics-cooling` | all 8 model pages | model names (e.g. "AHC-2.4 hydro container") | "All models" table | P1 |
| H5 | `/en/asics-cooling/hydro-systems` | 6 hydro model pages | model + type (e.g. "WHR-200-2U hydro rack for Whatsminer") | product line cards (exist; make crawlable) | P0 |
| H6 | `/en/asics-cooling/hydro-systems` | `/en/products/container-hydro`, `/en/products/rack-hydro` | hydro container for Whatsminer; hydro rack | product line sections | P0 |
| H7 | `/en/asics-cooling/hydro-systems` | `/en/products/pdu`, `/en/ams`, `/en/firmwares/antminer` (S21 Hydro section, fragment [VERIFY]), `/en/firmwares/whatsminer-series-m6x` | power distribution for hydro racks; monitor loop temperatures in AMS; firmware for Antminer S21 Hydro; Whatsminer M60-series hydro firmware | site requirements / AMS / supported miners | P1 |
| H8 | `/en/asics-cooling/immersion-systems` | `ict-100`, `ic-1000` | covered by C7 | tanks & components | P1 |
| H9 | `/en/products` (catalog) | `/en/products/cell`, `/en/products/rack`, `/en/products/container`, `/en/products/coolant`, `/en/products/container-1k` | product names (Cell, Rack, Container, Coolant, Container-1K) | product sections (exist; confirm each section links to its product page with a descriptive anchor) | P0 |
| H10 | `/en/products` (catalog) | `/en/asics-cooling/immersion-systems` | industrial immersion cooling systems | intro | P1 |

**Product ↔ product**

| # | From | To | Anchor (example) | Placement | P |
|---|---|---|---|---|---|
| H11 | each hydro model page | `/en/asics-cooling/hydro-systems`; sibling model in the same line (WHR-200-2U ↔ AHR-200; WHC-1.2-2U ↔ WHC-2.4-2U ↔ AHC-2.4 ↔ HW-Cluster-2.4); `/en/ams` | all hydro cooling systems; sibling model name; "Integration with BiXBiT AMS" heading becomes a link | breadcrumb + "Compare with" + AMS block | P1 |
| H12 | `ict-100`, `ic-1000` | `/en/asics-cooling/immersion-systems`, `/en/products/coolant`, each other | immersion cooling systems; BiXBiT dielectric coolant; model name | breadcrumb + specs | P1 |
| H13 | `/en/products/container` | `/en/products/container-1k`, `/en/products/container-hydro`, `/en/asics-cooling/hydro-systems/ahc-2.4`, `/en/asics-cooling/immersion-systems/ic-1000`, `/en/products/coolant`, `/en/products/pdu`, `/en/ams`, `/en/calc` | single-loop version for moderate climates; hydro container alternative; AHC-2.4 40 ft hydro container; IC-1000 all-in-one immersion container; coolant for the first fill; in-container power distribution; container monitoring; estimate fleet economics | "Other containers", site requirements, cost, monitoring | P0 |
| H14 | `/en/products/rack` | `/en/products/cell`, `/en/products/coolant`, `/en/products/container`, `/en/products/rack-hydro`, `/en/products/pdu` | small-site immersion tank; immersion fluid for racks; scale racks into a container; hydro rack for hydro miners; rack power distribution | format comparison, scaling, coolant | P0 |
| H15 | `/en/products/rack-hydro`, `/en/products/container-hydro` | `/en/asics-cooling/hydro-systems`, WHR-200-2U / AHR-200 (rack-hydro), WHC-2.4-2U / AHC-2.4 (container-hydro) | hydro cooling systems for ASIC mining; model names | compare block | P1 |
| H16 | `/en/products/coolant` | `/en/products/cell`, `/en/products/rack`, `/en/products/container`, `/en/asics-cooling/immersion-systems` | fill volume for Cell; for Rack; for Container; immersion cooling for mining farms | compatibility / fill-volume table | P1 |
| H17 | `/en/products/cell` | `/en/products/coolant`, `/en/products/rack`, `ict-100` | coolant for the Cell; scale up to a rack; industrial modular immersion unit | kit / scaling | P1 |
| H18 | `/en/products/server` | `/en/asics-cooling/immersion-systems`, `/en/asics-cooling/hydro-systems`, `/en/products/pdu`, blog `how-to-calculate-the-pue-of-a-datacenter` | immersion cooling systems; direct liquid cooling for mining; power distribution; how to calculate PUE | sections | P1 |
| H19 | `/en/products/pdu` (PDU cluster) | `/en/products/rack`, `/en/products/container`, `/en/asics-cooling/hydro-systems` | PDU in BiXBiT racks; containers; hydro systems | "Where it's used" | P1 [confirm with PDU cluster owner] |

**Blog → products (existing posts; RU mirrors follow the same pattern for `/ru/products/*` except `server` and `pdu`, which 404 in RU)**

| # | From (blog post) | To | Anchor (example) | Placement | P |
|---|---|---|---|---|---|
| H-B1 | `how-shipping-containers-change-the-cryptocurrency-mining-industry` | `/en/products/container`, `/en/asics-cooling/hydro-systems` | BiXBiT immersion mining containers; hydro-cooled containers | after the intro + conclusion (with EN-FEB-4 refresh; K4 de-cannibalization) | P0 |
| H-B2 | `immersion-liquid-choosing-the-right-one-for-mining` | `/en/products/coolant` | BiXBiT dielectric immersion fluid | fluid comparison section (C4 already links to immersion-systems) | P1 |
| H-B3 | `novec-and-coolant-liquids-comparison-why-we-stick-to-our-own-formula` (GSC 469 impr, pos 8.5) | `/en/products/coolant` | our immersion cooling fluid | conclusion | P1 |
| H-B4 | `how-does-immersion-cooling-work` | `/en/products/cell` | immersion cooling tank for ASIC miners | "system components" paragraph (C9 covers the pillar link) | P2 |
| H-B5 | `immersion-cooling-or-how-to-stop-wasting-money-on-air` | `/en/products` | immersion cooling equipment | conclusion (EN-DEC-3 refresh) | P2 |
| H-B6 | `how-to-make-1500-asics-out-of-1000-bought-the-magic-of-immersion-cooling`, `review-of-miners-2021-new-models-vs-old-ones-with-immersion-cooling` | `/en/products/container`, `/en/products/rack` | immersion containers; immersion racks | body | P2 |
| H-B7 | `hydro-asic-2026-ranking-models-for-largescale-mining-farms` (117 inlinks), `bitmain-releases-t19-hydro-btc-miner-with-a-performance-of-145-th-s` | `/en/asics-cooling/hydro-systems`, `/en/asics-cooling/hydro-systems/ahr-200` | hydro cooling racks and containers; AHR-200 rack for Antminer hydro miners | model sections | P1 |
| H-B8 | `full-review-of-microbt-whatsminer-m50-m50s-and-m53-asics-features-profit-payback` (GSC 850 impr) | `/en/asics-cooling/hydro-systems/whr-200-2u` | WHR-200-2U hydro rack for Whatsminer | M53 Hydro section (EN-MAY-2) | P1 |
| H-B9 | `killers-of-the-mining-equipment-getting-rid-of-noise-and-dust` (GSC 400 impr) | `/en/asics-cooling/hydro-systems` | liquid cooling removes fan noise and dust | solutions section (EN-FEB-3) | P2 |
| H-B10 | `how-to-calculate-the-pue-of-a-datacenter`, `datacenter-cooling-methods-everything-you-need-to-know`, `data-centre-cooling-trends-2026` | `/en/products/server`, `/en/asics-cooling` | prefab data center cooling; cooling systems for ASIC mining | methods / conclusion (EN-OCT-3, EN-JUN-2) | P1 |
| H-B11 | `asic-cooling-trends-2026` | `/en/asics-cooling`, `/en/asics-cooling/hydro-systems` | BiXBiT cooling systems; hydro cooling for ASIC mining | trends list | P2 |
| H-B12 | `creating-a-mining-farm-setting-priorities` | `/en/products/container`, `/en/products/pdu` | containerized mining farm; power distribution for the farm | infrastructure section | P2 |
| H-B13 | planned posts: EN-JAN-1 (hydro vs immersion), EN-NOV-1 (S21 series), EN-NOV-2 (Whatsminer lineup), EN-MAR-2 (fluid maintenance) | hydro-systems + AHR-200; hydro-systems + WHR-200-2U; `/en/products/coolant` | per `content/blog-plan.md` | at publication | P1 |

**Incoming links check (hardware, after rollout):** each model page ≥ 4 incoming (sub-hub card, hub table, sibling, one blog or product page); `/en/products/pdu` gains H3, H7, H13, H14, H18, H-B12 (+ PDU cluster rows); `/en/products/coolant` gains C7, H3, H12, H13, H14, H17, H-B2, H-B3.

---

## Notes on Usage

- Anchor text should be descriptive and keyword-relevant — no "click here" or "learn more"
- Prioritize links from established/existing pages TO new cluster pages to accelerate indexing
- Each spoke page should have 1–2 links back to the pillar (hub) and 2–4 links to related spokes
- The pillar page links out to all spokes; spokes link back to the pillar and to related spokes only (avoid circular loops with no editorial justification)
- Cross-cluster links (firmware → cooling, firmware → AMS) are high-priority for topical authority and user journey

---

## Full Linking Matrix *(v1, 2026-06-19; superseded by Architecture v2)*

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| Homepage | /en/antminer-firmware | "Antminer firmware" | Primary navigation + hero CTA section | P0 |
| Homepage | /en/antminer-firmware | "custom ASIC firmware" | Product ecosystem section | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/install | "full installation guide" | "How It Works" section, step 2 CTA | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/comparison | "compare BiXBiT with other firmware options" | Features section, after feature grid | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/autotuning | "per-chip autotuning" | Key Features section, autotuning feature bullet | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/security | "firmware security and audit" | Security/trust section | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/overclocking | "overclocking mode" | Key Features section | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/undervolting | "undervolting mode" | Key Features section | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/antminer-s19 | "Antminer S19 firmware" | Compatible models section | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/antminer-s21 | "Antminer S21 firmware" | Compatible models section | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/update | "firmware update guide" | How It Works section, step 3 note | P0 |
| /en/antminer-firmware (pillar) | /en/antminer-firmware/custom | "what is custom firmware" | Intro paragraph or FAQ | P1 |
| /en/antminer-firmware (pillar) | /en/ams | "AMS monitoring dashboard" | Features section — AMS integration feature | P0 |
| /en/antminer-firmware/update | /en/antminer-firmware | "BiXBiT firmware overview" | Intro paragraph | P0 |
| /en/antminer-firmware/update | /en/antminer-firmware/install | "complete installation guide" | Method 1 intro note | P1 |
| /en/antminer-firmware/update | /en/ams | "fleet-wide firmware updates via AMS" | Method 3 section | P1 |
| /en/antminer-firmware/update | /en/antminer-firmware/security | "verify firmware integrity before updating" | Pre-flight checklist section | P2 |
| /en/antminer-firmware/custom | /en/antminer-firmware | "BiXBiT firmware product overview" | H2: What BiXBiT Custom Firmware Offers | P0 |
| /en/antminer-firmware/custom | /en/antminer-firmware/security | "firmware security deep-dive" | Security section inline link | P1 |
| /en/antminer-firmware/custom | /en/antminer-firmware/overclocking | "overclocking with custom firmware" | What Custom Firmware Enables section | P1 |
| /en/antminer-firmware/custom | /en/antminer-firmware/undervolting | "undervolting for electricity cost reduction" | What Custom Firmware Enables section | P1 |
| /en/antminer-firmware/custom | /en/antminer-firmware/autotuning | "per-chip autotuning explained" | What Custom Firmware Enables section | P1 |
| /en/antminer-firmware/custom | /en/immersion-cooling | "immersion cooling for overclock deployments" | Custom firmware + immersion context | P2 |
| /en/antminer-firmware/antminer-s19 | /en/antminer-firmware | "BiXBiT firmware overview" | Intro paragraph | P0 |
| /en/antminer-firmware/antminer-s19 | /en/antminer-firmware/install | "installation guide" | Install section CTA | P1 |
| /en/antminer-firmware/antminer-s19 | /en/antminer-firmware/update | "firmware update guide" | Install section alternate link | P1 |
| /en/antminer-firmware/antminer-s19 | /en/antminer-firmware/antminer-s21 | "Antminer S21 firmware" | End of page — next-gen note | P2 |
| /en/antminer-firmware/antminer-s19 | /en/antminer-firmware/autotuning | "per-chip autotuning on S19" | Performance section | P1 |
| /en/antminer-firmware/antminer-s19 | /en/antminer-firmware/undervolting | "undervolting the S19" | Tuning modes section | P1 |
| /en/antminer-firmware/antminer-s19 | /en/ams | "AMS fleet management for S19 fleets" | Fleet management section | P1 |
| /en/antminer-firmware/antminer-s21 | /en/antminer-firmware | "BiXBiT firmware overview" | Intro paragraph | P0 |
| /en/antminer-firmware/antminer-s21 | /en/antminer-firmware/antminer-s19 | "S19 firmware for comparison" | Intro or migration section | P2 |
| /en/antminer-firmware/antminer-s21 | /en/antminer-firmware/install | "installation guide" | Install section CTA | P1 |
| /en/antminer-firmware/antminer-s21 | /en/antminer-firmware/autotuning | "per-chip autotuning" | Tuning section | P1 |
| /en/antminer-firmware/antminer-s21 | /en/ams | "fleet management for mixed S21 fleet" | Fleet section | P1 |
| /en/antminer-firmware/antminer-s21 | /en/hydro-cooling | "S21 Hydro cooling solutions" | S21 Hydro section | P2 |
| /en/antminer-firmware/overclocking | /en/antminer-firmware | "BiXBiT firmware overview" | Intro | P0 |
| /en/antminer-firmware/overclocking | /en/antminer-firmware/autotuning | "per-chip autotuning in overclock context" | Overclock profiles section | P1 |
| /en/antminer-firmware/overclocking | /en/antminer-firmware/undervolting | "undervolting as the alternative approach" | Is overclocking right for you section | P2 |
| /en/antminer-firmware/overclocking | /en/immersion-cooling | "immersion cooling for sustained overclocking" | Thermal management section | P1 |
| /en/antminer-firmware/overclocking | /en/ams | "monitor overclocked fleet in AMS" | Post-configuration step | P1 |
| /en/antminer-firmware/autotuning | /en/antminer-firmware | "BiXBiT firmware overview" | Intro | P0 |
| /en/antminer-firmware/autotuning | /en/antminer-firmware/overclocking | "overclocking vs autotuning" | Comparison section | P1 |
| /en/antminer-firmware/autotuning | /en/antminer-firmware/undervolting | "undervolting via per-chip voltage control" | Voltage scaling section | P1 |
| /en/antminer-firmware/autotuning | /en/ams | "monitor autotuning results in AMS" | Fleet autotuning section | P1 |
| /en/antminer-firmware/undervolting | /en/antminer-firmware | "BiXBiT firmware" | Intro | P0 |
| /en/antminer-firmware/undervolting | /en/antminer-firmware/autotuning | "per-chip autotuning enables precise undervolting" | How undervolting works section | P1 |
| /en/antminer-firmware/undervolting | /en/immersion-cooling | "immersion cooling for extended undervolt headroom" | Immersion section | P2 |
| /en/antminer-firmware/undervolting | /en/ams | "monitor undervolted fleet in AMS" | Configuration step | P1 |
| /en/antminer-firmware/install | /en/antminer-firmware | "BiXBiT firmware overview" | Intro | P0 |
| /en/antminer-firmware/install | /en/antminer-firmware/update | "firmware update guide (existing installations)" | Method 1 alternate reference | P1 |
| /en/antminer-firmware/install | /en/antminer-firmware/autotuning | "configure autotuning after install" | Post-installation configuration step | P1 |
| /en/antminer-firmware/install | /en/ams | "connect to AMS after installation" | Post-installation step 4 | P1 |
| /en/antminer-firmware/install | /en/antminer-firmware/security | "checksum verification and security" | Pre-installation checklist | P1 |
| /en/antminer-firmware/security | /en/antminer-firmware | "BiXBiT firmware overview" | Intro | P0 |
| /en/antminer-firmware/security | /en/antminer-firmware/install | "firmware installation guide" | Distribution chain audit section | P1 |
| /en/antminer-firmware/security | /en/antminer-firmware/comparison | "full firmware comparison including security" | Questions to ask any vendor section | P1 |
| /en/antminer-firmware/security | /en/ams | "dev fee detection with AMS monitoring" | Dev fee detection section | P1 |
| /en/antminer-firmware/comparison | /en/antminer-firmware | "BiXBiT firmware product page" | Intro and CTA | P0 |
| /en/antminer-firmware/comparison | /en/antminer-firmware/install | "install BiXBiT firmware" | End of page CTA | P1 |
| /en/antminer-firmware/comparison | /en/antminer-firmware/security | "security comparison and audit guide" | Security row in comparison table | P1 |
| /en/antminer-firmware/comparison | /en/ams | "AMS fleet management" | Fleet management comparison section | P1 |

---

## Cross-Cluster Links (Firmware → Other BiXBiT Products) *(v1, superseded)*

| Source Page | Target Page | Anchor Text | Rationale |
|---|---|---|---|
| /en/antminer-firmware (pillar) | /en/ams | "AMS monitoring dashboard" | Firmware + AMS are integrated products |
| /en/antminer-firmware/overclocking | /en/immersion-cooling | "immersion cooling for sustained overclock" | Overclock requires better cooling |
| /en/antminer-firmware/undervolting | /en/immersion-cooling | "lower temperatures enable deeper undervolt" | Thermal headroom + voltage headroom linked |
| /en/antminer-firmware/custom | /en/immersion-cooling | "custom firmware in immersion deployments" | Common operator upgrade path |
| /en/antminer-firmware/antminer-s21 | /en/hydro-cooling | "S21 Hydro liquid cooling" | S21 Hydro is a hydro-cooled variant |
| /en/ams | /en/antminer-firmware | "custom firmware telemetry" | AMS pages should reference firmware product |
| /en/immersion-cooling | /en/antminer-firmware | "firmware optimized for immersion" | Cooling pages should reference firmware |

---

## Links TO Cluster FROM Existing Site Pages *(v1, superseded)*

These links should be added or verified on existing bixbit.io/en pages to support cluster indexing:

| Existing Page | Add Link To | Anchor Text | Notes |
|---|---|---|---|
| Homepage | /en/antminer-firmware | "Antminer custom firmware" | Primary navigation + product cards |
| /en/ams | /en/antminer-firmware | "BiXBiT Antminer firmware" | AMS product page should mention firmware integration |
| /en/immersion-cooling | /en/antminer-firmware/overclocking | "firmware tuning for immersion overclock" | Cooling pages should link to firmware content |
| /en/immersion-cooling | /en/antminer-firmware | "custom firmware for immersion mining" | Cooling pages should link to firmware |

---

## Anchor Text Guidelines

- Use exact-match anchors sparingly (max 1–2 per page) — prefer partial-match descriptive anchors
- Avoid identical anchor text from the same source page to the same target
- Never use generic anchors: "click here", "learn more", "read this", "here"
- Model-specific anchors (e.g., "Antminer S19 firmware", "Whatsminer M30S firmware") are acceptable as exact-match because they are descriptive
- Security and trust pages: use anchors that frame the link as advice, not sales (e.g., "firmware security audit guide" not "BiXBiT secure firmware")

---

## Whatsminer Firmware Cluster — Full Linking Matrix *(v1, superseded)*

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| Homepage | /en/whatsminer-firmware | "Whatsminer firmware" | Primary navigation + product ecosystem section | P0 |
| Homepage | /en/whatsminer-firmware | "custom MicroBT firmware" | Product cards section alongside Antminer firmware | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/install | "full Whatsminer firmware installation guide" | How It Works section, step 2 CTA | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/comparison | "compare BiXBiT with other Whatsminer firmware options" | Features section, after feature grid | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/autotuning | "per-chip autotuning on Whatsminer" | Key Features section, autotuning feature bullet | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/security | "Whatsminer firmware security guide" | Security/trust section | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/overclocking | "Whatsminer overclocking mode" | Key Features section | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/undervolting | "undervolting Whatsminer ASICs" | Key Features section | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/whatsminer-m30s | "Whatsminer M30S firmware" | Compatible models section | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/whatsminer-m50 | "Whatsminer M50 and M60 firmware" | Compatible models section | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/update | "firmware update guide" | How It Works section, step 3 note | P0 |
| /en/whatsminer-firmware (pillar) | /en/whatsminer-firmware/custom | "what is custom firmware for Whatsminer" | Intro paragraph or FAQ | P1 |
| /en/whatsminer-firmware (pillar) | /en/ams | "AMS monitoring dashboard" | Features section — AMS integration feature | P0 |
| /en/whatsminer-firmware/update | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware overview" | Intro paragraph | P0 |
| /en/whatsminer-firmware/update | /en/whatsminer-firmware/install | "complete first-time installation guide" | Method 1 intro note | P1 |
| /en/whatsminer-firmware/update | /en/ams | "fleet-wide firmware updates via AMS" | Method 3 section | P1 |
| /en/whatsminer-firmware/update | /en/whatsminer-firmware/security | "verify firmware integrity before updating" | Pre-flight checklist section | P2 |
| /en/whatsminer-firmware/custom | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware product overview" | H2: What BiXBiT Custom Firmware Offers | P0 |
| /en/whatsminer-firmware/custom | /en/whatsminer-firmware/security | "firmware security deep-dive" | Security section inline link | P1 |
| /en/whatsminer-firmware/custom | /en/whatsminer-firmware/overclocking | "overclocking Whatsminer with custom firmware" | What Custom Firmware Enables section | P1 |
| /en/whatsminer-firmware/custom | /en/whatsminer-firmware/undervolting | "undervolting for electricity cost reduction" | What Custom Firmware Enables section | P1 |
| /en/whatsminer-firmware/custom | /en/whatsminer-firmware/autotuning | "per-chip autotuning on Whatsminer explained" | What Custom Firmware Enables section | P1 |
| /en/whatsminer-firmware/custom | /en/immersion-cooling | "immersion cooling for overclock deployments" | Custom firmware + immersion context | P2 |
| /en/whatsminer-firmware/whatsminer-m30s | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware overview" | Intro paragraph | P0 |
| /en/whatsminer-firmware/whatsminer-m30s | /en/whatsminer-firmware/install | "firmware installation guide" | Install section CTA | P1 |
| /en/whatsminer-firmware/whatsminer-m30s | /en/whatsminer-firmware/update | "firmware update guide" | Install section alternate link | P1 |
| /en/whatsminer-firmware/whatsminer-m30s | /en/whatsminer-firmware/whatsminer-m50 | "Whatsminer M50 firmware" | End of page — next-gen note | P2 |
| /en/whatsminer-firmware/whatsminer-m30s | /en/whatsminer-firmware/autotuning | "per-chip autotuning on M30S" | Performance section | P1 |
| /en/whatsminer-firmware/whatsminer-m30s | /en/whatsminer-firmware/undervolting | "undervolting the M30S for electricity savings" | Tuning modes section | P1 |
| /en/whatsminer-firmware/whatsminer-m30s | /en/ams | "manage M30S fleet in AMS" | Fleet management section | P1 |
| /en/whatsminer-firmware/whatsminer-m50 | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware overview" | Intro paragraph | P0 |
| /en/whatsminer-firmware/whatsminer-m50 | /en/whatsminer-firmware/whatsminer-m30s | "Whatsminer M30S firmware" | Intro or migration section | P2 |
| /en/whatsminer-firmware/whatsminer-m50 | /en/whatsminer-firmware/install | "firmware installation guide" | Install section CTA | P1 |
| /en/whatsminer-firmware/whatsminer-m50 | /en/whatsminer-firmware/autotuning | "per-chip autotuning" | Tuning section | P1 |
| /en/whatsminer-firmware/whatsminer-m50 | /en/ams | "mixed-fleet management in AMS" | Fleet section | P1 |
| /en/whatsminer-firmware/whatsminer-m50 | /en/immersion-cooling | "immersion cooling for M60 deployments" | Thermal section | P2 |
| /en/whatsminer-firmware/overclocking | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware overview" | Intro | P0 |
| /en/whatsminer-firmware/overclocking | /en/whatsminer-firmware/autotuning | "per-chip autotuning and overclock interaction" | Overclock profiles section | P1 |
| /en/whatsminer-firmware/overclocking | /en/whatsminer-firmware/undervolting | "undervolting as the alternative to overclocking" | Is overclocking right for you section | P2 |
| /en/whatsminer-firmware/overclocking | /en/immersion-cooling | "immersion cooling for sustained Whatsminer overclocking" | Thermal management section | P1 |
| /en/whatsminer-firmware/overclocking | /en/ams | "monitor overclocked Whatsminer fleet in AMS" | Post-configuration step | P1 |
| /en/whatsminer-firmware/autotuning | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware overview" | Intro | P0 |
| /en/whatsminer-firmware/autotuning | /en/whatsminer-firmware/overclocking | "overclocking vs autotuning on Whatsminer" | Comparison section | P1 |
| /en/whatsminer-firmware/autotuning | /en/whatsminer-firmware/undervolting | "undervolting via per-chip voltage control" | Voltage scaling section | P1 |
| /en/whatsminer-firmware/autotuning | /en/ams | "monitor autotuning results in AMS" | Fleet autotuning section | P1 |
| /en/whatsminer-firmware/undervolting | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | Intro | P0 |
| /en/whatsminer-firmware/undervolting | /en/whatsminer-firmware/autotuning | "per-chip autotuning enables precise undervolting" | How undervolting works section | P1 |
| /en/whatsminer-firmware/undervolting | /en/whatsminer-firmware/overclocking | "overclocking vs undervolting comparison" | Mode selection section | P2 |
| /en/whatsminer-firmware/undervolting | /en/immersion-cooling | "immersion cooling for extended undervolt headroom" | Immersion section | P2 |
| /en/whatsminer-firmware/undervolting | /en/ams | "monitor undervolted Whatsminer fleet in AMS" | Configuration step | P1 |
| /en/whatsminer-firmware/install | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware overview" | Intro | P0 |
| /en/whatsminer-firmware/install | /en/whatsminer-firmware/update | "updating existing BiXBiT installations" | Method 1 alternate reference | P1 |
| /en/whatsminer-firmware/install | /en/whatsminer-firmware/autotuning | "configure autotuning after install" | Post-installation configuration step | P1 |
| /en/whatsminer-firmware/install | /en/ams | "connect your Whatsminer fleet to AMS" | Post-installation step 4 | P1 |
| /en/whatsminer-firmware/install | /en/whatsminer-firmware/security | "checksum verification and firmware security" | Pre-installation checklist | P1 |
| /en/whatsminer-firmware/security | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware overview" | Intro | P0 |
| /en/whatsminer-firmware/security | /en/whatsminer-firmware/install | "firmware installation guide" | Distribution chain audit section | P1 |
| /en/whatsminer-firmware/security | /en/whatsminer-firmware/comparison | "full Whatsminer firmware comparison including security" | Questions to ask section | P1 |
| /en/whatsminer-firmware/security | /en/ams | "dev fee detection with AMS monitoring" | Dev fee detection section | P1 |
| /en/whatsminer-firmware/comparison | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware product page" | Intro and CTA | P0 |
| /en/whatsminer-firmware/comparison | /en/whatsminer-firmware/install | "install BiXBiT Whatsminer firmware" | End of page CTA | P1 |
| /en/whatsminer-firmware/comparison | /en/whatsminer-firmware/security | "Whatsminer firmware security comparison" | Security row in comparison table | P1 |
| /en/whatsminer-firmware/comparison | /en/ams | "AMS fleet management for Whatsminer" | Fleet management comparison section | P1 |

---

## Cross-Cluster Links (Whatsminer ↔ Antminer Firmware) *(v1, superseded)*

These links connect the two firmware clusters at points of genuine semantic overlap. They serve mixed-fleet operators and reinforce BiXBiT's authority across both ASIC platforms.

| Source Page | Target Page | Anchor Text | Context / Rationale | Priority |
|---|---|---|---|---|
| /en/whatsminer-firmware (pillar) | /en/antminer-firmware | "Antminer firmware" | Mixed-fleet section: "Supported Platforms" | P1 |
| /en/antminer-firmware (pillar) | /en/whatsminer-firmware | "Whatsminer firmware" | Mixed-fleet section: "Supported Platforms" | P1 |
| /en/whatsminer-firmware/comparison | /en/antminer-firmware/comparison | "Antminer firmware comparison" | End of page "Also see" — operators evaluating both platforms | P1 |
| /en/antminer-firmware/comparison | /en/whatsminer-firmware/comparison | "Whatsminer firmware comparison" | End of page "Also see" — operators evaluating both platforms | P1 |
| /en/whatsminer-firmware/security | /en/antminer-firmware/security | "Antminer firmware security guide" | Cross-platform security section | P2 |
| /en/antminer-firmware/security | /en/whatsminer-firmware/security | "Whatsminer firmware security guide" | Cross-platform security section | P2 |
| /en/whatsminer-firmware/autotuning | /en/antminer-firmware/autotuning | "Antminer per-chip autotuning" | Platform comparison section | P2 |
| /en/antminer-firmware/autotuning | /en/whatsminer-firmware/autotuning | "Whatsminer per-chip autotuning" | Platform comparison section | P2 |
| /en/whatsminer-firmware/install | /en/antminer-firmware/install | "Antminer firmware installation" | Mixed-fleet footer note | P2 |
| /en/antminer-firmware/install | /en/whatsminer-firmware/install | "Whatsminer firmware installation" | Mixed-fleet footer note | P2 |
| /en/whatsminer-firmware/undervolting | /en/antminer-firmware/undervolting | "Antminer undervolting guide" | Mixed-fleet cross-reference | P2 |
| /en/antminer-firmware/undervolting | /en/whatsminer-firmware/undervolting | "Whatsminer undervolting guide" | Mixed-fleet cross-reference | P2 |

---

## Cross-Cluster Links (Whatsminer Firmware → Other BiXBiT Products) *(v1, superseded)*

| Source Page | Target Page | Anchor Text | Rationale |
|---|---|---|---|
| /en/whatsminer-firmware (pillar) | /en/ams | "AMS monitoring dashboard" | Firmware + AMS are integrated products |
| /en/whatsminer-firmware/overclocking | /en/immersion-cooling | "immersion cooling for sustained Whatsminer overclock" | Overclock requires better cooling |
| /en/whatsminer-firmware/undervolting | /en/immersion-cooling | "immersion cooling extends undervolt headroom" | Thermal headroom enables deeper undervolting |
| /en/whatsminer-firmware/custom | /en/immersion-cooling | "custom firmware in immersion deployments" | Common operator upgrade path |
| /en/whatsminer-firmware/whatsminer-m50 | /en/immersion-cooling | "immersion cooling for M60 deployments" | M60 higher power density benefits from immersion |
| /en/ams | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | AMS pages should reference firmware product |
| /en/immersion-cooling | /en/whatsminer-firmware | "firmware optimized for immersion mining" | Cooling pages should reference firmware |

---

## Links TO Whatsminer Cluster FROM Existing Site Pages *(v1, superseded)*

| Existing Page | Add Link To | Anchor Text | Notes |
|---|---|---|---|
| Homepage | /en/whatsminer-firmware | "Whatsminer custom firmware" | Add alongside Antminer firmware in product navigation |
| /en/ams | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | AMS product page should mention Whatsminer firmware integration |
| /en/immersion-cooling | /en/whatsminer-firmware/overclocking | "firmware tuning for immersion overclock" | Cooling pages should link to firmware content |
| /en/antminer-firmware | /en/whatsminer-firmware | "Whatsminer firmware" | Mixed-fleet section on Antminer pillar |

---

## Immersion Cooling Cluster — Full Linking Matrix *(v1, superseded)*

### Pillar to Spokes

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| Homepage | /en/immersion-cooling-mining | "immersion cooling for Bitcoin mining" | Product ecosystem section alongside firmware cards | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/vs-air-cooling | "immersion vs air cooling comparison" | H2: Why Immersion Cooling section | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/single-phase | "single-phase immersion cooling" | H2: How It Works — system types | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/two-phase | "two-phase immersion cooling" | H2: How It Works — system types | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/antminer | "immersion cooling for Antminer" | H2: Supported ASIC Hardware | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/whatsminer | "immersion cooling for Whatsminer" | H2: Supported ASIC Hardware | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/roi | "immersion cooling ROI and TCO framework" | H2: TCO Comparison section | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/setup-guide | "ASIC immersion cooling setup guide" | H2: Implementation section | P0 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/tank | "immersion cooling tank specifications" | H2: System Configurations | P1 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/dielectric-fluid | "dielectric fluid selection guide" | H2: How It Works — fluid paragraph | P1 |
| /en/immersion-cooling-mining (pillar) | /en/immersion-cooling-mining/data-center | "immersion cooling for data center mining" | H2: System Configurations — scale tier | P1 |

### Spoke to Pillar (all spokes)

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| /en/immersion-cooling-mining/vs-air-cooling | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems" | Intro paragraph + end CTA | P0 |
| /en/immersion-cooling-mining/single-phase | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems overview" | Intro + end CTA | P0 |
| /en/immersion-cooling-mining/two-phase | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems" | Intro + end CTA | P0 |
| /en/immersion-cooling-mining/dielectric-fluid | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems" | Intro + end CTA | P0 |
| /en/immersion-cooling-mining/setup-guide | /en/immersion-cooling-mining | "BiXBiT immersion cooling system overview" | Intro | P0 |
| /en/immersion-cooling-mining/roi | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems" | Intro + end CTA | P0 |
| /en/immersion-cooling-mining/data-center | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems" | Intro + end CTA | P0 |
| /en/immersion-cooling-mining/antminer | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems overview" | Intro + end CTA | P0 |
| /en/immersion-cooling-mining/whatsminer | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems overview" | Intro + end CTA | P0 |
| /en/immersion-cooling-mining/tank | /en/immersion-cooling-mining | "BiXBiT immersion cooling systems overview" | Intro + end CTA | P0 |

### Spoke-to-Spoke Links

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| /en/immersion-cooling-mining/vs-air-cooling | /en/immersion-cooling-mining/roi | "immersion cooling ROI calculator" | TCO / cost comparison section | P1 |
| /en/immersion-cooling-mining/vs-air-cooling | /en/immersion-cooling-mining/single-phase | "single-phase immersion systems" | How Immersion Works section | P1 |
| /en/immersion-cooling-mining/vs-air-cooling | /en/immersion-cooling-mining/two-phase | "two-phase immersion cooling" | How Immersion Works section | P2 |
| /en/immersion-cooling-mining/single-phase | /en/immersion-cooling-mining/two-phase | "two-phase immersion cooling comparison" | Single vs Two-Phase H2 | P1 |
| /en/immersion-cooling-mining/single-phase | /en/immersion-cooling-mining/dielectric-fluid | "dielectric fluid selection guide" | Fluid Selection H2 | P1 |
| /en/immersion-cooling-mining/single-phase | /en/immersion-cooling-mining/antminer | "Antminer immersion cooling compatibility" | Compatible Hardware H2 | P1 |
| /en/immersion-cooling-mining/single-phase | /en/immersion-cooling-mining/whatsminer | "Whatsminer immersion cooling compatibility" | Compatible Hardware H2 | P1 |
| /en/immersion-cooling-mining/single-phase | /en/immersion-cooling-mining/setup-guide | "ASIC immersion cooling setup guide" | Installation H2 | P1 |
| /en/immersion-cooling-mining/two-phase | /en/immersion-cooling-mining/single-phase | "single-phase immersion cooling" | Comparison H2 | P1 |
| /en/immersion-cooling-mining/two-phase | /en/immersion-cooling-mining/dielectric-fluid | "two-phase dielectric fluid selection" | Fluid section | P1 |
| /en/immersion-cooling-mining/two-phase | /en/immersion-cooling-mining/antminer | "Antminer compatibility for two-phase immersion" | Hardware H2 | P1 |
| /en/immersion-cooling-mining/two-phase | /en/immersion-cooling-mining/whatsminer | "Whatsminer compatibility for two-phase immersion" | Hardware H2 | P1 |
| /en/immersion-cooling-mining/dielectric-fluid | /en/immersion-cooling-mining/single-phase | "single-phase immersion system configuration" | Single-phase H2 | P1 |
| /en/immersion-cooling-mining/dielectric-fluid | /en/immersion-cooling-mining/two-phase | "two-phase fluid applications" | Two-phase H2 | P2 |
| /en/immersion-cooling-mining/dielectric-fluid | /en/immersion-cooling-mining/setup-guide | "immersion cooling setup and fluid filling guide" | Handling section | P1 |
| /en/immersion-cooling-mining/setup-guide | /en/immersion-cooling-mining/dielectric-fluid | "dielectric fluid selection guide" | Step 2 — fluid fill | P1 |
| /en/immersion-cooling-mining/setup-guide | /en/immersion-cooling-mining/single-phase | "single-phase immersion cooling" | Intro context note | P1 |
| /en/immersion-cooling-mining/setup-guide | /en/immersion-cooling-mining/antminer | "Antminer immersion setup" | Step 3 — ASIC context | P1 |
| /en/immersion-cooling-mining/setup-guide | /en/immersion-cooling-mining/whatsminer | "Whatsminer immersion setup" | Step 3 — ASIC context | P1 |
| /en/immersion-cooling-mining/roi | /en/immersion-cooling-mining/vs-air-cooling | "immersion vs air cooling technical comparison" | PUE savings H2 | P1 |
| /en/immersion-cooling-mining/roi | /en/immersion-cooling-mining/setup-guide | "immersion cooling deployment guide" | End CTA | P2 |
| /en/immersion-cooling-mining/antminer | /en/immersion-cooling-mining/setup-guide | "full Antminer immersion setup guide" | Hardware Prep H2 | P1 |
| /en/immersion-cooling-mining/antminer | /en/immersion-cooling-mining/roi | "calculate your immersion cooling ROI" | Benchmarks H2 | P1 |
| /en/immersion-cooling-mining/whatsminer | /en/immersion-cooling-mining/setup-guide | "full Whatsminer immersion setup guide" | Hardware Prep H2 | P1 |
| /en/immersion-cooling-mining/whatsminer | /en/immersion-cooling-mining/roi | "calculate your immersion cooling ROI" | Benchmarks H2 | P1 |
| /en/immersion-cooling-mining/tank | /en/immersion-cooling-mining/single-phase | "single-phase immersion system design" | Tank specs H2 | P1 |
| /en/immersion-cooling-mining/tank | /en/immersion-cooling-mining/dielectric-fluid | "immersion cooling fluid selection" | Fluid section | P1 |
| /en/immersion-cooling-mining/tank | /en/immersion-cooling-mining/setup-guide | "installation guide for immersion tanks" | Ordering H2 | P1 |
| /en/immersion-cooling-mining/tank | /en/immersion-cooling-mining/roi | "total cost of ownership" | Secondary cooling H2 | P1 |
| /en/immersion-cooling-mining/tank | /en/immersion-cooling-mining/antminer | "Antminer immersion compatibility" | ASIC count table | P1 |
| /en/immersion-cooling-mining/tank | /en/immersion-cooling-mining/whatsminer | "Whatsminer immersion compatibility" | ASIC count table | P1 |
| /en/immersion-cooling-mining/data-center | /en/immersion-cooling-mining/roi | "immersion cooling TCO for data center scale" | PUE section | P1 |
| /en/immersion-cooling-mining/data-center | /en/immersion-cooling-mining/setup-guide | "ASIC immersion cooling setup guide" | Retrofit section | P1 |
| /en/immersion-cooling-mining/data-center | /en/immersion-cooling-mining/single-phase | "single-phase immersion cooling" | System specs section | P1 |

---

## Cross-Cluster Links: Immersion Cooling ↔ Antminer Firmware *(v1, superseded)*

| Source Page | Target Page | Anchor Text | Context / Rationale | Priority |
|---|---|---|---|---|
| /en/immersion-cooling-mining (pillar) | /en/antminer-firmware/overclocking | "immersion-optimized Antminer overclocking" | H2: Firmware Integration section | P0 |
| /en/immersion-cooling-mining (pillar) | /en/antminer-firmware | "BiXBiT Antminer firmware" | H2: Firmware Integration section | P0 |
| /en/immersion-cooling-mining (pillar) | /en/whatsminer-firmware/overclocking | "immersion-optimized Whatsminer overclocking" | H2: Firmware Integration section | P0 |
| /en/immersion-cooling-mining (pillar) | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | H2: Firmware Integration section | P0 |
| /en/immersion-cooling-mining (pillar) | /en/ams | "AMS fleet monitoring for immersion deployments" | H2: System Configurations section | P1 |
| /en/immersion-cooling-mining/antminer | /en/antminer-firmware | "BiXBiT Antminer firmware" | Firmware section | P0 |
| /en/immersion-cooling-mining/antminer | /en/antminer-firmware/overclocking | "Antminer overclocking in immersion" | Firmware section | P0 |
| /en/immersion-cooling-mining/antminer | /en/antminer-firmware/autotuning | "per-chip autotuning on Antminer" | Firmware section | P0 |
| /en/immersion-cooling-mining/antminer | /en/antminer-firmware/antminer-s19 | "Antminer S19 firmware guide" | Compatible models table | P1 |
| /en/immersion-cooling-mining/antminer | /en/antminer-firmware/antminer-s21 | "Antminer S21 firmware guide" | Compatible models table | P1 |
| /en/immersion-cooling-mining/antminer | /en/ams | "AMS fleet management" | Monitoring section | P1 |
| /en/immersion-cooling-mining/whatsminer | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | Firmware section | P0 |
| /en/immersion-cooling-mining/whatsminer | /en/whatsminer-firmware/overclocking | "Whatsminer overclocking in immersion" | Firmware section | P0 |
| /en/immersion-cooling-mining/whatsminer | /en/whatsminer-firmware/autotuning | "per-chip autotuning on Whatsminer" | Firmware section | P0 |
| /en/immersion-cooling-mining/whatsminer | /en/whatsminer-firmware/whatsminer-m30s | "Whatsminer M30S firmware guide" | Compatible models table | P1 |
| /en/immersion-cooling-mining/whatsminer | /en/whatsminer-firmware/whatsminer-m50 | "Whatsminer M50 and M60 firmware guide" | Compatible models table | P1 |
| /en/immersion-cooling-mining/whatsminer | /en/ams | "AMS fleet management" | Monitoring section | P1 |
| /en/immersion-cooling-mining/vs-air-cooling | /en/antminer-firmware/overclocking | "immersion-optimized Antminer overclocking" | Firmware Factor section | P1 |
| /en/immersion-cooling-mining/vs-air-cooling | /en/whatsminer-firmware/overclocking | "immersion-optimized Whatsminer overclocking" | Firmware Factor section | P1 |
| /en/immersion-cooling-mining/setup-guide | /en/antminer-firmware/install | "BiXBiT Antminer firmware installation guide" | Step 4 — firmware config | P0 |
| /en/immersion-cooling-mining/setup-guide | /en/whatsminer-firmware/install | "BiXBiT Whatsminer firmware installation guide" | Step 4 — firmware config | P0 |
| /en/immersion-cooling-mining/setup-guide | /en/antminer-firmware/autotuning | "per-chip autotuning setup" | Step 4 | P1 |
| /en/immersion-cooling-mining/setup-guide | /en/whatsminer-firmware/autotuning | "Whatsminer autotuning configuration" | Step 4 | P1 |
| /en/immersion-cooling-mining/setup-guide | /en/ams | "AMS fleet monitoring" | Step 5 | P1 |
| /en/immersion-cooling-mining/roi | /en/antminer-firmware/undervolting | "Antminer undervolting for J/TH reduction" | Firmware component H2 | P1 |
| /en/immersion-cooling-mining/roi | /en/whatsminer-firmware/undervolting | "Whatsminer undervolting efficiency gains" | Firmware component H2 | P1 |
| /en/immersion-cooling-mining/roi | /en/antminer-firmware | "BiXBiT Antminer firmware" | Worked example context | P1 |
| /en/immersion-cooling-mining/roi | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | Worked example context | P1 |
| /en/immersion-cooling-mining/single-phase | /en/antminer-firmware/autotuning | "per-chip autotuning with immersion thermal headroom" | Firmware section | P1 |
| /en/immersion-cooling-mining/single-phase | /en/whatsminer-firmware/autotuning | "Whatsminer autotuning in immersion deployments" | Firmware section | P1 |
| /en/immersion-cooling-mining/two-phase | /en/antminer-firmware/overclocking | "firmware overclock profiles for two-phase deployments" | Firmware H2 | P1 |
| /en/immersion-cooling-mining/two-phase | /en/whatsminer-firmware/overclocking | "Whatsminer overclocking in two-phase immersion" | Firmware H2 | P1 |
| /en/immersion-cooling-mining/data-center | /en/ams | "AMS fleet management for large immersion deployments" | Firmware integration H2 | P1 |
| /en/immersion-cooling-mining/data-center | /en/antminer-firmware | "BiXBiT Antminer firmware" | Firmware integration H2 | P1 |
| /en/immersion-cooling-mining/data-center | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | Firmware integration H2 | P1 |

### Firmware Clusters → Immersion Cooling (updated — replaces partial entries in earlier sections)

| Source Page | Target Page | Anchor Text | Context / Rationale | Priority |
|---|---|---|---|---|
| /en/antminer-firmware/overclocking | /en/immersion-cooling-mining | "immersion cooling for sustained overclocking" | Thermal management section | P1 |
| /en/antminer-firmware/undervolting | /en/immersion-cooling-mining | "immersion cooling extends undervolt headroom" | Thermal headroom section | P2 |
| /en/antminer-firmware/custom | /en/immersion-cooling-mining | "custom firmware for immersion deployments" | Immersion context | P2 |
| /en/antminer-firmware/antminer-s21 | /en/immersion-cooling-mining/antminer | "immersion cooling for Antminer S21" | Thermal / hardware section | P2 |
| /en/antminer-firmware/antminer-s19 | /en/immersion-cooling-mining/antminer | "Antminer S19 immersion cooling" | Thermal / hardware section | P2 |
| /en/whatsminer-firmware/overclocking | /en/immersion-cooling-mining | "immersion cooling for sustained Whatsminer overclocking" | Thermal management section | P1 |
| /en/whatsminer-firmware/undervolting | /en/immersion-cooling-mining | "immersion cooling extends Whatsminer undervolt headroom" | Thermal headroom section | P2 |
| /en/whatsminer-firmware/custom | /en/immersion-cooling-mining | "custom firmware in immersion deployments" | Immersion context | P2 |
| /en/whatsminer-firmware/whatsminer-m50 | /en/immersion-cooling-mining/whatsminer | "immersion cooling for Whatsminer M60" | Thermal / hardware section | P2 |
| /en/ams | /en/immersion-cooling-mining | "immersion cooling fleet monitoring" | AMS product page context | P2 |

---

## Fleet Monitoring / AMS Cluster — Full Linking Matrix *(v1, superseded)*

### Pillar to Spokes

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| Homepage | /en/ams | "ASIC fleet monitoring software" | Product ecosystem section alongside firmware and cooling | P0 |
| /en/ams (pillar) | /en/ams/vs-braiins-manager | "compare AMS with Braiins Manager" | H2: How AMS Compares — comparison table CTA | P0 |
| /en/ams (pillar) | /en/ams/vs-luxor-commander | "compare AMS with Luxor Commander" | H2: How AMS Compares — comparison table CTA | P0 |
| /en/ams (pillar) | /en/ams/vs-minerstat | "compare AMS with Minerstat" | H2: How AMS Compares — comparison table CTA | P0 |
| /en/ams (pillar) | /en/ams/mining-farm-monitoring-software | "how to choose mining farm monitoring software" | H2: Getting Started — pre-CTA resource link | P0 |
| /en/ams (pillar) | /en/ams/asic-fleet-management | "full ASIC fleet management technical guide" | H2: Getting Started — deep dive CTA | P0 |
| /en/ams (pillar) | /en/ams/antminer-monitoring-software | "AMS for Antminer fleets" | H2: Supported Hardware — Antminer section | P0 |
| /en/ams (pillar) | /en/ams/whatsminer-monitoring-software | "AMS for Whatsminer fleets" | H2: Supported Hardware — Whatsminer section | P0 |
| /en/ams (pillar) | /en/ams/mining-farm-alerts-automation | "alert and automation configuration guide" | H2: Core Capabilities — Alert System section | P1 |
| /en/ams (pillar) | /en/ams/mining-hosting-monitoring | "AMS for mining hosting operators" | H2: Who AMS Is Built For — Hosting section | P1 |
| /en/ams (pillar) | /en/ams/mining-farm-power-monitoring | "per-unit power consumption monitoring" | H2: Core Capabilities — Telemetry section | P2 |
| /en/ams (pillar) | /en/ams/mining-fleet-dashboard | "dashboard features and enterprise requirements" | H2: Core Capabilities — overview | P2 |

### Spoke to Pillar (all spokes link back)

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| /en/ams/vs-braiins-manager | /en/ams | "BiXBiT AMS overview" | Intro paragraph + end CTA | P0 |
| /en/ams/vs-luxor-commander | /en/ams | "BiXBiT AMS overview" | Intro paragraph + end CTA | P0 |
| /en/ams/vs-minerstat | /en/ams | "BiXBiT AMS overview" | Intro paragraph + end CTA | P0 |
| /en/ams/mining-farm-monitoring-software | /en/ams | "BiXBiT AMS: enterprise ASIC fleet monitoring" | H2: comparison section CTA | P0 |
| /en/ams/asic-fleet-management | /en/ams | "BiXBiT AMS fleet management platform" | Intro + end CTA | P0 |
| /en/ams/antminer-monitoring-software | /en/ams | "BiXBiT AMS overview" | Intro + end CTA | P0 |
| /en/ams/whatsminer-monitoring-software | /en/ams | "BiXBiT AMS overview" | Intro + end CTA | P0 |
| /en/ams/mining-farm-alerts-automation | /en/ams | "BiXBiT AMS alert system" | Intro + end CTA | P0 |
| /en/ams/mining-hosting-monitoring | /en/ams | "BiXBiT AMS overview" | Intro + end CTA | P0 |
| /en/ams/mining-farm-power-monitoring | /en/ams | "BiXBiT AMS fleet monitoring" | Intro + end CTA | P0 |
| /en/ams/mining-fleet-dashboard | /en/ams | "BiXBiT AMS" | Intro + end CTA | P0 |

### Spoke-to-Spoke Links

| Source Page | Target Page | Anchor Text | Context / Placement | Priority |
|---|---|---|---|---|
| /en/ams/vs-braiins-manager | /en/ams/vs-luxor-commander | "AMS vs Luxor Commander" | End of page — "Also compare" | P1 |
| /en/ams/vs-braiins-manager | /en/ams/vs-minerstat | "AMS vs Minerstat" | End of page — "Also compare" | P1 |
| /en/ams/vs-braiins-manager | /en/ams/whatsminer-monitoring-software | "Whatsminer monitoring — why Braiins Manager falls short" | H2: Whatsminer gap section | P0 |
| /en/ams/vs-luxor-commander | /en/ams/vs-braiins-manager | "AMS vs Braiins Manager" | End of page — "Also compare" | P1 |
| /en/ams/vs-luxor-commander | /en/ams/vs-minerstat | "AMS vs Minerstat" | End of page — "Also compare" | P1 |
| /en/ams/vs-minerstat | /en/ams/vs-braiins-manager | "AMS vs Braiins Manager" | End of page — "Also compare" | P1 |
| /en/ams/vs-minerstat | /en/ams/asic-fleet-management | "ASIC fleet management guide" | H2: feature depth section | P1 |
| /en/ams/mining-farm-monitoring-software | /en/ams/vs-braiins-manager | "AMS vs Braiins Manager comparison" | H2: decision framework — comparison CTA | P0 |
| /en/ams/mining-farm-monitoring-software | /en/ams/vs-luxor-commander | "AMS vs Luxor Commander comparison" | H2: decision framework | P1 |
| /en/ams/mining-farm-monitoring-software | /en/ams/vs-minerstat | "AMS vs Minerstat comparison" | H2: decision framework | P1 |
| /en/ams/mining-farm-monitoring-software | /en/ams/asic-fleet-management | "ASIC fleet management technical guide" | H2: methodology section | P1 |
| /en/ams/mining-farm-monitoring-software | /en/ams/antminer-monitoring-software | "monitoring Antminer fleets with AMS" | H2: hardware type section | P1 |
| /en/ams/mining-farm-monitoring-software | /en/ams/whatsminer-monitoring-software | "monitoring Whatsminer fleets with AMS" | H2: hardware type section | P1 |
| /en/ams/asic-fleet-management | /en/ams/mining-farm-monitoring-software | "how to choose monitoring software" | H2: tools section | P1 |
| /en/ams/asic-fleet-management | /en/ams/mining-farm-alerts-automation | "alert design and automation in detail" | H2: alert section | P0 |
| /en/ams/asic-fleet-management | /en/ams/antminer-monitoring-software | "Antminer fleet management with AMS" | H2: mixed-fleet section | P1 |
| /en/ams/asic-fleet-management | /en/ams/whatsminer-monitoring-software | "Whatsminer fleet management with AMS" | H2: mixed-fleet section | P1 |
| /en/ams/asic-fleet-management | /en/ams/mining-hosting-monitoring | "hosting operator fleet management" | H2: scale section | P1 |
| /en/ams/antminer-monitoring-software | /en/ams/whatsminer-monitoring-software | "add Whatsminer units to the same dashboard" | H2: mixed-fleet note | P1 |
| /en/ams/antminer-monitoring-software | /en/ams/vs-braiins-manager | "AMS vs Braiins Manager for Antminer fleets" | H2: comparison section | P1 |
| /en/ams/whatsminer-monitoring-software | /en/ams/antminer-monitoring-software | "add Antminer units to the same dashboard" | H2: mixed-fleet note | P1 |
| /en/ams/whatsminer-monitoring-software | /en/ams/vs-braiins-manager | "why Braiins Manager doesn't cover Whatsminer" | H2: Braiins gap section | P0 |
| /en/ams/whatsminer-monitoring-software | /en/ams/asic-fleet-management | "full mixed-fleet management guide" | H2: mixed-fleet section | P1 |
| /en/ams/mining-farm-alerts-automation | /en/ams/asic-fleet-management | "full fleet management guide" | Intro context link | P1 |
| /en/ams/mining-farm-alerts-automation | /en/ams/antminer-monitoring-software | "Antminer alert configuration" | H2: per-model section | P1 |
| /en/ams/mining-farm-alerts-automation | /en/ams/whatsminer-monitoring-software | "Whatsminer alert configuration" | H2: per-model section | P1 |
| /en/ams/mining-hosting-monitoring | /en/ams/asic-fleet-management | "technical fleet management guide" | Intro resource link | P1 |
| /en/ams/mining-hosting-monitoring | /en/ams/antminer-monitoring-software | "Antminer client fleet monitoring" | H2: hardware section | P1 |
| /en/ams/mining-hosting-monitoring | /en/ams/whatsminer-monitoring-software | "Whatsminer client fleet monitoring" | H2: hardware section | P1 |
| /en/ams/mining-hosting-monitoring | /en/ams/mining-farm-alerts-automation | "alert configuration for multi-client operations" | H2: operations section | P1 |
| /en/ams/mining-hosting-monitoring | /en/ams/mining-farm-power-monitoring | "per-unit power tracking for billing" | H2: billing section | P1 |
| /en/ams/mining-farm-power-monitoring | /en/ams/asic-fleet-management | "fleet management guide" | Intro resource link | P1 |
| /en/ams/mining-farm-power-monitoring | /en/ams/mining-hosting-monitoring | "per-client power tracking for billing" | H2: hosting section | P1 |
| /en/ams/mining-fleet-dashboard | /en/ams/asic-fleet-management | "fleet management methodology" | H2: operational context | P1 |
| /en/ams/mining-fleet-dashboard | /en/ams/mining-farm-alerts-automation | "alert configuration" | H2: alerts section | P1 |
| /en/ams/mining-fleet-dashboard | /en/ams/mining-hosting-monitoring | "multi-client dashboard views" | H2: enterprise features section | P1 |

---

## Cross-Cluster Links: AMS (Fleet Monitoring) ↔ Antminer Firmware *(v1, superseded)*

| Source Page | Target Page | Anchor Text | Context / Rationale | Priority |
|---|---|---|---|---|
| /en/ams (pillar) | /en/antminer-firmware | "BiXBiT Antminer firmware" | H2: AMS + BiXBiT Firmware — integrated stack section | P0 |
| /en/ams (pillar) | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | H2: AMS + BiXBiT Firmware — integrated stack section | P0 |
| /en/ams/antminer-monitoring-software | /en/antminer-firmware | "BiXBiT Antminer firmware" | H2: firmware integration section | P0 |
| /en/ams/antminer-monitoring-software | /en/antminer-firmware/install | "install BiXBiT firmware before connecting to AMS" | H2: setup steps — Step 1 | P0 |
| /en/ams/antminer-monitoring-software | /en/antminer-firmware/autotuning | "autotuning results visible in AMS" | H2: telemetry section | P1 |
| /en/ams/antminer-monitoring-software | /en/antminer-firmware/overclocking | "alert setup for overclocked Antminer" | H2: alert configuration section | P1 |
| /en/ams/antminer-monitoring-software | /en/antminer-firmware/update | "firmware update via AMS" | H2: AMS + firmware stack section | P1 |
| /en/ams/whatsminer-monitoring-software | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | H2: firmware integration section | P0 |
| /en/ams/whatsminer-monitoring-software | /en/whatsminer-firmware/install | "install Whatsminer firmware before connecting to AMS" | H2: setup steps — Step 1 | P0 |
| /en/ams/whatsminer-monitoring-software | /en/whatsminer-firmware/autotuning | "autotuning results in AMS" | H2: telemetry section | P1 |
| /en/ams/whatsminer-monitoring-software | /en/whatsminer-firmware/undervolting | "undervolting telemetry in AMS" | H2: telemetry section | P1 |
| /en/ams/whatsminer-monitoring-software | /en/whatsminer-firmware/update | "firmware updates via AMS" | H2: AMS + firmware stack section | P1 |
| /en/ams/vs-braiins-manager | /en/antminer-firmware/comparison | "BiXBiT vs Braiins OS+ firmware comparison" | H2: firmware comparison section | P1 |
| /en/ams/vs-braiins-manager | /en/antminer-firmware | "BiXBiT Antminer firmware" | H2: firmware integration section | P1 |
| /en/ams/vs-braiins-manager | /en/whatsminer-firmware | "BiXBiT Whatsminer firmware" | H2: firmware section | P1 |
| /en/ams/mining-farm-alerts-automation | /en/antminer-firmware/overclocking | "reset alert baselines after overclocking Antminer" | H2: threshold configuration section | P1 |
| /en/ams/mining-farm-alerts-automation | /en/whatsminer-firmware/overclocking | "reset alert baselines after overclocking Whatsminer" | H2: threshold configuration section | P1 |
| /en/ams/mining-farm-power-monitoring | /en/antminer-firmware/undervolting | "undervolting Antminer to reduce J/TH" | H2: optimization actions section | P1 |
| /en/ams/mining-farm-power-monitoring | /en/whatsminer-firmware/undervolting | "undervolting Whatsminer to reduce J/TH" | H2: optimization actions section | P1 |
| /en/ams/asic-fleet-management | /en/antminer-firmware/update | "Antminer firmware update guide" | H2: firmware management section | P1 |
| /en/ams/asic-fleet-management | /en/whatsminer-firmware/update | "Whatsminer firmware update guide" | H2: firmware management section | P1 |

### Firmware Clusters → AMS (updated — replaces earlier partial entries across the matrix above)

These entries confirm that existing firmware spoke pages already have AMS cross-links defined. No new entries needed — verify against the Antminer and Whatsminer sections above.

Key confirmed cross-links (firmware → AMS):
- All Antminer firmware spokes with "monitor in AMS" links → `/en/ams` (confirmed in Antminer section)
- All Whatsminer firmware spokes with "monitor in AMS" links → `/en/ams` (confirmed in Whatsminer section)
- New target: firmware spokes should now link to **specific AMS spokes** (not just the pillar) where contextually appropriate:
  - `/en/antminer-firmware/overclocking` → `/en/ams/mining-farm-alerts-automation` — "configure AMS alerts for overclocked fleet" (upgrade from generic AMS link) — P1
  - `/en/antminer-firmware/undervolting` → `/en/ams/mining-farm-power-monitoring` — "track J/TH improvement in AMS power monitoring" — P1
  - `/en/whatsminer-firmware/overclocking` → `/en/ams/mining-farm-alerts-automation` — "configure AMS alerts for overclocked Whatsminer" — P1
  - `/en/whatsminer-firmware/undervolting` → `/en/ams/mining-farm-power-monitoring` — "track undervolting results in AMS" — P1

---

## Cross-Cluster Links: AMS ↔ Immersion Cooling *(v1, superseded)*

| Source Page | Target Page | Anchor Text | Context / Rationale | Priority |
|---|---|---|---|---|
| /en/ams/mining-farm-alerts-automation | /en/immersion-cooling-mining | "immersion deployments require different alert thresholds" | H2: threshold configuration section | P1 |
| /en/ams/antminer-monitoring-software | /en/immersion-cooling-mining | "Antminer in immersion: different monitoring baselines" | H2: alert config — immersion note | P2 |
| /en/ams/whatsminer-monitoring-software | /en/immersion-cooling-mining/whatsminer | "Whatsminer immersion: different monitoring baselines" | H2: alert config — immersion note | P2 |
| /en/immersion-cooling-mining (pillar) | /en/ams | "AMS fleet monitoring for immersion deployments" | H2: System Configurations section | P1 (already in matrix) |
| /en/immersion-cooling-mining/setup-guide | /en/ams | "AMS fleet monitoring" | Step 5 | P1 (already in matrix) |
| /en/immersion-cooling-mining/data-center | /en/ams | "AMS fleet management for large immersion deployments" | Firmware integration H2 | P1 (already in matrix) |

---

## Links TO AMS Cluster FROM Existing Site Pages *(v1, superseded)*

| Existing Page | Add Link To | Anchor Text | Notes |
|---|---|---|---|
| Homepage | /en/ams | "ASIC fleet monitoring" | Add to product navigation alongside firmware and cooling |
| /en/antminer-firmware | /en/ams | "AMS monitoring dashboard" | Already in matrix — confirm it exists on live page |
| /en/whatsminer-firmware | /en/ams | "AMS monitoring dashboard" | Already in matrix — confirm it exists on live page |
| /en/immersion-cooling-mining | /en/ams | "AMS fleet monitoring" | Already in matrix — confirm it exists on live page |
| /en/antminer-firmware/install | /en/ams/antminer-monitoring-software | "connect to AMS after installation" | Update existing AMS link to point to specific spoke |
| /en/whatsminer-firmware/install | /en/ams/whatsminer-monitoring-software | "connect your Whatsminer fleet to AMS" | Update existing AMS link to point to specific spoke |
