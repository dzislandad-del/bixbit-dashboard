# Link-gap: BiXBiT (bixbit.io) vs ePIC Blockchain (epicblockchain.io)

**Дата:** 2026-09-25 · **Агент:** offpage-seo · **Методы:** только white-hat
**Предыдущий отчёт:** `reports/competitor-gap-ePIC-2026-06-19.md` (в июне DataForSEO отдавал 401, метрик не было)

## 0. Источники данных

| Источник | Статус | Что взято |
|---|---|---|
| DataForSEO `/v3/backlinks/summary/live` | OK | Сводка по ePIC (BiXBiT — из ранее снятого summary) |
| DataForSEO `/v3/backlinks/referring_domains/live` | OK | ePIC: 170 main-доменов (limit 1000, rank desc) → `data/dfs-referring-domains-epicblockchain.io-2026-09-25.json` |
| DataForSEO `/v3/backlinks/domain_intersection/live` | OK, **но фильтр не сработал** | Вернул все 170 доменов ePIC, хотя `exclude_targets:["bixbit.io"]` был передан. Gap посчитан локально как разность множеств ePIC RD минус BiXBiT RD (885). Сырой ответ → `data/dfs-domain-intersection-epicblockchain.io-not-bixbit.io-2026-09-25.json` |
| DataForSEO `/v3/backlinks/anchors/live` | OK | Топ-30 анкоров ePIC (в `data/` не сохранялся, ответ inline) |
| Moz API | **Недоступен** | В `.env` нет ключей |
| Bing Webmaster | **Недоступен** | В `.env` нет ключей |

Ограничение: источник один (DataForSEO), поэтому confidence-weighted merge из skill `seo-backlinks` не делался. Поле `rank` в DFS — внутренняя шкала 0–1000. У большинства мелких доменов оно пустое (`null`), в таблицах это «—». DA/DR не приводятся, потому что их нет ни в одном доступном источнике.

## 1. Сравнение профилей

| Метрика | BiXBiT | ePIC | Комментарий |
|---|---|---|---|
| DFS rank (target) | **254** | 190 | У BiXBiT выше |
| Backlinks | **6 706** | 377 | В 18 раз больше, но ~57% из спам-кластеров (см. §4) |
| Referring domains (всего) | **1 104** | 185 | |
| Referring main domains | **885** | 170 | |
| Nofollow RD (всего) | 613 (~56%) | 64 (~35%) | Доля dofollow: BiXBiT ~44%, ePIC ~65% |
| Main-домены, где все ссылки nofollow (локальный расчёт) | 401 / 885 (45%) | 58 / 170 (34%) | |
| backlinks_spam_score (target) | **44** | 13 | Главный риск BiXBiT |
| Домены со spam_score ≥ 50 | 391 (44%), 3 814 ссылок | 40 (24%) | |
| Домены со spam_score ≥ 30 | 519 (59%) | 50 (29%) | |
| Топ TLD доменов | blogspot.com 185, .com 127, **.com.tr 115**, .website 69, .online 68, .space 67, .site 67, .ru 52, .xyz 34 | .com 95, .io 9, .org 9, .net 5, blogspot 5, pages.dev 4 | У ePIC профиль в основном на .com, у BiXBiT сильно размыт |
| Страны ссылок (топ) | TR, RU, UA, BR, неопределённые | US 85, IO 29, AI 18, CA 15 | ePIC сидит в США и Канаде (это ICP-рынок) |
| Первое появление | 2025-08 и позже | 2019-01 | ePIC старше примерно на 6 лет |
| Общих доменов (overlap) | 51 | 51 | Среди них bitcointalk.org, d-central.tech, prnewswire.com, cryptoindustry.com, b.tc, block.cc, lusha.com. Остальное в основном каталоги-«оценщики» |

**Анкоры ePIC (DFS):** бренд и URL: «ePIC Blockchain» (51 RD), «epicblockchain.io» (42), «www.epicblockchain.io» (13), «ePIC Blockchain Technologies» (11). Коммерческий анкор «mining fleet management» стоит на 18 RD, все nofollow, это сеть PR-синдикации (см. §2.3). Кроме того, есть 13 RD с явным PBN-анкором «High Quality Dofollow Backlinks … Buy Backlinks» (spam 63, с 2026-08). Похоже на негативное SEO против ePIC или на мусорную автогенерацию. **Не повторять и не использовать как модель.**

