# Пересчёт приоритетов кластеров: реальные объёмы DataForSEO

**Дата:** 2026-09-25 · **Рынок:** United States / en
**Кластеры:** antminer-firmware, whatsminer-firmware, immersion-cooling-mining, mining-fleet-monitoring. PDU не входил в задачу.

**Источники:**

| Источник | Данные | Файл | Стоимость |
|---|---|---|---|
| DataForSEO Google Ads `search_volume` | объём, CPC, конкуренция; 308 ключей из кластеров и брифов + 24 ключевых термина ниши | `data/dfs-search-volume-clusters-us-2026-09-25.json` | $0.09 |
| DataForSEO Labs `bulk_keyword_difficulty` | KD для 57 ключей с объёмом | `data/dfs-keyword-difficulty-clusters-us-2026-09-25.json` | $0.02 |
| DataForSEO Labs `ranked_keywords` (bixbit.io) | текущие позиции BiXBiT | `data/dfs-ranked-keywords-bixbit.io-2026-09-25.json` (выгрузка того же дня) | — |

**Не использовано:** GSC. Коннектор работает, но задача была про DataForSEO. Для запросов с n/d GSC — следующий шаг, см. ниже.

---

## 1. Главный вывод

**Спрос в US по всем четырём кластерам очень маленький.** Объём есть только у 57 из 308 ключей. 39 из них — на нижнем пороге Google Ads (10/мес). У остальных 251 ключа — `n/d`, то есть меньше ~10/мес. Это не ноль, но и не опора для планирования.

**Что это меняет:**
1. **Кластеры по 11 страниц — это слишком много.** Если делить тему на узкие споки при таких объёмах, получатся «тонкие» страницы. Рекомендация: слить похожие споки. Например, update + install, а overclocking + undervolting + autotuning объединить в одну страницу «tuning modes». Тогда вместо 45 запланированных URL останется около 20.
2. **Приоритет задаёт коммерческая ценность и текущая позиция, а не объём.** `antminer firmware` — 50/мес, но CPC $70.51 (самый дорогой клик в нише), а BiXBiT уже на #15. `whatsminer firmware` — 20/мес, CPC $32.03, BiXBiT на #3.
3. **У части P0 основание не в объёме, а в GEO.** Страница-сравнение и страница про dev fee получают P0 по итогам competitor-gap от 2026-09-25: LLM отвечают на эти запросы по сторонним страницам, где BiXBiT нет. В брифах это явно помечено.
4. **Самый большой спрос лежит за пределами запланированных ключей:**
   - `immersion cooling` — 1600, BiXBiT #32; `immersion computer cooling` — 390, #15;
   - группа mineral oil — ~200/мес, BiXBiT уже на #1–5;
   - `mining software` — 260, CPC $39.51;
   - `braiins os` — 210, `vnish firmware` — 140, `bitmain firmware` — 140, BiXBiT #45.
5. **Кластеры планировали URL, которых нет на сайте:** `/en/antminer-firmware`, `/en/immersion-cooling-mining`. На живом сайте эти темы уже закрывают `/en/firmwares/antminer`, `/en/firmwares/whatsminer-series-*`, `/en/asics-cooling/immersion-systems` и `/en/ams`, и они уже ранжируются. Рекомендация: оптимизировать существующие URL, а не создавать дубли, иначе они будут каннибализировать друг друга. Нужно решение команды [VERIFY].

### Итог по кластерам

| Кластер | Приоритет кластера (было → стало) | P0 / P1 / P2 было | P0 / P1 / P2 стало | ↑ / ↓ | Главный ключ (vol · CPC · KD · позиция BiXBiT) |
|---|---|---|---|---|---|
| Antminer firmware | P0 → **P0** | 1 / 7 / 3 | 3 / 3 / 5 | 2 / 3 | antminer firmware · 50 · $70.51 · 6 · #15 |
| Whatsminer firmware | P0 → **P0** (защита позиций) | 1 / 7 / 3 | 1 / 4 / 6 | 1 / 4 | whatsminer firmware · 20 · $32.03 · 4 · **#3** |
| Immersion cooling | P1 → **P1** | 3 / 5 / 3 | 1 / 3 / 7 | 1 / 6 | immersion cooling mining · 20 · $2.55 · 0 · #14; широкий immersion cooling · 1600 · $3.93 · 21 · #32 |
| Fleet monitoring (AMS) | P1 → **P1** | 6 / 4 / 2 | 1 / 4 / 7 | 0 / 8 | asic monitor · 70 · $0.44 · 0 · **#7** |
| **Итого (45 брифов)** | | **11 / 23 / 11** | **6 / 14 / 25** | **4 / 21** | |

