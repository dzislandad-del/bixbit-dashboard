# Link-gap: BiXBiT (bixbit.io) vs EMCD (emcd.io)

**Дата:** 2026-09-25 · **Агент:** offpage-seo · **Методы:** только white-hat
**Предыдущие отчёты:** `reports/competitor-gap-EMCD-2026-06-19.md` (июнь, без метрик DFS), `reports/sub/competitor-gap-ePIC-backlinks-2026-09-25.md` (ePIC, для cross-gap)

## 0. Источники данных

| Источник | Статус | Что взято |
|---|---|---|
| DataForSEO `/v3/backlinks/summary/live` (emcd.io) | OK | Сводка → `data/dfs-backlinks-probes-emcd.io-2026-09-25.json` (`summary_emcd`) |
| DataForSEO `/v3/backlinks/referring_domains/live` (emcd.io, limit 1000, rank desc) | OK | Топ-1000 из **2 649** main RD → `data/dfs-referring-domains-emcd.io-2026-09-25.json` |
| DataForSEO `referring_domains` с фильтром `domain in [...]` (3 зонда) | OK | (а) 88 gap-доменов ePIC вне топ-1000 EMCD; (б) 84 известных отраслевых медиа/каталога; (в) 35 «чистых» доменов BiXBiT. Итоги → тот же probes-файл |
| DataForSEO `/v3/backlinks/backlinks/live` (domain_from like %emcd.io → braiins.com, luxor.tech, epicblockchain.io, bixbit.io) | OK | Везде 0 ссылок (см. §2.2) |
| BiXBiT RD | Из ранее снятого файла | `data/dfs-referring-domains-bixbit.io-2026-09-25.json` (885 main RD, полный список) |
| `domain_intersection` | Не использовался | В прогоне ePIC фильтр exclude не сработал. Gap посчитан локально как разность множеств |
| WebFetch статьи EMCD firmware comparison | Частично | Страница отдала только заголовок, поэтому ссылки, автор и дата не видны. Вывод о ссылочной политике сделан по DFS |
| Moz API / Bing Webmaster | **Недоступны** | Нет ключей в `.env` |

**Ограничения.** Источник один, поэтому confidence-weighted merge не делался. DFS `rank` — внутренняя шкала 0–1000, DA/DR не приводятся. У EMCD в выгрузке **только топ-1000 из 2 649** main RD по rank. Хвост (1 649 доменов, в основном с rank < 15) закрыт зондами по спискам, но не полностью. Поля nofollow по доменам в основном выгрузке отсутствуют (AI-режим ответа), они есть только в зондах.

## 1. Сравнение профилей

| Метрика | BiXBiT | EMCD | Комментарий |
|---|---|---|---|
| DFS rank (target) | 254 | **442** | EMCD заметно сильнее |
| Backlinks | 6 706 | **63 997** | ×9.5 |
| Referring domains (всего) | 1 104 | **3 819** | ×3.5 |
| Referring main domains | 885 | **2 649** | ×3 |
| Nofollow RD (всего) | 613 (56%) | 2 426 (64%) | У EMCD доля nofollow даже выше: много UGC, пресс-релизов и sponsored |
| Nofollow main RD | — | 1 376 (52%) | |
| backlinks_spam_score (target) | **44** | 35 | Оба высокие. У EMCD target_spam_score = 2 |
| Main RD со spam ≥ 50 | 391 / 885 (44%) | 164 / топ-1000 (16%), 7 176 ссылок (~22% выборки) | Спам у BiXBiT в процентах тяжелее |
| Main RD со spam ≥ 30 | 519 (59%) | 341 / 1000 (34%) | |
| Ссылки по TLD (топ) | blogspot, .com, **.com.tr**, .website/.online/.space/.site | .com 15 863, **.ru 6 894**, .online 5 800, .website 5 532, .space 5 225, .site 5 022, .xyz 1 244 | Одни и те же спам-кластеры .online/.website/.space/.site есть у обоих, похоже на общий фон автогенерации |
| Страны ссылок | TR, RU, UA, BR | RU 7 016, US 4 266, UA 2 080 | EMCD силён в СНГ **и** в US |
| Возраст | с 2025-08 | с 2019-01 | 589 из 1000 топ-доменов EMCD появились в 2026 г., темп прироста высокий |
| Overlap (main RD) | 55 в топ-1000 EMCD, плюс ~16 найдено зондами | | Из 55 общих **18 — это xyz-сети** `link-legion-*.xyz` (9) и `seo-anomaly-top-*.xyz` (9), см. §5 |
| Sponsored-атрибут | — | 129 ссылок | cointelegraph, u.today, minerstat, zycrypto, cryptonews.com: EMCD покупает размещения с корректной разметкой `sponsored` |

