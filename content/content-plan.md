# Контент-план BiXBiT — Q4 2026 (октябрь–декабрь)

**Создан:** 2026-09-28 · **Владелец:** content-seo · **Сайт:** https://bixbit.io/en (US B2B English)
**Статус:** черновик, приоритеты и слаги утверждает команда (см. §5).
**Обновлять:** ежемесячно (IMPLEMENTATION.md, «Monthly content plan»), после каждого `/rank-check`.

**Источники (только они, чисел со стороны нет):**
- Архитектура v2 (17 URL): `reports/content-architecture-2026-09-25.md`, матрица ссылок: `content/internal-linking.md` → «Architecture v2 — Linking Matrix»
- Приоритеты: `reports/cluster-repriorization-2026-09-25.md`, `content/clusters/*.md`, строки **Priority:** / **Target (architecture v2)** в `content/briefs/*.md`
- Позиции и CTR: `reports/rank-tracking-baseline-2026-09-25.md` (SERP 2026-09-28 + GSC §6), `data/rank-tracking/keywords.md`
- GSC: `data/gsc-queries-pages-us-2026-09-28.json`, `data/gsc-countries-2026-09-28.json`, `data/gsc-queries-all-2026-09-28.json` (окно 2026-08-29..09-25)
- GA4: `data/ga4-organic-landing-2026-09-28.json`, `data/ga4-channels-2026-09-28.json` (окно 2026-08-31..09-27)
- Bing: `reports/bing-webmaster-baseline-2026-09-28.md` · Конкуренты: `reports/competitor-gap-summary-2026-09-25.md`
- Текущие title/description: `data/page-snapshot-2026-09-28.json` · Черновики мета от 2026-09-16: `content/page-optimize/{firmwares,ams,homepage}.md`

> **Оговорка по GSC.** Цифры «по странице» ниже — сумма пар «запрос–страница». Этот разрез не включает анонимизированные запросы, поэтому реальные итоги по страницам выше. Итог по стране (US 23 697 показов → 76 кликов) взят из разреза `country`. Первая задача W0: снять разрез `page`.

---

## 1. Цель квартала

**Забрать клики с позиций, которые у нас уже есть, и довести P0-страницы архитектуры v2 до рабочего состояния.** Объём спроса в US маленький: у 251 из 308 ключей объём n/d. Поэтому квартал начинается с CTR (правки title и description) и с углубления живых URL. Новых страниц всего 4.

Логика по месяцам:
1. **Октябрь.** Сначала CTR: правим title/description страниц, которые уже в топ-10. Затем ставим CTA на страницах кодов ошибок Whatsminer, чиним хаб `/en/firmwares` и выпускаем первую новую страницу (`dev-fee`).
2. **Ноябрь.** P0-пиллары: Antminer, сравнение прошивок, AMS, Whatsminer-хаб, immersion.
3. **Декабрь.** P1: серийные страницы Whatsminer, обновление двух постов про immersion, гайд по установке, сравнение AMS. P2 уходит в бэклог Q1.

### 1.1 Метрики успеха

Baseline взят из файлов выше. Колонка «Ориентир Q4» — это **предложение**, не прогноз. Её утверждает команда.

| Метрика | Baseline (дата, источник) | Ориентир Q4 (предложение) |
|---|---|---|
| US: показы → клики, CTR (28 дн, разрез country) | 23 697 → 76, **CTR 0.32%**, ср. поз. 14.0 (GSC 08-29..09-25) | CTR ≥ 0.8%, клики ≥ 150 / 28 дн |
| Все страны: показы → клики, CTR | 113 155 → 2 263, CTR 2.0% | рост кликов без падения CTR |
| Клики по 4 CTR-страницам (US, сумма по запросам) | `/en/firmwares` 3 / 1 545; `-m3x` 0 / 732; `/en/ams` 2 / 612; `-m2x` 0 / 551 | ≥ 1% CTR на каждой через 28 дн после деплоя |
| Небрендовые клики по отслеживаемым ключам с показами | **0** по всем 16 (включая топ-5) | ≥ 1 клик на ключах в топ-5 |
| Rank tracking (30 ключей, Google US) | найден 17; топ-3 — 2; топ-10 — 10; #11–20 — 6 (SERP 09-28) | найден ≥ 20; топ-10 ≥ 12 |
| `antminer firmware` (CPC $70.51) | SERP #8 (GSC 23.6) · `/en/firmwares/antminer` | топ-5 |
| `bitmain firmware` | SERP #17 | топ-10 |
| `whatsminer firmware` / `whatsminer custom firmware` | #4 / #2 | защита: не ниже топ-5 / топ-3 |
| `asic monitoring software` (не отслеживается, кандидат) | GSC 4.8 (запрос), `/en/ams` 3.0 | удержать топ-5, получить клики |
| `immersion cooling mining` | #12, ранжируется блог, не `/en/asics-cooling/immersion-systems` (у неё 1 показ в US) | в выдаче коммерческая страница |
| Новые страницы (4) | не существуют | опубликованы, проиндексированы, ≥ 3 входящих ссылки у каждой |
| GA4 **AI Assistant** (GEO-метрика) | **68 сессий** / 34 engaged / 28 дн | рост в динамике (ориентир ≥ 100 / 28 дн) |
| GA4 органика | 2 877 сессий / 28 дн (2.7% всех сессий) | рост |
| Страницы кодов ошибок Whatsminer → переходы на прошивку/AMS | не измеряется (keyEvents: en 2, ru 13 — метрике не доверяем) | событие клика по CTA настроено, есть baseline |
| GEO: ChatGPT цитирует bixbit.io | 0/11; «lowest dev fee»: BiXBiT 0/5 (competitor-gap 09-25) | ≥ 1 цитирование (замер — `geo-ai`, `/geo-check`) |

