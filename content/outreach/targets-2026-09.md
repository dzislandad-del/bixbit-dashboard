# Outreach targets — 2026-09

> **Для человека.** Агент готовит список и поводы, а переговоры, отправку писем и любые договорённости ведёт человек (PR / BD / маркетинг).
> Методы только white-hat: без покупки ссылок, PBN, обменов и скрытых sponsored-размещений. Если площадка берёт деньги за листинг, ссылка должна стоять с `rel="sponsored"`, а решение принимает человек.
> Шаблоны писем: `content/outreach/templates.md`. Исправления фактов: `content/outreach/fact-corrections-2026-09.md`.

**Дата:** 2026-09-28 · **Агент:** offpage-seo

## Источники данных

| Источник | Что взято |
|---|---|
| `data/dfs-referring-domains-{bixbit.io,epicblockchain.io,emcd.io,hiveon.com,pitbit}-2026-09-25.json` | Множества referring domains. Gap посчитан локально (python) как `RD конкурента \ RD bixbit.io`, потому что `domain_intersection` игнорирует exclude-target |
| `data/dfs-backlinks-probes-emcd.io-2026-09-25.json` | Зонды EMCD по доменам вне топ-1000: число ссылок и атрибут |
| `data/dfs-backlinks-mention-check-bixbit.io-2026-09-28.json` | **Новый вызов (1 из 2 разрешённых):** `backlinks/live` для bixbit.io с фильтром по 9 доменам, где у нас уже есть упоминание. Нужен, чтобы понять, какие упоминания стоят со ссылкой, а какие без |
| `data/geo-{epic,emcd,pitbit}-2026-09-25/`, `data/dfs-llm-mentions-*`, `reports/sub/competitor-gap-*-geo-2026-09-25.md` | Домены, которые LLM и AIO цитируют по нашим темам |
| `reports/sub/competitor-gap-{ePIC,EMCD,PiTBiT}-backlinks-2026-09-25.md` | Типы площадок, ручные проверки, отсев спама |

**Размер gap (локально):** ePIC 119 из 170 RD · EMCD 966 из топ-1000 (+ зонды) · PiTBiT 38 из 78 · Hiveon 746 из топ-1000. У ≥2 конкурентов сразу: 104 домена, но больше 80% из них это спам-сети (`seo-anomaly-top-*.xyz`, `*seo*.link`, каталоги с spam 45–95). Такие домены в таблицу не попали.

**Как читать метрики.** Все значения взяты из полей DataForSEO, свои оценки DA/DR не добавлялись.
- `rank` — DFS rank донора в профиле конкретного конкурента, шкала 0–1000. У одного и того же домена он разный для разных целей: например, criptonoticias.com — 3 у ePIC и 58 у EMCD.
- `bl` — число backlinks на этого конкурента. `с` — дата first_seen.
- `spam` — `backlinks_spam_score`, если это поле есть хотя бы в одном файле.
- `dr_from` — `domain_from_rank` из вызова 2026-09-28. Это ранг самого домена-донора.
- «н/д» — поля нет в выгрузках. Домен взят из GEO-цитирований.
- Hiveon в скоупе не заявлен, но его RD-файл уже был снят. Он использован только как дополнительный сигнал cross-gap.

**Чего нет в данных.** Выгрузок referring domains по Braiins, Vnish, Awesome Miner, LiquidStack, Engineered Fluids и Submer нет. Поэтому cooling-целей в таблице мало, и они взяты из профилей ePIC, EMCD и PiTBiT. Следующий шаг — снять RD `liquidstack.com` и `engineeredfluids.com` (2 вызова, отдельный бюджет).

**Шкала достижимости.** Высокая: есть готовый повод или уже есть контакт/упоминание. Средняя: нужен сильный повод (данные, спикер, партнёрство). Низкая: tier-1, конкурент-владелец площадки или платный вход.

---

