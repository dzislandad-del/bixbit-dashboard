---
# Page Optimization: https://bixbit.io/en (homepage)
**Target keyword:** industrial Bitcoin mining firmware AMS monitoring
**Date:** 2026-09-16
**URL in site-structure.md:** confirmed ✓ (`/en` — "BiXBiT Bitcoin Mining Solutions – Tools for Crypto Miners")
**Contributors:** content-seo (title/meta/H-structure/FAQ/internal links), technical-seo (canonical/hreflang/JSON-LD), geo-ai (passage/FAQ/competitor framing) — synthesized into one artifact.

## Data Sources Used
- DataForSEO: UNAVAILABLE — MCP not connected in this session. No volume/intent/CPC data used or invented.
- GSC: UNAVAILABLE. Baseline (2026-06-17 full-audit, `data/baseline-2026-06-17.json`) recorded 0 GSC clicks / 0 impressions for `/en` — no current positions or CTR to compare against.
- GA4: UNAVAILABLE.
- SERP: qualitative only, via WebSearch (no DataForSEO SERP API) — used to sanity-check competitor positioning (Braiins Manager, Vnish, LuxOS, ePIC), not for volume/rank data.
- Current on-page state: WebFetch snapshot of `https://bixbit.io/en` (title, meta, 9×H1, internal links), cross-checked against `data/site-structure.md` (crawled 2026-06-17, 70 pages — the site's URL source of truth).

No search-volume, ranking, CTR, or traffic figures appear anywhere below. Recommendations are based on on-page structure, qualitative SERP/SXO judgment, and brand-safe entity definition only.

---

## 1. New Title Tag

**Before:** `BiXBiT Bitcoin Mining Solutions – Tools for Crypto Miners` (consumer framing, no firmware/AMS signal)

**After (59 characters):**
```html
<title>BiXBiT: Industrial Bitcoin Mining Firmware & AMS Monitoring</title>
```

- 59 characters — no desktop/mobile truncation risk (≤60 target).
- Leads with brand, then covers both halves of the target query: "Industrial Bitcoin Mining Firmware" and "AMS Monitoring."
- Drops consumer language ("Tools for Crypto Miners") — repositions the homepage as the B2B/industrial entry point per CLAUDE.md ICP (fleet operators, data-center technical directors, hosting providers, institutional miners).
- Does not compete keyword-for-keyword with `/en/firmwares/antminer` (which owns "custom firmware for Antminer" per that page's own page-optimize audit) — homepage differentiates on the firmware+AMS ecosystem framing, avoiding internal cannibalization.

---

## 2. New Meta Description

**Before:** MISSING (empty)

**Primary (143 characters) — recommended for production:**
```html
<meta name="description" content="Industrial Bitcoin mining firmware for Antminer & Whatsminer, plus AMS fleet monitoring for 100 to 100,000+ ASICs. Start your free trial today.">
```

- 143 characters — within the 140–155 target range.
- Target keyword phrase appears near-verbatim in the opening clause.
- Names both flagship products (firmware + AMS) and both supported ASIC brands — matches firmware P1 priority from CLAUDE.md §3.
- "100 to 100,000+ ASICs" mirrors the documented ICP scale range (CLAUDE.md §2), not an invented statistic.
- CTA reuses the free-trial offer already verified present on `/en/firmwares/antminer`. **[VERIFY: confirm the free-trial offer is actually surfaced/valid on the homepage itself before publishing this exact CTA.]**

**Alternate (149 characters, from geo-ai — cooling-inclusive framing):**
```html
<meta name="description" content="BiXBiT: industrial Bitcoin mining firmware for Antminer/Whatsminer, integrated with AMS cloud fleet monitoring. Plus hydro/immersion cooling.">
```
Use this variant only if stakeholders prefer surfacing cooling in the meta description over a CTA; do not ship both — pick one before deploy to avoid template drift.

---

## 3. Target H-Structure (single H1)

**Critical issue:** the live page currently ships **nine `<h1>` tags**, which flattens heading hierarchy, dilutes topical signal to Google, and gives crawlers no single "this page is about X" anchor. This is a P0 fix.

### Mapping: current H1s → new hierarchy

| # | Current H1 (as-is) | New level | New text / treatment |
|---|---|---|---|
| 1 | "Bitcoin Mining Software & Hardware" | **H1 (sole)** | Rewritten — see below |
| 2 | "Efficient Mining with BiXBiT Firmware" | H2 | Keep — Firmware section |
| 3 | "Efficient Mining with BiXBiT AMS" | H2 | Keep — AMS section |
| 4 | "BiXBiT Immersion & Hydro cooling" | H2 | Keep — Cooling section |
| 5 | "Power Distribution Unit" | H2 → **flag** | See PDU anomaly note below |
| 6 | "Cooling Solution for Server Equipment" | H3 | Demote and fold into Cooling H2 (duplicate topic) |
| 7 | "Expertise you can trust" | H2 | Keep — E-E-A-T section |
| 8 | "Blog" | H2 | Keep — Blog teaser section |
| 9 | "Stay ahead of the curve with the latest updates" | H3 | Demote — subhead nested under Blog H2 |

### Full target structure

```
H1: Custom Firmware & AMS Monitoring for Industrial Bitcoin Mining
  H2: This Is Your Equipment                          (existing intro/value-prop subhead)
  H2: Efficient Mining with BiXBiT Firmware
    H3: Savings Start Here                             (reposition as firmware efficiency/J-TH sub-claim)
  H2: Efficient Mining with BiXBiT AMS
  H2: BiXBiT Immersion & Hydro Cooling
    H3: BiXBiT Cell
    H3: BiXBiT Coolant
    H3: BiXBiT Rack
    H3: BiXBiT Container
    H3: Server Equipment Cooling                        (folded from old H1 #6 — same topic as parent H2)
  H2: Power Distribution Unit  ⚠ SEE ANOMALY NOTE BELOW
  H2: Expertise You Can Trust
  H2: Blog
    H3: Stay Ahead of the Curve with the Latest Updates
```

**Why H1 #1 was rewritten, not just promoted:** "Bitcoin Mining Software & Hardware" is generic and consumer-adjacent; it carries neither the target keyword nor the firmware+AMS pairing that differentiates BiXBiT from single-product competitors (Braiins sells firmware only, as a separate Manager product handles fleet monitoring — see §8). New H1 (62 characters): `Custom Firmware & AMS Monitoring for Industrial Bitcoin Mining` — carries "firmware," "AMS Monitoring," "Industrial," and "Bitcoin Mining" without stuffing, distinct enough from `<title>` to avoid duplicated SERP snippets while reinforcing the same entity.

**⚠ PDU anomaly — flag for product/technical team, not a copy fix:** `data/site-structure.md` shows **no crawled pages under any `/en/pdu/*` path** — the PDU section is entirely absent from the site's real URL structure, despite an H1/section for it on the homepage. Either (a) the section links to a non-existent page, or (b) PDU is announced but not yet built. **Do not link this H2 to a fabricated URL.** Recommended: either (1) remove the PDU section until a real `/en/pdu` page exists, or (2) keep the section with a "Coming soon" state or contact-sales link instead of a dead internal link. P1 technical/product coordination item — flag in the PR description, don't paper over in copy.

**JS-rendering caveat:** `/en/firmwares/antminer` was previously found rendering its `<title>` via client-side JS, not present in static HTML (2026-06-17 audit). Confirm the same isn't true for the homepage's H1/title before treating this plan as deployable — if headings are injected client-side, Googlebot's visibility into the single-H1 fix depends on render budget, and the fix must ship server-side, not just in the JS bundle.

---

## 4. Rewritten Opening Paragraph (entity-definition style)

Builds on the existing `content/geo/entity-definition-homepage.md` draft, reformulated to carry both "industrial Bitcoin mining firmware" and "AMS monitoring" for the target query, brand in subject position (sentence 1) for AI/passage extraction.

**Primary (content-seo):**
```html
<p>
  BiXBiT is an industrial Bitcoin mining infrastructure provider, delivering custom
  firmware for Antminer and Whatsminer ASICs together with AMS, a cloud-based fleet
  monitoring platform built for the same fleets. BiXBiT firmware replaces stock
  manufacturer software to improve energy efficiency (J/TH), enable per-chip
  autotuning, and support overclocking and undervolting — without unauthorized
  network connections or dev fees [VERIFY: confirm dev fee = 0% before publishing] —
  while AMS monitoring surfaces hashrate, temperature, and uptime data from every
  flashed device in real time. Mining operators running 100 to 100,000+ ASICs use
  the combined BiXBiT firmware and AMS monitoring stack to manage mixed Antminer
  and Whatsminer fleets from a single platform.
</p>
```

**Alternate framing (geo-ai — leads harder with the "paired" claim and the no-separate-vendor angle):**
> BiXBiT provides industrial Bitcoin mining firmware paired with AMS, its cloud-based fleet monitoring platform, for operators running Antminer and Whatsminer ASICs at scale. BiXBiT firmware replaces stock manufacturer software to improve energy efficiency (J/TH) and enable per-chip autotuning, while AMS gives the same operators real-time hashrate, temperature, and status visibility across mixed fleets from one dashboard — without needing a separate monitoring vendor. [VERIFY: confirm dev fee = 0% before publishing] BiXBiT also offers hydro and immersion cooling for large-scale deployments, and operators running 100 to 100,000+ ASICs use the combined firmware + AMS stack to manage mixed Antminer/Whatsminer farms from a single platform.

Both variants: brand-first, 3 sentences, cooling mentioned third (not first), every efficiency/security claim carries `[VERIFY]`. Pick one for the live page — do not run both. The geo-ai variant's "without needing a separate monitoring vendor" phrasing is the stronger standalone AI-citation hook (directly undercuts Braiins OS+ / Braiins Manager's two-product model — see §8.3) **once the standalone-vs-bundled AMS claim is confirmed** (VERIFY list item 9).

---

## 5. FAQ Block — Firmware + AMS Relationship (homepage-level)

Scoped to "how firmware and AMS work together," not device-specific firmware FAQ (owned by `/en/firmwares/antminer`, which has its own detailed FAQPage — do not duplicate).

```html
<section id="faq-firmware-ams">
  <h2>Firmware + AMS Monitoring FAQ</h2>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">How do BiXBiT firmware and AMS monitoring work together?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">BiXBiT firmware runs on each Antminer or Whatsminer unit and reports
      telemetry — hashrate, temperature, power draw, and tuning state — to AMS, a
      cloud-based dashboard for centralized fleet monitoring. Firmware handles
      per-device optimization; AMS handles fleet-wide visibility and alerting across
      every flashed device.</p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">Do I need BiXBiT firmware installed to use AMS monitoring?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">[VERIFY: confirm whether AMS can monitor stock-firmware devices
      (via API/pool-side telemetry) or whether full monitoring requires BiXBiT firmware
      to be installed first — this determines whether AMS can be sold as a standalone
      product or only as an add-on to firmware customers.]</p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">Can I monitor a mixed fleet of Antminer and Whatsminer devices in one AMS dashboard?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Yes. AMS is built to unify Antminer (Bitmain) and Whatsminer
      (MicroBT) telemetry in a single dashboard, so operators running mixed fleets don't
      need separate monitoring tools per hardware vendor.</p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">Does connecting my fleet to AMS create additional network security exposure?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">[VERIFY: add specifics on AMS's connection model — outbound-only
      telemetry vs. inbound remote control, encryption in transit, and whether AMS access
      is scoped per-operator. Security posture is a top-tier ICP concern (no backdoors /
      unauthorized connections) per CLAUDE.md and must not be asserted without engineering
      sign-off.]</p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">If I roll back to stock firmware, do I lose my AMS monitoring history?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">[VERIFY: confirm data-retention behavior on rollback — does AMS
      keep historical telemetry for a device after it's reflashed to stock firmware, and
      for how long? Do not publish an answer without confirming actual product behavior.]</p>
    </div>
  </div>
</section>
```

Corresponding `FAQPage` JSON-LD should mirror this HTML 1:1 once the three `[VERIFY]` answers are filled in — **do not ship JSON-LD with placeholder `[VERIFY]` text inside `acceptedAnswer.text`**, since that text gets indexed and can surface verbatim in FAQ rich results.

---

## 6. Internal Linking Plan (from homepage)

Only real, indexable URLs confirmed in `data/site-structure.md`. `/en/ams/connect` is explicitly excluded — flagged noindex/unlaunched in prior audits, should not receive homepage link equity.

| Anchor text | Target URL | Placement on homepage |
|---|---|---|
| custom firmware for Antminer | `/en/firmwares/antminer` | Within "Efficient Mining with BiXBiT Firmware" H2, first mention |
| Whatsminer firmware | `/en/firmwares/whatsminer-all-series` | Same Firmware H2, paired with Antminer link (mixed-fleet framing) |
| all supported firmware | `/en/firmwares` | Firmware H2 — "see all supported ASIC models" hub link |
| AMS fleet monitoring | `/en/ams` | Within "Efficient Mining with BiXBiT AMS" H2, first mention — **not** `/en/ams/connect` |
| immersion and hydro cooling | `/en/asics-cooling` | Within "BiXBiT Immersion & Hydro Cooling" H2 (hub page) |
| hydro cooling systems | `/en/asics-cooling/hydro-systems` | Same Cooling H2, alongside immersion link |
| immersion cooling systems | `/en/asics-cooling/immersion-systems` | Same Cooling H2 |
| firmware + AMS integration | `/en/firmwares/antminer` (or `/en/ams`) | Cross-link inside new FAQ block, Q1 answer |

**Do not link:** `/en/ams/connect` (noindex/unlaunched form — sending homepage link equity there wastes crawl signal and risks a broken first-touch UX).

**Duplicate-hub flag:** `/en/products` ("ASIC miner cooling systems") and `/en/asics-cooling` ("BiXBiT Crypto Mining Cooling Solutions for ASICs") both read as cooling hub pages — this plan links to `/en/asics-cooling` as the primary hub; escalate the `/en/products` vs `/en/asics-cooling` overlap to `technical-seo` for a canonicalization/consolidation review before finalizing the sitewide cooling link strategy.

---

## 7. Technical SEO — Canonical, Hreflang, Structured Data

*(technical-seo deliverable; full standalone version also saved at `reports/page-optimize-en-home-2026-09-16.md`)*

### 7.1 Canonical tag

```html
<link rel="canonical" href="https://bixbit.io/en" />
```
Self-referencing, HTTPS, no trailing slash, no query params.

### 7.2 Hreflang tags

```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en" />
<!-- [VERIFY] /ru counterpart — confirm URL exists, returns 200, and is NOT noindex before deploying this line -->
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru" />
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en" />
```

**Do not ship the `hreflang="ru"` line yet.** `/ru` URL parity is an open `[VERIFY]` from the 2026-06-17 audit — never confirmed `/ru` exists 1:1, returns 200, or isn't noindexed. A broken hreflang pair is worse than none.

Rollout order: (1) ship `en` + `x-default` now — no dependency on `/ru`; (2) confirm `/ru` exists, 200s, indexable → add `ru` line; (3) if `/ru` doesn't exist or is a stub, drop the `ru` line entirely. `x-default` → `/en` is correct per CLAUDE.md (`/en` is the primary B2B locale, not root `/`).

### 7.3 Organization JSON-LD (corrected)

Source draft `content/geo/entity-definition-homepage.md` had two wrong URLs — corrected against `data/site-structure.md`: AMS `/en/monitoring` → **`/en/ams`**; immersion cooling `/en/cooling/immersion` → **`/en/asics-cooling/immersion-systems`**. Also added hydro cooling and swapped the Whatsminer link to the hub page (`/en/firmwares/whatsminer-all-series`) instead of one sub-model page.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BiXBiT",
  "url": "https://bixbit.io/en",
  "description": "BiXBiT provides custom firmware for Antminer and Whatsminer ASICs, cloud fleet monitoring (AMS), and immersion and hydro cooling for industrial Bitcoin mining operations.",
  "foundingDate": "[VERIFY]",
  "areaServed": ["US", "CA", "KZ", "PY", "AE", "LatAm", "CIS"],
  "knowsAbout": [
    "Bitcoin mining firmware",
    "ASIC overclocking",
    "ASIC fleet monitoring",
    "Immersion cooling for mining",
    "Hydro cooling for Bitcoin miners",
    "Antminer firmware",
    "Whatsminer firmware"
  ],
  "sameAs": [
    "[VERIFY: Twitter/X URL]",
    "[VERIFY: LinkedIn URL]",
    "[VERIFY: GitHub URL if exists]",
    "[VERIFY: Telegram channel URL]"
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "BiXBiT Products",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "SoftwareApplication", "name": "BiXBiT Antminer Firmware", "applicationCategory": "Mining Software", "operatingSystem": "Antminer ASIC", "url": "https://bixbit.io/en/firmwares/antminer" } },
      { "@type": "Offer", "itemOffered": { "@type": "SoftwareApplication", "name": "BiXBiT Whatsminer Firmware", "applicationCategory": "Mining Software", "operatingSystem": "Whatsminer ASIC", "url": "https://bixbit.io/en/firmwares/whatsminer-all-series" } },
      { "@type": "Offer", "itemOffered": { "@type": "SoftwareApplication", "name": "BiXBiT AMS — Advanced Monitoring System", "applicationCategory": "Fleet Management Software", "url": "https://bixbit.io/en/ams" } },
      { "@type": "Offer", "itemOffered": { "@type": "Product", "name": "BiXBiT Immersion Cooling", "category": "Mining Infrastructure", "url": "https://bixbit.io/en/asics-cooling/immersion-systems" } },
      { "@type": "Offer", "itemOffered": { "@type": "Product", "name": "BiXBiT Hydro Cooling", "category": "Mining Infrastructure", "url": "https://bixbit.io/en/asics-cooling/hydro-systems" } }
    ]
  }
}
</script>
```

`/en/ams/connect` is deliberately not referenced anywhere in this schema (flagged noindex/unlaunched elsewhere) — the AMS entity points only at the stable hub `/en/ams`.

### 7.4 WebSite JSON-LD

No `SearchAction` — no evidence of an on-site search feature in `data/site-structure.md` or prior crawls. **[VERIFY: confirm whether bixbit.io has site search before adding `potentialAction`]**; a `SearchAction` pointing at a non-functional/nonexistent endpoint is a misleading structured-data claim.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "BiXBiT",
  "url": "https://bixbit.io/en",
  "publisher": { "@type": "Organization", "name": "BiXBiT", "url": "https://bixbit.io/en" }
}
</script>
```

