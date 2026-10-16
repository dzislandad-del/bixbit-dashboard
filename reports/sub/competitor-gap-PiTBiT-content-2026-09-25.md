# Content / Keyword Gap: BiXBiT vs PiTBiT (pitbitecosystem.com + pitbit.online), 2026-09-25

**Scope:** US/en and Kazakhstan/ru (the CIS proxy). Clusters: firmware and monitoring.
**Previous report:** `reports/competitor-gap-PiTBiT-2026-06-19.md` (June, no DataForSEO, based on WebFetch).
**Related:** `reports/sub/competitor-gap-ePIC-content-2026-09-25.md` and `reports/sub/competitor-gap-EMCD-content-2026-09-25.md`. This report links to their findings and does not restate them.
**Snapshot:** `data/dfs-pitbit-gap-2026-09-25.json`

---

## 0. Data sources and status

| Source | Endpoint / params | Status | Result |
|---|---|---|---|
| DataForSEO Labs | `domain_rank_overview` pitbitecosystem.com, US 2840/en | OK | **1 keyword**, ETV 0.46 |
| DataForSEO Labs | `domain_rank_overview` pitbit.online, US 2840/en | OK | **1 keyword**, ETV 0.03 |
| DataForSEO Labs | `domain_rank_overview` for both domains, KZ 2398/ru | OK, empty | **0 keywords** |
| DataForSEO Labs | `ranked_keywords` for both domains, US, `historical_serp_mode=all` | OK | 2 + 2 keywords, all outside the top 20 (see §1.1) |
| DataForSEO Labs | `ranked_keywords` for both domains, KZ/ru and Ukraine 2804/ru | OK, empty | **0 keywords** |
| DataForSEO Labs | `domain_intersection` pitbitecosystem.com ∩ bixbit.io (US, KZ), pitbit.online ∩ bixbit.io (US) | OK, empty | **0 shared keywords** |
| DataForSEO Labs / SERP | Russia 2643, Belarus 2112 | **40501 Invalid Field: location_code** in both Labs and SERP | PiTBiT's home market (RU) **can't be measured** with this toolset |
| Keywords Data | `google_ads/search_volume` KZ/ru, 30 CIS queries (3 calls of up to 10 each) | OK | Most are 10/mo or n/d (see §1.3) |
| Keywords Data | `google_ads/search_volume` US/en, brand queries | OK | see §1.4 |
| SERP | `organic/live/advanced` KZ/ru depth 20: "прошивка antminer", "мониторинг асиков", "прошивка s19", "прошивка whatsminer" | OK (all 20000; "прошивка s19" returned 11 results) | §1.2, §2 |
| SERP | "pitbit" US/en depth 10 | OK | §1.4 |
| BiXBiT US/en and KZ | reused from `data/dfs-ranked-keywords-bixbit.io-2026-09-25.json` (162 kw) and `data/dfs-serp-firmware-probe-emcd-2026-09-25.json` (6 KZ kw) | reused, not re-pulled | — |
| GSC / GA4 | — | not checked this run | — |
| WebFetch / site crawl of PiTBiT | — | not used this run | PiTBiT product facts come from the June report and are all `[VERIFY]` |

**Methodology note.** Labs coverage in KZ/ru is too thin for this niche. Labs lists 6 off-topic KZ keywords for BiXBiT. Live SERP puts `bixbit.io/ru/...` at **#1 for "прошивка whatsminer"** and **#3 for "мониторинг асиков"**. Both are real rankings that Labs doesn't record, because the queries sit at 10/mo. For the CIS, treat the live SERP checks as the actual signal. "0 in Labs" means PiTBiT has no measurable Google footprint on tracked keywords. It does not mean PiTBiT has zero traffic.

---

## 1. Where PiTBiT ranks and BiXBiT does not

### 1.1 Domain scale (Labs)

