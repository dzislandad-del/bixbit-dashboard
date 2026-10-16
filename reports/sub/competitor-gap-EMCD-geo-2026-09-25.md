# GEO / AI-Citation Gap: BiXBiT vs EMCD (emcd.io), 2026-09-25

**Question:** EMCD is a mining pool, not a firmware vendor. Do its articles "feed" LLM answers about ASIC firmware, and is BiXBiT present in those answers?
**Method: MEASURED.** Live DataForSEO AI Optimization calls plus reuse of the ePIC run from the same day. This replaces the June Claude self-test in `reports/competitor-gap-EMCD-2026-06-19.md`.

---

## 0. Data sources and status

| Source | Status | Notes |
|---|---|---|
| ePIC run reuse (`data/geo-epic-2026-09-25/`) | OK | 10 non-branded prompts × 4 LLMs = 40 answers, plus 10 AIO keywords. **Not re-run.** Every answer was grepped for `emcd`. (`aio-q8` matched only a base64 string, a false positive.) |
| ChatGPT `chat_gpt/llm_responses/live` | OK, 6/6 | gpt-4.1-mini, web_search + force_web_search, US on EN prompts, no location on RU prompts |
| Perplexity `perplexity/llm_responses/live` | OK, 6/6 | sonar |
| Claude `claude/llm_responses/live` | OK, 6/6 | claude-sonnet-4-6. e2, r1 and r2 were truncated at 2000 tokens |
| Gemini `gemini/llm_responses/live` | OK, 6/6 | gemini-3.5-flash. The endpoint has no location parameter |
| Google AIO (`serp/google/organic/live/advanced` + `load_async_ai_overview`) | OK, 1 keyword | "vnish vs braiins os", US/en |
| LLM Mentions `llm_mentions/search/live`, target `domain: emcd.io`, scope `sources` | OK, 2 calls | Google AIO: 170 answers. ChatGPT: 5 answers (US/en only) |
| Russian-language prompts | Supported | All 4 LLMs answered in Russian. ChatGPT also switched to Russian on the English CIS prompt e4 |
| WebFetch of the top EMCD article | **Partial** | Returned only the page title (the body is probably rendered client-side). Whether BiXBiT appears on the page is **unverified** |
| curl | Not used | Denied in the previous run, so it was not retried |

**Raw data:** `data/geo-emcd-2026-09-25/`
- `e1.json`–`e4.json`, `r1.json`, `r2.json`: condensed per-engine records with task IDs, named brands, cited URLs and verbatim anchors.
- `gemini-e2.raw.json`: full raw Gemini response for e2.
- `llm-mentions-google-emcd-sources.json`, `llm-mentions-chatgpt-emcd-sources.json`: full LLM Mentions dumps.
- The other live answers came back inline through MCP, so only condensed records exist for them. Their task IDs are kept for re-pull.

**Limits:**
- Each prompt was run once per engine, so every cell is n=1.
- LLM answers vary between runs; treat 1-answer differences as noise.

---

## 1. Headline: how often LLMs cite emcd.io (measured)

| Scope | emcd.io cited | BiXBiT named | BiXBiT in the same answer as an emcd.io citation |
|---|---|---|---|
| ePIC prompt set q1–q10 × 4 LLMs (40) | **6 / 40** (15%) | 11 / 40 | 2 (Perplexity q1, Gemini q4) |
| New EMCD prompts e1–e4, r1, r2 × 4 LLMs (24) | **4 / 24** (17%) | 8 / 24 | 0 |
| **All LLM answers (64)** | **10 / 64 (16%)** | 19 / 64 | 2 / 10 |
| Firmware-only prompts (52; excludes q7 monitoring, q8 cooling, r2 pools) | 8 / 52 (15%) | — | — |
| **Comparison prompts** (q1, q4, q5, e2, e3, r1 = 24 answers) | **8 / 24 (33%)** | — | — |
| Google AIO (11 keywords) | **0 / 11**, and emcd.io is not in the top-20 organic results for "vnish vs braiins os" | — | — |

emcd.io citations by engine (of 16 answers each):

| Engine | emcd.io cited | Prompts |
|---|---|---|
| ChatGPT | **0** | — |
| Perplexity | 4 | q1, q5, q7, e2 |
| Claude | 3 | q4, e2, r1 |
| Gemini | 3 | q4, q5, r2 |

**Conclusion:**
- EMCD feeds LLMs through **one article**, and only when the prompt asks for a "Vnish vs Braiins vs LuxOS" comparison. In those prompts it is cited in a third of answers.
- Claude leans on that article hardest: 4 passages in e2 and 2 passages in r1 are attributed to it.
- EMCD has **no footprint in Google AIO or ChatGPT** for firmware.

