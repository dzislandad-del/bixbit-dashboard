# Competitor Gap — сводка: ePIC · EMCD · PiTBiT

**Дата:** 2026-09-25
**Отчёты:** `competitor-gap-{ePIC,EMCD,PiTBiT}-2026-09-25.md`, подробности в `reports/sub/`. Данные: `data/dfs-*-2026-09-25.json`, `data/geo-{epic,emcd,pitbit}-2026-09-25/`.
**Источники:** DataForSEO (Labs, Backlinks, AI Optimization, On-Page, SERP).
**Недоступно:** PageSpeed (500), CrUX (403), Moz, Bing, российская выдача (DataForSEO 40501). GSC и GA4 в этом прогоне не использовались.

## 1. Сводная матрица

| Измерение | BiXBiT | ePIC | EMCD | PiTBiT |
|---|---|---|---|---|
| Органика US (ключи / ETV) | **162 / 115** | 10 / 15 | 955 / 267 (358 майнинговых) | 4 / ~0 |
| Прошивки, охлаждение, мониторинг в US | **Whatsminer #3, asic monitor #7, immersion #1–2** | Только брендовые запросы | 2 firmware-ключа, оба ниже топ-30 | 0 |
| Ссылающиеся домены (main) / spam score | 885 / 44 | 170 / 13 | **2 649 / 35** | ~96 / 30–34 |
| AI-упоминания (измерено) | 13/50; 28/84 | 7/50 | emcd.io цитируется в 33% сравнительных ответов | 1/84 |
| ChatGPT | **0** цитирований bixbit.io | 3/8 | 0/16 | 0 |
| hreflang | 2 шаблона | нет (только EN) | **все страницы, 5 языков** | нет |
| Firmware-страница (lab LCP / вес) | **42 с / 23.8 MB** | 9 с / 2.0 MB | 13 с / 6.9 MB | 3.7 с / 6.5 MB |
| TTFB | **~40 мс** | 2.3 с | 300–400 мс | 250–1048 мс |

## 2. Где BiXBiT выигрывает

| Преимущество | Против кого | Данные |
|---|---|---|
| Whatsminer-прошивки: единственный вендор в выдаче | Все три | US: whatsminer firmware #3, custom #2. KZ/ru: «прошивка whatsminer» #1. LLM называют BiXBiT в 4 из 5 движков |
| Охлаждение (immersion, hydro, mineral oil) | Все три | 13 cooling-ключей в топ-20 US. У конкурентов 0 |
| Мониторинг (AMS) | ePIC, EMCD; PiTBiT в выдаче | asic monitor #7 (US), «мониторинг асиков» #3 (KZ) |
| Органика US по коммерческим запросам | ePIC, PiTBiT; EMCD в нише | 162 ключа против 10 и 4; в 9 из 14 общих ключей с EMCD BiXBiT выше |
| AI-упоминания в целом | ePIC, PiTBiT | 13/50 против 7/50 (ePIC); 28/84 против 1/84 (PiTBiT) |
| Скорость сервера и главной страницы | Все три | TTFB ~40 мс, главная: LCP 2.75 с, CLS 0.001 |
| Англоязычные отраслевые доноры | PiTBiT, EMCD | bitcointalk 177, d-central, b.tc, irlbtc 104, prnewswire |
| СНГ-медиа | ePIC | bits.media, forklog, habr, minecool, ultramining |

## 3. Где BiXBiT проигрывает

