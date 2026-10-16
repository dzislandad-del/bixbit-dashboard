# docs.bixbit.io, группа A: мета-теги и H1 (30 страниц EN + RU)

**Дата:** 2026-09-29 · **Движок:** VitePress 2.0.0-alpha.17 · **ALT к этим страницам:** `group-a-alt.csv` (102 изображения на 18 страницах)

**Охват:** главная, `/docs.html`, хаб установки и `antminer.html`, весь раздел `/additional_instructions/`, раздел `/ams/`, плюс их `/ru/`-версии. Не входят: `basic_asic_miner_configuration`, `functionality_of_the_bixbit_firmware/**` (другой агент) и `installing_and_updating_bixbit_firmware/whatsminer.html` (готово: `whatsminer-installing-updating.md`).

**Как проверено:** сырой HTML всех 30 страниц (python urllib, 2026-09-29): `<title>`, `description`, `og:*`, canonical, текст. Инвентарь: `data/docs-bixbit-io-inventory-2026-09-29/inventory.json`. Запросы: `data/bing-queries-2026-09-28.json`. Bing отдаёт запросы по всем хостам сразу, поэтому к docs.bixbit.io их можно привязать только по смыслу. GSC по docs.bixbit.io не подключён.

---

## 0. Как вставлять

1. **Шаблон title.** Считаю, что в `.vitepress/config` будет `titleTemplate: ':title | BiXBiT Docs'` (схема из `whatsminer-installing-updating.md`, §2, вариант A). Сейчас суффикс ` | Documentation` / ` | Документация`. Frontmatter `title` ≤ 46 символов, итоговый `<title>` ≤ 60.
2. **og:title / og:description отдельно не нужны.** Конфиг сайта уже выводит их сам. Код `transformHead` опубликован на `/docs.html` (блок с `pageData.frontmatter.head.push`): `og:title` = `title`, `og:description` добавляется, если у страницы есть `description`, `og:image` берётся из поля `ogImage`. Сейчас `og:description` нет ни на одной странице, потому что у страниц нет своего `description`. После вставки frontmatter он появится сам. Если добавить ещё и `head` с `og:*`, как в образце, теги задвоятся. [VERIFY: в репозитории `transformHead` такой же, как в примере на `/docs.html`]. Если конфиг другой, `head`-блок для og собирается из тех же `title`/`description`, пример — `whatsminer-installing-updating.md`.
3. **Все значения в двойных кавычках.** Во многих description есть `: `, без кавычек YAML их не прочитает. Все 30 блоков ниже проверены парсером (`ruby -ryaml`, `YAML.safe_load`): ошибок нет.
4. **PageCMS.** В форме редактора: «Заголовок» — это `title`, «SEO-описание» — это `description` (так в инструкции `/docs.html`, раздел SEO). В Source это те же поля frontmatter.
5. **H1.** Правку предлагаю только там, где H1 плохой: пустой, «Home» или шире содержания страницы. Где столбец «H1 → предлагаю» пуст, текущий H1 оставить.
6. **hreflang** между EN и RU не выводится ни на одной странице. Решение общее для сайта, см. `whatsminer-installing-updating.md`, §4 п. 2.

---

## 1. Сводная таблица

| # | URL | Новый `title` (длина) | Итоговый `<title>` | `description` | H1 → предлагаю |
|---|---|---|---|---|---|
| 1 | `/` | Antminer & Whatsminer Firmware Guides (37) | 51 | 153 | BiXBiT Documentation |
| 2 | `/ru/` | Документация по прошивкам ASIC и AMS (36) | 50 | 147 | Документация BiXBiT |
| 3 | `/docs.html` | PageCMS Editor Guide (Internal) (31) | 45 | 156 | — |
| 4 | `/ru/docs.html` | Редактирование документации в PageCMS (37) | 51 | 150 | — |
| 5 | `/installing_and_updating_bixbit_firmware/` | Install and Update BiXBiT Firmware (34) | 48 | 156 | Installing and Updating BiXBiT Firmware |
| 6 | `/ru/installing_and_updating_bixbit_firmware/` | Установка и обновление прошивки BiXBiT (38) | 52 | 144 | Установка и обновление прошивки BiXBiT |
| 7 | `/installing_and_updating_bixbit_firmware/antminer.html` | Install & Update Antminer Firmware (34) | 48 | 156 | — |
| 8 | `/ru/installing_and_updating_bixbit_firmware/antminer.html` | Установка и обновление прошивки Antminer (40) | 54 | 160 | — |
| 9 | `/additional_instructions/` | Antminer & Whatsminer How-To Guides (35) | 49 | 156 | Additional Instructions |
| 10 | `/ru/additional_instructions/` | Инструкции для Antminer и Whatsminer (36) | 50 | 153 | Дополнительные инструкции |
| 11 | `/additional_instructions/asic_overclock.html` | Whatsminer Overclocking: Manual Settings (40) | 54 | 158 | Whatsminer Overclocking on BiXBiT Firmware |
| 12 | `/ru/additional_instructions/asic_overclock.html` | Разгон Whatsminer: ручная настройка (35) | 49 | 147 | Разгон Whatsminer на прошивке BiXBiT |
| 13 | `/additional_instructions/configuring_dns.html` | Configure DNS for AMS on Antminer & Whatsminer (46) | 60 | 153 | — |
| 14 | `/ru/additional_instructions/configuring_dns.html` | Настройка DNS для подключения к AMS (35) | 49 | 147 | — |
| 15 | `/additional_instructions/factory_firmware_installation_and_rollback.html` | Antminer/Whatsminer Factory Firmware Rollback (45) | 59 | 156 | — |
| 16 | `/ru/additional_instructions/factory_firmware_installation_and_rollback.html` | Откат заводской прошивки Antminer и Whatsminer (46) | 60 | 143 | — |
| 17 | `/additional_instructions/log_export.html` | Export Logs from Antminer and Whatsminer (40) | 54 | 157 | — |
| 18 | `/ru/additional_instructions/log_export.html` | Экспорт логов Antminer и Whatsminer (35) | 49 | 146 | — |
| 19 | `/additional_instructions/preparation_for_immersion_cooling.html` | Prepare Whatsminer for Immersion Cooling (40) | 54 | 156 | Preparing a Whatsminer for Immersion Cooling |
| 20 | `/ru/additional_instructions/preparation_for_immersion_cooling.html` | Подготовка Whatsminer к иммерсии (32) | 46 | 152 | Подготовка Whatsminer к иммерсионному охлаждению |
| 21 | `/additional_instructions/sd-card_flashing.html` | Write Whatsminer Firmware to SD (PhoenixCard) (45) | 59 | 155 | Writing a Whatsminer Firmware Image to an SD Card |
| 22 | `/ru/additional_instructions/sd-card_flashing.html` | Запись прошивки Whatsminer на SD (PhoenixCard) (46) | 60 | 151 | Запись образа прошивки Whatsminer на SD-карту |
| 23 | `/additional_instructions/sd-card_formatting.html` | Format an SD Card to FAT32 for ASIC Firmware (44) | 58 | 158 | — |
| 24 | `/ru/additional_instructions/sd-card_formatting.html` | Форматирование SD-карты в FAT32 для прошивки (44) | 58 | 154 | — |
| 25 | `/additional_instructions/whatsminer_error_codes.html` | Whatsminer Error Codes: List and Fixes (38) | 52 | 155 | Whatsminer Error Codes: List of Errors and Fixes |
| 26 | `/ru/additional_instructions/whatsminer_error_codes.html` | Коды ошибок Whatsminer: список и решения (40) | 54 | 152 | Коды ошибок Whatsminer: список и способы устранения |
| 27 | `/ams/` | AMS Monitoring System Documentation (35) | 49 | 152 | AMS Monitoring System |
| 28 | `/ru/ams/` | AMS: система мониторинга ASIC (29) | 43 | 143 | AMS — система мониторинга |
| 29 | `/ams/connecting_a_device.html` | Connect Antminer & Whatsminer to AMS (36) | 50 | 159 | — |
| 30 | `/ru/ams/connecting_a_device.html` | Подключение Antminer и Whatsminer к AMS (39) | 53 | 147 | — |

