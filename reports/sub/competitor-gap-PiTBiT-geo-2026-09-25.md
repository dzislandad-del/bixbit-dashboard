# GEO / AI-Citation Gap: BiXBiT vs PiTBiT (pitbitecosystem.com, pitbit.online), 2026-09-25

**Question:** How often do LLMs name or cite PiTBiT, a CIS competitor in firmware and monitoring, compared with BiXBiT? Which sources feed PiTBiT, and what do LLMs get wrong about BiXBiT in Russian-language answers?
**Method: MEASURED.**
- 64 saved answers from the ePIC and EMCD runs were re-scanned at no cost.
- 7 new prompts were each run on 4 LLMs (28 live calls) through the DataForSEO AI Optimization API.
- 5 LLM Mentions calls were made.
- 4 source pages were checked with WebFetch.

This replaces the June Claude self-test in `reports/competitor-gap-PiTBiT-2026-06-19.md` §AI-visibility ("brand unknown").

---

## 0. Data sources and status

| Source | Status | Notes |
|---|---|---|
| Re-scan of saved answers (`data/geo-epic-2026-09-25/` 44 files, `data/geo-emcd-2026-09-25/` 24 condensed records) | OK, free | Scanned 64 LLM answers + 11 AIO with `grep -i pitbit`. Caveat: EMCD records are condensed (brand list + cited URLs), not full text |
| ChatGPT `chat_gpt/llm_responses/live` | OK, 7/7 | gpt-4.1-mini, web_search + force_web_search. RU prompts had no location; EN prompts used US |
| Perplexity `perplexity/llm_responses/live` | OK, 7/7 | sonar |
| Claude `claude/llm_responses/live` | OK, 7/7 | claude-sonnet-4-6, max_output_tokens 1500. p2, p4 and p6 were truncated near the limit |
| Gemini `gemini/llm_responses/live` | OK, 7/7 | gemini-3.5-flash, max 1000–1500 tokens, no location param. p2, p3, p5 and p6 were truncated |
| LLM Mentions `llm_mentions/search/live` | OK, 5 calls | `pitbitecosystem.com` and `pitbit.online` on google and chat_gpt (US/en only): **0 results in all 4 calls**. A keyword `pitbit` partial_match call returned 465 items, all unrelated (it matched "pit bit…"). That call was discarded as noise |
| WebFetch | OK, 4 pages | altcoinlog.com, top-mining.ru, cryptorussia.ru, ultramining.com |
| Google AIO | Not run | Budget. PiTBiT has 0 AIO answers in the LLM Mentions DB, so there was nothing to measure |
| curl | Not used | Denied in the earlier run, so it was not retried |

**Raw data:** `data/geo-pitbit-2026-09-25/`
- `p1.json`–`p7.json`: condensed per-engine records (task IDs, brands, cited URLs, verbatim anchors, attribution risks).
- `gemini-p2.raw.json`, `gemini-p6.raw.json`: full raw Gemini responses.
- `llm-mentions-pitbit.json`: task IDs and counts for the LLM Mentions calls.

**Limits:**
- Each prompt was run once per engine (n=1 per cell). LLM output varies between runs, so treat a 1-answer difference as noise.
- Truncated answers may have cut the last brands in a list.

---

## 1. Score (measured)

| Scope | PiTBiT named | pitbit* domain cited | BiXBiT named | bixbit.io cited |
|---|---|---|---|---|
| Saved ePIC + EMCD answers (64) | **1** (Claude e4, "PITBIT") | 1 (same answer, `/catalog/firmware/firmware-for-antminer-s21-hyd/`) | 19 | 18 |
| New non-branded prompts p1, p2, p4, p5, p7 (20) | **0** | 1 (Perplexity p1: 2 URLs cited, brand not in text) | **9** | 8 (+1 via `launch.bixbitusa.io`) |
| **All non-branded LLM answers (84)** | **1 / 84 (1%)** | **2 / 84** | **28 / 84 (33%)** | 26 / 84 |
| RU non-branded only (p1, p2, p4, p5 + r1, r2, e4-RU; 28) | 1 | 2 | 12 | 11 |
| Branded prompts p3 ("PiTBiT или Vnish") and p6 ("PiTBiT review") (8) | 8/8 (forced by the prompt) | 6/8 | **1/8** (Claude p6, as an alternative) | 0/8 |
| LLM Mentions DB, Google AIO + ChatGPT (US) | **0** answers | 0 | bixbit.io: 49 AIO queries (09-25 ePIC run) | — |

