# Content Brief: Hardware Product Pages — Unique Title / Description / H1 / Schema Template
**Slug:** all 19 hardware URLs (`/en/asics-cooling`, `/en/asics-cooling/hydro-systems`, 8 model pages, `/en/products`, 8 `/en/products/*`)
**Cluster:** hardware (`content/clusters/hardware.md`)
**Brief type:** Template / on-page fix (not a copywriting brief)
**Created:** 2026-09-28
**Owner:** SEO + developer (template change) + product team (facts marked [VERIFY])

**Priority:** P0. Crawl 2026-09-28: `/en/asics-cooling` and all 8 model pages share one title ("BiXBiT Crypto Mining Cooling Solutions for ASICs") and one description ("Keep ASIC miners running stable…"); each model page has 2 internal links and is outside the sitemap. CTR is the first lever: the hardware URLs have 0 US clicks on ~3 500 US impressions in 28 days (GSC US). Priority from CTR and duplication, not from volume.
**Target (architecture v2):** existing URLs only, no new pages. Architecture v2 (`reports/content-architecture-2026-09-25.md`) did not cover hardware; this cluster extends it with existing URLs only [VERIFY with the team that no hardware slugs are being renamed].

---

## Page Goal

Make every hardware URL distinguishable to Google and to a buyer scanning the SERP: model, product type, which miners it serves, and brand. Nothing else changes in this step.

## Search Intent

Model pages: transactional / navigational (a buyer who already heard the model name, or a category search where the model page is the most specific result). Category pages: commercial investigation. Titles lead with the category term where there is measured demand, with the model name where there is none.

---

## Target Keywords (per URL, data from `content/clusters/hardware.md` §3)

| URL | Primary keyword in title | Vol (US) | KD | BiXBiT pos |
|---|---|---|---|---|
| `/en/products/container` | mining container | 390 | n/d | #22 |
| `/en/products/rack` | mining rack | 40 | n/d | #6 |
| `/en/products/rack-hydro` | hydro rack | 40 | 8 | #16 |
| `/en/products/container-hydro` | hydro mining container | 10 | n/d | GSC 8.8 |
| `/en/products/container-1k` | immersion mining container | 10 | n/d | GSC 52 |
| `/en/products/cell` | immersion cooling tank | 70 | 3 | — |
| `/en/products/coolant` | immersion cooling fluid | 110 | 9 | — |
| `/en/products/server` | prefab data center cooling (`prefab data center` 140) | 140 | n/d | — |
| `/en/products` | asic immersion cooling | 10 | 0 | GSC 9.6 |
| `/en/asics-cooling` | crypto mining cooling systems | n/d (GSC 16 impr) | — | GSC 27.3 |
| `/en/asics-cooling/hydro-systems` | hydro cooling for ASIC mining (`mining water cooling` 90) | 90 | n/d | #27 |
| 8 model pages | model name (n/d) + product type | n/d | — | — |

---

## The template

### Title (≤ 60 characters where possible, hard limit 65)

- **Model pages:** `{Model} {Product type} for {Miner family} | BiXBiT`
  - `{Product type}` from a fixed list: Hydro Cooling Rack · Hydro Cooling Container · Skid-Mounted Hydro Cooling System · Immersion Cooling Tank · Immersion Cooling Container.
  - `{Miner family}`: Antminer, Whatsminer, or "ASIC Mining" when the product is miner-agnostic.
  - Capacity may be added only if the product team confirms the figure from the spec sheet (the live pages state figures such as 200 kW and 2.4 MW; treat them as [VERIFY] until the spec sheet is checked).
- **Category / product-line pages:** `{Category keyword}: {Differentiator} | BiXBiT`.
- Brand at the end, never twice. No "Buy", no "Best", no profitability words.

### Meta description (140–155 characters)

`{Model or category}: {one-sentence definition from the product team}. {Up to two verified facts: capacity, miner compatibility}. Request specs and a quote.`
No percentages of hashrate or power savings unless the source is named on the page [VERIFY].

### H1

`BiXBiT {Model} {Product type}` on model pages (today the H1 is only `BiXBiT {Model}`). On category pages the H1 carries the primary keyword in natural language.

### Product schema (model pages and old product pages)

