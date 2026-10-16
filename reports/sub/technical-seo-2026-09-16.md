# Technical SEO Audit — bixbit.io/en
**Date:** 2026-09-16
**Scope:** https://bixbit.io/en (English locale, B2B ASIC firmware + industrial cooling)
**Auditor:** Technical SEO Agent
**Prior baseline:** `reports/sub/technical-seo-2026-06-17.md` (2026-06-17)

**Methodology note:** WebFetch converts pages to markdown and cannot see `<head>` or
`<script>` content (confirmed via repeated false-negative results earlier today on
canonical/hreflang/JSON-LD checks). All technical-element claims in this report (canonical,
hreflang, meta description, meta robots, JSON-LD) are based on **raw HTML fetched via `curl`**
with a real HTTP status code, not WebFetch's rendering. WebFetch was used only for
body-content/navigation checks (page purpose, H1, links).

---

## Executive Summary

**The June 2026-06-17 baseline is substantially stale and must not be reused as current fact.**
Three months of undocumented site changes have occurred. The two most important corrections:

1. **The June "zero canonical / zero meta description / zero JSON-LD sitewide" findings are
   WRONG as of today.** Canonical tags, meta descriptions, and JSON-LD (WebSite + Organization,
   partial BreadcrumbList/FAQPage) are now deployed on every one of the 10 pages checked this
   pass. This was likely already true in June too — WebFetch cannot see `<head>`, so the June
   audit (if it also relied on WebFetch) may have reported false negatives from day one. Anyone
   using this repo's prior report to justify "add schema/canonical from scratch" work should
   re-scope that work as **fix/complete existing schema**, not **greenfield build**.
2. **Five URLs suspected dead/missing (`/en/products/pdu`, `/en/blog`, `/en/faq`, `/en/calc`,
   `/en/documentation`) are all live, real, content-rich pages (HTTP 200)**, none in the old
   site-structure.md. `data/site-structure.md` has been rewritten (see that file) — this was
   priority #1 per task instructions and is complete.

That said, real and new problems were found: a **confirmed, sitewide copy-paste bug in the
Organization JSON-LD description** (cooling-product ad copy served as the company description on
every single page), a **broken empty `FAQPage` schema** on two hub pages, a **duplicated
`BreadcrumbList` bug** on `/en/documentation`, **hreflang deployed on only 2 of 10+ templates**,
**7 legacy Antminer firmware pages silently noindexed and dropped from the sitemap** (needs human
confirmation this was intentional), a **placeholder meta description on `/en/faq`**, and the
**`/en/products/pdu` page has zero sitemap presence** despite being a fully built commercial page.
`Product`/`SoftwareApplication` schema is still completely absent sitewide — unchanged from June.

**Health score: MODERATE-TO-SERIOUS** (upgraded from June's CRITICAL — foundational technical
elements exist now — but several are broken or half-deployed in ways that actively produce bad
signals to Google, not just absence of signal).

---

## 1. site-structure.md — updated (priority #0 this pass)

`data/site-structure.md` has been rewritten with a 2026-09-16 crawl date. Summary of changes:
- Added **PDU** section (was "NOT FOUND") — `/en/products/pdu` confirmed live.
- Added **Blog** section (was "NOT FOUND") — `/en/blog` hub + ~400-URL sitemap confirmed, actively
  publishing (newest post 2026-09-09).
- Added **Documentation** section (previously unstructured "Knowledge Base" mention) — hub +
  5 articles enumerated with URLs and lastmod dates.
- Added **Tools** section — `/en/faq`, `/en/calc`, both confirmed live with real content.
- Firmware section updated with a major architecture change: **7 legacy Antminer model pages
  (asic-s19, asic-S17-S17Pro, asic-S17-plus, asic-T17-plus, asic-T17, asic-T9-plus,
  asic-s9-s9j-s9i) are still live but now noindex,follow, duplicate-titled against the antminer
  hub, and removed from sitemap-firmware.xml** — flagged `[VERIFY]`.
- Every entry now carries a per-page technical fingerprint (canonical/hreflang/meta
  description/JSON-LD presence) captured this pass, not carried over as assumption.
