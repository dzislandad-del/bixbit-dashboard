---
# Page Optimization: /en/firmwares (category hub)
**Target keyword:** custom firmware for ASIC miners
**Page type:** Category hub — lists all firmware lines (Antminer + Whatsminer); must NOT cannibalize child pages
**Date:** 2026-09-16
**URL in site-structure.md:** confirmed — "BiXBiT Custom ASIC Mining Firmware" (crawled 2026-06-17)
**Contributors:** content-seo (title/meta/H-structure/opening paragraph/FAQ/internal links — this file), technical-seo (canonical/hreflang/schema, §8, originally `content/page-optimize/firmwares-hub.md`), geo-ai (alternate passage/spec table/differentiator, §9). Synthesized into one artifact — geo-ai's deliverable was originally written to this same filename and was overwritten by content-seo's pass; both are preserved below.

## Data Sources Used
- GSC: UNAVAILABLE — not connected this session
- DataForSEO: UNAVAILABLE — not connected this session
- SERP/volume: not queried — no invented numbers below; all recommendations are qualitative/structural
- On-page snapshot: via WebFetch of the live page (this session)

**Cannibalization guardrail:** `/en/firmwares/antminer` already targets "custom firmware for Antminer" (see `content/page-optimize/firmwares-antminer.md`). This hub targets the broader, brand-agnostic query "custom firmware for ASIC miners" — comparison/selection intent across both brands, not a single-brand product query. Title, meta, H1, and opening paragraph below are deliberately phrased to differ from the Antminer child page.

---

## 1. Title Tag

