# Link-gap: BiXBiT (bixbit.io) vs PiTBiT (pitbitecosystem.com + pitbit.online)

Дата: 2026-09-25 · Агент: offpage-seo · Методы: только white-hat. Все outreach-действия помечены «передать человеку»: переговоры ведёт человек, агент их не ведёт.

## 0. Источники данных

| Источник | Статус | Что взято |
|---|---|---|
| DataForSEO `/v3/backlinks/summary/live` (оба домена PiTBiT) | OK | Сводки лежат в `data/dfs-referring-domains-pitbit-2026-09-25.json` (`summaries`) |
| DataForSEO `/v3/backlinks/referring_domains/live` (limit 1000, live, rank desc) | OK | pitbitecosystem.com: 47 main RD. pitbit.online: 49 RD, из них 1 это pitbitecosystem.com. Компактная выгрузка лежит в том же файле. Ответ пришёл inline и в tool-results не сохранился, поэтому поля переписаны вручную: domain, rank, backlinks, spam, first_seen, all_nofollow |
| DataForSEO `/v3/backlinks/backlinks/live` (фильтр `domain_from in/like`) | OK, 5 запросов | URL, анкоры, dofollow и is_lost по нерядовым донорам PiTBiT и по июньским доменам, а также обратная проверка тех же доменов для bixbit.io |
| BiXBiT RD | Из ранее снятого файла | `data/dfs-referring-domains-bixbit.io-2026-09-25.json` (885 main RD) |
| `domain_intersection` | Не использовался | Фильтр exclude игнорируется. Gap посчитан локально как (RD eco ∪ RD online) \ RD BiXBiT |
| Cross-reference | Из файлов | ePIC: `data/dfs-referring-domains-epicblockchain.io-2026-09-25.json` (170). EMCD: `data/dfs-referring-domains-emcd.io-2026-09-25.json` (топ-1000) и probes-файл |
| Moz API / Bing Webmaster | **Нет доступа** | Ключей в `.env` нет |

## 1. Сравнение профилей

| Метрика | BiXBiT | pitbitecosystem.com | pitbit.online |
|---|---|---|---|
| DFS rank (target) | **254** | 97 | 130 |
| Backlinks | **6 706** | 60 | 105 (из них 50 с собственного pitbitecosystem.com) |
| Referring main domains | **885** | 47 | 49 (48 без своего домена) |
| Nofollow main RD | 401 (45%, все ссылки nf) | 13 (28%) | 11 (22%) |
| backlinks_spam_score | 44 | 34 | 30 (target_spam_score 25) |
| RD со spam ≥ 45 | 391 / 885 (44%) | **35 / 47 (74%)** | **45 / 49 (92%)** |
| Прирост в сентябре 2026 | — | 20 RD, почти все это «SEO-checker» автоспам (`*seo*.link/.info`, `backlink*`) | 4 |
| Первое появление | 2025-08 | 2025-05 | 2023-11 |
| Broken pages (DFS crawl) | — | **406 из 683** просканированных | — |
| Гео доноров | TR, RU, UA, BR | RU (все нормальные доноры) | Каталоги без гео, плюс RU и BY |

**Вывод.** У PiTBiT профиль крошечный. Нормальных доноров всего около 15, почти все из RU: каталоги майнинг-компаний, партнёры-хостеры, одно медиа-обзорное, вакансии, реестр РБК. Остальное (примерно 80 из 96 RD) это автогенерируемые каталоги и SEO-чекеры. **40 из 77 уникальных доменов PiTBiT ссылаются и на BiXBiT.** Это тот же фоновый спам: australianwebdirectory.*, betwinnermirror.com, *-directory.com, urls-shortener.eu и т.п. Он общий для ниши, это не сигнал качества.

## 2. Проверка июньского отчёта (2026-06-19)

