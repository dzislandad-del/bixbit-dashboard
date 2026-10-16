# Бриф: Antminer S19 Series Guide (обновление)

**ID плана:** EN-OCT-1 · **Язык:** EN · **Тип:** обновление, URL не меняется · **Приоритет:** P0
**URL:** `/en/blog/post/antminer-19-series-profitability-and-price-guide` (слаг не трогаем: у поста 20 310 показов за 90 дней)
**Пара hreflang:** `/ru/blog/post/bitmain-vypustil-modeli-antminer-s19-i-antminer-s19-pro-harakteristiki-i-pribylnost` (обновление RU-DEC-3). Связь переводов делается в CMS, как только RU-версия обновлена
**Поддерживает (architecture v2):** `/en/firmwares/antminer#s19`. Пост закрывает запросы о характеристиках и экономике S19 (информационный интент) и ведёт на коммерческую секцию. Запрос «antminer s19 firmware» у страницы прошивки **не забирает**
**Автор / ревьюер:** [VERIFY: инженер BiXBiT] / [VERIFY] · **Дата проверки фактов:** —

## 1. Цель и интент
- **Интент:** informational/commercial research. Человек выбирает или эксплуатирует S19, S19 Pro, S19 XP и хочет понять характеристики, эффективность и то, от чего зависит экономика.
- **Читатель:** оператор фермы с парком S19. Его боль — J/TH старого парка на фоне новых моделей.
- **Действие после чтения:** переход на `/en/firmwares/antminer#s19` (настройка эффективности) и в `/en/calc`.
- **Почему P0:**
  - самый видимый релевантный пост блога: GSC 90 дн — 20 310 показов / 38 кликов / поз. 7.4; Bing 12 мес — 2 894 / 45;
  - ChatGPT цитирует копию этого поста на `bixbit.tech` (competitor-gap ePIC, GEO);
  - контекстной ссылки на `/en/firmwares/antminer` сейчас нет. Есть только ссылка на noindex `/en/firmwares/asic-s19`.

## 2. Ключи
| Ключ | Объём | GSC (28 дн, пост) | Роль |
|---|---|---|---|
| antminer s19 pro | 590 (US, dfs-blog-plan-volumes 09-28) | 48 / 0 / поз. 21 | H1, title |
| antminer s19 xp | 170 | «antminer s19 xp profitability» 8 / поз. 12 | H2 |
| antminer s19 pro profitability | n/d | 64 / 0 / поз. 8 | H2 «What drives S19 profitability» (факторы, не обещания) |
| antminer s19 | n/d (в выборке нет) | 77 / 0 / поз. 20 | в тексте |
| antminer s19 efficiency j/th | n/d | 8 / 0 / поз. 6 | H2 про эффективность |
| **не брать в цель:** antminer s19 firmware, antminer s19 overclock | — | принадлежат `/en/firmwares/antminer` | только ссылка |

## 3. Title / description / H1
- **Title (≤60):** `Antminer S19 Series Guide: S19, S19 Pro & XP Specs and Efficiency` [VERIFY длина].
- **Description (≤155):** `Antminer S19, S19 Pro and S19 XP compared: hashrate, power draw, J/TH efficiency and the factors that decide whether an S19 fleet stays viable.`
  - Убрать из текущего description «ROI» и «for profitable Bitcoin mining».
- **H1:** `Antminer S19 Series: Specs, Efficiency and What Drives Profitability`.

## 4. Структура и AEO
1. **Лид (40–60 слов):** что такое серия S19, какие модели в неё входят и чем они отличаются по J/TH [VERIFY]. Без маркетинга.
2. **H2 «Antminer S19 models compared»** — таблица: модель / хешрейт TH/s / мощность W / J/TH / охлаждение (air / hydro) / год выхода.
   - Все цифры [VERIFY по спецификациям Bitmain]. В подписи — дата и источник данных.
3. **H2 «Which S19 model is the most efficient?»** — ответ в 40–60 слов сразу под заголовком, затем пояснение.
4. **H2 «What drives S19 profitability (and what you can control)»** — только факторы, без расчёта «вы заработаете X»:
   - цена электроэнергии, hashprice, J/TH, аптайм, охлаждение;
   - ссылка «model your own numbers in the BiXBiT calculator» → `/en/calc`.
5. **H2 «Improving S19 efficiency with firmware tuning»** — коротко: какие режимы бывают (autotuning, undervolting, overclocking).
   - Подробности даёт ссылка на `/en/firmwares/antminer#s19`.
   - Прирост в % и J/TH — только [VERIFY: подтверждённые тесты BiXBiT]; если данных нет, цифр не писать.
   - Dev fee упомянуть как «transparent dev fee [VERIFY: current rate with the team]» со ссылкой на `/en/firmwares/dev-fee`, когда она выйдет (W4).
6. **H2 «Cooling S19 units: air, hydro, immersion»** — 2–3 абзаца со ссылкой на immersion-systems.
7. **H2 «Monitoring an S19 fleet»** — ссылка на `/en/ams`.
8. **FAQ (4–5 вопросов):**
   - «Is the Antminer S19 still worth running?» — ответ только через факторы, без да/нет по прибыли;
   - «S19 Pro vs S19 XP: what's the difference?»;
   - «What is the S19 Pro's efficiency in J/TH?» [VERIFY];
   - «Can the S19 be overclocked?» → ссылка на страницу прошивки;
   - «How long does an S19 last?» [VERIFY].

## 5. Сущности
Bitmain, Antminer S19 / S19 Pro / S19j Pro / S19 XP / S19 XP Hyd, SHA-256, J/TH, hashprice, autotuning, hydro cooling, immersion cooling.

## 6. [VERIFY]
- Хешрейт, мощность, J/TH каждой модели (спецификации Bitmain, с датой).
- Модели S19, поддерживаемые прошивкой BiXBiT.
- Любые цифры прироста от прошивки.
- Ставка dev fee.
- Срок службы.

## 7. Внутренние ссылки
| Куда | Анкор (пример) | Где | Обяз. |
|---|---|---|---|
| `/en/firmwares/antminer#s19` | tune S19 efficiency with BiXBiT firmware | секция про firmware tuning | да |
| `/en/calc` | model S19 economics for your power price | секция про profitability | да |
| `/en/ams` | monitor S19 hashrate and temperatures across a fleet | секция про мониторинг | да |
| `/en/asics-cooling/immersion-systems` | running S19 units in immersion | секция про охлаждение | да |
| `/en/firmwares/dev-fee` | how the firmware dev fee works | секция про firmware tuning, после W4 | после выхода |
| `/en/blog/post/antminer-s19-pro-vs-whatsminer-m30-…` | S19 Pro vs Whatsminer M30 | FAQ | да |

- Убрать ссылку на noindex `/en/firmwares/asic-s19` (гигиена H3).

## 8. Внешние источники
Спецификации Bitmain (официальная страница модели) [VERIFY URL]; протокол тестов BiXBiT, если есть [VERIFY].

## 9. Запреты
- Никаких «profitable», «ROI in N months», «guaranteed».
- Не писать «no dev fee».
- Прогнозов цены BTC нет.

## 10. После публикации
- Чек-лист `content/blog-plan.md` §4.
- Отдельно `/geo-check` через месяц: цитирует ли ChatGPT `bixbit.io`, а не `bixbit.tech`.
- Замер через 28 дней: antminer s19 pro, antminer s19 pro profitability, переходы с поста на `/en/firmwares/antminer` (GA4).
