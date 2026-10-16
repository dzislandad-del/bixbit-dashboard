# Бриф: What Is PUE in a Data Center (обновление)

**ID плана:** EN-OCT-3 · **Язык:** EN · **Тип:** обновление, URL не меняется · **Приоритет:** P1
**URL:** `/en/blog/post/how-to-calculate-the-pue-of-a-datacenter`
**Пара hreflang:** RU-версия поста не найдена [VERIFY в CMS]. Если её нет, hreflang не ставить
**Поддерживает (architecture v2):** `/en/asics-cooling/immersion-systems`, `/en/asics-cooling/hydro-systems`. Пост — вход техдиректоров ДЦ (ICP) в кластер охлаждения
**Автор / ревьюер:** [VERIFY: инженер по охлаждению] · **Дата проверки:** —

## 1. Цель и интент
- **Интент:** informational — определение и формула PUE, пример расчёта.
- **Читатель:** техдиректор ДЦ или хостинг-провайдер, который считает энергоэффективность площадки.
- **Действие после чтения:** перейти к сравнению охлаждения (hydro/immersion) как рычагу PUE.
- **Почему сейчас:**
  - спрос: `data center pue` 1 000/мес (CPC $7.17), `what is pue` 590, `pue calculation` 170 (US, dfs-blog-plan-volumes 2026-09-28);
  - Bing 12 мес — 2 788 показов / 16 кликов, второй пост блога в Bing;
  - Google 90 дн — 1 733 показа, поз. 37.9, при этом по `data center pue` поз. 6.5;
  - в постановке задачи пост назван нерелевантным; предлагаю оставить (решение команды, `content/blog-plan.md` §6, вопрос 6).

## 2. Ключи
| Ключ | Объём (US) | GSC 28 дн | Роль |
|---|---|---|---|
| data center pue | 1 000 | 33 / 0 / поз. 6.5 | title, H1 |
| what is pue | 590 | 12 / поз. 49 | лид (определение) |
| pue calculation | 170 | 15 / поз. 34 | H2 с формулой |
| pue formula, calculate pue | n/d | 12 / поз. 47; 6 / поз. 44 | H2 |
| «pue 1.1 achievable? what does it actually take?» | n/d | 7 / поз. 85 | вопрос в FAQ |

## 3. Title / description / H1
Текущие title и description в порядке («What Is PUE in a Data Center? Formula and How to Calculate It»), их оставляем. Меняем:
- **H1:** `What Is PUE in a Data Center and How to Calculate It`.
- **Description:** добавить «…and how cooling choice (air, hydro, immersion) changes it» [≤155].

## 4. Структура и AEO
1. **Лид (40–60 слов):** определение PUE как отношения полной мощности объекта к мощности ИТ-нагрузки; идеал = 1.0. Это passage для AIO по «what is pue».
2. **H2 «PUE formula»:** формула отдельной строкой, расшифровка переменных.
3. **H2 «How to calculate PUE: step-by-step example»:** 4–5 нумерованных шагов с условным примером. В тексте пометить, что числа иллюстративные.
4. **H2 «What is a good PUE?»:** ответ в 40–60 слов. Диапазоны давать только со ссылкой на внешний источник (например, отраслевые опросы) [VERIFY источник и год].
5. **H2 «PUE in bitcoin mining facilities»:** чем майнинговая площадка отличается от классического ДЦ (плотность, профиль нагрузки 24/7).
6. **H2 «How cooling choice affects PUE: air vs hydro vs immersion»:** таблица с качественными факторами (вентиляторы, чиллеры, драйкулеры, насосы). Числа PUE для решений BiXBiT — только [VERIFY: измерения на объектах], иначе без чисел.
   - Ссылки на immersion-systems и hydro-systems.
7. **H2 «Measuring PUE continuously»:** учёт мощности на уровне стойки и устройства → `/en/products/pdu` [VERIFY: умеет ли PDU мерить] и `/en/ams` [VERIFY: функция].
8. **FAQ (4–5 вопросов):**
   - «Is a PUE of 1.1 achievable?»;
   - «PUE vs DCiE»;
   - «Does immersion cooling lower PUE?» [VERIFY];
   - «How often should PUE be measured?».

## 5. Сущности
Power Usage Effectiveness, DCiE, The Green Grid, IT load, chillers, dry coolers, CRAC, direct-to-chip (hydro), single-phase immersion.

## 6. [VERIFY]
Диапазоны PUE по отрасли (источник и год); PUE на объектах BiXBiT; возможности PDU и AMS по учёту мощности.

## 7. Внутренние ссылки
| Куда | Анкор (пример) | Где | Обяз. |
|---|---|---|---|
| `/en/asics-cooling/immersion-systems` | immersion cooling systems for high-density mining | секция про охлаждение | да |
| `/en/asics-cooling/hydro-systems` | hydro (direct-to-chip) cooling for ASICs | секция про охлаждение | да |
| `/en/products/pdu` | rack-level power metering | секция про измерение | да (PDU: 0 ссылок из блога) |
| `/en/ams` | track power and uptime per unit | секция про измерение | да |
| `/en/blog/post/datacenter-cooling-methods-everything-you-need-to-know` | data center cooling methods | вводная часть | да |

## 8. Запреты
Не обещать экономию в $ и не давать «PUE гарантированно ниже X». Никаких юр-утверждений о соответствии нормам.

## 9. Замер
Через 28 дней: data center pue, what is pue, pue calculation (GSC); Bing — клики поста; переходы на immersion-systems и hydro-systems (GA4).
