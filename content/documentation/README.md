# content/documentation: мета, H1 и ALT для документации и FAQ

> **Дата:** 2026-09-28. **Владелец:** content-seo. **Источники:** краул `data/crawl-2026-09-28/`, сырой HTML 106 страниц + 28 legacy-URL (python urllib, 2026-09-28),
> GSC `data/gsc-pages-2026-09-28.json`, `data/gsc-queries-pages-all-2026-09-28.json` (28 дней, все страны).
> Изображения в документации встроены в HTML как base64, имён файлов нет. Все 67 уникальных картинок без ALT декодированы и просмотрены, ALT написаны по картинке и тексту шага, а не по догадке.

## 1. Файлы пакета

| Файл | Что внутри | Кому |
|---|---|---|
| `meta-docs.md` | 106 URL: title, description, H1 сейчас → новые; GSC; целевой запрос; приоритет по CTR; техправки H1 | контент-менеджер CMS, SEO |
| `meta-docs.csv` | то же плоской таблицей (url, title, description, h1, note) для импорта | CMS |
| `alt-docs.csv` | 116 строк: 105 новых ALT, 8 замен неверных ALT, 3 строки шаблона | CMS, фронтенд (шаблон) |
| `translation-map-docs.csv` | 51 пара EN ↔ RU по содержанию (не по slug) | разработчик: переключатель языка (P0-5 dev-task), hreflang |
| `README.md` | покрытие, правила ALT, дубли, что осталось | все |

## 2. Покрытие

| Что | Сделано | Осталось |
|---|---|---|
| Мета + H1, документация EN | 51 из 51 индексируемых URL | — |
| Мета + H1, документация RU | 53 из 53 (3 legacy — H1 на время до 301, мету не вносить) | — |
| FAQ `/en/faq`, `/ru/faq` | мета + H1 (на обеих нет H1) | FAQPage-разметка — задача technical-seo |
| ALT: изображения без атрибута `alt` | **105 из 105** на 28 страницах (EN 45 + иконка FAQ, RU 58 + иконка FAQ) | — |
| ALT: существующие | 281 проверены автоматически (язык, длина, дубли на странице); 8 заменены (4 на русском на EN-страницах, 4 не соответствуют картинке) | визуально не сверены ~273 существующих ALT, см. §5 |
| ALT: шаблон | логотип в шапке (`alt="logo"` → `BiXBiT`), флаги языка (→ `alt=""`) | — |
| Legacy EN `user-guide-for-whatsminer-asic/*` (28 URL) | карта 301 (§4.1) | мета и ALT не делались: страницы уходят в 301 |
| docs.bixbit.io, `/es/documentation` | не в объёме задачи | решение по хосту (§4.2) |

Пустых `alt=""` на контентных изображениях документации нет (0 из 386). Цифра 3 149 из отчёта краула относится к остальному сайту, в основном к шаблону прошивок.

## 3. Правила ALT (как написаны и как дописывать новые)

1. **Описывает, что на картинке и зачем она на шаге.** «Whatsminer control board module: fan connector (1), retaining screws (2) and PSU cable (3)», а не «image» или «step 1».
2. **Маркеры ①②③ со скриншотов** передаются как (1), (2), (3) с названием детали. Текст шага ссылается на них, и ALT должен давать ту же связь человеку со скринридером.
3. **Цифры в ALT только те, что видны на картинке и совпадают с текстом:** 13.83 V, 14.52 V, 138,571 GH/s, 533 / 3900 / 4100. Если на картинке цифра, которой нет в тексте, или она нечитаема, её не пишем, либо ставим `[VERIFY]`.
4. **Язык ALT = язык страницы.** На EN-странице нет кириллицы, на RU-странице английские только названия кнопок и полей интерфейса (Overclock, Liquid Cooling, Burn).
5. **Длина до ~125 символов**, без «Image of…», без переспама ключами. Бренд BiXBiT — только там, где он действительно в кадре (интерфейс прошивки).
6. **Одна и та же картинка на родителе и на подстранице** (например, раздел 3 и 3.1 доп. БП) получает один ALT. Дубли ALT внутри одной страницы не допускаются.
7. **Декоративные** (иконка вопроса у блока поддержки, флаги рядом с подписью US/RU) получают `alt=""`, атрибут обязателен.
8. **Логотип-ссылка** получает ALT, равный названию ссылки: `BiXBiT`.
9. **Не выдумывать содержимое.** Если картинку не открывали или она не совпадает с текстом, в ALT пишем по фактическому изображению и ставим `[VERIFY]` в note (так помечены 9 строк).