---

## 2. Допущения по нагрузке

- **Мощность: 2–3 единицы контента в неделю.** Это допущение: реальная мощность команды не известна. Пересчитать план, когда она будет известна.
- **Единица (ед.)** — одно из:
  - пакет правки title и description для 1–2 страниц;
  - одна H2-секция на живой странице (примерно 400–800 слов);
  - обновление одного блог-поста.
  - Новая страница — это 3–4 ед., растянутые на 2 недели (черновик → [VERIFY] → публикация и входящие ссылки).
- **[VERIFY] у инженеров занимает около 1 недели** (допущение). Поэтому черновик и публикация страниц с тех-фактами разнесены на разные недели.
- **Деплой — через dev.** Задачи, которые зависят от шаблонов (FAQPage, sitemap, вес страницы, hreflang), ведёт `technical-seo`. Здесь они указаны только как зависимости.
- **Праздники:** US Thanksgiving (26 ноября) и 21 декабря – 3 января. На эти недели заложена сниженная нагрузка (допущение).
- **Метрики измерять не раньше чем через 14 дней после деплоя** (CTR — на 28-дневном окне). Лаг GSC — 3 дня.

---

## 3. План по месяцам

Колонки: **Тип** — правка (мета, CTA, ссылки; без нового текста) / обновление (новые секции или рефреш живого URL) / новая (новый URL из v2). **Ключ** — целевой; в скобках текущая позиция: SERP 09-28 или GSC (средняя по показам, US). ID ссылок (F/C/A) — из `content/internal-linking.md`.

### Октябрь — месяц 1: CTR + быстрые P0