Внутри группы A новые title не повторяются. Из дублей, которые есть сейчас, в группу попадает `Antminer | Documentation`: так же называется хаб `/functionality_of_the_bixbit_firmware/antminer/` (RU — `Antminer | Документация`). Новый title у `antminer.html` дубль снимает, хаб правит другой агент. У всех 30 страниц сейчас одинаковый `description` («Documentation» / «Документация»), и в `og:title` нет бренда.

---

## 2. По страницам

### 1. `/`

- **URL:** https://docs.bixbit.io/ · **файл:** `index.md` [VERIFY: путь в репозитории] · слов: 5
- **Сейчас:** title `Home | Documentation` · description `Documentation` · H1 `Home`
- **H1 → предлагаю:** BiXBiT Documentation
- **Итоговый `<title>`:** Antminer & Whatsminer Firmware Guides | BiXBiT Docs (51) · title 37 · description 153
- **Заметка:** Сейчас на странице 5 слов. Нужен короткий вводный абзац и ссылки на 4 раздела, иначе это тонкая страница.

```yaml
---
title: "Antminer & Whatsminer Firmware Guides"
description: "BiXBiT documentation for Antminer and Whatsminer: firmware install and update, overclocking, immersion prep, SD card flashing, error codes and AMS setup."
---
```

### 2. `/ru/`

- **URL:** https://docs.bixbit.io/ru/ · **файл:** `ru/index.md` [VERIFY: путь в репозитории] · слов: 7
- **Сейчас:** title `Главная | Документация` · description `Документация` · H1 `Главная`
- **H1 → предлагаю:** Документация BiXBiT
- **Итоговый `<title>`:** Документация по прошивкам ASIC и AMS | BiXBiT Docs (50) · title 36 · description 147
- **Заметка:** Сейчас 7 слов. То же: вводный абзац и ссылки на разделы.

```yaml
---
title: "Документация по прошивкам ASIC и AMS"
description: "Документация BiXBiT для Antminer и Whatsminer: установка и обновление прошивки, разгон, иммерсия, запись SD-карты, коды ошибок и подключение к AMS."
---
```

### 3. `/docs.html`

- **URL:** https://docs.bixbit.io/docs.html · **файл:** `docs.md` [VERIFY: путь в репозитории] · слов: 3176
- **Сейчас:** title `Docs | Documentation` · description `Documentation` · H1 `Docs`
- **H1:** оставить
- **Итоговый `<title>`:** PageCMS Editor Guide (Internal) | BiXBiT Docs (45) · title 31 · description 156
- **Заметка:** **Внутренняя инструкция для редакторов, открыта всем и есть в sitemap.** Текст русский и на EN-URL. Рекомендую `noindex` + убрать из sitemap (или закрыть страницу). В ней видна конфигурация `transformHead` сайта.

```yaml
---
title: "PageCMS Editor Guide (Internal)"
description: "Internal guide for docs.bixbit.io editors: PageCMS workflow, frontmatter, SEO fields, image ALT text, Vue components and VitePress Markdown syntax examples."
head:
  - - meta
    - name: robots
      content: "noindex, follow"
---
```

### 4. `/ru/docs.html`

- **URL:** https://docs.bixbit.io/ru/docs.html · **файл:** `ru/docs.md` [VERIFY: путь в репозитории] · слов: 3176
- **Сейчас:** title `Docs | Документация` · description `Документация` · H1 `Docs`
- **H1:** оставить
- **Итоговый `<title>`:** Редактирование документации в PageCMS | BiXBiT Docs (51) · title 37 · description 150
- **Заметка:** Полный дубль `/docs.html`. Рекомендую `noindex`, как и у EN.

