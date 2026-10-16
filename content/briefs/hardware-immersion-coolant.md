# Content Brief: BiXBiT Coolant — Dielectric Immersion Cooling Fluid for ASIC Miners
**Slug:** `/en/products/coolant` (existing)
**Cluster:** hardware (`content/clusters/hardware.md`); informational side lives in the immersion cluster (`immersion-cooling-dielectric-fluid.md` → refresh of `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining`)
**Brief type:** Product page refresh (transactional)
**Created:** 2026-09-28
**Author assignment:** Chemist / fluids engineer who owns the BiXBiT formula [VERIFY: assign real name]

**Priority:** P1. High commercial value per click: `immersion cooling fluid` 110/mo (CPC **$7.11**, KD 9), `dielectric fluid for immersion cooling` 70 (CPC **$7.60**, KD 2), `dielectric coolant` 170 (CPC $3.38), `immersion cooling fluid price` 20 (CPC $3.18), `immersion cooling oil` 10 (CPC $23.57). BiXBiT is outside the quick-win band: page GSC position 26.8 (140 impressions, 5 clicks; best CTR among hardware pages, 3.6%); `mining coolants` 25.8. Not P0 because the position is >20 and the SERP is held by fluid manufacturers (Shell, Castrol, 3M, ExxonMobil, Engineered Fluids).
**Target (architecture v2):** `/en/products/coolant` (existing page). Hardware extension; no new slug.

---

## Page Goal

Sell BiXBiT coolant to operators who already run or plan immersion, by stating what the fluid is, which data sheet values it has, how it compares to mineral oil and engineered fluids, and how to buy/replace it. Conversion: quote / order request.

## Search Intent