- Entries not re-touched this pass are explicitly labeled **"not re-verified this pass"** rather
  than silently kept or deleted.

---

## 2. robots.txt

**Fetched from:** https://bixbit.io/robots.txt — **unchanged since June**, byte-for-byte same
directives (Disallow /igra/, /assets/, search, registration, tags, auth, download; Allow
overrides for asset file types; Clean-param; Sitemap directive).

No explicit AI-crawler allow/block rules for GPTBot, ClaudeBot, PerplexityBot, Google-Extended,
CCBot — all remain implicitly **allowed** via the wildcard `User-Agent: *` (no disallow rule
matches their paths). For a brand prioritizing GEO/AI-citation, this remains the correct posture.

**[P1] `/download/` still disallowed — unresolved from June.** Same open question: does this
block firmware binary downloads linked from firmware pages? Not re-verified this pass; carry
forward as `[VERIFY]`.

**[P2] `Clean-param` remains a Yandex-only, non-standard directive** — ignored by Google/Bing,
harmless but should not be relied on for canonicalization there.

---

## 3. Sitemap

**Sitemap index:** https://bixbit.io/sitemap.xml → 5 child sitemaps, same file names as June
(sitemap-category.xml, sitemap-product.xml, sitemap-blog.xml, sitemap-documentation.xml,
sitemap-firmware.xml).

| Sitemap | en URLs | Change vs. June | Key issues |
|---|---|---|---|
| sitemap-category.xml | 10 | same count | still missing `/en/asics-cooling*` (3 pages), `/en/documentation` hub, `/en/products/pdu` |
| sitemap-product.xml | 7 | same count | `/en/products/coolant` duplicate entry **still present**; `/en/products/ container-1k` **still has a literal space** (confirmed the space-free URL is a live 200 page — this is a sitemap generation bug, not a dead page); **`/en/products/pdu` entirely absent** |
| sitemap-firmware.xml | 6 | **down from 13** | 7 legacy Antminer model pages removed — consistent with their new noindex status (see Firmware section below) |
| sitemap-documentation.xml | 5 | new coverage confirmed | only child articles listed; hub page `/en/documentation` itself not in any sitemap |
| sitemap-blog.xml | ~400 (en+ru) | **up from ~290** | actively growing; newest lastmod 2026-09-09 (6 days old); oldest still 2018-10-15 (thin/stale posts still included, unresolved P2 from June) |

**[P0] `/en/products/pdu` has zero sitemap presence.** This is a fully built, live commercial
page (Smart PDU product, 6/12/16/20-pin configs, quote form) with a working canonical and basic
schema, but Google has no sitemap-based discovery path to it — it relies entirely on internal
links (confirmed linked from `/en/firmwares` "Order PDU" CTA). Add to sitemap-category.xml or a
new sitemap-pdu.xml entry immediately.

**[P1] `/en/asics-cooling` + 2 sub-pages still absent from every sitemap — unresolved 3 months
after being flagged P1 in June.** These are live, indexable, canonical-tagged pages targeting
high-value "immersion cooling" / "hydro cooling" queries with zero sitemap discoverability.

**[P1] Duplicate + malformed URL bugs in sitemap-product.xml are unresolved 3 months later**
(`/en/products/coolant` duplicate; `/en/products/ container-1k` space bug). Same fix recommended
in June was not applied — flag to dev/CMS owner as a recurring sitemap-generator defect, not a
one-off.

**[P2] Stale lastmod dates persist on sitemap-category.xml and sitemap-product.xml** (2024-09-04
sitewide) even though the actual pages (e.g. `/en/firmwares`, `/en/ams`) have visibly changed
(new meta descriptions, new JSON-LD) since then. sitemap-firmware.xml and
sitemap-documentation.xml *do* show realistic, varied lastmod dates — the sitemap generator
appears to only correctly timestamp those two files.

---

## 4. Canonical Tags — REVERSED from June finding

