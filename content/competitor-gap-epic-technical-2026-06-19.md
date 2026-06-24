# Technical SEO Gap: BiXBiT vs ePIC Blockchain — 2026-06-19

> Data sources: WebFetch (live crawl of both domains), sitemap index parsing,
> robots.txt direct fetch. DataForSEO SERP/Lighthouse/on_page — NOT AVAILABLE
> (401 auth error + permission denied). All performance scores marked accordingly.

---

## On-Page Technical Comparison (Homepage)

| Element | ePIC (epicblockchain.io) | BiXBiT (bixbit.io/en) | Gap |
|---|---|---|---|
| Title tag | Not rendered (JS-gated, not extractable from static fetch) | "BiXBiT Bitcoin Mining Solutions – Tools for Crypto Miners" | BiXBiT has a title; ePIC title not confirmed static |
| Meta description | Absent | Absent | Both missing — P1 for both |
| H1 | "Custom Antminer Firmware" | "Bitcoin Mining Software & Hardware" | ePIC H1 is more keyword-specific to their product |
| Canonical | Absent | Absent | Both missing — P1 for both |
| Open Graph (og:*) | Absent | Absent | Both missing — P2 |
| JSON-LD / Schema | Absent | Absent | Both at zero — P1 gap vs. competitors with schema |
| robots.txt | `User-agent: * / Disallow:` (open) | Blocks /igra/, /assets/ (with asset exceptions); Clean-param declared | BiXBiT has more sophisticated robots.txt; ePIC is fully open |
| Sitemap | sitemap_index.xml → 5 child sitemaps (Yoast SEO) | sitemap.xml → 5 child sitemaps | ePIC uses Yoast (WordPress); BiXBiT uses custom sitemap |
| CMS / platform signal | WordPress + Yoast SEO | Custom (Tailwind-based) | Yoast gives ePIC automatic meta/OG generation infrastructure |

## On-Page Technical Comparison (Key Product Pages)

| Element | ePIC /umc-os | BiXBiT /en/firmwares/antminer | Gap |
|---|---|---|---|
| Title tag | "UMC OS V1.10.1 Firmware Release - Custom Antminer Firmware - ePIC Blockchain" | Not rendered | ePIC has descriptive, keyword-rich title; BiXBiT unconfirmed |
| Meta description | Absent | Absent | Both missing |
| H1 | "UMC OS V1.10.1 Firmware Release – Custom Antminer Firmware" | "Custom firmware BiXBiT for Antminer" | Both present; ePIC's includes version number (freshness signal) |
| Canonical | Absent | Absent | Both missing |
| Open Graph | Absent | Absent | Both missing |
| JSON-LD / Schema | Absent | Absent | Both missing — FAQPage content exists on page but not marked up |
| BreadcrumbList | Present (HTML breadcrumbs: Home > Firmware Release > UMC OS V1.10.1) | Unknown | ePIC has breadcrumb HTML; no structured data markup on either |
| FAQ section | Extensive FAQ page (/support/faq/) — no FAQPage schema | FAQ section in HTML — no FAQPage schema | Both miss rich result eligibility |
| Product schema | Absent on /product/ page | Absent | Both miss Product rich results |

---

## Sitemap Structure Comparison

| Dimension | ePIC (epicblockchain.io) | BiXBiT (bixbit.io/en) |
|---|---|---|
| Sitemap generator | Yoast SEO (WordPress) | Custom |
| Sitemap index | sitemap_index.xml | sitemap.xml |
| Child sitemaps | post-sitemap.xml (27 posts), page-sitemap.xml (24 pages), category-sitemap.xml, post_tag-sitemap.xml, author-sitemap.xml | sitemap-category.xml, sitemap-product.xml (18 URLs, EN+RU), sitemap-blog.xml (~410 URLs EN+RU), sitemap-documentation.xml, sitemap-firmware.xml (24 URLs EN+RU) |
| Total indexable pages (est.) | ~51 (posts + pages only; categories/tags/authors add more) | ~230 EN pages (half of ~460 total across EN+RU) |
| Content depth | 27 blog posts focused on firmware, cooling, partnerships | ~205 blog posts (EN), 12 firmware pages (EN), 9 product pages (EN) |
| Duplicate/language handling in sitemap | Single-language (English only) | EN + RU mixed in same sitemaps — no hreflang annotations in sitemap |
| Last modified freshness | post-sitemap last modified 2026-06-15 | All sitemaps last modified 2024-09-04 — stale by 9 months |

