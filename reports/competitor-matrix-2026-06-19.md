# BiXBiT Competitor Matrix — 2026-06-19
**Охват:** Braiins · Vnish · LuxOS · ePIC · EMCD · PiTBiT
**Источник:** 6 gap-анализов, WebFetch-верифицированные данные, Claude self-test

---

## 1. Где BiXBiT выигрывает

| Преимущество | Braiins | Vnish | LuxOS | ePIC | EMCD | PiTBiT | Вес |
|---|---|---|---|---|---|---|---|
| **Whatsminer firmware** | ✗ Antminer only | ✗ Antminer only | △ "select models" | △ часть M-серии | N/A | ✗ нет | **Critical** |
| **Immersion + Hydro Cooling (hardware)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Critical** |
| **PDU / Power Distribution** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | High |
| **Software-only install** (vs hardware замена) | ✓ | ✓ | ✓ | ✗ ePIC = control board $100–200/unit | N/A | ✓ | High vs ePIC |
| **Документация на основном домене** | ✗ отдельный домен | N/A | ✗ отдельный домен | N/A | N/A | N/A | Medium |
| **llms.txt** (создан, ждёт деплоя) | ✗ 404 | ✗ 404 | ✗ 404 | ✗ 404 | ✗ 404 | ✗ 404 | High (first-mover) |
| **Нет geo-IP language override** | N/A | ✗ CRITICAL BUG | N/A | N/A | N/A | N/A | Structural |
| **Mixed-fleet Claude #1** ("firmware for Antminer + Whatsminer") | ✗ | ✗ | ✗ | △ слабо | ✗ | ✗ | **Unique** |
| **Firmware + AMS + Cooling в одном вендоре** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Unique** |
| **Больший EN контент (~70 vs)** | ✗ Braiins сильнее | — | ✗ Luxor сильнее | ≈ паритет | N/A | ✓ vs PiTBiT (~7 стр) | Medium |

---

## 2. Где BiXBiT проигрывает

| Слабость | Braiins | Vnish | LuxOS | ePIC | EMCD | PiTBiT | Приоритет |
|---|---|---|---|---|---|---|---|
| **Dev fee 2.8%** | 2.5% (0% с пулом) | 2.8% → 1.8% с тирингом | не раскрыт | **1.5%** | N/A | 2.75% / one-time | P0 (продуктовый) |
| **Нет tier pricing для крупных ферм** | N/A | ✓ есть тиринг | ✓ Luxor Pool rebate | N/A | N/A | ✓ B2B тиры | P0 |
| **Нет JSON-LD schema** | частично | ✗ | ✓ FAQPage+Org+WebSite | ✗ | ✓ частично | ✗ | P0 (LuxOS реализовал) |
| **CLS = 0.888** | неизвестно | неизвестно | неизвестно | неизвестно | N/A | неизвестно | P0 |
| **8 H1 на homepage** | ✗ тоже нарушает | 2 H1 | 8–10 H1 тоже | неизвестно | N/A | норм | P0 |
| **Нет meta descriptions** | ✓ есть | ✗ нет | ✓ есть | ✗ нет | ✓ есть | ✗ нет | P0 |
| **Нет canonical + hreflang** | неизвестно | ✗ сломан | неизвестно | ✗ нет | ✓ | ✗ нет | P0 |
| **Sitemap lastmod 2024-09-04** | — | ✓ 2026-06-13 | ✓ динамический | неизвестно | ✓ | неизвестно | P1 |
| **Нет comparison pages** | ✗ тоже нет | ✗ | ✗ | ✗ | ✗ | ✗ | P0 (первый получит) |
| **Нет benchmark page (J/TH до/после)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ есть таблицы | P0 (E-E-A-T) |
| **Нет model-specific product pages** | ✗ | ✓ есть | ✗ | ✓ есть | N/A | ✓ 28 моделей | P0 |
| **Нет named case studies** | ✗ | ✗ | ✓ TeraWulf, Core Scientific | ✗ | ✗ | ✗ | P1 |
| **Нет wire PR / media presence** | ✓ активно | ✗ | ✓ 5+ релизов | ✗ | ✓ | ✗ | P1 |
| **Отсутствие в d-central.tech matrix** | ✓ есть | ✓ есть | ✓ есть | ✓ есть | N/A | ✗ нет | **P0 critical** |
| **Отсутствие в EMCD firmware article** | ✓ есть | ✓ есть | ✓ есть | ✓ есть | — | ✗ нет | P0 |
| **Отсутствие в hashrateindex.com** | ✓ (Luxor) | ✗ | ✓ (владеет) | ✓ | ✗ | ✗ | P0 |
| **Нет dev fee transparency page** | ✓ | △ на homepage | ✗ | ✓ | N/A | ✓ публичные цены | P0 |
| **Claude citation rate** | ✓ тройка | ✓ тройка | 8/10 | 7/10 | N/A | неизвестно | BiXBiT ≈ 3/10 |

