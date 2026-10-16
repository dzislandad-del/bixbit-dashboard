# Бриф: Antminer S21 Series Explained: S21, S21 Pro, S21 XP and Hydro

**ID плана:** EN-NOV-1 · **Язык:** EN · **Тип:** новая · **Приоритет:** P0
**URL:** новый слаг `/en/blog/post/antminer-s21-series-explained` [VERIFY у команды, §6 вопрос 9] · **Пара hreflang:** нет. RU-адаптация RU-NOV-2 (`/ru/firmwares/antminer`), после её выхода связать переводы в CMS
**Поддерживает (architecture v2):** `/en/firmwares/antminer#s21` [VERIFY: id фрагмента у dev]. Пост закрывает информационный спрос по линейке S21 (модели, J/TH, охлаждение) и передаёт читателя и вес в коммерческую секцию S21. Запросы «antminer s21 firmware», «antminer s21 pro firmware», «s21 firmware update» у страницы прошивки **не забирает**
**Автор / ревьюер:** [VERIFY: инженер BiXBiT по прошивкам Antminer, должность] / [VERIFY: второй инженер или продакт] · **Дата проверки фактов:** —
**Бриф подготовлен:** 2026-10-10 · **Окно публикации:** черновик до 2026-10-27, [VERIFY] у инженеров неделю, публикация до 2026-11-09 (до W6)

## 1. Цель и интент
- **Интент:** informational / comparison. Человек выбирает или уже купил S21 и хочет понять, чем S21, S21 Pro, S21 XP и Hydro-версии отличаются по хешрейту, мощности, J/TH и требованиям к охлаждению.
- **Чем пост отличается от `/en/firmwares/antminer#s21`:** страница прошивки отвечает на «какую прошивку поставить на S21 и что она даёт» (коммерческий интент). Пост отвечает на «что это за модели и какая из них подходит моей площадке». В посте про прошивку только короткий абзац и ссылка, без таблицы режимов и без цифр прироста.
- **Читатель (ICP):** оператор фермы, который обновляет парк S19 → S21, и техдиректор ДЦ / хостинг-провайдер, который планирует электрику и охлаждение под S21 Hydro. Боли: J/TH на фоне hashprice, теплоотвод (air vs hydro), плотность мощности на стойку.
- **Действие после чтения:** переход на `/en/firmwares/antminer#s21` (настройка эффективности), для Hydro — на `/en/asics-cooling/hydro-systems`.
- **Почему P0 при малом GSC:**
  - самый большой измеренный спрос в firmware-кластере блога: antminer s21 1 000/мес, s21 pro 480, s21 xp 320 (US), CPC $1.94–3.22;
  - у сайта нет страницы, которая отвечает на информационный S21-запрос: в GSC по «antminer s21» всего 2 показа (`/en/firmwares/antminer` поз. 4, `/` поз. 3), то есть вход в тему пустой;
  - сезон: по Google Trends US «antminer s21» растёт в ноябре–декабре (ноябрь 2025: 29–38) и пикует в апреле (75), сейчас (авг–окт 2026) 4–9. Пост должен быть проиндексирован до роста.

## 2. Ключи (только из данных)

Источники: `data/dfs-blog-plan-volumes-us-2026-09-28.json` (Google Ads US, 2026-09-28; «10» — порог 0–15); GSC — `data/gsc-queries-pages-all-2026-10-10.json` (2026-09-10..10-07, все страны, i/c/pos).

| Ключ | Объём US (CPC, конкуренция) | Динамика 6 мес (Ads) | GSC i/c/pos (28 дн) | Роль |
|---|---|---|---|---|
| antminer s21 | 1 000 ($1.94, HIGH) | 720 → 880 | 1 / 1 / 4 (`/en/firmwares/antminer`); 1 / 0 / 3 (`/`) | title, H1 |
| antminer s21 pro | 480 ($3.22, HIGH) | 210 → 320 | нет | H2 / строка таблицы |
| antminer s21 xp | 320 ($2.40, HIGH) | 260 стабильно | нет | H2 / строка таблицы |
| antminer s21 hydro | n/d в файле-источнике | — | нет | H2 про Hydro [VERIFY: в `content/briefs/antminer-s21-firmware.md` для этого ключа указано 90/мес из DFS 2026-09-25; в этот бриф не переносим, сверить] |
| antminer s21+ / s21 vs s19 pro | n/d | — | «antminer s21+» 1 / 0 / 10 (RU-документация, мусор); «antminer s21 vs s19 pro» 1 / 0 / 27 (`review-of-miners-2021-…`) | FAQ |
| antminer s21 profitability / s21 pro profitability | n/d | — | 1 / 0 / 96 и 1 / 0 / 62 (`/en/firmwares/antminer`) | только факторы в FAQ, без расчёта прибыли |
| **не брать в цель:** antminer s21 firmware, antminer s21 pro firmware, firmware antminer s21, antminer s21 firmware update | 10 / 10 / n/d / n/d (Ads, см. commercial-бриф) | — | 5 / 0 / 12.6; 6 / 0 / 22.7; 9 / 0 / 13.9; 4 / 0 / 22.2 — все на `/en/firmwares/antminer` | — (только ссылка на страницу прошивки; слово «firmware» в title и H1 не ставить) |

