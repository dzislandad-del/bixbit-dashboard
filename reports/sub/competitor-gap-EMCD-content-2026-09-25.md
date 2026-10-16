# Content / Keyword Gap: BiXBiT vs EMCD (emcd.io) — 2026-09-25

**Scope:** US/en (main), Kazakhstan/ru (the CIS proxy). Clusters: firmware, ASIC, cooling, monitoring.
**Previous report:** `reports/competitor-gap-EMCD-2026-06-19.md` (June, no DataForSEO, based on WebSearch/WebFetch).
**Related:** `reports/sub/competitor-gap-ePIC-content-2026-09-25.md`. Findings that overlap with it are referenced, not repeated.

---

## 0. Data sources and status

| Source | Endpoint / params | Status | Snapshot |
|---|---|---|---|
| DataForSEO Labs | `domain_rank_overview` emcd.io, US 2840/en | OK | inline (numbers in §1.1) |
| DataForSEO Labs | `ranked_keywords` emcd.io, US/en, limit 1000, filter `like` %firmware% / %min% / %asic% / %cool% / %monitor% / %hash% / %antminer% / %whatsminer% | OK, total_count **358** | `data/dfs-ranked-keywords-emcd.io-us-2026-09-25.json` |
| DataForSEO Labs | `ranked_keywords` emcd.io, US/en, filter2 %vnish% / %braiins% / %luxos% / %overclock% / %tun% / %immersion% / %efficien% / %s21% | OK, total_count **3** (2 GPU, 1 "miner efficiency") | extract in `data/dfs-serp-firmware-probe-emcd-2026-09-25.json` |
| DataForSEO Labs | `regex` filter operator | **40501 Invalid Field**, replaced with `like` chains | — |
| DataForSEO Labs | `domain_intersection` emcd.io ∩ bixbit.io, US/en, `intersections=true` | OK, **14 shared keywords** | `data/dfs-domain-intersection-emcd.io-vs-bixbit.io-2026-09-25.json` |
| DataForSEO Labs | Russia (2643) | **Not supported by Labs** (40501 on location_code; 2643 is missing from `locations_and_languages`) | — |
| DataForSEO Labs | Kazakhstan 2398/ru: `domain_rank_overview` + `ranked_keywords` for both domains | OK: EMCD 51 kw, BiXBiT 6 kw | `data/dfs-ranked-keywords-emcd.io-kz-ru-2026-09-25.json`; BiXBiT KZ in the probe file |
| DataForSEO SERP | `organic/live/regular` "best custom asic firmware" | **2 × 40101 Internal SE Server Error** | — |
| DataForSEO SERP | `organic/live/advanced` "best custom asic firmware" | **40106 partial**, page 1 only | `data/dfs-serp-firmware-probe-emcd-2026-09-25.json` |
| DataForSEO SERP | `organic/live/advanced` "vnish vs braiins os", depth 20 | OK | same file |
| DataForSEO SERP | `organic/live/advanced` "прошивка для асиков", KZ/ru | OK, page 1 only | same file |
| BiXBiT US/en | ranked_keywords (pulled earlier) | 162 kw | `data/dfs-ranked-keywords-bixbit.io-2026-09-25.json` |
| GSC / GA4 | — | not checked this run | — |
| keyword_overview | — | not pulled. Volumes for keywords outside Labs (e.g. "прошивка для асиков") are **n/d** | — |

Volumes are Google Ads monthly averages from Labs. Firmware long-tail sits at the 10/mo floor, so volumes don't rank the tail against itself.

---

## 1. Where EMCD ranks and BiXBiT does not

### 1.1 Domain scale

| Metric (Labs) | bixbit.io US/en | emcd.io US/en | bixbit.io KZ/ru | emcd.io KZ/ru |
|---|---|---|---|---|
| Ranked keywords | 162 | **955** | 6 | **51** |
| ETV / mo | 115 | **266.8** | 2.4 | **36.7** |
| pos 1 | 2 | 2 | 0 | 0 |
| pos 2–3 | 5 | 23 | 0 | 1 |
| pos 4–10 | 39 | 124 | 0 | 6 |
| pos 11–20 | — | 188 | 3 | 16 |
| Movement | — | new 417 / up 237 / down 262 / lost 251 | new 5 | new 25 / lost 12 |