Порядок кластеров из CLAUDE.md §3 (firmware → immersion → monitoring) данные **подтверждают**: у firmware самый высокий CPC и лучшие позиции. Меняется наполнение внутри кластеров.

---

## 2. Как считали приоритет

| Критерий | Вес | Правило |
|---|---|---|
| Коммерческая ценность | высокий | CPC ≥ $15 или прямой коммерческий интент по продукту |
| Текущая позиция BiXBiT | высокий | #4–20 = quick win, быстрее всего окупается; #1–3 = защищать |
| Объём (US) | средний | ≥ 50 = заметно; 20–40 = средне; 10 = порог; n/d = в отдельную страницу не выносить |
| Доказательства из GEO / competitor-gap (2026-09-25) | средний | Если LLM цитируют конкурентов вместо BiXBiT — можно поднять до P0, в брифе пишем «priority from GEO, not volume» |
| KD | низкий | Почти везде 0–57, поэтому решает редко |

- **P0** — делать сейчас.
- **P1** — следующие 30–60 дней.
- **P2** — позже, или как секция внутри другой страницы, а не отдельный URL.

---

## 3. Было / стало по страницам

`n/d` = меньше ~10/мес. Vol — сумма целевых ключей брифа в US. Позиция — Google US, DataForSEO ranked_keywords.

### 3.1 Antminer firmware

| Страница (бриф) | Было | Стало | Vol | KD | BiXBiT | Почему |
|---|---|---|---|---|---|---|
| Пиллар (`antminer-firmware-pillar`) | P0 | **P0** | 60 | 6 | #15 `/en/firmwares/antminer` | CPC $70.51; quick win из #15. Добавить `bitmain firmware` (140, #45) |
| Сравнение (`antminer-firmware-comparison`) | P1 | **P0 ↑** | n/d | — | — | Спрос на бренды конкурентов: braiins os 210, vnish firmware 140. GEO-разрыв в запросах-сравнениях |
| Безопасность / dev fee (`antminer-firmware-security`) | P2 | **P0 ↑** | n/d | — | — | GEO: на запрос «lowest dev fee» ePIC называют в 4 из 5 движков, BiXBiT — ни в одном. Одна страница для Antminer и Whatsminer |
| S19 (`antminer-s19-firmware`) | P1 | P1 | 50 | 18–57 | — | 5 ключей × 10 |
| S21 (`antminer-s21-firmware`) | P1 | P1 | 30 | 50 | — | CPC $16.46; рядом antminer s21 hydro — 90, KD 3 |
| Установка (`antminer-firmware-install`) | P1 | P1 | n/d | — | — | Объединить с update. У ePIC гайд по установке стоит #7 по «antminer custom firmware» |
| Обновление (`antminer-firmware-update`) | P1 | **P2 ↓** | 20 | 55 | — | Секция страницы установки |
| Custom (`antminer-custom-firmware`) | P1 | **P2 ↓** | 10 | — | — | Секция пиллара |
| Разгон (`antminer-overclocking-firmware`) | P1 | **P2 ↓** | 20 | — | — | Объединить в «tuning modes» |
| Андервольт (`antminer-undervolting`) | P2 | P2 | n/d | — | — | Объединить в «tuning modes» |
| Автотюнинг (`antminer-autotuning`) | P2 | P2 | n/d | — | — | Объединить в «tuning modes» |

### 3.2 Whatsminer firmware

