# Content Brief: Mining Container (Immersion, 20 ft / 40 ft)
**Slug:** `/en/products/container` (existing)
**Cluster:** hardware (`content/clusters/hardware.md`)
**Brief type:** Product page refresh (commercial)
**Created:** 2026-09-28
**Author assignment:** Engineer who has commissioned BiXBiT containers on site [VERIFY: assign real author/reviewer name]

**Priority:** P0. The largest commercial demand in the cooling area: `mining container` / `crypto mining container` / `container for mining` / `container crypto mining` 390/mo each (Labs groups them into one intent), CPC $4.20–4.30; `crypto mining shipping container` 170; `crypto mining container for sale` 170. BiXBiT is already in the quick-win band: #22 (`mining container`), #17 (`crypto mining shipping container`), #9 (`mining container price`), #27 (`container miner`). GSC 28 days: 2 087 impressions (US 1 462), **0 clicks**, position 21.9. Demand is seasonal (Sep–Dec 2025: 720–1 300/mo; Jun–Aug 2026: 20–70/mo): ship before the autumn/winter peak.
**Target (architecture v2):** `/en/products/container` (existing page). Not part of the 17 URLs of architecture v2; hardware extension, existing URL, no new slug.

---

## Page Goal

Turn the container page from a short product card into the page that answers what a mining-farm buyer asks before requesting a quote: what fits inside, what the site must provide, how it behaves in their climate, what drives the price, and how it is monitored. Conversion: quote request / spec download.

## Search Intent