| Разрыв | Кто впереди | P | Закрытие |
|---|---|---|---|
| Вес firmware-страницы (23.8 MB, LCP 42 с) | **Все три** | **P0** | AVIF/WebP + srcset, preload hero, lazy-load |
| Как объяснять dev fee («lowest dev fee» в LLM: ePIC 4/5, BiXBiT 0/5) | ePIC | **P0** | Страница про dev fee и TCO. Не заявлять «самая низкая комиссия» (2.8% `[VERIFY]` — это диапазон Vnish) |
| ChatGPT не цитирует bixbit.io (0/11) | ePIC | **P0** | Блок фактов, llms.txt (~~301 с `bixbit.tech`~~ отменено 2026-09-30: bixbit.io заблокирован в РФ, bixbit.tech — вход для РФ) |
| LLM искажают факты о BiXBiT (в т.ч. приписывают BiXBiT dev fee PiTBiT 2.75%) | PiTBiT, altcoinlog | **P0** | Канонический блок фактов; аутрич в altcoinlog |
| BiXBiT нет в статьях-сравнениях, которые цитируют LLM (d-central, spark.money, EMCD) | ePIC, EMCD | **P0** | Своя страница `/firmwares/comparison` (en+ru) и питч с фактшитом |
| hreflang на 2 шаблонах из 10+ | EMCD | **P0** | Во все шаблоны + связь «translation of» |
| Качество ссылок (44% доменов spam ≥ 50, TR/RU; нет US/CA) | ePIC, EMCD | P1 | Аутрич в US/LatAm; disavow только явного спама, решение за человеком |
| HTML (дублирующийся `<body>`), og:image = favicon, schema не связана | ePIC | P1 | Исправить шаблон, OG-картинки, `@graph` |
| Страницы прошивки по моделям | PiTBiT (26 на ru) | P1 | Шаблон `/firmwares/antminer/{model}` |
| Запросы про доходность ASIC (4 × 480–590/мес) | EMCD | P1 | J/TH/TCO + калькулятор, без обещаний доходности |
| Языки (ES, PT под LatAm) | EMCD | P2 | `international-seo` |
| Видео и Telegram в СНГ | PiTBiT | P2 | Видео на ru по S19, S21, T21 |

## 4. Уникальные возможности (никто не занял)

| Возможность | Почему уникальна | P |
|---|---|---|
| **«прошивка antminer» (ru)** | В топ-20 ни одного вендора, только YouTube, форумы и зеркала | **P0** |
| **«прошивка для асиков» (KZ)** | Слабая первая страница; operativa.ru (#3) уже упоминает прошивку BiXBiT для S9k (статья 2022 года), можно попросить обновить | **P0** |
| **llms.txt** | 404 у BiXBiT, ePIC, EMCD и PiTBiT | P1 |
| **Позиционирование «Antminer + Whatsminer + охлаждение + мониторинг + PDU в одной экосистеме»** | Ни у кого из трёх нет больше двух из этих направлений | P0 (для контента) |
| **Прошивка без замены железа** | Против ePIC UMC (замена контроллера) `[VERIFY]` | P1 |
| **Cross-gap домены: ссылаются на ≥2 конкурентов, но не на BiXBiT** | criptonoticias.com, miningdisrupt.com, bitcoinminingstock.io, digitalcurrencyresearch.io, top-mining.ru, rushash.ru, kernelpanicpodcast.com (сначала проверить spam) | **P0** |
| **Листинги ASIC-каталогов** | asicminervalue.com, asicprices.com, onlybestminers.com | P1 |

## 5. Порядок работ (объединённый)

1. **Эта неделя:**
   - Убрать «no dev fee» из брифов в `content/`.
   - Сжать изображения на `/en/firmwares/antminer`.
   - Блок фактов и llms.txt.
   - Первый абзац firmware-страниц: Antminer + Whatsminer + AMS.
   - ~~Проверить `bixbit.tech` … и склеить с основным доменом~~ — отменено 2026-09-30: bixbit.tech — рабочий домен для РФ (bixbit.io заблокирован), bixbitusa.io — домен партнёров. См. dev-task P0-0.
2. **30 дней:**
   - `/firmwares/comparison` (en+ru), страница про dev fee и TCO, /ru-хаб Antminer.
   - hreflang во все шаблоны.
   - Аутрич в altcoinlog, d-central, spark.money, EMCD и в 4 cross-gap P0-домена.
3. **60 дней:**
   - Страницы моделей, J/TH-калькулятор, сравнение программ мониторинга на ru.
   - HTML, OG и `@graph`.
   - Каталоги ASIC.
4. **90 дней:**
   - Wire PR, конференции, подкасты, видео на ru.
   - BD: EMCD `/fw/`, хостинги в СНГ.
   - Аудит спама.
   - ES и PT.
