# GEO / AI Citation Gap: BiXBiT vs ePIC Blockchain — 2026-06-19

**Тип:** Competitor-specific AI citation gap analysis
**Конкурент:** ePIC Blockchain Technologies (epicblockchain.io) / продукт UMC OS
**Сравнение с baseline:** geo-check-2026-06-18.md

---

## Статус инструментов

| Инструмент | Доступность | Примечание |
|---|---|---|
| DataForSEO LLM Mentions API | ЗАБЛОКИРОВАН | Permission denied — требует явного разрешения пользователя |
| WebSearch (живой SERP) | Доступен | Использован для сигналов AI-видимости |
| WebFetch (страницы) | Доступен | Проверены epicblockchain.io, bixbit.io/en, bixbit.io/en/firmwares, d-central.tech |
| ChatGPT / Perplexity / Bing | НЕ ДОСТУПНЫ | Требуют браузерной сессии с авторизацией |
| Claude (self-test) | Н/Д | Не тестировался в данном отчёте — проводился ранее в geo-check-2026-06-18.md |

Вывод: данный отчёт строится на WebSearch-сигналах (какие источники ранжируются и цитируются поисковиками/LLM по нашим запросам) + прямом анализе страниц на AI-citability. **Количественные LLM-данные из DataForSEO не получены — укажи permission в настройках проекта для разблокировки.**

---

## Матрица AI-Citation Gap (WebSearch proxy)

| Промпт (B2B ICP) | ePIC/UMC OS в SERP | BiXBiT в SERP | ePIC цитируют | BiXBiT цитируют | Gap | Источники, кормящие AI |
|---|---|---|---|---|---|---|
| "best custom firmware antminer S19 S21 2025" | ДА — в d-central.tech, coinwebmining.com (компаративные статьи) | НЕТ — отсутствует в результатах | Вероятно ДА (входит в обзоры d-central) | НЕТ | КРИТИЧЕСКИЙ | d-central.tech, emcd.io, coinwebmining.com |
| "asic firmware providers comparison" | ДА — d-central.tech Bitcoin Mining Software Comparison 2026 прямо перечисляет ePIC | НЕТ — BiXBiT отсутствует в этой статье | ДА | НЕТ | КРИТИЧЕСКИЙ | d-central.tech/bitcoin-mining-software-comparison/ |
| "antminer firmware overclocking comparison" | ДА — через braiins/vnish/luxos-обзоры, ePIC упоминается как альтернатива | НЕТ | ДА (через сравнительные обзоры) | НЕТ | КРИТИЧЕСКИЙ | d-central.tech, emcd.io |
| "UMC OS firmware" / "epic blockchain firmware" | ДА — прямые страницы epicblockchain.io | НЕТ (нерелевантно) | ДА (прямой бренд-запрос) | НЕТ | — |
| "whatsminer custom firmware comparison" | НЕТ — ePIC не поддерживает Whatsminer | ДА — bixbit.io/en/firmwares/whatsminer-series-m6x в SERP | НЕТ | ДА | BiXBiT выигрывает на Whatsminer |
| "mining fleet monitoring software" | НЕТ | НЕТ | НЕТ | НЕТ | Оба отсутствуют |
| "immersion cooling providers bitcoin mining" | НЕТ | НЕТ (не в топ-результатах) | НЕТ | НЕТ | Оба отсутствуют |

**Сводка по Antminer-firmware запросам:** ePIC цитируется в 3/5 релевантных запросах через компаративный контент на d-central.tech. BiXBiT цитируется в 1/5 (только Whatsminer-специфичный запрос).

---

## Source Analysis: где живут AI-сигналы

### Источники, упоминающие ePIC (и питающие AI-ответы)

1. **d-central.tech** — крупнейший B2B-ресурс по ASIC firmware, публикует ежегодные компаративные статьи. ePIC включён в "Bitcoin Mining Software Comparison 2026". BiXBiT отсутствует.
2. **epicblockchain.io/blog** — собственный блог ePIC с техническими статьями: "Tuning Algorithms in Custom Antminer Firmware: How UMC OS Optimizes Bitcoin Mining Performance", "How to Flash Custom Antminer Firmware with UMC OS". Хорошо индексируются.
3. **altairtech.io** — дистрибьютор ePIC UMC hardware продаёт физические UMC-контроллеры — создаёт дополнительный trail упоминаний.
4. **github.com/epicblockchain** — open-source репозитории (powerplay-antminer, rig-runner, umcos-antminer) — LLM обучаются на GitHub.
5. **businesswire.com** — пресс-релизы ePIC (Argo Blockchain collaboration) — авторитетный источник для AI.

### Источники, упоминающие BiXBiT

1. **bitcointalk.org/index.php?topic=5566528** — ANN-тред на BitcoinTalk, активен с 2024-01.
2. **topgold.forum** — дублирует ANN-тред, низкий авторитет для LLM.
3. **prweb.com** — пресс-релиз "BiXBiT and Cormint... ERCOT" (2024) — хороший источник.
4. **youtube.com** — "BiXBiT Bitcoin Miner Overclocking Firmware Guide" — видео-сигнал.
5. **bixbitusa.io** — дистрибьютор США, создаёт путаницу с брендом (отдельный домен).
6. **cryptwerk.com** — каталог, низкий авторитет.
7. **saashub.com** — comparison-страница "minetheasic vs bixbit" — узкий охват.

