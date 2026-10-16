# Архитектура контента v2: расширяем живые URL вместо 45 новых страниц

**Дата:** 2026-09-25 · **Основа:** `reports/cluster-repriorization-2026-09-25.md` (объёмы DataForSEO, US/en) и находки competitor-gap от 2026-09-25 · **Кластеры:** Antminer, Whatsminer, Immersion, AMS (PDU в объём не входил)

## Итог

- **Было (v1):** 45 брифов, каждый — отдельный будущий URL (`/en/antminer-firmware/*`, `/en/whatsminer-firmware/*`, `/en/immersion-cooling-mining/*`, `/en/ams/<spoke>`). Ни один из этих URL не существует. При этом живые страницы уже ранжируются: `/en/firmwares/antminer` на #15, `-m3x` на #3, `/en/ams` на #7.
- **Стало (v2): 17 URL.**
  - **13 существующих** страниц расширяются новыми H2-секциями.
  - **4 новых** страницы — только под самостоятельные интенты.
  - По приоритетам: P0 — 7, P1 — 7, P2 — 3.
  - Вы просили «~20 страниц», получилось меньше: ещё 3 URL можно было бы добавить, только выделив секции без измеримого спроса, а это те самые тонкие страницы, от которых мы уходим.
- **Каждый из 45 брифов** теперь привязан к URL и секции. В каждый бриф добавлена строка `**Target (architecture v2, 2026-09-25):**`. Сами брифы остаются справочным материалом для авторов: ключи, структура, FAQ.

### Как решали: секция или новый URL

Отдельный URL получает только тема с **самостоятельным поисковым интентом**, то есть когда человек ищет именно её, а не подробность продукта. И только если есть хотя бы одно из трёх:
- (а) измеримый спрос,
- (б) доказанный GEO-разрыв,
- (в) формат, который не помещается в продуктовую страницу: пошаговая инструкция или таблица сравнения нескольких вендоров.

Всё остальное становится H2-секцией живой страницы. Так эти страницы набирают глубину, а не делят позиции с новыми.

## Три P0-темы из запроса: решение

| Тема | Решение | Почему |
|---|---|---|
| **Сравнение с конкурентами** | **Новый URL** `/en/firmwares/comparison` (P0). Одна страница для Antminer и Whatsminer | Самостоятельный интент: выбор между вендорами. Спрос идёт через бренды конкурентов (braiins os 210, vnish firmware 140). В GEO LLM отвечают на запросы-сравнения по сторонним страницам без BiXBiT (d-central, spark.money, EMCD). Многовендорная таблица внутри продуктовой страницы выглядела бы как самореклама |
| **Dev fee** | **Новый URL** `/en/firmwares/dev-fee` (P0). Сюда же безопасность и бэкдоры, для обеих платформ | Самостоятельный вопрос о цене и доверии. GEO: на запрос «lowest dev fee» ePIC называют в 4 из 5 движков, BiXBiT — ни в одном. Нужна одна каноническая страница, на которую будут ссылаться хабы, FAQ и llms.txt. Честная подача: 2.8% / 2% M2x [VERIFY], аргумент через TCO, без «lowest» |
| **Mineral oil** | **Отдельный URL уже есть**, нового не создаём: обновляем `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` (P1) | Информационный интент, отдельный от коммерческой страницы immersion-systems. BiXBiT уже на #1–5, это ~200/мес. Новый URL разделил бы накопленные позиции |

Ещё две новые страницы (P1):
- **`/en/documentation/antminer-firmware-install`** — пошаговая инструкция. Такой формат не вписывается в продуктовую страницу. ePIC стоит #7 с install-гайдом. Страница живёт в существующем разделе `/en/documentation`.
- **`/en/ams/comparison`** — выбор ПО для мониторинга: AMS против Minerstat, Braiins Manager, Luxor Commander и Hive OS. Три брифа-сравнения и бриф «how to choose» объединены в одну страницу. Только у запроса про Minerstat есть измеримый спрос (20/мес), но формат подборки нужен для GEO.