---

## 3. Уникальные возможности BiXBiT (нет ни у кого)

### TIER 1 — Структурные, не копируемые

**A. Единственный full-stack провайдер: firmware + AMS + immersion cooling + hydro cooling + PDU**
Ни один конкурент не предлагает больше двух категорий одновременно. Это не реализовано в контенте ни на одной странице BiXBiT. Требует: hub-страница "BiXBiT Ecosystem" + internal linking от firmware к cooling к AMS.

**B. Whatsminer firmware + Antminer firmware в одном вендоре**
Braiins и Vnish — только Antminer. LuxOS — "select models" без деталей. ePIC — частично. PiTBiT — нет. BiXBiT поддерживает M2x–M6x + S19–S21 полностью. **В Claude этот запрос уже возвращает BiXBiT #1.** Нужно усилить: dedicated mixed-fleet page + passage-фраза "одна из немногих прошивок для обеих платформ".

**C. Firmware + immersion cooling integration**
Только у BiXBiT есть прошивка с immersion-профилями И физическая иммерсионная система. Это позволяет: более агрессивный overclock (стабильная Tj), оптимизированное охлаждение, единый вендор для commissioning. **Ни один конкурент не может это воспроизвести** — у них нет cooling hardware.

### TIER 2 — Тактические, реализуемые быстро

**D. llms.txt — первый в нише**
Все шесть конкурентов: 404. BiXBiT файл создан — нужен только деплой (30 минут). Потенциально формирует AI-индексацию сущностей до того как конкуренты среагируют.

**E. software-only install vs ePIC hardware replacement**
ePIC требует замены control board ($100–200/unit). На 1 000 ASIC = $100–200k дополнительных CAPEX до установки прошивки. BiXBiT — чистый software install. Это не оформлено в контент ни разу. Требует: сравнительная таблица TCO на /comparison странице.

**F. Geo-IP language stability**
Vnish имеет критический баг: `/en/` URL отдают китайский контент с азиатских IP. У BiXBiT этой проблемы нет. После внедрения правильного hreflang BiXBiT структурно превосходит Vnish по интернациональному краулингу.

**G. robots.txt `ai-train=yes` — 15-минутный fix**
Только LuxOS явно разрешил AI-краулерам обучаться на контенте. У остальных пяти конкурентов этого нет. Добавление в robots.txt: потенциальный долгосрочный эффект на LLM-присутствие при минимальных затратах.

---

## 4. Claude AI-Citation Scoreboard

| Конкурент | Claude mention rate | Позиция в "тройке" | Ключевые запросы |
|---|---|---|---|
| Braiins | ~100% firmware запросов | #1 по умолчанию | все firmware-запросы |
| LuxOS | **8/10** | #2–3 | enterprise, overclocking, monitoring, dev fee |
| ePIC | **7/10** | #3–4 | dev fee comparison, autotuning, Whatsminer |
| Vnish | ~90% firmware запросов | #2 по умолчанию | все Antminer-запросы |
| **BiXBiT** | **≈3/10** | вне тройки | только branded + "firmware for mixed fleet" |
| PiTBiT | неизвестно (не тестировался) | вероятно вне топ-5 | — |
| EMCD | N/A (не firmware) | N/A | — |