**Primary:** transactional: buy immersion cooling fluid / dielectric coolant for ASIC immersion.
**Secondary:** commercial comparison: our fluid vs mineral oil vs branded fluids; price per liter drivers.
**Do NOT optimize for:** "what is mineral oil immersion", "antminer in mineral oil" (BiXBiT is #1–2 there with the blog post; keep them there), 3M/Novec brand queries (the existing post `novec-and-coolant-liquids-comparison-why-we-stick-to-our-own-formula` covers the comparison story, GSC pos 8.5).

---

## Target Keywords

> Volumes: DataForSEO Google Ads / Labs, US / en, 2026-09-28. GSC: average position, all countries, 28 days.

| Type | Keyword | Vol (US) | CPC | KD | BiXBiT pos |
|---|---|---|---|---|---|
| Primary | `immersion cooling fluid` | 110 | $7.11 | 9 | — |
| Secondary | `dielectric fluid for immersion cooling` | 70 | $7.60 | 2 | — |
| Secondary | `dielectric coolant` | 170 | $3.38 | n/d | — |
| Secondary | `immersion cooling fluid price` | 20 | $3.18 | n/d | — |
| Secondary | `mining coolant` / `mining coolants` | 10 / 10 | — | n/d | GSC 23 / 25.8 |
| Long-tail | `single phase immersion cooling fluid`, `dielectric fluid immersion cooling` | 10 / 10 | — / $11.35 | n/d | — |
| Long-tail | `immersion cooling oil` | 10 | $23.57 | n/d | — |

Cannibalization: `mining coolants` (26 impr): coolant 54% (pos 25.8) vs mineral oil post 46% (pos 53.2). `asic immersion cooling` also leaks here (pos 73): not a target for this page.

---

## H1

BiXBiT Coolant: Dielectric Immersion Cooling Fluid for ASIC Miners

**Fix:** the live H1 "BiXBiT Сoolant" contains a Cyrillic "С" (U+0421). Replace with Latin "C" everywhere on the page (H1, alt texts, schema `name`).

(Title: "Immersion Cooling Fluid for ASIC Miners | BiXBiT"; see `hardware-product-title-template.md`.)

## Meta description (draft)

BiXBiT dielectric immersion cooling fluid for Antminer and Whatsminer [VERIFY]: data sheet, compatibility and fill volumes per tank, rack and container. Request a quote. (≈150 chars; replaces "Non-toxic… Eliminates heat & noise. Saves electricity", which needs a source [VERIFY].)

---

## Page Structure

### Above the fold
What the fluid is (base type: synthetic / hydrocarbon / other [VERIFY]), single-phase use, for which BiXBiT systems. CTAs: quote, safety/technical data sheet download [VERIFY SDS/TDS availability].

### H2: Technical Data
Table from the TDS only: dielectric strength, flash point, pour point, kinematic viscosity at operating temperature, density, thermal conductivity, specific heat, pack sizes. **Every value [VERIFY]**. No value from memory or competitors.

### H2: BiXBiT Coolant vs Mineral Oil vs Engineered Fluids
Comparison on criteria, not on numbers we do not have: base type, material compatibility, evaporation, odor, maintenance, availability, cost drivers. Mark BiXBiT cells [VERIFY]. Link the mineral oil post for the full story (anchor: "mineral oil vs synthetic immersion fluids") and the Novec comparison post.

### H2: Compatibility
- Miner families tested [VERIFY: which Antminer/Whatsminer models, any prep steps such as fan removal].
- Materials: seals, cables, thermal paste considerations [VERIFY].
- Systems: Cell, Rack, Container, Container-1K, ICT-100, IC-1000 (links) with fill volume per system [VERIFY].

### H2: How Much Coolant Do You Need
Explain the calculation inputs (tank volume, displacement by miners, reserve for top-up) and give per-system fill volumes only from the spec sheets [VERIFY]. This answers `immersion cooling fluid price` intent via volume × price-per-liter drivers without inventing a price.

### H2: Maintenance and Replacement
Testing, filtration, top-up schedule [VERIFY with engineering]; link planned blog EN-MAR-2 "Immersion Fluid Maintenance" when published.

### H2: Safety, Storage and Shipping
Handling, storage, disposal, shipping classification [VERIFY from SDS]. No health or environmental claims ("non-toxic", "eco-friendly") without SDS backing.

### H2: FAQ

---

## Key Entities and Terms to Include

dielectric fluid, single-phase immersion, synthetic fluid, mineral oil, engineered fluid, dielectric strength, flash point, viscosity, thermal conductivity, SDS/TDS, top-up, filtration, material compatibility, Antminer, Whatsminer, immersion tank, immersion container.

---

## FAQ (5–6 questions)

1. **What is dielectric immersion cooling fluid?** 40–60 words.
2. **Is BiXBiT coolant compatible with Antminer and Whatsminer?** [VERIFY tested models].
3. **How much fluid does a tank / rack / container need?** [VERIFY per system].
4. **How often should the fluid be tested or replaced?** [VERIFY].
5. **Can I use mineral oil instead?** Neutral trade-offs + link to the mineral oil post.
6. **How is the fluid shipped and stored?** [VERIFY from SDS].

---

## E-E-A-T Signals

- Named fluids engineer; TDS/SDS downloadable and dated [VERIFY].
- Lab test references (in-house or third-party) only if they exist [VERIFY].
- Link to the two existing expert posts (mineral oil guide, Novec comparison) as supporting evidence.

## Internal Links

Out: `/en/products/cell`, `/en/products/rack`, `/en/products/container`, `/en/products/container-1k`, `/en/asics-cooling/immersion-systems` (+ ICT-100, IC-1000), mineral oil post, Novec post.
In: mineral oil post (C4 in immersion cluster adds link to immersion-systems; this cluster adds a product link), Novec post, `/en/products` catalog, `/en/products/cell`, `/en/products/rack`, `/en/products/container`, immersion pillar "Tanks and system components" section. Full list: `content/internal-linking.md` → Hardware.

## Schema Recommendation

Keep `Product` (+ `AggregateOffer` only if real offers exist [VERIFY]) and `BreadcrumbList`; fix `name` spelling; `additionalProperty` from TDS; review `AggregateRating` [VERIFY]; `FAQPage` with the visible FAQ.

## Word Count Target

900–1 200 words (current ~640).

## [VERIFY] Blockers — DO NOT PUBLISH WITHOUT RESOLVING

1. Fluid base type and all TDS values.
2. Tested miner models and material compatibility.
3. Fill volume per BiXBiT system.
4. Maintenance intervals.
5. SDS classification; source for "non-toxic" and "saves electricity" claims.
6. Pack sizes, availability by region, whether a public price exists.