## Главная таблица: URL | тип | что добавляется | приоритет

| # | URL | Тип | Приоритет | Кластер | Что добавляется | Брифы → секции |
|---|---|---|---|---|---|---|
| 1 | `/en/firmwares` | существующий | **P0** | Прошивки (общее) | A canonical opening passage (Antminer + Whatsminer + AMS, one sentence reused in schema and llms.txt); a summary block on the transparent dev fee [VERIFY] linking to /en/firmwares/dev-fee; a supported-models table [VERIFY]; a real FAQPage in place of the empty mainEntity; links to comparison and dev-fee | — |
| 2 | `/en/firmwares/antminer` | существующий | **P0** | Antminer | H2 sections: what custom firmware is; S19 series; S21 / S21 Hydro; tuning modes (overclocking, undervolting, autotuning); install and update (summary + link to the guide); FAQ; SoftwareApplication schema. Secondary keyword: bitmain firmware | `antminer-firmware-pillar` (P0), `antminer-custom-firmware` (P2), `antminer-s19-firmware` (P1), `antminer-s21-firmware` (P1), `antminer-overclocking-firmware` (P2), `antminer-undervolting` (P2), `antminer-autotuning` (P2) |
| 3 | `/en/firmwares/whatsminer-all-series` | существующий | **P0** | Whatsminer | H2 sections: why third-party Whatsminer firmware (the category explainer); a series overview linking to m2x/m3x/m5x/m6x; tuning modes; FAQ; SoftwareApplication schema. Rule: don't remove 'whatsminer firmware' from -m3x until the hub is in the top 5 [VERIFY that the page is indexed; lastmod 2024-11] | `whatsminer-firmware-pillar` (P0), `whatsminer-custom-firmware` (P2), `whatsminer-overclocking-firmware` (P2), `whatsminer-undervolting` (P2), `whatsminer-autotuning` (P2) |
| 4 | `/en/asics-cooling/immersion-systems` | существующий | **P0** | Immersion | H2 sections: immersion for bitcoin mining (the pillar); Antminer and Whatsminer in immersion (models, firmware profiles [VERIFY]); single-phase vs two-phase; immersion vs air; tanks and system components; deployment steps; ROI/TCO (link to /en/calc, no profitability promises); data center deployments; FAQ; Product schema. Move 'immersion cooling mining' (#14 via a blog post) onto this page | `immersion-cooling-mining-pillar` (P0), `immersion-cooling-antminer` (P1), `immersion-cooling-whatsminer` (P2), `single-phase-immersion-cooling` (P1), `two-phase-immersion-cooling` (P2), `immersion-cooling-vs-air-cooling` (P2), `immersion-cooling-tank` (P2), `immersion-cooling-asic-setup` (P2), `immersion-cooling-roi` (P2), `immersion-cooling-data-center` (P2) |
| 5 | `/en/ams` | существующий | **P0** | AMS | H2 sections: Antminer + Whatsminer in one dashboard (a mixed fleet); Antminer monitoring and dashboard; Whatsminer monitoring; alerts and automation (remote reboot [VERIFY]); per-unit power monitoring [VERIFY]; multi-client for hosting providers [VERIFY]; fleet management at scale; the firmware link; SoftwareApplication schema + the existing FAQ. Secondary keyword: mining software (260) | `mining-fleet-monitoring-pillar` (P0), `antminer-monitoring-software` (P1), `mining-fleet-dashboard` (P2), `whatsminer-monitoring-software` (P1), `mining-farm-alerts-automation` (P2), `mining-farm-power-monitoring` (P2), `mining-hosting-monitoring` (P2), `asic-fleet-management` (P2) |
| 6 | `/en/firmwares/comparison` | **новый** | **P0** | Прошивки (общее) | A new page: an HTML comparison table (fee, models, autotuning, Whatsminer support, monitoring) with every competitor figure [VERIFY]; decision framework; FAQ. Standalone intent: commercial comparison and GEO comparison prompts, plus competitor brand demand (braiins os 210, vnish firmware 140) | `antminer-firmware-comparison` (P0), `whatsminer-firmware-comparison` (P1) |
| 7 | `/en/firmwares/dev-fee` | **новый** | **P0** | Прошивки (общее) | A new page: what a dev fee is and how it's charged; BiXBiT's fee by series [VERIFY: 2.8% / 2% M2x]; TCO calculation (efficiency gain minus fee), no 'lowest fee' claim; security (no backdoor, how to check) [VERIFY]; FAQ. Standalone intent: pricing and trust question, GEO 'lowest dev fee' (ePIC 4/5, BiXBiT 0/5) | `antminer-firmware-security` (P0), `whatsminer-firmware-security` (P1) |
| 8 | `/en/firmwares/whatsminer-series-m3x` | существующий | **P1** | Whatsminer | H2 sections: M30S/M30S+/M30S++ modes table [VERIFY]; efficiency and tuning for the M3x; FAQ. Keep the current ranking and add a link to the hub | `whatsminer-m30s-firmware` (P1) |
| 9 | `/en/firmwares/whatsminer-series-m5x` | существующий | **P1** | Whatsminer | H2 sections: M50/M50S/M53 modes [VERIFY]; immersion/hydro notes; FAQ | `whatsminer-m50-firmware` (P1) |
| 10 | `/en/firmwares/whatsminer-series-m6x` | существующий | **P1** | Whatsminer | H2 sections: M60/M60S/M63 modes [VERIFY]; immersion and hydro profiles; FAQ | — |
| 11 | `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` | существующий | **P1** | Immersion | Refresh: current fluid types table [VERIFY], mineral oil vs synthetic vs engineered fluids, an Antminer-in-mineral-oil section, updated date; a link to immersion-systems. This post already has its own URL, so no new page | `immersion-cooling-dielectric-fluid` (P1) |
| 12 | `/en/blog/post/how-does-immersion-cooling-work` | существующий | **P1** | Immersion | Refresh: definition, how it works, single/two-phase at a glance; a CTA link to immersion-systems | — |
| 13 | `/en/documentation/antminer-firmware-install` | **новый** | **P1** | Antminer | A new documentation page: web UI / SD card / batch fleet install, update, rollback and recovery; HowTo schema. Standalone intent: step-by-step instructions (ePIC ranks #7 with an install guide). URL fits the existing /en/documentation section [VERIFY with the team] | `antminer-firmware-install` (P1), `antminer-firmware-update` (P2) |
| 14 | `/en/ams/comparison` | **новый** | **P1** | AMS | A new page: how to choose monitoring software (criteria); a comparison table with every competitor figure [VERIFY]; an 'alternatives' section (minerstat alternative 10, minerstat vs 10). Standalone intent: choosing and comparing vendors, GEO best-of-list queries | `mining-farm-monitoring-software` (P1), `ams-vs-minerstat` (P1), `ams-vs-braiins-manager` (P2), `ams-vs-luxor-commander` (P2) |
| 15 | `/en/firmwares/whatsminer-series-m2x` | существующий | **P2** | Whatsminer | Dev fee fact (2% on M2x [VERIFY]) and a link to the hub. Nothing else | — |
| 16 | `/en/documentation/user-guide-for-whatsminer-asic` | существующий | **P2** | Whatsminer | Sections: install custom firmware, update, rollback; a link to the hub | `whatsminer-firmware-install` (P2), `whatsminer-firmware-update` (P2) |
| 17 | `/en/asics-cooling` | существующий | **P2** | Immersion | A short immersion vs hydro vs air comparison block and links to immersion-systems / hydro-systems. Adding it to the sitemap is a separate technical task | — |

## Порядок работ

1. **P0, первые 2–4 недели:**
   - `/en/firmwares` — каноническая фраза, блок dev fee, исправление пустого FAQPage. Мало работы, эффект сразу.
   - `/en/firmwares/antminer` — пиллар: секции S19, S21 и tuning.
   - `/en/firmwares/dev-fee` — новая страница.
   - `/en/firmwares/comparison` — новая страница.
   - `/en/firmwares/whatsminer-all-series` — хаб.
   - `/en/asics-cooling/immersion-systems` — пиллар.
   - `/en/ams` — пиллар.
2. **P1, 30–60 дней:**
   - серийные страницы `-m3x`, `-m5x`, `-m6x`;
   - обновление двух блог-постов про immersion;
   - `/en/documentation/antminer-firmware-install`;
   - `/en/ams/comparison`.
3. **P2:** `-m2x`, `/en/asics-cooling`, секции в Whatsminer user guide, P2-секции внутри P0-страниц (углублять по данным GSC).

## Риски и что проверить [VERIFY]

- **Каннибализация Whatsminer.** Сейчас по `whatsminer firmware` ранжируется `-m3x` (#3), а хабом становится `-all-series`. Правило: не убирать «whatsminer firmware» из `-m3x`, пока хаб не войдёт в топ-5. Отдельно проверить, что `-all-series` индексируется (lastmod 2024-11, на 09-16 не перепроверялась).
- **Длинные страницы.** На `/en/firmwares/antminer`, `/en/asics-cooling/immersion-systems` и `/en/ams` будет по 6–9 H2-секций. Нужны оглавление, якоря (id фрагментов утвердить с dev) и сворачиваемые FAQ. Вес страницы Antminer (23.8 MB) — отдельный P0 из тех-отчёта. Если сжать картинки, лишний текст на скорость почти не повлияет.
- **Старые noindex-страницы моделей** (`/en/firmwares/asic-s19` и т.п.). v2 это решение поддерживает: модели собираются в хабе. Нужно подтвердить, что так задумано. Как вариант, заменить noindex на 301 в `#s19`.
- **Новые URL** (`/en/firmwares/comparison`, `/en/firmwares/dev-fee`, `/en/documentation/antminer-firmware-install`, `/en/ams/comparison`) — согласовать слаги с командой и CMS.
- **Все технические факты** — модели, режимы, J/TH, dev fee, данные конкурентов — остаются с `[VERIFY]`.

## Соответствие брифов (v1 → v2)

| Бриф | Было (v1) | Стало (v2) | Секция | Приоритет секции |
|---|---|---|---|---|
| `mining-fleet-monitoring-pillar` | `/en/ams` | `/en/ams` | Main page content (pillar) | P0 |
| `antminer-monitoring-software` | `/en/ams/antminer-monitoring-software` | `/en/ams` | H2 Antminer monitoring and dashboard | P1 |
| `whatsminer-monitoring-software` | `/en/ams/whatsminer-monitoring-software` | `/en/ams` | H2 Whatsminer monitoring (mixed fleet) | P1 |
| `mining-fleet-dashboard` | `/en/ams/mining-fleet-dashboard` | `/en/ams` | H2 Antminer monitoring and dashboard (dashboard part) | P2 |
| `mining-farm-alerts-automation` | `/en/ams/mining-farm-alerts-automation` | `/en/ams` | H2 Alerts and automation | P2 |
| `mining-farm-power-monitoring` | `/en/ams/mining-farm-power-monitoring` | `/en/ams` | H2 Per-unit power monitoring | P2 |
| `mining-hosting-monitoring` | `/en/ams/mining-hosting-monitoring` | `/en/ams` | H2 Multi-client for hosting providers | P2 |
| `asic-fleet-management` | `/en/ams/asic-fleet-management` | `/en/ams` | H2 Fleet management at scale | P2 |
| `mining-farm-monitoring-software` | `/en/ams/mining-farm-monitoring-software` | `/en/ams/comparison` | H2 How to choose monitoring software | P1 |
| `ams-vs-minerstat` | `/en/ams/vs-minerstat` | `/en/ams/comparison` | H2 AMS vs Minerstat | P1 |
| `ams-vs-braiins-manager` | `/en/ams/vs-braiins-manager` | `/en/ams/comparison` | H2 AMS vs Braiins Manager | P2 |
| `ams-vs-luxor-commander` | `/en/ams/vs-luxor-commander` | `/en/ams/comparison` | H2 AMS vs Luxor Commander | P2 |
| `immersion-cooling-mining-pillar` | `/en/immersion-cooling-mining` | `/en/asics-cooling/immersion-systems` | Main page content (pillar) | P0 |
| `immersion-cooling-antminer` | `/en/immersion-cooling-mining/antminer` | `/en/asics-cooling/immersion-systems` | H2 Antminer and Whatsminer in immersion | P1 |
| `single-phase-immersion-cooling` | `/en/immersion-cooling-mining/single-phase` | `/en/asics-cooling/immersion-systems` | H2 Single-phase vs two-phase | P1 |
| `immersion-cooling-whatsminer` | `/en/immersion-cooling-mining/whatsminer` | `/en/asics-cooling/immersion-systems` | H2 Antminer and Whatsminer in immersion (Whatsminer part) | P2 |
| `two-phase-immersion-cooling` | `/en/immersion-cooling-mining/two-phase` | `/en/asics-cooling/immersion-systems` | H2 Single-phase vs two-phase (two-phase part) | P2 |
| `immersion-cooling-vs-air-cooling` | `/en/immersion-cooling-mining/vs-air-cooling` | `/en/asics-cooling/immersion-systems` | H2 Immersion vs air (short version also on /en/asics-cooling) | P2 |
| `immersion-cooling-tank` | `/en/immersion-cooling-mining/tank` | `/en/asics-cooling/immersion-systems` | H2 Tanks and system components | P2 |
| `immersion-cooling-asic-setup` | `/en/immersion-cooling-mining/setup-guide` | `/en/asics-cooling/immersion-systems` | H2 Deployment steps | P2 |
| `immersion-cooling-roi` | `/en/immersion-cooling-mining/roi` | `/en/asics-cooling/immersion-systems` | H2 ROI / TCO (link to /en/calc) | P2 |
| `immersion-cooling-data-center` | `/en/immersion-cooling-mining/data-center` | `/en/asics-cooling/immersion-systems` | H2 Data center deployments | P2 |
| `immersion-cooling-dielectric-fluid` | `/en/immersion-cooling-mining/dielectric-fluid` | `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` | Refresh the existing post | P1 |
| `antminer-firmware-install` | `/en/antminer-firmware/install` | `/en/documentation/antminer-firmware-install` | Main page content (new how-to) | P1 |
| `antminer-firmware-update` | `/en/antminer-firmware/update` | `/en/documentation/antminer-firmware-install` | H2 Update and rollback | P2 |
| `whatsminer-firmware-install` | `/en/whatsminer-firmware/install` | `/en/documentation/user-guide-for-whatsminer-asic` | H2 Install custom firmware | P2 |
| `whatsminer-firmware-update` | `/en/whatsminer-firmware/update` | `/en/documentation/user-guide-for-whatsminer-asic` | H2 Update and rollback | P2 |
| `antminer-firmware-pillar` | `/en/antminer-firmware` | `/en/firmwares/antminer` | Main page content (pillar) | P0 |
| `antminer-s19-firmware` | `/en/antminer-firmware/antminer-s19` | `/en/firmwares/antminer` | H2 Antminer S19 series | P1 |
| `antminer-s21-firmware` | `/en/antminer-firmware/antminer-s21` | `/en/firmwares/antminer` | H2 Antminer S21 / S21 Hydro | P1 |
| `antminer-custom-firmware` | `/en/antminer-firmware/custom` | `/en/firmwares/antminer` | H2 What is custom Antminer firmware | P2 |
| `antminer-overclocking-firmware` | `/en/antminer-firmware/overclocking` | `/en/firmwares/antminer` | H2 Tuning modes → overclocking | P2 |
| `antminer-undervolting` | `/en/antminer-firmware/undervolting` | `/en/firmwares/antminer` | H2 Tuning modes → undervolting | P2 |
| `antminer-autotuning` | `/en/antminer-firmware/autotuning` | `/en/firmwares/antminer` | H2 Tuning modes → autotuning | P2 |
| `antminer-firmware-comparison` | `/en/antminer-firmware/comparison` | `/en/firmwares/comparison` | Main page content (new page), Antminer part | P0 |
| `whatsminer-firmware-comparison` | `/en/whatsminer-firmware/comparison` | `/en/firmwares/comparison` | Whatsminer column/section of the comparison page | P1 |
| `antminer-firmware-security` | `/en/antminer-firmware/security` | `/en/firmwares/dev-fee` | Main page content (new page) | P0 |
| `whatsminer-firmware-security` | `/en/whatsminer-firmware/security` | `/en/firmwares/dev-fee` | Whatsminer section of the dev-fee page | P1 |
| `whatsminer-firmware-pillar` | `/en/whatsminer-firmware` | `/en/firmwares/whatsminer-all-series` | Main page content (hub) | P0 |
| `whatsminer-custom-firmware` | `/en/whatsminer-firmware/custom` | `/en/firmwares/whatsminer-all-series` | H2 Why third-party Whatsminer firmware | P2 |
| `whatsminer-overclocking-firmware` | `/en/whatsminer-firmware/overclocking` | `/en/firmwares/whatsminer-all-series` | H2 Tuning modes → overclocking | P2 |
| `whatsminer-undervolting` | `/en/whatsminer-firmware/undervolting` | `/en/firmwares/whatsminer-all-series` | H2 Tuning modes → undervolting | P2 |
| `whatsminer-autotuning` | `/en/whatsminer-firmware/autotuning` | `/en/firmwares/whatsminer-all-series` | H2 Tuning modes → autotuning | P2 |
| `whatsminer-m30s-firmware` | `/en/whatsminer-firmware/whatsminer-m30s` | `/en/firmwares/whatsminer-series-m3x` | Page content (M3x series) | P1 |
| `whatsminer-m50-firmware` | `/en/whatsminer-firmware/whatsminer-m50` | `/en/firmwares/whatsminer-series-m5x` | Page content (M5x); the M60 part goes to /en/firmwares/whatsminer-series-m6x | P1 |

## Какие файлы изменены

- `content/clusters/*.md` (4 файла): в начало каждого добавлена секция **«Architecture v2 (2026-09-25): authoritative»** — таблица URL, приоритеты, секции из брифов и порядок работ. Старые Hub/Spoke-списки, порядок производства и кросс-кластерные таблицы помечены как *superseded*. Сами разделы оставлены: в них ключи и структура для авторов.
- `content/internal-linking.md`: добавлена **«Architecture v2 — Linking Matrix»** — 40 обязательных ссылок (Firmware F1–F24, Cooling C1–C10, AMS A1–A6), правила для якорей и проверка входящих ссылок на новые страницы. Матрицы v1 помечены как *superseded*.
- `content/briefs/*.md` (45): добавлена строка `Target (architecture v2)`. Заодно в 4 брифах (whatsminer-firmware-pillar, antminer-firmware-comparison, whatsminer-firmware-security, antminer-firmware-security) остались подсказки в VERIFY-пометках, которые подталкивали авторов писать про «0% dev fee». Их тоже заменил на «transparent dev fee [VERIFY: 2.8% / 2% M2x]».
- `content/geo/entity-definition-homepage.md`: 3 места с «no dev fee» / «0%» заменены на «transparent dev fee [VERIFY: 2.8% / 2% M2x]».
- Коммита не было. Всё видно в `git diff content/`.