## 1. Таблица целей (36 доменов)

| # | Домен | Тип | Ссылается на конкурентов | Ref-метрики (из файлов) | Релевантность | Достижимость | P | Повод | Кому |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **d-central.tech** | Обзорник / магазин (US/CA) | ePIC, EMCD, Hiveon | ePIC: 4 bl, с 2026-08 · Hiveon: 4 bl · EMCD-зонд: 4, df. **BiXBiT уже есть:** 2 df-ссылки из Whatsminer-troubleshooting (aside) на наши docs, dr_from 290 | firmware, monitoring | Высокая: нашими docs они уже пользуются | **P0** | Добавить BiXBiT в `/firmware-comparison/` и `/bitcoin-mining-software-comparison/`. Это самый цитируемый LLM-источник (8 gap-цитирований), но BiXBiT там не назван. Повод — фактшит по Whatsminer, которого нет в их таблицах | Передать человеку (PR) |
| 2 | **spark.money** | Обзорник, таблица сравнения прошивок | н/д (в RD-выгрузках нет) | н/д · GEO: 4 цитирования в ответах про ePIC, в том числе основной источник ChatGPT по dev fee | firmware | Средняя | **P0** | Дополнение к таблице dev fee: BiXBiT — «transparent dev fee» `[VERIFY: current rate]`, модели Whatsminer и Antminer `[VERIFY]`. Источник — публичная страница `/en/firmwares/dev-fee`, когда она выйдет | Передать человеку (PR) |
| 3 | **altcoinlog.com** | Медиа / рейтинг прошивок (RU, UA-хостинг) | н/д | **BiXBiT уже есть:** nofollow → `/ru/firmwares`, с 2023-11, dr_from 342, page rank 69 | firmware | Высокая: мы уже в статье | **P0** | **Исправление факта**, а не ссылка: LLM приписывают BiXBiT dev fee PiTBiT 2.75%. См. `fact-corrections-2026-09.md` §1 | Передать человеку (PR RU) |
| 4 | **top-mining.ru** | RU-медиа / рейтинг прошивок | EMCD, PiTBiT | EMCD: rank 13, 5 bl, с 2024-09 · PiTBiT: rank 4, 3 bl (df, карточка бренда и «ТОП-6») | firmware | Высокая: BiXBiT уже #2 в рейтинге | **P0** | **Unlinked mention:** BiXBiT есть в рейтинге, но DFS не видит ни одной ссылки на bixbit.io. Попросить ссылку и карточку `/proshivka/bixbit/`, а также поправить подачу: сейчас BiXBiT описан как «производитель иммерсии» (F8) | Передать человеку (PR RU) |
| 5 | **criptonoticias.com** | Крипто-медиа ES / LatAm | ePIC, EMCD | ePIC: rank 3, 3 bl, с 2021-05 · EMCD: rank 58, 9 bl (df), с 2026-02 | firmware, cooling | Средняя | **P0** | Комментарий инженера на испанском: майнинг в Парагвае и LatAm, J/TH и теплоотвод `[VERIFY цифры]` | Передать человеку (PR) |
| 6 | **miningdisrupt.com** | Отраслевая конференция (US) | ePIC, EMCD, Hiveon | rank 55 у всех трёх · ePIC 1 bl · EMCD 3 bl · Hiveon 1 bl | firmware, cooling | Средняя: заявка спикера | **P0** | Доклад про тюнинг J/TH флота или immersion. Exhibitor-страница, если она платная, только с `sponsored` | Передать человеку (PR / events) |
| 7 | **bitcoinminingstock.io** | Медиа о публичных майнерах | ePIC, EMCD | ePIC: 1 bl, с 2025-08 · EMCD-зонд: 1, df | firmware, monitoring | Средняя | **P0** | Материал с данными об эффективности флотов (обезличенная статистика AMS `[VERIFY + юр. OK]`) | Передать человеку (PR) |
| 8 | **altairtech.io** | ASIC-реселлер / хостинг (US) | ePIC | ePIC: rank 118, 6 bl, с 2026-02 · GEO: 12 упоминаний в AIO-источниках рядом с bixbit.io | firmware, cooling | Средняя: нужна реальная партнёрка | **P0** | Партнёрский листинг «compatible firmware / AMS» на product-страницах `[VERIFY: условия у sales]` | Передать человеку (BD) |
| 9 | **lightspeedhosting.com** | Майнинг-хостинг, блог (US) | ePIC | ePIC: rank 109, 16 bl, с 2020-07 | monitoring, firmware | Средняя | **P0** | Интеграция AMS для клиентов хостинга, технический гостевой пост `[VERIFY: есть ли кейс]` | Передать человеку (BD) |
| 10 | **digitalcurrencyresearch.io** | Исследования / статьи | ePIC, EMCD | ePIC: 1 bl, с 2024-07 · EMCD-зонд: 5, в основном df · spam 10 | firmware | Средняя | **P1** | Данные или экспертный материал для research | Передать человеку (PR) |
| 11 | **emcd.io** | Пул + медиа (конкурент по GEO) | — (outbound: 0 ссылок на Braiins, LuxOS, ePIC, bixbit.io) | Не донор. GEO: статья-сравнение прошивок — 8 из 10 цитирований emcd.io | firmware | Низкая / средняя | **P1** | Цель — **упоминание**, а не ссылка: секция Whatsminer / BiXBiT в сравнении. Раздел `/fw/` — это коммерческие переговоры | Передать человеку (BD) |
| 12 | **asicminervalue.com** | ASIC-каталог и калькулятор | EMCD | EMCD: rank 297, 5 698 bl, с 2025-02 · GEO: 31 упоминание в AIO-источниках | firmware | Низкая / средняя | **P1** | Поле или блок «compatible firmware» на страницах моделей Antminer и Whatsminer. Проверить, есть ли вообще такой формат `[VERIFY]` | Передать человеку (BD) |
| 13 | **hashrateindex.com** | Отраслевые данные (Luxor) | ePIC | ePIC: 1 bl, с 2026-01 · GEO: 10 цитирований в ChatGPT-ответах про Braiins, 16 в AIO | firmware, monitoring | Низкая: площадка конкурента (Luxor) | **P1** | Данные для отчётов (Whatsminer tuning, immersion). Ожидаемый отклик низкий | Передать человеку (PR) |
| 14 | **theminingconference.com** | Конференция | EMCD, Hiveon | rank 12, по 1 bl, с 2026-04 · spam 5 | cooling, firmware | Средняя | **P1** | Спикерская заявка (immersion и hydro cooling) | Передать человеку (events) |
| 15 | **kernelpanicpodcast.com** | Майнинг-подкаст (EN) | ePIC, EMCD, PiTBiT, Hiveon | По 1–2 bl · first_seen 2026-09-23…25 у всех · **spam 70** | firmware | Средняя | **P1 (условно)** | Гость-инженер, ссылка в show notes. **Сначала ручная проверка:** синхронное появление у 4 брендов и spam 70 похожи на автогенерацию | Передать человеку (PR) после проверки |
| 16 | **tokenradar.io** | Крипто-медиа / обзоры | ePIC | ePIC: rank 84, 9 bl, с 2024-05 · spam 5 | firmware | Средняя | **P1** | Включение в обзоры «best ASIC firmware» с фактурой (dev fee `[VERIFY]`, модели `[VERIFY]`) | Передать человеку (PR) |
| 17 | **onlybestminers.com** | Обзоры и магазин ASIC | EMCD | EMCD: rank 238, 1 850 bl, с 2023-02 | firmware | Средняя | **P1** | Обзор прошивки или включение в их firmware-гайд | Передать человеку (PR / BD) |
| 18 | **readytomine.com** | Майнинг-гайды | EMCD | EMCD: rank 121, 163 bl, с 2023-10 · spam 10 | firmware | Средняя | **P1** | Гостевой гайд по прошивке Whatsminer (у EMCD этой темы нет) | Передать человеку (PR) |
| 19 | **miner.ae** | Майнинг-сервис (UAE) | EMCD | EMCD: rank 115, 88 bl, с 2023-03 | cooling, firmware, monitoring | Средняя | **P1** | Гео-приоритет ОАЭ. Партнёрство: прошивка, AMS и hydro cooling для их клиентов `[VERIFY]` | Передать человеку (BD) |
| 20 | **zhenchainmicro.com** | Поставщик ASIC (US) | EMCD | EMCD: rank 46, 34 bl, с 2025-03 | firmware | Средняя | **P1** | «Recommended firmware / monitoring» на карточках товаров `[VERIFY]` | Передать человеку (BD) |
| 21 | **rushash.ru** | Майнинг-хостинг под ключ (RU) | EMCD, PiTBiT | EMCD: rank 18, 4 bl, с 2026-01 · PiTBiT: 1 bl (главная, блок партнёров, df) | monitoring, cooling | Средняя | **P1** | Партнёрство: прошивка, AMS и hydro/immersion для клиентов хостинга. Логотип появляется только при реальной интеграции | Передать человеку (BD) |
| 22 | **trustmining.ru** | Каталог и отзывы майнинг-компаний (RU) | PiTBiT | PiTBiT: rank 30, 3 bl (профиль компании, df), с 2026-08 | firmware | Высокая | **P1** | Профиль компании. Если он платный, то только с `sponsored` `[VERIFY условия]` | Передать человеку (маркетинг) |
| 23 | **headframe.io** | Блог-сравнение ПО мониторинга | н/д | н/д · GEO: источник RU-ответов «облачный мониторинг асиков» (p4: 0 из 4 у BiXBiT) | monitoring | Средняя | **P1** | Добавить AMS в сравнение мониторинга. Фактура AMS `[VERIFY: тарифы, лимиты]` | Передать человеку (PR) |
| 24 | **bitexpert.io** | Wiki / справочник (RU) | н/д | н/д · GEO: источник p4 (мониторинг) | monitoring | Средняя | **P1** | Статья или раздел про AMS. Там же проверить tcs-mining.ru и hashrate.ru (тоже источники p4) | Передать человеку (PR RU) |
| 25 | **saashub.com** | Каталог ПО | н/д | **BiXBiT уже есть:** RD rank 10, 7 bl, с 2025-05 | firmware | Высокая: листинг можно править | **P1** | **Исправление факта:** «80 TH/s», «10–20%». См. `fact-corrections` §2 | Передать человеку (маркетинг) |
| 26 | **cryptonews.net** | Крипто-медиа | н/д | **BiXBiT уже есть:** df-ссылки, dr_from 446–476. Whatsminer-статья → `/en/firmwares` (anchor «here»), виделась только 2026-06-11. Hashrate-гайд → `/en/ams`, last_seen 2025-12 | firmware, monitoring | Высокая | **P1** | Упоминание из SERP «whatsminer tool» по DFS **не unlinked**: ссылка есть. Вручную проверить, жива ли она сейчас (last_seen = first_seen). Если нет, попросить восстановить. Предложить обновлённый материал о прошивках Whatsminer | Передать человеку (PR) |
| 27 | **operativa.ru** | Тех-медиа (RU) | н/д | **BiXBiT уже есть:** df → `/ru/firmwares/asic-s9-s9j-s9i`, dr_from 181, last_seen 2026-09-18 | firmware | Высокая | **P2** | Статья про S9k устарела. Предложить обновить её на актуальные модели и новую ссылку. Сначала проверить, не legacy/noindex ли цель `[VERIFY]` | Передать человеку (PR RU) |
| 28 | **blocktribune.com** | Крипто-медиа | ePIC | ePIC: rank 23, 2 bl, с 2026-08 | firmware, cooling | Средняя | **P2** | Новость о реальном релизе (прошивка, Hydro, Immersion) с цифрами `[VERIFY]` | Передать человеку (PR) |
| 29 | **nobsbitcoin.com** | Bitcoin-новости | ePIC | ePIC: 1 bl, с 2024-07 | firmware | Средняя | **P2** | Короткая новость о релизе или открытой документации | Передать человеку (PR) |
| 30 | **eenewseurope.com** | Электроника, трейд-медиа (EU) | ePIC | ePIC: 1 bl, с 2026-02 | cooling, PDU | Средняя / низкая | **P2** | Инженерный материал: PDU, hydro cooling для дата-центров `[VERIFY спеки]` | Передать человеку (PR) |
| 31 | **ungovernable.network** (+ ungovernablemisfits.com) | Майнинг-подкаст / комьюнити | ePIC | ePIC: 3 bl (spam 6) + 2 bl (spam 10), с 2026-07/08 | firmware | Средняя | **P2** | Гостевой эпизод про эффективность флота | Передать человеку (PR) |
| 32 | **beincrypto.com** | Крипто-медиа (RU/ES/EN) | EMCD | EMCD: rank 58, 34 bl, с 2025-07 | firmware | Средняя / низкая | **P2** | Экспертная колонка «как выбирать прошивку: dev fee, безопасность, автотюнинг». Только редакционно | Передать человеку (PR) |
| 33 | **hashrateindex.ru** | Майнинг-аналитика (RU) | EMCD | EMCD: rank 71, 47 bl, с 2025-01 · spam 2 | firmware, monitoring | Средняя | **P2** | Обезличенные данные эффективности флотов `[VERIFY + юр. OK]` | Передать человеку (PR RU) |
| 34 | **dc-mining.ru** | Газовый майнинг / готовые решения (RU) | PiTBiT | PiTBiT: rank 53, 3 bl (товарные стр., df), с 2025-11 · spam 15 | cooling | Средняя | **P2** | Совместное решение для газовых площадок: immersion/hydro, прошивка, AMS `[VERIFY кейс]` | Передать человеку (BD) |
| 35 | **cryptodesk.ru** | Магазин ASIC с блогом-обзорами (RU) | PiTBiT | PiTBiT: 4 bl, с 2025-08 | firmware, monitoring | Средняя | **P2** | Обзор «прошивка + AMS» с демо-доступом `[VERIFY]` | Передать человеку (PR RU) |
| 36 | **mineshop.eu** | ASIC-реселлер (EU) | Hiveon | Hiveon: 8 bl, с 2026-01 · spam 5 · GEO: 21 упоминание в AIO-источниках, цитировался в RU-ответе p1 | firmware | Средняя | **P2** | Партнёрский листинг совместимого ПО `[VERIFY]` | Передать человеку (BD) |

