---
# Page Optimization: /en/firmwares (hub/category page)
**Target keyword:** custom firmware for ASIC miners
**Date:** 2026-09-16
**Page type:** Category hub/catalog — NOT a single-product page. Aggregates Whatsminer (M2x–M7x) and Antminer (S21/S19/T21/T19/L9/L7) firmware lines.
**URL in site-structure.md:** confirmed ✓ (`/en/firmwares — "BiXBiT Custom ASIC Mining Firmware"`)
**Related audits:** `content/page-optimize/firmwares-antminer.md` (child page, already has SoftwareApplication+FAQPage), `content/page-optimize/homepage.md` (Organization.hasOfferCatalog references two of this hub's children)

## Data Sources Used
- GSC: not queried this pass — no indication in task input that it was checked; treat as UNAVAILABLE unless re-run.
- DataForSEO: not queried this pass — UNAVAILABLE.
- PageSpeed/CrUX: not queried this pass — UNAVAILABLE.
- Current on-page state: WebFetch snapshot provided in task input, cross-checked against `data/site-structure.md` (crawled 2026-06-17, 70 pages).

No search-volume, ranking, CTR, or CWV figures appear below — none were supplied or fetched.

---

## 1. Canonical Tag

```html
<link rel="canonical" href="https://bixbit.io/en/firmwares">
```

Self-referencing, no trailing slash, HTTPS — consistent with the format used on `/en` and `/en/firmwares/antminer`. Currently absent per the WebFetch snapshot; this is a P0 fix (without it, any tracking-parameter or trailing-slash variant risks splitting authority on the single most important hub page for the firmware vertical).

---

## 2. Hreflang

```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares">
<!-- [VERIFY] /ru counterpart — confirm URL exists, returns 200, and is NOT noindex before deploying this line -->
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares">
```

Same rollout logic as `homepage.md` §7.2 and `ams.md` §8.2: ship `en` + `x-default` now, hold `ru` until parity is confirmed.

**On the WebFetch claim of "hreflang present for EN/RU":** treat this as **false**, per the same reasoning applied in the homepage and `/en/ams` audits. This is now the **third consecutive** page-optimize pass on this site where the crawl tool reported hreflang as present and it could not be corroborated. The pattern strongly suggests the tool is matching the site's footer/nav language switcher (a visible EN/RU toggle link) and misclassifying it as `<link rel="alternate" hreflang>` in `<head>`, rather than actually parsing `<head>`. **Recommendation:** stop trusting this tool's hreflang field entirely until someone manually confirms via `curl -s https://bixbit.io/en/firmwares | grep hreflang` or browser "View Page Source" (not DevTools Elements, which shows the post-hydration DOM). This is a tooling/process gap, not a one-off data error — flag it to whoever owns the crawler config.

---

## 3. Schema Decision — CollectionPage + brand-level SoftwareApplication, not a duplicate product entity

**Decision:** Use two coordinated JSON-LD nodes, not one:

1. **`CollectionPage`** as the page-level entity, with an embedded **`ItemList`** (`mainEntity`) pointing to the real child firmware pages.
2. **One generalized `SoftwareApplication`** describing "BiXBiT Custom Firmware" as a brand-level product family (not tied to a specific ASIC model or J/TH figure), linked to its children via `hasPart` references (URL + name only — no re-statement of child `featureList`, `offers`, or model-specific claims).

**Rejected alternative: full duplicate `SoftwareApplication` matching `/en/firmwares/antminer`'s schema.** Rejected because:
- It would create two `SoftwareApplication` entities both plausibly matching "custom firmware for Antminer" queries, splitting rich-result eligibility and confusing which URL Google should show.
- `/en/firmwares/antminer` already owns the Antminer-specific `featureList` (overclocking, autotuning, J/TH tuning, Farm Protect, etc.) and its own `Offer`. Restating that content on the hub with a second `@type: SoftwareApplication` is the same anti-pattern flagged in `homepage.md` §9 ("Do not add SoftwareApplication or FAQPage schema types to the homepage beyond what's needed").
- The hub's actual job is discovery/navigation across ~10 firmware URLs (Antminer hub + Whatsminer hub + 4 confirmed Whatsminer sub-series pages), which is exactly what `ItemList`/`CollectionPage` is designed to represent — not a single downloadable product.

**Why not `ItemList` alone, with no `SoftwareApplication` at all:** the target query "custom firmware for ASIC miners" is a category/brand-level commercial query, not purely navigational — a bare `CollectionPage`+`ItemList` with no product entity forfeits `SoftwareApplication` rich-result eligibility for the hub itself. A brand-level `SoftwareApplication` (scoped to "firmware for ASIC miners" generically, no model-specific technical claims) captures that without duplicating any child page's entity.

**Consistency check against `homepage.md`:** the homepage's `Organization.hasOfferCatalog` (see `homepage.md` §7.3) already lists exactly two offers: `SoftwareApplication` "BiXBiT Antminer Firmware" → `/en/firmwares/antminer`, and "BiXBiT Whatsminer Firmware" → `/en/firmwares/whatsminer-all-series`. This hub's `ItemList` must **not** introduce a third, conflicting grouping — so the two top-level `ItemList` entries mirror those exact two URLs, with the four confirmed Whatsminer sub-series pages nested underneath as additional list positions (not as a competing hierarchy).

**Real dev-fee fact used:** 2.8% developer fee applies to all firmware lines except Whatsminer M2x, which is 2%. Firmware versions in circulation: Whatsminer M3x–M7x = v1.8.1; Whatsminer M2x = v1.6.0.2. These are stated facts from the live page (not invented), placed as `additionalProperty` `PropertyValue` entries on the brand-level `SoftwareApplication` (a single fixed price doesn't make sense at hub level since it varies by line) — each still carries `[VERIFY]` per CLAUDE.md rule 4, because commercial terms can change without a corresponding audit update.

**Site-structure gap found while building the `ItemList`:** the task brief lists "Whatsminer M2x–**M7x**" as the product range, but `data/site-structure.md` (crawled 2026-06-17) only has confirmed URLs through `whatsminer-series-m6x` — there is no `whatsminer-series-m7x` entry. Either (a) the M7x page is newer than the last crawl, or (b) M7x firmware is sold under an existing URL not yet distinguished in the crawl. **Do not fabricate a M7x URL.** It is omitted from the `ItemList` below and flagged in §7.

### JSON-LD (CollectionPage + ItemList + brand-level SoftwareApplication)

```json
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "BiXBiT Custom Firmware for ASIC Miners",
    "url": "https://bixbit.io/en/firmwares",
    "description": "Directory of BiXBiT custom firmware lines for industrial ASIC mining: Whatsminer (M2x–M7x) and Antminer (S21, S19, T21, T19, L9, L7) series.",
    "isPartOf": {
      "@type": "WebSite",
      "url": "https://bixbit.io/en",
      "name": "BiXBiT"
    },
    "mainEntity": {
      "@type": "ItemList",
      "name": "BiXBiT Firmware Lines",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://bixbit.io/en/firmwares/antminer",
          "name": "BiXBiT Custom Firmware for Antminer"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://bixbit.io/en/firmwares/whatsminer-all-series",
          "name": "BiXBiT Custom Firmware for Whatsminer (All Series)"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://bixbit.io/en/firmwares/whatsminer-series-m6x",
          "name": "BiXBiT Firmware for Whatsminer M6x"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://bixbit.io/en/firmwares/whatsminer-series-m5x",
          "name": "BiXBiT Firmware for Whatsminer M5x"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://bixbit.io/en/firmwares/whatsminer-series-m3x",
          "name": "BiXBiT Firmware for Whatsminer M3x"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://bixbit.io/en/firmwares/whatsminer-series-m2x",
          "name": "BiXBiT Firmware for Whatsminer M2x"
        }
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
    "description": "Custom firmware family for industrial Bitcoin ASIC mining, covering Whatsminer (M2x–M7x) and Antminer (S21, S19, T21, T19, L9, L7) series. Monetized via a developer fee taken from mining output rather than an upfront license price: 2.8% standard across all lines, reduced to 2% for the Whatsminer M2x line. [VERIFY: reconfirm fee structure and coverage list is still current before publishing.]",
    "url": "https://bixbit.io/en/firmwares",
    "publisher": {
      "@type": "Organization",
      "name": "BiXBiT",
      "url": "https://bixbit.io"
    },
    "additionalProperty": [
      {
        "@type": "PropertyValue",
        "name": "Developer Fee (standard, most lines)",
        "value": "2.8% [VERIFY: reconfirm still current before publishing]"
      },
      {
        "@type": "PropertyValue",
        "name": "Developer Fee (Whatsminer M2x)",
        "value": "2% [VERIFY: reconfirm still current before publishing]"
      },
      {
        "@type": "PropertyValue",
        "name": "Firmware Version (Whatsminer M3x-M7x)",
        "value": "v1.8.1 [VERIFY: reconfirm still current before publishing]"
      },
      {
        "@type": "PropertyValue",
        "name": "Firmware Version (Whatsminer M2x)",
        "value": "v1.6.0.2 [VERIFY: reconfirm still current before publishing]"
      },
      {
        "@type": "PropertyValue",
        "name": "Enterprise / Partnership Terms",
        "value": "Reduced developer fee, custom feature development, white-label options, and mass-installation support available for enterprise/partner accounts. [VERIFY: reconfirm eligibility thresholds and current terms before publishing.]"
      }
    ],
    "hasPart": [
      {
        "@type": "SoftwareApplication",
        "name": "BiXBiT Custom Firmware for Antminer",
        "url": "https://bixbit.io/en/firmwares/antminer"
      },
      {
        "@type": "SoftwareApplication",
        "name": "BiXBiT Custom Firmware for Whatsminer (All Series)",
        "url": "https://bixbit.io/en/firmwares/whatsminer-all-series"
      }
    ]
  }
]
</script>
```

**Note on `hasPart`:** intentionally limited to `@type` + `name` + `url` — no `featureList`, `offers`, or `applicationCategory` restated, to avoid the exact duplication problem flagged in the task brief. The full entity definitions live on the child pages only.

---

## 4. FAQPage JSON-LD (draft — topics only, not verified against live copy)

**Important caveat, stated up front:** the task input supplied only the **topics** covered by the existing FAQ (fee/cost, installation, profile generation, hashrate optimization, warranty, factory firmware restoration, SD card issues, download issues, firmware safety, Antminer access) — not the actual question/answer text on the page. Everything below is a **plausible draft built from those topics**, formulated to be safe (no invented specs) and must be checked against the live page's real copy before this JSON-LD is shipped. Do not deploy as-is.

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does BiXBiT firmware cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT firmware is not sold for a fixed price. It runs on a developer-fee model: a percentage of the miner's output goes to BiXBiT after installation — 2.8% for most firmware lines, reduced to 2% for the Whatsminer M2x line. [VERIFY: confirm against live page copy before publishing — exact wording and any trial-period terms.]"
      }
    },
    {
      "@type": "Question",
      "name": "How do I install BiXBiT custom firmware?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Installation involves downloading the firmware package for your specific miner series (Whatsminer or Antminer), then flashing it to the device following the model-specific instructions on that firmware line's page. [VERIFY: confirm against live page copy before publishing — exact install method, e.g., web UI upload vs. SD card, differs by model line.]"
      }
    },
    {
      "@type": "Question",
      "name": "What is a firmware profile and how is it generated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A firmware profile is a configuration preset (frequency, voltage, cooling mode) tuned for a specific miner model and operating condition. [VERIFY: confirm against live page copy before publishing — exact profile-generation workflow described on the page.]"
      }
    },
    {
      "@type": "Question",
      "name": "How does BiXBiT firmware optimize hashrate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT firmware adjusts chip frequency and voltage (overclocking/underclocking) and includes autotuning to balance hashrate against power draw and heat. [VERIFY: confirm against live page copy before publishing — no specific % hashrate gain should be published without engineering confirmation.]"
      }
    },
    {
      "@type": "Question",
      "name": "Does BiXBiT firmware come with a warranty?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[VERIFY: confirm against live page copy before publishing — warranty terms, if any, and whether installing third-party firmware affects the original manufacturer's hardware warranty, must be stated exactly as the live page states them. Do not infer warranty terms.]"
      }
    },
    {
      "@type": "Question",
      "name": "Can I restore the factory (stock) firmware after installing BiXBiT firmware?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, BiXBiT firmware supports restoring the original manufacturer firmware. [VERIFY: confirm against live page copy before publishing — exact rollback steps and any prerequisites.]"
      }
    },
    {
      "@type": "Question",
      "name": "What if my SD card isn't recognized during installation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[VERIFY: confirm against live page copy before publishing — this is a device-specific troubleshooting answer (SD card format, size, or file-system requirements) that must match the page's actual guidance, not a generic assumption.]"
      }
    },
    {
      "@type": "Question",
      "name": "The firmware download isn't working — what should I do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[VERIFY: confirm against live page copy before publishing — likely covers mirrored download links, browser/antivirus blocking, or contacting support via Telegram, but exact guidance must come from the live page.]"
      }
    },
    {
      "@type": "Question",
      "name": "Is BiXBiT firmware safe to install?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT firmware includes safety-oriented features referenced elsewhere on the site (such as Farm Protect on the Antminer line). [VERIFY: confirm against live page copy before publishing — specific security claims, certifications, or audit references must be sourced from the actual page text, not assumed.]"
      }
    },
    {
      "@type": "Question",
      "name": "How do I get access to Antminer firmware specifically?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Antminer-specific firmware, models, and access details are covered on the dedicated Antminer firmware page. [VERIFY: confirm against live page copy before publishing — exact access/request process, e.g., direct download vs. request form vs. Telegram contact.]"
      }
    }
  ]
}
</script>
```

---

## 5. Non-Duplication Statement (explicit)

- This hub does **not** carry a second full `SoftwareApplication` entity matching `/en/firmwares/antminer`'s schema (see `firmwares-antminer.md` — that page owns Antminer-specific `featureList`, `Offer`, and its own 7-question `FAQPage`).
- The hub's `SoftwareApplication` (`@id: https://bixbit.io/en/firmwares#software`) is scoped to the **brand-level firmware family** — no J/TH figures, no per-model `featureList`, no Antminer-specific claims. It links out via `hasPart` (URL + name only).
- The hub's `FAQPage` (§4) covers different questions than the Antminer page's FAQ (cost/install/profile/hashrate/warranty/restore/SD-card/download/safety/access at the **category** level) versus the Antminer page's FAQ (Antminer-model-specific: which models supported, immersion/hydro compatibility, AMS integration, rollback). If the live page's actual FAQ text turns out to overlap with the Antminer page's questions, deduplicate before publishing — keep the more specific version on `/en/firmwares/antminer` and generalize or remove the duplicate on the hub.
- The hub's `ItemList` mirrors, rather than conflicts with, the two `hasOfferCatalog` entries already planned for the homepage's `Organization` schema (`/en/firmwares/antminer` and `/en/firmwares/whatsminer-all-series` — see `homepage.md` §7.3), with the four Whatsminer sub-series pages added as additional, non-conflicting list positions.