**Механика профиля EMCD:**
- Ядро — **майнинг-инструменты и агрегаторы**: miningpoolstats.stream (rank 429, 729 ссылок), crypto-miner-profitability.com (313, 6 370), asicminervalue.com (297, 5 698), onlybestminers.com (238, 1 850), asicprices.com (220, 950). Это sitewide-листинги пула. Для BiXBiT доступны только те, где есть раздел под прошивки или ПО.
- **СНГ-медиа:** forklog.com (67 ссылок), bits.media (104), rbc.ru, habr, miningclub.info, плюс большой пласт .ru-сайтов (см. §5).
- **Платный PR (nofollow/sponsored):** cointelegraph, decrypt, cryptoslate, newsbtc, u.today, crypto.news, bitcoinist, ambcrypto, beincrypto.
- **Вакансии** (careers-page.com, wantapply, goapplyjob, hirelens, geekjob.ru, findmyremote.ai, hh.ru/kz) и **реферальные или аффилиат-сайты** (topparrain, amarkets.su, coinhold.io). Это побочный эффект масштаба компании, а не цели для аутрича.

## 2. Gap: ссылаются на EMCD, но не на BiXBiT

Всего gap-доменов в топ-1000 EMCD: **945**, из них со spam < 50: 813. После фильтра по тематике (крипто и майнинг-медиа, железо, хостинг, форумы, обзоры, СНГ-медиа) и отсева сетей (§5) осталось около 60 кандидатов. Ниже топ-30.

Колонки: rank — DFS rank донора в профиле EMCD («—», если null); «Ссылок» — backlinks на EMCD; атрибут указан там, где он есть в зонде.