**Main finding: EMCD has almost no footprint in BiXBiT's priority clusters.** Of EMCD's 358 mining-related US keywords:
- **Firmware:** 2 keywords, both outside the top 30. `/fw/` ranks #34 for "antminer firmware" and #36 for "bitmain firmware".
- **Cooling / immersion / hydro:** 0.
- **Monitoring / fleet management:** 0.
- **Whatsminer / Vnish / Braiins / LuxOS / autotuning / overclocking of ASICs:** 0.
- Its volume comes from GPU mining (`/the-best-gpus-for-mining/` 69 kw, `/best-nvidia-amd-gpu-settings-for-mining/` 41 kw), "mining on a laptop" (44 kw), altcoins, and three ASIC articles: `asic-miners-profitability-and-roi` (31 kw), `mining-with-antminer-s9-asic-is-it-still-profitable` (25 kw) and `mining-pool-how-it-works` (30 kw).

**June claim check.** June said "best custom asic firmware vnish vs braiins os vs luxos" was #1. That is not confirmed now:
- The URL `/articles/mining/best-custom-asic-firmware-vnish-vs-braiins-os-vs-luxos/` does not appear in Labs for US/en at any position up to 100.
- It is not on page 1 for "best custom asic firmware". Page 1 is braiins.com, reddit, hashrateindex, hiveon, youtube, bitcointalk, nicehash, d-central and hackernoon. Only page 1 came back (40106).
- It is not in the top 20 for "vnish vs braiins os". That SERP is reddit, d-central ×3, braiins, vnish.us, vni.sh ×2, linkedin, hashrateindex, mineshop, voskcointalk, vnish-firmware.com and solarayeffect.
- The June figure came from WebSearch rather than Google US data. It was either wrong, or a different locale, or the article has since dropped. BiXBiT is not in either SERP.

### 1.2 Gap table (EMCD top 20, BiXBiT not ranking or lower, relevant to the clusters)

"Compete" means building a BiXBiT page for the ranking. "Get mentioned" means getting BiXBiT added to EMCD's article (outreach) instead. "Skip" means off-scope for the ICP.

| Keyword | Vol | EMCD pos + URL | BiXBiT pos | Cluster | Prio | Compete / get mentioned |
|---|---|---|---|---|---|---|
| asic miners profitability | 590 | 14 — `/articles/mining/asic-miners-profitability-and-roi/` | — | Firmware → efficiency / TCO | **P1** | **Compete, reframed.** BiXBiT cannot promise profitability (CLAUDE.md §4). Target it with a "cost per TH / J/TH / break-even inputs" explainer and calculator where the operator enters their own $/kWh, J/TH and dev fee. No revenue forecasts |
| asic miner profit | 590 | 19 — same | — | same | P1 | same page (one URL for the whole group) |
| asic miners profit | 480 | 14 — same | — | same | P1 | same |
| asic miner profitability | 480 | 16 — same | — | same | P1 | same |
| crypto miner profitability | 260 | 17 — same | — | same | P2 | same (broader, GPU-mixed intent) |
| miners profitability | 260 | 20 — same | — | same | P2 | same |
| asic profitability / asic profit | 170 / 170 | 16 / 20 — same | — | same | P2 | same |
| asic crypto mining | 590 | 18 — same | 36 (`/en/blog/post/asic-evolution-…`) | ASIC (top of funnel) | P2 | **Compete.** Refresh the existing asic-evolution post, which also ranks for "asic miners" (4400, BiXBiT 20) |
| mine with asic | 110 | 20 — same | 41 (asic-evolution) | ASIC | P3 | compete via the same refresh |
| antminer s9 | 590 | 16 — `/articles/mining/mining-with-antminer-s9-asic-is-it-still-profitable/` | — | Antminer firmware (legacy) | P3 | **Compete only if BiXBiT supports S9** `[VERIFY: S9/S9k support on the current firmware]`. A 2022 operativa.ru article says BiXBiT had S9k firmware `[VERIFY: still current]`. Legacy hardware, low ICP fit (operators with 100+ units rarely run S9) |
| bitmain antminer s9 / s9 antminer profit | 110 / 110 | 13 / 13 — same | — | same | P3 | same |
| setup antminer s9 / antminer s9 setup / s9 antminer setup / set up antminer s9 | 30 each | 3 / 4 / 4 / 4 — same | — | Antminer firmware → install | P3 | If S9 is supported: add an S9 section to `antminer-firmware-install`, not a separate page |
| antminer s9 configuration | 30 | 5 — same | — | same | P3 | same |
| power consumption antminer s9 | 20 | 14 — same | — | Efficiency | P3 | skip (stock-spec query) |
| what is a antminer | 70 | 14 — same | — | Antminer firmware hub | P3 | cover in a hub FAQ ("What is an Antminer?"), not a page |
| mining pool | 1300 | 17 — `/articles/mining/mining-pool-how-it-works-…` | — | out of scope (pool) | — | **Skip.** EMCD's core product. BiXBiT doesn't run a pool |
| what is pool mining + 25 pool variants | 20–1300 | 7–30 — same | — | out of scope | — | Skip |
| GPU / laptop / altcoin / games (≈230 kw) | — | 2–30 | — | out of scope | — | Skip. Not the B2B ICP |