---

## 6. Regression Checklist

| Check | Result | Notes |
|---|---|---|
| JSON-LD valid syntax (both blocks) | PASS (manual check) | No trailing commas; all `@type`/`@context` present; array-wrapper format matches the convention used in `firmwares-antminer.md` |
| No duplicate `SoftwareApplication` entity vs `/en/firmwares/antminer` | PASS | Hub `SoftwareApplication` is brand-level only; child entity referenced via `hasPart` (name+url only), not restated |
| No duplicate/competing `FAQPage` questions vs `/en/firmwares/antminer`'s 7 Q&A | NEEDS HUMAN CHECK | Draft topics chosen to be category-level, not model-specific — but exact live FAQ text was not available; verify no literal overlap once live copy is confirmed |
| `ItemList` consistent with homepage `Organization.hasOfferCatalog` | PASS | Same two top-level URLs (`/en/firmwares/antminer`, `/en/firmwares/whatsminer-all-series`) used in both; no third conflicting grouping introduced |
| All `ItemList` URLs exist in `data/site-structure.md` | PARTIAL | 6 of 6 listed URLs confirmed in crawl; Whatsminer **M7x** has no confirmed URL and was deliberately omitted, not fabricated |
| Canonical self-referencing, no trailing slash | PASS | `https://bixbit.io/en/firmwares` |
| Hreflang `ru` line withheld pending verification | PASS | Same gating logic as homepage/AMS/`firmwares/antminer` audits |
| No invented dev-fee/version numbers | PASS | 2.8%/2% and v1.8.1/v1.6.0.2 sourced directly from task input as "real facts from the live page," each still flagged `[VERIFY]` per standing rule (commercial terms can change) |
| No J/TH, %, or hashrate figures invented | PASS | None stated; hashrate-optimization FAQ answer deliberately avoids specific percentages |