| Страница (бриф) | Было | Стало | Vol | KD | BiXBiT | Почему |
|---|---|---|---|---|---|---|
| Хаб (`whatsminer-firmware-pillar`) | P0 | **P0** | 40 | 4 | **#3** `/en/firmwares/whatsminer-series-m3x` | CPC $32.03. Защищать позицию; конкурентов в этом сегменте нет. Добавить `whatsminer tool` (50, #16) |
| M30S (`whatsminer-m30s-firmware`) | P1 | P1 | 10 | — | — | Оптимизировать существующую `-m3x` |
| M50/M60 (`whatsminer-m50-firmware`) | P1 | P1 | 10 | — | — | Оптимизировать существующие `-m5x` и `-m6x` |
| Сравнение (`whatsminer-firmware-comparison`) | P1 | P1 | n/d | — | — | GEO: LLM называют BiXBiT для Whatsminer в 4 из 5 движков. Закрепить это |
| Безопасность / dev fee (`whatsminer-firmware-security`) | P2 | **P1 ↑** | n/d | — | — | Входит в общую страницу про dev fee |
| Custom (`whatsminer-custom-firmware`) | P1 | **P2 ↓** | 10 | 50 | — | Секция хаба |
| Обновление (`whatsminer-firmware-update`) | P1 | **P2 ↓** | 10 | 42 | — | Объединить с установкой |
| Установка (`whatsminer-firmware-install`) | P1 | **P2 ↓** | n/d | — | — | Инструкции уже есть в `/en/documentation` |
| Разгон (`whatsminer-overclocking-firmware`) | P1 | **P2 ↓** | 10 | — | — | «Tuning modes» |
| Андервольт / автотюнинг | P2 | P2 | n/d | — | — | «Tuning modes» |

### 3.3 Immersion cooling

| Страница (бриф) | Было | Стало | Vol | KD | BiXBiT | Почему |
|---|---|---|---|---|---|---|
| Пиллар (`immersion-cooling-mining-pillar`) | P0 | **P0** | 30 | 0 | #14 (блог-пост) | Перенести позицию с блога на коммерческую `/en/asics-cooling/immersion-systems` |
| Диэлектрическая жидкость / mineral oil (`immersion-cooling-dielectric-fluid`) | P2 | **P1 ↑** | ~200 по группе | 0 | **#1–5** | Самый большой блок, который уже наш. Обновить существующий пост, а не делать новый URL |
| *Обновить пост `how-does-immersion-cooling-work` (брифа нет)* | — | **P1 (новое)** | 390 + 90 + 1600 (широкие) | 10–21 | #15 / #19 / #32 | Широкий трафик, из поста — ссылки на пиллар |
| Antminer (`immersion-cooling-antminer`) | P0 | **P1 ↓** | 40 | 55 | — | CPC $2.12; Whatsminer — секцией на этой же странице |
| Single-phase (`single-phase-immersion-cooling`) | P1 | P1 | 20 | 40 | — | Two-phase — секцией на этой странице |
| Whatsminer (`immersion-cooling-whatsminer`) | P0 | **P2 ↓** | n/d | — | — | Секция страницы Antminer |
| Two-phase (`two-phase-immersion-cooling`) | P2 | P2 | n/d | — | — | Секция single-phase |
| Tank (`immersion-cooling-tank`) | P1 | **P2 ↓** | 10 | — | — | |
| Vs air (`immersion-cooling-vs-air-cooling`) | P1 | **P2 ↓** | n/d | — | — | |
| ROI (`immersion-cooling-roi`) | P1 | **P2 ↓** | n/d | — | — | Можно использовать `/en/calc` |
| Setup (`immersion-cooling-asic-setup`) | P1 | **P2 ↓** | n/d | — | — | |
| Data center (`immersion-cooling-data-center`) | P2 | P2 | n/d | — | — | |

### 3.4 Fleet monitoring (AMS)