| # | Домен | Rank | Ссылок | Тип | Приоритет | Outreach-угол |
|---|---|---|---|---|---|---|
| 1 | criptonoticias.com | 58 | 9 (df) | Крипто-медиа ES / LatAm | **P0 (cross)** | Питч на испанском: майнинг в Парагвае и LatAm, комментарий инженера BiXBiT про J/TH и теплоотвод [VERIFY цифры] |
| 2 | miningdisrupt.com | 55 | 3 | Конференция (US) | **P0 (cross)** | Заявка спикера или exhibitor. Если листинг платный, `rel="sponsored"` |
| 3 | asicminervalue.com | 297 | 5 698 | ASIC-каталог и калькулятор доходности | **P0** | Запросить поле или раздел «compatible firmware» на страницах моделей Antminer/Whatsminer. Питч с фактическим списком поддерживаемых моделей [VERIFY у продукта]. Достижимость средняя |
| 4 | onlybestminers.com | 238 | 1 850 | Обзоры и магазин ASIC | **P0** | Обзор прошивки BiXBiT или включение в их firmware-гайд. Возможна партнёрка по предустановке [VERIFY у sales] |
| 5 | asicprices.com | 220 | 950 | Агрегатор цен ASIC (US) | **P1** | Листинг ПО или прошивок, ресурсная страница для операторов |
| 6 | crypto-miner-profitability.com | 313 | 6 370 | Калькулятор доходности | **P1** | Спросить, есть ли у них блок «firmware tuning» (разница J/TH stock vs tuned). Дать данные [VERIFY]. Без заявлений о доходности |
| 7 | miner.ae | 115 | 88 | Майнинг-сервис (UAE) | **P0** | ОАЭ — гео-приоритет. Партнёрство: прошивка, AMS, hydro cooling для их клиентов, кейс. **Передать BD** |
| 8 | beincrypto.com | 58 | 34 | Крипто-медиа (RU/ES/EN) | **P1** | Экспертная колонка «Как выбирать ASIC-прошивку: dev fee, безопасность, автотюнинг». Июньский отчёт: у них есть партнёрский материал EMCD+Vnish |
| 9 | blockchain-media.org | 302 | 1 360 | Крипто-медиа (UA) | **P1** | Питч СНГ/UA: технический разбор тюнинга. Проверить вручную, не агрегатор ли это |
| 10 | hashtelegraph.com | 56 | 5 | Крипто-медиа (UA/RU) | **P1** | Новость или интервью по релизу прошивки |
| 11 | rbc.ru | — | 3 (df) | Бизнес-медиа РФ | **P2** | Экспертный комментарий в материалы про промышленный майнинг. Достижимость низкая, нужен PR |
| 12 | readytomine.com | 121 | 163 | Майнинг-гайды | **P1** | Гостевой гайд по прошивкам для Whatsminer (у EMCD этой темы нет) |
| 13 | hashrateindex.ru | 71 | 47 | Майнинг-аналитика RU | **P1** | Данные для аналитики эффективности флотов, обезличенная статистика AMS [VERIFY, нужен юр. OK] |
| 14 | bestminingpool.ru | 109 | 110 | Майнинг-ресурс RU | **P2** | Раздел ПО и прошивок, гостевой материал |
| 15 | miningpoolstats.ru / miningmoon.ru / top-mining.ru / mineinfo.ru / prostomining.com / geekminers.ru | 102 / 106 / 13 / 7 / 6 / 30 | 125 / 34 / 5 / 1 / 1 / 2 | Майнинг-ниша RU | **P2** | Пакетный аутрич на русском: гайд «прошивка Antminer/Whatsminer без бэкдоров» и листинг |
| 16 | cryptonomist.ch | 43 | 31 | Крипто-медиа (CH/IT/EN) | **P2** | Питч с данными |
| 17 | cryptodaily.co.uk / coinjournal.net / themerkle.com | 71 / 69 / 61 | 15 / 5 / 2 | Крипто-медиа UK/US | **P2** | Новостной питч (релиз, кейс). Проверить, не платные ли там размещения |
| 18 | financefeeds.com | 84 | 55 | Финтех-медиа | **P3** | Только при институциональном угле (фонды или публичные майнеры) |
| 19 | theminingconference.com | 12 | 1 | Конференция | **P1** | Спикерская заявка (immersion и hydro cooling) |
| 20 | zhenchainmicro.com | 46 | 34 | Поставщик ASIC (US) | **P1** | Реселлер: «рекомендуемая прошивка / мониторинг» на карточках. **Передать BD** [VERIFY] |
| 21 | asicmarketplace.com | — | 4 (nf) | ASIC-маркетплейс (US) | **P2** | Листинг или партнёрство. Ссылки nofollow, ценность в трафике и упоминании |
| 22 | intermine-solutions.de | 2 | 3 | Майнинг-решения (DE) | **P2** | Партнёрство (охлаждение, прошивка) [VERIFY профиль компании] |
| 23 | hamushosting.com | 7 | 7 | Хостинг [VERIFY: майнинг или веб] | **P2** | Если майнинг-хостинг, то AMS-интеграция или кейс |
| 24 | miningtalks.io | 84 | 5 | Майнинг-комьюнити | **P2** | Участие инженера в дискуссиях, AMA. Без спама |
| 25 | fpgeeks.com | 15 | 3 | Форум (hardware) | **P3** | Участие в ветках по ASIC-тюнингу, ссылка только уместная |
| 26 | cointelegraph.com | — | 20 (nf, 4 sponsored) | Tier-1 медиа | **P2** | Только редакционный путь: exclusive-данные или экспертный комментарий. **Не покупать** sponsored ради ссылки |
| 27 | decrypt.co / cryptoslate.com / bitcoinist.com / crypto.news / ambcrypto.com | — | 6 / 8 / 5 / 3 / 2 (все nf) | Крипто-медиа | **P2** | PR-питчи. Ценность в упоминаниях и AI-цитируемости, не в PageRank |
| 28 | minerstat.com | — | 22 (nf, 10 sponsored) | Мониторинг майнинга (конкурент AMS) | **P3** | Вероятно, платный листинг пула. Для BiXBiT смысл есть, только если у них раздел ASIC-прошивок [VERIFY]. Конкурент AMS, достижимость низкая |
| 29 | asic.tools | 14 | 2 | Инструменты ASIC | **P3** | Листинг |
| 30 | coincamps.ai / cryptalist.io | 11 / 70 | 13 / 12 | Каталоги крипто-сервисов | **P3** | Бесплатный листинг компании, если есть |

**Не цели (исключено):** miningpoolstats.stream, cloverpool.com, pool-btc.com, miningpoolslist.com (листинги пулов, BiXBiT не пул); kucoin.com (биржевой блог); вакансии и реферальные сайты (см. §1).

### 2.2. EMCD как цель

**Факты DFS:** с emcd.io **0 живых ссылок** на braiins.com, luxor.tech, epicblockchain.io и bixbit.io. Июньский отчёт фиксирует статью `emcd.io/articles/mining/best-custom-asic-firmware-vnish-vs-braiins-os-vs-luxos/` (BiXBiT не упомянут) и раздел `/fw/` с прошивками в партнёрстве с Vnish. Сегодня WebFetch отдал только заголовок статьи, поэтому состав упомянутых вендоров (Vnish, Braiins OS, LuxOS, BiXBiT нет) подтверждён, а ссылки не проверены.

