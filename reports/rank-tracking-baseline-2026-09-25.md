# Rank tracking baseline: bixbit.io, Google US

**Baseline:** 2026-09-25. Набор ключей и объёмы взяты из пересчёта приоритетов от этой даты. **SERP сняты:** 2026-09-28.
**Источник:** DataForSEO `serp/google/organic/live/regular` · United States · en · desktop · depth 100
**Позиция:** `rank_group`, только органика. Считается только домен `bixbit.io`. Партнёрские домены (bixbitusa.io) исключены из отслеживания.
**Файлы:** ключи — `data/rank-tracking/keywords.md`; baseline — `data/rank-tracking/baseline-2026-09-25.json`; сырые выгрузки батчей — `data/rank-tracking/raw/`

---

## 1. Сводка

| Показатель | Значение |
|---|---|
| Отслеживаемых ключей | 30 (P0 — 19, P1 — 11) |
| BiXBiT найден в выдаче | **17** |
| Топ-3 | 2 (`whatsminer custom firmware` #2, `microbt firmware` #2) |
| Топ-10 | 10 |
| #11–20 | 6 |
| #21+ | 1 (`immersion cooling` #33) |
| Нет в топ-100 (выдача полная) | 5 |
| Не найден, но выдача короткая (<80 результатов) | 8 — статус неоднозначный, см. §4 |

**Главное:**
1. **Firmware — сильная зона.** 10 из 16 firmware-ключей в топ-20, из них 9 в топ-10. `antminer firmware` (CPC $70.51) на **#8**. В Labs 25.09 было #15: база Labs отстаёт от живой выдачи.
2. **Monitoring (AMS): видимость есть, но по другим формулировкам.** *Уточнено по GSC, см. §6.* Живой SERP не нашёл BiXBiT ни по одному из 5 ключей. GSC при этом показывает `/en/ams` на средней позиции 7.5 по `asic monitor`, а по неотслеживаемым `asic monitoring software` (75 показов, поз. 4.8) и `asic monitoring` (91, поз. 9.6) AMS уже в топ-10. Настоящий разрыв — `mining software` (260, CPC $39.51) и `mining monitoring software`: BiXBiT нет ни в SERP, ни в GSC.
3. **Брендовые GEO-запросы конкурентов** (`braiins os`, `vnish firmware`): BiXBiT не ранжируется. Это ожидаемо, потому что страницы-сравнения ещё нет. Выдачу полностью занимают домены брендов: braiins.com держит #1–3, домены Vnish — #1–3.
4. **Ранжируются не те URL.** По `immersion cooling mining` (P0) в выдаче блог-пост, а не коммерческая `/en/asics-cooling/immersion-systems`. По `immersion cooling antminer` — `/en/products`. По `whatsminer custom firmware` — хаб `/en/firmwares`, а не `-m3x`.

---

## 2. Таблица позиций

Позиция `—` = BiXBiT не найден. «Labs 09-25» — позиция из `ranked_keywords` на 2026-09-25, для сравнения.

### Firmware

| Ключ | Позиция | Приоритет | URL | Labs 09-25 | Примечание |
|---|---|---|---|---|---|
| antminer firmware | **8** | P0 | /en/firmwares/antminer | 15 | +/en/firmwares #39 |
| whatsminer firmware | **4** | P0 | /en/firmwares/whatsminer-series-m3x | 3 | 9 URL BiXBiT в топ-100 |
| bitmain firmware | **17** | P0 | /en/firmwares/antminer | 45 | |
| antminer custom firmware | — | P0 | — | — | Короткая выдача (19) |
| custom firmware antminer | **5** | P0 | /en/firmwares/antminer | — | Порядок слов меняет позицию: см. строку выше |
| whatsminer custom firmware | **2** | P0 | /en/firmwares | — | URL ≠ target; -m3x #6 |
| braiins os | — | P0 | — | — | Нет в топ-100; braiins.com #1–3 |
| vnish firmware | — | P0 | — | — | 76 результатов, первый проход; домены Vnish #1–3 |
| best antminer custom firmware | — | P0 | — | — | Короткая выдача (14) |
| antminer firmware comparison | **11** | P0 | /en/firmwares/antminer | — | ePIC #4, Awesome Miner #3 |
| antminer dev fee firmware | **5** | P0 | /en/firmwares | — | Braiins #6, ePIC #7. Текст про dev fee на странице — [VERIFY: 2.8% / 2% M2x] |
| antminer firmware security | **8** | P0 | /en/firmwares/antminer | — | ⚠ Частичная выдача (40106, 8 результатов) |
| whatsminer tool | **10** | P0 | /en/firmwares/whatsminer-series-m3x | 16 | |
| microbt firmware | **2** | P0 | /en/firmwares/whatsminer-series-m3x | — | 14 URL BiXBiT в выдаче |
| antminer s19 firmware | **8** | P1 | /en/firmwares/antminer | — | Vnish #2, Braiins #9 |
| antminer s21 firmware | — | P1 | — | — | Короткая выдача (58); Awesome Miner #2 |

### Immersion cooling

| Ключ | Позиция | Приоритет | URL | Labs 09-25 | Примечание |
|---|---|---|---|---|---|
| immersion cooling mining | **12** | P0 | /en/blog/post/immersion-liquid-choosing-the-right-one-for-mining | 14 | URL ≠ target (коммерческая страница) |
| asic immersion cooling | — | P0 | — | — | ⚠ Нестабильно: в другой попытке /en/products #8 |
| immersion cooling | **33** | P1 | /en/blog/post/how-does-immersion-cooling-work | 32 | LiquidStack #26 |
| immersion computer cooling | **15** | P1 | /en/blog/post/how-does-immersion-cooling-work | 15 | LiquidStack #21 |
| what is immersion cooling | **18** | P1 | /en/blog/post/how-does-immersion-cooling-work | 19 | LiquidStack #16 |
| mineral oil immersion cooling | **4** | P1 | /en/blog/post/immersion-liquid-choosing-the-right-one-for-mining | 5 | |
| antminer mineral oil | — | P1 | — | 2 | ⚠ Нестабильно: в другой попытке тот же пост #2 |
| immersion cooling antminer | **13** | P1 | /en/products | — | URL ≠ target; /en/products/cell #47 |
| single phase vs two phase immersion cooling | — | P1 | — | — | Нет в топ-100; Engineered Fluids #2 |

### Monitoring (AMS)

| Ключ | Позиция | Приоритет | URL | Labs 09-25 | Примечание |
|---|---|---|---|---|---|
| asic monitor | — | P0 | — | 7 | В выдаче всего ~10 результатов; спам-страница с «BiXBiT AMS» в title (не наш домен) |
| mining software | — | P0 | — | — | Нет в топ-100; Awesome Miner #5, Hiveon #9, Minerstat #10 |
| mining monitoring software | — | P0 | — | — | Нет в топ-100; Awesome Miner #1, Braiins #4 |
| antminer dashboard | — | P1 | — | — | Короткая выдача (54); Minerstat #6 |
| minerstat alternative | — | P1 | — | — | Нет в топ-100; Minerstat #2 |

---

## 3. Выводы для плана (P0–P2)

| # | Приоритет | Что | Основание |
|---|---|---|---|
| 1 | **P0** | AMS: расширить `/en/ams` под `mining monitoring software` / `mining software`, опираясь на уже работающие `asic monitoring*` | В GSC есть `asic monitoring*` в топ-10, но нет `mining *software` |
| 2 | **P0** | Страница-сравнение прошивок: `braiins os`, `vnish firmware`, `best antminer custom firmware` | Нет URL; GEO-разрыв подтверждён |
| 3 | **P0** | Добить `antminer firmware` #8 → топ-5 и `bitmain firmware` #17 → топ-10 на `/en/firmwares/antminer` | Самый дорогой клик в нише, позиция уже близко |
| 4 | **P1** | Перенести сигналы с блог-постов на `/en/asics-cooling/immersion-systems` (ссылки из постов, анкоры) | P0 `immersion cooling mining` ранжирует блог |
| 5 | **P1** | `antminer dev fee firmware` #5 ранжирует `/en/firmwares`: проверить, что там правильная цифра dev fee | Репутационный риск, если на странице «no dev fee» [VERIFY] |

---

## 4. Методика и ограничения

- **Обрезанные выдачи.** MCP DataForSEO по умолчанию отдаёт «AI-optimized» ответ, и он может урезать список результатов. Например, по `bitmain firmware` в этом режиме пришло 17 результатов, в полном (`noAiMode: true`) — 85. Найденные позиции от этого не страдают. А вот «не найден» на коротком списке ненадёжен, поэтому 11 таких ключей перезапущены в полном режиме, до 2 попыток на ключ. **Для следующих съёмов всегда ставить `noAiMode: true`.**
- **Короткие выдачи у Google.** По узким запросам Google сам отдаёт 1–6 страниц. Статус `not_found_short_serp` означает «нет среди того, что вернул Google», а не «не ранжируется». Для таких ключей надёжнее смотреть GSC.
- **Волатильность.** У 2 ключей (`asic immersion cooling`, `antminer mineral oil`) две попытки подряд дали разный состав выдачи: BiXBiT то #2–8, то вообще не найден. В baseline записана попытка с бо́льшим числом результатов, альтернатива сохранена в `alt_observation`.
- **`vnish firmware`** снят только в первом проходе (76 результатов, AI-режим). BiXBiT не найден, но полностью исключить обрезку списка нельзя: при следующем съёме перепроверить.
- **Ошибки API:** 40101 (Internal SE error) на 3 ключах, после ретрая ответ пришёл. 40106 (partial) на `antminer firmware security`: позиция #8 записана с флагом.
- **Стоимость:** около 52 live-вызовов SERP (30 в первом проходе, повторы после ошибок и перезапуски). Проверочный вызов 2026-09-28 показал $0.018 за запрос с depth 100, значит итого около **$0.94**. Следующие съёмы — через `scripts/serp-rank.py`: он печатает фактическую стоимость, 30 ключей ≈ $0.54–1.08.
- **GSC** подключён 2026-09-28 (`scripts/gsc-query.py`), сверка — в §6.

## 5. Как повторять съём
Раз в месяц командой `/rank-check` (`scripts/serp-rank.py`, полный ответ API без обрезки). Результат сохранять в `data/rank-tracking/rank-YYYY-MM-DD.json` в той же схеме, что и baseline. Дельты считать по полю `position`. Ключи с флагами `volatile` и `not_found_short_serp` помечать отдельно, чтобы не поднимать ложных алертов в `/weekly-drift`.

---

## 6. Сверка с Google Search Console (US, 2026-08-29..2026-09-25)

Данные получены через `scripts/gsc-query.py`. Файлы: `data/gsc-queries-us-2026-09-28.json` (1242 запроса) и `data/gsc-queries-pages-us-2026-09-28.json` (2084 пары «запрос–страница»). В baseline JSON они записаны в поле `gsc_28d_us`.

**Как читать:** позиция в GSC — это средневзвешенное по всем показам, устройствам и дням. Живой SERP — один снимок на desktop. Поэтому цифры расходятся, например `antminer firmware`: SERP #8, GSC 23.6.

### 6.1 Что GSC поменял в выводах

| Ключ | Живой SERP | GSC: показы / клики / ср. поз. | Страница в GSC | Вывод |
|---|---|---|---|---|
| asic monitor | не найден (короткая выдача) | 32 / 0 / 11.7 | /en/ams — 7.5 | **Ранжируется.** Статус SERP был ложноотрицательным |
| antminer custom firmware | не найден (короткая выдача) | 32 / 0 / 12.3 | /en/firmwares/antminer — 10.3 | **Ранжируется** на границе топ-10 |
| asic immersion cooling | нестабильно | 51 / 0 / 24.5 | /en/products — 9.6 | Ранжируется `/en/products`, а не страница immersion |
| antminer s21 firmware | не найден (короткая выдача) | 20 / 0 / 22.3 | /en/firmwares — 28.7 | Ранжируется слабо, отдельной страницы S21 нет |
| whatsminer firmware | #4 | 93 / 0 / 9.4 | -m3x — 3.9 | Подтверждено |
| whatsminer custom firmware | #2 | 66 / 0 / 5.0 | /en/firmwares — 2.0 | Подтверждено |
| antminer firmware | #8 | 80 / 0 / 23.6 | /en/firmwares/antminer — 22.1 | В среднем хуже, чем в снимке SERP |
| immersion cooling | #33 | 69 / 0 / 41.2 | блог — 41.2 | Подтверждено |

У 14 из 30 ключей в GSC нет показов за 28 дней: `braiins os`, `vnish firmware`, все запросы про сравнение, dev fee и security, `microbt firmware`, `mining software`, `mining monitoring software`, `antminer dashboard`, `minerstat alternative`, `antminer mineral oil`, `single phase vs two phase`, `custom firmware antminer`. Для ключей с объёмом n/d это ожидаемо. Но у `microbt firmware` в живом SERP #2, а показов 0, то есть спрос по нему в US практически нулевой.

### 6.2 Главная проблема — CTR, а не позиции

**23 697 показов → 76 кликов (CTR 0.32%)** по US за 28 дней, итог в разрезе по стране. *Поправка 2026-09-28: раньше здесь было «13 437 → 29». Это была сумма в разрезе по запросам, а в нём GSC не показывает анонимизированные запросы.* Из видимых запросов 20 из 29 кликов — брендовый `bixbit`. По всем 16 отслеживаемым ключам с показами **0 кликов**, в том числе там, где BiXBiT в топ-5 (`whatsminer custom firmware` 2.0 и `asic monitoring software` 4.8). Следующий шаг — `/page-optimize` для title/description на `/en/firmwares`, `/en/firmwares/whatsminer-series-m3x` и `/en/ams`. [VERIFY: исключить, что клики теряются из-за редиректов или отслеживания]

### 6.3 Кандидаты в отслеживание (есть в GSC, нет в списке из 30)

| Запрос | Показы | Ср. поз. | Кластер | Кого заменить |
|---|---|---|---|---|
| asic firmware | 98 | 7.5 | Firmware | `microbt firmware` (0 показов) |
| asic monitoring | 91 | 9.6 | AMS | `antminer dashboard` (0 показов) |
| asic monitoring software | 75 | 4.8 | AMS | `minerstat alternative` (0 показов) |
| immersion cooling technology | 90 | 22.1 | Immersion | `single phase vs two phase immersion cooling` (0 показов) |

Ротацию не делал: список ключей утверждаете вы.