**Checked pages (raw HTML, 2026-09-16):** `/en`, `/en/ams`, `/en/firmwares`,
`/en/firmwares/antminer`, `/en/products/pdu`, `/en/firmwares/asic-s19` (+6 more legacy firmware
pages), `/en/asics-cooling`, `/en/blog`, `/en/faq`, `/en/documentation`, `/en/calc` — **10/10
pages have a correct, self-referencing `<link rel="canonical">` tag.**

Example (homepage):
```html
<link rel="canonical" href="https://bixbit.io/en"/>
```

**[P2] `/en/blog` emits the canonical tag twice** (identical duplicate `<link rel="canonical">`
found in source). Not harmful to Google (same URL, so no conflicting signal) but indicates a
templating bug worth a quick dev fix — duplicate `<link>` tags in `<head>` are a minor code-smell
that can compound with other template bugs.

**No further canonical work needed at P0/P1 — this item can be closed out from the backlog.**

---

## 5. Hreflang — partially deployed, most commercial pages still missing it

**Result: hreflang found on only 2 of the ~10 templates checked** — `/en/blog` and `/en/calc`.
Both show:
```html
<link rel="alternate" href="https://bixbit.io/en/blog" hreflang="x-default"/>
<link rel="alternate" href="https://bixbit.io/ru/blog" hreflang="ru"/>
```

**Absent** on: `/en` (homepage), `/en/ams`, `/en/firmwares`, `/en/firmwares/antminer`,
`/en/products/pdu`, `/en/asics-cooling`, `/en/faq`, `/en/documentation`, all 7 legacy Antminer
firmware pages — despite confirmed `/ru/*` counterparts existing for most of these in
sitemap-category.xml and sitemap-firmware.xml.

**[P0] Hreflang missing on the highest-commercial-value templates** (homepage, firmware hub,
antminer hub, PDU, cooling hub, AMS, FAQ). Only the blog and calculator templates got it. This is
a partial rollout, not a global gap — dev has clearly built the capability (it works correctly on
2 templates) but has not extended it to the money pages. Recommended fix, same pattern already
proven on `/en/calc`:

```html
<!-- On https://bixbit.io/en/firmwares/antminer -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer"/>
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer"/>
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer"/>
```

`[VERIFY]`: confirm every `/ru/*` counterpart URL actually exists before wiring hreflang pairs
(spot-checked `/ru` presence in sitemap-category.xml/firmware.xml only, did not fetch `/ru/*`
pages this pass).

---

## 6. JSON-LD Schema — deployed but with real bugs

**Checked pages (raw HTML):** `/en`, `/en/ams`, `/en/firmwares`, `/en/firmwares/antminer`,
`/en/products/pdu`, `/en/firmwares/asic-s19`, `/en/asics-cooling`, `/en/blog`, `/en/faq`,
`/en/documentation`, `/en/calc`.

**Result: every page has at least `WebSite` + `Organization` JSON-LD.** This directly reverses
the June "zero JSON-LD sitewide" finding. Several pages also have `BreadcrumbList` and/or
`FAQPage`. However:

### Bug 1 — [P1] Organization schema `description` is cooling-page ad copy, reused sitewide
Confirmed byte-identical on **every single page checked** (homepage, ams, firmwares, antminer,
pdu, asics-cooling, faq, documentation, blog, calc):
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BiXBiT",
  "description": "BiXBiT immersion cooling systems for mining ✅ Safe construction, maximum hashrate without a risk of overheating ✅ Non-toxic and eco-friendly coolant ➤ Worldwide shipping!",
  "url": "https://bixbit.io/en",
  "logo": "https://bixbit.io/site/images/logo_header.svg",
  "sameAs": [
    "https://www.facebook.com/bixbit.official",
    "https://www.instagram.com/bixbit.official/",
    "https://www.youtube.com/channel/UC7qDZbXNlHnX-yU3bgBZtnw"
  ]
}
```
This description is cooling-product marketing copy, not a company description — it is factually
misleading as the `Organization` entity's description on e.g. the PDU or firmware pages, and
weakens E-E-A-T / Knowledge Panel signal quality for the brand as a whole. `name`, `url`, `logo`,
and `sameAs` (real Facebook/Instagram/YouTube profiles) are correctly populated and can stay as-is.

**Fix — replace `description` only, keep everything else:**
```json
"description": "BiXBiT is an industrial provider of custom ASIC firmware, monitoring software, and cooling infrastructure for professional Bitcoin mining operations."
```
`[VERIFY: exact company description wording — hand to content owner, do not ship generated copy as fact without sign-off]`

### Bug 2 — [P2] `FAQPage` schema deployed with an empty `mainEntity` array
Found on `/en/firmwares` and `/en/documentation`:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": []
}
```
An empty `FAQPage` is invalid for rich-result eligibility and will likely surface as a warning in
GSC's Enhancements report. Either populate `mainEntity` with real Q&A for that page, or remove the
schema block entirely on pages without FAQ content — don't ship the empty wrapper.