**Verdict: BiXBiT 28 vs PiTBiT 1 on non-branded AI answers (84 answers).**
- PiTBiT is effectively **invisible to LLMs unless the user types its name**.
- When the name is typed, the engines answer mostly from PiTBiT's own pages (13 own URLs in Perplexity p6), one sponsored article (ultramining.com) and YouTube.
- Claude p3 calls PiTBiT "относительно малоизвестная прошивка" ("a relatively little-known firmware").
- Perplexity p3 could not read `pitbitecosystem.com/catalog/firmware/` ("на найденной странице нет содержимого", i.e. "the page found has no content"). That points to a PiTBiT citability defect: a JS-rendered or blocked body.

**The June claim does not hold.** The June report said PiTBiT and BiXBiT are "equally weak". Measured today, BiXBiT is far ahead.
- **The risk is not PiTBiT outranking BiXBiT. It is PiTBiT's facts leaking into BiXBiT answers** (see §3).
- A second risk: on PiTBiT-branded queries BiXBiT is not offered as the alternative (1/8). Vnish, Braiins and LuxOS are.

---

## 2. Query × engine matrix (new prompts)

**Legend:**
- **P** = PiTBiT named; **p** = a pitbit domain cited
- **B** = BiXBiT named; **b** = bixbit.io cited
- `—` = neither

| # | Prompt | ChatGPT | Perplexity | Claude | Gemini | Other brands (union) | Key sources |
|---|---|---|---|---|---|---|---|
| p1 | (RU) Какая лучшая прошивка для Antminer S21? | **B b** (2019 S17 blog post) | p (not in text) | — | **B b** | VNISH, Braiins OS+, Asic Boost, Hashrate.farm, Hiveon, Awesome Miner, HashCore, NiceHash | vnish.* (15+ mirrors), braiins.com, minerfirmware.com, mineshop.eu, crazy-mining.org, pitbitecosystem.com |
| p2 | (RU) Прошивка для асиков с мониторингом фермы | **B** (launch.bixbitusa.io) | **B b** | **B b** | **B b** | Vnish, Braiins, Hive OS/ASIC Hub, MSKMINER, Awesome Miner, Jeensys, MinersMe, LuxOS, Foreman, Kryptex×BiXBiT AMS | bixbit.io/ru/ams, bixbit.io/ru/firmwares, pool.kryptex.com/ru, **altcoinlog.com**, coindaily.ru, hub.forklog.com, mskminer.com, trustpool.cc |
| p3 | (RU) PiTBiT или Vnish? *(branded)* | P | P p | P | P p | Vnish, Braiins OS+, LuxOS | vnish.* (13), pitbitecosystem.com, d-central.tech (5), YouTube, top-mining.ru, altcoinlog.com |
| p4 | (RU) Облачный мониторинг асиков | — | — | — | — | Moonone, Minerstat, Hive OS, Awesome Miner, Monito.run, Jeensys, AntminerTools, ASICLink, MinerWatchdog, Foreman, Headframe | headframe.io, moonone.ru, monito.run, tcs-mining.ru, hashrate.ru, bemining.ru, bankstoday.net, bitexpert.io |
| p5 | (RU) Dev fee прошивок Antminer, самая низкая | — | — | — | — | DCENT_OS 0%, ePIC 1.5%, NiceHash 1.4%, VNISH MOD 0.5%, DJAY OS, Money-Mining, MSKMINER, Pro-Miner, Awesome Miner | d-central.tech, vnish.*, asic.es, coindaily.ru, pro-miner.ru, millionminer.com, nicehash.com |
| p6 | (EN) PiTBiT firmware review *(branded)* | P p | P p (13 own URLs) | P p, **B** (saashub) | P p | Vnish, Braiins, LuxOS, DJAY OS | **ultramining.com** (sponsored), pitbitecosystem.com/en/reviews/, pitbit.online, **youtube.com/watch?v=a3YllTMvcJM**, t.me/s/PitBitPro, linkedin.com, saashub.com |
| p7 | (EN) Antminer firmware with built-in cloud fleet monitoring | **B b** | B b ("not clearly shown") | **B b** | — | Braiins Manager, LuxOS Commander, ePIC, VNISH, NiceHash ASIC Manager, Awesome Miner | d-central.tech, hashrateindex.com, braiins.com, docs.luxor.tech, epicblockchain.io, bixbit.io/en/firmwares(/antminer), launch.bixbitusa.io |