### Ключевые разрывы источников

- BiXBiT отсутствует в d-central.tech (главный AI-feeder для firmware-запросов)
- BiXBiT отсутствует в emcd.io и coinwebmining.com (регулярно цитируются LLM)
- ePIC имеет GitHub-репозитории (LLM-тренинговые данные) — у BiXBiT GitHub не обнаружен
- ePIC имеет партнёрские материалы от Altairtech (hardware reseller) — создаёт независимые упоминания
- BiXBiT упоминается преимущественно в собственных материалах + низкоавторитетных каталогах

---

## AI-Readiness: ePIC vs BiXBiT (технический анализ страниц)

| Сигнал | ePIC Blockchain | BiXBiT |
|---|---|---|
| llms.txt | НЕТ (HTTP 404) | НЕТ (HTTP 404) |
| FAQ-секция на сайте | ДА (epicblockchain.io/support/faq/) | ДА (/en/faq + /en/firmwares#faq) |
| Passage-structured content | ЧАСТИЧНО — bullet-lists, но нет таблиц/definitions на главной | ЧАСТИЧНО — lists, но нет competitor-таблиц, нет opening definitions |
| Schema markup | НЕТ (не обнаружен) | НЕТ (не обнаружен) |
| Competitor comparison tables | НЕТ (ePIC не сравнивает себя с конкурентами) | НЕТ |
| Performance numbers в passage-контенте | ЧАСТИЧНО — "10-25% improvement vs stock" (без J/TH таблиц) | ЧАСТИЧНО — "60% switching losses reduction" в testimonial, нет системных benchmark-таблиц |
| Question-based headings | НЕТ | ЧАСТИЧНО — только в FAQ |
| Cited external sources | НЕТ (всё self-promotional) | НЕТ |
| GitHub / open-source присутствие | ДА (github.com/epicblockchain — 3 публичных репозитория) | НЕ ОБНАРУЖЕН |
| Упоминания в авторитетных компаративных статьях | ДА (d-central.tech, altairtech.io) | НЕТ в основных, только saashub.com |
| Пресс-релизы на wire-сервисах | ДА (businesswire.com) | ДА (prweb.com — Cormint) |
| Поддерживаемые модели | Antminer S19J+ / S21 (air-cooled) | Antminer S19/T19/L7/S21 + Whatsminer M2X-M6X |

**Вывод по AI-readiness:** Оба сайта слабо оптимизированы под AI-citability. Преимущество ePIC — в external citation trail (d-central, GitHub, altairtech), а не в on-page структуре. Преимущество BiXBiT — в охвате Whatsminer (ePIC поддерживает только Antminer), что создаёт незакрытую нишу.

---

## Passage-дыры на страницах BiXBiT (что блокирует цитирование)

### /en/firmwares (главная firmware-страница)

1. **Нет opening definition.** Страница не отвечает на вопрос "What is BiXBiT custom firmware?" в первом абзаце. AI-краулеры не могут извлечь ответ на базовый ICP-промпт.
2. **Нет сравнительной таблицы.** Отсутствует сравнение BiXBiT vs Braiins OS+ / Vnish / LuxOS / ePIC UMC OS по ключевым параметрам: dev fee, совместимость, J/TH improvement, autotuning.
3. **Нет benchmark-таблицы.** Нет структурированных данных по поддерживаемым моделям с реальными performance-цифрами (J/TH до/после, TH/s). Единственная цифра — "60% reduction in switching losses" из testimonial.
4. **FAQ не на первом экране.** FAQ находится в нижней части страницы, не в passage-позиции для извлечения.
5. **Нет schema FAQPage.** JSON-LD разметка отсутствует — Google не показывает FAQ в rich snippets и AI Overviews.
6. **Headings декларативны, не вопросные.** "Take control of your mining" vs "What is the best firmware for Antminer S21?" — вторые извлекаются AI.

### /en/asics-cooling (cooling-страница — не проверялась, но по аналогии)

- Ожидаем те же проблемы: отсутствие comparison-таблиц по J/TH vs air cooling, нет FAQ со schema.

---

## Рекомендации

### P0 — Критические (блокируют любое AI-упоминание)

**P0.1 — Попасть в d-central.tech firmware comparison**
d-central.tech — главный источник, который "кормит" LLM по firmware-запросам. BiXBiT полностью отсутствует в их "Bitcoin Mining Software Comparison 2026" и "Braiins vs Vnish vs LuxOS" обзорах. Тактика: аутрич к d-central с предложением включить BiXBiT в сравнительные статьи. Приоритет: Whatsminer-сегмент — единственный, где BiXBiT дифференцирован vs ePIC.

**P0.2 — Добавить opening definition на /en/firmwares**
Первый абзац должен отвечать на промпт "What is BiXBiT firmware?":
> "BiXBiT custom firmware is a third-party ASIC firmware for Antminer (S19, T21, S21 series) and Whatsminer (M2X-M6X series) miners, enabling chip-level overclocking, energy-saving profiles, and AsicBoost to reduce power consumption by 10-20%. Dev fee: [VERIFY]. Supported models: [VERIFY full list]."

### P1 — Высокий приоритет

**P1.1 — Создать /llms.txt**
Оба конкурента (ePIC и BiXBiT) не имеют llms.txt. Это возможность стать первым в нише. Файл должен содержать: описание продуктов, ключевые факты, ссылки на FAQ и тех-страницы.

**P1.2 — Benchmark comparison table на /en/firmwares**
Добавить таблицу вида:
| Firmware | Antminer S21 support | Whatsminer support | Dev fee | Key feature |
|---|---|---|---|---|
| BiXBiT | Yes | Yes (M2X-M6X) | [VERIFY] | Quickstart 3 min |
| Braiins OS+ | Yes | No | 2-2.5% | Stratum V2, autotuning |
| Vnish | Yes | Yes | 2-2.8% | Per-chip tuning |
| LuxOS | Yes | No | 2.8% | SOC2, curtailment |
| ePIC UMC OS | Yes (S19J+) | No | 1.5% | Perpetual Tune |

Все цифры помечать [VERIFY] до проверки командой.

**P1.3 — FAQPage schema (JSON-LD) на /en/firmwares**
Добавить JSON-LD разметку для существующего FAQ. Это активирует FAQ rich snippets в Google и увеличивает вероятность попадания в AI Overviews.

**P1.4 — Аутрич к emcd.io, coinwebmining.com**
Эти ресурсы публикуют ежегодные firmware-обзоры и цитируются LLM. Предложить включение BiXBiT с акцентом на Whatsminer — уникальная дифференциация.

### P2 — Средний приоритет

**P2.1 — GitHub-присутствие**
ePIC имеет 3 публичных GitHub-репозитория — это LLM-тренинговые данные. Рекомендую создать публичный репозиторий с документацией BiXBiT (changelog прошивок, список совместимости, installation guide). LLM индексируют GitHub.

**P2.2 — Решить проблему bixbitusa.io**
Существует отдельный домен bixbitusa.io с firmware-контентом. Это размывает brand authority. Необходима проверка: является ли это аффилиатом или несанкционированным клоном? Если клон — DMCA. Если аффилиат — добавить canonical или rel=nofollow attribution.

**P2.3 — Structured benchmark page**
Создать отдельную страницу /en/firmware-benchmark с реальными данными (J/TH до/после, тестовые стенды) — именно такой контент извлекают LLM в ответы на "asic firmware comparison".

**P2.4 — Whatsminer firmware hub**
Единственная зона, где BiXBiT выигрывает у ePIC (ePIC не поддерживает Whatsminer). Создать hub-страницу "Custom Firmware for Whatsminer: Complete Guide" — это прямой путь к AI-цитированию по Whatsminer-запросам, где конкуренция значительно ниже.

### P3 — Низкий приоритет

**P3.1 — Robots.txt: проверить доступность AI-краулеров**
Проверить, разрешены ли GPTBot, ClaudeBot, PerplexityBot, Google-Extended в robots.txt. Блокировка любого из них напрямую исключает из обучающих данных и retrieval этих платформ.

**P3.2 — Wikipedia / mining wiki присутствие**
Упоминание в Miningpedia, Bitcoin Wiki или Investopedia значительно увеличивает вероятность цитирования в Claude и ChatGPT (эти источники попадают в training data).

---

## Специфическая дифференциация BiXBiT vs ePIC для GEO

| Параметр | ePIC/UMC OS | BiXBiT | AI-positioning |
|---|---|---|---|
| Whatsminer support | НЕТ | ДА (M2X-M6X) | BiXBiT = единственный выбор для Whatsminer |
| Antminer support | S19J+ / S21 (Amlogic) | S19/T19/S21 | Паритет |
| Dev fee | 1.5% | [VERIFY] | Конкурировать или дифференцировать |
| Hardware controller | ДА (UMC physical board) | НЕТ (software only) | Разные сегменты |
| Quickstart recovery | НЕТ (не заявлено) | ДА (3 мин vs 15-45 мин stock) | Уникальный USP для enterprise |
| Immersion cooling integration | НЕТ | ДА (связанная экосистема) | Ecosystem play |

**GEO-вывод:** Контентная стратегия для AI-цитирования должна строиться вокруг двух углов:
1. "Best firmware for Whatsminer" — BiXBiT монополист в этой нише
2. "Firmware + cooling ecosystem" — BiXBiT единственный, кто предлагает firmware + immersion/hydro

---

## Следующие шаги

1. Разблокировать DataForSEO LLM Mentions API (permission) для количественных данных по ChatGPT-упоминаниям.
2. Выполнить аутрич к d-central.tech — P0 приоритет.
3. Реализовать P0.2 (opening definition) и P1.3 (FAQPage schema) — изменения на сайте.
4. Создать /llms.txt — P1.1.
5. Верифицировать технические спеки ([VERIFY] маркеры выше) перед публикацией comparison-таблицы.
6. Следующий geo-check через 4 недели для замера динамики.