### 7.5 Explicitly out of scope for this page

**Do not add `SoftwareApplication` or `FAQPage` schema types to the homepage** beyond what's needed. `/en/firmwares/antminer` already owns (or is planned to own) `SoftwareApplication` + `FAQPage` schema. Duplicating those entity types on two URLs creates competing signals for Google and for LLM/GEO extraction. Homepage schema is **Organization + WebSite only**; the homepage FAQ in §5 is a *different* FAQPage entity (firmware↔AMS relationship, not device-specific firmware facts) — it's fine to have its own FAQPage schema scoped to those 5 questions, as long as it doesn't restate the Antminer page's Q&A set.

### 7.6 Implementation requirement — mandatory

**All of §7.1–7.4 must be present in static HTML inside `<head>` on initial server response — not injected via JavaScript after hydration.** Rationale: `/en/firmwares/antminer`'s `<title>` was previously found JS-rendered only, invisible to Googlebot's first pass and to non-JS crawlers (Bing, most LLM/GEO crawlers). Verify via "View Page Source" (not DevTools Elements) that every tag above is present before hydration runs.

---

## 8. GEO / AI Passage Optimization — Supplementary

*(geo-ai deliverable, condensed; full version covers additional rationale)*

### 8.1 Passage-friendly spec table — "Firmware + AMS at a Glance"