**Before:** `BiXBiT Custom ASIC Mining Firmware` (35 chars — decent but doesn't contain the target phrase)

**After:** `Custom Firmware for ASIC Miners | BiXBiT` (40 chars)

- Leads with the exact target phrase "custom firmware for ASIC miners" (category-level, brand-agnostic)
- Brand in second position, consistent with the pattern used on `/en/firmwares/antminer`
- Deliberately does NOT say "Antminer" or "Whatsminer" by name in the title — avoids direct keyword overlap with child pages while still being the natural umbrella term a searcher comparing both brands would use

---

## 2. Meta Description

**Before:** MISSING (confirmed absent on live page)

**After (140 chars):**
```
BiXBiT custom firmware for ASIC miners: overclocking, autotuning & efficiency tuning for Antminer and Whatsminer. Dev fee 2.8% (2% for M2x).
```

- 140 characters — within the 140–155 target range
- Target phrase in the first clause
- Covers both brands explicitly (Antminer + Whatsminer) — signals category scope to searchers and to Google that this is the umbrella page, not a single-brand duplicate
- Dev fee figure (2.8%, 2% for M2x) is a **published, on-page fact** — the one place in this project where this number does not need `[VERIFY]` to appear in copy. Still flagged below for periodic reconfirmation since commercial terms can change (see VERIFY list, item 1).
- No invented performance/efficiency percentages

---

## 3. Heading Structure

### Issues identified in current structure
1. **Typo:** H3 "Feedback on bone work from our partner" — almost certainly a content error (likely intended "done work" or "our work"). Flagged as `[VERIFY]` below; do not silently guess-fix in CMS without content-team confirmation, since it may also be a mistranslation from the RU source.
2. **Near-duplicate headings at different levels:** H2 "Optimize Mining with ASIC Custom Firmware" and H3 "Optimize mining with BiXBiT firmware" say almost the same thing. Recommend giving each section a distinct job: the H2 becomes the brand-selector section (Whatsminer/Antminer picker), and the H3 is repositioned as the page's closing CTA with distinct wording.

### Recommended H2 rename
"Optimize Mining with ASIC Custom Firmware" → **"Choose Firmware by ASIC Brand"** (this is the section that actually contains the Whatsminer/Antminer H3 picker cards — the new heading matches its real function and stops overlapping semantically with the target phrase already covered by H1/title/meta, avoiding on-page keyword dilution).

### Recommended H3 rename (closing CTA)
"Optimize mining with BiXBiT firmware" → **"Start Optimizing Your Fleet with BiXBiT"** (keeps CTA intent, removes duplication with the H2 above and with the H1).

### Final H1→H4 hierarchy

```
H1: BiXBiT Custom Firmware for ASIC Miners — Antminer & Whatsminer
  (reordered from current "BiXBiT Custom firmware for Whatsminer & Antminer" to
  lead with the target category phrase; both brand names retained)

  H2: Take Control of Your Mining
    H3: Increase mining efficiency
    H3: Advanced Management Made Easy
    H3: Smart Cooling & Noise Control

  H2: Choose Firmware by ASIC Brand   [renamed — see above]
    H3: Whatsminer Firmware
      H4: M7x | M6x | M5x | M3x | M2x
    H3: Antminer Firmware
      H4: S21 | S19 | T21 | T19 | L9 | L7

  H2: Strategic Partnerships for Advanced Mining Efficiency
    (Enterprise section: reduced dev fee, custom feature development,
    white-label branding, mass installation, 24/7 support — keep as-is)

  H2: Free Access to the BiXBiT AMS Monitoring System with the Firmware
    (unchanged — strong differentiator, keep prominent)

  H2: FAQ
    H3: [existing FAQ topics — cost/fee, installation, profile generation,
        hashrate optimization, warranty, rollback, SD card issues, boot
        issues, firmware security, Antminer access]
    H3: What is the difference between BiXBiT firmware for Antminer and
        Whatsminer?                                          [NEW]
    H3: Does the developer fee differ between Antminer and Whatsminer
        firmware lines?                                      [NEW]
    H3: Which ASIC miner brands and series does BiXBiT firmware support? [NEW]
    H3: Knowledge Base
    H3: Feedback on Completed Work from Our Partners
        [VERIFY: original copy reads "bone work" — likely typo for "done
        work" or "our work"; confirm intended wording with content team
        before publishing]
    H3: Have Questions?

  H2: Try Other BiXBiT Products

  H2: Start Optimizing Your Fleet with BiXBiT   [renamed — see above]
```

---

## 4. Opening Paragraph (place immediately under H1)

```html
<p>
  BiXBiT custom firmware for ASIC miners is third-party firmware built for
  Antminer and Whatsminer devices used in industrial Bitcoin mining. It
  replaces stock manufacturer firmware to enable overclocking, underclocking,
  and automatic efficiency tuning (autotuning), with free access to the
  BiXBiT AMS fleet monitoring dashboard included. All BiXBiT firmware lines
  run on a 2.8% developer fee, reduced to 2% for the Whatsminer M2x series.
</p>
```

- Entity-definition style ("X is..."), matching the pattern LLMs extract for "what is" / comparative queries — consistent with the GEO approach already used on the Antminer child page
- Covers both brands in sentence one, satisfying the category-hub intent
- Dev fee figures are the confirmed on-page facts (2.8% / 2% M2x) — no invented tech specs
- No J/TH or overclocking percentages stated — those remain `[VERIFY]`-gated per brand-specific child pages

---

## 5. New FAQ Questions (category/comparative intent — do not duplicate existing single-brand topics)

1. **"What is the difference between BiXBiT firmware for Antminer and Whatsminer?"**
   Draft answer: BiXBiT firmware for both brands shares the same core feature set — overclocking, underclocking, autotuning, efficiency tuning, and AMS fleet monitoring integration — but is built as brand-specific firmware images tailored to each manufacturer's control board and chip architecture. `[VERIFY: confirm with engineering whether there are functional differences beyond packaging — e.g., autotuning granularity — before stating more specifically.]`

2. **"Does the developer fee differ between Antminer and Whatsminer firmware lines?"**
   Draft answer: Yes. BiXBiT firmware carries a 2.8% developer fee across all lines, except the Whatsminer M2x series, which runs a reduced 2% fee. `[VERIFY: reconfirm these figures are still current before publishing — commercial terms can change; this is the only page in the project where the number is a first-party confirmed fact rather than an inference.]`

3. **"Which ASIC miner brands and series does BiXBiT firmware support?"**
   Draft answer: BiXBiT supports Whatsminer (M2x, M3x, M5x, M6x, M7x series) and Antminer (S19, S21, T19, T21, L7, L9 series). `[VERIFY: confirm S21, T21, L9, L7 are shipping/production firmware and not placeholder cards — see internal linking note below; current dedicated crawl data only confirms separate pages for older Antminer models (S9, T9+, T17, T17+, S17, S17+, S19).]`

These three are deliberately comparative/category-scoped ("difference between," "differ between," "which brands") — distinct from the existing single-topic FAQ entries (cost, install, rollback, etc.) already confirmed present on the page.

---

## 6. Internal Linking Plan

| Card / anchor on hub | Target URL | Status |
|---|---|---|
| Whatsminer M6x | `/en/firmwares/whatsminer-series-m6x` | Confirmed in site-structure.md |
| Whatsminer M5x | `/en/firmwares/whatsminer-series-m5x` | Confirmed in site-structure.md |
| Whatsminer M3x | `/en/firmwares/whatsminer-series-m3x` | Confirmed in site-structure.md |
| Whatsminer M2x | `/en/firmwares/whatsminer-series-m2x` | Confirmed in site-structure.md |
| Whatsminer M7x | not resolved | **`[VERIFY]`** — site-structure.md (crawled 2026-06-17) has no `whatsminer-series-m7x` entry, only `whatsminer-all-series`. Confirm whether the live M7x card links to a page created after the June crawl, or falls back to `whatsminer-all-series`. |
| Antminer S21 / S19 / T21 / T19 / L9 / L7 | `/en/firmwares/antminer` (all six, single URL) | **Expected/normal** if this is intentionally one consolidated Antminer page for current-generation models. **However:** site-structure.md's June crawl shows separate legacy pages (`asic-s19`, `asic-S17-S17Pro`, `asic-S17-plus`, `asic-T17-plus`, `asic-T17`, `asic-T9-plus`, `asic-s9-s9j-s9i`) that do NOT correspond 1:1 to the S19/S21/T19/T21/L9/L7 set shown on the current hub. `[VERIFY]` — confirm with technical-seo whether these legacy per-model pages still exist and are simply not linked from the hub (orphan risk), or were consolidated/redirected into `/en/firmwares/antminer` (in which case redirects should be confirmed, not just removed links). |
| "Enable analytics" → `/en/ams` | Confirmed in site-structure.md | Keep |
| Cooling section links | `/en/asics-cooling/*` | Confirmed in site-structure.md | Keep |
| "Order PDU" → `/en/products/pdu` | **Not in site-structure.md** ("NOT FOUND — no PDU pages discovered in crawl") | **`[VERIFY]`** — third page in a row (after homepage, `/en/ams`) referencing URLs absent from the June crawl (also `/en/blog`, `/en/faq`, `/en/documentation/new-user-guide-for-whatsminer-asic`). Strong signal site-structure.md is stale rather than these being dead links. Recommend re-running `/full-audit` to refresh the baseline before further page-optimize work relies on it as ground truth. |

**Recommended addition:** Add one contextual link from `/en/firmwares` to `/en/firmwares/antminer` using anchor text "custom firmware for Antminer" (and one to the Whatsminer all-series page) — reinforces the hub→spoke relationship without keyword overlap, since the hub itself doesn't need to repeat the brand-specific phrase.

---

## 7. [VERIFY] List

1. **Dev fee reconfirmation** — 2.8% (2% for Whatsminer M2x) is a real, published on-page fact (firmware versions cited: M2x 1.6.0.2, other Whatsminer 1.8.1) and is used as-is in title/meta/FAQ without invention. Still mark for periodic reconfirmation before reuse on other pages (Antminer child page, homepage, AMS) — commercial terms can change and this session cannot verify "current as of today."
2. **H3 typo** — "Feedback on bone work from our partner" likely means "done work" or "our work." Confirm exact intended wording with content team before editing; do not silently auto-correct given possible RU→EN translation origin.
3. **Near-duplicate H2/H3** — resolved via renames in Section 3 above; confirm renames with content/design team before deploy since they affect on-page navigation copy, not just SEO metadata.
4. **Whatsminer M7x URL** — not present in site-structure.md June crawl; confirm actual link target on the live page.
5. **Antminer legacy per-model pages** (`asic-s19`, `asic-S17-S17Pro`, `asic-S17-plus`, `asic-T17-plus`, `asic-T17`, `asic-T9-plus`, `asic-s9-s9j-s9i`) — confirm whether still live/orphaned or consolidated/redirected into `/en/firmwares/antminer`. Flag for technical-seo (redirect audit, orphan-page check).
6. **`/en/products/pdu`, `/en/blog`, `/en/faq`, `/en/documentation/new-user-guide-for-whatsminer-asic`** — none appear in site-structure.md (June 2026 crawl). This is the third hub-level page in this project surfacing the same gap. Recommend a fresh `/full-audit` crawl to refresh `data/site-structure.md` — current file should not be treated as complete ground truth for internal-linking decisions until re-crawled.
7. **Hreflang claim** — original WebFetch reported "hreflang present EN/RU" but this was explicitly flagged as unreliable in the task brief; do not treat as confirmed. Recommend technical-seo verify via raw HTML source, not rendered fetch.
8. **Canonical tag** — not confirmed present; recommend technical-seo add self-referencing canonical `https://bixbit.io/en/firmwares` if missing, consistent with the pattern used on `/en/firmwares/antminer`.
9. **JSON-LD** — none present on page currently. Recommend technical-seo add `CollectionPage` or `ItemList` schema (hub of firmware products) rather than `SoftwareApplication` (reserved for individual firmware product pages like the Antminer child page) — avoids schema-level duplication/competition between hub and spokes. FAQPage schema can be added once new FAQ copy (Section 5) is finalized and confirmed.
10. **S21 / T21 / L9 / L7 production status** — confirm these are shipping, non-beta firmware lines before stating support for them in the new FAQ answer (item 3 in Section 5) or in any schema `featureList`/model list.
11. **FAQ answer for new Q1 (brand differences)** — kept deliberately general (packaging/architecture, not functional claims) pending engineering confirmation of any real feature differences between Antminer and Whatsminer builds.

---

## 8. Technical SEO — Canonical, Hreflang, Structured Data

*(technical-seo deliverable, condensed from `content/page-optimize/firmwares-hub.md`)*

### 8.1 Canonical
```html
<link rel="canonical" href="https://bixbit.io/en/firmwares">
```
Self-referencing, no trailing slash. Currently absent — P0.

### 8.2 Hreflang
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares">
<!-- [VERIFY] /ru counterpart — confirm exists, 200, not noindex before deploying -->
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares">
```
Ship `en` + `x-default` now, hold `ru`. **On the WebFetch "hreflang present" claim:** false, per the same reasoning as the homepage and `/en/ams` audits — this is the **third consecutive** page where the tool reported hreflang it could not corroborate, which points to a tooling defect (likely mis-reading the footer/nav language switcher as `<head>` hreflang), not a per-page fact. Recommend a `curl`/view-source check going forward instead of trusting this tool's hreflang field at all.

### 8.3 Schema decision: `CollectionPage` + `ItemList` + one brand-level `SoftwareApplication` — not a duplicate product entity

Rejected a full second `SoftwareApplication` matching `/en/firmwares/antminer`'s schema — that would create two entities both plausibly matching "custom firmware for Antminer," splitting rich-result eligibility. Instead:

```json
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "BiXBiT Custom Firmware for ASIC Miners",
    "url": "https://bixbit.io/en/firmwares",
    "description": "Directory of BiXBiT custom firmware lines for industrial ASIC mining: Whatsminer (M2x–M7x) and Antminer (S21, S19, T21, T19, L9, L7) series.",
    "isPartOf": { "@type": "WebSite", "url": "https://bixbit.io/en", "name": "BiXBiT" },
    "mainEntity": {
      "@type": "ItemList",
      "name": "BiXBiT Firmware Lines",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "url": "https://bixbit.io/en/firmwares/antminer", "name": "BiXBiT Custom Firmware for Antminer" },
        { "@type": "ListItem", "position": 2, "url": "https://bixbit.io/en/firmwares/whatsminer-all-series", "name": "BiXBiT Custom Firmware for Whatsminer (All Series)" },
        { "@type": "ListItem", "position": 3, "url": "https://bixbit.io/en/firmwares/whatsminer-series-m6x", "name": "BiXBiT Firmware for Whatsminer M6x" },
        { "@type": "ListItem", "position": 4, "url": "https://bixbit.io/en/firmwares/whatsminer-series-m5x", "name": "BiXBiT Firmware for Whatsminer M5x" },
        { "@type": "ListItem", "position": 5, "url": "https://bixbit.io/en/firmwares/whatsminer-series-m3x", "name": "BiXBiT Firmware for Whatsminer M3x" },
        { "@type": "ListItem", "position": 6, "url": "https://bixbit.io/en/firmwares/whatsminer-series-m2x", "name": "BiXBiT Firmware for Whatsminer M2x" }
      ]
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://bixbit.io/en/firmwares#software",
    "name": "BiXBiT Custom Firmware for ASIC Miners",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Antminer ASIC (Bitmain), Whatsminer ASIC (MicroBT)",
    "description": "Custom firmware family for industrial Bitcoin ASIC mining, covering Whatsminer (M2x–M7x) and Antminer (S21, S19, T21, T19, L9, L7) series. Monetized via a developer fee taken from mining output: 2.8% standard, reduced to 2% for the Whatsminer M2x line. [VERIFY: reconfirm fee structure and coverage list is still current before publishing.]",
    "url": "https://bixbit.io/en/firmwares",
    "publisher": { "@type": "Organization", "name": "BiXBiT", "url": "https://bixbit.io" },
    "additionalProperty": [
      { "@type": "PropertyValue", "name": "Developer Fee (standard, most lines)", "value": "2.8% [VERIFY: reconfirm still current before publishing]" },
      { "@type": "PropertyValue", "name": "Developer Fee (Whatsminer M2x)", "value": "2% [VERIFY: reconfirm still current before publishing]" },
      { "@type": "PropertyValue", "name": "Firmware Version (Whatsminer M3x-M7x)", "value": "v1.8.1 [VERIFY: reconfirm still current before publishing]" },
      { "@type": "PropertyValue", "name": "Firmware Version (Whatsminer M2x)", "value": "v1.6.0.2 [VERIFY: reconfirm still current before publishing]" },
      { "@type": "PropertyValue", "name": "Enterprise / Partnership Terms", "value": "Reduced developer fee, custom feature development, white-label options, mass-installation support. [VERIFY: reconfirm eligibility and terms before publishing.]" }
    ],
    "hasPart": [
      { "@type": "SoftwareApplication", "name": "BiXBiT Custom Firmware for Antminer", "url": "https://bixbit.io/en/firmwares/antminer" },
      { "@type": "SoftwareApplication", "name": "BiXBiT Custom Firmware for Whatsminer (All Series)", "url": "https://bixbit.io/en/firmwares/whatsminer-all-series" }
    ]
  }
]
</script>
```

`hasPart` is deliberately limited to `@type`+`name`+`url` — no restated `featureList`/`offers` — the full entity definitions live only on the child pages. The `ItemList`'s two top-level entries mirror exactly the two URLs already referenced in the homepage's `Organization.hasOfferCatalog` (`content/page-optimize/homepage.md` §7.3), so no third conflicting grouping is introduced across the site's schema graph. Whatsminer **M7x** has no confirmed URL in `data/site-structure.md` and is deliberately omitted, not fabricated.

### 8.4 FAQPage JSON-LD (topic-based draft, not verified against live copy)

Built from the *topics* the task input described (fee/cost, installation, profile generation, hashrate optimization, warranty, factory restoration, SD card issues, download issues, firmware safety, Antminer access) — not the real Q&A text, which wasn't available to either agent. **Do not deploy as-is.** Full 10-question draft with per-answer `[VERIFY]` tags is in `content/page-optimize/firmwares-hub.md` §4 (kept there rather than duplicated here to avoid this file becoming unwieldy) — every answer is a safe, generic paraphrase pending confirmation against the live page's actual copy. Once real FAQ text is available, this must also be diffed against `/en/firmwares/antminer`'s own 7-question FAQPage (`firmwares-antminer.md`) to rule out literal duplicate Q&A pairs across hub and child page.

### 8.5 Regression checklist (schema-specific)

| Check | Result |
|---|---|
| JSON-LD valid syntax (both blocks) | PASS (manual check) — no trailing commas, `@type`/`@context` present |
| No duplicate `SoftwareApplication` vs `/en/firmwares/antminer` | PASS — hub entity is brand-level only, child referenced via `hasPart` (name+url only) |
| `ItemList` consistent with homepage `Organization.hasOfferCatalog` | PASS — same two top-level URLs, no third conflicting grouping |
| All `ItemList` URLs exist in `data/site-structure.md` | PARTIAL — 6/6 listed confirmed; Whatsminer M7x omitted (no confirmed URL) |
| Canonical self-referencing | PASS |
| Hreflang `ru` withheld pending verification | PASS (intentional) |
| No invented dev-fee/version numbers | PASS — sourced from live page as stated facts, still `[VERIFY]`-tagged per standing rule |
| FAQPage vs `/en/firmwares/antminer` FAQ overlap | NEEDS HUMAN CHECK — real live FAQ text unavailable to either agent |

---

## 9. GEO / AI Passage Optimization — Alternate Framing

*(geo-ai deliverable — this was the original content of this file before content-seo's pass overwrote it; preserved here as an alternate/supplementary framing, not deleted)*

### 9.1 Alternate opening paragraph

> BiXBiT builds custom firmware for ASIC miners, covering both Antminer (Bitmain) and Whatsminer (MicroBT) devices under one firmware brand for industrial Bitcoin mining operations. All BiXBiT firmware lines run on a 2.8% developer fee, reduced to 2% for the Whatsminer M2x series — the only ASIC firmware [VERIFY: reconfirm competitor coverage before publishing this comparative claim] publicly covering both major ASIC brands under a single vendor. `[Note: dev fee figures here are the same real on-page facts used in §4's opening paragraph — reconfirm still current before publishing, per standing project rule, even though not technically a `[VERIFY]`.]`

Structural note: current H1 buries brand/category behind two model names ("BiXBiT Custom firmware for Whatsminer & Antminer"); recommend reordering to lead with the brand + category noun phrase, consistent with how `/en/firmwares/antminer`'s own GEO passage was structured. (This matches content-seo's own H1 rewrite in §3 above — the two passes converged independently on the same fix.)