**Единственный запрос где BiXBiT #1:** "Which firmware supports both Antminer AND Whatsminer?" — все конкуренты проигрывают.

---

## 5. Технический SEO Scoreboard

| Элемент | BiXBiT | Braiins | Vnish | LuxOS | ePIC | PiTBiT |
|---|---|---|---|---|---|---|
| JSON-LD schema | ✗ 0 | неизвестно | ✗ 0 | ✓ 4 типа | ✗ 0 | ✗ 0 |
| Meta description | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ |
| Canonical | ✗ | неизвестно | ✗ (geo-IP bug) | неизвестно | ✗ | ✗ |
| Hreflang | ✗ | неизвестно | ✗ сломан | неизвестно | ✗ | N/A |
| og: / twitter:card | ✗ | неизвестно | ✗ | ✓ | ✗ | ✗ |
| H1 per page | ✗ 8 H1 | △ | ✗ 2 H1 | ✗ 8–10 H1 | неизвестно | ✓ |
| Sitemap freshness | ✗ 2024-09 | — | ✓ 2026-06 | ✓ динамически | неизвестно | неизвестно |
| llms.txt | △ создан | ✗ | ✗ | ✗ | ✗ | ✗ |
| ai-train в robots.txt | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |
| CLS | ✗ 0.888 | неизвестно | неизвестно | неизвестно | неизвестно | неизвестно |
| Model-specific pages | ✗ | ✗ | ✓ | ✗ | △ | ✓ |

**Вывод по тех-SEO:** LuxOS единственный конкурент с серьёзной schema-реализацией. Все остальные (включая BiXBiT) на нулевом уровне schema. Кто внедрит первым — получает rich results во всей нише.

---

## 6. Ссылочный ландшафт

| Источник | → Braiins | → Vnish | → LuxOS | → ePIC | → EMCD | → PiTBiT | → BiXBiT |
|---|---|---|---|---|---|---|---|
| d-central.tech | ✓ | ✓ | ✓ | ✓ | N/A | ✗ | **✗ P0** |
| hashrateindex.com | ✓ | ✗ | ✓ (владеет) | ✓ | ✗ | ✗ | **✗ P0** |
| EMCD article | ✓ | ✓ | ✓ | ✓ | — | ✗ | **✗ P0** |
| nicehash.com | ✓ вероятно | ✓ вероятно | ✓ вероятно | ✓ вероятно | N/A | ✗ | ✗ |
| bitcointalk.org | ✓ | ✓ | ✓ | △ | ✗ | ✗ | ✗ |
| whatsminer.com (OEM) | ✗ | ✗ | △ | △ | N/A | ✗ | **✗ уникальный шанс** |
| PRNewswire/GlobeNewswire | ✗ | ✗ | ✓ 5+ | ✗ | ✓ | ✗ | ✗ |

**Единственный источник где BiXBiT может получить ссылку которой нет у конкурентов:** whatsminer.com — как единственный провайдер с реальной full-coverage Whatsminer firmware.

---

## 7. Приоритизированный план закрытия (всех gap-ов)

### P0 — Блокируют всё остальное (технические)
| # | Действие | Effort | Затрагивает конкурентов |
|---|---|---|---|
| 1 | H1: 8 → 1 на homepage | S | Braiins, Vnish, LuxOS тоже нарушают |
| 2 | Meta descriptions на все страницы | M | Vnish, ePIC, PiTBiT тоже без |
| 3 | Canonical + hreflang EN↔RU | M | Vnish сломан; LuxOS неизвестно |
| 4 | CLS 0.888 — fix | M | Только у BiXBiT известно |
| 5 | FAQPage + Organization JSON-LD | M | Только LuxOS внедрил; первый после него получает ниш |
| 6 | Задеплоить llms.txt | S | Все 6 конкурентов: 404 — first-mover |
| 7 | `ai-train=yes` в robots.txt | S | Только LuxOS имеет |
| 8 | Sitemap lastmod — динамический | M | Vnish/LuxOS актуальны; BiXBiT 21 мес стал |

