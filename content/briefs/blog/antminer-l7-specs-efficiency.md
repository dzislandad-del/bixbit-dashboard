# Бриф: Bitmain Antminer L7 Review: Specs and Efficiency (обновление)

**ID плана:** EN-OCT-4 · **Язык:** EN · **Тип:** обновление, URL не меняется · **Приоритет:** P1
**URL:** `/en/blog/post/bitmain-antminer-l7-review-specifications-price-payback`. Слаг не меняем, хотя в нём есть «payback»: у поста 8 553 показа за 90 дн и 19 входящих ссылок, смена URL дороже слова в слаге. Если команда всё же захочет новый слаг — только 301 и только решением команды
**Пара hreflang:** `/ru/blog/post/obzor-bitmain-antminer-l7-harakteristiki-cena-okupaemost` (тот же тип материала — обзор). **Не** `razgon-antminer-l7`: это пост про разгон, у него своя тема (RU-OCT-4)
**Поддерживает:** зависит от ответа команды на §6 вопрос 8 (поддерживает ли прошивка BiXBiT Antminer L7):
- **Вариант A (поддержка подтверждена):** `/en/firmwares/antminer#l7` [VERIFY: есть ли секция L7 и её id]. Пост закрывает запросы о характеристиках L7 и ведёт в секцию прошивки.
- **Вариант B (не подтверждена или нет):** `/en/ams` (мониторинг L7 [VERIFY]) и `/en/calc` (если калькулятор считает Scrypt [VERIFY]). Секции про прошивку BiXBiT нет совсем.
**Автор / ревьюер:** [VERIFY: инженер BiXBiT] / [VERIFY] · **Дата проверки фактов:** —
**Бриф подготовлен:** 2026-10-10

## 1. Цель и интент
- **Интент:** informational / commercial research. Человек выбирает или эксплуатирует Antminer L7 (Scrypt, LTC/DOGE [VERIFY]) и ищет характеристики, потребление и эффективность. Значимая доля запросов — «profitability» (antminer l7 profitability 60 показов, l7 profitability 31, l7 antminer profitability 20, l7 miner profitability 18): на них отвечаем **факторами**, а не цифрами прибыли или окупаемости.
- **Главная правка:** убрать обещания окупаемости («payback», «ROI», «pays for itself in N months», цены с расчётом срока возврата) из title, description, H1, H2 и текста.
- **Чем пост отличается от `/en/firmwares/antminer`:** страница прошивки отвечает на «antminer l7 custom firmware» (26 показов, поз. 14.5) и «antminer l7 overclock firmware» (38 показов). Пост эти запросы **не забирает**: в варианте A — один абзац и ссылка, в варианте B — ничего о прошивке BiXBiT.
- **Каннибализация cross-locale (`data/cannibalization/cannibal-2026-10-10.json`):**
  - bitmain antminer l7 — 121 показ: EN-пост 89 / поз. 9.1, RU `razgon-antminer-l7` 26 / поз. 16.7;
  - l7 miner — 57: EN 50 / 13.5, RU razgon 7 / 18.3;
  - l7 antminer — 47: EN 38 / 12.6, RU razgon 6 / 17.3.
  Причина — нет hreflang (K7 в `content/blog-plan.md` §1.4). Лечится связкой EN-пост ↔ RU-обзор в CMS (§4 чек-листа, п. 8), а не переписыванием текста. В RU `razgon-antminer-l7` ссылку на EN-обзор не ставить.
- **Читатель (ICP):** оператор с парком Scrypt-оборудования или хостинг-провайдер, который размещает L7 клиентов. Боли: потребление и J/MH, температура, шум, аптайм.
- **Действие после чтения:** A — `/en/firmwares/antminer#l7`; B — `/en/ams` и `/en/calc`.

## 2. Ключи (только из данных)

Источники: `data/dfs-blog-plan-volumes-us-2026-09-28.json` (Google Ads US); GSC — `data/gsc-blog-queries-pages-2026-10-10.json` (2026-09-10..10-07, все страны, пост). Пост целиком за 28 дн: 1 492 показа / 2 клика / поз. 8.1 (`data/gsc-blog-pages-28d-2026-10-10.json`).

