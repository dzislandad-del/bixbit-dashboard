# Бриф: Bitcoin Mining Containers: Types, Site Requirements and Planning Checklist (обновление)

**ID плана:** EN-NOV-4 (перенесён из EN-FEB-4, группа K4) · **Язык:** EN · **Тип:** обновление, URL не меняется · **Приоритет:** P1 (поднят с P2 из-за сезона и каннибализации)
**URL:** `/en/blog/post/how-shipping-containers-change-the-cryptocurrency-mining-industry` (слаг не трогаем: 22 входящие ссылки, история показов) · **Пара hreflang:** `/ru/blog/post/kak-konteynery-dlya-mayninga-menyayut-industriyu-dobychi-kriptovalyut` (RU-DEC-2). Связь переводов в CMS после обновления RU-версии
**Поддерживает:** `/en/products/container` (hardware-расширение, не входит в 17 URL v2; коммерческий бриф `content/briefs/hardware-mining-container.md`). Пост забирает информационный спрос (какие бывают контейнеры, что нужно площадке, как планировать) и отдаёт товарной странице коммерческий («for sale», «price», «crypto mining shipping container»). Вторично — `/en/asics-cooling/hydro-systems` и `/en/products/container-hydro`
**Автор / ревьюер:** [VERIFY: инженер, который вводил контейнеры BiXBiT в эксплуатацию] / [VERIFY: продакт контейнеров] · **Дата проверки фактов:** —
**Бриф подготовлен:** 2026-10-10

> **Конфликт ID [решение владельца плана].** В `content/blog-plan.md` §2 строка EN-NOV-4 уже занята постом `how-to-detect-and-cure-an-asic-virus`. Нужно либо перенумеровать (например, вирус → EN-NOV-5 или перенос на декабрь), либо пересчитать нагрузку ноября: с этим постом EN = 5 ед. при допущении 4. Строку EN-FEB-4 в плане пометить «перенесено в ноябрь».

## Зависимость (обязательная)
**Публиковать после или одновременно с рефрешем `/en/products/container`** (бриф `hardware-mining-container.md`, P0). Причины:
- пост снимает с себя коммерческие формулировки и ставит ссылку на товар с коммерческим анкором. Если товарная страница ещё короткая (~930 слов, без таблиц и чек-листа), пользователь и AIO попадут на слабую страницу;
- в посте и на товаре не должно быть одного и того же блока. Чек-лист в посте — общий уровень («что проверить»), а инженерные значения (напряжение, фундамент, климат) живут только на товаре;
- сезон: «mining container» в US — 1 300 (окт 2025), 1 000 (ноя), 720 (дек), затем 20–110 (`data/dfs-blog-2026-10-10.json`). Обе страницы должны быть проиндексированы в октябре–начале ноября. Если товар задерживается, пост не публиковать раньше него, а выпустить в один день.

## 1. Цель и интент
- **Проблема (данные GSC 2026-09-10..10-07, `data/cannibalization/cannibal-2026-10-10.json`):** пара «пост ↔ `/en/products/container`» — третья по показам каннибализирующая пара сайта (637 показов). По одним и тем же запросам товар стоит на ~17–23, пост — на ~43–62, и пост забирает 30–50% показов:
  - crypto mining shipping container — товар 64 показа / поз. 18.0, пост 34 / 49.6;
  - bitcoin mining shipping container — товар 49 / 17.9, пост 25 / 48.6;
  - shipping container mining — товар 29 / 18.4, пост 22 / 61.7;
  - industrial container bitcoin mining — товар 17 / 22.3, пост 16 / 49.6.
  Пост целиком: 411 показов / 0 кликов / поз. 39.0 за 28 дн (`data/gsc-blog-pages-28d-2026-10-10.json`).
- **Интент поста после обновления:** informational / how-to planning. Человек на стадии «стоит ли строить контейнерную площадку и что для этого нужно», ещё не выбирает поставщика.
- **Что пост не забирает у товарной страницы:** mining container, crypto mining container, container crypto mining, crypto mining container for sale, crypto mining shipping container, mining container price, bitcoin mining container. Эти слова допустимы в тексте, но не в title/H1/H2.
- **Единственный запрос, где пост уже лидирует:** «bitcoin mining container design» — пост 18 показов / поз. 29.2 (82% показов), товар 4 / 61.8. Это и есть информационная ниша поста.
- **Читатель (ICP):** оператор, который планирует новую площадку или расширение; хостинг-провайдер; инвестор в инфраструктуру на стадии ТЭО (без инвест-советов). Боли: сроки запуска, требования к электрике, климат, отвод тепла, шум, разрешения.
- **Действие после чтения:** переход на `/en/products/container` (запрос КП / спецификация); для жидкостного охлаждения — на `/en/products/container-hydro` и `/en/asics-cooling/hydro-systems`.