| Домен | Июнь | Сейчас (DFS) | Вердикт |
|---|---|---|---|
| top-mining.ru | «ссылается на PiTBiT» | Подтверждено: `/proshivka/pitbit/` (карточка бренда, df, utm) и `/rating/rejting-proshivok-dlya-asikov-top-5/` («Рейтинг прошивок для асиков: ТОП-6», анкор «кастомная прошивка», df, 2026-08-12). На BiXBiT ссылок нет | **Подтверждён**, это главная цель |
| cryptodesk.ru | «обзор» | Подтверждено: «Обзор PITBIT ONLINE: прошивка и система мониторинга ASIC-майнеров», 2 df-ссылки. Но last_seen 2025-09-27, так что страница могла выпасть из краула [VERIFY вручную] | **Подтверждён** (возможно, устарел) |
| altcoinlog.com | «roundup, PiTBiT есть, BiXBiT нет» | **Опровергнуто.** DFS не видит ссылки на PiTBiT. А BiXBiT **уже есть** в `/prochivka-asic/` («Лучшие прошивки для асиков в 2026 году», nofollow → `/ru/firmwares`, с 2023-11) | Не gap. Задача другая: освежить описание BiXBiT, добавить EN-версию и ссылку на `/en` |
| ultramining.com | «ссылается на PiTBiT» | **Опровергнуто.** Ссылок на PiTBiT нет: в июне ссылка вела на Telegram, для PiTBiT это unlinked. У BiXBiT 2 **dofollow**-ссылки (цитата про иммерсионное охлаждение, `/ru/blog/...попутном-нефтяном-газе`), одна потеряна (tag-страница отдаёт 400) | BiXBiT выигрывает |
| dubaipeople.ae | «sponsored PR» | Частично: df-ссылка на `/en/` жила с 2026-07-09 по 2026-08-12, сейчас **is_lost**. Страница отдаёт «One moment, please...» | Потеряна у PiTBiT. P2 только редакционным путём |

## 3. Gap: ссылаются на PiTBiT, но не на BiXBiT (без спама)

Из 37 gap-доменов 23 это автоспам (SEO-чекеры, backlink-генераторы, pbn-подобные каталоги). Они **не цели**, список в §6. Ниже 14 реальных.