Add `Product` JSON-LD on the 8 model pages (today only WebSite + Organization) and keep the one already on old pages. Fields: `name`, `brand` (`BiXBiT`), `category`, `description` (same as meta), `image`, `url`, `sku` = model [VERIFY], `additionalProperty` only with verified spec values. **No `offers.price`** unless a public price exists. **`AggregateRating`** on old pages: keep only if backed by real reviews visible on the page [VERIFY]; otherwise remove. Add `BreadcrumbList` on model pages (Home → Cooling → Hydro/Immersion Systems → Model). Generate JSON-LD with a serializer (crawl P1: 9 posts already broke on string concatenation).

---

## Proposed titles, descriptions and H1 (drafts; every fact in brackets is [VERIFY])

| URL | Title (chars) | H1 | Description draft (key facts [VERIFY]) |
|---|---|---|---|
| `/en/asics-cooling` | Crypto Mining Cooling Systems: Hydro & Immersion \| BiXBiT (57) | Cooling Systems for ASIC Mining: Hydro and Immersion | Hydro and immersion cooling systems for ASIC mining farms: racks, containers, tanks and coolant, with AMS monitoring. Compare options and request a quote. |
| `/en/asics-cooling/hydro-systems` | Hydro Cooling for ASIC Mining: Racks & Containers \| BiXBiT (58) | Hydro Cooling Systems for Antminer and Whatsminer Hydro Miners | Hydro cooling racks and containers for Antminer and Whatsminer hydro miners, with dry coolers, power distribution and AMS monitoring. Request specs. |
| `…/hydro-systems/whr-200-2u` | WHR-200-2U Hydro Cooling Rack for Whatsminer \| BiXBiT (53) | BiXBiT WHR-200-2U Hydro Cooling Rack | WHR-200-2U: hydro cooling rack for Whatsminer hydro miners [capacity per page: 200 kW, VERIFY]. Power distribution and AMS monitoring included [VERIFY]. |
| `…/hydro-systems/ahr-200` | AHR-200 Hydro Cooling Rack for Antminer S21 Hydro \| BiXBiT (58) | BiXBiT AHR-200 Hydro Cooling Rack | AHR-200: turnkey hydro cooling rack for Antminer S21 Hydro [per page: 36 units, VERIFY], with power distribution and control system. Request specs. |
| `…/hydro-systems/whc-1.2-2u` | WHC-1.2-2U Hydro Cooling Container for Whatsminer \| BiXBiT (58) | BiXBiT WHC-1.2-2U Hydro Cooling Container | [VERIFY: the live intro calls it an immersion container — product team to confirm type and capacity before this line is written]. |
| `…/hydro-systems/whc-2.4-2u` | WHC-2.4-2U Hydro Container with Dry Cooler \| BiXBiT (51) | BiXBiT WHC-2.4-2U Hydro Cooling Container | WHC-2.4-2U: integrated hydro mining container with racks, power distribution and control cabinets, dry cooler and monitoring [VERIFY capacity, compatible miners]. |
| `…/hydro-systems/hw-cluster-2.4` | HW-Cluster-2.4 Skid-Mounted Hydro Cooling System \| BiXBiT (57) | BiXBiT HW-Cluster-2.4 Skid-Mounted Hydro Cooling | HW-Cluster-2.4: skid-mounted hydro cooling for indoor mining halls [per page: 2.4 MW, VERIFY]. Compatible miners and footprint on request. |
| `…/hydro-systems/ahc-2.4` | AHC-2.4 40 ft Hydro Mining Container for Antminer \| BiXBiT (58) | BiXBiT AHC-2.4 Hydro Cooling Container | AHC-2.4: 40 ft hydro cooling container for Antminer hydro miners [per page: 2.4 MW, 420 units, VERIFY]. Request specs and a quote. |
| `…/immersion-systems/ict-100` | ICT-100 Modular Immersion Cooling Tank for ASICs \| BiXBiT (57) | BiXBiT ICT-100 Modular Immersion Cooling Unit | ICT-100: plug-and-play modular immersion cooling unit for ASIC miners [VERIFY: "tank" is the right term; capacity; fluid]. |
| `…/immersion-systems/ic-1000` | IC-1000 Immersion Cooling Container for ASIC Mining \| BiXBiT (60) | BiXBiT IC-1000 Immersion Cooling Container | IC-1000: pre-assembled all-in-one immersion cooling container for ASIC mining [VERIFY capacity, loop design, climate range]. |
| `/en/products` | ASIC Immersion Cooling Equipment & Containers \| BiXBiT (54) | ASIC Immersion Cooling Equipment: Tanks, Racks, Containers, Coolant | Immersion cooling equipment for ASIC miners: Cell tanks, stackable racks, 20/40 ft containers and dielectric coolant [VERIFY sizes]. Request a quote. |
| `/en/products/container` | Mining Container for ASICs: 20 & 40 ft Immersion \| BiXBiT (57) | BiXBiT Mining Container: 20 ft and 40 ft Immersion-Cooled | See `hardware-mining-container.md`. |
| `/en/products/container-hydro` | Hydro Mining Container for Whatsminer \| BiXBiT (46) | BiXBiT Hydro Mining Container | See `hardware-hydro-cooling.md`. |
| `/en/products/container-1k` | Single-Loop Immersion Mining Container \| BiXBiT (47) | BiXBiT Immersion Mining Container (Single-Loop) | Single-loop immersion mining container for moderate climates [VERIFY climate range, capacity]. Request specs. |
| `/en/products/rack` | Mining Rack for ASIC Miners: Immersion-Ready \| BiXBiT (53) | BiXBiT Mining Rack for ASIC Miners | See `hardware-mining-rack.md`. |
| `/en/products/rack-hydro` | Hydro Mining Rack: Water-Cooled ASIC Rack \| BiXBiT (50) | BiXBiT Hydro Mining Rack | See `hardware-hydro-cooling.md`. Fixes the "ASIC Minings" typo. |
| `/en/products/cell` | Immersion Cooling Tank for ASIC Miners: Cell \| BiXBiT (53) | BiXBiT Cell: Immersion Cooling Tank for ASIC Miners | Cell immersion cooling tank for ASIC miners [VERIFY capacity]. Kit includes [VERIFY]. Pairs with BiXBiT dielectric coolant. Request a quote. |
| `/en/products/coolant` | Immersion Cooling Fluid for ASIC Miners \| BiXBiT (48) | BiXBiT Coolant: Dielectric Immersion Cooling Fluid | See `hardware-immersion-coolant.md`. Fixes the Cyrillic "С" in the H1. |
| `/en/products/server` | Prefab Data Center Cooling: Liquid & Immersion \| BiXBiT (55) | Prefab Data Center Cooling: Direct Liquid and Immersion | Direct liquid and immersion cooling for servers and prefab data centers: racks, server tanks and containers [VERIFY scope]. Request a project review. |