| Страница (бриф) | Было | Стало | Vol | KD | BiXBiT | Почему |
|---|---|---|---|---|---|---|
| Хаб `/en/ams` (`mining-fleet-monitoring-pillar`) | P0 | **P0** | 20 (+ asic monitor 70) | 0–38 | **#7** | Quick win #7 → топ-3. Протестировать `mining software` (260, CPC $39.51) как вторичный ключ |
| Antminer monitoring (`antminer-monitoring-software`) | P0 | **P1 ↓** | 50 | 12 | — | antminer dashboard — 30. S11 dashboard — секцией здесь |
| Mining farm monitoring software (`mining-farm-monitoring-software`) | P0 | **P1 ↓** | 20 | — | — | Нужна под GEO-запросы в стиле подборок «лучшие инструменты» |
| Whatsminer monitoring (`whatsminer-monitoring-software`) | P0 | **P1 ↓** | n/d | — | — | Отличие BiXBiT (Antminer + Whatsminer в одном дашборде); важно для GEO |
| AMS vs Minerstat (`ams-vs-minerstat`) | P1 | P1 | 20 | 24 | — | Единственное сравнение с измеримым спросом |
| AMS vs Braiins Manager (`ams-vs-braiins-manager`) | P0 | **P2 ↓** | n/d | — | — | |
| ASIC fleet management (`asic-fleet-management`) | P0 | **P2 ↓** | n/d | — | — | |
| AMS vs Luxor Commander (`ams-vs-luxor-commander`) | P1 | **P2 ↓** | n/d | — | — | |
| Alerts (`mining-farm-alerts-automation`) | P1 | **P2 ↓** | n/d | — | — | |
| Hosting (`mining-hosting-monitoring`) | P1 | **P2 ↓** | n/d | — | — | Материал для продаж и BD, а не SEO |
| Power / Dashboard | P2 | P2 | n/d | — | — | |

---

## 4. Что изменено в файлах

- **`content/clusters/*.md` (4 файла):**
  - удалены пометки о недоступности данных (401), вместо них — реальные источники и ключевой вывод;
  - в строки Vol/KD проставлены цифры, в строки Priority — «было → стало» с обоснованием;
  - переписан порядок производства страниц;
  - в monitoring заполнена таблица seed-ключей.
- **`content/briefs/*.md` (45 брифов):**
  - новая строка `**Priority:**` (стало / было / почему);
  - таблица Target Keywords с колонками Vol (US, 2026-09) / KD / BiXBiT pos;
  - сноска об источниках данных.
- **Попутно исправлено (P0 из competitor-gap):** в 5 брифах было написано «no dev fee»: antminer-firmware-pillar, antminer-custom-firmware, antminer-firmware-security, whatsminer-firmware-pillar, ams-vs-braiins-manager. Утверждение заменено нейтральной формулировкой «transparent dev fee» и пометкой `[VERIFY: 2026-09 audit found 2.8% (2% on M2x) — get the current rate from the team]`.
- **Не изменено:** структура разделов и URL-слаги в брифах. Слияния страниц и переход на существующие URL описаны в поле Priority как рекомендации: это решение команды, а не правка вслепую. Кластер PDU не трогал.
- Все изменения видны в `git diff content/` и откатываются через git. Коммита не было.

## 5. Ограничения и следующие шаги

1. **Google Ads сильно огрубляет маленькие объёмы.** «10» означает примерно 0–15, а «n/d» — меньше ~10. **Следующий шаг: подтянуть показы из GSC** (коннектор работает) по запросам с n/d. Если GSC покажет показы, P2-страницы можно поднять обратно.
2. **Только US.** Спрос в СНГ и LatAm не измерялся. Отдельная задача по ES/LatAm была остановлена.
3. **Не измерено:** `whatsminer m30s++ firmware` (Google Ads не принимает символ «+») и один длинный ключ из брифа two-phase.
4. **В `content/geo/entity-definition-homepage.md` тоже написано «no dev fee».** Это вне этой задачи; исправить до публикации.
5. **Нужно решение команды:** оптимизируем существующие URL (`/en/firmwares/*`, `/en/asics-cooling/*`, `/en/ams`) или строим новые `/en/antminer-firmware/*`? Рекомендация — существующие.
