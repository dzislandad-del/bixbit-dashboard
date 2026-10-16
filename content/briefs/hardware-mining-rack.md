# Content Brief: Mining Rack for ASIC Miners (Immersion-Ready)
**Slug:** `/en/products/rack` (existing)
**Cluster:** hardware (`content/clusters/hardware.md`)
**Brief type:** Product page refresh (transactional), CTR-first
**Created:** 2026-09-28
**Author assignment:** Product engineer for the Rack line [VERIFY: assign real reviewer name]

**Priority:** P0 (quick win). BiXBiT is already in positions #4–13: `mining rack` #6, `rack mining` #9 (40/mo each, CPC $0.36); GSC `asic miner rack` 4.5 (1 click), `miner rack` 7.3, `bitcoin miner rack` 7.6, `mining rack` 10.0, `crypto mining rack` 13.3 (20/mo, **CPC $3.82**, KD 1), `bitcoin mining rack` 13.8. Page: 532 impressions, 8 clicks, position 12.2; GA4 9 organic sessions. Volume is small, so the value is protecting and converting existing positions: title/description + a spec table + FAQ.
**Target (architecture v2):** `/en/products/rack` (existing page). Hardware extension; no new slug.

---

## Page Goal

Convert operators who search for a rack/frame for ASIC miners into quote requests for the BiXBiT Rack, and route immersion buyers to the tank, coolant and container pages. Also answer "leading miner rack providers?" style queries (GSC 12 impressions, pos 4.7) with a clear vendor statement.

## Search Intent

**Primary:** transactional: buy a rack / frame for ASIC miners.
**Secondary:** commercial comparison: which rack format (air frame vs immersion rack vs hydro rack).
**Do NOT optimize for:** GPU mining racks (`gpu mining rack` 70/mo: GPU rigs, off-ICP), DIY builds (`mining rack diy`, `how to build a mining rack`), and `hydro mining rack` (→ `/en/products/rack-hydro`).

---

## Target Keywords

> Volumes: DataForSEO Google Ads / Labs, US / en, 2026-09-28. `#N`: DataForSEO ranked_keywords 2026-09-25. GSC: average position, all countries, 28 days.

| Type | Keyword | Vol (US) | CPC | KD | BiXBiT pos |
|---|---|---|---|---|---|
| Primary | `mining rack` | 40 | $0.36 | n/d | #6 (GSC 10.0) |
| Secondary | `asic miner rack` | 10 | — | n/d | GSC 4.5 |
| Secondary | `miner rack` | 40 | $0.36 | n/d | GSC 7.3 |
| Secondary | `crypto mining rack` | 20 | $3.82 | 1 | GSC 13.3 |
| Secondary | `bitcoin mining rack` | n/d (GSC 42 impr) | — | — | GSC 13.8 |
| Secondary | `rack mining` | 40 | $0.36 | n/d | #9 |
| Long-tail | `asic mining rack`, `mining server rack`, `mining rack for sale` | 10 each | — / $0.31 / — | 55 / 18 / n/d | — |

---

## H1

BiXBiT Mining Rack for ASIC Miners

(Title: "Mining Rack for ASIC Miners: Immersion-Ready | BiXBiT"; see `hardware-product-title-template.md`. Keep "Mining Rack" as the first words: the page already ranks #6 for it.)

**Title change risk:** the page ranks #4–13; change title and description only, keep the URL, H1 wording close to the current "BiXBiT Rack", and compare GSC position/CTR 28 days after the change. Roll back if the average position for `mining rack` drops by more than 3.

---

## Meta description (draft)

BiXBiT stackable mining rack for ASIC miners: immersion-ready, corrosion-resistant frame [VERIFY], built to scale from one rack to a container. Request specs and a quote. (≈150 chars; current description begins "Buy stackable mining rig frame…".)

---

## Page Structure

### Above the fold
Definition in one sentence: what the Rack is (stackable frame / immersion rack) and for whom [VERIFY exact product type: the live meta says "stackable mining rig frame… immersion cooling, corrosion-resistant"]. CTAs: quote, spec download.

### H2: Specifications
Table: miners per rack, supported models, dimensions, materials, load rating, fluid volume if immersion [VERIFY every value]. Leave out any unconfirmed row.

### H2: Which Rack Format Fits Your Site
Short comparison (3 rows): BiXBiT Rack (immersion) · Hydro Rack (`/en/products/rack-hydro`, WHR-200-2U, AHR-200) · Cell tank (`/en/products/cell`) for small sites. One line on when each fits; no invented numbers.

### H2: Scaling from Rack to Container
How racks combine into a room or a container deployment (`/en/products/container`) [VERIFY]. Power per rack and distribution → `/en/products/pdu`.

### H2: Coolant and Maintenance
Which fluid, fill volume, inspection intervals [VERIFY]; link `/en/products/coolant` and the mineral oil post (`/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining`).

### H2: Monitoring
Per-miner telemetry via AMS, temperature alerts [VERIFY]; link `/en/ams`.

### H2: FAQ

---

## Key Entities and Terms to Include

ASIC miner, Antminer, Whatsminer, mining rack, stackable rack, immersion rack, frame, corrosion-resistant, dielectric fluid, tank, container, PDU, three-phase power, AMS, hashrate, temperature, maintenance.

---

## FAQ (4–6 questions)

1. **How many ASIC miners fit in one BiXBiT Rack?** [VERIFY].
2. **Which miner models does the rack support?** [VERIFY].
3. **Is the rack for air, immersion or hydro cooling?** [VERIFY]; links to rack-hydro and cell.
4. **What power distribution does a rack need?** Link PDU [VERIFY input spec].
5. **Who are the leading mining rack suppliers?** Neutral answer: what to compare (materials, compatibility, cooling integration, monitoring, lead time), then BiXBiT's scope. No competitor claims.

---

## E-E-A-T Signals

- Named reviewer, spec-sheet date [VERIFY].
- Photos of the rack loaded with miners (descriptive alt text).
- Materials/certifications only if documented [VERIFY].

## Internal Links

Out: `/en/products/cell`, `/en/products/coolant`, `/en/products/container`, `/en/products/rack-hydro`, `/en/products/pdu`, `/en/ams`, mineral oil blog post.
In: `/en/products` (catalog), `/en/asics-cooling` (hub), `/en/products/container`, `/en/products/cell`, `/en/products/pdu` (PDU cluster). The new-template model pages already link here from their footer/nav (crawl) — keep.

## Schema Recommendation

Keep existing `Product` + `BreadcrumbList`; update `description`; add verified `additionalProperty`; review `AggregateRating` [VERIFY]. Add `FAQPage` with the visible FAQ.

## Word Count Target

900–1 300 words (current ~1 590 words: tighten, move repeated marketing copy out, keep the table and FAQ).

## [VERIFY] Blockers — DO NOT PUBLISH WITHOUT RESOLVING

1. Product type (immersion rack vs frame) and cooling compatibility.
2. Capacity, dimensions, materials, supported models.
3. Fluid volume and maintenance intervals.
4. Source of `AggregateRating`.