| # | Домен | DFS rank домена | Ссылка у PiTBiT | Тип | Приоритет | Угол (передать человеку) |
|---|---|---|---|---|---|---|
| 1 | **top-mining.ru** | 178 | 2 стр., df: карточка бренда и «ТОП-6 прошивок» | RU-медиа / рейтинг прошивок | **P0** (cross EMCD) | Запросить карточку `/proshivka/bixbit/` и включение в «Рейтинг прошивок». Фактура: dev fee 2.8% / 2% для M2x [VERIFY], поддержка Whatsminer (у PiTBiT её нет) [VERIFY модели], immersion. Если размещение платное, то только с `rel="sponsored"`, покупать ради ссылки нельзя |
| 2 | **rushash.ru** | 104 | Главная, df, блок партнёров | Майнинг-хостинг «под ключ» (RU) | **P0** (cross EMCD) | BD-партнёрство: прошивка, AMS-мониторинг и hydro/immersion для клиентов хостинга. Реальная интеграция даёт логотип в блоке партнёров. **Передать BD** |
| 3 | **trustmining.ru** | 51 | 3 стр. профиля компании (about, offices, shop), df, с 2026-08 | Каталог и отзывы майнинг-компаний (RU) | **P0** (быстро) | Зарегистрировать профиль BiXBiT: офисы, каталог, сайт. Если профиль платный, то только с разметкой sponsored [VERIFY условия] |
| 4 | **dc-mining.ru** | 139 | 3 товарные стр. «GAS EcoSystem», df, анкор «PITBIT ECOSYSTEM» | Газовый майнинг / готовые решения (RU) | **P1** | Совместный продукт для газовых площадок: immersion или hydro, прошивка и AMS. У BiXBiT уже есть контент про попутный газ (его цитирует ultramining). **Передать BD** [VERIFY кейс] |
| 5 | **cryptodesk.ru** | 222 | Обзор PITBIT ONLINE, 2 df | Магазин ASIC с блогом «Обзоры товара» (RU) | **P1** | Предложить обзор «Прошивка BiXBiT + AMS»: демо-доступ, тех-данные [VERIFY]. Сначала вручную проверить, жива ли страница PiTBiT |
| 6 | **hidix.ru** | 23 | Туториал «Разгон Antminer L7, прошивка PitBit», df, 3 ссылки | Тех-блог / гайды (RU) | **P1** | Гостевой туториал «Тюнинг Antminer S19/S21 или Whatsminer M3x на BiXBiT: J/TH до и после» [VERIFY цифры и модели]. Только реальные тест-данные |
| 7 | **crypto-emergency.com** | 273 | Пост про Blockchain Life 2025, nf | Крипто-медиа RU, event-репортажи | **P1** | Пресс-кит к ближайшему Blockchain Life (Дубай, UAE это гео-приоритет): если BiXBiT участвует, дать анонс и фактуру [VERIFY участие] |
| 8 | **kernelpanicpodcast.com** | — | 1, spam 70* | Майнинг-подкаст (EN) | **P1** (cross ×3) | Гость-инженер, ссылка в show notes. *У PiTBiT обе ссылки first_seen 2026-09-25, в одной волне со спамом. Проверить вручную, что это реальные show notes |
| 9 | **companies.rbc.ru** | 622 | Карточка юрлица, df | Бизнес-реестр РФ | **P2** (cross EMCD rbc.ru) | Заполнить карточку, только если есть российское юрлицо [VERIFY]. У EMCD ссылки с rbc.ru, скорее всего, редакционные, это отдельный PR-трек |
| 10 | **pk.by** | 150 | Страница «Ремонт ASIC в Минске», df, реферальная ссылка PiTBiT | Сервис ремонта ASIC (BY) | **P2** | Сервисное партнёрство: ремонтники ставят прошивку клиентам. Только если есть реальная партнёрская программа [VERIFY у sales]; ссылка с корректным `rel`. **Передать BD** |
| 11 | **dubaipeople.ae** | 157 | Потеряна (2026-08) | Lifestyle/PR-медиа UAE | **P2** | Только редакционный материал с UAE-углом (хостинг, охлаждение при +45 °C) [VERIFY]. Не покупать |
| 12 | hh.ru / tourbc.ru / it-vacancies.ru | 697 / 180 / 224 | Работодательские профили | Вакансии | **P3** (hh.ru cross EMCD) | Только при реальном найме в RU/KZ (hh.kz). Не SEO-цель |
| 13 | ontivideo.ru | 32 | Карточка компании (Москва), nf | Бизнес-каталог | **P3** | Только при наличии офиса. Низкая ценность |
| 14 | minerfirmware.online | — | nf, first_seen 2026-09-25 | EN-гайд по прошивкам | Не gap | BiXBiT **уже есть** (nf, тот же день). Мониторить, проверить корректность описания |

## 4. Cross-competitor: в gap у ≥2 из ePIC / EMCD / PiTBiT

| Домен | ePIC | EMCD | PiTBiT | Тип | Приоритет | Комментарий |
|---|---|---|---|---|---|---|
| **kernelpanicpodcast.com** | ✓ | ✓ | ✓ (оба домена) | Майнинг-подкаст EN | **P1** | Единственный домен в gap у всех трёх. Spam 70 и синхронное появление 2026-09-25 требуют ручной проверки |
| **top-mining.ru** | — | ✓ (5 ссылок) | ✓ (2 стр., df) | RU рейтинг прошивок | **P0** | Самая релевантная цель в СНГ |
| **rushash.ru** | — | ✓ (4, rank 18) | ✓ (главная, df) | RU хостинг | **P0** | BD |
| rbc.ru | — | ✓ (3 df, probes) | ✓ (companies.rbc.ru) | Бизнес-медиа / реестр | **P2** | У конкурентов разные типы ссылок |
| hh.ru | — | ✓ | ✓ | Вакансии | **P3** | Не SEO-цель |
| onvaxs.com, plurio.shop | — | ✓ | ✓ | Спам (60) | Исключить | Общий фоновый спам |
| ycm.info, wheretobuybest.link | ✓ | — | ✓ | Спам (50–80) | Исключить | То же |