Как найти картинку в CMS: у inline-изображений нет имени файла. В `alt-docs.csv` указаны порядковый номер изображения в контенте (`img #N`, без картинок шапки), фрагмент текста перед ним и sha1 первых 10 символов data-URI.

## 4. Дубли документации: рекомендация

### 4.1 `user-guide-for-whatsminer-asic` против `new-user-guide-for-whatsminer-asic` (EN)

**Факт (2026-09-28):**
- `/en/documentation/user-guide-for-whatsminer-asic` отвечает 200, стоит в sitemap, но **контента нет**: только боковое меню, H1 нет. На неё ведут 209 ссылок из блога с анкором-опечаткой «User guid for Whatsminer ASIC» и 302-редирект с поста про WhatsminerTool.
- 28 старых подстраниц `/en/documentation/user-guide-for-whatsminer-asic/*` живы (200, self-canonical, индексируемые), но краул до них не дошёл: **внутренних ссылок нет**. При этом в GSC у них **48 кликов и 3 426 показов** за 28 дней. `6-miner-overclock` стоит на поз. 1.6 по «whatsminer m3 overclock». Это дубли новой версии руководства.
- RU-версия одна (`rukovodstvo-polzovatelia-whatsminer-asic`), но внутри неё 3 legacy-страницы старой структуры (§4.4).

**Рекомендация [VERIFY: подтверждение команды]:**
1. `user-guide-for-whatsminer-asic` → **301** на `new-user-guide-for-whatsminer-asic`, убрать из sitemap. Пока 301 нет, внести временную мету и H1 из `meta-docs.md`.
2. 28 подстраниц → **301** по карте ниже (сопоставление по содержанию, 3 пары под `[VERIFY]`).
3. 302 с `/en/blog/post/detailed-guide-on-how-to-install-the-new-bixbit-firmware-via-whatsminertool` заменить на 301 **сразу на** `new-user-guide-for-whatsminer-asic/4-firmware-installation-and-update`, без цепочки через старый хаб. RU-пост → `rukovodstvo-…/4-obnovlenie-proshivki-mainera` (сейчас 302 на хаб руководства).
4. 209 ссылок из блога переписать на новый URL, анкор исправить на «Whatsminer user manual» (список — `data/crawl-2026-09-28/links.csv.gz`, target = старый хаб).
5. После 301 переименовывать slug `new-user-guide-…` не нужно: URL уже набрал показы, «new» в адресе на ранжирование не влияет.