| Ключ | Объём US (CPC) | Динамика 6 мес (Ads) | GSC i/c/pos (пост, 28 дн) | Роль |
|---|---|---|---|---|
| antminer l7 | 210 ($2.15, HIGH) | 70 → 210, растёт | 120 / 0 / 11.1 | title, H1 |
| bitmain antminer l7 | n/d | — | 89 / 0 / 9.1 (+ RU razgon 26 / 16.7) | H1 |
| bitmain antminer l7 review | n/d | — | 22 / 0 / 1.4 | H1 («Review» оставить) |
| antminer l7 specs / specifications | n/d | — | 19 / 0 / 4.2; 10 / 0 / 4.3 | H2 + таблица |
| antminer l7 power consumption | n/d | — | 10 / 0 / 6.8 | H2 / строка таблицы |
| l7 miner / l7 antminer | n/d | — | 50 / 0 / 13.5; 38 / 0 / 12.6 | в тексте |
| antminer l7 profitability (+ l7 profitability, l7 miner profitability, bitmain antminer l7 profitability) | n/d | — | 60 / 0 / 8; 31 / 0 / 9.3; 18 / 0 / 8.1; 13 / 0 / 7.2 | H2 «What determines L7 economics» — только факторы |
| bitmain antminer l7 9050m / 8800 / 9.5 gh/s / l7-9160m | n/d | — | 10 / 11.9; 5 / 11.6; 6 / 10.3; 4 / 9.2 | строки таблицы версий [VERIFY] |
| l7 dogecoin | n/d | — | 12 / 0 / 10 | H2 «What coins does the L7 mine?» |
| antminer l7 overclock | n/d | — | 12 / 0 / 17.7 | вариант A: FAQ со ссылкой; вариант B: FAQ без BiXBiT |
| antminer l7 price | n/d | — | 9 / 0 / 12.6 | не цель: цены устаревают, в посте не указывать |
| **не брать в цель (страница прошивки):** antminer l7 custom firmware, antminer l7 overclock firmware, antminer l7 firmware | n/d | — | 26 показов (`/en/firmwares/antminer` 14.5); 38 (S17-пост, `/en/firmwares/antminer` 27.2, noindex legacy `asic-S17-S17Pro`) | — |

- Ключа «antminer l7» нет в `data/rank-tracking/keywords.md`. Если вариант A, предложить человеку добавить «antminer l7 custom firmware» с target `/en/firmwares/antminer` (ротацию утверждает человек).

## 3. Title / description / H1
- **Title (≤60):** `Antminer L7 Specs: Hashrate, Power Draw and Efficiency` (54 симв.).
- **Description (≤155):** `Bitmain Antminer L7 specifications by version: hashrate, power consumption, efficiency, cooling and the factors that decide how an L7 fleet performs.` (149 симв.)
- **H1:** `Bitmain Antminer L7 Review: Specifications, Efficiency and Operating Requirements`.
- Убрать из текущего title «Payback & Price» (сейчас: «Bitmain Antminer L7 Review – Specifications, Payback & Price»).

## 4. Структура (H2/H3) и AEO

AEO по правилам `geo-ai`: AIO в 28 из 30 ключей ниши, featured snippet в 0 из 30. Passage: определение 40–60 слов, таблица версий с единицами и датой, ответы 40–60 слов под H2-вопросами, FAQ ≤ 80 слов.

1. **Лид (40–60 слов, passage):** что такое Antminer L7: Scrypt-майнер Bitmain для Litecoin и Dogecoin (merged mining [VERIFY]), год выхода [VERIFY], выпускался в нескольких версиях по хешрейту (MH/s) [VERIFY список], воздушное охлаждение [VERIFY]. Без цен и без окупаемости.
2. **H2 «Antminer L7 specifications by version»** — таблица:
   - колонки: Version / Hashrate (MH/s) / Power (W) / Efficiency (J/MH) / Cooling / Noise (dB) / Operating temperature (°C) / Input voltage (V);
   - строки: версии, которые встречаются в запросах (8800, 9050, 9160, 9300, 9500 MH/s) [VERIFY: какие реально выпускались];
   - **каждая ячейка [VERIFY по спецификации Bitmain]**, подпись: источник и дата проверки. Таблица HTML.