```yaml
---
title: "Редактирование документации в PageCMS"
description: "Внутренняя инструкция для редакторов docs.bixbit.io: PageCMS, frontmatter, SEO-поля, ALT-тексты, компоненты Vue и примеры разметки VitePress Markdown."
head:
  - - meta
    - name: robots
      content: "noindex, follow"
---
```

### 5. `/installing_and_updating_bixbit_firmware/`

- **URL:** https://docs.bixbit.io/installing_and_updating_bixbit_firmware/ · **файл:** `installing_and_updating_bixbit_firmware/index.md` [VERIFY: путь в репозитории] · слов: 0
- **Сейчас:** title `Installing and Updating BiXBiT Firmware | Documentation` · description `Documentation` · H1 `нет`
- **H1 → предлагаю:** Installing and Updating BiXBiT Firmware
- **Итоговый `<title>`:** Install and Update BiXBiT Firmware | BiXBiT Docs (48) · title 34 · description 156
- **Заметка:** Хаб, 0 слов и нет H1. Нужен H1 и 2–3 предложения со ссылками на Antminer и Whatsminer.

```yaml
---
title: "Install and Update BiXBiT Firmware"
description: "How to install and update BiXBiT firmware on Antminer and Whatsminer ASIC miners: installer_tool.exe, WhatsMinerTool, PhoenixCard SD card and upgrade paths."
---
```

### 6. `/ru/installing_and_updating_bixbit_firmware/`

- **URL:** https://docs.bixbit.io/ru/installing_and_updating_bixbit_firmware/ · **файл:** `ru/installing_and_updating_bixbit_firmware/index.md` [VERIFY: путь в репозитории] · слов: 0
- **Сейчас:** title `Установка и обновление прошивки BiXBiT | Документация` · description `Документация` · H1 `нет`
- **H1 → предлагаю:** Установка и обновление прошивки BiXBiT
- **Итоговый `<title>`:** Установка и обновление прошивки BiXBiT | BiXBiT Docs (52) · title 38 · description 144
- **Заметка:** Хаб, 0 слов и нет H1. То же, что у EN.

```yaml
---
title: "Установка и обновление прошивки BiXBiT"
description: "Как установить и обновить прошивку BiXBiT на ASIC-майнеры Antminer и Whatsminer: installer_tool.exe, WhatsMinerTool, SD-карта через PhoenixCard."
---
```

### 7. `/installing_and_updating_bixbit_firmware/antminer.html`

- **URL:** https://docs.bixbit.io/installing_and_updating_bixbit_firmware/antminer.html · **файл:** `installing_and_updating_bixbit_firmware/antminer.md` [VERIFY: путь в репозитории] · слов: 1052
- **Сейчас:** title `Antminer | Documentation` · description `Documentation` · H1 `Installing and Updating BiXBiT Firmware on Antminer Devices`
- **H1:** оставить
- **Итоговый `<title>`:** Install & Update Antminer Firmware | BiXBiT Docs (48) · title 34 · description 156
- **Заметка:** Title сейчас `Antminer | Documentation`, одно слово. Формат совпадает с готовой страницей Whatsminer (`Install & Update Whatsminer Firmware`).

```yaml
---
title: "Install & Update Antminer Firmware"
description: "Install and update BiXBiT firmware on Antminer S19, S21, T21 and L7 with installer_tool.exe: compatible hashboards, known issues, IP scan and bulk flashing."
---
```

### 8. `/ru/installing_and_updating_bixbit_firmware/antminer.html`

- **URL:** https://docs.bixbit.io/ru/installing_and_updating_bixbit_firmware/antminer.html · **файл:** `ru/installing_and_updating_bixbit_firmware/antminer.md` [VERIFY: путь в репозитории] · слов: 904
- **Сейчас:** title `Antminer | Документация` · description `Документация` · H1 `Установка и обновление прошивки BiXBiT на устройствах Antminer`
- **H1:** оставить
- **Итоговый `<title>`:** Установка и обновление прошивки Antminer | BiXBiT Docs (54) · title 40 · description 160

```yaml
---
title: "Установка и обновление прошивки Antminer"
description: "Как установить и обновить прошивку BiXBiT на Antminer S19, S21, T21 и L7 через installer_tool.exe: совместимые хэш-платы, известные проблемы, массовая прошивка."
---
```

### 9. `/additional_instructions/`

- **URL:** https://docs.bixbit.io/additional_instructions/ · **файл:** `additional_instructions/index.md` [VERIFY: путь в репозитории] · слов: 0
- **Сейчас:** title `Additional Instructions | Documentation` · description `Documentation` · H1 `нет`
- **H1 → предлагаю:** Additional Instructions
- **Итоговый `<title>`:** Antminer & Whatsminer How-To Guides | BiXBiT Docs (49) · title 35 · description 156
- **Заметка:** Хаб, 0 слов и нет H1. Нужен H1 и список инструкций с одной строкой пояснения к каждой.

```yaml
---
title: "Antminer & Whatsminer How-To Guides"
description: "Extra guides for ASIC miners on BiXBiT firmware: overclocking, DNS for AMS, factory firmware rollback, log export, immersion prep, SD cards and error codes."
---
```

### 10. `/ru/additional_instructions/`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/ · **файл:** `ru/additional_instructions/index.md` [VERIFY: путь в репозитории] · слов: 0
- **Сейчас:** title `Дополнительные инструкции | Документация` · description `Документация` · H1 `нет`
- **H1 → предлагаю:** Дополнительные инструкции
- **Итоговый `<title>`:** Инструкции для Antminer и Whatsminer | BiXBiT Docs (50) · title 36 · description 153
- **Заметка:** Хаб, 0 слов и нет H1.