**By engine, non-branded new (5 prompts each), BiXBiT named:**
- ChatGPT **3/5**. It was 0/8 on firmware in the ePIC run; today it cites bixbit.io and launch.bixbitusa.io.
- Perplexity 2/5.
- Claude 2/5.
- Gemini 2/5.

**Verbatim anchors (quotes of 25 words or fewer):**
- **BiXBiT.** Perplexity p2: "Для удалённого мониторинга всей фермы: BiXBiT AMS или Kryptex × BiXBiT AMS."
- **BiXBiT.** Gemini p1: "BiXBiT (Биксбит) — Лучший вариант для иммерсионного охлаждения и кастомных БП"
- **BiXBiT gap.** Perplexity p7: "the results do not clearly show a built-in cloud fleet-monitoring console as explicitly as Luxor, Braiins, or ePIC."
- **PiTBiT.** Claude p3: "PiTBiT — это относительно малоизвестная прошивка с ограниченной документацией в открытых источниках."
- **PiTBiT.** Gemini p6: "Yes, PiTBiT is generally considered reliable and safe." This is sourced to pitbitecosystem.com/en/reviews/ and ultramining.com.
- **PiTBiT.** Perplexity p6: "the evidence available here is mostly self-reported marketing claims".

---

## 3. Factual errors LLMs make about BiXBiT (for the fact block)

All items are `[VERIFY]` with the product owner. None should be repeated in copy.

| # | Engine / prompt | What the LLM says about BiXBiT | Source it cites | Assessment |
|---|---|---|---|---|
| F1 | **Claude p2 (RU)** | "devfee 2,75% … либо единоразовую оплату" (devfee 2.75% or a one-time payment); "совместимы с Antminer L9, L7, S21+, T21" | altcoinlog.com/prochivka-asic/ | **Entity conflation, verified by WebFetch.** Both quotes come from altcoinlog's **PITBIT** section, which sits immediately before its Bixbit section. PiTBiT's pricing and model list were attributed to BiXBiT. **P0** |
| F2 | Claude p2 (RU) | "разработчик: BiXBiT, Россия" (developer: BiXBiT, Russia) | none | Jurisdiction label. Same pattern as Gemini r1 and Claude e4 in the EMCD run. Review with brand/legal |
| F3 | Gemini p1 (RU) | "профили для однофазных и двухфазных иммерсионных ванн" (profiles for single- and two-phase immersion tanks); "Даунвольт до -50%" (downvolt up to -50%); "Умный старт" (smart start); "интеграция с альтернативными БП" (integration with alternative PSUs); DevFee 2.8% | bixbit.io/en/firmwares/antminer, crazy-mining.org | Two-phase immersion profiles and "-50%" are unverified; "-50%" is from crazy-mining.org only. The 2.8% matches the Antminer baseline |
| F4 | ChatGPT p1 (RU) | Puts BiXBiT in the **S21** slot on the strength of "overclocking potential of up to 60%" | bixbit.io/en/blog/…s17-s17-pro…60 (the S17 release post, not dated in the citation; likely ~2019) | Stale evidence: an S17 post is used for an S21 answer. BiXBiT has no citable S21 page, while PiTBiT has `/catalog/firmware/proshivka_dlya_antminer_s21/` (cited by Perplexity p1) |
| F5 | ChatGPT p2, p7 | AMS is "бесплатная" (free), "совместима с любой прошивкой" (compatible with any firmware), "не взимает платы за разработку" (charges no development fee); "Telegram alerts, API access"; **"BiXBiT Prime firmware"** | launch.bixbitusa.io | Check whether "Prime" is a real product name and whether AMS is free for every fleet size |
| F6 | Claude p6 (EN) | "Free to download", "Increases hashrate up to 80 TH/s, cuts power usage by 10–20%" | saashub.com/compare-minetheasic-vs-bixbit-… | "80 TH/s" is a meaningless absolute figure and is repeated from the EMCD run (Claude e4). Correct the saashub listing |
| F7 | altcoinlog.com page (WebFetch) | Bixbit "1.8%-2.8% DevFee" | — | Conflicts with the 2026-09 baseline (2.8%, and 2% on M2x) `[VERIFY current]` |
| F8 | top-mining.ru page (WebFetch) | "Bixbit является … производителем систем иммерсионного охлаждения" ("Bixbit is a manufacturer of immersion cooling systems"); the firmware is framed as secondary | — | Explains why Gemini frames BiXBiT as "immersion first" |