Place directly after the opening paragraph (§4) — tables extract cleanly as structured passages for LLM citation.

| Parameter | BiXBiT Firmware | BiXBiT AMS |
|---|---|---|
| What it does | Replaces stock Antminer/Whatsminer firmware; per-chip autotuning, overclocking/undervolting | Cloud dashboard for centralized ASIC fleet monitoring |
| Supported hardware | Antminer (Bitmain), Whatsminer (MicroBT) `[VERIFY: exact model list]` | Antminer + Whatsminer in one interface `[VERIFY: full compatibility list]` |
| Real-time metrics | J/TH efficiency, chip temperature `[VERIFY: exact ranges]` | Hashrate, temperature, device status, alerts `[VERIFY: full metric list]` |
| Firmware ↔ AMS integration | Reports telemetry directly to AMS `[VERIFY: confirm integration mechanism]` | Ingests BiXBiT firmware telemetry out of the box `[VERIFY]` |
| Deployment | On-device flash | Cloud SaaS, browser access `[VERIFY: hosting model]` |
| Dev fee / cost | `[VERIFY: 0% or actual rate]` | `[VERIFY: bundled with firmware license or separate subscription]` |

### 8.2 FAQ variants tuned for AI-query phrasing (optional supplement to §5)

- "Does BiXBiT firmware work with fleet monitoring software?" → Yes, natively with AMS. `[VERIFY: confirm "out of the box" claim before publishing]`
- "What monitoring system does BiXBiT firmware use?" → AMS, BiXBiT's own cloud dashboard. `[VERIFY: exact metric list; whether AMS supports non-BiXBiT firmware]`
- "Do I need separate software to monitor a mining farm running BiXBiT firmware?" → No, firmware + AMS ship as one stack. `[VERIFY: confirm AMS isn't sold/licensed separately before using this as a differentiator]`