**Что изменилось с июня (2026-06-19).** Июньский отчёт перечислял PRNewswire, BusinessWire, CBInsights, Crunchbase, ZoomInfo, Tracxn, Medium, GitHub, Bitcoin Magazine и Proactive Investors по данным WebSearch. DFS подтверждает: prnewswire.com (15 ссылок, **есть и у BiXBiT**), cbinsights.com, crunchbase.com, zoominfo.com, medium.com, github.com. **Не подтверждены** как живые RD в DFS: businesswire, tracxn, bitcoinmagazine, proactiveinvestors, zeusbtc.com. Июньский P0 altairtech.io подтверждён: это самый сильный gap-домен (rank 118).

## 2. Gap: ссылаются на ePIC, но не на BiXBiT

Всего gap-доменов **119** из 170. Отсеяно около 45 спам- и нерелевантных доменов (см. §2.3). Ниже 30 целей, отсортированы по сочетанию rank, тематики и достижимости.

Колонки: rank — DFS rank домена-донора в профиле ePIC; «Ссылок» — число backlinks на ePIC; df/nf — атрибут ссылок по DFS.

| # | Домен | Rank | Ссылок на ePIC (nf) | Тип | Приоритет | Outreach-угол |
|---|---|---|---|---|---|---|
| 1 | altairtech.io | 118 | 6 (0 nf) | ASIC-реселлер / хостинг | **P0** | Партнёрство реселлера: карточка «BiXBiT firmware / AMS compatible» на product/partner-страницах. Нужна реальная партнёрская программа [VERIFY: условия у sales] |
| 2 | lightspeedhosting.com | 109 | 16 (0 nf) | Майнинг-хостинг, блог | **P0** | Хостинг-провайдер из ICP: кейс или интеграция AMS-мониторинга для клиентов хостинга, гостевой технический пост в их блоге |
| 3 | miningdisrupt.com | 55 | 1 (0 nf) | Отраслевая конференция | **P0** | Заявка спикера (доклад про J/TH-тюнинг / immersion) и страница exhibitor. Если листинг платный, ссылка должна быть `rel="sponsored"` |
| 4 | hashrateindex.com | — | 1 (0 nf) | Отраслевые данные и медиа (Luxor) | **P1** | Данные для их research (обезличенная статистика флота AMS [VERIFY]). Принадлежит Luxor, то есть конкуренту LuxOS: достижимость средняя |
| 5 | criptonoticias.com | 3 | 3 (0 nf) | Крипто-медиа ES (LatAm) | **P0** | Пресс-питч на испанском: майнинг в Парагвае / LatAm, комментарий эксперта BiXBiT. Гео-приоритет из CLAUDE.md |
| 6 | tokenradar.io | 84 | 9 (0 nf) | Крипто-медиа / обзоры | **P1** | Добавить BiXBiT в обзоры «best ASIC firmware», дать фактуру по dev fee (2.8% / 2% M2x) [VERIFY] |
| 7 | blocktribune.com | 23 | 2 (0 nf) | Крипто-медиа | **P1** | Новостной питч: релиз прошивки или Hydro/Immersion-продукта с цифрами [VERIFY] |
| 8 | kernelpanicpodcast.com | — | 1 (0 nf, spam 70*) | Майнинг-подкаст | **P1** | Гость-инженер в эпизоде, ссылка в show notes. *Spam score, вероятно, ложноположительный, проверить вручную |
| 9 | ungovernablemisfits.com / ungovernable.network | — | 2 + 3 | Майнинг-подкаст и комьюнити | **P1** | Гостевой эпизод про эффективность флота, ссылка в show notes |
| 10 | bitcoinminingstock.io | — | 1 (0 nf) | Отраслевой сайт о публичных майнерах | **P1** | Питч с данными или комментарием для их материалов об эффективности флотов |
| 11 | nobsbitcoin.com | — | 1 (0 nf) | Bitcoin-новости | **P1** | Короткая новость о релизе прошивки или открытой документации |
| 12 | eenewseurope.com | — | 1 (0 nf) | Электроника, трейд-медиа | **P1** | Инженерный угол: PDU / hydro cooling для дата-центров [VERIFY: спеки] |
| 13 | proto.xyz | 20 | 2 (0 nf) | Экосистема Block Proto (майнинг-железо) | **P1** | Если BiXBiT поддерживает Proto-риги или AMS их мониторит [VERIFY], попасть в листинг совместимого ПО |
| 14 | github.com | — | 5 (2 nf) | Dev-платформа | **P1** | Публичный репозиторий (AMS API docs / SDK / release notes) с ссылкой на bixbit.io/en. У BiXBiT уже есть bixbit-dev.github.io |
| 15 | cbinsights.com | 26 | 4 (0 nf) | Бизнес-профиль | **P1** | Заявить или обновить профиль компании |
| 16 | crunchbase.com | — | 3 (2 nf) | Бизнес-профиль | **P1** | Заполнить профиль организации (website, продукты) |
| 17 | messari.io | — | 4 (0 nf) | Крипто-исследования и профили | **P2** | Заявка на профиль или листинг в секторе mining infrastructure |
| 18 | chipstrat.com | — | 2 (0 nf) | Аналитика полупроводников | **P2** | Экспертный комментарий по ASIC-эффективности или прошивкам |
| 19 | btcdaily.org | 7 | 1 (0 nf) | Bitcoin-новости | **P2** | Новостной питч |
| 20 | blockspy.org | 7 | 1 (0 nf) | Крипто-каталог / медиа | **P2** | Листинг компании |
| 21 | greenhausblockchain.com | 10 | 2 (0 nf) | Блог о майнинге | **P2** | Гостевой пост или ресурсная ссылка на гайд по прошивкам |
| 22 | gridlesscompute.com | — | 1 (0 nf) | Off-grid майнинг (Африка) | **P2** | Кейс или партнёрство по мониторингу удалённых сайтов [VERIFY: есть ли кейс] |
| 23 | blocktrainer.de | — | 1 (0 nf) | Bitcoin-образование DE | **P2** | Образовательный материал про тюнинг ASIC |
| 24 | cointime.ai | 51 | 13 (0 nf) | Крипто-агрегатор | **P2** | Попасть через синдикацию новостей (появится само после P1-публикаций) |
| 25 | newswire.ca / c212.net (Cision) | — | 3 + 8 | Пресс-релизы | **P2** | Реальные новости через уже используемый PRNewswire, дистрибуция в Канаду. Ссылки nofollow: ценность в упоминаниях и AI-цитируемости, не в PageRank |
| 26 | medium.com | — | 5 (4 nf) | Блог-платформа | **P2** | Переопубликовать EN-статьи с canonical на bixbit.io/en |
| 27 | zoominfo.com / craft.co / dealroom.co / growjo.com / pitchbook.com | — | по 1–2 | Бизнес-профили | **P3** | Заявить профили, консистентный NAP и website |
| 28 | indodax.com | — | 1 (1 nf) | Биржа, блог (ID) | **P3** | Низкий приоритет, только если будет новостной повод |
| 29 | bitcoinminingmuseum.com | — | 1 | Нишевый ресурс | **P3** | Ресурсная ссылка на историю или гайд по прошивкам |
| 30 | noderunners.network | — | 2 | Bitcoin-комьюнити | **P3** | Участие в комьюнити, без спама |