3. **H2 «What coins does the Antminer L7 mine?»** — ответ в 40–60 слов: алгоритм Scrypt, Litecoin, Dogecoin через merged mining, пулы, которые это поддерживают [VERIFY]. Без прогнозов курсов.
4. **H2 «How efficient is the Antminer L7?»** — ответ в 40–60 слов: J/MH по версиям [VERIFY], что это значит при разной цене энергии (качественно), как L7 соотносится с более новыми Scrypt-моделями (L9 и т.п.) — только если есть проверенные спецификации [VERIFY], иначе сравнение не делать.
5. **H2 «What determines L7 economics»** (закрывает запросы «profitability» без обещаний):
   - факторы: цена электроэнергии, J/MH, сложность сети и награда за блок LTC/DOGE, аптайм, охлаждение, комиссия пула;
   - явная фраза: «This article does not estimate profit or payback; numbers change daily» — или эквивалент;
   - ссылка на `/en/calc` **только если калькулятор поддерживает Scrypt/L7** [VERIFY]; иначе ссылку не ставить.
   - Удалить старые таблицы «payback period», «daily profit», «price» целиком.
6. **H2 «Operating the L7: cooling, power and noise»** — воздушный поток, температура на входе, пыль, шум, электрика [VERIFY диапазоны]. Если иммерсия L7 подтверждена инженерами — 1 абзац со ссылкой на `/en/asics-cooling/immersion-systems` [VERIFY], иначе не упоминать.
7. **H2 «Tuning the L7 with firmware»** — **только вариант A**:
   - 1 абзац (≤90 слов): какие режимы доступны на L7 в прошивке BiXBiT [VERIFY], без цифр прироста, если нет протокола тестов;
   - dev fee: «transparent dev fee [VERIFY: current rate with the team]», ссылка на `/en/firmwares/dev-fee` после W4;
   - ссылка на `/en/firmwares/antminer#l7`.
   **Вариант B:** раздел удаляется целиком. Вместо него можно (не обязательно) нейтральный абзац «Stock vs custom firmware on Scrypt miners» без упоминания BiXBiT как поставщика для L7 и без ссылок на страницу прошивки.
8. **H2 «Monitoring an L7 fleet»** — что отслеживать (хешрейт по платам, температура, ошибки вентиляторов); ссылка на `/en/ams` **если AMS поддерживает L7** [VERIFY]. В варианте B это главная продуктовая ссылка поста.
9. **H2 «Antminer L7 FAQ»** (4–5 вопросов, ответ ≤ 80 слов):
   - «What is the hashrate of the Antminer L7?» [VERIFY];
   - «How much power does the Antminer L7 use?» [VERIFY];
   - «Can you mine Dogecoin with the L7?» [VERIFY];
   - «Can you overclock the Antminer L7?» — A: зависит от прошивки, охлаждения и запаса БП; ссылка на `/en/firmwares/antminer#l7` [VERIFY]. B: общий ответ без BiXBiT и без ссылки на прошивку; цифры «+X%» не писать;
   - «Is the Antminer L7 still profitable?» — ответ только через факторы, без «да/нет» и сроков.

## 5. Сущности и термины
Bitmain, Antminer L7 (версии по MH/s [VERIFY]), Scrypt, Litecoin (LTC), Dogecoin (DOGE), merged mining, MH/s, J/MH, hashboard, control board, PSU, air cooling, intake temperature, mining pool, network difficulty, uptime; для варианта A — autotuning, underclocking, overclocking.

## 6. Факты на проверку [VERIFY]
- **Поддержка L7 прошивкой BiXBiT** (§6 вопрос 8 в `content/blog-plan.md`; в меню сайта есть «Antminer L7», но статус не подтверждён). Определяет вариант A или B.
- Есть ли на `/en/firmwares/antminer` секция L7 и её id фрагмента.
- Поддерживает ли AMS L7; считает ли `/en/calc` Scrypt.
- Версии L7 и по каждой: MH/s, W, J/MH, шум, рабочая температура, напряжение (спецификация Bitmain, дата).
- Год выхода; merged mining LTC+DOGE.
- Совместимость с иммерсией (если упоминаем).
- Режимы тюнинга и любые цифры прироста (только вариант A, только с протоколом).
- Ставка dev fee (только вариант A): «transparent dev fee [VERIFY: current rate with the team]».