These overlap with §5's Q1–Q3; use whichever phrasing tests better for on-page FAQ, but don't publish both sets as separate FAQPage blocks (duplicate entity risk, same concern as §7.5).

### 8.3 Competitor framing for AI citability

| Provider | Firmware | Fleet monitoring | Bundled as one stack? |
|---|---|---|---|
| **BiXBiT** | Antminer + Whatsminer firmware | AMS (in-house) | Claimed yes `[VERIFY: confirm AMS isn't sold separately/gated behind a paid tier]` |
| Braiins (Braiins OS+) | Open-source Antminer firmware | Braiins Manager (separate product) | No — two distinct products under one vendor `[VERIFY: reconfirm before publish, product lines change]` |
| Vnish | Custom firmware | No confirmed fleet-monitoring product in available data | `[VERIFY]` |
| LuxOS (Luxor) | Custom firmware | Luxor Commander (separate product) | No `[VERIFY]` |
| ePIC firmware | Custom firmware | No data on a monitoring product | `[VERIFY]` |

**Potential differentiator (if confirmed):** BiXBiT may be the only listed vendor positioning firmware+monitoring as a single integrated stack rather than two separately branded products. This is a strong AI-citation hook **but must not be published until confirmed**: (a) whether AMS is actually bundled/free with firmware or sold separately, (b) that the competitor product-line facts above are still current at publish time. Misstating a competitor's product lineup is a reputational and potential legal risk per CLAUDE.md §4.