### 2.3. Отсеяно (не цели)
- **PR-синдикационная сеть «mining fleet management»**, все ссылки nofollow, spam 12–15, появилась в 2026-04: cryptotimesgazette.com, cryptoinsiderreview.com, corporatecryptotimes.com, blockchainnewsonline.com, cryptocurrencynewsline.com, globalcybercurrencytimes.com, worldcybercurrencynews.com, cybercurrencynewscenter.com, cryptonewsbroadcast.com, smartsbusinesswire.com, cryptocurrencyinsidertoday.com, miningpressreleases.com, canadianbusinesstoday.com, personalfinancenewswire.com. Это платное размещение с низкой ценностью, **не покупать**.
- **Спам / PBN-признаки:** chillspot1.com (spam 30), wheretobuybest.link (80), prolinkseo.com (45), exchangegoldforcash.com (55), firstrepubliccapital.com (60), ycm.info (50), pagesearch.net (50), sipgroup.blogspot.com (35), block.xyz (35), webainews.com (30), плюс 13 доменов с PBN-анкором.
- **Нерелевантные или устаревшие форумы:** zcashcommunity.com, grin.mw, ethereum-magicians.org (2019–2020, обсуждения ASIC-resistance), vdfalliance.org, ifttt.com, lady-grodno.com, alicloud.my.id и т.п.

## 3. Где выигрывает BiXBiT