### Bug 3 — [P0] The actual `/en/faq` page has NO FAQPage schema
Ironic gap: `/en/ams` (which has an FAQ widget) correctly ships `FAQPage` with real content
("What is BiXBiT AMS?", "Is the BiXBiT AMS system paid?" — confirmed real Q&A). `/en/documentation`
and `/en/firmwares` ship a broken empty `FAQPage`. But `/en/faq` — the site's dedicated FAQ page,
confirmed via WebFetch to have two real content sections ("BiXBiT Immersion Cooling Systems" and
"Firmware and BiXBiT AMS" with genuine Q&A on dev-fee cost, warranty, flashing difficulty, leak
risk, noise, etc.) — has **only WebSite + Organization, no FAQPage at all.** This is the single
highest-value, lowest-effort schema fix available on the whole site (real content already exists,
just needs to be wrapped in FAQPage markup).

### Bug 4 — [P1] `BreadcrumbList` on `/en/documentation` has the wrong section name
```json
{
  "@type": "ListItem",
  "position": 2,
  "item": { "@id": "/en/firmwares", "name": "Firmwares" }
}
```
This is on the **Documentation** page — it should read `{"@id": "/en/documentation", "name":
"Documentation"}`. Looks like the firmware hub's breadcrumb JSON-LD block was copy-pasted onto
the documentation template without updating the values. Straightforward template fix.

### Bug 5 — [P2] `BreadcrumbList` "Home" item has a malformed double-`/en/en` id
Found identically on `/en/blog` and `/en/calc`:
```json
{ "@type": "ListItem", "position": 1, "item": { "@id": "https://bixbit.io/en/en", "name": "Home" } }
```
Should be `"@id": "https://bixbit.io/en"`. Looks like string concatenation of a base path that
already includes `/en` plus an additional hardcoded `/en` segment. Same root-cause class of bug
across both affected templates — likely one shared breadcrumb component.

### Bug 6 — [P2] `WebSite` schema emitted per-page with the page's own URL
Every page emits its own `{"@type": "WebSite", "url": "<this page's URL>"}` instead of a single
site-level `WebSite` entity pointing at the homepage/root. Non-standard usage of the `WebSite`
type (which is meant to describe the site as a whole, once). Low priority, but worth flattening
into a single sitewide statement when the other schema bugs get fixed.

### Still fully absent — unchanged from June
**[P0] No `Product` or `SoftwareApplication` schema anywhere**, including `/en/firmwares/antminer`
(flagship firmware hub) and `/en/products/pdu` (flagship hardware product) — the two highest
commercial-value schema types called for in `CLAUDE.md` §schema-priorities are still 100% missing.
Ready-to-implement snippets from the June report remain valid and are **not duplicated here** —
see `reports/sub/technical-seo-2026-06-17.md` §6 for the drafted `SoftwareApplication` JSON-LD;
apply it now that `Organization`/`WebSite` boilerplate already exists on the page (append, don't
replace).

**Important process note for whoever runs `/page-optimize` next:** the JSON-LD snippets already
drafted in `content/page-optimize/homepage.md`, `content/page-optimize/ams.md`, and
`content/page-optimize/firmwares.md` are **proposals**, written without visibility into the schema
that is actually already live (their authors were also working from WebFetch, which cannot see
it). Before shipping any of those snippets, diff them against what's actually in production
(`WebSite` + `Organization` + partial `BreadcrumbList`/`FAQPage`, per this report) so the deploy
**adds** `Product`/`SoftwareApplication` and **fixes** the bugs above, instead of duplicating or
overwriting existing (partially working) schema blocks.

