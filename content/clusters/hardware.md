# Topic Cluster: Mining Hardware (Containers, Racks, Hydro, Immersion Equipment, Coolant, Server Cooling)
**Site:** https://bixbit.io/en
**Cluster slug:** hardware
**Created:** 2026-09-28
**Priority:** P1 overall (CLAUDE.md §3: cooling hardware is topic #2). Individual pages range P0–P2, see §4.
**Data (all real, nothing estimated):**
- DataForSEO, US / en, 2026-09-28: Labs `keyword_suggestions` ×7 seeds, Google Ads `search_volume` (96 keywords), SERP ×3 (`noAiMode`, depth 30). Compact dump: `data/dfs-hardware-cluster-2026-09-28.json`.
- BiXBiT positions: `data/dfs-ranked-keywords-bixbit.io-2026-09-25.json` (Google US, `#N`).
- GSC 28 days (2026-08-29 → 2026-09-25): `data/gsc-queries-pages-all-2026-09-28.json` (all countries), `data/gsc-queries-pages-us-2026-09-28.json` (US), `data/gsc-pages-2026-09-28.json`.
- GA4 organic landings 28 days: `data/ga4-organic-landing-2026-09-28.json`. `keyEvents` are unreliable (see `docs/agent-knowledge.md` §6): compare pages to each other only.
- Crawl: `reports/crawl-2026-09-28.md`, `data/crawl-2026-09-28/pages.json`. Cannibalization: `data/cannibalization/cannibal-2026-09-28.json`.
- `n/d` = Google Ads returned no volume (<~10/mo). Volumes are US only; most GSC impressions for these pages come from other countries.

**Relationship to other clusters (do not duplicate):**
- `content/clusters/immersion-cooling-mining.md` owns immersion **as a topic** (what it is, single vs two-phase, ROI, the pillar on `/en/asics-cooling/immersion-systems`, the mineral oil and how-it-works blog posts). This cluster owns the **product pages** that sell immersion equipment (`/en/products`, `cell`, `rack`, `container`, `container-1k`, `coolant`, `ICT-100`, `IC-1000`) and links them to the immersion pillar.
- `content/clusters/pdu-power-distribution.md` owns `/en/products/pdu`. This cluster only adds links to it from racks and containers (power distribution is part of every rack/container deployment).
- Firmware clusters own `/en/firmwares/*`. Hydro product pages link to the matching firmware page (Antminer Hydro, Whatsminer hydro series) and nothing more.

---

## 1. Key findings

1. **Containers are the biggest commercial pocket in the whole cooling area, and BiXBiT already ranks in it.** `mining container`, `container for mining`, `crypto mining container`, `container crypto mining`: 390/mo each (Labs groups them as one intent), CPC $4.20–4.30. `crypto mining shipping container` 170 and `crypto mining container for sale` 170. BiXBiT: `mining container` #22, `container miner` #27, `crypto mining shipping container` #17, `mining container price` #9, all on `/en/products/container`. GSC: 2 087 impressions (US 1 462), **0 clicks**, average position 21.9.
   - Seasonality is extreme: the 390 average is driven by Sep–Dec 2025 (720–1 300/mo); Jun–Aug 2026 was 20–70/mo. Plan the refresh to be live before the next autumn peak, not to chase current volume.
   - The SERP (2026-09-28) is a mix of Chinese manufacturer listings, Alibaba/Made-in-China, YouTube product videos and off-topic results (gold mining, games). No page answers cost, site planning or climate questions with specifics. That is the content gap. PAA includes "How much does a Bitcoin mining container cost?".
2. **Racks are a quick win.** `mining rack` #6 and `rack mining` #9 (40/mo each), `asic miner rack` GSC position 4.5 (1 click), `miner rack` 7.3, `crypto mining rack` 20/mo at CPC $3.82 (GSC 13.3). `/en/products/rack`: 333 impressions, 8 clicks, position 12.2. Half of the Labs "mining rack" demand is GPU racks (off-ICP), so do not chase it.
3. **Hydro has no owner cluster, and it is the best-engaged hardware landing.** `/en/asics-cooling/hydro-systems`: 688 impressions, 8 clicks, position 20.4; GA4 13 organic sessions (11 engaged), the highest among hardware pages. Demand: `mining water cooling` 90 (#27), `hydro miner` 90 (CPC $1.53), `antminer s21 hydro` 90, `hydro rack` 40 (#16, `/en/products/rack-hydro`), `hydro cooling system` 40 at CPC $6.42 (#29), `hydro container` 20 (GSC 13.3 on `container-hydro`), `hydro mining container` 10 at CPC $2.69 (GSC 8.8).
4. **Two product lines live on two templates.** Old template `/en/products/*` (container, container-hydro, container-1k, rack, rack-hydro, cell, coolant, server): has Product/BreadcrumbList schema and hreflang, carries almost all rankings. New template `/en/asics-cooling/{hydro,immersion}-systems/<model>` (8 models): **one shared title and one shared description** ("BiXBiT Crypto Mining Cooling Solutions for ASICs" / "Keep ASIC miners running stable…"), only 2 internal links each, outside the sitemap, no Product schema, no hreflang. GSC shows them getting a trickle (AHC-2.4 7 impressions at position 2.9, WHC-2.4-2U 7 at 7.3), so Google is willing to rank them once they are distinguishable.
   - Overlap by function: `container-hydro` ↔ WHC-1.2-2U / WHC-2.4-2U / AHC-2.4; `rack-hydro` ↔ WHR-200-2U / AHR-200; `container-1k` ↔ IC-1000; `cell` ↔ ICT-100. **[VERIFY with the team: are the old-template products still sold, or are they the previous generation?]** The answer decides whether old pages stay as separate products or get consolidated later. Until then, do not redirect anything: the old pages hold the rankings.
5. **`/en/products` is where Google ranks commercial immersion queries, not the immersion pillar.** `asic immersion cooling` (GSC 9.6), `asic immersion cooling system` (8.9), `immersion cooling antminer` (16.9; DFS SERP #13), `asic miner immersion cooling` (11.6) land on `/en/products`; `/en/asics-cooling/immersion-systems` has 9 impressions in 28 days. The immersion cluster targets the pillar. **Decision needed** (shared with the immersion cluster): keep `/en/products` as the immersion equipment catalog and keep its immersion wording until the pillar starts ranking; review in 60 days. Do not strip "immersion" from the `/en/products` title now.
6. **Coolant has real commercial demand with high CPC.** `immersion cooling fluid` 110 (CPC $7.11, KD 9), `dielectric fluid for immersion cooling` 70 (CPC $7.60, KD 2), `dielectric coolant` 170 (CPC $3.38), `immersion cooling fluid price` 20, `immersion cooling oil` 10 (CPC $23.57). `/en/products/coolant` sits at GSC 26.8 (140 impressions, 5 clicks, the best CTR among hardware pages at 3.6%). The informational side (`mineral oil for immersion cooling` #1, `antminer mineral oil` #2) belongs to the blog post in the immersion cluster.
7. **Server/data center demand is large but wide.** `server immersion cooling` 1 600 (KD 21, informational), `modular data center` 1 900 (CPC $12.63), `direct to chip cooling` 590 (CPC $11.92), `data center immersion cooling` 590 (CPC $11.23), `immersion cooling for data centers` 210, `prefab data center` 140 (**CPC $16.59**). `/en/products/server` gets 38 impressions (position 7.1). SERPs are owned by Vertiv, GIGABYTE, Submer, Asperitas, Baltimore Aircoil (AIO references on `immersion cooling tank`). Treat as a P1 page fix plus blog support, not a head-term push.
8. **Immersion tanks: demand exists, BiXBiT is invisible.** `immersion cooling tank` 70/mo, CPC $9.54, KD 3; BiXBiT is not in the top ~26. SERP is data-center oriented (GIGABYTE, Submer, Engineered Fluids, Midas). `/en/products/cell` holds `asic immersion cooling kit` (GSC 22.2) and `immersion cooling kit`.
9. **On-page defects found while building the cluster** (fix together with titles):
   - `/en/products/coolant` H1 is "BiXBiT Сoolant" with a **Cyrillic "С"** (U+0421). Google reads it as a different word.
   - `/en/products/rack-hydro` title has a typo: "…for ASIC Minings".
   - `/en/asics-cooling/hydro-systems/whc-1.2-2u` intro says "Pre-assembled all-in-one immersion cooling container", the same text as IC-1000, although it sits in the hydro line. **[VERIFY: correct product description]**.
   - Old product meta descriptions contain unsourced performance claims: "+40% hashrate, -30% power" (`container`), "Gain 40% more hashrate" (`cell`). `/en/products/container` has an H3 "Bitcoin mining profitability with immersion cooling". Profitability wording conflicts with CLAUDE.md §4; claims need a source or removal **[VERIFY]**.
   - `AggregateRating` sits in Product schema on the old product pages. **[VERIFY: are these real, visible customer reviews?]** If not, remove it (structured-data policy risk).
   - `content/seo-fixes/meta-descriptions-all-pages.md` describes `/en/products/rack` as "air-cooled" and `/en/products/server` as "for servers and GPU rigs"; neither matches the live pages. For hardware URLs, the briefs from this cluster supersede that file.
   - RU menu links to `/ru/products/server` (404, 1 477 links) — already in `reports/crawl-2026-09-28.md` P0-1; out of scope here, but the EN server brief must not assume a RU counterpart.

---

## 2. Hub-and-spoke map (existing URLs only)

No new URLs are proposed. Every intent with measurable demand already has a matching page. Intents without a page (`mining container price`, `direct to chip cooling`, `dry cooler`) are served as sections or through planned blog posts (§6).

```
/en/asics-cooling  (HARDWARE HUB — cooling systems overview, product navigation)
├── /en/asics-cooling/hydro-systems  (HYDRO SUB-HUB)            ← owned here
│   ├── Hydro racks:      whr-200-2u · ahr-200
│   ├── Hydro containers: whc-1.2-2u · whc-2.4-2u · ahc-2.4 · hw-cluster-2.4
│   └── Legacy-template hydro: /en/products/rack-hydro · /en/products/container-hydro
├── /en/asics-cooling/immersion-systems  (IMMERSION PILLAR)     ← owned by immersion cluster
│   └── Models: ict-100 · ic-1000                               ← product pages owned here
├── /en/products  (IMMERSION EQUIPMENT CATALOG, legacy template) ← owned here, wording shared (§1.5)
│   ├── /en/products/cell        (tank / kit)
│   ├── /en/products/rack        (stackable immersion rack)
│   ├── /en/products/container   (immersion mining container, 20/40 ft)
│   ├── /en/products/container-1k (single-loop immersion container)
│   └── /en/products/coolant     (dielectric fluid)
├── /en/products/server  (prefab data center / server cooling)
└── /en/products/pdu     (power)                                 ← owned by PDU cluster
```

---

## 3. Keyword → URL mapping with data

Volumes: US Google Ads / Labs, 2026-09. BiXBiT pos: DFS ranked_keywords (US, 2026-09-25) unless marked GSC (average position, all countries, 28 days).

| URL | Primary intent | Main keywords (Vol · CPC · KD) | BiXBiT now | GSC 28d (impr / clicks / pos) | GA4 org. sessions |
|---|---|---|---|---|---|
| `/en/asics-cooling` | Commercial investigation (compare cooling types, pick a vendor) | `asic cooler` 40 · $0.21; `crypto mining cooling systems` n/d; `mining cooling solutions` 10; `asic miner cooling system` 10; `mining farm cooling` 10 | `asic cooler` #26; GSC `crypto mining cooling systems` 27.3 | 1 216 / 0 / 14.5 (mostly brand "bixbit") | 2 |
| `/en/asics-cooling/hydro-systems` | Commercial investigation | `mining water cooling` 90; `hydro miner` 90 · $1.53; `antminer s21 hydro` 90 · $1.65; `hydro cooling system` 40 · $6.42; `asic hydro cooling` 10; `whatsminer hydro` 10 · $1.42; `antminer hydro` 20 · $1.39 | `mining water cooling` #27; `hydro hosting` #34 | 688 / 8 / 20.4 | **13** |
| `/en/products/container` | Transactional | `mining container` 390 · $4.20; `crypto mining container` 390 · $4.30; `container for mining` 390 · $4.20; `crypto mining shipping container` 170; `crypto mining container for sale` 170; `mining container price` 40; `crypto container` 170 (ambiguous) | #22 / #27 (`container miner`) / #17 / #9 (`price`) | 2 087 / 0 / 21.9 (US 1 462 / 0) | 5 |
| `/en/products/container-hydro` | Transactional | `hydro container` 20; `hydro mining container` 10 · $2.69; `whatsminer hydro container` n/d | `whatsminer hydro` #18 | 346 / 8 / 18.5; `hydro mining container` GSC 8.8, `whatsminer hydro container` 6.6, `hydro container` 13.3 | 10 |
| `/en/products/container-1k` | Transactional | `immersion container` 10; `immersion cooling container` 10; `immersion mining container` 10 | — | 97 / 1 / 36.0 | 1 |
| `/en/products/rack` | Transactional | `mining rack` 40 · $0.36; `rack mining` 40; `miner rack` 40 · $0.36; `crypto mining rack` 20 · $3.82 · KD 1; `asic miner rack` 10; `mining server rack` 10 · KD 18 | #6 / #9 | 532 / 8 / 12.2; `asic miner rack` 4.5, `miner rack` 7.3 | 9 |
| `/en/products/rack-hydro` | Transactional | `hydro rack` 40 · $1.53 · KD 8; `hydro mining rack` n/d (GSC 30 impr) | #16; `hydro cooling system` #29 | 207 / 6 / 20.3; `hydro mining rack` 10.3 | 8 |
| `/en/products/cell` | Transactional | `immersion cooling tank` 70 · **$9.54** · KD 3; `asic immersion cooling kit` 10; `immersion cooling kit` 10; `asic immersion cooling tank` 10 | `immersion cooling miners` #37; not in top 26 for `immersion cooling tank` | 517 / 2 / 50.2; `asic immersion cooling kit` 22.2 | 3 |
| `/en/products/coolant` | Transactional | `immersion cooling fluid` 110 · **$7.11** · KD 9; `dielectric coolant` 170 · $3.38; `dielectric fluid for immersion cooling` 70 · **$7.60** · KD 2; `immersion cooling fluid price` 20 · $3.18; `immersion cooling oil` 10 · $23.57; `mining coolant(s)` 10 | — | 140 / 5 / 26.8; `mining coolants` 25.8 | 4 |
| `/en/products` | Commercial (catalog) | `asic immersion cooling` 10; `immersion cooling antminer` 20 · KD 55; `bitcoin immersion cooling` n/d | `immersion cooling antminer` #13 (rank-tracking) | 1 260 / 5 / 13.2; `asic immersion cooling` 9.6 | 7 |
| `/en/products/server` | Commercial investigation (DC buyers) | `prefab data center` 140 · **$16.59**; `immersion cooling for data centers` 210 · $9.32; `data center immersion cooling` 590 · $11.23; `server immersion cooling` 1 600 · KD 21 (informational); `immersion cooling server` 50 · $5.49; `server cooling solutions` 70 · $3.72; `modular data center` 1 900 · $12.63 (wide) | — | 38 / 1 / 7.1 | 4 |
| 6 hydro models (`/en/asics-cooling/hydro-systems/*`) | Transactional (model / navigational) | Model names: n/d. Category terms go to the sub-hub | — | whr-200-2u 2 / 0 / 8; ahr-200 1 / 0 / 2; whc-1.2-2u 1 / 0 / 4; whc-2.4-2u 7 / 0 / 7.3; ahc-2.4 7 / 0 / 2.9; hw-cluster-2.4 0 | 1–2 each |
| `ict-100`, `ic-1000` | Transactional (model) | n/d | — | ic-1000 2 / 0 / 44 | 0 |

---

## 4. Priorities (rules: `reports/cluster-repriorization-2026-09-25.md` §2)

| P | URL / task | Why (criteria) | Brief |
|---|---|---|---|
| **P0** | Unique title / description / H1 / Product schema for all 19 hardware URLs | 9 duplicate titles and descriptions (crawl P1); CTR is the first lever (0 clicks on 1 462 US impressions for containers); cheapest change with the widest effect | `content/briefs/hardware-product-title-template.md` |
| **P0** | `/en/products/container` | Largest commercial demand in the cooling area (390 ×4 variants, CPC $4.2–4.3); already #9–27 = quick-win band; 0 clicks; cannibalization with the shipping-containers post | `content/briefs/hardware-mining-container.md` |
| **P0** | `/en/products/rack` | Position #4.5–13 (quick win), direct product intent; small volume (40) | `content/briefs/hardware-mining-rack.md` |
| **P0** | `/en/asics-cooling/hydro-systems` (+ `container-hydro`, `rack-hydro`, 6 models as sections/links) | No owner cluster; best-engaged hardware landing (GA4); #16–29 on hydro terms; `hydro cooling system` CPC $6.42; `container-hydro` at GSC 6.6–13.3 | `content/briefs/hardware-hydro-cooling.md` |
| **P1** | `/en/asics-cooling` (hardware hub) | 1 216 impressions, 0 clicks; hub for internal links to every product; content shared with immersion cluster (its comparison block, their P2) | `content/briefs/hardware-hub.md` |
| **P1** | `/en/products/coolant` | CPC $7.11–7.60 on the core terms (commercial value high), KD 2–9; position 26 (outside quick-win band); H1 Cyrillic bug | `content/briefs/hardware-immersion-coolant.md` |
| **P1** | `/en/products/container-hydro` | GSC 6.6–13.3 = quick win, small volume; handled inside the hydro brief | (in `hardware-hydro-cooling.md`) |
| **P1** | `/en/products/rack-hydro` | `hydro rack` #16 (quick win); handled inside the hydro brief | (in `hardware-hydro-cooling.md`) |
| **P1** | `/en/products/cell` | `immersion cooling tank` 70 at CPC $9.54, KD 3, but BiXBiT not visible and SERP is DC-oriented; `asic immersion cooling kit` GSC 22 | Outline below (§5), no separate brief |
| **P1** | `/en/products/server` | `prefab data center` CPC $16.59 (≥ $15 rule), but wide DC SERP with strong incumbents; fix title/schema/sections, support via blog | Outline below (§5) |
| **P1** | `/en/products` (catalog) | Ranks #9–17 for commercial immersion terms; wording decision shared with immersion cluster (§1.5) | Title only, in the template brief |
| **P2** | `/en/products/container-1k`, `ict-100`, `ic-1000`, 6 hydro model pages beyond the template | n/d volumes, GSC 0–7 impressions; value comes from the template fix and hub links, not from new copy | Template brief + links |

**Tracked keywords:** propose adding to `data/rank-tracking/keywords.md` (human approves the rotation): `mining container` → `/en/products/container`; `mining rack` → `/en/products/rack`; `mining water cooling` → `/en/asics-cooling/hydro-systems`; `hydro rack` → `/en/products/rack-hydro`; `immersion cooling fluid` → `/en/products/coolant`. Also flag: tracked #18 `asic immersion cooling` and #24 `immersion cooling antminer` target `/en/asics-cooling/immersion-systems`, but Google ranks `/en/products` (§1.5).

---

## 5. Outlines for P1 pages without a separate brief

### `/en/products/cell` — immersion tank / kit
- Title/description: see template brief.
- H1: "BiXBiT Cell: Immersion Cooling Tank for ASIC Miners" (currently "BiXBiT Cell").
- Sections: what the Cell is and who it is for (small sites, pilots, test benches) [VERIFY positioning with sales]; supported miners [VERIFY: current meta says "24 GPUs or 6 ASICs" — confirm for current ASIC generations]; what ships in the kit [VERIFY]; fluid volume and coolant pairing (link `/en/products/coolant`); how it scales to Rack and Container (links); FAQ ("Can I put an Antminer S21 in an immersion tank?" [VERIFY], "Which fluid does it use?", "How is heat rejected?" [VERIFY]).
- Remove or source "Gain 40% more hashrate" [VERIFY].
- Links: `/en/products/coolant`, `/en/products/rack`, `/en/asics-cooling/immersion-systems/ict-100` (industrial alternative), `/en/asics-cooling/immersion-systems`.

### `/en/products/server` — prefab data center / server cooling
- Title/description: see template brief. Add `hreflang` (missing) and `BreadcrumbList` + `Product`/`Service` schema (only Organization/WebSite now).
- H1 stays close to the current "Prefab Data Centers Cooling Solutions", extended with "Direct Liquid and Immersion".
- Sections follow the live page (Direct Liquid Cooling rack/container, Immersion Server Tank, Immersion Cooling Container); add a comparison table direct-to-chip vs immersion for server loads with all values [VERIFY]; a PUE section linking the PUE post (`/en/blog/post/how-to-calculate-the-pue-of-a-datacenter`), no invented PUE numbers.
- Commercial claims on the live page ("minimum market price", "6-month money-back guarantee", "12 months free technical support") — [VERIFY: current terms with sales] before they go into meta or schema.
- Links: `/en/asics-cooling/immersion-systems`, `/en/asics-cooling/hydro-systems`, `/en/products/pdu`, blog `datacenter-cooling-methods-everything-you-need-to-know`.

---

## 6. Blog support (from `content/blog-plan.md`, no new topics added)

| Blog item | Month | Links it must carry to this cluster |
|---|---|---|
| EN-FEB-4 `how-shipping-containers-change-the-cryptocurrency-mining-industry` (K4: move commercial wording to the product page) | Feb 2027 → **suggest moving to Nov 2026**, before the container season (§1.1) [decision: blog owner] | `/en/products/container`, `/en/asics-cooling/hydro-systems` (hydro containers) |
| EN-JAN-1 "Hydro (Direct-to-Chip) vs Immersion Cooling for ASIC Mining" | Jan 2027 | `/en/asics-cooling/hydro-systems`, `/en/asics-cooling/immersion-systems`, `/en/asics-cooling` |
| EN-OCT-3 PUE post refresh | Oct 2026 | `/en/products/server`, `/en/asics-cooling` |
| EN-MAR-2 "Immersion Fluid Maintenance" | Mar 2027 | `/en/products/coolant` |
| EN-JUN-2 DC cooling posts merge | Jun 2027 | `/en/products/server`, `/en/asics-cooling` |
| EN-FEB-3 noise and dust post | Feb 2027 | `/en/asics-cooling/hydro-systems` |
| EN-NOV-1 Antminer S21 series (incl. S21 Hydro) | Nov 2026 | `/en/asics-cooling/hydro-systems/ahr-200` [VERIFY: AHR-200 is built for S21 Hydro per its page], hydro sub-hub |
| EN-NOV-2 Whatsminer lineup (air vs hydro) | Nov 2026 | `/en/asics-cooling/hydro-systems/whr-200-2u`, hydro sub-hub |
| EN-MAY-2 M50/M53 review refresh | May 2027 | hydro sub-hub (M53 Hydro) |
| Existing posts without a plan slot: `novec-and-coolant-liquids-comparison-why-we-stick-to-our-own-formula` (GSC 469 impr, pos 8.5), `hydro-asic-2026-ranking-models-for-largescale-mining-farms` (117 inlinks), `bitmain-releases-t19-hydro-btc-miner-…` (GSC pos 7.8), `asic-cooling-trends-2026` | — | contextual links only (see `content/internal-linking.md` → Hardware, H-B rows); no rewrite scheduled |

---

## 7. Competitor content gaps (hardware)

- **Containers:** the SERP leaders (apextomining, LianLi, Alibaba sellers, Bitmain Antbox listings) publish slot counts and a spec table, nothing on site planning, climate range, power interconnection, noise, lead time or what is included. A container page that answers "what do I need on site before delivery" [VERIFY each item with engineering] and "what drives the price" (no price invented) covers a gap nobody fills. PAA asks about cost directly.
- **Hydro:** results are miner listings (Bitaxe, Antminer S21/S23 Hydro on Alibaba/Newegg), news and Reddit. Very few vendor pages explain the full loop (miner → CDU/dry cooler → heat reuse) for a farm. BiXBiT's hub already has "How Hydro Cooling Works" and "Heat Reuse"; making those concrete (component list, which miners, which firmware) is the gap.
- **Immersion tanks / fluids:** owned by data-center vendors (GIGABYTE, Submer, Engineered Fluids, Shell, Castrol). They do not talk about ASICs. BiXBiT's angle: fluid + tank + firmware profile + monitoring for Antminer/Whatsminer, with the mineral oil post as proof of expertise.
- **E-E-A-T across the cluster:** named engineering author or reviewer on each product page [VERIFY names], downloadable spec sheet (already offered as "Download Technical Specs"), deployment photos with real alt text, and case references (the hub timeline mentions Cormint) [VERIFY what may be published].