**Near-gaps (EMCD outside the top 20, but worth taking before they do):**

| Keyword | Vol | EMCD | BiXBiT | KD | Prio | Action |
|---|---|---|---|---|---|---|
| **bitmain firmware** | **140** | 36 `/fw/` | 45 `/en/firmwares` | 12 | **P1** | **Compete.** It is 2.8× the volume of "antminer firmware" (50). Add "Bitmain" as a synonym to the title/H1/intro of `/en/firmwares/antminer` and point "bitmain firmware" to that page instead of `/en/firmwares` (fixes the current cannibalization). See `content/page-optimize/firmwares.md` |
| miner efficiency | 50 | 37 (profitability article) | — | **6** | **P1** | **Compete.** Low KD and an exact match for the ICP pain (J/TH). Primary keyword for the efficiency spoke (§3, row 2) |
| antminer firmware | 50 | 34 `/fw/` | 15 | 6 | P1 (defend) | BiXBiT is ahead. Held by `/en/firmwares/antminer` |

### 1.3 EMCD's firmware content: facts to verify

Nothing below was checked against EMCD's live pages in this run. The June report and the SERP snippets are the only sources.

- EMCD distributes firmware under `/fw/` in partnership with Vnish `[VERIFY: partnership terms and whether /fw/ is Vnish-built]`.
- `/fw/` model list is S19 / S17 / S9 / L3+ (from June) `[VERIFY: current model list]`.
- The June comparison article gives dev fees of Braiins 2–2.5%, Vnish 2–2.8% and LuxOS 2.8% `[VERIFY each against vendor pages, with date]`.
- The d-central SERP snippet (2026-08-20) says "VNish charges a 2–2.8% dev fee" `[VERIFY]`.
- vni.sh says "flat dev fee" and "Braiins … can reach a 0% pool fee" `[VERIFY]`.
- BiXBiT's own published dev fee (2026-09-16 baseline) is 2.8% standard and 2% on M2x `[VERIFY: current]`. It is in the same range as Vnish, so **no "lowest fee" or "no dev fee" claim is possible**. Same constraint as the ePIC report, §3 row 1.

### 1.4 CIS: Kazakhstan / ru

| Keyword | Vol (KZ) | EMCD pos + URL | BiXBiT pos | Cluster | Prio | Compete / get mentioned |
|---|---|---|---|---|---|---|
| асики | 880 | 11 — `/ru/articles/majning/asiki-dlya-majninga/` | — | ASIC → firmware (ru) | **P1** | **Compete.** Build a /ru ASIC hub with links down to the /ru firmware pages `[VERIFY: /ru firmware pages exist and are indexable]` |
| майнинг ферма / майнинговые фермы | 590 / 590 | 25 / 31 — `/ru/articles/majning/chto-takoe-majning-ferma/` | — | Cooling / containers (ru) | **P1** | **Compete.** BiXBiT sells the farm infrastructure (containers, hydro, immersion). A commercial "farm build" page fits better than EMCD's definition article |
| майнинговые фермы это | 90 | 18 — same | — | same | P2 | same page, FAQ block |
| майнеры это / майнинг это | 720 / 720 | 15 — basics articles | — | out of scope (definitions) | P3 | skip or glossary |
| как удалить майнер | 320 | 10 — malware article | — | out of scope (malware) | — | Skip |
| kryptex / криптекс | 140 / 170 | 3 / 8 | — | out of scope (GPU app) | — | Skip |
| прошивка для асиков | n/d | not on page 1 | own pages not on page 1; **operativa.ru #3 mentions BiXBiT** ("Кастомная прошивка асика s9k доступна на сайте BiXBiT", 2022) | Firmware (ru) | **P1** | **Compete.** Page 1 is forums from 2017–2022, YouTube and an Avito listing (PitBit service). Weak SERP, no strong commercial page. Pull the volume with keyword_overview on the next run |