Для справки: cross-gap ePIC∩EMCD (criptonoticias, miningdisrupt, bitcoinminingstock.io, digitalcurrencyresearch.io) у PiTBiT отсутствует. PiTBiT на EN-рынке не представлен вообще.

## 5. Где выигрывает BiXBiT

- **Масштаб:** rank 254 против 97/130, 885 main RD против примерно 15 реальных доноров у PiTBiT.
- **СНГ-медиа, которых у PiTBiT нет:** bits.media (34 ссылки), miningclub.info (10), minecool.ru (rank 86), ultramining.com (2 df, редакционная цитата), forklog.com, habr.com, neftegaz.ru, cryptosummit.ru, altcoinlog.com (roundup прошивок).
- **EN-отрасль:** bitcointalk.org (177 ссылок), b.tc (rank 227), d-central.tech, prnewswire.com, cryptoindustry.com, block.cc, bixbit-dev.github.io. У PiTBiT EN-доноров ноль.
- **Контентные поводы для ссылок,** которых у PiTBiT нет: Whatsminer, immersion и hydro, PDU (июньский content gap остаётся актуальным [VERIFY]).
- **Техника у PiTBiT:** 406 broken pages из 683 по DFS. Это возможность для broken-link outreach, если на их битые URL ссылаются внешние сайты. Отдельно это не проверялось, запрос можно сделать следующим циклом.

## 6. Отсеяно (не цели)

- **23 спам-домена в gap:** dacheckerfree.site, rankcheckertools.shop, seocheckerforfree.online, backlinkmaker.link, tokoseo.com, goldbacklinks.info, boost-traffic.com/.info, wholinkstomysite.store, freesimpleseo.link, backlinkwizards.link, usaseobiz.info, youseotools.link, digitseotools.info, indiabacklink.com, theseobiz.com, onvaxs.com, jobsapp.info, plurio.shop, ycm.info, wheretobuybest.link и т.п.
- **40 общих доменов** PiTBiT∩BiXBiT почти целиком спам-каталоги: `*webdirectory*`, `*directory.com`, `topacted.com`, `99bestsite.com`, `betwinnermirror.com`, `homesforsaleoldgreenwichct.com`, url-шортенеры. У BiXBiT они попадают в общую ревизию спам-кластеров. **Кандидаты в disavow только на ревью человека**, сам я ничего не применяю.

## 7. План

| Шаг | Что | Цели | Срок | Владелец |
|---|---|---|---|---|
| 1 | RU-рейтинги и каталоги | top-mining.ru (карточка и ТОП), trustmining.ru (профиль) | 0–30 дн. | **Передать человеку (PR RU)**. Шаблон письма готовит offpage в `content/outreach/` |
| 2 | Хостинг и партнёры СНГ | rushash.ru, dc-mining.ru, pk.by | 0–60 дн. | **Передать человеку (BD) для переговоров** |
| 3 | Обзоры и гайды RU | cryptodesk.ru, hidix.ru | 30–60 дн. | Человек (PR). Тех-данные только с [VERIFY] |
| 4 | Event / UAE | crypto-emergency.com (Blockchain Life), dubaipeople.ae (только editorial) | по календарю событий | Человек (PR) |
| 5 | Подкаст (cross ×3) | kernelpanicpodcast.com, после ручной проверки | 0–45 дн. | Человек (PR) |
| 6 | Обновить существующие упоминания | altcoinlog.com (освежить описание, попросить ссылку на `/en`), ultramining.com (восстановить потерянную tag-ссылку не нужно, это archive-страница), minerfirmware.online (проверить описание) | 0–30 дн. | offpage + человек |
| 7 | Повтор | summary и RD обоих доменов PiTBiT; проверить broken pages PiTBiT на внешние ссылки | 2026-12 | offpage-seo |