```yaml
---
title: "Инструкции для Antminer и Whatsminer"
description: "Дополнительные инструкции для ASIC на прошивке BiXBiT: разгон, DNS для AMS, откат заводской прошивки, логи, подготовка к иммерсии, SD-карты, коды ошибок."
---
```

### 11. `/additional_instructions/asic_overclock.html`

- **URL:** https://docs.bixbit.io/additional_instructions/asic_overclock.html · **файл:** `additional_instructions/asic_overclock.md` [VERIFY: путь в репозитории] · слов: 599
- **Сейчас:** title `ASIC Miner Overclocking and Other Related Functions | Documentation` · description `Documentation` · H1 `ASIC Miner Overclocking and Other Related Functions`
- **H1 → предлагаю:** Whatsminer Overclocking on BiXBiT Firmware
- **Итоговый `<title>`:** Whatsminer Overclocking: Manual Settings | BiXBiT Docs (54) · title 40 · description 158
- **Заметка:** H1 обещает любой ASIC, а на странице только Whatsminer. Bing показывает запросы `overclock firmware m32`, `overclock m30s+++ bixbit`.

```yaml
---
title: "Whatsminer Overclocking: Manual Settings"
description: "How to overclock a Whatsminer on BiXBiT firmware: autotune logic, PSU Power Limit, Target Voltage and Frequency, reference formulas and an M32 worked example."
---
```

### 12. `/ru/additional_instructions/asic_overclock.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/asic_overclock.html · **файл:** `ru/additional_instructions/asic_overclock.md` [VERIFY: путь в репозитории] · слов: 534
- **Сейчас:** title `Разгон ASIC-майнера и другие функции связанные с разгоном | Документация` · description `Документация` · H1 `Разгон ASIC-майнера и другие функции связанные с разгоном`
- **H1 → предлагаю:** Разгон Whatsminer на прошивке BiXBiT
- **Итоговый `<title>`:** Разгон Whatsminer: ручная настройка | BiXBiT Docs (49) · title 35 · description 147
- **Заметка:** В текущем H1 пропущена запятая («функции, связанные с разгоном»), и он тоже шире содержания.

```yaml
---
title: "Разгон Whatsminer: ручная настройка"
description: "Как разогнать Whatsminer на прошивке BiXBiT: логика автотюна, PSU Power Limit, Target Voltage и Target Frequency, формулы расчёта и пример для M32."
---
```

### 13. `/additional_instructions/configuring_dns.html`

- **URL:** https://docs.bixbit.io/additional_instructions/configuring_dns.html · **файл:** `additional_instructions/configuring_dns.md` [VERIFY: путь в репозитории] · слов: 111
- **Сейчас:** title `Configuring DNS | Documentation` · description `Documentation` · H1 `Configuring DNS in Case of Connection Issues with AMS`
- **H1:** оставить
- **Итоговый `<title>`:** Configure DNS for AMS on Antminer & Whatsminer | BiXBiT Docs (60) · title 46 · description 153

```yaml
---
title: "Configure DNS for AMS on Antminer & Whatsminer"
description: "Fix AMS connection issues by setting a custom DNS server on Antminer and Whatsminer with BiXBiT firmware: static IP required, DNS field and entry format."
---
```

### 14. `/ru/additional_instructions/configuring_dns.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/configuring_dns.html · **файл:** `ru/additional_instructions/configuring_dns.md` [VERIFY: путь в репозитории] · слов: 94
- **Сейчас:** title `Настройка DNS | Документация` · description `Документация` · H1 `Настройка DNS в случае проблем с подключением к AMS`
- **H1:** оставить
- **Итоговый `<title>`:** Настройка DNS для подключения к AMS | BiXBiT Docs (49) · title 35 · description 147

```yaml
---
title: "Настройка DNS для подключения к AMS"
description: "Как решить проблемы подключения к AMS: настройка DNS-сервера на Antminer и Whatsminer с прошивкой BiXBiT, статический IP, поле DNS и формат записи."
---
```

### 15. `/additional_instructions/factory_firmware_installation_and_rollback.html`

- **URL:** https://docs.bixbit.io/additional_instructions/factory_firmware_installation_and_rollback.html · **файл:** `additional_instructions/factory_firmware_installation_and_rollback.md` [VERIFY: путь в репозитории] · слов: 858
- **Сейчас:** title `Factory Firmware Installation and Rollback | Documentation` · description `Documentation` · H1 `Factory Firmware Installation and Rollback`
- **H1:** оставить
- **Итоговый `<title>`:** Antminer/Whatsminer Factory Firmware Rollback | BiXBiT Docs (59) · title 45 · description 156

```yaml
---
title: "Antminer/Whatsminer Factory Firmware Rollback"
description: "Roll back Antminer or Whatsminer to factory firmware before installing BiXBiT: SD or USB image by control board, WhatsMinerTool .bin or PhoenixCard SD card."
---
```

### 16. `/ru/additional_instructions/factory_firmware_installation_and_rollback.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/factory_firmware_installation_and_rollback.html · **файл:** `ru/additional_instructions/factory_firmware_installation_and_rollback.md` [VERIFY: путь в репозитории] · слов: 683
- **Сейчас:** title `Установка и откат заводской прошивки | Документация` · description `Документация` · H1 `Установка и откат заводской прошивки`
- **H1:** оставить
- **Итоговый `<title>`:** Откат заводской прошивки Antminer и Whatsminer | BiXBiT Docs (60) · title 46 · description 143

```yaml
---
title: "Откат заводской прошивки Antminer и Whatsminer"
description: "Как откатить Antminer или Whatsminer на заводскую прошивку перед установкой BiXBiT: образ на флешку по модели КПУ, WhatsMinerTool или SD-карта."
---
```