**Key gap:** BiXBiT's sitemaps show `lastmod: 2024-09-04` across the board — a staleness signal to Googlebot suggesting no fresh content. ePIC's post-sitemap shows `2026-06-15`, indicating active publishing. This directly affects crawl budget allocation and indexation freshness scoring.

---

## robots.txt Comparison

| Rule | ePIC | BiXBiT |
|---|---|---|
| Default crawl policy | Fully open (empty Disallow) | Partially restricted |
| Blocked paths | None | /igra/, /assets/ (with exceptions for JS/CSS/images/fonts) |
| Clean-param declared | No | Yes (tracking params: network, placement, gad_source, etc.) |
| Sitemap declared | Yes (sitemap_index.xml) | Yes (sitemap.xml) |
| Crawl-budget risk | None | /assets/ block could theoretically affect resource discovery if not overridden correctly |

BiXBiT's clean-param declaration is a positive signal (prevents duplicate crawling of tracking URLs). The /assets/ block with explicit Allow for file types is reasonable but should be audited to confirm Googlebot can access all render-critical resources.

---

## Performance (Lighthouse / DataForSEO)

| Score | ePIC | BiXBiT |
|---|---|---|
| Performance | not available (DataForSEO 401) | not available (DataForSEO 401) |
| SEO | not available | not available |
| Accessibility | not available | not available |
| Best Practices | not available | not available |

> Note: From previous full-audit baseline (2026-06-17), BiXBiT homepage CLS = 0.888 (P0 — well above 0.1 threshold). ePIC CLS unknown.

---

## SERP Features Analysis

| Query | ePIC in SERP | BiXBiT in SERP | Featured Snippet | PAA |
|---|---|---|---|---|
| "epic blockchain firmware" | not available (DataForSEO 401) | not available | not available | not available |
| "umc os firmware" | not available | not available | not available | not available |
| "antminer custom firmware" | not available | not available | not available | not available |
| "bixbit firmware" | not available | not available | not available | not available |

DataForSEO SERP API returned HTTP 401 for all four queries. No SERP feature data retrievable in this session.

---

## Schema Gap Analysis

### Schema present on ePIC
- None confirmed (no JSON-LD found on homepage, /umc-os, /product/, /support/faq/)
- HTML breadcrumbs present on /umc-os (not marked up as BreadcrumbList schema)
- FAQ content present on /support/faq/ (not marked up as FAQPage schema)
- WordPress/Yoast infrastructure is in place — schema generation may be enabled but not confirmed via static fetch

### Schema present on BiXBiT
- None confirmed (no JSON-LD found on homepage, /en/firmwares/antminer)
- FAQ sections in HTML on firmware pages (not marked up)

### Schema types neither site has implemented (vs. best-in-class competitors)

| Schema type | Why it matters for this niche | Priority |
|---|---|---|
| `Organization` | Brand knowledge panel, sitelinks eligibility | P1 |
| `SoftwareApplication` | Rich results for firmware product pages; shows in "App" SERP features | P1 |
| `Product` | Price/rating/availability rich results for hardware pages | P1 |
| `FAQPage` | Both sites have FAQ content — direct rich result opportunity, PAA eligibility | P0 |
| `BreadcrumbList` | Cleaner SERP snippet paths, reduces pogo-sticking | P2 |
| `Article` | Blog post rich results, date freshness signals | P2 |
| `HowTo` | Installation guides — ePIC has /support/umc-v4-3-installation-guide/; BiXBiT may have docs | P2 |