**Primary:** transactional / commercial investigation: operator shortlisting container suppliers for a new site or an expansion.
**Secondary:** "how much does a mining container cost" (PAA on the SERP; `mining container price` 40/mo, #9): answered with cost drivers, not with an invented number.
**Do NOT optimize for:** the general "how shipping containers changed mining" story. That belongs to the blog post (see Cannibalization).

**SERP (2026-09-28, US, volatile):** manufacturer listings (apextomining, LianLi, Bitmain Antbox via marketplaces), Alibaba / Made-in-China, YouTube product videos, off-topic results (gold mining, games). AI Overview present; PAA: "How much does a Bitcoin mining container cost?" plus generic mining questions. bixbit.io was not in the returned top ~26 in this snapshot (DFS ranked_keywords 2026-09-25: #22).

---

## Target Keywords

> Volumes: DataForSEO Google Ads / Labs, US / en, 2026-09-28. `#N`: DataForSEO ranked_keywords 2026-09-25. GSC: average position, all countries, 28 days.

| Type | Keyword | Vol (US, 2026-09) | CPC | KD | BiXBiT pos |
|---|---|---|---|---|---|
| Primary | `mining container` | 390 | $4.20 | n/d | #22 (GSC 24.4) |
| Secondary | `crypto mining container` | 390 | $4.30 | n/d | GSC 17.6 |
| Secondary | `container for mining` | 390 | $4.20 | n/d | GSC 21.7 |
| Secondary | `crypto mining shipping container` | 170 | — | n/d | #17 (GSC 19.3) |
| Secondary | `crypto mining container for sale` | 170 | — | n/d | — |
| Secondary | `container miner` | 390 (DFS ranked_keywords) | $4.20 | n/d | #27 |
| Long-tail | `mining container price` | 40 | — | n/d | #9 |
| Long-tail | `bitcoin mining container` / `bitcoin mining containers` | n/d (GSC 53 / 62 impr) | — | — | GSC 23.1 / 24.3 |
| Long-tail | `shipping container mining`, `mobile mining container`, `asic mining container` | 10 each | — | 39 / 23 / 27 | GSC 18.6 (shipping) |

Not targeted here: `immersion mining container` / `immersion container` (→ `container-1k`, IC-1000), `hydro container` (→ `container-hydro`), `crypto container` 170 (ambiguous, mostly not mining).

---

## H1

BiXBiT Mining Container: 20 ft and 40 ft Immersion-Cooled ASIC Containers

(Title and description: `hardware-product-title-template.md` → "Mining Container for ASICs: 20 & 40 ft Immersion | BiXBiT".)

---

## Page Structure

### Above the fold
- One-sentence definition: a pre-built, immersion-cooled container that houses ASIC miners, power distribution and cooling for outdoor deployment [VERIFY wording with product team].
- Three verified facts max (e.g. available lengths, miner capacity, climate range). The current meta claims "20' & 40' options" and "-40°C to +40°C": **[VERIFY both against the spec sheet]**.
- CTAs: "Request a quote", "Download technical specs".

### H2: What Fits Inside a BiXBiT Container
- Table per version (20 ft / 40 ft): miner count by model family, power capacity, tanks/racks inside, coolant volume. **Every cell [VERIFY]**. If a value is not confirmed, leave the row out rather than estimate.
- Supported miners: Antminer / Whatsminer models [VERIFY list]; note on firmware profiles for immersion with a link to `/en/firmwares/antminer` (tuning section) and the Whatsminer hub.

### H2: Site Requirements Before Delivery
Operator checklist (this is the gap no competitor fills). Each item needs the engineering value [VERIFY]:
- H3: Power: grid connection or on-site generation, transformer, voltage/phase at the container input, link to `/en/products/pdu` for in-container distribution.
- H3: Foundation and footprint: pad, clearance, crane access.
- H3: Network: uplink, remote access, AMS connectivity.
- H3: Water / fluid logistics: first fill of dielectric coolant (link `/en/products/coolant`), top-up and maintenance.
- H3: Permits and noise: note that rules differ by jurisdiction; no legal guarantees (CLAUDE.md §4).

### H2: Climate Range and Heat Rejection
- How the container rejects heat (dry cooler / heat exchanger design) [VERIFY].
- Operating ambient range [VERIFY]; when to choose the single-loop version (`/en/products/container-1k`) and when a hydro container fits better (`/en/asics-cooling/hydro-systems`, AHC-2.4 / WHC-2.4-2U). Short 3-row comparison table, values [VERIFY].
- Heat reuse option, if offered [VERIFY].

### H2: What Drives Mining Container Cost
Answers PAA "How much does a Bitcoin mining container cost?" **without a price**:
- Cost drivers: container size, miner capacity, cooling type (immersion vs hydro vs air), coolant volume, power equipment scope, shipping and duties to the destination, commissioning.
- What is included in a BiXBiT quote [VERIFY scope].
- Lead time [VERIFY].
- Link `/en/calc` for fleet economics, with the explicit note that it does not promise profitability.
- 40–60-word answer paragraph at the top of the section (AIO/PAA-ready).

### H2: Monitoring and Control
- Container sensors and AMS integration: temperatures, pumps, power, per-miner hashrate [VERIFY which telemetry is actually exposed]. Link `/en/ams`.
- Remote power control via PDU (link `/en/products/pdu`).

### H2: Deployment Process
Numbered steps: project review → site assessment → manufacturing → shipping → installation → commissioning → handover [VERIFY steps and who does what]. Mention warranty/support terms only if confirmed [VERIFY].

### H2: Other BiXBiT Containers
Cards with links: `/en/products/container-1k` (single-loop immersion), `/en/asics-cooling/immersion-systems/ic-1000`, `/en/products/container-hydro`, `/en/asics-cooling/hydro-systems/ahc-2.4`. One line each explaining when to pick it [VERIFY].

### H2: FAQ

---

## Key Entities and Terms to Include

ASIC miner, Antminer, Whatsminer, 20 ft / 40 ft container, ISO container, immersion cooling, dielectric fluid, dry cooler, heat exchanger, power distribution, PDU, transformer, three-phase power, hashrate, J/TH, ambient temperature, commissioning, AMS, firmware profiles, heat reuse, lead time.

Do not use: "profitability", "guaranteed hashrate increase", "+40% hashrate", "-30% power" (unless the product team provides a named source, then cite it on the page) [VERIFY].

---

## FAQ (5–7 questions)

1. **How much does a mining container cost?** Answer with cost drivers and "request a quote"; no number unless the team publishes a price [VERIFY].
2. **How many ASIC miners fit in a 20 ft and a 40 ft container?** [VERIFY per model family].
3. **What power supply does the site need?** [VERIFY input spec]. Link PDU.
4. **What temperature range can the container operate in?** [VERIFY].
5. **Immersion container vs hydro container: which should I choose?** Short answer + links to container-1k and hydro-systems.
6. **Can I monitor and restart miners remotely?** AMS + PDU [VERIFY capabilities].
7. **How long does delivery and commissioning take?** [VERIFY].

---

## Cannibalization (GSC 2026-09-28)

`crypto mining shipping container` (189 impr): 72% on the product page (pos 19.3), 28% on the blog post `how-shipping-containers-change-the-cryptocurrency-mining-industry` (pos 51.8). Same pattern for `bitcoin mining shipping container`, `shipping container mining`, `industrial container bitcoin mining`.
- Action (blog-plan K4 / EN-FEB-4): the blog post becomes informational (history, why containers, site-planning checklist at a general level), removes commercial wording from its title/H1, and links to `/en/products/container` with the anchor "BiXBiT immersion mining containers". Suggest moving EN-FEB-4 up to November 2026, ahead of the seasonal peak [decision: blog owner].
- The product page does not add a history/"how containers changed mining" section.

---

## E-E-A-T Signals

- Named engineer/reviewer and date of last technical review [VERIFY].
- Real deployment photos (with descriptive alt text) and, if allowed, a named deployment [VERIFY which references may be published].
- Spec sheet linked and dated.
- Clear statement of what is and is not included in the scope.

## Internal Links

Out: `/en/products/container-1k`, `/en/products/container-hydro`, `/en/asics-cooling/hydro-systems/ahc-2.4`, `/en/asics-cooling/immersion-systems/ic-1000`, `/en/products/coolant`, `/en/products/pdu`, `/en/ams`, `/en/calc`, `/en/firmwares/antminer` (tuning section).
In: `/en/asics-cooling` (hub navigation), `/en/products` (catalog card), `/en/products/rack`, blog `how-shipping-containers-change-the-cryptocurrency-mining-industry`, blog `how-to-make-1500-asics-out-of-1000-bought-the-magic-of-immersion-cooling`. Full list: `content/internal-linking.md` → Hardware.

## Schema Recommendation

Keep existing `Product` + `BreadcrumbList`; update `description`, add verified `additionalProperty` values. Review `AggregateRating` [VERIFY source]. Add `FAQPage` only with the visible FAQ (never an empty FAQPage, see crawl P1).

## Word Count Target

1 200–1 600 words (current page ~930). Tables and the checklist carry most of the value.

## [VERIFY] Blockers — DO NOT PUBLISH WITHOUT RESOLVING

1. Container lengths, miner capacity per model, power capacity.
2. Ambient temperature range (current meta: -40°C to +40°C).
3. Heat rejection design and coolant volume.
4. Scope of delivery, lead time, warranty/support terms.
5. Telemetry available in AMS for containers.
6. Source for "+40% hashrate, -30% power" in the current description, and the "profitability" H3 wording (remove if unsourced).
7. Which deployments can be named.
