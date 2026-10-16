# Content Brief: Hydro Cooling Systems for ASIC Mining (Sub-Hub + Hydro Products)
**Slug:** `/en/asics-cooling/hydro-systems` (existing sub-hub). Also covers `/en/products/container-hydro`, `/en/products/rack-hydro` and the 6 model pages as linked sections.
**Cluster:** hardware (`content/clusters/hardware.md`)
**Brief type:** Sub-hub (commercial) + satellite product pages
**Created:** 2026-09-28
**Author assignment:** Hydro systems engineer [VERIFY: assign real author/reviewer name]

**Priority:** P0. Hydro has no owner in the existing clusters, and the sub-hub is the best-engaged hardware landing (GA4 28 days: 13 organic sessions, 11 engaged; highest among hardware pages). GSC: 688 impressions, 8 clicks, position 20.4. Demand (US): `mining water cooling` 90 (#27), `hydro miner` 90 (CPC $1.53), `antminer s21 hydro` 90 (CPC $1.65), `hydro cooling system` 40 at **CPC $6.42** (#29 via `rack-hydro`), `hydro rack` 40 (#16), `hydro container` 20, `hydro mining container` 10 (CPC $2.69). Quick wins in GSC: `whatsminer hydro container` 6.6, `hydro mining container` 8.8, `hydro mining rack` 10.3, `hydro container` 13.3.
**Target (architecture v2):** `/en/asics-cooling/hydro-systems` (existing). Architecture v2 lists it only as a link target (C2, C10); this brief adds its content. `container-hydro` and `rack-hydro` stay as separate product URLs (P1). No new slugs.

---

## Page Goal

Be the page an operator lands on when evaluating hydro (liquid-to-chip) cooling for Antminer/Whatsminer hydro miners: explain the loop, show the product line (racks → containers → skid), show what the site needs, and route to the right model page. Conversion: quote / project review.

## Search Intent

**Primary:** commercial investigation: "hydro cooling system for mining", "mining water cooling", "hydro miner" setups.
**Secondary:** navigational to models (WHR-200-2U, AHR-200, WHC-*, AHC-2.4, HW-Cluster-2.4).
**Do NOT optimize for:** PC/consumer "hydro cooling" (260/mo, mostly CPU coolers, Corsair, cooling mats), `dry cooler` 880 (generic HVAC), buying hydro miners themselves (`antminer s21 hydro` as a miner purchase; we cover it as "which hydro miners our systems support").

**SERP `hydro cooling asic miner` (2026-09-28, volatile):** miner listings (Bitaxe hydro, Antminer S21/S23 Hydro on Alibaba, Newegg, Amazon), news, Reddit, YouTube how-to ("hook the Antminer S23 Hydro to a chiller"). Almost no farm-scale vendor pages: the gap is a clear system page. PAA: "Is there a water-cooled Bitcoin miner available?", "How much does a Hydro Bitcoin miner cost?".

---

## Target Keywords

> Volumes: DataForSEO Google Ads / Labs, US / en, 2026-09-28. `#N`: DataForSEO ranked_keywords 2026-09-25. GSC: average position, all countries, 28 days.

| Type | Keyword | Vol (US) | CPC | KD | BiXBiT pos | URL |
|---|---|---|---|---|---|---|
| Primary | `mining water cooling` | 90 | — | n/d | #27 | hydro-systems |
| Secondary | `hydro cooling system` | 40 | $6.42 | n/d | #29 (rack-hydro); GSC 27.6 hydro-systems | hydro-systems (move from rack-hydro) |
| Secondary | `hydro miner` | 90 | $1.53 | n/d | — | hydro-systems (section "Supported hydro miners") |
| Secondary | `antminer s21 hydro` | 90 | $1.65 | n/d | — | hydro-systems section → AHR-200 |
| Secondary | `asic hydro cooling` / `hydro cooling asic` | 10 / n/d | — | n/d | GSC 32.4 / 12.3 (rack-hydro) | hydro-systems |
| Secondary | `whatsminer hydro` / `whatsminer hydro cooling` | 10 / n/d | $1.42 | n/d | #18 (container-hydro); GSC 17.9 | hydro-systems |
| Secondary | `antminer hydro` | 20 | $1.39 | n/d | — | hydro-systems |
| Long-tail | `crypto mining cooling systems`, `mining cooling solutions` | n/d / 10 | — | — | GSC 37.1 / 28.2 | hub `/en/asics-cooling` (not here) |
| Satellite | `hydro container`, `hydro mining container`, `whatsminer hydro container`, `hydro cooled container` | 20 / 10 / n/d / n/d | — / $2.69 | — | GSC 13.3 / 8.8 / 6.6 / 39.3 | `/en/products/container-hydro` |
| Satellite | `hydro rack`, `hydro mining rack` | 40 / n/d | $1.53 | 8 | #16 / GSC 10.3 | `/en/products/rack-hydro` |

Cannibalization (GSC): `hydro container` 78% container-hydro / 22% hydro-systems; `hydro mining rack` rack-hydro 45% / hydro-systems 34% / rack 21%; `hydro cooling system` rack-hydro 61% (pos 54) / hydro-systems 39% (pos 27.6). Rule: category terms (`hydro cooling system`, `mining water cooling`) → sub-hub; `hydro container*` → container-hydro; `hydro rack*` → rack-hydro. Titles and anchors follow this split.

---

## H1

Hydro Cooling Systems for Antminer and Whatsminer Hydro Miners

(Title: "Hydro Cooling for ASIC Mining: Racks & Containers | BiXBiT", see `hardware-product-title-template.md`.)

---

## Page Structure (the live page already has most H2s; extend, do not rebuild)

### Intro (40–60 words, AIO-ready)
What hydro cooling is for ASIC mining: coolant runs through cold plates inside hydro miners, heat goes to a dry cooler or heat-reuse loop; BiXBiT supplies racks, containers and skid systems plus monitoring [VERIFY wording].

### H2: Hydro Racks Product Line (exists)
- H3 cards WHR-200-2U, AHR-200 → crawlable links; one line each: which miners, what is included [VERIFY]. Live pages state "200kW module for Whatsminer" and "36 Antminer S21 Hydro" [VERIFY both].
- Link to `/en/products/rack-hydro` as a separate product [VERIFY relation: previous generation or different format].

### H2: Hydro Containers Product Line (exists)
- H3 cards WHC-1.2-2U, WHC-2.4-2U, HW-Cluster-2.4, AHC-2.4 → crawlable links; one line each [VERIFY]. Note: the WHC-1.2-2U page intro currently says "immersion" [VERIFY].
- Link to `/en/products/container-hydro` [VERIFY relation].
- **New:** comparison table across the 6 models + 2 legacy products: format (rack / container / skid), miner family, capacity, heat rejection, indoor/outdoor. **All values [VERIFY]** from spec sheets. This table is the main citable asset for AI answers.

### H2: Supported Hydro Miners (new)
- Which Antminer Hydro (e.g. S21 Hydro, per AHR-200 page) and Whatsminer hydro series (e.g. M53/M63 family) each system supports [VERIFY list].
- Firmware: BiXBiT firmware profiles for hydro miners [VERIFY which models are supported] → links `/en/firmwares/antminer` (S21 Hydro section, fragment [VERIFY with dev]) and `/en/firmwares/whatsminer-series-m6x` / `-m5x`.
- Answers PAA "Is there a water-cooled Bitcoin miner available?" in 2–3 sentences, without prices of miners.

### H2: How Hydro Cooling Works (exists)
Keep the four steps; add one diagram with real components (miner cold plate → manifold → pump/CDU → dry cooler → return) [VERIFY component names]. Coolant type used in the loop [VERIFY]; not the dielectric immersion fluid.

### H2: Hydro vs Immersion vs Air (new, short)
3-row table: where each fits (climate, density, maintenance, noise), no invented numbers. Link `/en/asics-cooling/immersion-systems` (C10) and the planned blog EN-JAN-1. Keep it short: the full comparison belongs to the blog post and the hub.

### H2: Site Requirements (new)
Power (link `/en/products/pdu`), water/glycol fill and make-up, dry cooler placement, ambient range, network for AMS [VERIFY each value].

### H2: Heat Reuse (exists)
Keep; add only verified project examples [VERIFY]. No profitability or payback claims.

### H2: Monitoring with AMS (exists as "BiXBiT AMS — Your Central Hub…")
Which loop telemetry is visible (supply/return temperature, flow, pump status) [VERIFY], link `/en/ams`.

### H2: Engineering and Project Design Services (exists)
Keep; add the deployment steps list [VERIFY].

### H2: FAQ (new)

---

## Satellite pages (P1, in the same sprint)

### `/en/products/container-hydro`
- Title: "Hydro Mining Container for Whatsminer | BiXBiT"; H1 "BiXBiT Hydro Mining Container".
- Keep current content; verify description claims ("up to 160 Whatsminer units", "1.6 MW") [VERIFY]; add a short "compare with WHC-2.4-2U / AHC-2.4" block with links; FAQ 3 questions (capacity, heat rejection, monitoring) [VERIFY].
- Target: `hydro container`, `hydro mining container`, `whatsminer hydro container`.

### `/en/products/rack-hydro`
- Title: "Hydro Mining Rack: Water-Cooled ASIC Rack | BiXBiT" (fixes "ASIC Minings"). H1 "BiXBiT Hydro Mining Rack".
- Verify description claims ("cools up to 12 ASIC miners", "10 kW each", "leak protection") [VERIFY]; add links to WHR-200-2U / AHR-200 and the sub-hub; hand the `hydro cooling system` phrase to the sub-hub (remove it from this title/H1).
- Target: `hydro rack`, `hydro mining rack`.

### 6 model pages
Template only (title/description/H1/Product schema): `hardware-product-title-template.md`. Each adds 3 links: sub-hub, sibling in the same line, `/en/ams`. Copy beyond that is P2.

---

## Key Entities and Terms to Include

hydro cooling, liquid cooling, direct-to-chip, cold plate, hydro miner, Antminer S21 Hydro, Whatsminer hydro (M-series hydro variants), coolant loop, manifold, CDU, pump, dry cooler, glycol, supply/return temperature, flow rate, heat reuse, skid-mounted, 40 ft container, power distribution, PDU, AMS, J/TH, hashrate stability.

---

## FAQ (5–7 questions)

1. **What is hydro cooling for ASIC miners?** 40–60 words.
2. **Which miners work with BiXBiT hydro systems?** [VERIFY list].
3. **Hydro or immersion: which is better for my site?** Short, conditional answer + links.
4. **What does the site need for a hydro container (power, water, space)?** [VERIFY].
5. **Can the waste heat be reused?** [VERIFY verified use cases].
6. **How is a hydro system monitored?** AMS [VERIFY telemetry].
7. **Does BiXBiT firmware support hydro miners?** [VERIFY models]; link firmware pages.

---

## E-E-A-T Signals

- Named hydro engineer/reviewer; spec-sheet versions dated [VERIFY].
- Real installation photos with descriptive alt text.
- If allowed, one short project reference (the hub timeline mentions a "Hydro Container" stage and cooperation with Cormint) [VERIFY what may be published].

## Internal Links

Out: 6 model pages, `/en/products/container-hydro`, `/en/products/rack-hydro`, `/en/asics-cooling/immersion-systems`, `/en/asics-cooling`, `/en/products/pdu`, `/en/ams`, `/en/firmwares/antminer` (S21 Hydro), `/en/firmwares/whatsminer-series-m6x`.
In: `/en/asics-cooling` (C2), `/en/products/container`, blog posts (EN-JAN-1, EN-FEB-3, EN-NOV-1/2, EN-MAY-2, `hydro-asic-2026-ranking-models-for-largescale-mining-farms`, `bitmain-releases-t19-hydro-…`). Full list: `content/internal-linking.md` → Hardware.

## Schema Recommendation

Sub-hub: `CollectionPage` (or `WebPage`) + `ItemList` of the 6 models (+ 2 legacy products) + `BreadcrumbList`; `FAQPage` only with visible FAQ. Today only WebSite + Organization are present. Model pages: `Product` (template brief).

## Word Count Target

1 500–1 900 words (currently ~1 180). Growth comes from the comparison table, supported-miners section and FAQ.

## [VERIFY] Blockers — DO NOT PUBLISH WITHOUT RESOLVING

1. Capacity and compatibility figures for all 6 models and 2 legacy products.
2. Relationship between legacy (`container-hydro`, `rack-hydro`) and new models: current, previous generation, or different format.
3. WHC-1.2-2U product type (hydro vs immersion).
4. Supported hydro miners and firmware support per model.
5. Loop coolant type, dry cooler specs, ambient range.
6. Telemetry exposed in AMS for hydro loops.
7. Publishable project references.