### 9.2 Alternate meta/og:description (154 chars)

```
BiXBiT: custom firmware for ASIC miners — Antminer & Whatsminer, one vendor. 2.8% dev fee (2% on M2x). Overclocking, autotuning, free AMS monitoring.
```

Coordinate with §2's primary meta description before deploy — do not ship both; both lead with brand + category term + the real dev-fee fact, differing mainly in whether AMS-bundling is mentioned (this variant includes it, §2 doesn't).

### 9.3 Passage-friendly spec table — "BiXBiT Firmware Lineup at a Glance"

Place directly after the opening paragraph — tables extract cleanly as LLM-citable passages.

| Brand / Line | Supported Series | Firmware Version | Developer Fee |
|---|---|---|---|
| Antminer (all supported models) | S21, S19, T21, T19, L9, L7 | `[VERIFY: no version number supplied in this pass]` | 2.8% |
| Whatsminer M3x–M7x | M3x, M5x, M6x, M7x | v1.8.1 | 2.8% |
| Whatsminer M2x | M2x | v1.6.0.2 | 2% |

All figures are real, on-page facts (not invented) — see standing note on reconfirming currency before reuse.

### 9.4 FAQ variants (category-intent AI-query phrasing)

- "What is custom ASIC firmware?" → third-party firmware replacing stock manufacturer software to unlock overclocking/autotuning; BiXBiT's version covers both Antminer and Whatsminer.
- "Does BiXBiT support both Antminer and Whatsminer firmware?" → Yes — single vendor, both brands, free AMS monitoring included.
- "How much does BiXBiT custom firmware cost?" → No upfront price; 2.8% developer fee (2% on Whatsminer M2x), taken from mining output.