## 2. Ключи (только из данных)

Источники: `data/dfs-blog-2026-10-10.json` (Labs suggestions US/en; «10» — порог 0–15; intent — разметка Labs); GSC — `data/gsc-blog-queries-pages-2026-10-10.json` и `cannibal-2026-10-10.json` (2026-09-10..10-07, все страны).

| Ключ | Объём US (CPC, intent Labs) | Сезонность | GSC i/pos (пост) | Роль |
|---|---|---|---|---|
| bitcoin mining container design | n/d | — | 18 / 29.2 (товар 4 / 61.8) | title, H1 |
| types of mining containers / air vs hydro vs immersion container | n/d | — | нет | H2 (таблица типов) |
| hydro mining container | 10 ($2.69) | — | товар `container-hydro` 23 / 8.2 | упоминание в H3 + ссылка на `container-hydro`, не цель |
| immersion mining container | 10 | — | товар `container` 20 / 20.8, `container-1k` 14 / 47.7 | упоминание в H3 + ссылка, не цель |
| mobile mining container | 10 | авг 2026: 70 | bitcoin mining mobile containers 7 / 51.9 | H3 «Mobile vs fixed deployments» |
| bitcoin mining container cost per mw 2025 | n/d | — | 11 / 39.8 | H2 «What drives the cost» — только драйверы, без цены, ссылка на товар |
| shipping container gpu mining / gpu mining shipping container | n/d | — | 8 / 21.1; 10 / 16 | не цель (GPU вне ICP); в тексте не развивать |
| **не брать в цель (товарная страница):** mining container | 390 ($4.20, transactional) | окт 2025 1 300 → авг 2026 20 | товар 59 / 25.1 | — только ссылка |
| crypto mining container / container crypto mining | 390 / 390 ($4.30, transactional / commercial) | окт 2025 1 000 → авг 2026 50 | — | — |
| crypto mining container for sale | 170 (transactional) | окт 2025 590, ноя 480 | — | — |
| crypto mining shipping container | 170 (transactional) | окт 2025 590, ноя 390 | пост 34 / 49.6, товар 64 / 18.0 | — (отдаём товару) |
| mining container price | 40 (Labs: informational, по смыслу коммерческий) | окт 2025 170 | товар `container` 16 / 9.4 («mining container cost») | — (цена → товар) |

- Информационный спрос по контейнерам в Google Ads **не измерен** (n/d). Ценность обновления — снятие каннибализации в пик сезона и passage для AIO, а не новый трафик. Ожидания по кликам ставить низкие.
- Отслеживание: контейнерных ключей в `data/rank-tracking/keywords.md` сейчас нет (проверено 2026-10-10). Кандидат в ротацию — «mining container» с target `/en/products/container`; пост в отслеживание не ставим. Ротацию утверждает человек.

## 3. Title / description / H1
- **Title (≤60):** `Bitcoin Mining Container Design: Air vs Hydro vs Immersion` (58 симв.).
- **Description (≤155):** `How mining containers differ by cooling type, what a site needs before delivery (power, foundation, network, permits) and a step-by-step planning list.` (151 симв.)
- **H1:** `Bitcoin Mining Containers Explained: Types, Site Requirements and a Planning Checklist`.
- Из текущего title «How Shipping Containers are Changing Crypto Mining» убрать «crypto mining» как главную фразу. В title/H1 не ставить «for sale», «price», «buy», «best».

## 4. Структура (H2/H3) и AEO

AEO по правилам `geo-ai`: AIO в 28 из 30 ключей ниши, featured snippet в 0 из 30. Делаем отдельные, самодостаточные passage: определение в 40–60 слов, таблица типов, нумерованный чек-лист, FAQ. Исторический текст «как контейнеры изменили индустрию» сократить до одного абзаца в конце.