| Metric | bixbit.io US/en | pitbitecosystem.com US/en | pitbit.online US/en | bixbit.io KZ/ru | PiTBiT (both) KZ/ru |
|---|---|---|---|---|---|
| Ranked keywords | **162** | 1 (2 in history) | 1 (2 in history) | 6 | **0** |
| ETV / mo | **115** | 0.46 | 0.03 | 2.4 | 0 |
| Best position | 1 | 29 | 46 | 11 | — |
| Shared with BiXBiT | — | 0 | 0 | — | 0 |

**PiTBiT's full Labs keyword list (US):**

| Keyword | Vol (US) | PiTBiT pos + URL | BiXBiT | In scope? |
|---|---|---|---|---|
| bitmain warranty check | 110 | 29, `pitbitecosystem.com/en/warranty/` | not ranking. BiXBiT ranks #26 for "whatsminer warranty check" (20) via `/en/documentation/error-codes-for-whatsminer-asic/...` | Service/ops, adjacent. Outside the top 20 |
| repairbit | 140 | 97, `/` (lost) | — | No (unrelated brand) |
| piitb | 30 | 46, `pitbit.online/` | — | No (typo/noise) |
| repairbit | 140 | 89, `pitbit.online/` (lost) | — | No |

**Conclusion: in US/en and KZ/ru, PiTBiT has zero keywords in the top 20 in the firmware or monitoring clusters.** No keyword gap exists at the domain level. PiTBiT isn't building search visibility on its own domains. It reaches people through YouTube, marketplaces and forums (§1.2).

**What changed since June.** June counted ~7 indexed pages and inferred that PiTBiT's model pages compete for "[model] firmware" queries. Labs shows none of those pages ranking in US or KZ. June's point that PiTBiT has better *page structure* (model in the URL/H1, mode tables) still holds as a UX/format benchmark. It isn't producing rankings.

### 1.2 Where PiTBiT does show up in CIS SERPs (other channels)