**Вывод о достижимости:**
- **Ссылка из статьи — маловероятна.** EMCD не ставит внешних ссылок даже на Braiins и LuxOS, которых сравнивает. Реалистичная цель — **упоминание BiXBiT в сравнении** (unlinked). Для GEO это ценно: статья в июне была №1 в SERP и кормит LLM. Приоритет **P1, GEO-угол**, а не ссылочный.
- **Гостевой пост** — нет публичной «write for us» (по доступным данным). Путь через контент-команду EMCD. Достижимость низкая или средняя.
- **Партнёрство `/fw/`** — EMCD уже раздаёт Vnish. BiXBiT конкурирует с Vnish за это место, и это коммерческие переговоры (дистрибуция прошивки через пул, возможна ко-маркетинговая страница). **P1, передать человеку (BD) для переговоров.** SEO-выгода вторична.
- **Угол питча** (для человека): «В вашем сравнении нет прошивки с поддержкой Whatsminer + Antminer одновременно. Предлагаем фактуру: список моделей, dev fee 2.8% / 2% для M2x [VERIFY], методика автотюнинга [VERIFY]». Без требования ссылки.

## 3. Где выигрывает BiXBiT

- **Качество на домен.** Спам-доля выше у BiXBiT (плохо), но чистых доменов, которые ссылаются **только** на BiXBiT, много. Зонд (в) подтвердил: эти домены **не ссылаются на EMCD**:
  - Майнинг-ниша: **minecool.ru** (rank 86), **bigstarmining.com** (51), **kryptex.com** (майнинг-ПО), **minershero.com**, **asicminershopforall.com**, **asicrigshop.com**.
  - Крипто-медиа: **coindoo.com** (51), **cryptohamster.org** (51), **newscrypto.net** (46), **thebitsignal.com** (23), coinedict.com, zecripto.com, kryptonewswire.com, cryptofr.com, businesscomputingworld.co.uk.
  - LatAm: **uol.com.br** (14), **pdsdigital.com.py** (Парагвай — ICP-гео).
  - Прочее: **prnewswire.com** (есть и у ePIC, у EMCD нет), saashub.com, digitalinfranet.org, storeboard.com, bixbit-dev.github.io (собственный).
- **Общие сильные площадки** (оба в профиле, для паритета): bitcointalk.org (BiXBiT 177 ссылок против 22 у EMCD), forklog.com, bits.media, d-central.tech, cryptonews.net, irlbtc.com (BiXBiT 104 против 6), ultramining.com, u.today, newsbtc.com, habr.com, miningclub.info, b.tc, lusha.com.
- **Тематика.** У BiXBiT профиль ближе к firmware, железу и ASIC-магазинам. У EMCD он пуловый и финансовый. По firmware-сущностям BiXBiT конкурирует не с объёмом EMCD, а с его одной статьёй (§2.2).

## 4. Cross-gap: ссылаются на ePIC **и** EMCD, но не на BiXBiT (наивысший приоритет)

Найдено **16 доменов**: 5 из пересечения топ-1000 EMCD с ePIC и 11 из зонда (а).