- **Размер профиля:** 885 main RD против 170, 6 706 ссылок против 377, target rank 254 против 190. По объёму BiXBiT впереди даже после вычета спама: примерно 494 домена со spam < 50.
- **Уникальные домены BiXBiT:** 834, из них около 204 «чистых» (spam < 30, без TLD-спам-кластеров). Релевантные уникальные:
  - Крипто- и майнинг-медиа: cryptonews.net (rank 96), newscrypto.net (46), coindoo.com (51), forklog.com (23), cryptohamster.org (51), thebitsignal.com (23), hyperbulle.fr (13), uol.com.br (14, BR — LatAm).
  - Майнинг-ниша: minecool.ru (86), irlbtc.com (65, 104 ссылки), bigstarmining.com (51), ultramining.com (23).
  - Собственные ресурсы: bixbit.pro (99), bixbit-dev.github.io (14). Это не внешний авторитет.
- **СНГ-покрытие:** кластер .ru-доменов (ya.ru, software-expert.ru и др.) закрывает СНГ-рынок, которого у ePIC нет. Часть из них — софт-каталоги сомнительного качества, их нужно проверить вручную.
- **Общие сильные площадки** (есть у обоих): bitcointalk.org, d-central.tech, prnewswire.com, cryptoindustry.com, b.tc, block.cc.

## 4. Риск: спам-профиль BiXBiT

- Target spam score **44** (у ePIC 13). 391 домен со spam ≥ 50 даёт **3 814 ссылок (~57% всех backlinks)**.
- Кластеры: .website 69, .space 67, .site 67, .online 67 (почти все spam ≥ 50); **.com.tr 115 доменов / 1 314 ссылок**, из них 96 со spam ≥ 30; .xyz 34; blogspot.com 185 доменов, 37 со spam ≥ 30.
- Всплески появления: 2025-09 (86 доменов), 2025-10 (98), **2026-01 (156)**, 2026-08 (38). Такой рисунок похож на автоматические или купленные размещения, либо на негативное SEO. [VERIFY у команды: не заказывались ли ссылки подрядчиком в эти месяцы.]

**Рекомендация (на ревью человека, сам ничего не применяю):**
1. Выгрузить backlinks по доменам со spam ≥ 50 и кластерам `.online/.website/.space/.site/.xyz/.com.tr` (эндпоинт `/v3/backlinks/backlinks/live` с фильтром по spam_score) и вручную проверить выборку.
2. Подготовить кандидата в disavow в формате `domain:` **только** для явного спама (PBN-анкоры, казино/гемблинг, doorway). Google в основном игнорирует такие ссылки сам, поэтому disavow нужен как страховка при ручных санкциях или резком падении трафика, а не по умолчанию.
3. Файл disavow загружает в GSC только человек, после ревью.
4. Не трогать чистые .ru, .com.tr и blogspot-домены с spam < 30. Они могут быть реальными упоминаниями.

## 5. План закрытия gap

| Шаг | Что | Цели | Срок | Владелец |
|---|---|---|---|---|
| 1 | Партнёрские и реселлерские листинги | altairtech.io, lightspeedhosting.com, proto.xyz [VERIFY] | 0–30 дней | **Передать человеку (sales/BD) для переговоров** |
| 2 | Конференция и подкасты | miningdisrupt.com, kernelpanicpodcast.com, ungovernablemisfits.com | 0–60 дней | Человек (PR). Шаблоны готовит offpage |
| 3 | Медиа-питчи с данными (US + LatAm ES) | criptonoticias.com, tokenradar.io, blocktribune.com, nobsbitcoin.com, bitcoinminingstock.io, eenewseurope.com, btcdaily.org | 30–90 дней | Человек (PR). Нужна фактура с [VERIFY] |
| 4 | Профили компании | crunchbase, cbinsights, messari, zoominfo, craft, dealroom, pitchbook | 0–14 дней | Маркетинг |
| 5 | Dev- и контент-платформы | github.com (публичный docs/SDK-репо), medium.com (canonical) | 14–45 дней | Dev + контент |
| 6 | Гигиена профиля | Ревью спам-кластеров и кандидат в disavow | 0–30 дней | SEO-лид (решение за человеком) |
| 7 | Повтор замера | Повторить эти 4 эндпоинта, сравнить RD/spam | 2026-12 | offpage-seo |

Следующий шаг для offpage-seo: шаблоны писем для P0/P1 в `content/outreach/` с пометкой «для человека». Переговоры ведёт человек.

*Все метрики взяты из DataForSEO Backlinks API за 2026-09-25. Moz и Bing не использовались (нет ключей). DA/DR не приводятся. Тех-факты о продуктах BiXBiT и ePIC помечены [VERIFY].*