**Proposed fact-block additions** (on top of the ePIC P0-1 table, not duplicating it):
1. **Pricing model:** one explicit sentence. Suggested wording: "BiXBiT firmware is licensed via dev fee only; no one-time license `[VERIFY]`". This directly contradicts F1.
2. **Supported Antminer models list,** including S21 variants `[VERIFY]`.
3. **AMS pricing and compatibility:** free tier limits, and "works with stock / third-party firmware" `[VERIFY]`.
4. **Official product names:** is "Prime" a product? `[VERIFY]`
5. **Company jurisdiction / HQ statement** (brand/legal decision).

---

## 4. Sources that name PiTBiT but not BiXBiT (targets)

Sources were checked in the answers and, where marked, by WebFetch.

| # | Source | Where cited | PiTBiT | BiXBiT | Type | Priority | Action (white-hat) |
|---|---|---|---|---|---|---|---|
| 1 | **ultramining.com** `/news/en/introducing-pitbit-a-brand-trusted-by-miners/` (2025-06-27) | Claude p6 (3 passages), Gemini p6 | Yes | **No** (WebFetch) | Sponsored advertorial (WebFetch: "exclusive advertorial") | P1 | ultramining publishes CIS/EN mining news. Pitch a *news* item on a real BiXBiT milestone (e.g. Whatsminer M6x support) `[VERIFY facts]`. If it is paid, it must be labeled sponsored. No disguised paid placement. The June report already listed ultramining as a PiTBiT link source |
| 2 | **youtube.com**: "PITBIT V2 firmware for Antminer S21 Pro 234TH → 300TH" (`a3YllTMvcJM`) plus shorts | ChatGPT p6, Gemini p3, p6 | Yes | No | Video | P2 | See ePIC P3 (transcribed walkthroughs). Add: an S21-specific BiXBiT video with a full transcript and J/TH on screen `[VERIFY numbers]` |
| 3 | **t.me/s/PitBitPro** (web preview of a public Telegram channel), **linkedin.com** PiTBiT posts | Perplexity p6 | Yes | No | Social | P2 | Perplexity indexes `t.me/s/` previews. Make sure BiXBiT's official Telegram channel is public and posts plain-text changelogs. This also fixes the unsourced "@bixbit_official" handle (EMCD F-risk) `[VERIFY handle]` |
| 4 | **pitbitecosystem.com/en/reviews/** | Gemini p6 → "generally considered reliable" | Own | — | Reviews page | P1 | BiXBiT has no crawlable reviews/cases page that is cited. Publish real, attributable customer cases as text (no invented quotes) |
| 5 | **pitbitecosystem.com** per-model pages (`/catalog/firmware/proshivka_dlya_antminer_s21/`, S19 Hyd, L9) | Perplexity p1, p6; Claude e4 | Own | — | Model landing | P1 | Per-model pages are PiTBiT's only citation lever. BiXBiT needs an S21 page so that F4 stops happening |

**Not gaps: sources that name both brands** (WebFetch today; this supersedes the June claim that "BiXBiT is absent"):

| Source | What the page says about BiXBiT | Action |
|---|---|---|
| altcoinlog.com `/prochivka-asic/` | Order: HiveON, Vnish, PITBIT, **Bixbit**, Braiins | **P0 correction request:** clearly separate the sections (which caused F1) and update BiXBiT's dev fee (F7) using the public fact sheet |
| top-mining.ru `/rating/rejting-proshivok-dlya-asikov-top-5/` | Braiins, **Bixbit (#2)**, HiveOn, Vnish, PitBit. BiXBiT is framed as an immersion maker (F8) | P1: pitch a factual firmware update (Whatsminer, AMS) |
| cryptorussia.ru `/news/biznes/proshivki-dlia-asic-…` | Names both | P2: fact check only |

**Monitoring slot (p4: 0/4 for both brands).** The CIS "облачный мониторинг асиков" ("cloud ASIC monitoring") answers are built from these sources, and none of them names AMS in the answers:
- headframe.io (blog comparison 2025)
- moonone.ru blog
- tcs-mining.ru
- hashrate.ru
- bemining.ru
- bankstoday.net
- bitexpert.io/wiki

This is not a PiTBiT gap (PiTBiT Online is also absent), but it is the largest open CIS slot. **P1:** pitch an AMS listing to headframe.io, tcs-mining.ru, hashrate.ru, bitexpert.io and bankstoday.net. moonone.ru is a competitor vendor, so skip it.

---

## 5. Quick wins (new only; ePIC/EMCD items are referenced, not repeated)

| Priority | Action | Why (measured) | Effort |
|---|---|---|---|
| **P0** | **altcoinlog.com correction request:** separate PITBIT and Bixbit, update BiXBiT's dev fee and models from the public fact sheet | Verified cause of F1, where Claude gave BiXBiT PiTBiT's 2.75% dev fee, one-time license and model list | S |
| **P0** | Add **"pricing model" and "official product names"** lines to the fact block and to `llms.txt` (extends ePIC P0-1 and the EMCD P1 fact block) | F1, F5 ("Prime"), F6 | S |
| **P0** | **One passage on `/en/firmwares` and `/ru/firmwares`** stating that BiXBiT firmware is managed through AMS cloud monitoring: what is monitored, alerting, API, fleet size `[VERIFY]` | Perplexity p7 says BiXBiT does "not clearly show" a cloud console. RU monitoring prompt p4 scores 0/4 | S |
| **P1** | **`/en/firmwares/antminer-s21` and `/ru/…` model page** with a crawlable text table (modes, J/TH, dev fee, all `[VERIFY]`) | ChatGPT p1 backs an S21 recommendation with an old S17 post. PiTBiT's S21 pages get cited | M |
| **P1** | **Consolidate the `launch.bixbitusa.io` AMS entity** (canonical or clear link to bixbit.io/en/ams). This extends ePIC P1-5 (bixbit.tech) | ChatGPT cites launch.bixbitusa.io for AMS in 2 of 2 AMS mentions (p2, p7) | S |
| **P1** | **Fix saashub.com** BiXBiT listing (the "80 TH/s", "10–20%" claims) | Source of F6 on Claude, now seen in two runs | S |
| **P1** | **Crawlable reviews/case page** (real clients only) | PiTBiT's `/en/reviews/` drives Gemini's "reliable" verdict | M |
| **P1** | **AMS pitch to RU monitoring listicles** (headframe.io, tcs-mining.ru, hashrate.ru, bitexpert.io) | p4: neither brand appears on any engine | M |
| **P2** | Add a PiTBiT row to the planned comparison page (ePIC P1-3 / EMCD P0), with cells sourced from PiTBiT's public pages `[VERIFY]` | Branded "PiTBiT или Vnish" / review queries offer BiXBiT as an alternative in only 1 of 8 answers | S |
| **P2** | Public Telegram channel with text changelogs (`t.me/s/` preview) | Perplexity uses PiTBiT's `t.me/s/` channel as a source | S |

**Referenced, not repeated:**
- Dev-fee table, Whatsminer-first opener, llms.txt deploy, and the d-central/spark.money outreach (ePIC §4–5).
- emcd.io pitch, Kryptex co-listing, and RU FAQPage (EMCD §4).

**Do not do:**
- Don't publish comparative claims about PiTBiT that BiXBiT cannot source.
- Don't use disguised sponsored posts.
- Don't make profitability or ROI statements. PiTBiT's "+30% profit" and "3.7M rubles" case claims should not be mirrored.

---

## 6. Cost and re-measure

**New calls, estimated from ePIC per-call averages scaled to a 1500-token cap:** about **$1.30–1.40**, within the ~$1.5 budget.

| Item | Calls | Estimated cost |
|---|---|---|
| ChatGPT | 7 | ~$0.21 |
| Perplexity | 7 | ~$0.04 |
| Claude | 7 | ~$0.55 |
| Gemini | 7 | ~$0.45 |
| LLM Mentions | 5 | Price not returned in AI mode (small) |

- MCP AI-mode responses return no `cost` field, so the exact spend is not captured.
- Re-scanning the 64 saved answers cost $0.

**Re-measure:** re-run p1, p2, p4 and p7 plus the branded p3 and p6 about 4–6 weeks after the altcoinlog correction, the AMS passage and the S21 page ship. Check that F1 is gone from Claude.