### 17. `/additional_instructions/log_export.html`

- **URL:** https://docs.bixbit.io/additional_instructions/log_export.html · **файл:** `additional_instructions/log_export.md` [VERIFY: путь в репозитории] · слов: 245
- **Сейчас:** title `Log Export | Documentation` · description `Documentation` · H1 `Log Export`
- **H1:** оставить
- **Итоговый `<title>`:** Export Logs from Antminer and Whatsminer | BiXBiT Docs (54) · title 40 · description 157
- **Заметка:** Bing: `bixbit log` (35 показов).

```yaml
---
title: "Export Logs from Antminer and Whatsminer"
description: "Export Antminer and Whatsminer logs for troubleshooting: download them from the BiXBiT firmware web interface or use WhatsMinerTool Remote Ctrl > Export Log."
---
```

### 18. `/ru/additional_instructions/log_export.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/log_export.html · **файл:** `ru/additional_instructions/log_export.md` [VERIFY: путь в репозитории] · слов: 197
- **Сейчас:** title `Экспорт логов | Документация` · description `Документация` · H1 `Экспорт логов`
- **H1:** оставить
- **Итоговый `<title>`:** Экспорт логов Antminer и Whatsminer | BiXBiT Docs (49) · title 35 · description 146

```yaml
---
title: "Экспорт логов Antminer и Whatsminer"
description: "Как выгрузить логи Antminer и Whatsminer для диагностики: через web-интерфейс прошивки BiXBiT или в WhatsMinerTool через Remote Ctrl > Export Log."
---
```

### 19. `/additional_instructions/preparation_for_immersion_cooling.html`

- **URL:** https://docs.bixbit.io/additional_instructions/preparation_for_immersion_cooling.html · **файл:** `additional_instructions/preparation_for_immersion_cooling.md` [VERIFY: путь в репозитории] · слов: 676
- **Сейчас:** title `Preparing an ASIC Miner for Immersion Cooling | Documentation` · description `Documentation` · H1 `Preparing for Immersion Cooling`
- **H1 → предлагаю:** Preparing a Whatsminer for Immersion Cooling
- **Итоговый `<title>`:** Prepare Whatsminer for Immersion Cooling | BiXBiT Docs (54) · title 40 · description 156
- **Заметка:** Текущий title обещает любой ASIC, а инструкция только для Whatsminer.

```yaml
---
title: "Prepare Whatsminer for Immersion Cooling"
description: "Prepare a Whatsminer for immersion cooling on BiXBiT firmware: remove fans, enable Liquid Cooling, disable PSU fan checks or flash the PSU with AirToLiquid."
---
```

### 20. `/ru/additional_instructions/preparation_for_immersion_cooling.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/preparation_for_immersion_cooling.html · **файл:** `ru/additional_instructions/preparation_for_immersion_cooling.md` [VERIFY: путь в репозитории] · слов: 599
- **Сейчас:** title `Подготовка ASIC-майнера к иммерсионному охлаждению | Документация` · description `Документация` · H1 `Подготовка к иммерсионному охлаждению`
- **H1 → предлагаю:** Подготовка Whatsminer к иммерсионному охлаждению
- **Итоговый `<title>`:** Подготовка Whatsminer к иммерсии | BiXBiT Docs (46) · title 32 · description 152

```yaml
---
title: "Подготовка Whatsminer к иммерсии"
description: "Как подготовить Whatsminer к иммерсионному охлаждению на прошивке BiXBiT: снять вентиляторы, включить Liquid Cooling, отключить проверку вентилятора БП."
---
```

### 21. `/additional_instructions/sd-card_flashing.html`

- **URL:** https://docs.bixbit.io/additional_instructions/sd-card_flashing.html · **файл:** `additional_instructions/sd-card_flashing.md` [VERIFY: путь в репозитории] · слов: 429
- **Сейчас:** title `Writing an image to the SD card | Documentation` · description `Documentation` · H1 `Writing an image to the SD card`
- **H1 → предлагаю:** Writing a Whatsminer Firmware Image to an SD Card
- **Итоговый `<title>`:** Write Whatsminer Firmware to SD (PhoenixCard) | BiXBiT Docs (59) · title 45 · description 155
- **Заметка:** H1 сейчас в sentence case и без сущности. Bing: `bixbit whatsminer firmware sd card after prefix`, `bixbit phoenixcard startup product`, `phoenixcard 4.2.2 download`, `how to install whatsminer firmware sd card`.

```yaml
---
title: "Write Whatsminer Firmware to SD (PhoenixCard)"
description: "Write a Whatsminer firmware .img to an SD card with PhoenixCard: select the drive, pick the image, keep Product mode, click Burn and check the burn result."
---
```

### 22. `/ru/additional_instructions/sd-card_flashing.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/sd-card_flashing.html · **файл:** `ru/additional_instructions/sd-card_flashing.md` [VERIFY: путь в репозитории] · слов: 415
- **Сейчас:** title `Запись образа прошивки на SD-карту | Документация` · description `Документация` · H1 `Запись образа прошивки на SD-карту`
- **H1 → предлагаю:** Запись образа прошивки Whatsminer на SD-карту
- **Итоговый `<title>`:** Запись прошивки Whatsminer на SD (PhoenixCard) | BiXBiT Docs (60) · title 46 · description 151
- **Заметка:** Bing: `whatsminer bixbit прошивка sd after префикс инструкция`.

```yaml
---
title: "Запись прошивки Whatsminer на SD (PhoenixCard)"
description: "Как записать образ прошивки Whatsminer (.img) на SD-карту в PhoenixCard: выбрать диск и образ, режим Product, нажать Burn и проверить результат записи."
---
```

### 23. `/additional_instructions/sd-card_formatting.html`