## 7. Внутренние ссылки

**Вариант A (поддержка подтверждена):**
| Куда | Анкор | Где в тексте | Обязательна? |
|---|---|---|---|
| `/en/firmwares/antminer#l7` | L7 tuning modes in BiXBiT firmware | H2 «Tuning the L7» | да |
| `/en/firmwares/antminer#l7` | overclocking the L7 safely | FAQ «Can you overclock» | да (другой анкор) |
| `/en/ams` | monitor L7 hashboards and temperatures | H2 «Monitoring» | да [VERIFY поддержку] |
| `/en/calc` | run L7 numbers for your power price | H2 «Economics» | только если калькулятор считает Scrypt |
| `/en/firmwares/dev-fee` | how the firmware dev fee works | H2 «Tuning» | после W4 |

**Вариант B (поддержки нет):**
| Куда | Анкор | Где в тексте | Обязательна? |
|---|---|---|---|
| `/en/ams` | monitor L7 hashboards and temperatures | H2 «Monitoring» | да [VERIFY поддержку L7] |
| `/en/calc` | run L7 numbers for your power price | H2 «Economics» | только если калькулятор считает Scrypt |
| `/en/asics-cooling` | cooling options for mining farms | H2 «Operating the L7» | желательно |

**Оба варианта — соседние посты:**
| Куда | Анкор | Где | Обязательна? |
|---|---|---|---|
| `/en/blog/post/antminer-19-series-profitability-and-price-guide` | Antminer S19 series specs for SHA-256 fleets | лид или H2 «How efficient» (контраст SHA-256 vs Scrypt) | желательно |

- Требование шаблона «≥ 2 контекстные ссылки на продвигаемые страницы» в варианте B выполняется, только если AMS и калькулятор поддерживают L7. Если нет ни того, ни другого — у поста нет продвигаемой страницы, и команде стоит решить, держать ли его в плане (понизить до P3 или оставить как гигиену без продвижения).
- Убрать из текста ссылки на noindex legacy-страницы прошивок (`/en/firmwares/asic-*`), если они есть.
- Анкор «Antminer firmware» дословно не использовать (закреплён за F22).

## 8. Внешние источники (E-E-A-T)
- Официальная страница L7 у Bitmain (спецификации по версиям) [VERIFY URL и дату].
- Для merged mining — документация пула или Litecoin/Dogecoin [VERIFY].
- Протокол тестов BiXBiT на L7 — только вариант A и только если существует [VERIFY].

## 9. Запреты
- Никаких сроков окупаемости, ROI, «daily profit», цен с расчётом возврата, прогнозов курсов LTC/DOGE, инвест-советов.
- В варианте B — ни слова о том, что BiXBiT прошивает L7; ссылок на страницу прошивки с L7-анкором нет.
- Не писать «no dev fee»; не обещать прирост хешрейта без протокола.
- Не ставить ссылку на `/en/firmwares/dev-fee` до W4 и на `/en/firmwares/comparison` до W6.
- Партнёрский домен (agent-knowledge §2) не упоминать.

## 10. После публикации
- Чек-лист `content/blog-plan.md` §4; связать hreflang EN ↔ RU `obzor-bitmain-antminer-l7-…` (RU-обзор тоже содержит «окупаемость» в title — отдельная RU-задача, в этот бриф не входит; отметить для RU-плана).
- Через 28 дней: GSC по посту — antminer l7, bitmain antminer l7, antminer l7 specs; доля RU `razgon-antminer-l7` в паре «bitmain antminer l7» (baseline 26 из 121 показов) должна упасть после hreflang.
- Вариант A: переходы пост → `/en/firmwares/antminer` (GA4), позиция `/en/firmwares/antminer` по «antminer l7 custom firmware» (baseline 14.5).
- CTR поста: сейчас 2 клика на 1 492 показа при поз. 8.1 — главный индикатор того, что новый title работает.
