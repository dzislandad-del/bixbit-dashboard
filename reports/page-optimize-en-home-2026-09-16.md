# Page Optimize — Technical SEO: canonical, hreflang, JSON-LD

**URL:** https://bixbit.io/en
**Target query:** industrial Bitcoin mining firmware AMS monitoring
**Date:** 2026-09-16
**Scope:** technical-seo only (canonical / hreflang / structured data). H1 consolidation is owned by content-seo (parallel workstream) — not touched here.

Baseline this diffs against: `reports/sub/technical-seo-2026-06-17.md` (2026-06-17 full-audit) — confirmed at that time: **zero canonical, zero hreflang, zero JSON-LD** anywhere on the site, GSC 0 clicks/0 impressions, CLS 0.888 on `/en` (P0, tracked separately, see note in section 6).

Site-structure source of truth: `data/site-structure.md` (crawled 2026-06-17, 70 pages).

---

## 1. Canonical tag

Self-referencing, HTTPS, no trailing slash, no query params:

```html
<link rel="canonical" href="https://bixbit.io/en" />
```

Place in `<head>`, static HTML (see section 8 — implementation requirement).

---

## 2. Hreflang tags

```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en" />
<!-- [VERIFY] /ru counterpart — confirm URL exists, returns 200, and is NOT noindex before deploying this line -->
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru" />
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en" />
```

**Deployment instruction: do NOT ship the `hreflang="ru"` line to production yet.**

Status: `/ru` URL parity is an open `[VERIFY]` from the 2026-06-17 audit (`data/site-structure.md` / `reports/sub/technical-seo-2026-06-17.md` line ~205) — never confirmed that `/ru` exists 1:1 with `/en` pages, returns 200, or isn't noindexed. Shipping an hreflang pair to a non-existent, redirecting, or noindexed URL is worse than shipping no hreflang at all (Google will either ignore the whole cluster or, in edge cases, treat it as a soft signal of low quality).

Rollout order:
1. Ship `hreflang="en"` (self) + `hreflang="x-default"` (→ `/en`) now — this alone fixes ambiguity for English-only crawlers, no dependency on `/ru`.
2. Confirm `/ru` exists, 200s, and is indexable → then add the `ru` line.
3. If `/ru` does not exist or is a stub, drop the `ru` line entirely rather than leaving a broken hreflang pair live.

`x-default` correctly points to `/en` per CLAUDE.md (`/en` is the primary B2B expansion locale, not root `/`).

---

## 3. Organization JSON-LD (corrected)

Source draft: `content/geo/entity-definition-homepage.md`. Two URLs in that draft are wrong — corrected against `data/site-structure.md`:

| Entity | Draft URL (wrong) | Corrected URL |
|---|---|---|
| AMS | `https://bixbit.io/en/monitoring` | `https://bixbit.io/en/ams` |
| Immersion cooling | `https://bixbit.io/en/cooling/immersion` | `https://bixbit.io/en/asics-cooling/immersion-systems` |

Also added (not in draft, present in site-structure): Whatsminer firmware **hub** URL. The draft pointed Whatsminer only at `/en/firmwares/whatsminer-series-m3x` (one sub-series page); the actual hub page is `/en/firmwares/whatsminer-all-series` — using the hub is the correct canonical target for a homepage-level Organization entity, not one sub-model page. Hydro cooling added as a sibling offer since it's an equally real product page.

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
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "SoftwareApplication",
          "name": "BiXBiT Antminer Firmware",
          "applicationCategory": "Mining Software",
          "operatingSystem": "Antminer ASIC",
          "url": "https://bixbit.io/en/firmwares/antminer"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "SoftwareApplication",
          "name": "BiXBiT Whatsminer Firmware",
          "applicationCategory": "Mining Software",
          "operatingSystem": "Whatsminer ASIC",
          "url": "https://bixbit.io/en/firmwares/whatsminer-all-series"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "SoftwareApplication",
          "name": "BiXBiT AMS — Advanced Monitoring System",
          "applicationCategory": "Fleet Management Software",
          "url": "https://bixbit.io/en/ams"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Product",
          "name": "BiXBiT Immersion Cooling",
          "category": "Mining Infrastructure",
          "url": "https://bixbit.io/en/asics-cooling/immersion-systems"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Product",
          "name": "BiXBiT Hydro Cooling",
          "category": "Mining Infrastructure",
          "url": "https://bixbit.io/en/asics-cooling/hydro-systems"
        }
      }
    ]
  }
}
</script>
```

Note on `/en/ams/connect`: per instruction, this URL is NOT used anywhere in this schema (it's the onboarding/connect form flagged `[VERIFY]` noindex in a separate audit). The AMS product entity above points only to the stable hub `/en/ams`.

---

## 4. WebSite JSON-LD

Base entity — no `SearchAction` included. `[VERIFY: confirm whether bixbit.io has an on-site search feature]` — nothing in `data/site-structure.md` or prior crawls indicates a search endpoint/template exists. Do not add `SearchAction` until confirmed; a `potentialAction` pointing at a non-functional or nonexistent search URL is an invalid/misleading structured-data claim and can trigger a manual structured-data quality flag.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "BiXBiT",
  "url": "https://bixbit.io/en",
  "publisher": {
    "@type": "Organization",
    "name": "BiXBiT",
    "url": "https://bixbit.io/en"
  }
}
</script>
```

If site search is later confirmed to exist, the addition is:
```json
"potentialAction": {
  "@type": "SearchAction",
  "target": "https://bixbit.io/en/search?q={search_term_string}",
  "query-input": "required name=search_term_string"
}
```
`[VERIFY]` the actual search URL pattern before adding — the one above is a placeholder, not a confirmed endpoint.