---

## 7. Meta Descriptions — REVERSED from June finding, with quality issues

**Result: every page checked has a `<meta name="description">` tag** — reverses June's "zero
meta descriptions sitewide" finding.

**[P0] `/en/faq` meta description is a literal placeholder stub, not real copy:**
```html
<meta name="description" content="FAQs start with a question and then provide a concise answer">
```
This reads like unedited CMS/template boilerplate instruction text, not a description written for
searchers. Immediate rewrite needed — this is a one-line fix with outsized CTR impact since FAQ
pages often surface in search with rich snippets.

Suggested replacement (`[VERIFY]` before shipping):
```html
<meta name="description" content="Answers to common questions about BiXBiT immersion cooling systems, custom ASIC firmware, and AMS monitoring — leak safety, dev fees, warranty, and setup.">
```

**[P1] `/en/firmwares/asic-s19` (and all 6 other legacy Antminer model pages) duplicate the
antminer hub's meta description verbatim** — same text as `/en/firmwares/antminer`: "Boost
hashrates, cut energy costs, and optimize ASIC performance with Antminer custom firmware by
BiXBiT. Easy download and 24/7 support." Since these pages are noindex'd, this is lower urgency
than a live duplicate-content issue, but confirms the pages were never given unique meta content
before being deprecated — relevant context for the `[VERIFY]` decision on whether to keep them
noindexed or 301 them to the hub.

**No further meta-description backlog item at P0/P1 beyond the two above** — this can mostly be
closed out from the June backlog.

---

## 8. Meta Robots / Noindex

**[P1] 7 legacy Antminer firmware pages carry `<meta name="robots" content="noindex, follow">`**
— confirmed uniformly on `/en/firmwares/asic-s19`, `asic-S17-S17Pro`, `asic-S17-plus`,
`asic-T17-plus`, `asic-T17`, `asic-T9-plus`, `asic-s9-s9j-s9i`. Combined with their removal from
sitemap-firmware.xml, this reads as a deliberate consolidation into `/en/firmwares/antminer`. No
other checked page had a `noindex` directive. **`[VERIFY]` with dev/content owner: confirm intent.**
If intentional, a 301 redirect to the hub (rather than noindex + self-canonical + keep-alive) may
consolidate link equity more cleanly, if these URLs still carry backlinks — check Search
Console/backlink data before deciding (unavailable this pass, see Data Gaps).

---

## 9. Indexation (GSC)

**Status: NO ACCESS this session.** No GSC MCP/API connector was reachable — not re-tested this
pass per task scope (prior session already confirmed no connector available). The June baseline
("0 clicks / 0 impressions over 90 days") is **3 months old and not re-confirmed** — do not treat
it as current. Given that canonical/meta/JSON-LD have visibly changed since June, GSC data has
likely changed too (for better or worse) and must be re-pulled the next time a GSC connector is
available before drawing indexation conclusions.

---

## 10. Core Web Vitals

**Status: NO ACCESS this session** — no PageSpeed Insights/CrUX connector available (confirmed
via ToolSearch + blocked `.env` read per permission rule, consistent with prior session findings).

The June baseline figure (`data/baseline-2026-06-17.json`: **CLS = 0.888**, flagged P0) is
**three months old and NOT re-confirmed in this pass.** Do not cite it as current CWV status in
any downstream report or client-facing material — cite it only as "last known baseline,
2026-06-17, unverified since." Re-run PageSpeed Insights manually the moment API access is
restored:
```
https://pagespeed.web.dev/report?url=https%3A%2F%2Fbixbit.io%2Fen&strategy=mobile
```

---

## 11. HTTP Status Codes (new data this pass — was unavailable in June)