| Старый URL (`/en/documentation/user-guide-for-whatsminer-asic/…`) | GSC клики / показы / поз. | 301 → (`/en/documentation/new-user-guide-for-whatsminer-asic/…`) | Примечание |
|---|---|---|---|
| `4-1-update-the-firmware-using-the-utility-whatsminertool` | 3 / 774 / 37.0 | `4-2-procedure-for-control-boards-h3-h6-or-h6os` | [VERIFY] старый 4.1 = обновление через WhatsMinerTool |
| `4-miner-firmware-update` | 4 / 453 / 41.7 | `4-firmware-installation-and-update` |  |
| `4-2-updating-the-firmware-using-the-sd-card` | 13 / 338 / 14.3 | `4-3-procedure-for-control-board-h616` | [VERIFY] SD-карта теперь в 4.3 и Прил. 3.2 |
| `6-miner-overclock` | 0 / 270 / 11.1 | `6-miner-overclocking-and-related-functions` | поз. 1.6 по «whatsminer m3 overclock» — сохранить вес |
| `5-immersion-cooling` | 5 / 267 / 15.1 | `5-immersion-cooling-1` |  |
| `3-3-pool-and-worker-setup` | 5 / 190 / 10.4 | `3-3-pool-and-worker-setup-1` |  |
| `5-2-updating-the-power-supply-unit-firmware` | 5 / 187 / 21.7 | `5-3-disabling-power-supply-fan-checks` | прошивка БП M2X теперь в 5.3.2 |
| `3-initial-device-setup` | 0 / 158 / 16.6 | `3-initial-device-setup-1` |  |
| `7-3-reset-miner-settings-to-factory-values` | 4 / 151 / 5.2 | `7-3-resetting-miner-settings-to-factory-defaults` |  |
| `6-3-additional-overclocking-settings` | 3 / 145 / 24.9 | `6-1-options-available-on-the-overclock-tab` | [VERIFY] Advanced Options теперь в 6.1 |
| `6-5-overclocking-recommendations` | 1 / 79 / 19.3 | `6-4-overclocking-recommendations` |  |
| `4-3-installing-the-updated-version` | 1 / 61 / 27.0 | `4-4-updating-bixbit-firmware-to-a-newer-version-on-any-control-board-model` |  |
| `6-1-overclocking-settings-page` | 2 / 50 / 12.4 | `6-1-options-available-on-the-overclock-tab` |  |
| `appendix-1-3-ams` | 1 / 46 / 33.3 | `appendix-1-3-ams-1` |  |
| `3-1-miner-identification-on-the-network` | 1 / 42 / 12.2 | `3-1-miner-identification-on-the-network-1` |  |
| `5-2b-disabling-power-supply-fan-check-for-m3x-m5x-series-miners` | 0 / 33 / 5 | `5-3-disabling-power-supply-fan-checks` | теперь 5.3.1 |
| `7-2-logs-export` | 0 / 26 / 5.2 | `7-2-log-export` |  |
| `2-connecting-a-device` | 0 / 25 / 19 | `2-connecting-a-device-1` |  |
| `7-additional-operations` | 0 / 25 / 44.5 | `7-additional-operations-1` |  |
| `6-2-options-available-on-the-overclock-page` | 0 / 23 / 68.7 | `6-1-options-available-on-the-overclock-tab` | старый 6.2 = новый 6.1 |
| `appendix-1-additional-functionality` | 0 / 20 / 7.5 | `appendix-1-additional-functionality-of-bixbit-firmware` |  |
| `appendix-1-2-hotel-fee` | 0 / 15 / 5.8 | `appendix-1-2-hotel-fee-1` |  |
| `1-technical-requirements` | 0 / 14 / 65.3 | `1-technical-requirements-1` |  |
| `6-4-general-overclocking-strategy` | 0 / 14 / 27.4 | `6-3-general-overclocking-strategy` |  |
| `appendix-1-1-tab-proxy` | 0 / 8 / 6.5 | `appendix-1-3-proxy` |  |
| `5-1-preparing-the-miner-for-the-dive` | 0 / 7 / 16.3 | `5-1-preparing-the-miner-for-immersion` |  |
| `appendix-2-determining-the-permissible-operating-temperature-limit-of-miners-chips` | 0 / 4 / 6 | `appendix-2-determining-the-permissible-operating-temperature-limit-of-miners-chips-1` |  |
| `7-1-export-of-the-list-of-miners-of-the-main-window-with-table-data-to-csv-file` | 0 / 1 / 8 | `7-1-export-the-device-list-and-their-information-from-whatsminertool-to-a-csv-file` |  |
### 4.2 docs.bixbit.io