---

## 5. Explicitly out of scope for this page

**Do not add `SoftwareApplication` or `FAQPage` schema to the homepage.**

Both already exist (or are planned) on `/en/firmwares/antminer` per the GEO draft in `content/geo/entity-definition-homepage.md`. Homepage schema in this pass is limited to **Organization + WebSite only**. Reasoning: duplicating `SoftwareApplication`/`FAQPage` entities for the same product (Antminer firmware) on two URLs creates competing/conflicting entity signals for Google (and for LLM extraction under GEO) — the firmware page should be the single canonical source of that structured data, homepage should reference it via `hasOfferCatalog` → `url` link only (as done in section 3), not restate it as a full typed entity.

---

## 6. Regression checklist (run before any commit)

- [ ] **JSON validity**: no trailing commas, all brackets balanced, valid against schema.org vocabulary. Run both blocks (Organization, WebSite) through https://validator.schema.org/ and Google's Rich Results Test before merge.
- [ ] **`@type` correctness**: `Organization`, `WebSite`, `OfferCatalog`, `Offer`, `SoftwareApplication`, `Product` — all valid schema.org types, no typos.
- [ ] **URL correctness against `data/site-structure.md`** — every URL in both JSON-LD blocks cross-checked against the live crawl list, not invented. Confirmed corrections already applied: `/en/ams` (not `/en/monitoring`), `/en/asics-cooling/immersion-systems` (not `/en/cooling/immersion`), `/en/asics-cooling/hydro-systems`, `/en/firmwares/whatsminer-all-series` (hub, not a single sub-series page).
- [ ] **HTTPS everywhere** — no `http://` URLs in canonical, hreflang, or JSON-LD.
- [ ] **Canonical is self-referencing, no trailing slash** — `https://bixbit.io/en` exactly, not `https://bixbit.io/en/`.
- [ ] **No duplicate/competing schema** — confirm homepage does not also carry `SoftwareApplication`/`FAQPage` (see section 5) after this + any other concurrent edit lands.
- [ ] **Single canonical only** — confirm no second, conflicting `<link rel="canonical">` is injected elsewhere in the template (headers, plugins, CMS defaults).
- [ ] **hreflang reciprocity** — once `/ru` line is added (post-VERIFY), confirm `/ru` page links back with a matching hreflang pair to `/en`; one-directional hreflang is invalid.
- [ ] **Static HTML, not JS-injected** — see section 8, mandatory.
- [ ] **CLS 0.888 P0 not reopened here** — this CWV issue is already tracked from the 2026-06-17 baseline (`data/baseline-2026-06-17.json`) as a site-wide P0 unrelated to markup/schema/canonical changes. Adding JSON-LD script tags and two `<link>` elements to `<head>` is negligible payload and should not measurably affect CLS/LCP, but re-run PageSpeed Insights on `/en` post-deploy to confirm no regression, and do not treat this ticket as having "fixed" CLS.
- [ ] **9× `<h1>` issue** — not addressed here (content-seo owns it in parallel). Flag for a joint re-check once content-seo's H1 consolidation lands, since Organization schema `name`/`description` should ideally align with the eventual single H1 copy.

---

## 7. Open [VERIFY] items for the technical team

| # | Item | Why it matters | Blocks |
|---|---|---|---|
| 1 | `foundingDate` for BiXBiT Organization schema | Unverified fact, must not be fabricated | Organization JSON-LD field (currently placeholder) |
| 2 | `sameAs` social/profile URLs (Twitter/X, LinkedIn, GitHub, Telegram) | Unverified; wrong/missing links weaken entity disambiguation for Google + LLMs | Organization JSON-LD `sameAs` array |
| 3 | Does `/ru` exist as a true 1:1 locale of `/en` (all pages), return 200, and is it indexable (not noindex)? | Determines whether hreflang `ru` line can ship at all | hreflang deployment (section 2) |
| 4 | Does bixbit.io have a functioning on-site search? If yes, what's the query URL pattern? | Determines whether `WebSite.potentialAction.SearchAction` can be added | WebSite JSON-LD enhancement (section 4) |
| 5 | Confirm `/en/ams/connect` noindex status is actually deployed (per separate audit flag) | This report deliberately avoids linking it as the AMS canonical URL; if noindex isn't actually live, that's a separate P0 for indexation, not for this schema | Cross-check with indexation audit |

---

## 8. Implementation requirement — mandatory

**All of the above (canonical, hreflang, JSON-LD) must be present in static HTML inside `<head>` on initial server response — not injected via JavaScript after hydration.**

Rationale: `/en/firmwares/antminer` was previously found rendering its `<title>` only via client-side JS (not present in static HTML), per the 2026-06-17 audit's SPA/rendering findings. Googlebot's rendering queue can lag significantly behind crawl/discovery for JS-injected `<head>` elements, and many secondary crawlers (Bing, LLM crawlers for GEO purposes) do not execute JS at all — a JS-injected canonical/hreflang/JSON-LD is invisible to them entirely. Verify via "View Page Source" (not DevTools Elements/Inspect) that all tags in sections 1–4 are present before hydration runs.

---

## Data availability note

This deliverable is pure on-page/technical markup — no live GSC, PageSpeed, or DataForSEO calls were needed or made. CWV figures cited (CLS 0.888) are pulled from the existing baseline snapshot (`data/baseline-2026-06-17.json`), not re-fetched. If a fresh CWV re-check is wanted post-deploy, that's a separate `/weekly-drift` or direct PageSpeed run.