Spot-checked 21 URLs via raw `curl -w "%{http_code}"` this pass, all returned **HTTP 200** with no
redirect chains observed (`url_effective` matched requested URL in every case):
`/en`, `/en/ams`, `/en/firmwares`, `/en/firmwares/antminer`, `/en/products/pdu`, `/en/blog`,
`/en/faq`, `/en/calc`, `/en/documentation`, `/en/asics-cooling`, `/en/asics-cooling/hydro-systems`,
`/en/asics-cooling/immersion-systems`, `/en/about`, `/en/contacts`, `/en/sustainability`,
`/en/ams/connect`, `/en/products/container-1k`, and all 7 legacy Antminer model pages.

**One 404 confirmed:** the literal space-containing URL from sitemap-product.xml
(`/en/products/ container-1k`, URL-encoded as `%20`) returns **HTTP 404** — proving the sitemap
entry is a generator bug, not a genuinely missing page (the correct URL without the space is a
live 200).

No internal-link-graph or full-site status sweep was performed (would require a real crawler,
out of scope for a WebFetch/curl-based spot-check pass).

---

## Prioritized Fix Table

| # | Issue | URL(s) | Priority | Impact | Effort | Fix |
|---|---|---|---|---|---|---|
| 1 | `/en/faq` has no FAQPage schema despite real Q&A content | /en/faq | P0 | High | Low | Wrap existing Q&A content in FAQPage JSON-LD — content already exists, just needs markup |
| 2 | Organization schema description is cooling ad copy, sitewide | all pages (Organization block) | P0 | High | Low | Replace `description` field only with a real company description; keep name/url/logo/sameAs |
| 3 | `Product`/`SoftwareApplication` schema still 100% absent | /en/firmwares/antminer, /en/products/pdu, /en/asics-cooling/*, all /en/products/* | P0 | High | Medium | Deploy snippets already drafted in June report §6, adapted to append (not replace) existing WebSite/Organization blocks |
| 4 | `/en/products/pdu` missing from every sitemap | /en/products/pdu | P0 | High | Low | Add to sitemap-category.xml or new sitemap-pdu.xml |
| 5 | Hreflang missing on highest-value templates | /en, /en/ams, /en/firmwares, /en/firmwares/antminer, /en/products/pdu, /en/asics-cooling, /en/faq, /en/documentation | P0 | High | Medium | Extend the working hreflang implementation (already correct on /en/blog, /en/calc) to remaining templates |
| 6 | `/en/faq` meta description is placeholder boilerplate | /en/faq | P0 | Medium | Low | Replace with real descriptive copy (draft above, `[VERIFY]`) |
| 7 | 7 legacy Antminer pages noindexed + dropped from sitemap — undocumented | /en/firmwares/asic-s19, S17-S17Pro, S17-plus, T17-plus, T17, T9-plus, s9-s9j-s9i | P1 | Medium | Low | `[VERIFY]` intent with dev/content owner; consider 301→hub if unintentional or if backlinks exist |
| 8 | Empty `FAQPage` schema (`mainEntity: []`) shipped | /en/firmwares, /en/documentation | P1 | Medium | Low | Populate with real FAQ content or remove the schema block |
| 9 | `BreadcrumbList` wrong section name (copy-paste bug) | /en/documentation | P1 | Medium | Low | Fix item name/id from "Firmwares" → "Documentation" |
| 10 | `/en/asics-cooling` + 2 sub-pages still absent from all sitemaps — unresolved 3 months | /en/asics-cooling, /hydro-systems, /immersion-systems | P1 | High | Low | Add 3 URLs to sitemap-category.xml (same fix recommended in June, still not applied) |
| 11 | Duplicate + malformed URLs in sitemap-product.xml — unresolved 3 months | /en/products/coolant (dup), /en/products/ container-1k (space) | P1 | Medium | Low | Fix sitemap generator; same fix recommended in June, still not applied |
| 12 | `BreadcrumbList` malformed Home id (`/en/en` double-slug) | /en/blog, /en/calc | P2 | Low | Low | Fix breadcrumb component's Home `@id` concatenation logic |
| 13 | Legacy Antminer pages duplicate title+meta description from hub | /en/firmwares/asic-* (7 pages) | P2 | Low | Low | Moot if pages stay noindexed; relevant only if `[VERIFY]` #7 concludes they should be reindexed |
| 14 | `WebSite` schema emitted per-page instead of sitewide | all pages | P2 | Low | Low | Consolidate to a single sitewide WebSite entity pointing at homepage |
| 15 | Duplicate `<link rel="canonical">` tag (same URL, twice) | /en/blog | P2 | Low | Low | Remove duplicate tag in template |
| 16 | `/download/` disallowed in robots.txt — unresolved 3 months | robots.txt | P1 | Medium | Low | `[VERIFY]` whether firmware binaries live under `/download/`; carried forward from June, not re-checked this pass |
| 17 | Stale sitemap lastmod dates (2024-09-04) on category/product sitemaps | sitemap-category.xml, sitemap-product.xml | P2 | Medium | Low | Fix sitemap generator to emit real lastmod (firmware/documentation sitemaps already do this correctly — copy that logic) |
| 18 | Blog sitemap includes 2018-era thin posts | sitemap-blog.xml | P3 | Low | Medium | Content audit for pruning/refresh/noindex candidates — hand to content-seo agent |
| 19 | CWV data unavailable — baseline 3 months stale, unverified | /en (baseline CLS=0.888) | P0 | Unknown | Low | Re-run PageSpeed Insights the moment API access is restored; do not cite the June figure as current |
| 20 | GSC indexation data unavailable — baseline 3 months stale, unverified | all /en/* | P0 | Unknown | Low | Re-pull GSC the moment API access is restored |

---

## Data Gaps (honest accounting)

- **Google Search Console** — no connector reachable this session. June's "0 clicks/impressions"
  figure is stale and unverified; do not reuse it.
- **PageSpeed Insights / CrUX (Core Web Vitals)** — no connector reachable this session. June's
  CLS=0.888 baseline is stale and unverified; do not reuse it as current.
- **GA4, DataForSEO, Moz, Bing Webmaster** — not attempted this pass (out of scope for this
  targeted site-structure/technical pass); flag for the next `/full-audit` run.
- **Full 70+ page re-crawl** — not performed. This pass targeted the 5 flagged URLs, the sitemap
  network, and a handful of high-priority pages (~28 URLs total touched). Everything else in
  `data/site-structure.md` is carried over from June and explicitly labeled "not re-verified this
  pass."
- **`/ru/*` locale pages** — sitemap presence confirmed, but no `/ru/*` page content, schema, or
  status was fetched this pass. Hreflang target validity is therefore `[VERIFY]`, not confirmed.
- **Internal link graph / orphan-page analysis** — not performed; would need a real crawler.
- **Render-blocking/JS execution trace** — not performed; needs Playwright (`seo-visual` skill),
  not run this pass.

---

## [VERIFY] Items for Human Review

- `[VERIFY]` Whether the 7 legacy Antminer model pages (noindex,follow, dropped from sitemap,
  duplicate title/meta) are an intentional content consolidation into `/en/firmwares/antminer`,
  or a broken deploy. If intentional, document it; if not, evaluate 301 redirects instead.
- `[VERIFY]` Real company description for the `Organization` schema `description` field — do not
  ship the drafted replacement copy in this report without content-owner sign-off.
- `[VERIFY]` `/en/faq` meta description replacement copy — draft provided, needs sign-off before
  shipping.
- `[VERIFY]` Whether `/en/download/` (disallowed in robots.txt) hosts any firmware binaries linked
  from firmware pages — unresolved for 3 months, not re-checked this pass.
- `[VERIFY]` All `/ru/*` counterpart URLs actually exist and are live before wiring hreflang pairs
  on the remaining templates.
- `[VERIFY]` The 2026 `[VERIFY]` items from the June report that were not re-touched this pass
  (GSC property configuration, `/en/ams/connect` noindex decision, `x-default` hreflang target)
  remain open — see `reports/sub/technical-seo-2026-06-17.md` for original context.
- Technical firmware specs (J/TH, °C, model compatibility) were not asserted anywhere in this
  report as new fact — none were generated or verified this pass, per CLAUDE.md rule #4.