All 19 titles are unique; the same primary keyword is not used as the head of more than one title (container vs container-hydro vs container-1k are split by cooling type).

---

## Other template fixes (same deployment)

1. Add the 8 model pages, `/en/asics-cooling`, `hydro-systems`, `immersion-systems` and `/en/products/pdu` to the sitemap (dev-task P2 list), fix the `container-1k` space and the duplicate `coolant` entry.
2. Model pages: make the product cards on the sub-hubs plain `<a href>` links (crawlable), add sibling links (see `content/internal-linking.md` → Hardware).
3. hreflang on the new template (`content/hreflang-spec.md`); do not add `ru` alternates for URLs that 404 in RU (`/ru/products/server`).
4. Image alt text on model pages: model + view (e.g. "BiXBiT AHC-2.4 hydro container, side view"), not empty.

## FAQ

Not applicable to this template brief. Page FAQs live in the page briefs.

## Internal Links

Covered in `content/internal-linking.md` → "Hardware" (rows H1–H16).

## E-E-A-T Signals

- Each model page names the engineering team or reviewer and the spec-sheet version/date [VERIFY names].
- The "Download Technical Specs" file is the single source for every number in title/description/schema.

## Schema Recommendation

See "Product schema" above. Validate in Rich Results Test before and after; compare with what is live (`./scripts/page-snapshot.py --urls … --compare none`), deliver as a diff.

## [VERIFY] Blockers — DO NOT PUBLISH WITHOUT RESOLVING

1. Product type of WHC-1.2-2U (hydro or immersion; the live intro text contradicts its category).
2. Capacity figures shown on the pages (200 kW, 2.4 MW, 36 units, 420 units, 160 units, 1.6 MW) against the spec sheets.
3. Miner compatibility per model (W = Whatsminer, A = Antminer is an inference from names, not confirmed).
4. Whether old-template products (`container-hydro`, `rack-hydro`, `container-1k`, `cell`) are current products or a previous generation.
5. Source of `AggregateRating` values on old product pages.
6. Source for "+40% hashrate", "-30% power", "40% more hashrate" claims in current descriptions (remove if unsourced).
7. Regression check (CLAUDE.md §7.5) before the template ships.
