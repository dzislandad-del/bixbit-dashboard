# Rank tracking — отслеживаемые ключи BiXBiT

**Создано:** 2026-09-28 · **Рынок:** Google US, `location_name: United States`, `language_code: en`, desktop, depth 100
**Baseline:** `data/rank-tracking/baseline-2026-09-25.json` (дата baseline привязана к набору данных кластеров от 2026-09-25; сами SERP сняты 2026-09-28)
**Источники отбора:** `reports/cluster-repriorization-2026-09-25.md`, брифы P0/P1 в `content/briefs/`, `content/clusters/*.md`, GEO-запросы по брендам конкурентов.
**Лимит:** 30 ключей (бюджет DataForSEO).

Vol и CPC взяты из DataForSEO Google Ads (US, 2026-09); `n/d` означает меньше ~10 в месяц. Target URL — страница, которая должна ранжироваться по ключу по рекомендации пересчёта приоритетов (использовать существующие URL, а не создавать новые). [VERIFY: команда ещё не утвердила решение «существующие URL или новые»]

## Правила отбора
1. Главный ключ каждого брифа с P0 (все 6 P0-страниц).
2. Ключи из брифов P1 с измеримым объёмом, или P1-блоки, где BiXBiT уже в топ-20.
3. Широкие ключи с большим объёмом из §1.4 отчёта о пересчёте приоритетов (`immersion cooling`, `mining software`, `bitmain firmware` и др.).
4. Брендовые GEO-запросы конкурентов: `braiins os`, `vnish firmware`, `custom firmware antminer`, `whatsminer custom firmware`.
5. Не вошли, т.к. n/d и нет позиции: `whatsminer m30s firmware`, `whatsminer m50 firmware`, `mining farm monitoring software`, `whatsminer firmware security`, `antminer firmware install`. Первые кандидаты на ротацию.

## Ключи

| # | Keyword | Кластер | Приоритет | Тип | Vol | Target URL |
|---|---|---|---|---|---|---|
| 1 | antminer firmware | Antminer FW | P0 | Commercial head | 50 (CPC $70.51) | /en/firmwares/antminer |
| 2 | whatsminer firmware | Whatsminer FW | P0 | Commercial head, защита | 20 (CPC $32.03) | /en/firmwares/whatsminer-series-m3x |
| 3 | bitmain firmware | Antminer FW | P0 | Commercial head | 140 | /en/firmwares/antminer |
| 4 | antminer custom firmware | Antminer FW | P0 | Commercial / GEO | 10 | /en/firmwares/antminer |
| 5 | custom firmware antminer | Antminer FW | P0 | GEO (brand-intent) | [VERIFY: не измерялся отдельно] | /en/firmwares/antminer |
| 6 | whatsminer custom firmware | Whatsminer FW | P0 | Commercial / GEO | 10 | /en/firmwares/whatsminer-series-m3x |
| 7 | braiins os | Antminer FW (comparison) | P0 | GEO, бренд конкурента | 210 | /en/firmwares (страница-сравнение — новая) |
| 8 | vnish firmware | Antminer FW (comparison) | P0 | GEO, бренд конкурента | 140 | /en/firmwares (страница-сравнение — новая) |
| 9 | best antminer custom firmware | Antminer FW (comparison) | P0 | Commercial / GEO | n/d | страница-сравнение (новая) |
| 10 | antminer firmware comparison | Antminer FW (comparison) | P0 | Commercial / GEO | n/d | страница-сравнение (новая) |
| 11 | antminer dev fee firmware | Antminer FW (security) | P0 | Trust / GEO | n/d | страница dev fee / security (новая) |
| 12 | antminer firmware security | Antminer FW (security) | P0 | Trust / GEO | n/d | страница dev fee / security (новая) |
| 13 | whatsminer tool | Whatsminer FW | P0 | Secondary hub | 50 | /en/firmwares/whatsminer-series-m3x |
| 14 | microbt firmware | Whatsminer FW | P0 | Secondary hub | 10 | /en/firmwares/whatsminer-series-m3x |
| 15 | antminer s19 firmware | Antminer FW | P1 | Model | 10 | /en/firmwares/antminer [VERIFY: есть ли отдельная страница модели] |
| 16 | antminer s21 firmware | Antminer FW | P1 | Model | 10 | /en/firmwares/antminer [VERIFY] |
| 17 | immersion cooling mining | Immersion | P0 | Commercial head | 20 | /en/asics-cooling/immersion-systems |
| 18 | asic immersion cooling | Immersion | P0 | Commercial | 10 | /en/asics-cooling/immersion-systems |
| 19 | immersion cooling | Immersion | P1 | Broad head | 1600 | /en/blog/post/how-does-immersion-cooling-work |
| 20 | immersion computer cooling | Immersion | P1 | Broad | 390 | /en/blog/post/how-does-immersion-cooling-work |
| 21 | what is immersion cooling | Immersion | P1 | Informational | 90 | /en/blog/post/how-does-immersion-cooling-work |
| 22 | mineral oil immersion cooling | Immersion (fluid) | P1 | Informational, защита | 20 | /en/blog/post/immersion-liquid-choosing-the-right-one-for-mining |
| 23 | antminer mineral oil | Immersion (fluid) | P1 | Informational, защита | 50 | /en/blog/post/immersion-liquid-choosing-the-right-one-for-mining |
| 24 | immersion cooling antminer | Immersion | P1 | Commercial | 20 | /en/asics-cooling/immersion-systems |
| 25 | single phase vs two phase immersion cooling | Immersion | P1 | Informational | 20 | страница single-phase (новая) |
| 26 | asic monitor | Monitoring (AMS) | P0 | Commercial head | 70 | /en/ams |
| 27 | mining software | Monitoring (AMS) | P0 | Broad secondary (тест) | 260 (CPC $39.51) | /en/ams |
| 28 | mining monitoring software | Monitoring (AMS) | P0 | Commercial | 10 | /en/ams |
| 29 | antminer dashboard | Monitoring (AMS) | P1 | Commercial | 30 | /en/ams |
| 30 | minerstat alternative | Monitoring (AMS) | P1 | Competitor alt | 10 | страница AMS vs Minerstat (новая) |

**Итого:** P0 — 19, P1 — 11. Firmware — 16, Immersion — 9, Monitoring — 5. PDU не отслеживается (не входил в пересчёт приоритетов).

## Как обновлять
- Пересъём раз в месяц тем же набором параметров (endpoint `serp/google/organic/live/regular`, depth 100, **обязательно `noAiMode: true`**: AI-режим MCP обрезает список результатов) → новый файл `data/rank-tracking/rank-YYYY-MM-DD.json`, сравнение с baseline в `/weekly-drift`.
- Позиция считается по `rank_group` (только органика, без SERP-фич). `rank_absolute` сохраняется рядом.
- Ротация: ключ с n/d, который 2 съёма подряд вне топ-100, заменить кандидатом из списка «не вошли».