### LLM Mentions DB (historical sample, US/en)

| Platform | Answers citing emcd.io | Firmware answers among them |
|---|---|---|
| Google AIO | 170 | **0** |
| ChatGPT | 5 | **0** |

- **Top AIO URLs:**
  - `/articles/mining/is-mining-crypto-on-a-laptop-worth-it/` (27 answers)
  - `/how-long-does-a-gpu-last-while-mining/` (22)
  - `/mining-with-antminer-s9-asic-is-it-still-profitable/` (10)
  - `/asic-miners-profitability-and-roi/` (3)
- **ChatGPT topics:** crypto-ban countries, Dash, S9 profitability.
- In the historical corpus, EMCD is a **GPU and profitability** source, not a firmware source, the same pattern the ePIC run found for BiXBiT. The firmware article's pull shows up only in live web-search answers.

---

## 2. Query × engine matrix

**Legend:**
- **M** = emcd.io cited
- **m** = EMCD named in text but emcd.io not cited
- **B** = BiXBiT named
- **b** = bixbit.io cited
- `—` = none of these

### New EMCD-specific prompts

| # | Prompt | ChatGPT | Perplexity | Claude | Gemini | Brands named (union) |
|---|---|---|---|---|---|---|
| e1 | Which bitcoin mining pools also offer their own custom ASIC firmware? | — | **B** (via pool.kryptex.com) | — | **B** (via pool.kryptex.com) | Braiins, LuxOS, NiceHash FW (MARA), PowerPool×Vnish, Crypto LLC, ePIC, **Kryptex×VNISH / Kryptex×BiXBiT**, Kryptex×GMiner, Antpool |
| e2 | Best ASIC firmware comparison: Vnish vs Braiins OS vs LuxOS vs others, 2026 | — | **M** | **M** (4 passages) | — | Vnish, Braiins OS+, LuxOS, NiceHash FW, ePIC UMC, Tether MiningOS |
| e3 | Vnish vs Braiins OS+ for S19/S21, better alternatives? | — | — | — | — | Vnish, Braiins, LuxOS, Awesome Miner FW, DCENT_OS, NiceHash FW |
| e4 | Best firmware for Antminer S21 in Russia/Kazakhstan/CIS | — (RU: Vnish only) | **B b** | **B** (no bixbit.io link) | **B b** (4 bixbit.io URLs) | Vnish, Braiins, BiXBiT, PITBIT, Awesome Miner, NiceHash, ROI ASIC |
| r1 | (RU) Лучшая кастомная прошивка для Antminer и Whatsminer 2026 | — | **B b** (4 bixbit.io/ru URLs) | **M** (2 passages) | **B b** | Vnish, Braiins, LuxOS, BiXBiT, AsicDip vPro, NiceHash, MicroBT stock |
| r2 | (RU) Какой майнинг-пул выбрать в РФ/СНГ; пулы с собственной прошивкой | — | m | m | **m M** (`/ru/articles/kriptovalyuta/kak-uvelichit-dohod-ot-majninga/`) | EMCD, ViaBTC, AntPool, Trustpool, F2Pool, Promminer, WhitePool, Braiins, Vnish |
| AIO | "vnish vs braiins os" (US) | — | — | — | — | Vnish, Braiins. Sources: vni.sh, YouTube, LinkedIn, Reddit, bitcointalk, braiins.com |

### Reused ePIC prompts: only the cells where emcd.io appears

| # | Prompt | Engine and result | Notes |
|---|---|---|---|
| q1 | Best custom firmware for Antminer 2026 | Perplexity **M, B b** | Same answer cites emcd.io and names BiXBiT |
| q4 | Alternatives to Braiins OS+ | Claude **M**; Gemini **M, B b** | — |
| q5 | Compare ASIC firmware providers | Perplexity **M, B b** (offer only); Gemini **M** | — |
| q7 | Fleet monitoring software | Perplexity **M** | `emcd.io/monitoring/` and the btc-tools sub-accounts article |

### Verbatim anchors (quotes of 20 words or fewer)

- **EMCD as source.** Claude e2 cites emcd.io for: "In 2026, Vnish firmware, Braiins OS+, and LuxOS remain among the most established custom ASIC firmware options".
- **EMCD as source.** Claude r1 cites emcd.io for: "Среди наиболее широко используемых — Vnish, Braiins OS и LuxOS".
- **EMCD as source.** Gemini r2 cites emcd.io for: "EMCD официально сотрудничает с разработчиками VNISH". This is EMCD's own claim of a partnership with Vnish.
- **BiXBiT win.** Perplexity e4: "BiXBiT is also a legitimate option, especially if you want a vendor with a CIS-friendly presence and S21 support."
- **BiXBiT win.** Perplexity r1: "если нужен единый стандарт на обе линейки, тогда Braiins OS+ или BiXBiT".
- **BiXBiT win.** Gemini e1: "They also provide co-branded firmware options powered by VNISH and BiXBiT." (source: pool.kryptex.com)
- **Gap.** Claude r1 (sourced to d-central.tech) says Vnish is "единственная крупная сторонняя прошивка, поддерживающая как Antminer, так и Whatsminer". BiXBiT is erased from the Whatsminer slot.