1. **Лид (40–60 слов, passage):** что такое контейнер для майнинга биткоина: стандартный ISO-контейнер (20 / 40 ft), в котором собраны ASIC-майнеры, распределение питания, охлаждение и сеть, поставляемый как готовый модуль. Три типа по охлаждению: воздух, hydro (жидкость к водоблокам), иммерсия. Без цифр, кроме тех, что прошли [VERIFY].
2. **H2 «What is a bitcoin mining container?»** — ответ в 40–60 слов сразу под H2 (можно переиспользовать лид другими словами), затем 1 абзац: чем контейнер отличается от здания-ангара (скорость развёртывания, модульность, перемещаемость).
3. **H2 «Types of mining containers: air, hydro and immersion»** — главная таблица поста:
   - колонки: Cooling type / How heat is removed / Typical miners (air-cooled / hydro / any) / Noise / Dust and humidity exposure / Ambient range / Maintenance focus;
   - значения — качественные (low / medium / high) или [VERIFY] для чисел (°C, дБ). Цифры BiXBiT по своим контейнерам **не дублировать** с товарной страницы: здесь общая инженерная логика, у товара — спецификация;
   - H3 «Air-cooled containers» (2–3 предложения);
   - H3 «Hydro containers» — ссылка на `/en/products/container-hydro` и `/en/asics-cooling/hydro-systems`;
   - H3 «Immersion containers» — ссылка на `/en/products/container` (коммерческий анкор, см. §7).
4. **H2 «Which container type fits your site?»** — ответ в 40–60 слов: выбор определяют климат площадки, модели майнеров (air-cooled или hydro-версии), доступная мощность и требования к шуму; затем короткий список «if → then» (3–4 строки) [VERIFY формулировки у инженера].
5. **H2 «Site requirements before a container arrives»** — общий уровень, без инженерных значений (они на товарной странице):
   - H3 «Power» — подключение к сети или генерация, трансформатор, фазность, распределение внутри (ссылка на `/en/products/pdu`);
   - H3 «Foundation and access» — площадка, проезд крана и тягача;
   - H3 «Network» — канал связи, удалённый доступ, мониторинг (ссылка на `/en/ams`);
   - H3 «Heat rejection and climate» — куда уходит тепло, зима/лето;
   - H3 «Permits and noise» — правила зависят от юрисдикции, юридических гарантий не даём (CLAUDE.md §4).
6. **H2 «Mining container planning checklist»** — нумерованный список 8–10 шагов (passage для AIO):
   1. Подтвердить доступную мощность и график подключения.
   2. Выбрать модели майнеров и тип охлаждения.
   3. Проверить климат площадки (мин/макс температура, пыль, влажность).
   4. Согласовать разрешения и ограничения по шуму.
   5. Подготовить фундамент и подъезд.
   6. Спланировать распределение питания внутри контейнера.
   7. Обеспечить связь и удалённый мониторинг.
   8. Спланировать логистику (доставка, таможня, монтаж).
   9. Пусконаладка и приёмка.
   10. План обслуживания (фильтры / теплоноситель / контур).
   Формулировки шагов [VERIFY у инженера]. Под списком — ссылка «compare BiXBiT immersion mining containers» на товар.
7. **H2 «What drives the cost of a mining container?»** — ответ в 40–60 слов: размер, вместимость, тип охлаждения, объём теплоносителя, состав электрооборудования, доставка и пошлины, пусконаладка. **Без цен и без $/MW** (GSC-запрос «cost per mw» закрываем драйверами). Ссылка на товарную страницу для КП. Никаких сроков окупаемости.
8. **H2 «Mobile vs fixed container deployments»** — 1–2 абзаца (запрос «mobile mining container»): когда перемещаемость имеет смысл (временная энергия, flare gas [VERIFY: упоминать ли], пилот перед стройкой).
9. **H2 «How containers changed mining infrastructure»** — бывший основной текст поста, сжатый до 120–180 слов. Если в нём есть цифры роста рынка или «X% ферм используют контейнеры» — удалить или дать источник [VERIFY].
10. **H2 «Mining container FAQ»** (4–6 вопросов, ответ ≤ 80 слов; PAA по контейнерам в снимке serp-features не сохранены, в коммерческом брифе зафиксирован PAA «How much does a Bitcoin mining container cost?»):
    - «How many ASIC miners fit in a 40 ft container?» — ответ общий («depends on model, cooling type and power budget») + ссылка на товар, где указаны цифры [VERIFY у товара];
    - «Air vs hydro vs immersion container: which is better for hot climates?» [VERIFY];
    - «What power connection does a mining container need?» — общий ответ + ссылка на товар / PDU;
    - «How much does a bitcoin mining container cost?» — драйверы стоимости, без цифры, ссылка на КП;
    - «Can a mining container be moved after deployment?»;
    - «How do you monitor miners inside a container remotely?» → `/en/ams` [VERIFY телеметрию].