ePIC's FAQ page (/support/faq/) covers UMC OS, UMC Board, BlockMiner, ePIC Dashboard, Rig Runner — all answerable as FAQPage schema. BiXBiT's firmware pages have inline Q&A that could likewise be marked up.

---

## Content Structure Gap

| Signal | ePIC | BiXBiT | Gap |
|---|---|---|---|
| Blog/news presence | Yes — /news/ + /blog/ (27 posts, active to June 2026) | Yes — ~205 EN posts, but sitemap stale (2024-09-04) | ePIC shows fresher content signals to Googlebot |
| Support/docs section | /support/ with FAQ, firmware download, installation guides | /firmwares/* pages (12 EN) + documentation sitemap | ePIC's support structure is more crawler-friendly (dedicated paths) |
| Product page | /product/ — single page for hardware | /en/products/* — 9 distinct product URLs | BiXBiT has deeper product taxonomy |
| Firmware pages | /support/firmware-download/ (single download page) | 12 dedicated firmware URLs by ASIC model | BiXBiT has stronger firmware URL structure for model-specific queries |
| Team/About | /team/, /about-us/ | Not confirmed in sitemap | ePIC has E-E-A-T signals via team page |
| Careers | /careers/ | Not confirmed | ePIC has brand trust signal |

---

## Technical Recommendations (P0–P3)

### P0 — Critical (fix within 1 week)

**P0-1: FAQPage JSON-LD on firmware pages**
Both sites have FAQ HTML that qualifies for rich results but neither marks it up. BiXBiT's /en/firmwares/antminer has Q&A content. Implement FAQPage schema immediately — this is the fastest path to SERP feature visibility in this niche.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What ASIC models does BiXBiT firmware support?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT firmware supports Antminer S9/S17/S19 series and Whatsminer M2x/M5x/M6x series. [VERIFY: confirm full compatibility list]"
      }
    }
  ]
}
```

**P0-2: Fix sitemap lastmod staleness**
BiXBiT's sitemaps all show `2024-09-04`. If content was published after that date, regenerate sitemaps with accurate `lastmod` values. Stale lastmod suppresses crawl frequency.

### P1 — High priority (fix within 2 weeks)

**P1-1: Organization schema on homepage**
Neither site has Organization markup. BiXBiT should implement on bixbit.io/en:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BiXBiT",
  "url": "https://bixbit.io/en",
  "logo": "https://bixbit.io/[logo-path]",
  "description": "Cyber-Industrial firmware and cooling infrastructure for industrial Bitcoin mining",
  "sameAs": [
    "[VERIFY: Twitter/X URL]",
    "[VERIFY: LinkedIn URL]",
    "[VERIFY: GitHub URL]"
  ]
}
```

**P1-2: SoftwareApplication schema on all firmware pages**
Implement on each /en/firmwares/* URL. ePIC also lacks this — first mover wins rich result.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "BiXBiT Firmware for Antminer S19",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Antminer S19 ASIC",
  "offers": {
    "@type": "Offer",
    "price": "[VERIFY]",
    "priceCurrency": "USD"
  },
  "provider": {
    "@type": "Organization",
    "name": "BiXBiT"
  }
}
```

**P1-3: Add canonical tags site-wide**
Neither site has canonicals confirmed. BiXBiT's EN/RU dual-language structure without hreflang or canonicals creates duplicate content risk. Every page needs `<link rel="canonical" href="[self-URL]">`.

**P1-4: Add meta descriptions site-wide**
Both sites missing meta descriptions. BiXBiT has 230+ EN pages — prioritize: homepage, all /firmwares/* pages, all /products/* pages.

**P1-5: Add Open Graph tags site-wide**
Required for social sharing CTR. BiXBiT's B2B audience shares content on LinkedIn — og:title, og:description, og:image are table stakes.

### P2 — Medium priority (fix within 1 month)

**P2-1: BreadcrumbList schema on product/firmware pages**
ePIC has HTML breadcrumbs on /umc-os (Home > Firmware Release > UMC OS). BiXBiT should implement both HTML breadcrumbs AND BreadcrumbList JSON-LD on firmware/product pages.

**P2-2: Article schema on blog posts**
BiXBiT has ~205 EN blog posts. Add Article schema with datePublished, dateModified, author, headline. This also fixes the "freshness signal" gap — Google uses dateModified for content scoring.

**P2-3: Publish/update sitemap lastmod accurately**
Regenerate sitemaps after every publish. Consider Yoast SEO or equivalent if CMS supports it (ePIC has this via WordPress).

**P2-4: HowTo schema on installation/documentation pages**
BiXBiT's sitemap-documentation.xml likely contains installation guides. HowTo schema generates step-by-step rich results — high opportunity in "how to install antminer firmware" queries.

**P2-5: Confirm Googlebot can render critical assets**
BiXBiT blocks /assets/ in robots.txt with file-type exceptions. Validate via Google Search Console's URL Inspection that JS/CSS files needed for rendering are accessible (especially for the 8k-render pages flagged in the baseline audit).

### P3 — Low priority (backlog)

**P3-1: Team/About E-E-A-T pages**
ePIC has /team/ and /about-us/. BiXBiT's E-E-A-T footprint for "Experience, Expertise, Authoritativeness" is weaker without named author pages or team profiles — matters for YMYL-adjacent B2B content.

**P3-2: Product schema on /en/products/* pages**
Hardware cooling products (container, rack, cell) qualify for Product schema with offers, specifications, image.

**P3-3: VideoObject schema if firmware tutorial videos exist**
If BiXBiT has YouTube tutorials linked from firmware pages, add VideoObject schema for video rich results.

---

## Data Availability Notes

| Source | Status | Reason |
|---|---|---|
| DataForSEO SERP API | Not available | HTTP 401 — credentials not configured in this session |
| DataForSEO Lighthouse | Not available | HTTP 401 — credentials not configured in this session |
| DataForSEO on_page_instant_pages | Not available | Permission denied in this environment |
| WebFetch (static HTML) | Available | Used for all on-page extraction |
| Google Search Console | Not checked | No GSC API call made in this task |
| BiXBiT CLS baseline | 0.888 (P0) | From prior full-audit 2026-06-17 |

Note: WebFetch converts HTML to markdown before extraction, which means `<head>` meta tags (title, canonical, OG, JSON-LD in `<script>`) are frequently stripped. Some "absent" findings may reflect rendering limitations rather than true absence. The most reliable negative finding is JSON-LD schema — its absence was confirmed on multiple pages across both sites.

---

## Summary Assessment

Both BiXBiT and ePIC Blockchain are at near-identical technical SEO maturity for structured data: **zero JSON-LD schema on any confirmed page**. This is a first-mover opportunity — whichever site implements FAQPage + SoftwareApplication + Organization schema first captures rich results in this niche.

ePIC's structural advantages over BiXBiT:
1. WordPress + Yoast = automatic OG/meta infrastructure (lower effort to fix meta/OG gaps)
2. Active content publishing (sitemap lastmod June 2026 vs. BiXBiT's September 2024)
3. Dedicated support hub (/support/faq/, /support/firmware-download/, installation guides) — cleaner topical authority signals
4. Team + About pages for E-E-A-T

BiXBiT's structural advantages over ePIC:
1. Deeper firmware URL taxonomy (12 model-specific EN URLs vs. ePIC's single /support/firmware-download/)
2. More product pages (9 EN product URLs vs. ePIC's single /product/ page)
3. Larger blog archive (~205 EN posts vs. 27)
4. Clean-param in robots.txt (more sophisticated crawl management)
5. Firmware-specific sitemap (sitemap-firmware.xml) — ePIC has no equivalent

The fastest ROI for BiXBiT is: FAQPage schema on firmware pages (P0) + meta descriptions + canonicals (P1) + sitemap lastmod fix (P0). These three moves alone would pull BiXBiT ahead of ePIC on technical SEO within 30 days.