Решение принимается по `content/localization-plan.md` (P0-5, вопрос Q5) и `content/hreflang-spec.md` §7. Позиция content-seo:
1. **Основной хост индексируемой документации — `bixbit.io/{en,ru}/documentation`.** Здесь трафик: 745 кликов за 28 дней, из них 414 на двух страницах кодов ошибок. Здесь же перелинковка с `/firmwares` и `/ams`.
2. Страницы кодов ошибок на docs.bixbit.io (совпадение 93–94%) должны получить **cross-domain canonical** на `…/list-of-errors-and-solutions-1` и `…/spisok-oshibok-i-sposoby-resheniia`. Иначе Google может выбрать канонической копию на поддомене, и самая трафиковая RU-страница просядет.
3. Уникальные Antminer-разделы docs.bixbit.io (установка и интерфейс прошивки Antminer, подключение к AMS) перенести в `/en|ru/documentation/*` с 301. Это закрывает запланированную в архитектуре v2 страницу `/en/documentation/antminer-firmware-install` без написания с нуля [VERIFY: slug у команды].
4. Если docs.bixbit.io остаётся отдельной продуктовой документацией, на его дублях нужен `noindex` или canonical, уникальные description (сейчас везде «Documentation») и sitemap. В кластеры и hreflang bixbit.io поддомен не включать.

### 4.3 Тонкие страницы-обёртки

`/en/documentation/error-codes-for-whatsminer-asic` и `/ru/documentation/kody-oshibok-dlia-whatsminer-asic` содержат только одну ссылку на список. RU-обёртка ранжируется по тем же запросам, что и список (поз. 9–23).
- **Не 301**: страница-раздел нужна для хлебных крошек и структуры CMS.
- Дать 2–3 предложения вступления и крупную ссылку «полный список кодов». Title отличается от title списка (сделано в `meta-docs.md`), чтобы не спорить за «ошибки whatsminer».
- То же для двух хабов доп. БП (`connecting-an-additional-…`, `podkliuchenie-…`): 2–6 ссылок без текста.

### 4.4 Внутренние дубли

| Что | Где | Рекомендация |
|---|---|---|
| Родитель раздела выводит полный текст всех подстраниц | EN 3, 4, 5, 6, 7, Прил. 1, Прил. 3, раздел 3 доп. БП; RU то же | На родителе оставить обзор (2–3 предложения) и список ссылок на подстраницы. Canonical на подстраницу не ставить: у родителя шире тема и свои запросы (RU «4. Установка и обновление»: 905 показов по «bixbit прошивка», «whatsminer прошивка») [VERIFY: умеет ли CMS] |
| RU legacy 5.1 без «-1» | `…/5-1-podgotovka-mainera-k-pogruzheniiu` ↔ `…-1` | 301 на `…-1` |
| RU legacy 5.2а / 5.2б | `…/5-2-obnovlenie-proshivki-bloka-pitaniia`, `…/5-2b-…-m3x-m5x` | 301 на `…/5-3-otkliuchenie-proverki-ventiliatorov-bloka-pitaniia` [VERIFY: 5.3.1/5.3.2 покрывают весь старый текст] |
| RU Приложение 3 под slug 4.4.2 / 4.4.3 | `4-4-2-formatirovanie-sd-karty`, `4-4-3-zagruzka-…` + `prilozhenie-3-…` | URL не менять: у 4.4.2 и 4.4.3 1 159 показов (FAT32, PhoenixCard). `prilozhenie-3` сделать обзором со ссылками (как в строке 1) |
| RU slug не совпадает с содержанием | `6-1…`, `6-2-dostupnye-…-optsii` (= Profile Switcher), `6-3-dopolnitelnye-…` (= стратегия), `6-4-obshchaia-strategiia-…` (= рекомендации) | URL не менять. Пары EN ↔ RU для переключателя языка и hreflang брать из `translation-map-docs.csv`, а не по slug |
| Нумерация приложений EN ≠ RU | EN 1.1 Boards / 1.3 Proxy, RU 1.1 Proxy / 1.3 Boards; AMS: «1.3» на странице, «1.4» в меню | Привести к одной схеме [VERIFY: какая верная] |

