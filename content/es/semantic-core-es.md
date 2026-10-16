# semantic-core-es.md: семантическое ядро для bixbit.io/es

> **Версия:** 2026-09-28. **Владелец:** international-seo, контент совместно с content-seo.
> **Данные:** `data/dfs-es-semantics-2026-09-28.json` (DataForSEO, этот запуск, $0.72), `data/dfs-search-volume-ru-kz-es-2026-09-28.json` (worldwide es, ранее),
> GSC 28 дней (2026-08-29 … 2026-09-25): `data/gsc-queries-pages-all-2026-09-28.json`, `data/gsc-pages-all-2026-09-28.json`, срезы по странам ven/mex/arg/col/esp (`gsc-query.py --country`, этот запуск).
> Живой статус `/es/`: `page-snapshot.py` от 2026-09-28 (17 URL, все 200).
> **Связанные файлы:** `content/es/meta-tags-es.md`, `content/es/content-plan-es.md`, `content/localization-plan.md` §6, `content/hreflang-spec.md`.

---

## 1. Главные выводы

1. **Спрос на испанском крошечный, но он есть во всех 5 странах.** Почти все firmware-ключи в Google Ads стоят на пороге 10/мес (это «10 = минимальное ведро», а не точное число). Как и для US, **объём не главный критерий**: решают показы GSC, текущие позиции и CPC.
2. **LatAm ищет англоязычными формулировками в испанском интерфейсе.** В GSC по VE/AR/CO главные небрендовые запросы — `whatsminer firmware` (746 показов, поз. 4–5, **0 кликов**), `antminer firmware` (170), `firmware antminer` (144), `whatsminer tool descargar` (328), `mejor firmware para antminer s9` (142). Ранжируются **EN-страницы**, `/es/` почти не показывается. ES-страницы должны покрывать оба порядка слов (`firmware antminer` / `antminer firmware`) и англицизмы (`overclock`, `firmware`).
3. **Бренд в Венесуэле:** `bixbit` — 170/мес в VE (Google Ads) и 720 показов / 49 кликов в GSC за 28 дней, всё уходит на `/en`. После hreflang `es` Google должен начать отдавать `/es` испаноязычным пользователям, поэтому главная ES должна быть готова к брендовому трафику.
4. **Whatsminer — самый большой ES-разрыв:** 746 показов по `whatsminer firmware` при позиции 4–5 и нулевом CTR, а ES-страницы Whatsminer **не переведены** (title/description на EN, H1 пустой). Это P0 для локали.
5. **Конкуренты с испанскими страницами в выдаче:** `hashcore.com/es/firmware/antminer-s19` (#3 по «firmware antminer», MX), `cdn.miners.tools/es/whatsminer/*` (7 из 16 результатов по «firmware whatsminer», VE), испанский блог NiceHash (#8). BiXBiT в MX #6, но с EN-страницей `/en/firmwares/antminer`; в VE #8 с EN-постом блога. Обе выдачи с AI Overview, отмечены `volatile`.
6. **Охлаждение и PDU на испанском — общий, не майнинговый спрос.** `refrigeracion por inmersion` 70 (ES) / 40 (MX), но «inmersion» в Labs забит кухонными блендерами; `liquido dielectrico` 720 (MX) — трансформаторы/промышленность. Майнинговые формулировки (`refrigeracion por inmersion mineria`, `tanque de inmersion mineria`, `pdu mineria`) — n/d. Цель — релевантность и GEO, а не объём.
7. **Мониторинг: спрос — на бренды конкурентов**, а не на родовые запросы: `minerstat` 90/50/70/20/70, `hive os` 70/70/50/20/40, `awesome miner` 30/10/10/10/20. Родовые `monitoreo asic`, `software de monitoreo mineria` — n/d. Отсюда ставка на `/es/ams/comparison` (после EN v2) и на LSI-покрытие `/es/ams`.

### Аномалии и то, что не используем
| Ключ | Значение | Почему не используем |
|---|---|---|
| `vnish` (worldwide es) | 110 000 | аномалия Google Ads (смешано с посторонним термином), из прошлого снимка. Используем только `vnish firmware` (10–30) |
| `asic` (MX) | 110 000 | смешано с ASIC (обувь), ASIC Australia, лабораториями ASIC в Мексике |
| `inmersion` / `batidora de inmersion` (MX) | 5 400 / 8 100 | кухонная техника |
| `liquido dielectrico` (MX) | 720 | трансформаторное масло, промышленность; только LSI |
| `mineria de bitcoins` | 880 (ES, MX) | информационный B2C-спрос; не для коммерческих страниц, нет ES-блога |
| `cuanto genera una antminer s19`, `antminer s19 profitability` | 10–20 | запрос о доходности: **не делаем контент** (правило: без заявлений о доходности) |
| GSC VE/AR/CO: `whatsminer firmware` 266 / 236 / 240, `whatsminer tool descargar` 119 / 102 / 107 | — | подозрительно одинаковые показы в трёх странах: возможно, автоматические (rank-трекеры) [VERIFY]. Выводы по CTR с этой оговоркой |

---

## 2. Методика и покрытие

| Источник | Что дал | Стоимость |
|---|---|---|
| Google Ads `search_volume` × 5 (ES 2724, MX 2484, AR 2032, CO 2170, VE 2862), 99 ключей, `noAiMode` | объём и CPC по странам | $0.45 |
| Labs `keyword_suggestions` (antminer — MX/ES/VE; whatsminer, asic, inmersion, mineria — MX) | long-tail, модели, LSI | $0.14 |
| Labs `keyword_ideas` (MX) | нерелевантно (vmware и т.п.), отброшено | $0.05 |
| Labs `bulk_keyword_difficulty` (MX, ES) | KD только для головных запросов; для long-tail — null (не измерено ≠ 0) | $0.05 |
| Labs `search_intent` (es) | интент для всех 99 ключей | $0.02 |
| SERP organic live, `noAiMode: true` × 2 | «firmware antminer» MX, «firmware whatsminer» VE | $0.01 |
| **Итого** | | **$0.72** |

- **Venezuela поддерживается** и Google Ads, и Labs (ошибки 40501 нет).
- Легенда объёмов: число — Google Ads (10 = нижнее ведро), `0` — Google Ads вернул 0, `–` — нет данных (null). Объёмы не округлялись и не достраивались.
- KD `–` означает «не измерено Labs», а не «лёгкий».
- Colombia и Argentina в Labs не запрашивались (экономия бюджета), по ним только Google Ads + GSC.

---

## 3. Ядро: кластер → ключ → страница

| Кластер | Ключ | Страны со спросом | Объём ES / MX / AR / CO / VE | CPC, $ (max) | KD (MX/ES) | Интент | Целевой URL |
|---|---|---|---|---|---|---|---|
| FW-A Antminer (pilar) | firmware antminer | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | antminer firmware | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | firmware para antminer | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | firmware personalizado antminer | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | firmware antminer s19 | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | antminer s19 firmware | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | firmware antminer s21 | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | firmware antminer s9 | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | antminer s9 firmware | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | descargar firmware antminer | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | descargar firmware antminer s9 | MX, VE | 0 / 10 / 0 / 0 / 10 | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | firmware antminer l7 | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares/antminer |
| FW-A Antminer (pilar) | firmware antminer l9 | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares/antminer |
| FW-B Tuning (secciones en /antminer) | overclock antminer | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | informational | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | overclock antminer s19 | ES, AR, CO | 10 / 0 / 10 / 10 / 0 | – | – | informational | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | overclock antminer s9 | ES, AR, VE | 10 / 0 / 10 / 0 / 10 | – | – | transactional | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | antminer s9 overclock | ES, AR, VE | 10 / 0 / 10 / 0 / 10 | – | – | informational | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | underclock antminer | n/d везде | – / – / – / – / – | – | – | informational | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | undervolt antminer | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | autotuning antminer | n/d везде | – / – / – / – / – | – | – | commercial | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | antminer modo bajo consumo | n/d везде | – / – / – / – / – | – | – | commercial | /es/firmwares/antminer (H2 + FAQ) |
| FW-B Tuning (secciones en /antminer) | antminer s19 consumo | n/d везде | – / – / – / – / – | – | – | informational | /es/firmwares/antminer (H2 + FAQ) |
| FW-C Hub firmware ASIC | firmware asic | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares |
| FW-C Hub firmware ASIC | firmware para asic | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares |
| FW-C Hub firmware ASIC | firmware personalizado asic | n/d везде | – / – / – / – / – | – | – | transactional | /es/firmwares |
| FW-C Hub firmware ASIC | overclocking asic | n/d везде | – / – / – / – / – | – | – | informational | /es/firmwares |
| FW-D Whatsminer | firmware whatsminer | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | informational | /es/firmwares/whatsminer-all-series (сначала перевод); модели -> -m3x / -m5x |
| FW-D Whatsminer | whatsminer firmware | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 20 | – | – | informational | /es/firmwares/whatsminer-all-series (сначала перевод); модели -> -m3x / -m5x |
| FW-D Whatsminer | firmware whatsminer m30s | n/d везде | – / – / – / – / – | – | – | informational | /es/firmwares/whatsminer-all-series (сначала перевод); модели -> -m3x / -m5x |
| FW-D Whatsminer | firmware whatsminer m50 | n/d везде | – / – / – / – / – | – | – | informational | /es/firmwares/whatsminer-all-series (сначала перевод); модели -> -m3x / -m5x |
| FW-D Whatsminer | whatsminer hydro | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | informational | /es/firmwares/whatsminer-all-series (сначала перевод); модели -> -m3x / -m5x |
| FW-E Comparación / alternativas | mejor firmware antminer | n/d везде | – / – / – / – / – | – | – | commercial | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | mejor firmware para antminer s9 | VE | 0 / 0 / 0 / 0 / 10 | – | – | commercial | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | braiins os | ES, MX, AR, CO, VE | 20 / 20 / 10 / 10 / 30 | 5.99 (CO) | – | informational | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | braiins os antminer s19 | ES, MX, AR | 10 / 10 / 10 / – / 0 | – | – | navigational | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | vnish firmware | ES, MX, AR, CO, VE | 20 / 10 / 20 / 10 / 30 | 0.27 (AR) | – | transactional | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | firmware vnish | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | 0.01 (MX) | – | transactional | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | vnish antminer | ES, AR, CO, VE | 10 / 0 / 10 / 10 / 10 | – | – | informational | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | luxos firmware | ES, MX, AR, VE | 10 / 10 / 10 / 0 / 10 | – | – | commercial | новая: /es/firmwares/comparison (после EN v2) |
| FW-E Comparación / alternativas | hiveon asic | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | informational | новая: /es/firmwares/comparison (после EN v2) |
| DOC Instrucciones (WhatsMinerTool, BTC Tools) | whatsminer tool | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 70 | – | – | informational | новая: /es/documentation/* (перевод EN-глав) |
| DOC Instrucciones (WhatsMinerTool, BTC Tools) | whatsminer tool descargar | n/d везде | – / – / – / – / – | – | – | informational | новая: /es/documentation/* (перевод EN-глав) |
| DOC Instrucciones (WhatsMinerTool, BTC Tools) | btc tools | n/d везде | – / – / – / – / – | – | – | informational | новая: /es/documentation/* (перевод EN-глав) |
| DOC Instrucciones (WhatsMinerTool, BTC Tools) | actualizar firmware antminer | n/d везде | – / – / – / – / – | – | – | transactional | новая: /es/documentation/* (перевод EN-глав) |
| DOC Instrucciones (WhatsMinerTool, BTC Tools) | actualizar firmware antminer s19 | n/d везде | – / – / – / – / – | – | – | transactional | новая: /es/documentation/* (перевод EN-глав) |
| DOC Instrucciones (WhatsMinerTool, BTC Tools) | como actualizar firmware antminer | n/d везде | – / – / – / – / – | – | – | transactional | новая: /es/documentation/* (перевод EN-глав) |
| DOC Instrucciones (WhatsMinerTool, BTC Tools) | instalar firmware antminer | n/d везде | – / – / – / – / – | – | – | transactional | новая: /es/documentation/* (перевод EN-глав) |
| DOC Códigos de error | codigos de error whatsminer | n/d везде | – / – / – / – / – | – | – | informational | новая: /es/documentation/<códigos de error Whatsminer> (после решения P0-5 docs.bixbit.io) |
| DOC Códigos de error | errores whatsminer | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 30 | 0.01 (CO) | – | informational | новая: /es/documentation/<códigos de error Whatsminer> (после решения P0-5 docs.bixbit.io) |
| DOC Códigos de error | error whatsminer | n/d везде | – / – / – / – / – | – | – | informational | новая: /es/documentation/<códigos de error Whatsminer> (после решения P0-5 docs.bixbit.io) |
| DOC Códigos de error | whatsminer error codes | n/d везде | – / – / – / – / – | – | – | informational | новая: /es/documentation/<códigos de error Whatsminer> (после решения P0-5 docs.bixbit.io) |
| DOC Códigos de error | codigos de error antminer | n/d везде | – / – / – / – / – | – | – | informational | не покрываем: нет EN-источника по кодам Antminer [VERIFY] |
| AMS Monitoreo | monitoreo asic | n/d везде | – / – / – / – / – | – | – | informational | /es/ams |
| AMS Monitoreo | monitoreo de asic | n/d везде | – / – / – / – / – | – | – | informational | /es/ams |
| AMS Monitoreo | monitoreo de mineros | n/d везде | – / – / – / – / – | – | – | informational | /es/ams |
| AMS Monitoreo | monitoreo granja mineria | n/d везде | – / – / – / – / – | – | – | informational | /es/ams |
| AMS Monitoreo | software de monitoreo mineria | n/d везде | – / – / – / – / – | – | – | commercial | /es/ams |
| AMS Monitoreo | software de mineria | ES, MX, AR, CO, VE | 10 / 20 / 10 / 10 / 10 | 9.09 (VE) | –/49 | commercial | /es/ams |
| AMS Monitoreo | software para mineria | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | 2.48 (MX) | –/49 | commercial | /es/ams |
| AMS Monitoreo | software para mineria de bitcoin | n/d везде | – / – / – / – / – | – | – | commercial | /es/ams |
| AMS Monitoreo | programa para minar bitcoin | n/d везде | – / – / – / – / – | – | – | transactional | /es/ams |
| AMS Alternativas | awesome miner | ES, MX, AR, CO, VE | 30 / 10 / 10 / 10 / 20 | 0.17 (AR) | 57/5 | informational | новая: /es/ams/comparison (после EN v2) |
| AMS Alternativas | minerstat | ES, MX, AR, CO, VE | 90 / 50 / 70 / 20 / 70 | 1.86 (ES) | 4/11 | informational | новая: /es/ams/comparison (после EN v2) |
| AMS Alternativas | hive os | ES, MX, AR, CO, VE | 70 / 70 / 50 / 20 / 40 | – | 29/27 | informational | новая: /es/ams/comparison (после EN v2) |
| AMS Alternativas | hiveos asic | ES, MX, CO, VE | 10 / 10 / 0 / 10 / 10 | – | – | informational | новая: /es/ams/comparison (после EN v2) |
| COOL Hub | refrigeracion para mineria | n/d везде | – / – / – / – / – | – | – | transactional | /es/asics-cooling |
| COOL Hub | enfriamiento mineria bitcoin | n/d везде | – / – / – / – / – | – | – | informational | /es/asics-cooling |
| COOL Hub | ruido antminer | n/d везде | – / – / – / – / – | – | – | informational | /es/asics-cooling |
| COOL Inmersión | refrigeracion por inmersion | ES, MX, AR, CO, VE | 70 / 40 / 20 / 10 / 10 | – | – | informational | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | refrigeracion por inmersion mineria | n/d везде | – / – / – / – / – | – | – | commercial | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | refrigeracion por inmersion asic | n/d везде | – / – / – / – / – | – | – | transactional | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | mineria por inmersion | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | 0.58 (ES) | – | informational | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | enfriamiento por inmersion | ES, MX, AR, CO, VE | 10 / 50 / 10 / 10 / 10 | 0.53 (MX) | 56/– | informational | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | tanque de inmersion | ES, MX, AR, CO, VE | 10 / 70 / 10 / 30 / 10 | – | – | transactional | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | tanque de inmersion mineria | n/d везде | – / – / – / – / – | – | – | transactional | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | liquido dielectrico mineria | n/d везде | – / – / – / – / – | – | – | informational | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | aceite dielectrico mineria | n/d везде | – / – / – / – / – | – | – | transactional | /es/asics-cooling/immersion-systems (дочистить перевод) |
| COOL Inmersión | liquido dielectrico | ES, MX, AR, CO, VE | 110 / 720 / 90 / 50 / 30 | 0.29 (MX) | 0/0 | informational | только LSI на immersion-systems: спрос в основном трансформаторный/промышленный |
| COOL Hidro | refrigeracion liquida asic | ES, AR, VE | 10 / 0 / 10 / 0 / 10 | – | – | transactional | /es/asics-cooling/hydro-systems (исправить «Hidroeléctrica») |
| COOL Hidro | refrigeracion liquida mineria | ES, MX, AR, VE | 10 / 10 / 10 / 0 / 10 | – | –/17 | transactional | /es/asics-cooling/hydro-systems (исправить «Hidroeléctrica») |
| COOL Hidro | antminer hydro | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | 0.15 (MX) | – | transactional | /es/asics-cooling/hydro-systems (исправить «Hidroeléctrica») |
| COOL Hidro | antminer s21 xp hydro | ES, MX, AR, CO, VE | 30 / 20 / 10 / 10 / 10 | 1.85 (MX) | – | navigational | /es/asics-cooling/hydro-systems (исправить «Hidroeléctrica») |
| COOL Contenedores | contenedor de mineria | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | – | – | transactional | новая: /es/products/container (сейчас 404), P2 |
| COOL Contenedores | contenedor mineria bitcoin | n/d везде | – / – / – / – / – | – | – | navigational | новая: /es/products/container (сейчас 404), P2 |
| PDU | pdu mineria | n/d везде | – / – / – / – / – | – | – | informational | /es/products/pdu (заполнить мета) |
| PDU | pdu para mineria | n/d везде | – / – / – / – / – | – | – | commercial | /es/products/pdu (заполнить мета) |
| PDU | pdu asic | n/d везде | – / – / – / – / – | – | – | informational | /es/products/pdu (заполнить мета) |
| PDU | pdu inteligente | ES, MX, AR, CO, VE | 10 / 20 / 10 / 10 / 10 | 1.29 (AR) | – | informational | /es/products/pdu (заполнить мета) |
| PDU | pdu administrable | ES, MX, AR, CO, VE | 10 / 10 / 10 / 10 / 10 | 0.92 (CO) | 26/– | navigational | /es/products/pdu (заполнить мета) |
| PDU | pdu 380v | n/d везде | – / – / – / – / – | – | – | transactional | /es/products/pdu (заполнить мета) |
| BRAND | bixbit | ES, MX, AR, CO, VE | 10 / 20 / 10 / 10 / 170 | 0.19 (VE) | – | transactional | /es (+ /es/ams/connect для «ams bixbit») |
| INFO общий (не коммерческий) | mineria de bitcoins | ES, MX, AR, CO, VE | 880 / 880 / 590 / 390 / 320 | 0.75 (ES) | 3/1 | informational | нет /es/blog (404) — P2 / не целевой |
| INFO общий (не коммерческий) | mineria bitcoin | n/d везде | – / – / – / – / – | – | – | informational | нет /es/blog (404) — P2 / не целевой |
| INFO общий (не коммерческий) | granja de mineria bitcoin | n/d везде | – / – / – / – / – | – | – | navigational | нет /es/blog (404) — P2 / не целевой |
| INFO общий (не коммерческий) | asic miner | ES, MX, AR, CO, VE | 320 / 260 / 110 / 110 / 70 | 0.75 (ES) | 14/0 | informational | нет /es/blog (404) — P2 / не целевой |
| INFO общий (не коммерческий) | minero asic | ES, MX, AR, CO, VE | 20 / 30 / 20 / 10 / 10 | 0.36 (ES) | 14/0 | informational | нет /es/blog (404) — P2 / не целевой |
| INFO общий (не коммерческий) | equipos asic | ES, MX, AR, CO, VE | 20 / 30 / 20 / 10 / 10 | 0.69 (ES) | – | commercial | нет /es/blog (404) — P2 / не целевой |
| INFO общий (не коммерческий) | antminer | ES, MX, AR, CO, VE | 480 / 480 / 210 / 210 / 320 | 0.85 (VE) | 0/0 | informational | LSI на /es/firmwares/* (запрос о железе, не о прошивке) |
| INFO общий (не коммерческий) | whatsminer | ES, MX, AR, CO, VE | 90 / 170 / 70 / 90 / 260 | 2.68 (ES) | 13/1 | informational | LSI на /es/firmwares/* (запрос о железе, не о прошивке) |

### 3.1. Ключи из GSC без измеренного объёма (есть показы, значит есть спрос)

| Ключ | Показы GSC 28 дн (VE+AR+CO+MX+ES) | Сейчас ранжируется | Целевой /es/ URL |
|---|---|---|---|
| whatsminer firmware | 746, 0 кликов | `/en/firmwares` поз. 5.2 (VE), `-m3x` поз. 4.2–4.3 (AR, CO) | `/es/firmwares/whatsminer-all-series` + `-m3x` (сначала перевод) |
| whatsminer tool descargar | 328 (всего по сайту 491) | EN-блог / EN-документация поз. 10–35 | новая: ES-глава «actualizar firmware con WhatsMinerTool» |
| antminer firmware / firmware antminer | 170 / 144 | `/en/firmwares/antminer` поз. 10–17 | `/es/firmwares/antminer` |
| mejor firmware para antminer s9 | 142 (всего 195) | `/en/firmwares`, `/en/firmwares/antminer` поз. 16–50; `/es/firmwares/antminer` поз. 23 | `/es/firmwares/antminer` (FAQ) → позже `/es/firmwares/comparison`. **[VERIFY: поддерживается ли S9 текущей прошивкой]** |
| descargar firmware antminer s9 | 88 (всего 120) | `/en/firmwares` поз. 31–44 | то же, [VERIFY: S9] |
| bixbit firmware | 112, 7 кликов (VE) | `/en/firmwares` поз. 1 | `/es/firmwares` |
| ams bixbit / bixbit ams | 186, 23 клика | `/en/ams` поз. 1; `/es/ams/connect` поз. 3 | `/es/ams` (продукт), `/es/ams/connect` (вход) |
| asic custom firmware / asic mining firmware | 18 / 13 (MX) | `/en/firmwares` поз. 5–9 | `/es/firmwares` (англоязычные формы в H2/тексте) |
| refrigeración para rig de minería | 18 | `/es/asics-cooling` поз. 35 | `/es/asics-cooling` |
| error whatsminer / whatsminer error code(s) | 14 (VE) + общемировые 111 | EN-страница кодов ошибок поз. 2 | новая: ES-страница кодов ошибок (P2, после P0-5 docs.bixbit.io) |
| donde puedo descargar el programa? / donde consigo | 3 / 2, по 1 клику | `/en/firmwares/whatsminer-series-m3x`, `/en/firmwares` | ответить в FAQ `/es/firmwares` («¿Dónde descargar el firmware?») |

### 3.2. Long-tail и LSI из Labs (MX / ES / VE)

Используются как LSI и H2/FAQ, не как отдельные страницы:
- **Модели Antminer** (спрос на железо, но это лексика аудитории): `antminer s21` (MX 170, ES 210, VE 90), `antminer s19 pro` (MX 140, ES 110), `antminer s19` (MX 110, ES 110, VE 140), `antminer s9` (MX 50, ES 70, VE 110), `antminer s21 pro`, `antminer s21 xp`, `antminer s19j pro`, `antminer s19 xp`, `antminer l7`, `antminer l9`, `antminer s19k pro`, `antminer s21 hyd`, `antminer s23 hyd 3u`. На странице упоминать только модели, реально поддерживаемые прошивкой **[VERIFY: список моделей]**.
- **Модели Whatsminer:** `whatsminer m30s` (MX 70), `whatsminer m50` (30), `whatsminer m20s`, `whatsminer m60` (по 10) → `-m3x`, `-m5x`, `-m2x`, `-m6x`.
- **Инструкционные:** `configurar antminer s9`, `como instalar antminer s9`, `instalacion electrica para antminer s9` (MX 50 — электрика, вне продукта), `antminer noise reduction` (MX 40), `ruido antminer`, `antminer repair`, `errores whatsminer`, `s9 firmware antminer` (VE 10).
- **Hydro:** `antminer s21 xp hydro` (ES 30, MX 20), `bitmain antminer s21 xp hydro` (ES 30, VE 20), `antminer s19 hydro`, `antminer hydro`, `antminer s19 xp hyd 255th` (ES 40) → LSI для `/es/asics-cooling/hydro-systems`.
- **Software:** `software de mineria` (MX 20; CPC ES $3.35, VE $9.09), `software para mineria` (CPC MX $2.48), `mejor software de mineria`, `software para mineria de criptomonedas` → LSI `/es/ams`. Осторожно: «minería» в испанском — это и горнодобывающая отрасль (`software para mineria subterranea`), поэтому всегда с «bitcoin/ASIC».

---

## 4. Карта «страница → основной и вторичные ключи»

| /es/ URL | Статус (2026-09-28) | Основной ключ | Вторичные | Кластер |
|---|---|---|---|---|
| `/es` | переведена, description есть (201 зн., длинный) | bixbit | software y hardware para minería de Bitcoin, firmware ASIC, refrigeración por inmersión | BRAND |
| `/es/firmwares` | переведена; пустой FAQPage | firmware asic | firmware personalizado asic, firmware para asic, bixbit firmware, asic custom firmware | FW-C |
| `/es/firmwares/antminer` | переведена | firmware antminer | antminer firmware, firmware para antminer, firmware antminer s19 / s21 / s9, overclock antminer, autotuning antminer, underclock / undervolt | FW-A, FW-B |
| `/es/firmwares/whatsminer-all-series` | **на EN**, H1 пустой | firmware whatsminer | whatsminer firmware, whatsminer tool | FW-D |
| `/es/firmwares/whatsminer-series-m2x` | **на EN** | firmware whatsminer m20s [n/d] | whatsminer m20s, m21s | FW-D |
| `/es/firmwares/whatsminer-series-m3x` | **на EN** | firmware whatsminer m30s | whatsminer m30s, m31s, m32 | FW-D |
| `/es/firmwares/whatsminer-series-m5x` | **на EN** | firmware whatsminer m50 | whatsminer m50, m53, m56 | FW-D |
| `/es/firmwares/whatsminer-series-m6x` | **на EN** | firmware whatsminer m60 [n/d] | whatsminer m60, m63, m66 | FW-D |
| `/es/ams` | переведена | monitoreo asic | software de monitoreo minería, software de minería, monitoreo de mineros | AMS |
| `/es/ams/connect` | переведена; H1 «Sí, tengo una cuenta» | ams bixbit (навигационный) | conectar AMS, clave API | BRAND |
| `/es/asics-cooling` | переведена, description пустой | refrigeración para minería | enfriamiento minería bitcoin, refrigeración para rig de minería | COOL |
| `/es/asics-cooling/immersion-systems` | смесь языков, description пустой | refrigeración por inmersión | refrigeración por inmersión minería / ASIC, tanque de inmersión, líquido dieléctrico | COOL |
| `/es/asics-cooling/hydro-systems` | смесь языков, H1 «Hidroeléctrica» (ошибка) | refrigeración líquida ASIC | antminer hydro, whatsminer hydro, refrigeración líquida minería | COOL |
| `/es/products/pdu` | title и description пустые | pdu minería | pdu inteligente, pdu administrable, pdu para minería | PDU |
| `/es/products/server` | тело на EN, H1 на EN | — (ES-спрос не измерен) | refrigeración por inmersión para servidores | COOL |
| `/es/documentation` | пустой хаб (55 слов), пустой FAQPage | — | — | DOC |
| `/es/faq` | переведена, description шаблонный (99 зн.) | — | comisión de desarrollo, firmware, AMS | — |

**Новые страницы (только после EN-версий архитектуры v2 и решения Q1 по /es/):**
`/es/firmwares/comparison` (FW-E), `/es/firmwares/dev-fee`, `/es/ams/comparison` (AMS-alt), `/es/documentation/<instalación de firmware Antminer>`, ES-главы WhatsMinerTool и кодов ошибок Whatsminer, `/es/products/container` (P2). Слаги — по EN-решению команды [VERIFY], hreflang строить из связи переводов в CMS, не подменой префикса.

---

## 5. Открытые вопросы и [VERIFY]

- [VERIFY] Поддерживает ли текущая прошивка Antminer S9 и L7/L9 (Scrypt): от этого зависит, можно ли таргетировать `mejor firmware para antminer s9`, `descargar firmware antminer s9`, `firmware antminer l7/l9`.
- [VERIFY] Список моделей Antminer и Whatsminer для title/H1/FAQ.
- [VERIFY] Показы VE/AR/CO похожи на автоматические (одинаковые числа в трёх странах).
- [VERIFY] Видео «Whatsminer M60. Firmware, Overclocking, Remote monitoring…» на YouTube (#4 в VE): канал BiXBiT? Если да, это ES-актив для перелинковки.
- Решение Q1 из `content/localization-plan.md` (публичная ли `/es/`, есть ли поддержка/sales на испанском) — блокер для всего плана.