| Неделя | Задача | URL | Тип | Целевой ключ | P | Бриф | Зависимость / [VERIFY] |
|---|---|---|---|---|---|---|---|
| **W0** (1–4 окт) | Подготовка (0 ед.): снять GSC по страницам (US и все страны); отправить команде вопросы из §5 (слаги, ставка dev fee, RU) | — | — | — | P0 | — | `./scripts/gsc-query.py --days 28 --dimensions page --country usa --out data/gsc-pages-us-YYYY-MM-DD.json` |
| **W1** (5–11 окт) | **Title и description** (1 ед.). Сейчас: «BiXBiT Custom ASIC Mining Firmware» (34 симв.). Отдельные запросы на странице: asic firmware 94 показа / поз. 4.7, asic custom firmware 52 / 6.6, whatsminer custom firmware 50 / **2.0**, custom firmware for miner 37 / 5.3 — везде 0 кликов | `/en/firmwares` | правка | asic firmware · custom firmware for ASIC miners | **P0** | `content/page-optimize/firmwares.md` (черновик 09-16 без GSC: обновить под эти запросы) | В текущем description: «up to 80 Th/s», «10-20%» → `[VERIFY: цифры]`. Dev fee — только «transparent dev fee» `[VERIFY: current rate with the team]`. Не каннибализировать `/en/firmwares/antminer` |
| W1 | **Title и description** (0.5 ед.). Запросы: whatsminer firmware 64 / **3.9**, whatsminer firmware update 39 / 4.3, whatsminer download 32 / 4.4, whatsminer tool download 37 / 6.1 — 0 кликов | `/en/firmwares/whatsminer-series-m3x` | правка | whatsminer firmware · whatsminer m3 firmware | **P0** | нет, сделать через `/page-optimize` | **SXO:** запросы «whatsminer tool …» — вероятно, ищут официальную утилиту MicroBT. Сниппет должен честно говорить, что есть на странице `[VERIFY: есть ли там загрузка/инструкция WhatsMinerTool]`. «whatsminer firmware» из title не убирать (правило v2). Цифра «130 Th/s» в description → `[VERIFY]` |
| W1 | **Title и description** (0.5 ед.). Запросы: asic monitoring software 73 / **3.0**, asic management software 54 / 4.3, asic miner monitoring software 52 / 6.1, asic monitoring 91 / 9.6 | `/en/ams` | правка | asic monitoring software · mining monitoring software | **P0** | `content/page-optimize/ams.md` (черновик 09-16: обновить под GSC) | «try it free» в черновике — `[VERIFY: AMS бесплатный / trial / платный]`. До подтверждения — нейтральный CTA |
| **W2** (12–18 окт) | **Title и description** (0.5 ед.). Запросы: whatsminer m20s firmware 30 / **2.0**, m21s firmware 27 / 2.1, m20s firmware download 36 / 2.1, m21s firmware download 30 / 3.8, whatsminer immersion firmware 27 / 5.6 — 0 кликов | `/en/firmwares/whatsminer-series-m2x` | правка | whatsminer m20s firmware · m21s firmware | P1 | нет, `/page-optimize` | Факт про dev fee для M2x (2%) `[VERIFY: current rate]` — это вся P2-правка v2 (#15). В description «Free M20s immersion…» и «90 Th/s» → `[VERIFY]` |
| W2 | **Хаб прошивок, контент** (1 ед.): каноническая вступительная фраза (Antminer + Whatsminer + AMS, та же формулировка для schema и llms.txt); блок-сводка «transparent dev fee»; таблица поддерживаемых моделей; настоящий FAQ; ссылки F2, F3 | `/en/firmwares` | обновление | custom firmware for ASIC miners | **P0** | `content/page-optimize/firmwares.md` + архитектура v2, строка 1 | Пустой `FAQPage` на странице — задача `technical-seo`. Модели `[VERIFY]`, dev fee `[VERIFY]`. Ссылки F4 и F5 ставить после выхода comparison / dev-fee |
| W2 | **CTA и перелинковка на странице кодов ошибок** (1 ед., спецификация в §4): контекстные CTA по группам ошибок → прошивка Whatsminer и AMS | `/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1` | правка | whatsminer error codes (поз. ~2 по всем странам) | **P0** | нет, §4 этого плана | Топ органических посадочных: GA4 221 сессия, engagement 47%, keyEvents 2. Bing: 124 показа. Пустой `FAQPage` здесь — `technical-seo`. Функции AMS в тексте CTA `[VERIFY]`. Нужно событие клика по CTA в GA4 (dev) |
| **W3** (19–25 окт) | **Новая страница про dev fee: черновик** (2 ед.). Что такое dev fee и как его списывают; ставка BiXBiT по сериям; TCO (прирост эффективности минус комиссия), без слова «lowest»; безопасность (бэкдоры, как проверить); FAQ | `/en/firmwares/dev-fee` | новая | antminer dev fee firmware (#5 сейчас через `/en/firmwares`) · antminer firmware security (#8, частичная выдача) | **P0** | `content/briefs/antminer-firmware-security.md` + `content/briefs/whatsminer-firmware-security.md` (секция Whatsminer, P1) | **Слаг `[VERIFY]` у команды.** Ставка 2.8% / 2% M2x `[VERIFY: current rate with the team]`. **Никогда «no dev fee»**. Заявления о безопасности `[VERIFY]` у инженеров. GEO: у ePIC 4/5, у BiXBiT 0/5 |
| W3 | **CTA на RU-странице кодов ошибок** (0.5 ед.) — зеркало W2 | `/ru/documentation/kody-oshibok-dlia-whatsminer-asic/spisok-oshibok-i-sposoby-resheniia` | правка | ошибки whatsminer | P1 | нет, §4 | **Зависит от решения по RU (§5, вопрос 1).** GA4: 198 сессий, engagement 33%. По всем странам запросы «ошибки whatsminer / ватсмайнер / вотсмайнер» дают поз. 2–3 и 61 клик. Если RU не в приоритете — только ссылки на `/ru/firmwares` и `/ru/ams`, без нового текста |
| **W4** (26 окт – 1 ноя) | **Публикация dev-fee** + входящие ссылки F5, F7, F15, F24 (≥ 3) (1 ед.) | `/en/firmwares/dev-fee` | новая | см. W3 | **P0** | как в W3 | После [VERIFY] инженеров. Обновить target в `data/rank-tracking/keywords.md` (§6.3) |
| W4 | **Пиллар Antminer, часть 1** (2 ед.): вступление; H2 «Antminer S19 series»; H2 «Antminer S21 / S21 Hydro». Вторичный ключ bitmain firmware; при необходимости добавить его в title. GSC: antminer firmware 60 / 22.1, firmware antminer 48 / 20.6, antminer s19 firmware 45 / 15.2, antminer s19 overclock 29 / 16.8, antminer t19 firmware 28 / 13.6 | `/en/firmwares/antminer` | обновление | antminer firmware (#8) · bitmain firmware (#17) · antminer s19 firmware (#8) · antminer s21 firmware (короткая выдача, GSC 22.3) | **P0** | `content/briefs/antminer-firmware-pillar.md`, `content/briefs/antminer-s19-firmware.md` (P1), `content/briefs/antminer-s21-firmware.md` (P1) | Режимы, хешрейт, J/TH и совместимость моделей — `[VERIFY]`, не сочинять. Вес страницы 23.8 MB — P0 `technical-seo`, идёт параллельно. Якоря `#s19`, `#s21` согласовать с dev |

**Октябрь, нагрузка:** W1 2 ед. · W2 2.5 ед. · W3 2.5 ед. · W4 3 ед.

### Ноябрь — месяц 2: P0-пиллары и сравнение

| Неделя | Задача | URL | Тип | Целевой ключ | P | Бриф | Зависимость / [VERIFY] |
|---|---|---|---|---|---|---|---|
| **W5** (2–8 ноя) | **Пиллар Antminer, часть 2** (1.5 ед.): H2 «What is custom Antminer firmware»; H2 «Tuning modes» (overclocking + undervolting + autotuning одной секцией); FAQ; правка существующей SoftwareApplication (diff, а не с нуля); ссылки F8–F11 | `/en/firmwares/antminer` | обновление | custom firmware antminer (#5) · antminer custom firmware (GSC 10.3) | **P0** (секции P2) | `content/briefs/antminer-custom-firmware.md`, `content/briefs/antminer-overclocking-firmware.md`, `content/briefs/antminer-undervolting.md`, `content/briefs/antminer-autotuning.md` | Все цифры по режимам `[VERIFY]`. F8 ставить после выхода install-гайда (W10); до этого — ссылка на документацию |
| W5 | **Страница-сравнение прошивок: черновик** (1.5 ед.): HTML-таблица (fee, модели, autotuning, поддержка Whatsminer, мониторинг); схема выбора; FAQ | `/en/firmwares/comparison` | новая | antminer firmware comparison (#11 через `/antminer`) · best antminer custom firmware · braiins os (210/мес, нет в топ-100) · vnish firmware (140/мес) | **P0** | `content/briefs/antminer-firmware-comparison.md`, `content/briefs/whatsminer-firmware-comparison.md` (P1) | **Слаг `[VERIFY]`.** Все данные конкурентов (Braiins OS+, Vnish, LuxOS, ePIC) — `[VERIFY]` по их документации с датой. Своя комиссия — «transparent dev fee» `[VERIFY]` |
| **W6** (9–15 ноя) | **Публикация сравнения** + входящие F4, F6, F14, F20, F22, F24 (≥ 3) (1 ед.) | `/en/firmwares/comparison` | новая | см. W5 | **P0** | как в W5 | Обновить target у 4 ключей в `keywords.md` (§6.3) |
| W6 | **Пиллар AMS** (2 ед.): H2 «Antminer + Whatsminer in one dashboard»; H2 «Antminer monitoring and dashboard»; H2 «Whatsminer monitoring». Вторичные ключи: mining software, mining monitoring software; ссылки A3, F9, F16 | `/en/ams` | обновление | asic monitor (GSC 7.5) · mining software (260, CPC $39.51, нет в топ-100) · mining monitoring software (нет в топ-100) | **P0** (секции P1) | `content/briefs/mining-fleet-monitoring-pillar.md`, `content/briefs/antminer-monitoring-software.md`, `content/briefs/whatsminer-monitoring-software.md`, `content/briefs/mining-fleet-dashboard.md` (P2) | Функции AMS (поддерживаемые модели, алерты, remote reboot) `[VERIFY]`. Не потерять то, что уже работает: `asic monitoring*` в топ-10 |
| **W7** (16–22 ноя) | **Хаб Whatsminer** (1.5 ед.): H2 «Why third-party Whatsminer firmware»; обзор серий со ссылками на m2x / m3x / m5x / m6x (F12); «Tuning modes»; FAQ; ссылки F14, F15, F16 | `/en/firmwares/whatsminer-all-series` | обновление | whatsminer firmware (хаб; сейчас ранжируется `-m3x` #4) · whatsminer tool (#10) | **P0** | `content/briefs/whatsminer-firmware-pillar.md`, `content/briefs/whatsminer-custom-firmware.md`, `content/briefs/whatsminer-overclocking-firmware.md`, `content/briefs/whatsminer-undervolting.md`, `content/briefs/whatsminer-autotuning.md` | Хаб почти невидим: около 65 показов в US, поз. 59–91. `[VERIFY: индексируется ли, lastmod 2024-11]` — проверить до написания. **Не убирать «whatsminer firmware» с `-m3x`**, пока хаб не в топ-5 |
| W7 | **Пиллар immersion, часть 1** (1.5 ед.): H2 «Immersion cooling for bitcoin mining»; H2 «Antminer and Whatsminer in immersion»; H2 «Single-phase vs two-phase» | `/en/asics-cooling/immersion-systems` | обновление | immersion cooling mining (#12, сейчас ранжируется блог) · asic immersion cooling (нестабильно; GSC: `/en/products` 9.6) · immersion cooling antminer (#13 через `/en/products`) · single phase vs two phase immersion cooling (нет в топ-100) | **P0** (секции P1/P2) | `content/briefs/immersion-cooling-mining-pillar.md`, `content/briefs/immersion-cooling-antminer.md`, `content/briefs/single-phase-immersion-cooling.md`, `content/briefs/immersion-cooling-whatsminer.md`, `content/briefs/two-phase-immersion-cooling.md` | **Решение §5, вопрос 4:** у страницы 1 показ в US, по immersion-запросам ранжируется `/en/products` (618 показов). Раздела `/en/asics-cooling/*` нет в sitemap — `technical-seo`, до публикации. Профили прошивки для immersion, °C, модели `[VERIFY]` |
| **W8** (23–29 ноя, Thanksgiving) | **Пиллар immersion, часть 2** (1 ед.): «Immersion vs air»; «Tanks and system components»; «Deployment steps»; «ROI / TCO» со ссылкой на `/en/calc` (**без обещаний доходности**); «Data center deployments»; FAQ; ссылки C3–C7 | `/en/asics-cooling/immersion-systems` | обновление | immersion cooling mining | **P0** (секции P2) | `content/briefs/immersion-cooling-vs-air-cooling.md`, `content/briefs/immersion-cooling-tank.md`, `content/briefs/immersion-cooling-asic-setup.md`, `content/briefs/immersion-cooling-roi.md`, `content/briefs/immersion-cooling-data-center.md` | Какие продукты относятся к immersion (C7: `/en/products/cell`, `/container`) `[VERIFY]`. P2-секции можно делать короткими и углублять в Q1 по данным GSC |
| W8 | **Рефреш поста про mineral oil** (1 ед.): таблица типов жидкостей; mineral oil vs synthetic vs engineered; секция «Antminer в mineral oil»; новая дата; ссылка C8 на immersion-systems | `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` | обновление | mineral oil immersion cooling (#4; GSC «mineral oil for immersion cooling» 1.7) · antminer mineral oil (нестабильно, #2 или не найден) | P1 | `content/briefs/immersion-cooling-dielectric-fluid.md` | **Защита:** позиции #1–5 уже наши, структуру URL и H1 не ломать. Свойства жидкостей `[VERIFY]`. Пост забирает запрос «immersion cooling mining» (14.3) — анкор C8 передаёт его пиллару |

**Ноябрь, нагрузка:** W5 3 ед. · W6 3 ед. · W7 3 ед. · W8 2 ед.

### Декабрь — месяц 3: P1-страницы и закрытие квартала

| Неделя | Задача | URL | Тип | Целевой ключ | P | Бриф | Зависимость / [VERIFY] |
|---|---|---|---|---|---|---|---|
| **W9** (30 ноя – 6 дек) | **Рефреш поста «how immersion cooling works»** (1 ед.): определение, как работает, single/two-phase кратко; ссылки C9 на пиллар и на пост про жидкости. GSC: immersion cooling technology 90 / 22.1, how does immersion cooling work 35 / 12.8, immersion cooling 69 / 41.2 — 0 кликов на 668 показов | `/en/blog/post/how-does-immersion-cooling-work` | обновление | immersion cooling (1600/мес, #33) · immersion computer cooling (390, #15) · what is immersion cooling (#18) | P1 | нет отдельного брифа; архитектура v2, строка 12 | Цифры эффективности `[VERIFY]`. Широкий информационный запрос: CTA на пиллар, без коммерческого давления |
| W9 | **Серия M3x, контент** (1 ед.): таблица режимов M30S / M30S+ / M30S++; эффективность и тюнинг; FAQ; ссылка на хаб (F13) | `/en/firmwares/whatsminer-series-m3x` | обновление | whatsminer firmware (#4) · whatsminer m30s firmware (n/d) · microbt firmware (#2, 0 показов) | P1 | `content/briefs/whatsminer-m30s-firmware.md` | Режимы, TH/s, J/TH `[VERIFY]`. Не просадить `-m3x`: title из W1 не менять без данных по CTR |
| **W10** (7–13 дек) | **Гайд по установке прошивки Antminer** (2 ед.): web UI / SD-карта / пакетная установка на парк, обновление, откат и восстановление; HowTo; ссылки F23 → `/antminer` и `/ams`; входящие F8, legacy noindex-страницы, индекс `/en/documentation` | `/en/documentation/antminer-firmware-install` | новая | antminer firmware install (n/d) · antminer firmware update (20/мес) | P1 | `content/briefs/antminer-firmware-install.md`, `content/briefs/antminer-firmware-update.md` (P2, секция) | **Слаг `[VERIFY]`.** Каждый шаг проверяют инженеры (`[VERIFY]`). ePIC на #7 со своим install-гайдом. Сверить с `docs.bixbit.io`, чтобы не было дублей `[VERIFY]` |
| W10 | **Серии M5x и M6x** (1 ед.): режимы M50 / M50S / M53 и M60 / M60S / M63; профили для immersion и hydro; FAQ; F18 → immersion-systems. GSC: `-m6x` whatsminer custom firmware 42 / 15.6, m61 firmware 24 / 12.2, m63 firmware 19 / 18.5; `-m5x` поз. 55–80 | `/en/firmwares/whatsminer-series-m5x`, `/en/firmwares/whatsminer-series-m6x` | обновление | whatsminer m50 firmware · whatsminer m61 / m63 firmware | P1 | `content/briefs/whatsminer-m50-firmware.md` (M60 → `-m6x`) | Режимы и совместимость `[VERIFY]`. `-m6x` нет в `data/tracked-pages.txt` — предложить добавить (§6) |
| **W11** (14–20 дек) | **Сравнение ПО для мониторинга** (2 ед.): критерии выбора; таблица AMS vs Minerstat / Braiins Manager / Luxor Commander / Hive OS; секция «alternatives»; входящие A2, F21, `/en/faq` | `/en/ams/comparison` | новая | minerstat alternative (10/мес, нет в топ-100) · mining farm monitoring software | P1 | `content/briefs/mining-farm-monitoring-software.md`, `content/briefs/ams-vs-minerstat.md`, `content/briefs/ams-vs-braiins-manager.md` (P2), `content/briefs/ams-vs-luxor-commander.md` (P2) | **Слаг `[VERIFY]`.** Данные конкурентов `[VERIFY]` с датой. Если не успеваем до праздников — публикация в W13 или в январе |
| W11 | **Блок сравнения охлаждения** (0.5 ед.): короткое сравнение immersion vs hydro vs air; ссылки C2 и C10 (hydro → immersion) | `/en/asics-cooling`, `/en/asics-cooling/hydro-systems` | правка | immersion vs hydro cooling | P2 | архитектура v2, строка 17 | Раздела нет в sitemap — `technical-seo`. Параметры систем `[VERIFY]` |
| **W12–W13** (21 дек – 3 янв, праздники) | **Итоги квартала** (1 ед.): разбор CTR до и после по всем правкам W1–W2; повторная правка title и description там, где CTR не вырос; план на Q1 | все из W1–W2 | правка | см. W1–W2 | P1 | этот план | `/rank-check` и `/weekly-drift` в начале января (§6). Обновить этот файл |

**Декабрь, нагрузка:** W9 2 ед. · W10 3 ед. · W11 2.5 ед. · W12–13 1 ед.

### Бэклог Q1 2027 (P2, по данным GSC)

| URL | Что | Бриф |
|---|---|---|
| `/en/ams` | Секции P2: alerts and automation, per-unit power monitoring, multi-client for hosting, fleet management at scale | `content/briefs/mining-farm-alerts-automation.md`, `content/briefs/mining-farm-power-monitoring.md`, `content/briefs/mining-hosting-monitoring.md`, `content/briefs/asic-fleet-management.md` |
| `/en/documentation/user-guide-for-whatsminer-asic` | Секции «install custom firmware», «update and rollback»; ссылка на хаб (F17) | `content/briefs/whatsminer-firmware-install.md`, `content/briefs/whatsminer-firmware-update.md` |
| `/en` | Title и description (сейчас в основном брендовый трафик: `bixbit` поз. 1.0, CTR ~14%); ссылки F1, C1, A1 | `content/page-optimize/homepage.md` |
| PDU (`/en/products/pdu`) | Кластер вне архитектуры v2. В брифах PDU объёмов нет (DataForSEO 401 в июне). Брифы предлагают несуществующие `/en/pdu/*`. Органика — 1 сессия за 28 дн | `content/clusters/pdu-power-distribution.md`, `content/briefs/pdu-*.md`. Решение — §5, вопрос 9 |

---

## 4. Страницы кодов ошибок Whatsminer: спецификация CTA и ссылок

**Почему P0.** После `/en` это самая посещаемая органическая посадочная в GA4 (без `(not set)`): en — 221 сессия, ru — 198 (для сравнения: `/en/firmwares` — 173). В GSC по всем странам запросы про ошибки Whatsminer (19 запросов) дают 631 показ и 96 кликов на поз. ~2–3. В Bing — 124 показа. Трафик поддерживающий: человек пришёл чинить майнер, а не покупать. Поэтому CTA должен решать его проблему, а не продавать в лоб.

| Где на странице | CTA / ссылка | Куда | Анкор (пример, EN) |
|---|---|---|---|
| Ошибки перегрева, вентиляторов, температуры | «Предупреждать, а не чинить» | `/en/ams` (секция alerts, после W6) | get temperature and fan alerts across your fleet in AMS `[VERIFY: функция]` |
| Ошибки питания / PSU / под- и перенапряжение | Мониторинг питания | `/en/ams` | monitor power and hashrate per unit `[VERIFY]` |
| Ошибки прошивки, обновления, хешбордов | Прошивка и установка | `/en/firmwares/whatsminer-all-series` (или `-m3x`, пока хаб не в индексе); `/en/documentation/user-guide-for-whatsminer-asic` | BiXBiT firmware for all Whatsminer series; how to update Whatsminer firmware |
| Конец страницы, общий блок | Прошивка + мониторинг | `/en/firmwares`, `/en/ams` | custom firmware for Whatsminer and Antminer; ASIC fleet monitoring (AMS) |
| Для RU-версии | То же на RU | `/ru/firmwares`, `/ru/ams` | зависит от §5, вопрос 1 |

Правила:
- Не больше 3–4 CTA на странице.
- Анкоры описательные, одинаковый анкор — максимум на 2 страницах (правило v2).
- Никаких обещаний «firmware fixes error X», если инженеры это не подтвердили `[VERIFY]`.
- Измерение: GA4-событие клика по CTA (задача dev) и переходы с этой страницы на `/en/firmwares*` и `/en/ams`. Сравнивать страницы между собой, в абсолют `keyEvents` не верить.

---

## 5. Решения за командой

| # | Вопрос | Данные | Что блокирует |
|---|---|---|---|
| 1 | **Приоритет RU-рынка.** Решает команда, план этот выбор не делает | Россия — 907 кликов Google из 2 263 (**40%**), CTR 2.3% против 0.32% в US. «прошивка antminer» и похожие: 44 запроса, 332 показа, 1 клик (поз. 3.6–12). В competitor-gap «прошивка antminer» — P0, в топ-20 нет ни одного вендора. RU-страница кодов ошибок — 198 сессий. CLAUDE.md ставит в приоритет англоязычные рынки | W3 (RU CTA), будущий RU-хаб Antminer, RU-версия сравнения (en+ru в competitor-gap) |
| 2 | **Слаги 4 новых страниц:** `/en/firmwares/comparison`, `/en/firmwares/dev-fee`, `/en/documentation/antminer-firmware-install`, `/en/ams/comparison` | Архитектура v2 | W3–W6, W10, W11 |
| 3 | **Текущая ставка dev fee** и как её подавать | Аудит 09-2026: 2.8%, для M2x 2%. LLM приписывают BiXBiT 2.75% (это ставка PiTBiT, источник — altcoinlog) | Dev-fee, сравнение, мета `/en/firmwares` и `-m2x` |
| 4 | **Целевой URL для immersion:** `/en/asics-cooling/immersion-systems` (так в v2) или `/en/products`, который уже ранжируется | `immersion-systems`: 1 показ в US, раздела нет в sitemap. `/en/products`: 618 показов, asic immersion cooling 9.6, immersion cooling antminer 16.9 | W7–W8 |
| 5 | **Whatsminer-хаб:** оставить хабом `-all-series` | Хаб: около 65 показов, поз. 59–91. `-m3x`: #4 по whatsminer firmware | W7 |
| 6 | **Legacy noindex-страницы Antminer:** оставить noindex или сделать 301 на `#s19` и т.п. | Архитектура v2, риски | Входящие ссылки на install-гайд (W10) |
| 7 | **Ротация отслеживаемых ключей** (утверждает человек) | Кандидаты из rank-tracking §6.3: asic firmware (98 показов / 7.5) вместо microbt firmware; asic monitoring (91 / 9.6) вместо antminer dashboard; asic monitoring software (75 / 4.8) вместо minerstat alternative; immersion cooling technology (90 / 22.1) вместо single phase vs two phase | §6.3 |
| 8 | **Как устроена цена AMS** (free / trial / платный) | В черновике `content/page-optimize/ams.md` — «try it free» `[VERIFY]` | W1 (мета `/en/ams`), CTA на страницах ошибок |
| 9 | **PDU в Q4:** вне плана или минимальный пакет для `/en/products/pdu` | Нет данных по объёмам. Нет URL в v2. Органика — 1 сессия | Бэклог |
| 10 | **Авторы для E-E-A-T:** какие инженеры подписывают страницы прошивок и охлаждения, где лежат тесты и документация, на которые можно ссылаться | Правило брифов: авторство инженеров | Все P0-страницы (подпись + дата проверки) |
| 11 | **Настройка keyEvents в GA4** | В Cross-network keyEvents ≈ числу сессий (56 116 / 57 638) | Измерение конверсий с органики и CTA |

---

## 6. Как отслеживать

### 6.1 Регулярные замеры

| Когда | Команда / скрипт | Что смотрим |
|---|---|---|
| Еженедельно (пн), после каждого деплоя | `/weekly-drift` → `./scripts/page-snapshot.py --out data/page-snapshot-YYYY-MM-DD.json` | Что новые title, description, H1 и JSON-LD реально на проде, и что нет регрессий (пустой FAQPage, canonical) |
| Еженедельно | `./scripts/gsc-query.py --days 28 --dimensions page --country usa` и `--dimensions country` | CTR и клики по страницам из W1–W2 против W0. Итоги считать по разрезу page/country, а не query |
| Еженедельно | `./scripts/ga4-query.py --preset channels` и `--preset organic-landing` | AI Assistant (baseline 68), органика (2 877), посадочные кодов ошибок |
| Ежемесячно: 2 ноя, 30 ноя, 4 янв | `/rank-check` (`scripts/serp-rank.py`, 30 ключей ≈ $0.54–1.08) | Дельты к `data/rank-tracking/baseline-2026-09-25.json`. Флаги `volatile` и `not_found_short_serp` без подтверждения в GSC не считать регрессией |
| Ежемесячно | `/geo-check` (агент `geo-ai`) | Цитирования после выхода dev-fee и comparison |
| Ежемесячно | `./scripts/bing-query.py --report pages` | Страницы кодов ошибок и `/en/firmwares` в Bing |

### 6.2 Как читать CTR после правок мета

- Окно «до» — 28 дней перед деплоем, «после» — 28 дней, начиная через 3+ дня после деплоя (лаг GSC).
- Сравнивать CTR при сопоставимой средней позиции. Если позиция сдвинулась больше чем на 2, эффект от мета отдельно не выделить.
- Объёмы маленькие (сотни показов на страницу), поэтому разница в 1–2 клика — шум. Выводы — не раньше 28 дней.
- Дату деплоя каждой правки фиксировать в журнале ниже.
- `[VERIFY]` из rank-tracking §6.2: исключить, что клики теряются из-за редиректов или отслеживания.

### 6.3 Список отслеживаемых ключей нужно обновить (решение за человеком)

План меняет целевые URL. `data/rank-tracking/keywords.md` надо обновить после публикации страниц, ротацию утверждает человек:
- `braiins os`, `vnish firmware`, `best antminer custom firmware`, `antminer firmware comparison` → `/en/firmwares/comparison` (сейчас target — `/en/firmwares` или «новая»);
- `antminer dev fee firmware`, `antminer firmware security` → `/en/firmwares/dev-fee`;
- `minerstat alternative` → `/en/ams/comparison`;
- `single phase vs two phase immersion cooling` → `/en/asics-cooling/immersion-systems` (секция), а не «страница single-phase (новая)»;
- `whatsminer custom firmware`: target `-m3x`, но ранжируется `/en/firmwares` (#2). Решить, какая страница целевая, чтобы не править мета обеих под один запрос;
- кандидаты на ротацию — §5, вопрос 7.

Также предлагаю добавить в `data/tracked-pages.txt` страницы `/en/firmwares/whatsminer-all-series`, `/en/firmwares/whatsminer-series-m6x` и 4 новые страницы после публикации (файл не менял).

### 6.4 Журнал изменений (заполнять при деплое)

| Дата деплоя | URL | Что изменено | Задача (неделя) | Замер через 28 дн |
|---|---|---|---|---|
| | | | | |

---

## 7. Зависимости от других агентов (не контент, но блокируют план)

| Зависимость | Агент | Блокирует |
|---|---|---|
| Пустой `FAQPage` на `/en/firmwares`, `/en/documentation`, странице кодов ошибок Whatsminer | `technical-seo` | W2 |
| Добавить `/en/asics-cooling/*` в sitemap | `technical-seo` | W7–W8, W11 |
| Вес `/en/firmwares/antminer` (23.8 MB) | `technical-seo` | W4–W5 (эффект от текста) |
| `Organization.description` (сейчас текст про охлаждение) | `technical-seo` + `geo-ai` | Консистентность сущности |
| llms.txt (404) и канонический блок фактов; черновик `content/geo/llms.txt` устарел (неверные URL) | `geo-ai` | GEO-метрики, W2 (каноническая фраза) |
| hreflang (нет на `/en`), `/es/`, `docs.bixbit.io` | `international-seo` + `technical-seo` | RU/ES-решения, W10 (дубли документации) |
| В GA4 есть и `/en/documentation/new-user-guide-for-whatsminer-asic/*`, и `/en/documentation/user-guide-for-whatsminer-asic/*`: какой раздел канонический `[VERIFY]` | `technical-seo` | Бэклог (секции Whatsminer user guide), ссылки из §4 |

**Вне плана:** блог-трафик на нерелевантные темы (например, `/en/blog/post/popular-erc-20-compatible-wallets` — 2 088 показов в US, 0 кликов). На ICP это не работает, в Q4 не трогаем.

---
> **W0 выполнено 2026-09-28:** GSC по страницам за 28 дней (все страны, без занижения из-за анонимизированных запросов) — `data/gsc-pages-2026-09-28.json`.
> Показы / клики / средняя позиция:
> - `/en/firmwares` — 4 095 / 135 / 15.8
> - `-m3x` — 3 549 / 85 / 8.2
> - `/en/ams` — 1 813 / 113 / 6.3
> - `/en/firmwares/antminer` — 2 178 / 29 / 15.5
> - `whatsminer-all-series` — 75 / 3 / 26.9
> - `/en/asics-cooling/immersion-systems` — 9 / 0 / 12.2
>
> `whatsminer-all-series` и `-m6x` добавлены в `data/tracked-pages.txt`, обе отдают 200.