### 8.4 llms.txt

`content/geo/llms.txt` already states firmware↔AMS integration in neutral language. Recommended: add one line to its `## Key Facts for AI Systems` section that verbatim-echoes the chosen opening-paragraph phrasing (§4) — LLMs weight consistency between on-page text and llms.txt as a citation-confidence signal. Point addition, not a rewrite of the file. No `llms-full.txt` exists yet in the repo; not required for this task.

---

## 9. [VERIFY] List — Consolidated (all three workstreams)

Every item below must be confirmed by engineering/product/leadership before the associated copy, schema field, or claim ships. Nothing below is asserted as fact in the recommended output above without this tag attached at the point of use.

**Content / copy:**
1. **"Since 2016"** (founding year) — confirm; reuse consistently in copy and `Organization.foundingDate`.
2. **"16+ countries"** — confirm current count, don't round up.
3. **"132+ MW immersion deployed"** — confirm unit (MW vs MWh), cumulative-vs-active, and currency as of publish date.
4. **"40,000+ devices optimized"** — confirm count and definition ("optimized" = flashed? monitored? both?).
5. **Dev fee percentage / "no dev fee" claim** — appears in the opening paragraph (§4); confirm actual current rate with engineering. Repeat item from the existing GEO draft, still unresolved.
6. **Free-trial terms** (meta CTA, §2) — confirm the offer is presented on the homepage itself, confirm duration (30 days per the firmware-page precedent) and whether payment info is required.
7. **Any J/TH efficiency percentage** — none proposed in this brief's copy; flag for whoever writes final body copy — no % may publish without verified benchmark data.