- **URL:** https://docs.bixbit.io/additional_instructions/sd-card_formatting.html · **файл:** `additional_instructions/sd-card_formatting.md` [VERIFY: путь в репозитории] · слов: 251
- **Сейчас:** title `SD Card Formatting | Documentation` · description `Documentation` · H1 `SD Card Formatting`
- **H1:** оставить
- **Итоговый `<title>`:** Format an SD Card to FAT32 for ASIC Firmware | BiXBiT Docs (58) · title 44 · description 158

```yaml
---
title: "Format an SD Card to FAT32 for ASIC Firmware"
description: "Fully format an SD card to FAT32 in Windows Disk Management before writing ASIC firmware: delete old volumes, create a new simple volume and check the result."
---
```

### 24. `/ru/additional_instructions/sd-card_formatting.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/sd-card_formatting.html · **файл:** `ru/additional_instructions/sd-card_formatting.md` [VERIFY: путь в репозитории] · слов: 430
- **Сейчас:** title `Полное форматирование SD-карты перед установкой прошивки | Документация` · description `Документация` · H1 `Полное форматирование SD-карты перед установкой прошивки`
- **H1:** оставить
- **Итоговый `<title>`:** Форматирование SD-карты в FAT32 для прошивки | BiXBiT Docs (58) · title 44 · description 154

```yaml
---
title: "Форматирование SD-карты в FAT32 для прошивки"
description: "Как полностью отформатировать SD-карту в FAT32 через «Управление дисками» перед записью прошивки ASIC: удалить тома, создать простой том, частые проблемы."
---
```

### 25. `/additional_instructions/whatsminer_error_codes.html`

- **URL:** https://docs.bixbit.io/additional_instructions/whatsminer_error_codes.html · **файл:** `additional_instructions/whatsminer_error_codes.md` [VERIFY: путь в репозитории] · слов: 2084
- **Сейчас:** title `Error codes for Whatsminer ASIC | Documentation` · description `Documentation` · H1 `Error codes for Whatsminer ASIC. List of errors and solutions`
- **H1 → предлагаю:** Whatsminer Error Codes: List of Errors and Fixes
- **Итоговый `<title>`:** Whatsminer Error Codes: List and Fixes | BiXBiT Docs (52) · title 38 · description 155
- **Заметка:** Главная страница группы по запросам. Bing: `whatsminer error codes` (149 показов, поз. ~4), `whatsminer error code list` (22), `whatsminer error code 541` (15). Та же таблица есть на bixbit.io (дубль 93–94%, решение — `content/localization-plan.md`).

```yaml
---
title: "Whatsminer Error Codes: List and Fixes"
description: "Whatsminer error codes 110 to 8410 with causes and fixes: fans, power supply, temperature sensors, EEPROM, hashboards, control board, pools and water flow."
---
```

### 26. `/ru/additional_instructions/whatsminer_error_codes.html`

- **URL:** https://docs.bixbit.io/ru/additional_instructions/whatsminer_error_codes.html · **файл:** `ru/additional_instructions/whatsminer_error_codes.md` [VERIFY: путь в репозитории] · слов: 1959
- **Сейчас:** title `Коды ошибок Whatsminer ASIC | Документация` · description `Документация` · H1 `Коды ошибок Whatsminer ASIC. Список ошибок и их решение`
- **H1 → предлагаю:** Коды ошибок Whatsminer: список и способы устранения
- **Итоговый `<title>`:** Коды ошибок Whatsminer: список и решения | BiXBiT Docs (54) · title 40 · description 152
- **Заметка:** Bing: `ошибки whatsminer` (9 показов, 6 кликов), `ошибки ватсмайнер` (6/6).

```yaml
---
title: "Коды ошибок Whatsminer: список и решения"
description: "Коды ошибок Whatsminer от 110 до 8410 с причинами и способами устранения: вентиляторы, блок питания, датчики температуры, EEPROM, хэш-платы, КПУ и пулы."
---
```

### 27. `/ams/`

- **URL:** https://docs.bixbit.io/ams/ · **файл:** `ams/index.md` [VERIFY: путь в репозитории] · слов: 0
- **Сейчас:** title `AMS - Monitoring System | Documentation` · description `Documentation` · H1 `нет`
- **H1 → предлагаю:** AMS Monitoring System
- **Итоговый `<title>`:** AMS Monitoring System Documentation | BiXBiT Docs (49) · title 35 · description 152
- **Заметка:** Хаб, 0 слов и нет H1. Bing: `bixbit ams` (146), `ams bixbit` (109) — брендовый спрос есть.

```yaml
---
title: "AMS Monitoring System Documentation"
description: "Documentation for AMS, the BiXBiT control and monitoring system for ASIC miners: connect Antminer and Whatsminer devices to a Workspace with an API key."
---
```

### 28. `/ru/ams/`

- **URL:** https://docs.bixbit.io/ru/ams/ · **файл:** `ru/ams/index.md` [VERIFY: путь в репозитории] · слов: 0
- **Сейчас:** title `AMS - система мониторинга | Документация` · description `Документация` · H1 `нет`
- **H1 → предлагаю:** AMS — система мониторинга
- **Итоговый `<title>`:** AMS: система мониторинга ASIC | BiXBiT Docs (43) · title 29 · description 143
- **Заметка:** Хаб, 0 слов и нет H1.

```yaml
---
title: "AMS: система мониторинга ASIC"
description: "Документация AMS — системы мониторинга и управления ASIC-майнерами от BiXBiT: как подключить Antminer и Whatsminer к пространству по API-ключу."
---
```

### 29. `/ams/connecting_a_device.html`