These overlap in intent with content-seo's §5 questions — reconcile into one FAQ set before publishing, don't ship two overlapping blocks.

### 9.5 Differentiator claim for AI-citability

> "BiXBiT is a single vendor offering custom firmware for both Antminer and Whatsminer ASICs" — `[VERIFY: reconfirm competitor coverage before publishing; Braiins OS+/Vnish/LuxOS/ePIC are believed to be largely Antminer-only per qualitative research, but this must be reconfirmed at publish time, not treated as static]`.

### 9.6 llms.txt recommendation

Add one line to `content/geo/llms.txt` under firmware coverage stating the dual-brand, single-vendor positioning plus the real dev-fee fact once the competitor-coverage claim in §9.5 is confirmed — this hub page is the natural canonical source for that fact (not a child page), since it's the only URL describing both firmware lines together.

---

## 10. Notes / Handoff

- **technical-seo:** action items 4–9 in §7 (JSON-LD, canonical, hreflang verification, redirect/orphan audit for legacy Antminer model pages, refreshed crawl of `data/site-structure.md`) — §8 above already delivers the canonical/hreflang/schema half of this; the redirect/orphan audit for legacy Antminer per-model pages (S9/T9+/T17/T17+/S17/S17+/S19 vs. the hub's S21/S19/T21/T19/L9/L7 cards) is still open.
- **Cross-page consistency:** the dev fee fact (2.8% / 2% M2x) confirmed here can now be used to close the open `[VERIFY: confirm dev fee]` items on `/en/firmwares/antminer`, homepage, and `/en/ams` — tag each reuse with "reconfirm current before publish."
- **Pick one opening paragraph** (§4 vs §9.1) and **one meta description** (§2 vs §9.2) before deploy — do not ship both; they largely agree on facts and differ only in emphasis (AMS-bundling mention, competitor-comparison framing).
- **This is the third consecutive page-optimize pass** (homepage, `/en/ams`, now `/en/firmwares`) surfacing live internal links (`/en/products/pdu`, `/en/blog`, `/en/faq`, `/en/documentation/...`) absent from `data/site-structure.md`. A `/full-audit` re-crawl is recommended before further page-optimize work relies on that file as ground truth.
- Code changes ship as a diff/PR, not directly to production, per `/page-optimize` runbook rules.