---

## 7. [VERIFY] List for Human Review

1. **Live FAQ text** — only topics were provided, not actual question/answer copy. §4's `FAQPage` JSON-LD is a topic-based draft and must be rewritten to match real on-page text before publishing.
2. **Dev fee currency** — 2.8% standard / 2% Whatsminer M2x: confirm still accurate at publish time (commercial terms change without notice).
3. **Firmware version currency** — v1.8.1 (Whatsminer M3x–M7x) and v1.6.0.2 (Whatsminer M2x): confirm still current.
4. **Hreflang status** — treat WebFetch's "present for EN/RU" as unreliable; this is the **third consecutive** audit (homepage, `/en/ams`, now `/en/firmwares`) where the tool reported hreflang that could not be corroborated. Manually confirm via `curl`/view-source, and treat this as a standing tooling defect to raise with whoever configures the crawler, not a page-specific issue.
5. **`/ru/firmwares` parity** — confirm existence, 200 status, and indexability before shipping the `hreflang="ru"` line.
6. **`/en/products/pdu` status** — referenced by an internal link on this page but does not appear anywhere in `data/site-structure.md` (which explicitly marks PDU as "NOT FOUND — no PDU pages discovered in crawl"). Do not assume this link 404s or that the page exists — status is simply unknown until re-crawled.
7. **`/en/blog` status** — same issue: linked from the page, absent from site-structure.md (marked "NOT FOUND — no /en/blog/* pages discovered in crawl").
8. **`/en/faq` status** — linked from the page, not present anywhere in `data/site-structure.md` at all (not even as a "NOT FOUND" note — it's simply missing from the last crawl's categories).
9. **`/en/documentation/new-user-guide-for-whatsminer-asic` status** — linked from the page, no `/en/documentation/*` path appears anywhere in `data/site-structure.md`.
10. **Standing recommendation — full re-crawl required:** items 6–9 mark the **third consecutive** page-optimize pass (homepage, `/en/ams`, now `/en/firmwares`) surfacing live internal links to URLs absent from `data/site-structure.md` (crawled 2026-06-17). This is no longer explainable as isolated noise — the site has evidently shipped new sections (PDU, blog, FAQ, documentation) in the ~3 months since the last crawl, and `data/site-structure.md` should not be treated as a reliable source of truth for internal-linking decisions until a fresh `/full-audit` re-crawl runs. Recommend running `/full-audit` before any further `/page-optimize` passes that depend on internal-link target validation.
11. **Whatsminer M7x URL** — no confirmed URL in the last crawl for M7x firmware, despite the product line being referenced in the target scope. Likely resolved by the same re-crawl in item 10; do not invent a URL (e.g., `whatsminer-series-m7x`) until confirmed live.
12. **FAQ overlap with `/en/firmwares/antminer`** — once real FAQ text is available, manually diff against the Antminer page's 7 questions (`firmwares-antminer.md` §"JSON-LD Schema") to ensure no literal duplicate question/answer pairs across the two pages.