- **URL:** https://docs.bixbit.io/ams/connecting_a_device.html · **файл:** `ams/connecting_a_device.md` [VERIFY: путь в репозитории] · слов: 226
- **Сейчас:** title `Connecting Devices to AMS | Documentation` · description `Documentation` · H1 `Connecting an ASIC Miner to AMS`
- **H1:** оставить
- **Итоговый `<title>`:** Connect Antminer & Whatsminer to AMS | BiXBiT Docs (50) · title 36 · description 159
- **Заметка:** Bing: запрос, скопированный с экрана AMS-вкладки (`how to connect: https://bixbit.io login click add device copy api key…`, 35 показов) — люди ищут эту инструкцию.

```yaml
---
title: "Connect Antminer & Whatsminer to AMS"
description: "Connect Antminer and Whatsminer miners on BiXBiT firmware to AMS monitoring: create a Workspace, copy its API key, paste it into the AMS tab and click Install."
---
```

### 30. `/ru/ams/connecting_a_device.html`

- **URL:** https://docs.bixbit.io/ru/ams/connecting_a_device.html · **файл:** `ru/ams/connecting_a_device.md` [VERIFY: путь в репозитории] · слов: 179
- **Сейчас:** title `Подключение устройств к AMS | Документация` · description `Документация` · H1 `Подключение ASIC-майнера к AMS`
- **H1:** оставить
- **Итоговый `<title>`:** Подключение Antminer и Whatsminer к AMS | BiXBiT Docs (53) · title 39 · description 147

```yaml
---
title: "Подключение Antminer и Whatsminer к AMS"
description: "Как подключить Antminer и Whatsminer на прошивке BiXBiT к мониторингу AMS: создать пространство, скопировать API-ключ, вставить его во вкладку AMS."
---
```

---

## 3. Найденные ошибки в контенте

Только список, в контенте ничего не исправлено. P1 — инструкция расходится со скриншотом или сама себе противоречит, пользователь может сделать не тот шаг. P2 — неполнота, битые ссылки и расхождения EN и RU. P3 — опечатки и косметика.