### Attribution risks

LLMs state these facts about BiXBiT. All are `[VERIFY]`; none should be repeated in copy until checked.
- **Claude e4:**
  - "Dev fee: ~2%". This is unsourced and conflicts with the 2.8% / 2% M2x baseline.
  - "Telegram @bixbit_official" (unsourced).
  - "hashrate increase up to 80 TH/s", sourced from saashub.com.
- **Gemini e4:**
  - "30-day free trial, followed by a 2.8% DevFee".
  - "up to 40% hashrate / up to 35% energy".
  - "Farm Protect".
- **Gemini r1:** labels BiXBiT "Российский разработчик" ("Russian developer"). This is an entity/jurisdiction label to review with brand/legal.
- **Claude r2:** says EMCD integrates with Braiins OS+. This is unsourced, and Gemini says EMCD partners with VNISH. The engines contradict each other.

---

## 3. EMCD URLs that LLMs cite, ranked, and what to do with each

| # | EMCD URL | Live LLM citations (of 10) | Engines / prompts | BiXBiT on page | Target type | Action (white-hat) |
|---|---|---|---|---|---|---|
| 1 | `emcd.io/articles/mining/best-custom-asic-firmware-vnish-vs-braiins-os-vs-luxos/` | **8** | Perplexity q1, q5, e2; Claude q4, e2, r1; Gemini q4, q5 | **Unverified** (WebFetch returned the title only). The extracted passages name only Vnish, Braiins OS and LuxOS, so BiXBiT is probably absent `[VERIFY manually]` | **P0 editorial outreach + P0 competing page** | (a) Pitch EMCD's content team a factual "Whatsminer / BiXBiT" section: the article is a 3-vendor comparison and Whatsminer is BiXBiT's proven slot. BiXBiT and EMCD are not direct competitors (pool vs firmware), so a co-marketing angle is plausible `[VERIFY: any existing EMCD–BiXBiT relationship]`. (b) Build a competing BiXBiT comparison page that covers the same prompt with Whatsminer coverage (see §4) |
| 2 | `emcd.io/ru/articles/kriptovalyuta/kak-uvelichit-dohod-ot-majninga/` | 1 (6 passages) | Gemini r2 | Not checked | RU outreach | This is the source of the "EMCD × VNISH" narrative for CIS pool + firmware queries. Pitch a firmware-agnostic addition that names BiXBiT for Whatsminer / immersion. No paid disguised placement |
| 3 | `emcd.io/monitoring/` and `/articles/mining/bitcoin-mining-software-how-to-manage-an-asic-mining-farm-with-btc-tools-sub-accounts-and-batch-updates/` | 1 | Perplexity q7 | Not checked | Competing passage | Fleet monitoring is a slot where no brand wins. Add an AMS spec passage (see §4) |
| — | Historical AIO URLs (laptop/GPU mining, S9 profitability, ASIC ROI) | 170 AIO answers, 0 firmware | — | — | Not a target | Off-ICP (GPU/retail) and profitability topics. CLAUDE.md bars profitability claims. **Do not chase** |

**Adjacent sources that carry BiXBiT in pool + firmware answers (defend and expand):**
- **`pool.kryptex.com/asic-firmware`** and `/articles/hashwatcher-kryptex-en`: the only reason BiXBiT appears in e1 on 2 of 4 engines. Keep the co-branded "Kryptex × BiXBiT" listing current and ask Kryptex for a dedicated BiXBiT page `[VERIFY partnership status]`.
- **Russian listicles cited by Perplexity r1:** coindaily.ru `/mining/soft/`, top-mining.ru `/rating/rejting-proshivok-dlya-asikov-top-5/`, altcoinlog.com `/prochivka-asic/`, crypto.ru `/proshivki-dlya-asikov/`, cryptorussia.ru. Check which of them omit BiXBiT and pitch a factual entry to those.
- **Pool listicles cited on r2** (vc.ru, dtf.ru, mining1.ru, promminer.ru, top-mining.ru): these drive the "which pool" answers. Low firmware relevance, **P3**.

---

## 4. Quick wins (impact/effort)