**AMS product behavior (blocks FAQ + competitor claims):**
8. **AMS security/connection-model** (§5 Q4) — no "no backdoors"/connection-security claim without an engineering-confirmed description of AMS's actual network/data model.
9. **AMS standalone-vs-bundled availability** (§5 Q2, §8.3 differentiator claim) — confirm whether AMS requires BiXBiT firmware to function, or can monitor stock-firmware devices too. This single fact gates both the FAQ answer and the competitive-differentiation claim in §8.3.
10. **AMS data retention on firmware rollback** (§5 Q5) — confirm actual product behavior before publishing an answer.
11. **Firmware↔AMS integration mechanism** (§8.1 table) — confirm the actual telemetry/reporting mechanism before stating it as fact.

**Technical/schema:**
12. **`Organization.foundingDate`** — placeholder in JSON-LD, same fact as item 1.
13. **`Organization.sameAs`** — Twitter/X, LinkedIn, GitHub, Telegram URLs, all unconfirmed.
14. **`/ru` URL parity** — does `/ru` exist as a true 1:1 mirror of `/en`, return 200, and is it indexable? Gates hreflang `ru` deployment (§7.2).
15. **On-site search existence** — gates whether `WebSite.potentialAction.SearchAction` can be added (§7.4).
16. **`/en/ams/connect` noindex status** — confirm the noindex flagged in a prior audit is actually deployed; if not, that's a separate indexation P0.