- SERP-особенность ниши: AI Overview в 28 из 30 отслеживаемых ключей, featured snippet в 0 из 30 (`data/serp-features/serp-features-2026-09-28.json`). По «antminer s21 firmware» AIO цитирует mineshop.eu, shop.bitmain.com, awesomeminer, vnish, nicehash; bixbit не цитируется, PAA есть. Формат — passage для AIO, а не «под сниппет».
- Отслеживание: в `data/rank-tracking/keywords.md` есть только «antminer s21 firmware» (#16, target `/en/firmwares/antminer`) — его не трогаем. Ключа «antminer s21» нет (проверено 2026-10-10). После публикации предложить человеку добавить его с target = этот пост (ротацию утверждает человек).

## 3. Title / description / H1
- **Title (≤60):** `Antminer S21 Series: S21 vs S21 Pro vs S21 XP vs Hydro` (54 симв.) [VERIFY длину в CMS с суффиксом бренда].
- **Description (≤155):** `Antminer S21, S21 Pro, S21 XP and Hydro models compared: hashrate, power draw, J/TH efficiency and the cooling and power each one needs on site.` (144 симв.)
- **H1:** `Antminer S21 Series Explained: S21, S21 Pro, S21 XP and Hydro Models`.
- Без «profitable», «ROI», «best miner to buy», без «no dev fee».

## 4. Структура (H2/H3) и AEO

Правила AEO (агент `geo-ai`): passage, который можно вырезать и процитировать без контекста; ответ в 40–60 слов сразу под H2-вопросом; цифры только [VERIFY]; таблица с единицами в заголовках, датой и источником; FAQ ≤ 80 слов на ответ. Featured snippet в нише не ловим (0 из 30), цель — цитата в AIO (28 из 30) и в ChatGPT/Perplexity.

1. **Лид (40–60 слов, passage для AIO):** что такое серия Antminer S21 (поколение Bitmain на SHA-256, год выхода [VERIFY]), какие модели в неё входят, чем они различаются: хешрейт, J/TH и тип охлаждения (air / hydro) [VERIFY]. Без маркетинга, без «revolutionary».
2. **H2 «Antminer S21 models at a glance»** — таблица:
   - колонки: Model / Hashrate (TH/s) / Power (W) / Efficiency (J/TH) / Cooling (air / hydro) / Release (year) / Input voltage (V);
   - строки: S21, S21 Pro, S21 XP, S21 Hydro, S21 XP Hydro, S21+ [VERIFY: какие модели включать, нет ли S21 Imm / S21+ Hydro];
   - **каждая ячейка [VERIFY по официальным спецификациям Bitmain]**, в подписи под таблицей: «Manufacturer specifications, checked YYYY-MM-DD» + ссылка на источник;
   - таблица HTML, не картинка (её цитируют LLM).
3. **H2 «Which Antminer S21 model should you run?»** — ответ в 40–60 слов сразу под заголовком: выбор определяется не прибылью, а тремя ограничениями площадки — доступная мощность на позицию, способ отвода тепла (воздух или жидкостный контур) и цена электроэнергии, к которой чувствителен J/TH. Затем H3 по сценариям:
   - H3 «Air-cooled sites: S21 and S21 Pro»;
   - H3 «Efficiency-first fleets: S21 XP»;
   - H3 «Liquid-cooled sites: S21 Hydro and S21 XP Hydro».
   В каждом — 2–3 предложения, цифры только из таблицы [VERIFY].
4. **H2 «S21 vs S19: what changed for operators»** — короткая таблица «S19 Pro / S19 XP → S21 / S21 XP» по J/TH и мощности [VERIFY] + абзац о том, что это значит для электрики и охлаждения. Ссылка на пост S19 (EN-OCT-1).
5. **H2 «Cooling and power requirements for the S21 lineup»**:
   - H3 «Air-cooled S21 units: airflow, intake temperature, noise» — диапазоны рабочей температуры [VERIFY по Bitmain];
   - H3 «S21 Hydro: what the liquid loop needs» — расход, температура подачи, требования к теплоносителю [VERIFY]; ссылка на `/en/asics-cooling/hydro-systems` и на AHR-200 [VERIFY: совместимость AHR-200 с S21 Hydro];
   - H3 «Power: voltage, phase and PDU sizing» — входное напряжение и потребление [VERIFY]; ссылка на `/en/products/pdu` [VERIFY: подходит ли PDU под S21].
6. **H2 «Tuning S21 efficiency with firmware»** — 1 абзац (≤90 слов) + ссылка, без цифр прироста:
   - какие режимы бывают в принципе: autotuning, underclocking/undervolting под дешёвую или дорогую энергию, overclocking при запасе по охлаждению;
   - поддерживает ли прошивка BiXBiT каждую модель S21 [VERIFY: список моделей и плат управления];
   - dev fee: «BiXBiT firmware uses a transparent dev fee [VERIFY: current rate with the team]»; ссылка на `/en/firmwares/dev-fee` только если страница уже вышла (W4);
   - ссылка на `/en/firmwares/comparison` — **только после её публикации (W6, 9–15 ноября)**. Если пост выходит раньше, ссылку добавить отдельной правкой после W6.
7. **H2 «Monitoring an S21 fleet»** — 2–3 предложения: что важно мониторить у S21 (хешрейт по платам, температура чипов, потребление, для Hydro — температура контура) [VERIFY: какие метрики реально видны в AMS]; ссылка на `/en/ams`.
8. **H2 «Antminer S21 FAQ»** — 5–6 вопросов, ответ ≤ 80 слов (PAA-тексты по S21 в снимке serp-features не сохранены: перед написанием проверить PAA вручную по «antminer s21», «antminer s21 pro» [VERIFY]):
   - «What is the difference between the Antminer S21 and S21 Pro?» [VERIFY цифры];
   - «S21 Pro vs S21 XP: which is more efficient?» [VERIFY];
   - «Does the S21 Hydro need a special cooling system?» → ссылка на hydro-systems;
   - «How much more efficient is the S21 than the S19 Pro?» (GSC «antminer s21 vs s19 pro») [VERIFY];
   - «Is the Antminer S21 profitable?» — ответ только через факторы (энергия, hashprice, J/TH, аптайм), без «да/нет» и без сроков окупаемости; ссылка на `/en/calc` с пометкой «model your own numbers»;
   - «Can you run custom firmware on the Antminer S21?» → короткий ответ + ссылка на `/en/firmwares/antminer#s21` [VERIFY поддержку].

## 5. Сущности и термины
Bitmain, Antminer S21 / S21 Pro / S21 XP / S21 Hydro / S21 XP Hydro / S21+ [VERIFY состав], Antminer S19 Pro / S19 XP (для сравнения), SHA-256, TH/s, J/TH, hashprice, hashboard, control board, air cooling, hydro (liquid) cooling, coolant loop, intake temperature, PDU, three-phase power, autotuning, underclocking, overclocking, fleet monitoring.

## 6. Факты на проверку [VERIFY]
- Состав линейки S21 и годы выхода каждой модели.
- Хешрейт (TH/s), мощность (W), J/TH, входное напряжение, рабочий диапазон температур — по каждой модели, с датой и URL спецификации Bitmain.
- Требования S21 Hydro к контуру: расход, температура подачи, теплоноситель.
- Совместимость AHR-200 и других hydro-систем BiXBiT с S21 Hydro; совместимость PDU.
- Какие модели S21 и какие платы управления поддерживает прошивка BiXBiT; какие режимы тюнинга доступны на S21.
- Ставка dev fee: «transparent dev fee [VERIFY: current rate with the team]». Сайт сам противоречив (`/en/faq` 1.8–2.8%, страницы серий 2.8%), брать ставку только у команды.
- Какие метрики S21 видны в AMS.
- Id фрагмента `#s21` на `/en/firmwares/antminer` и наличие там секции S21 / S21 Hydro.
- Слаг нового поста.

## 7. Внутренние ссылки
| Куда | Анкор (пример) | Где в тексте | Обязательна? |
|---|---|---|---|
| `/en/firmwares/antminer#s21` | tuning modes available for the S21 lineup | H2 «Tuning S21 efficiency» | да |
| `/en/firmwares/antminer#s21` | custom firmware support for the S21 | FAQ | да (второе вхождение, другой анкор) |
| `/en/asics-cooling/hydro-systems` | liquid cooling systems for S21 Hydro units | H3 «S21 Hydro» | да |
| `/en/asics-cooling/hydro-systems/ahr-200` | AHR-200 hydro rack for Antminer | H3 «S21 Hydro» | после [VERIFY] совместимости |
| `/en/ams` | track S21 hashrate and chip temperatures across sites | H2 «Monitoring» | да |
| `/en/products/pdu` | sizing power distribution for S21 racks | H3 «Power» | после [VERIFY] |
| `/en/calc` | model your own S21 numbers | FAQ «Is the S21 profitable?» | да |
| `/en/firmwares/dev-fee` | how the firmware dev fee is charged | H2 «Tuning» | только после выхода (W4) |
| `/en/firmwares/comparison` | how S21 firmware options compare | H2 «Tuning» | **только после W6** |
| `/en/blog/post/antminer-19-series-profitability-and-price-guide` | Antminer S19 series guide | H2 «S21 vs S19» | да |
| `/en/blog/post/hydro-asic-2026-ranking-models-for-largescale-mining-farms` | hydro ASIC models ranked for large farms | H3 «S21 Hydro» | желательно |

- Анкоры не повторяют закреплённые в матрице v2: «firmware for Antminer S21 Hydro» (H7, hydro-systems → antminer), «Antminer firmware» (F22), «hydro cooling system(s)» (только hydro sub-hub в меню/хабе). Каждый анкор из таблицы — не больше чем на 2 страницах.
- Входящие (чек-лист §4, п. 6): из S19-гайда (EN-OCT-1, секция «newer models»), из `hydro-asic-2026-ranking-…`, позже из J/TH-поста EN-DEC-1 (уже в плане) и RU-NOV-2 как hreflang-пара. В матрице `content/internal-linking.md` строка H-B13 уже предусматривает EN-NOV-1.

## 8. Внешние источники (E-E-A-T)
- Официальные страницы моделей Bitmain (shop.bitmain.com / support.bitmain.com) — спецификации с датой проверки [VERIFY URL].
- Собственные замеры BiXBiT на S21 (стенд, методика, дата), если есть [VERIFY]; если нет — цифры из прошивки не приводить.
- Подпись автора-инженера с должностью и дата последней тех-проверки над статьёй (§6 вопрос 7).

## 9. Запреты
- Никакой доходности, сроков окупаемости и прогнозов hashprice/BTC; «profitable» только в вопросе FAQ с ответом через факторы.
- Не писать «no dev fee» / «zero fee»: только «transparent dev fee» с подтверждённой ставкой.
- Не обещать прирост хешрейта или J/TH от прошивки без протокола тестов.
- Не ставить ссылку на `/en/firmwares/comparison` и `/en/firmwares/dev-fee` до их публикации; не ссылаться на noindex legacy-страницы `/en/firmwares/asic-*`.
- Партнёрский домен (agent-knowledge §2) не упоминать.

## 10. После публикации
- Чек-лист `content/blog-plan.md` §4 (JSON-LD `BlogPosting` + `BreadcrumbList` + `FAQPage` по видимому FAQ; переобход через `index-submit.py`).
- Отдельная правка после W6: добавить ссылку на `/en/firmwares/comparison`.
- Через 28 дней: GSC по посту (`--dimensions query,page --page-contains antminer-s21-series`) — antminer s21, s21 pro, s21 xp, s21 hydro; переходы пост → `/en/firmwares/antminer` (GA4); позиции `/en/firmwares/antminer` по «antminer s21 firmware» не должны просесть (каннибализация).
- Через месяц `./scripts/serp-features.py --keywords "antminer s21,antminer s21 pro,antminer s21 xp"`: есть ли цитата в AIO.
- Предложить человеку добавить «antminer s21» в `data/rank-tracking/keywords.md`.