| Priority | Action | Why (measured) | Effort |
|---|---|---|---|
| **P0** | **Verify the emcd.io comparison article by hand** (browser): does it name BiXBiT, and does it cover Whatsminer? Then send one editorial pitch to EMCD with a public BiXBiT fact sheet (Whatsminer M2x–M6x, Antminer models, dev fee 2.8% / 2% M2x `[VERIFY current]`, rollback, AMS) | The article is cited in 8 of 10 emcd.io citations, and in 33% of comparison answers on Perplexity, Claude and Gemini | S |
| **P0** | **Publish `/en/firmwares/comparison` (and `/ru/`)**, a passage-ready alternative for "Vnish vs Braiins OS vs LuxOS". Answer-first opening sentence, an HTML table (dev fee, Antminer models, Whatsminer models, autotune, rollback, open source, fleet tool), a "last verified" date, and every competitor cell `[VERIFY]` and linked to that vendor's page | e2/e3/r1 answers are assembled from comparison pages (emcd.io, d-central, vni.sh, spark.money). BiXBiT is absent from 11/12 of those answers. Perplexity r1 is the exception | M |
| **P0** | **Whatsminer claim in the first passage** of `/en/firmwares` and `/ru/firmwares`. Suggested wording: "BiXBiT is one of the few custom firmwares for Whatsminer M2x–M6x as well as Antminer" `[VERIFY wording]` | Claude r1 repeats d-central's claim that Vnish is "the only" firmware for both brands. Perplexity and Gemini already use bixbit.io/ru pages when they find them | S |
| **P1** | **Fix the published BiXBiT facts that LLMs misquote:** dev fee, trial, efficiency claims and Telegram handle. Put them in one plain-text fact block and in `llms.txt` | Claude e4 says "~2%" and Gemini e4 says "30-day trial, 2.8%": conflicting and unsourced | S |
| **P1** | **Russian-language citability.** Perplexity cites 4 `bixbit.io/ru/firmwares*` URLs on r1. Add an answer-first RU passage plus a FAQ ("Какую прошивку выбрать для Whatsminer?") with FAQPage schema. The `/en/firmwares` FAQPage currently ships `mainEntity: []` (2026-09-16 audit) | The RU/CIS prompts are BiXBiT's strongest cluster: e4 3/4, r1 2/4 | S |
| **P1** | **Kryptex co-listing:** ask for a dedicated, crawlable BiXBiT section on pool.kryptex.com | This is the only source that puts BiXBiT into "pool + firmware" answers (e1) | S |
| **P2** | **CIS pool-listicle presence** (coindaily.ru, top-mining.ru, crypto.ru): pitch a factual firmware entry | These feed the Perplexity RU answers | M |
| **P3** | **Do not target** EMCD's GPU, laptop or profitability corpus | Off-ICP, and it conflicts with the no-profitability rule | — |

**Not an EMCD gap:** ChatGPT does not cite emcd.io or bixbit.io for firmware in any of the 16 answers here. It relies on vendor mirror domains (vnish.us, vni.sh, vnish.group) and on spark.money / coinwebmining.com. That is the general ChatGPT gap already logged in the ePIC report.

**Guardrails:**
- All specs are `[VERIFY]` with the product owner.
- No "lowest fee" or "best" claims.
- No profitability statements.
- No paid or disguised placements.
- No mention spam.

---

## 5. Change since June

- The June report (`competitor-gap-EMCD-2026-06-19.md`) was a self-test.
- The measured result: EMCD's LLM influence on firmware is narrow (one English comparison article and one Russian pool article). EMCD is **absent from Google AIO and ChatGPT** for firmware.
- BiXBiT out-performs EMCD's firmware pull in the CIS and Russian slots: BiXBiT is named in 5 of 8 e4/r1 answers, while emcd.io is cited in 1 of those 8 (Claude r1).

## 6. Cost

- **New calls in this run:**
  - 24 LLM calls, estimated at about $1.19 using per-call averages from the ePIC run (ChatGPT ~$0.03, Perplexity ~$0.006, Claude ~$0.094, Gemini ~$0.069).
  - 1 AIO SERP call, about $0.01.
  - 2 LLM Mentions calls; their price is not returned in AI-mode output.
- **Estimated total:** about $1.3–1.5, within the ~$2 budget.
- MCP AI-mode responses do not return a `cost` field, so per-call cost was not captured.
- `user_data` shows an account balance of $43.98. The per-day statistic returned 0, so this run's exact spend cannot be isolated.
- Reusing the ePIC data saved about $2.25.

**Re-measure:** repeat e1–e4, r1 and r2 plus ePIC q1, q4 and q5 about 4–6 weeks after the comparison page and the EMCD pitch go out.