| Query (KZ/ru) | Vol KZ | PiTBiT | BiXBiT | Top-20 composition | Gap type |
|---|---|---|---|---|---|
| прошивка s19 | 10 | **#1: YouTube "Обзор S19 I на прошивке от PITBIT"** (PITBIT ECOSYSTEM channel, 2025) | not in results | YouTube ×5, reddit ×2, minecool.ru (Vnish tests, 2022), miningclub.info (2021). No commercial firmware page | **Channel gap (video) + page gap (ru S19 model page)** |
| прошивка для асиков | n/d | #6: m.avito.ru PitBit S19K Pro service listing (from the EMCD run, page 1 only) | own pages not on page 1. operativa.ru #3 mentions BiXBiT (2022) | forums 2017–2022, YouTube, Avito | Marketplace listing + page gap. See EMCD report §1.4 |
| прошивка antminer | 10 | not in top 20 | not in top 20 | YouTube ×9 (MSKMINER, 7Miners, VNISH OFFICIAL), reddit ×4 (ru auto-translation), bazabtc ×2 (download pages), forum.bits.media ×2. **Zero vendor landing pages** | **Open SERP: neither ranks.** Largest ru opportunity (§3 #1) |
| мониторинг асиков | 10 | not in top 20 | **#3 `/ru/ams`** | monito.run #1, moonone.ru #2/#5, tcs-mining.ru comparison #4, aximine #6, minermonitor.ru #7, VNISH video pack | BiXBiT leads PiTBiT (§2) |
| прошивка whatsminer | 10 | not in top 20 (PiTBiT has no Whatsminer firmware `[VERIFY]`) | **#1, #6, #12** + video + bits.media thread #11 | trendtonext, whatsminer.com, bazabtc, WMOC via chim-mining | BiXBiT leads PiTBiT (§2) |

**PiTBiT's real acquisition channel is YouTube.** The @pitbit003 channel shows **39.7K+ followers** in the SERP snippet. It holds #1 for "прошивка s19" and #5 on the brand SERP. BiXBiT Official also appears in Whatsminer SERPs (the video pack plus #13), but not in any Antminer SERP checked.

### 1.3 CIS volume check (KZ/ru, Google Ads)

| Query | Vol / mo KZ | Query | Vol / mo KZ |
|---|---|---|---|
| прошивка для асиков | n/d | мониторинг асиков | 10 |
| прошивка асика | 10 | асик мониторинг | n/d |
| прошивка antminer | 10 | мониторинг майнинг фермы | n/d |
| прошивка антмайнер | n/d | разгон асика / разгон antminer | n/d / n/d |
| прошивка s19 | 10 | vnish | 110 |
| прошивка s19j pro | 10 | вниш прошивка | 10 |
| прошивка s19 xp / прошивка s21 | n/d / n/d | braiins os | 10 |
| прошивка whatsminer | 10 | hiveos asic | 10 |
| прошивка l7 / прошивка l9 | 10 / n/d | прошивка без девфи | n/d |

In KZ, nearly every CIS firmware query sits at the 10/mo floor or below the reporting threshold. **Vnish (110) is the only CIS firmware brand with measurable demand.** Russia, where most of the demand should be, can't be measured (40501). Rank the ru work by SERP weakness and commercial fit, not by volume.

### 1.4 PiTBiT branded demand (reported separately)

| Brand query | US/en | KZ/ru | Note |
|---|---|---|---|
| pitbit | 70 | 20 | **US volume is polluted.** The US SERP is Pibit.AI (#1, #2, #4, #8), Pippit AI and pitbit.at (biotech). PiTBiT's properties only take #3 (pitbit.online), #5 (YouTube) and #7 (pitbit.systems client cabinet). The share with PiTBiT intent is unknown |
| питбит / pitbit online / pitbit firmware / pitbit ecosystem | n/d | n/d | Below threshold |
| **bixbit** | **140** | 10 | BiXBiT is #1 in the US |
| **биксбит** | — | **20** | — |
| bixbit firmware | 10 | — | — |

In KZ, branded demand is roughly **1.5× in BiXBiT's favor** (bixbit 10 + биксбит 20 vs pitbit 20). The KZ "pitbit" SERP wasn't pulled. PiTBiT's branded demand is too small to justify a dedicated "PiTBiT alternative" page. Cover it as a row in the ru comparison page (§3 #4).

---

## 2. Where BiXBiT wins

| Area | Evidence (DataForSEO, 2026-09-25) | PiTBiT |
|---|---|---|
| Overall US visibility | 162 kw, ETV 115, 46 in the top 10 | 2 + 2 kw, none in the top 20 |
| Whatsminer firmware, en | whatsminer firmware #3, whatsminer tools #8 (`/en/firmwares/whatsminer-series-m3x`) | none. Whatsminer isn't supported `[VERIFY]` |
| **Whatsminer firmware, ru** | "прошивка whatsminer" KZ: **#1** `/ru/documentation/rukovodstvo-polzovatelia-whatsminer-asic/4-obnovlenie-proshivki-mainera`, **#6** `/ru/firmwares`, **#12** `/ru/blog/post/anons-proshivki-dlya-whatsminer`, bits.media BiXBiT thread #11, BiXBiT Official video in the pack and #13. Related searches include **"BiXBiT прошивка"** and **"BiXBiT Прошивка отзывы"** | not in top 20 |
| **ASIC monitoring, ru** | "мониторинг асиков" KZ: **#3** `/ru/ams` | pitbit.online not in the top 20 |
| ASIC monitoring, en | asic monitor #7 `/en/ams` | none |
| Cooling / infra / PDU | full clusters, see the EMCD report §2 | no product `[VERIFY]` |
| Brand demand | bixbit 140 US, 30 KZ combined | pitbit 70 US (polluted), 20 KZ |

**Gap-closing risk.** The #1 for "прошивка whatsminer" goes to a **documentation page** (an upgrade guide), not the commercial `/ru/firmwares` page (#6). Intent matches (instructional). The commercial page needs to be linked from the doc page to convert.

---

## 3. Clusters and pages to close the gaps (ru focus)

No **/ru clusters** exist yet in `content/clusters/`. All five are en. The list below is the ru layer. Every /ru page first needs a check with `international-seo` that it exists, is indexable and has correct hreflang ru↔en `[VERIFY]`.

| # | Prio | Page (bixbit.io) | Type / intent | Hub (cluster) | Target queries (KZ vol) | What it closes / why |
|---|---|---|---|---|---|---|
| 1 | **P1** | `/ru/firmwares/antminer`: create or strengthen as the ru Antminer hub | Commercial / transactional | antminer-firmware (ru layer) | прошивка antminer (10), прошивка асика (10), прошивка для асиков (n/d) | **Open SERP:** 20/20 results are YouTube, forums, reddit auto-translations and download mirrors. No vendor page. Neither BiXBiT nor PiTBiT ranks. Localize from `content/briefs/antminer-firmware-pillar.md`. Add a modes table (TH/s, W, J/TH per mode). Every value is `[VERIFY: engineering test data per model]`. Title/H1: "Прошивка для Antminer (S19, S21, T21…)" `[VERIFY: supported model list]` |
| 2 | **P1** | `/ru/firmwares/antminer-s19` (+ `-s19j-pro`, `-s19-xp`, `-s21` as the next spokes) | Model product page / transactional | antminer-firmware (ru) | прошивка s19 (10), прошивка s19j pro (10), прошивка s19 xp / s21 (n/d) | PiTBiT's only #1 is a video on this query. The rest of the SERP is 2021–2023 forum threads. Localize `content/briefs/antminer-s19-firmware.md` / `antminer-s21-firmware.md`. Embed a ru S19 video (VideoObject). Use the model in the URL and H1, the format June credited to PiTBiT |
| 3 | **P1** | Video: BiXBiT Official ru videos for Antminer S19 / S21 / T21 (install, modes, before/after on a wattmeter) | Video / how-to | antminer-firmware (ru) | прошивка s19, прошивка antminer | YouTube holds most of the top 20 in every Antminer SERP checked, and it's PiTBiT's main channel (39.7K followers). BiXBiT's Whatsminer videos already rank, so the format works for BiXBiT. Every number shown on screen is `[VERIFY]` |
| 4 | **P1** | `/ru/blog/programmy-dlya-monitoringa-asikov` (comparison: BiXBiT AMS, Moonone, Monito, MagicMinerMonitor, Hive OS ASIC Hub, Vnish monitoring, PITBIT ONLINE) | Comparison / commercial investigation | mining-fleet-monitoring (ru layer) | мониторинг асиков (10). Related searches: "программа мониторинга асиков", "удаленный мониторинг асиков", "мониторинг асиков с телефона" | tcs-mining.ru's comparison at #4 shows Google rewards this format. Defends `/ru/ams` #3 and pushes for #1–2 against monito.run and moonone.ru. Competitor features are `[VERIFY]` at publication. No negative claims about PiTBiT without a source |
| 5 | P2 | `/ru/ams`: on-page | Product / transactional | mining-fleet-monitoring (ru) | мониторинг асиков, удаленный мониторинг асиков, мониторинг асиков с телефона | Add a "мобильное приложение / Telegram-уведомления" section if the feature exists `[VERIFY]`, and FAQ. This maps to two related-search phrasings. The current title "скачать программу управления майнингом AMS" misses "мониторинг асиков". Test "Мониторинг асиков BiXBiT AMS — …" |
| 6 | P2 | `/ru/otzyvy` or a case block on `/ru/firmwares` | Trust / navigational-commercial | antminer + whatsminer firmware (ru) | "BiXBiT прошивка отзывы" (Google related search, n/d) | Google already suggests this query. Without an owned page, the answer comes from forums. Use real operator cases with J/TH / uptime figures. Each figure is `[VERIFY]` and needs client consent |
| 7 | P2 | `/ru/documentation/.../4-obnovlenie-proshivki-mainera`: add a CTA and links to `/ru/firmwares/whatsminer-*` | How-to → transactional | whatsminer-firmware (ru) | прошивка whatsminer (10, #1) | Converts the #1 position. Also link the Whatsminer model spokes (M30S / M21S / M31S / M20S all appear as related searches) |
| 8 | P2 | `/ru/firmwares/whatsminer-m30s` (+ m20s / m21s / m31s) | Model product page | whatsminer-firmware (ru) | Прошивка Whatsminer M30S / M21S / M31S / M20S (related searches, n/d) | Extends a cluster PiTBiT can't enter. Localize `content/briefs/whatsminer-m30s-firmware.md`. Models and modes are `[VERIFY]` |
| 9 | P3 | `/en/documentation/how-to-check-bitmain-whatsminer-warranty` (or a section in the existing whatsminer doc) | Support / informational | antminer-firmware (support) | bitmain warranty check (110 US, PiTBiT #29), whatsminer warranty check (20, BiXBiT #26) | PiTBiT's only in-niche US ranking. Low ICP fit but cheap: it's a doc page. Add a note on how custom firmware affects warranty `[VERIFY: legal/warranty position]` |
| — | Skip | Elphapex firmware pages | — | — | elphapex firmware / elphapex dg1 firmware: n/d US | No measurable demand, and BiXBiT support is unknown `[VERIFY]` |
| — | Link | ru dev-fee / "без девфи" explainer | — | — | прошивка без девфи (n/d) | Already planned in en (ePIC report, plan #1). Localize after the en version ships. chim-mining.ru and bits.media no-dev-fee threads rank for this in the Whatsminer SERP |

**Internal linking additions** (for `content/internal-linking.md`, ru layer):
- `/ru/documentation/...whatsminer.../4-obnovlenie-proshivki-mainera` → `/ru/firmwares` and `/ru/firmwares/whatsminer-*` (anchors "прошивка Whatsminer", "разгон Whatsminer").
- `/ru/firmwares` (hub) ↔ `/ru/firmwares/antminer` ↔ `/ru/firmwares/antminer-s19`, `-s21`.
- `/ru/blog/programmy-dlya-monitoringa-asikov` → `/ru/ams` (anchor "мониторинг асиков"). `/ru/ams` → the firmware hub ("прошивка + мониторинг в одном стеке").
- `/ru/blog/post/anons-proshivki-dlya-whatsminer` (#12) → `/ru/firmwares/whatsminer-*`.

**Off-page handoff (offpage-seo, not repeated here):** bits.media BiXBiT Dev thread refresh; the Avito/marketplace listing channel PiTBiT uses (evaluate a BiXBiT listing in KZ/RU). See also the operativa.ru outreach in the EMCD report, plan #7.

**Order of work:** #7 and #5 first (on-page, days). Then #1 and #2 (they need engineering `[VERIFY]` data). #3 runs in parallel with the video team. Then #4, then #6 and #8. #9 is filler.

---

## 4. PiTBiT facts (not re-verified this run, all from June WebFetch)

All items below are **unverified** and must not be published in comparison content without a fresh primary source:
- Dev fee **2.75%**, or a one-time license at $150–$300 per model `[VERIFY]`
- **28** supported Antminer models (S19–S21 lines + Hydro), plus Elphapex DG `[VERIFY]`
- **90,000+** devices, **6,000+** clients. The Labs SERP snippet of pitbitecosystem.com on 2026-09-25 repeats "6 000+ клиентов с 2019 года" and "Хешрейт +50%, доход +30%". These are self-reported marketing claims `[VERIFY]`
- No Whatsminer firmware, no cooling, no PDU `[VERIFY]`
- B2B tier from 20 PH/s (0.5%), 10% partner program `[VERIFY]`
- BiXBiT dev fee for comparison: 2.8% (2% for M2x), per project memory, 2026-09 baseline `[VERIFY before publishing]`

---

## 5. Next pull
- Russia can't be measured in DataForSEO (Labs and SERP both return 40501, same for Belarus). Use **GSC for /ru** (country filter RU/KZ) as the only real source of CIS demand for BiXBiT. GSC wasn't checked this run.
- SERP KZ/ru: "pitbit" (brand), "прошивка s21", "программа мониторинга асиков", "удаленный мониторинг асиков".
- YouTube search visibility for "прошивка s19 / s21 / antminer" (DataForSEO SERP YouTube endpoint), BiXBiT vs PITBIT channel.