### 4.5 Смежная техническая проблема (передать technical-seo)

Скриншоты встроены в HTML как base64. Страницы документации весят до **11.7 MB** (`prilozhenie-3` RU), 11.2 MB (EN Appendix 3), 9.6 MB (RU 4.4.2), 5–8 MB у страниц доп. БП.
Это бьёт по LCP и краулинговому бюджету. Кроме того, у картинок нет имён файлов, и Google Images их не индексирует как отдельные ресурсы.
**ТЗ:** вынести изображения в файлы (`/assets/docs/<раздел>/<описательное-имя>.webp`) с `width`/`height` и `loading="lazy"` ниже первого экрана. ALT из `alt-docs.csv` переносятся без изменений.

## 5. Что осталось

1. **Визуальная проверка ~273 существующих ALT.** В выборке Appendix 3.2 два из восьми существующих ALT описывали не ту картинку (сдвиг на один шаг). Вероятно, ALT генерировались по порядку, и сдвиги есть и на других страницах. Приоритет: EN Appendix 3.1, 3.2, раздел 4, RU 4.4.2, 4.4.3 (у них больше всего картинок и показов).
2. **FAQPage.** На `/en/faq` и `/ru/faq` FAQ-контент есть (33 и 32 вопроса), а разметки нет. На 52 страницах документации, наоборот, пустой FAQPage (P1 из краула). Задача technical-seo.
3. **Контентные расхождения EN ↔ RU**, найденные при проверке фактов:
   - RU 4.2 без раздела 4.2.2 (заводская прошивка 2025+), а текущий RU description обещает «откат версии 2025 года»;
   - объём SD-карты: EN «2–16 GB», RU «8–16 ГБ» (Технические требования);
   - EN 5-й шаг доп. БП: вместо страницы статуса стоит дубль скриншота Overclock (на RU-версии картинка верная);
   - нумерация приложений (§4.4).
4. **Legacy EN (28 URL) и docs.bixbit.io** — мета и ALT не делались, ждут решения по 301/canonical.
5. **Замер эффекта:** через 28 дней после внедрения сравнить CTR страниц из таблицы приоритетов (`meta-docs.md`) в GSC.

## 6. [VERIFY]-список для команды

| # | Что проверить | Где |
|---|---|---|
| V1 | Текущая ставка dev fee (FAQ пишет 1.8%–2.8%, подтверждено 2.8% / 2% для M2x) | `/en/faq`, `/ru/faq` |
| V2 | «Для каждой ошибки» и «от инженеров BiXBiT» в description RU-кодов (из брифа) | RU список ошибок |
| V3 | 301 legacy EN: 3 пары с пометкой (старые 4.1, 4.2, 6.3) | §4.1 |
| V4 | Полнота переноса RU 5.2а / 5.2б в 5.3 перед 301 | §4.4 |
| V5 | Нумерация приложений EN/RU (Boards, Proxy, AMS 1.3/1.4) | §4.4 |
| V6 | Неверный скриншот на EN «5. General recommendations…», 2-я картинка | `alt-docs.csv` |
| V7 | Какой БП на двух финальных замерах 14.76 V (M30S+ V70) | `alt-docs.csv`, EN и RU |
| V8 | Разъём (4) на фото RU 5.1 (симулятор вентилятора для M2X?) | `alt-docs.csv` |
| V9 | Скриншот Boards: воздушное или жидкостное охлаждение | `alt-docs.csv` |
| V10 | Объём SD-карты 2–16 или 8–16 ГБ | EN/RU «Технические требования» |
| V11 | Решение по docs.bixbit.io (основной хост или вспомогательный) | §4.2 |