### Профили компании (не аутрич, делает маркетинг)

Это не переговоры, а заполнение карточек: website `https://bixbit.io/en`, продукты, одинаковое описание без «no dev fee».

| Домен | Кто из конкурентов там есть (данные) |
|---|---|
| crunchbase.com | ePIC 3 bl · Hiveon 2 bl · EMCD-зонд 1 nf · spam 2 |
| zoominfo.com | ePIC 1 · Hiveon 1 · EMCD-зонд 1 nf · spam 10 |
| cbinsights.com | ePIC: rank 26, 4 bl |
| cryptorank.io | ePIC 2 · EMCD-зонд 1 nf |
| sourceforge.net / slashdot.org | н/д в RD. GEO: источники ответов «alternatives to Braiins» (ePIC q4) |
| github.com | ePIC 5 bl. Публичный репозиторий (AMS API examples, changelog, проверка checksum) делать только с согласия инженеров |

### Резерв (следующий цикл)

- **Tier-1 крипто-медиа** (cointelegraph, decrypt, cryptoslate, bitcoinist, crypto.news): у EMCD по зондам почти всё nofollow или sponsored. Только редакционный путь под сильный повод. **Не покупать.**
- **Калькуляторы доходности** (crypto-miner-profitability.com: EMCD rank 313, 6 370 bl; hashrate.no: Hiveon rank 296, 12 992 bl, spam 3): блок про firmware tuning без заявлений о доходности. Достижимость низкая.
- **RU-листинги из GEO** (coindaily.ru, crypto.ru, cryptorussia.ru): cryptorussia.ru называет оба бренда, но в RD bixbit.io его нет, то есть это вероятный unlinked mention `[VERIFY вручную]`. По coindaily.ru и crypto.ru не проверено, есть ли там BiXBiT.
- **asicprices.com** (EMCD rank 220, 950 bl), **yesmining.io** (ePIC 4 bl, EMCD 3 nf), **hidix.ru** (PiTBiT 3 bl, spam 25), **miningtalks.io** (EMCD rank 84, spam 14).