| # | Приоритет | Страница | Что не так | Что сделать |
|---|---|---|---|---|
| 1 | P1 | `additional_instructions/log_export.html` (EN+RU) | Whatsminer, WhatsMinerTool: шаг 3 в тексте — «Select [Export Log]», а на скриншоте `/images/image-79.png` цифрой ③ отмечен **Mining Control**. | Переснять скриншот с отмеченным Export Log |
| 2 | P1 | `additional_instructions/asic_overclock.html` (EN+RU) | Рекомендации расходятся с примером M32. Правило: Min/Max Voltage в пределах ±50 от Target, а в примере ±100 (`1392 - 100 ~= 1300`, `1392 + 100 ~= 1500`; 1392 − 100 = 1292, 1392 + 100 = 1492). Правило: PSU Power Max выше PSU Power Limit минимум на 200 W, а в примере `3755 + 100 ~= 3850` (разница 95 W). Эти же значения на скриншоте `/images/image-74.png`. | [VERIFY: какое правило верно] — привести в соответствие правило, пример и скриншот |
| 3 | P1 | `additional_instructions/preparation_for_immersion_cooling.html` (EN+RU) | M3X/M5X/M6X: текст велит открыть вкладку «PSU Firmware», а на скриншоте `/images/image-41.png` вкладка называется **PSU Control**, PSU Firmware — только заголовок блока. Подсказка на `/images/image-40.png` тоже ведёт на вкладку «PSU Control». | Заменить на «PSU Control tab» / «вкладку PSU Control» |
| 4 | P2 | то же | На фото `/images/image-39.png` четыре маркера, а текст объясняет только ①–③. Маркер ④ (крупный план разъёма в БП) не описан. | [VERIFY: что показывает ④ — разъём вентилятора БП под заглушку?] и добавить пункт в список |
| 5 | P2 | то же | H3 — «…for M3X, M5X, M6X, and M7X Series», а в таблице методов только M3X, M5X, M6X. | [VERIFY: поддерживается ли M7X] — выровнять заголовок и таблицу |
| 6 | P2 | то же | Ссылка «Go to BiXBiT» за прошивками WhatsPower ведёт на `https://bixbit.tech/ru`: русская страница на другом домене, в том числе с EN-страницы. Скриншот меню `/images/image-43.png` тоже на русском. | [VERIFY: актуальный URL прошивок WhatsPower на bixbit.io/en] — поставить его на EN, скриншот переснять с EN-интерфейсом |
| 7 | P2 | `ams/connecting_a_device.html` (EN+RU) | Текст: «go to the "Workspace" tab» / «вкладку "Пространство"», а на скриншоте `/images/image-71.png` / `image-67.png` вкладки General и Notifications (Основное, Уведомления). | [VERIFY: как вкладка называется в текущем AMS] — поправить текст или скриншот |
| 8 | P2 | то же | Ссылка на регистрацию — `http://ams.bixbit.io`, без https. В EN ключ называется то «AMS Workspace key», то «AMS space key». Три раздела заканчиваются заглушкой «To be added with the release of AMS Hub». | https; одно название ключа; заглушки убрать или дописать |
| 9 | P2 | `installing_and_updating_bixbit_firmware/antminer.html` (EN+RU) | В конце таблицы совместимости три строки, где в колонке модели стоит код хэш-платы, а колонка плат пустая: «Antminer BHB42XXX —», «Antminer H6HB70701 —», «Antminer HHB68XXX —». | [VERIFY: что это за строки] — вписать модель или удалить |
| 10 | P3 | `ru/installing_and_updating_bixbit_firmware/antminer.html` | В тексте остался служебный маркер: «Выделите устройства с платами CVtek с помощью чекбоксов**[a]**» (похоже на метку комментария из Google Docs). Опечатка «стрес-тестирования» (надо «стресс-»). В шапке таблицы «хэшплат», в тексте «хэш-платы». | Удалить `[a]`, исправить опечатки |
| 11 | P3 | `installing_and_updating_bixbit_firmware/antminer.html` (EN+RU) | Скриншоты сняты с разных версий установщика: `image-8` — 0.9.9.4, «Using local files»; `image-12` — 0.9.9.3-stage38; в `image1` в списке версий 0.9.9.3. В окне Miner IP Management на `image-10` есть поля HTTP Port и SSH Port, текст их не описывает. | Переснять на одной версии; добавить в список полей HTTP Port / SSH Port |
| 12 | P2 | `additional_instructions/sd-card_flashing.html` (EN) | EN отстаёт от RU. Перед Step 5 пустой блок INFO: заголовок есть, текста нет. Нет INFO про PhoenixCard без подписей на кнопках (в RU есть). Нет двух скриншотов, которые есть в RU: процесс записи (`image-107`) и итог в Disk Management (`image-108`). Отсылка «Factory Firmware Installation and Rollback» в разделе Antminer — простой текст, в RU это ссылка. | Дотянуть EN до RU: INFO, 2 скриншота, ссылку |
| 13 | P2 | `additional_instructions/sd-card_formatting.html` (EN) | Нет раздела «Возможные проблемы и их решение» (в RU четыре подраздела: карта не видна, «Только для чтения», пустое поле файловой системы, RAW после форматирования). | Перевести раздел на EN |
| 14 | P2 | `additional_instructions/factory_firmware_installation_and_rollback.html` (EN+RU) | В разделе Whatsminer «via SD Card» шаги 2–3 (форматирование, PhoenixCard) описаны кратко, ссылок на подробные инструкции `sd-card_formatting.html` и `sd-card_flashing.html` нет. | Добавить две внутренние ссылки |
| 15 | P3 | то же (EN) | Step 1: скобка после «official website (in the "Firmware" section…» не закрыта. Имя файла в шаге 3 (`Whatsminer-all-20250915.16.bin`, в RU тоже) не совпадает с файлом на скриншоте `image-75` (`Whatsminer-M3x-all-20250321.14.bin`). | Закрыть скобку; пример имени привести к скриншоту или к актуальной версии |
| 16 | P3 | `ru/additional_instructions/asic_overclock.html` | «Autotune, которы длится» → «который»; «время автонастройки сократиться» → «сократится»; не отрисовался markdown `**1380 **` (пробел перед `**`). В H1 и title нет запятой: «функции, связанные с разгоном». | Исправить |
| 17 | P3 | `additional_instructions/asic_overclock.html` (EN) | В английском тексте десятичная запятая: `( 4,3 + 100)`, `4,3 / 5.0`, а в заголовке примера «BY 4.3%» — точка. | `4.3` везде |
| 18 | P3 | `additional_instructions/whatsminer_error_codes.html` (EN) | В кодах 120, 121, 130, 131 китайские полноширинные скобки: «Fanin speed error（Deviation 2000+）». Коды 5110–5112 стоят перед 5070–5072. На странице нет подзаголовков: около 110 кодов одной таблицей. | Обычные скобки; сортировка; H2 по группам кодов (вентиляторы, питание, температура, хэш-платы…) — удобнее и лучше для сниппетов |
| 19 | P3 | `ru/additional_instructions/whatsminer_error_codes.html` | Код 5070: в RU «Слишком быстрая скорость водного потока», в EN «water velocity is abnormal» (аномальная, не обязательно высокая). | [VERIFY: формулировка по документации MicroBT] |
| 20 | P3 | `ru/additional_instructions/sd-card_flashing.html` | «по окончанию процесса» → «по окончании»; «данные образа … присутствуют и находится» → «находятся». | Исправить |
| 21 | P3 | `ru/additional_instructions/sd-card_formatting.html` | В «[ОК]» кириллическая «О», рядом латинская «[OK]»; «Возможно включена физическая защита» — нужна запятая после «Возможно». | Исправить |
| 22 | P3 | `additional_instructions/log_export.html` (EN+RU) | В H3 «Using WhatsminerTool», в остальной документации «WhatsMinerTool». | Одно написание: WhatsMinerTool |
| 23 | P2 | `/docs.html`, `/ru/docs.html` | Внутренняя инструкция для редакторов (PageCMS, frontmatter, код `transformHead`) открыта, индексируется и есть в `sitemap.xml`. Обе версии на русском и одинаковые. Демо-ссылки битые: `/files/user-manual.pdf`, `/en/`, `/images/demo.gif` отдают 404, GIF с `media.giphy.com` тоже 404. У логотипа ALT «Логотип AMS», а на файле логотип BiXBiT. | `noindex` (frontmatter выше) и убрать из sitemap, либо закрыть авторизацией; исправить демо-ссылки |
| 24 | P2 | Хабы `/installing_and_updating_bixbit_firmware/`, `/additional_instructions/`, `/ams/` (EN+RU) | 6 пустых индексируемых страниц: 0 слов, нет H1, в sitemap есть. Главная: 5 и 7 слов, H1 «Home» / «Главная». | H1 (предложены выше) + 2–4 предложения и список дочерних страниц |
| 25 | P3 | EN-страницы, скриншоты | На EN видно русский интерфейс: `image-43` (меню сайта), `image-47` (окно «Открытие»), `image-50` (кнопка «Отмена»). На `image-107` / `image-113` в пути видна внутренняя папка сборки `…_antpoolsiteRU_AMS_249.7067_1.6.0.2_1psu` и пользователь `X99`. | При следующем обновлении переснять |

**Не ошибка, но для команды:** в инструкциях нет упоминаний dev fee и нет ссылок на bixbitusa.io, проверять там нечего. Технические значения в мете и ALT (модели, версии, IP, имена файлов) взяты только со страниц и скриншотов.

**Если меняется целевой URL или ключ:** `data/rank-tracking/keywords.md` не трогал. Если команда решит отслеживать `whatsminer error codes` по docs.bixbit.io (а не по bixbit.io), список надо обновить — ротацию утверждает человек.