| # | Домен | EMCD (ссылок, атрибут) | ePIC (ссылок) | Тип | Приоритет | Угол |
|---|---|---|---|---|---|---|
| 1 | criptonoticias.com | 9, df | 3 | Медиа ES / LatAm | **P0** | см. §2 #1 |
| 2 | miningdisrupt.com | 3 | 1 | Конференция | **P0** | Спикер или exhibitor |
| 3 | bitcoinminingstock.io | 1, df | 1 | Медиа о публичных майнерах | **P0** | Питч с данными об эффективности флотов [VERIFY] |
| 4 | digitalcurrencyresearch.io | 5, в основном df | — | Исследования / статьи | **P0** | Экспертный материал или данные для research |
| 5 | kernelpanicpodcast.com | 1 (spam 70*) | 1 | Майнинг-подкаст | **P1** | Гость-инженер. *spam, вероятно, ложноположительный, проверить вручную |
| 6 | toppodcast.com | 7, df | — | Каталог подкастов | **P2** | Появится автоматически после эпизода (#5) |
| 7 | yesmining.io | 3, nf | — | Майнинг-ресурс | **P1** | Листинг или гостевая статья |
| 8 | blocktrainer.de | 1, nf/ugc (форум) | 1 | Bitcoin-образование DE | **P2** | Участие в форуме, образовательный материал |
| 9 | cryptorank.io | 1, nf | — | Крипто-каталог / данные | **P2** | Профиль компании |
| 10 | crunchbase.com | 1, nf | 3 | Бизнес-профиль | **P1 (быстро)** | Заполнить профиль |
| 11 | zoominfo.com | 1, nf | 1 | Бизнес-профиль | **P2** | Заявить профиль |
| 12 | medium.com | 4, nf/ugc | 5 | Блог-платформа | **P2** | Переопубликация с canonical на bixbit.io/en |
| 13 | bitcoinlinux.com | 5, nf | — | Новостной агрегатор | **P3** | Подтянется синдикацией после PR |
| 14 | messageceo.com | 2 (spam 10) | 1 | Бизнес-каталог | **P3** | Проверить вручную, низкая ценность |
| 15 | viraltrendingcontent.com | 5 | 1 | Контент-агрегатор | **P3** | Не аутричить, может подтянуться сам |
| 16 | ziven.io | 1, df | — | [VERIFY: тип сайта неизвестен] | **P3** | Сначала ручная проверка |

Сильные gap-домены ePIC, которые **не** ссылаются на EMCD: altairtech.io, lightspeedhosting.com, hashrateindex.com. Они остаются P0 из отчёта по ePIC, но это не cross-gap.

## 5. Отсеяно: спам и сети (не цели, часть касается BiXBiT)

- **Общая xyz-сеть у BiXBiT и EMCD:** `link-legion-{232,235,237,238,241,242,244,245,249}.xyz` и `seo-anomaly-top-{26,34,40,226,228,234,235,236,240}.xyz`. Это автогенерированная сеть, бьющая по нескольким крипто-брендам. **Кандидат в disavow для BiXBiT** (`domain:`), **только на ревью человека**, сам не применяю.
- **Общий мусор:** avtoru.top, betwinnermirror.com, betulcrime.com, uncledspizza.com, fittyfoody.com, homesforsaleoldgreenwichct.com, quero.party, ggmap.us.com, tacticlinks.com. Нерелевантные или гемблинг-домены, у BiXBiT на ревью.
- **Вероятная биржа статей RU** у EMCD: сотни .ru/.su/.ua-блогов с rank 51 или 23, по 1–3 ссылки (dacha5.ru, power-fit.ru, tinochki.ru и т.п.), 2023–2026. Похоже на платные размещения. **Не повторять.**
- **PR-синдикация 2026-08:** около 40 доменов-клонов по 3 ссылки (coinstusk, cryptskies, cryptsnails, coinslopes, cryptargets …). Это платная рассылка, **не покупать**.
- **Sponsored-блоги 2026-06:** financialcalls, econonuestra, launchhighlights, foxtd, begottennotmade, thetradevariety (60–80 ссылок, spam 15–25).
- **spam ≥ 50:** 164 домена в топ-1000 EMCD, в цели не брались.

## 6. План

| Шаг | Что | Цели | Срок | Владелец |
|---|---|---|---|---|
| 1 | Cross-gap P0 | criptonoticias, miningdisrupt, bitcoinminingstock.io, digitalcurrencyresearch.io | 0–45 дн. | Человек (PR). Шаблоны готовит offpage в `content/outreach/` |
| 2 | Профили | crunchbase, zoominfo, cryptorank | 0–14 дн. | Маркетинг |
| 3 | ASIC-каталоги и магазины | asicminervalue, onlybestminers, asicprices, zhenchainmicro, miner.ae | 0–60 дн. | **Передать человеку (BD) для переговоров** |
| 4 | EMCD: упоминание в firmware-сравнении и `/fw/` | emcd.io | 30–90 дн. | **Передать человеку (BD)**. Цель — упоминание (GEO), а не ссылка |
| 5 | СНГ-пакет | beincrypto, hashtelegraph, blockchain-media.org, readytomine, hashrateindex.ru, RU-майнинг-ресурсы | 30–90 дн. | Человек (PR RU) |
| 6 | Гигиена | Ревью xyz-сети и общего мусора, кандидат в disavow | 0–30 дн. | SEO-лид (решение за человеком) |
| 7 | Повтор | summary и RD EMCD, дозакачка хвоста 1 649 RD (offset 1000) | 2026-12 | offpage-seo |

*Все метрики — DataForSEO Backlinks API, 2026-09-25. Moz и Bing не использовались (нет ключей). DA/DR не приводятся. Тех-факты о продуктах помечены [VERIFY]. Переговоры ведёт человек.*