BiXBiT's 6 KZ/ru keywords are all off-topic /ru/blog posts: smart home stoves (11, 15), supercomputers (16, 29, 44) and Jack Dorsey (23). **BiXBiT's /ru locale has no firmware, cooling or monitoring visibility in KZ.** Russia itself is not in Labs. Use the SERP API (location 2643) for spot checks on the next run.

---

## 2. Where BiXBiT is ahead

### 2.1 Shared keywords (intersection, 14 kw): BiXBiT ahead on 9

| Keyword | Vol | BiXBiT pos | EMCD pos | BiXBiT URL |
|---|---|---|---|---|
| antminer firmware | 50 | **15** | 34 | /en/firmwares/antminer |
| etc miner | 90 | **17** | 40 | /en/blog/post/how-to-start-mining-ethereum-classic |
| what is asic miner | 20 | **16** | 49 | /en/blog/post/asic-evolution-… |
| what is an asic miner | 140 | **21** | 26 | same |
| what is asic mining | 140 | **23** | 28 | same |
| what is asic miners | 20 | **24** | 46 | same |
| asics miners | 40 | **28** | 33 | same |
| most profitable miner | 50 | **29** | 31 | /en/blog/post/whats-the-most-profitable-miner-in-2025 |
| mining asic | 50 | **35** | 44 | /en/blog/post/asic-evolution-… |

EMCD is ahead on 5: asic crypto mining (18 vs 36), bitmain firmware (36 vs 45), mine with asic (20 vs 41), mine etc (8 vs 44) and antminer uses (17 vs 21).

### 2.2 BiXBiT-only territory (EMCD ranks for none of these)

| Keyword | Vol | BiXBiT pos | URL | Cluster |
|---|---|---|---|---|
| whatsminer firmware | 20 | 3 | /en/firmwares/whatsminer-series-m3x | Firmware |
| whatsminer tools / tool | 50 / 50 | 8 / 16 | /en/firmwares/whatsminer-series-m3x, /en/firmwares | Firmware |
| asic monitor | 70 | 7 | /en/ams | Monitoring |
| mineral oil for immersion cooling | 30 | 1 | /en/blog/post/immersion-liquid-… | Cooling |
| antminer in mineral oil / antminer mineral oil / mineral oil antminer | 50 each | 2 | same | Cooling |
| mineral oil immersion cooling | 20 | 5 | same | Cooling |
| what is novec liquid | 20 | 9 | /en/blog/post/novec-and-coolant-… | Cooling |
| how does immersion cooling work / what is immersion cooling | 30 / 90 | 12 / 19 | /en/blog/post/how-does-immersion-cooling-work | Cooling |
| immersion computer cooling | 390 | 15 | same | Cooling |
| hydro rack / whatsminer hydro | 40 / 10 | 16 / 18 | /en/products/rack-hydro, /container-hydro | Cooling (hydro) |
| mining rack / rack mining / mining container price | 40 / 40 / 40 | 6 / 9 / 9 | /en/products/rack, /container | Infra |
| crypto mining shipping container | 170 | 17 | /en/products/container | Infra |
| antminer s19 pro profitability / s19 profitability | 140 / 110 | 6 / 10 | /en/blog/post/antminer-19-series-… | ASIC models |
| antminer l7 | 210 | 8 | /en/blog/post/bitmain-antminer-l7-review-… | ASIC models |
| soundproof antminer / why is crypto mining noisy | 50 / 90 | 10 / 7 | /en/blog/post/killers-of-the-mining-equipment-… | Ops |

**Summary:** in US/en BiXBiT leads EMCD in every priority cluster: firmware (Antminer and Whatsminer), cooling, monitoring and infrastructure. EMCD leads on generic ASIC-profitability and legacy S9 traffic, and in CIS/ru.

---

## 3. Gap-closing plan