---

## 2. Исключено (не цели)

| Что | Почему |
|---|---|
| `bixbitusa.io`, `launch.bixbitusa.io` | Партнёрский домен, вне работы: не цель и не «наш» |
| `bixbit.pro`, `bixbit-dev.github.io` | Собственные ресурсы |
| `seo-anomaly-top-*.xyz`, `link-legion-*.xyz`, `*seo*.link/.info`, `backlink*`, каталоги с spam 45–95 (ycm.info, wheretobuybest.link, onvaxs.com, plurio.shop и др.) | Автогенерируемые сети. Часть из них есть и у BiXBiT: это кандидаты в disavow **на ревью человека** (см. `reports/sub/competitor-gap-*-backlinks-2026-09-25.md`) |
| Сеть PR-синдикации «mining fleet management» (cryptotimesgazette.com, miningpressreleases.com и др.), клоны 2026-08 (coinstusk, cryptskies…), биржа статей RU у EMCD | Платные размещения. Не покупать и не повторять |
| minerstat.com, moonone.ru, gomining.com | Конкуренты AMS или прошивок |
| miningpoolstats.stream, пуловые листинги, вакансии (hh.ru и др.), реферальные сайты | Не наш тип продукта или не SEO-цель |
| minerfirmware.online | Уже ссылается на нас (nofollow, 2026-09-25). Появился в одной волне со спамом у PiTBiT и Hiveon. Только мониторинг описания, без аутрича |
| pool.kryptex.com | Уже есть 15 страниц-карточек BiXBiT (nofollow → `/en`), это действующее партнёрство. Отдельная задача BD, не аутрич |

---

## 3. Порядок работ (для человека)

1. **0–14 дней:** altcoinlog (факт), saashub (факт), top-mining.ru (unlinked → ссылка), cryptonews.net (проверить ссылку), профили компании.
2. **0–45 дней:** d-central, spark.money (после выхода страницы dev fee и сравнения), criptonoticias, miningdisrupt, bitcoinminingstock.io. BD: altairtech, lightspeedhosting.
3. **30–90 дней:** остальные P1 и P2. Повторить замер RD и GEO через 4–6 недель после исправлений.

**Зависимости от контента:** питчи #1, #2, #11, #16 опираются на публичные страницы `/en/firmwares/dev-fee` и `/en/firmwares/comparison` (архитектура v2, слаги `[VERIFY]`). До их выхода в письмах давать ссылку на `/en/firmwares`.

*Все метрики взяты из DataForSEO (RD 2026-09-25 и backlinks 2026-09-28). Moz не используется. Bing `GetLinkCounts` пуст (2026-09-28). DA/DR не приводятся. Тех-факты помечены `[VERIFY]`. Переговоры ведёт человек.*