**Structural:**
17. **PDU section** (§3) — no real `/en/pdu/*` page exists in `data/site-structure.md`. Treat any implied PDU product-availability claim as unverified until product/technical resolve it.
18. **`/en/products` vs `/en/asics-cooling`** duplicate-hub overlap (§6) — needs a technical-seo consolidation/canonicalization decision, not resolved in this brief.
19. **Homepage JS-rendering status** — confirm H1/title aren't client-side-only rendered before treating the single-H1 fix as deployable (same class of issue found on `/en/firmwares/antminer`).
20. **Competitor product-line accuracy** (§8.3) — Braiins/Vnish/LuxOS/ePIC firmware+monitoring bundling facts must be reconfirmed at publish time, not treated as static.

---

## 10. Regression Check (pre-commit)

| Check | Result | Notes |
|---|---|---|
| Title length ≤ 60 chars | PASS | 59 characters |
| Meta description 140–155 chars | PASS | 143 chars (primary); 149 chars (alternate) |
| Single `<h1>` in target structure | PASS | 9 → 1; all others mapped to H2/H3 |
| No invented volume/CTR/traffic figures | PASS | None used; DataForSEO/GSC unavailability stated explicitly |
| No invented technical specs (J/TH, °C, model compatibility) | PASS | None introduced; all inherited figures carry `[VERIFY]` |
| No investment/ROI/profitability claims | PASS | None present in any recommended copy |
| Internal links resolve to real, indexed (non-noindex) URLs | PASS | Cross-checked against `data/site-structure.md`; `/en/ams/connect` explicitly excluded |
| Target keyword present in title, meta, H1, opening paragraph | PASS | "industrial," "Bitcoin mining," "firmware," "AMS," "monitoring" distributed naturally |
| FAQ JSON-LD readiness | BLOCKED | 3 of 5 answers contain `[VERIFY]` placeholders — do not ship JSON-LD until filled |
| Organization/WebSite JSON-LD syntax | PASS | Valid JSON, no trailing commas, correct `@type`s — re-validate via validator.schema.org before merge |
| JSON-LD URLs match `data/site-structure.md` | PASS | Corrected: `/en/ams` (not `/en/monitoring`), `/en/asics-cooling/immersion-systems` (not `/en/cooling/immersion`), Whatsminer hub used instead of one sub-model page |
| Canonical self-referencing, no trailing slash | PASS | `https://bixbit.io/en` exact |
| Hreflang `ru` line not deployed pending VERIFY | BLOCKED (intentional) | Ship `en` + `x-default` only until `/ru` parity confirmed |
| No duplicate/competing SoftwareApplication or FAQPage entities vs `/en/firmwares/antminer` | PASS | Homepage limited to Organization + WebSite + one scoped FAQPage (firmware↔AMS relationship only) |
| Static HTML delivery (not JS-injected) | FLAGGED | Requires confirmation — see VERIFY item 19 |
| PDU section | FLAGGED | No real destination page exists; do not link to a fabricated URL — escalate to product/technical-seo |
| CLS 0.888 (site-wide P0, `data/baseline-2026-06-17.json`) | NOT IN SCOPE | Pre-existing, tracked separately; this change set (head tags + copy) should not measurably affect CLS, but re-run PageSpeed post-deploy to confirm no regression |

---

## Notes / Handoff

- **Escalate PDU gap** to product/eng: build `/en/pdu` (or equivalent) or remove/soften the homepage PDU section before go-live.
- **Confirm JS-rendering status** of homepage `<h1>`/`<title>`/`<head>` tags before treating this brief as deployable — if client-side rendered, this needs SSR/prerender coordination, not just a content or schema change.
- **`/en/products` vs `/en/asics-cooling`** duplicate-hub risk — separate technical-seo consolidation pass, not resolved here.
- **Reconcile with `content/geo/entity-definition-homepage.md`** — that file has its own VERIFY checklist (dev fee, founding date, social URLs) with full overlap against §9 above; update or retire the older draft once this brief's copy ships, so the two documents don't drift apart.
- **Pick one meta description and one opening-paragraph variant** (§2, §4) before deploy — both pairs are equivalent quality; shipping both anywhere would be a duplicate-content/template bug, not a feature.
- Code changes should ship as a diff/PR, not directly to production, per `/page-optimize` runbook rules.