## 5. Сущности и термины
ISO shipping container, 20 ft / 40 ft, ASIC miner, Antminer, Whatsminer, air cooling, hydro cooling, immersion cooling, dielectric fluid, dry cooler, heat exchanger, ambient temperature, transformer, three-phase power, PDU, foundation, commissioning, remote monitoring, AMS, permits, noise, modular deployment, mobile deployment.

## 6. Факты на проверку [VERIFY]
- Любые числа в таблице типов (температурные диапазоны, шум, обслуживание).
- Формулировки «if → then» в разделе выбора и шаги чек-листа.
- Утверждения о рынке и истории из старого текста (доли, рост, «первые»).
- Телеметрия контейнеров в AMS.
- Совместимость `container-hydro` с конкретными моделями (если упоминаются).
- Сохраняются ли в посте старые цифры «+40% hashrate / -30% power» или «profitability» (в коммерческом брифе помечены к удалению) — если есть, удалить.

## 7. Внутренние ссылки
| Куда | Анкор | Где в тексте | Обязательна? |
|---|---|---|---|
| `/en/products/container` | BiXBiT immersion mining containers | H3 «Immersion containers» (после интро) | да (анкор зафиксирован в матрице H-B1) |
| `/en/products/container` | request a container quote and spec sheet | H2 «What drives the cost» | да (второе вхождение, другой анкор) |
| `/en/asics-cooling/hydro-systems` | hydro-cooled containers | H3 «Hydro containers» (H-B1) | да |
| `/en/products/container-hydro` | hydro container for Whatsminer and Antminer hydro units | H3 «Hydro containers» | да [VERIFY: какие модели] |
| `/en/products/pdu` | power distribution inside the container | H3 «Power» | да |
| `/en/ams` | monitor containerized miners remotely | H3 «Network» / FAQ | да |
| `/en/blog/post/creating-a-mining-farm-setting-priorities` | setting priorities for a new mining farm | H2 «Which container type» | желательно |
| `/en/blog/post/how-to-make-1500-asics-out-of-1000-bought-the-magic-of-immersion-cooling` | immersion cooling density in practice | H3 «Immersion containers» | желательно |

- Анкоры «mining container» и «immersion container» дословно не использовать (правило разделения анкоров в `content/internal-linking.md`: «mining container» → `container` из хабов, «immersion container» → `container-1k`/IC-1000). «BiXBiT immersion mining containers» и «hydro-cooled containers» — анкоры именно этого поста по матрице (H-B1).
- Проверить, что в старом тексте нет ссылок на noindex/404 (в т.ч. `/en/products/ container-1k` с пробелом из sitemap).
- Входящая ссылка с товарной страницы на пост не нужна (иначе товар передаёт вес информационному посту по своим ключам); с `/en/asics-cooling` — нет. Входящие — из блоговых постов про охлаждение и фермы.

## 8. Внешние источники (E-E-A-T)
- Фото реальных развёртываний BiXBiT с alt-текстом и, если можно, названием площадки [VERIFY: что разрешено публиковать].
- Ссылка на стандарт ISO 668 (размеры контейнеров) как нейтральный источник [VERIFY уместность].
- Подпись инженера и дата тех-проверки.

## 9. Запреты
- Никаких цен, $/MW, сроков окупаемости, «profitable container mining», инвест-советов.
- Не дублировать спецификацию товарной страницы (вместимость, климат, мощность BiXBiT-контейнеров) — только ссылка.
- Не давать юридических гарантий по разрешениям и шуму.
- Не писать «no dev fee», если в тексте всплывёт прошивка (только «transparent dev fee [VERIFY: current rate with the team]»).
- Партнёрский домен (agent-knowledge §2) не упоминать.

## 10. После публикации
- Чек-лист `content/blog-plan.md` §4; `dateModified` обновить; переобход поста и `/en/products/container` в один день.
- Через 28 дней (`cannibalization.py` + GSC): по crypto/bitcoin mining shipping container, shipping container mining, industrial container bitcoin mining доля показов поста должна упасть, позиция товара — вырасти или остаться в 17–23. Если товар просел, а пост поднялся — вернуть разговор о разделении интентов.
- «bitcoin mining container design»: позиция поста (baseline 29.2).
- Через месяц: AIO по «mining container» и «bitcoin mining container» (`./scripts/serp-features.py --keywords ...`), цитируется ли пост или товар.