| # | Prio | Page (bixbit.io) | Type / intent | Hub | Target queries (vol) | What it closes |
|---|---|---|---|---|---|---|
| 1 | **P1** | `/en/firmwares/antminer`: on-page update | Product / transactional | antminer-firmware | bitmain firmware (140, BiXBiT 45 → target top 10), antminer firmware (50, defend 15) | Add the "Bitmain" synonym to title/H1/first paragraph. Internal links using "Bitmain firmware" anchors from blog posts about S19 / L7. Fix the `/en/firmwares` vs `/antminer` split. Extends `content/page-optimize/firmwares.md` |
| 2 | **P1** | `/en/blog/asic-miner-efficiency-j-th` (new spoke) | Explainer + input calculator / informational → commercial investigation | antminer-firmware (+ link from whatsminer-firmware) | miner efficiency (50, KD 6), asic miner(s) profitability/profit (590 + 590 + 480 + 480), asic profitability (170) | Takes EMCD's profitability traffic with a TCO angle: J/TH, $/kWh, uptime, dev fee, and what firmware tuning changes. **No revenue promises or ROI claims.** The calculator uses the operator's own inputs and carries a disclaimer. Every stock/tuned J/TH figure is `[VERIFY: BiXBiT test data, model, ambient °C, PSU]`. Link to `antminer-undervolting`, `antminer-autotuning` and the dev-fee spoke from the ePIC report §3 row 1 |
| 3 | **P1** | `/ru/` ASIC firmware hub + a "прошивка для асиков" landing page | Commercial / ru | whatsminer-firmware + antminer-firmware (ru) | асики (880, EMCD 11), прошивка для асиков (n/d, weak SERP) | Covers the CIS priority geography. First confirm the /ru firmware pages exist, are indexable and have correct hreflang `[VERIFY]`. Hand off to `international-seo` |
| 4 | **P1** | `/ru/` mining farm build page (containers + hydro + immersion) | Commercial / ru | immersion-cooling-mining (ru) | майнинг ферма (590), майнинговые фермы (590), майнинговые фермы это (90) | Commercial answer to EMCD's definition article. FAQ block covers the "это" query |
| 5 | P2 | Refresh `/en/blog/post/asic-evolution-what-will-happen-to-computing-devices-for-mining` | Informational | ASIC → firmware hubs | asic miners (4400, BiXBiT 20), asic crypto mining (590, 36), what is an asic miner (140, 21), mine with asic (110, 41) | Already ranks 16–41. Update the date, add a definition passage (40–60 words, citable), a "how firmware changes ASIC efficiency" section and links to both firmware hubs |
| 6 | P2 | Outreach: EMCD `/articles/mining/best-custom-asic-firmware-vnish-vs-braiins-os-vs-luxos/` | **Get mentioned** | — | none measurable (not in Labs, not in the SERPs checked) | Low SEO value now. It is still a crawlable comparison that LLMs can cite (see `geo-ai`). **Odds are low: EMCD partners with Vnish** `[VERIFY]`. Offer a Whatsminer section, since June noted EMCD has no Whatsminer firmware coverage. Higher-value mention targets for the same effort are d-central (3 URLs in the "vnish vs braiins os" top 10) and hashrateindex "Top 5 Firmware 2026" (#3 for "best custom asic firmware"). Hand off to `offpage-seo` |
| 7 | P2 | Outreach: operativa.ru (2022 article naming BiXBiT, #3 for "прошивка для асиков" KZ) | **Get mentioned / refresh** | — | прошивка для асиков | Ask them to update the model list and add a link to the current /ru firmware page `[VERIFY: current S9k support]` |
| 8 | P3 | S9 section inside `content/briefs/antminer-firmware-install.md` | How-to | antminer-firmware | setup antminer s9 (30 ×4), antminer s9 configuration (30) | Only if S9/S9k is supported `[VERIFY]`. Otherwise skip, because EMCD's S9 traffic is legacy and off-ICP |
| — | Skip | — | — | — | mining pool (1300) and variants, GPU/laptop, altcoins, malware | Out of BiXBiT's product scope. Not a gap to close |

**Internal linking additions** (for `content/internal-linking.md`):
- asic-evolution post → `/en/firmwares/antminer` (anchor "Bitmain Antminer firmware") and `/en/firmwares/whatsminer-*`.
- New efficiency spoke ↔ `antminer-undervolting`, `antminer-autotuning`, `whatsminer-undervolting` and the dev-fee spoke.
- Antminer S19 / L7 review posts → `/en/firmwares/antminer` (these posts rank 6–10 and are the strongest internal-link donors).

**Order of work:** first #1 (on-page, one day), then #2 (new spoke, needs engineering `[VERIFY]` data), then #3 and #4 (ru, after checking with international-seo), then #5. #6 and #7 go to offpage-seo.

**Next pull:** `keyword_overview` KZ/ru for "прошивка для асиков", "прошивка antminer", "прошивка whatsminer", "иммерсионное охлаждение"; SERP Russia (2643) for the same queries; retry the "best custom asic firmware" SERP to depth 20.
