# Content Brief: Hardware Hub — Cooling Systems for ASIC Mining
**Slug:** `/en/asics-cooling` (existing)
**Cluster:** hardware (`content/clusters/hardware.md`). Shared page: the immersion cluster owns the "immersion vs hydro vs air" comparison block on it (architecture v2 #17, P2, content-plan W11).
**Brief type:** Hub (commercial investigation + navigation)
**Created:** 2026-09-28
**Author assignment:** Head of cooling engineering [VERIFY: assign real name]

**Priority:** P1. The hub has 1 216 impressions and 0 clicks in 28 days (GSC, position 14.5), but most impressions are the brand query `bixbit` (277, pos 1.1, a sitelink-style appearance). Non-brand: `crypto mining cooling systems` GSC 27.3, `asic cooler` #26 (40/mo), `asic miner cooling system` GSC 30.3, `mining cooling solutions` 10/mo. Small direct demand; the value is **distribution of internal links** to the hardware product URLs (the 8 model pages get 2 internal links each today), plus the brand CTR. Not P0: no quick-win keyword.
**Target (architecture v2):** `/en/asics-cooling` (existing, architecture v2 #17). This brief adds the navigation/product layer; the comparison block stays as specified in the immersion cluster.

---

## Page Goal

One page that tells a farm operator or data center lead which BiXBiT cooling system fits their site (hydro, immersion, containerized, server) and sends them to the right sub-hub or product in one click. Secondary goal: a clean, citable entity description of BiXBiT as a cooling hardware vendor (GEO), consistent with the Organization description fix (P0 in `docs/agent-knowledge.md` §3).

## Search Intent

**Primary:** commercial investigation: "crypto mining cooling systems", "ASIC miner cooling system", "mining cooling solutions".
**Secondary:** brand navigation (`bixbit`, `bixbit immersion cooling` 25+18 impressions).
**Do NOT optimize for:** `immersion cooling` head terms (immersion pillar and blog), `asic cooler` as a consumer fan product (the SERP is mixed; keep the phrase only in the body).

---

## Target Keywords

> Volumes: DataForSEO Google Ads, US / en, 2026-09-28. `#N`: DataForSEO ranked_keywords 2026-09-25. GSC: average position, all countries, 28 days.

| Type | Keyword | Vol (US) | CPC | KD | BiXBiT pos |
|---|---|---|---|---|---|
| Primary | `crypto mining cooling systems` | n/d (GSC 16 + 33 impr on hub/hydro) | — | — | GSC 27.3 |
| Secondary | `asic miner cooling system` / `asic cooling system` | 10 / 10 | — | n/d | GSC 30.3 |
| Secondary | `mining cooling solutions` | 10 | — | n/d | GSC 28.2 (hydro-systems) |
| Secondary | `mining farm cooling` / `crypto mining cooling` | 10 / 10 | — | n/d | — |
| Secondary | `asic cooler` | 40 | $0.21 | n/d | #26 |

Cannibalization: `crypto mining cooling systems` 61% hydro-systems (pos 37.1) / 30% hub (pos 27.3); `asic miner cooling system` split across cell, hydro-systems and hub. The hub takes the general "cooling systems" phrasing; hydro-systems keeps "hydro cooling system".

---

## H1

Cooling Systems for ASIC Mining: Hydro and Immersion

(Title: "Crypto Mining Cooling Systems: Hydro & Immersion | BiXBiT"; see `hardware-product-title-template.md`.)

---

## Page Structure (extend the live page; keep existing H2s where marked)

### Intro (40–60 words)
Who BiXBiT is as a cooling vendor and what it supplies: hydro racks and containers, immersion tanks and containers, dielectric coolant, server/data center cooling, with PDUs and AMS monitoring. No performance percentages unless sourced [VERIFY].

### H2: Choose a Cooling System (new, core of the hub)
Decision cards, each with 1–2 lines and a crawlable link:
- Hydro cooling for hydro miners → `/en/asics-cooling/hydro-systems`
- Immersion cooling for air-cooled ASICs → `/en/asics-cooling/immersion-systems`
- Mining containers (immersion, single-loop, hydro) → `/en/products/container`, `/en/products/container-1k`, `/en/products/container-hydro`
- Racks and tanks → `/en/products/rack`, `/en/products/rack-hydro`, `/en/products/cell`
- Dielectric coolant → `/en/products/coolant`
- Server and prefab data center cooling → `/en/products/server`
- Power distribution → `/en/products/pdu`

### H2: All Models (new)
Compact table: model, type, miner family, format, link. Rows: WHR-200-2U, AHR-200, WHC-1.2-2U, WHC-2.4-2U, HW-Cluster-2.4, AHC-2.4, ICT-100, IC-1000 (+ legacy products if still sold [VERIFY]). Capacity column only with verified values [VERIFY].

### H2: Immersion vs Hydro vs Air (owned by the immersion cluster, content-plan W11)
Short comparison block per `content/clusters/immersion-cooling-mining.md` (links C2, C10). Do not expand here; link the planned blog EN-JAN-1.

### H2: Product Benefits / Why Choose Us (exists)
Rewrite claims into verifiable statements (engineering in-house, spec sheets, AMS integration, warranty terms) [VERIFY each]. Remove unsourced percentages.

### H2: BiXBiT Ecosystem and AMS (exists)
Keep; one link to `/en/ams`, one to `/en/firmwares` ("firmware profiles for immersion and hydro").

### H2: Company Development Stages (exists)
Keep as E-E-A-T timeline (prototype → production line → immersion containers → hydro container → Smart PDU; cooperation with Cormint) [VERIFY years and wording]. Link each product milestone to its page.

### H2: Engineering and Project Design Services / Heat Reuse (exist)
Keep; link heat-reuse to hydro-systems heat-reuse section.

### H2: FAQ (new)

---

## Key Entities and Terms to Include

BiXBiT, ASIC mining, hydro cooling, immersion cooling, direct-to-chip, dielectric coolant, mining container, hydro container, immersion tank, rack, dry cooler, heat reuse, PDU, AMS, Antminer, Whatsminer, data center, prefab data center.

---

## FAQ (4–6 questions)

1. **Which cooling system is right for my mining site?** Conditional answer (miner type: hydro vs air-cooled; climate; density) + links.
2. **Can air-cooled ASICs be moved to immersion?** Short answer + link to immersion pillar [VERIFY BiXBiT guidance].
3. **Do you supply complete containerized solutions?** Links to container pages [VERIFY scope].
4. **Does BiXBiT cool servers and data centers, not only ASICs?** Link `/en/products/server`.
5. **How are BiXBiT cooling systems monitored?** AMS link.

---

## E-E-A-T Signals

- Named engineering lead; timeline with verified dates.
- Links to spec sheets and project references [VERIFY publishable].
- Consistent entity description (the sitewide `Organization.description` fix is tracked separately; do not duplicate it here).

## Internal Links

Out: every URL in "Choose a Cooling System" + all 8 model pages + `/en/ams`, `/en/firmwares`. This is the main fix for the model pages' 2-link problem.
In: homepage cooling block, main menu (exists), `/en/products` catalog, hydro/immersion sub-hubs (breadcrumb), blog posts `asic-cooling-trends-2026`, PUE post (EN-OCT-3), DC cooling posts (EN-JUN-2). Full list: `content/internal-linking.md` → Hardware.

## Schema Recommendation

`CollectionPage` + `ItemList` (models) + `BreadcrumbList`; `FAQPage` only with the visible FAQ. Currently only WebSite + Organization. Also add the page to the sitemap (dev-task P2).

## Word Count Target

1 300–1 600 words (current ~1 230); most additions are the decision cards, model table and FAQ.

## [VERIFY] Blockers — DO NOT PUBLISH WITHOUT RESOLVING

1. Model table values (type, miner family, capacity).
2. Which legacy-template products are current.
3. Timeline dates and partner names allowed in public copy.
4. Every claim in "Product Benefits" / "Why Choose Us".