### P0 — Контент и GEO (блокируют AI-цитируемость)
| # | Действие | Effort | Почему сейчас |
|---|---|---|---|
| 9 | **FAQ на /en/firmwares** (Whatsminer, dev fee, backdoors, AMS) | S | Passage extraction для AI |
| 10 | **Аутрич к d-central.tech** — добавить в firmware matrix | H | Все 4 прямых конкурента там; BiXBiT нет |
| 11 | **Аутрич к EMCD** — попасть в "Best Firmware" статью | M | #1 SERP позиция; LLM-источник |
| 12 | **Firmware comparison page** (все 5 конкурентов + BiXBiT) | M | Нет ни у кого — SERP-слот свободен |
| 13 | **Benchmark page** с J/TH до/после [VERIFY] | H | Нет ни у кого; ePIC и PiTBiT заявляют без данных |
| 14 | **Mixed-fleet page** `/en/firmware-for-mixed-fleet` | M | BiXBiT уже #1 в Claude — закрепить позицию |
| 15 | **Entity-definition** на homepage (content/geo/entity-definition-homepage.md) | S | Готово — только вставить |

### P0 — Продуктовые (требуют PM-решения)
| # | Действие | Кто | Влияние |
|---|---|---|---|
| 16 | **Dev fee tier** для 1 000+ ASIC | PM | ePIC 1.5% выигрывает прямое сравнение; Vnish имеет тиринг |
| 17 | **Публичное ценообразование** | PM/Sales | PiTBiT показывает $150–300/модель; BiXBiT = форма |
| 18 | **Model-specific product pages** (10–15 моделей) | Content+[VERIFY] | PiTBiT, ePIC, Vnish имеют; BiXBiT — только общая |

### P1 — Контент (в течение месяца)
| # | Действие |
|---|---|
| 19 | whatsminer.com OEM outreach — партнёрская ссылка |
| 20 | Wire PR через GlobeNewswire при следующем инфоповоде |
| 21 | altcoinlog.com — попасть в roundup где сейчас PiTBiT |
| 22 | hashrateindex.com — pitch независимых данных BiXBiT |
| 23 | Named case study (один крупный оператор) |
| 24 | B2B/Enterprise landing page с условиями хостинга |
| 25 | `/en/compare/bixbit-vs-vnish`, `/en/compare/bixbit-vs-epic` |

---

## 8. Единственные ниши BiXBiT без конкурента

| Ниша | Почему нет конкурента |
|---|---|
| "Firmware для смешанного парка Antminer + Whatsminer" | Braiins/Vnish: Antminer only. LuxOS: "select". ePIC: частично. Никто не артикулирует это как positioning |
| "Firmware + immersion cooling от одного вендора" | Все firmware-вендоры продают только ПО. BiXBiT = единственный с cooling hardware |
| "BiXBiT AMS для хостинговых операторов с Antminer + Whatsminer" | Braiins Manager не умеет Whatsminer. Luxor Commander — неизвестно. Minerstat — независим |
| "Software-only Whatsminer firmware без замены платы" | ePIC = hardware замена. LuxOS = select models. BiXBiT = full software |

---

*Матрица создана: 2026-06-19. Основана на 6 gap-отчётах: competitor-gap-Braiins, Vnish, LuxOS, ePIC, EMCD, PiTBiT. DataForSEO 401 на всех сессиях — DR/DA [est.]. Все технические данные конкурентов верифицированы WebFetch (2026-06-19).*
