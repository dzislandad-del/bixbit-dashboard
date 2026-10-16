# docs.bixbit.io, группа B: мета-теги (Basic configuration + Functionality of the BiXBiT firmware)

**Дата:** 2026-09-29 · **Движок:** VitePress 2.0.0-alpha.17 · **Страниц:** 26 (13 EN + 13 RU)
**Источник данных:** `data/docs-bixbit-io-inventory-2026-09-29/inventory.json` + сырой HTML всех 26 страниц (curl, 2026-09-29).
**ALT:** отдельно, `content/documentation/docs-bixbit-io/group-b-alt.csv` (96 строк, 47 уникальных скриншотов, все просмотрены).

## Как применять

1. Общий шаблон `titleTemplate: ':title | BiXBiT Docs'` (для `root` и `ru`) — как в образце `whatsminer-installing-updating.md`. Ниже `title` рассчитан под него: title ≤ 46, итоговый `<title>` ≤ 60.
2. Frontmatter вставляется в начало `.md`-файла страницы. Путь к файлу выведен из URL — `[VERIFY: путь в репозитории docs]`; хабы — `index.md` в папке.
3. **Все значения в кавычках.** В YAML строка без кавычек с «: » внутри (`Antminer Firmware: System Section`) ломает разбор frontmatter. Проверено: оба YAML-блока образца `whatsminer-installing-updating.md` не парсятся («mapping values are not allowed»), их тоже надо взять в кавычки. Все 26 блоков ниже проходят YAML-парсер.
4. Что было не так: все 26 страниц имеют `description` = «Documentation» / «Документация»; title без модели дублируются: «System Section» / «Раздел System» (Antminer и Whatsminer), «Settings Section», «Status Section», «Configuration Section», хабы «Antminer» / «Whatsminer» из одного слова.
5. Шаблон title: EN — «Antminer Firmware: <раздел>» / «Whatsminer Firmware: <раздел>», RU — «Прошивка Antminer: раздел <…>». Бренд BiXBiT приходит из суффикса `| BiXBiT Docs`, в og:title он есть явно. Все 26 title уникальны в пределах группы B и не совпадают с образцом (проверено скриптом); с группой A сверить при сборке.
6. H1: у 3 хабов (EN и RU) H1 нет вообще (страницы по 0 слов, только сайдбар) — нужен H1 и вводный текст со ссылками. «System Section» / «Раздел System» — дубль между моделями, исправить. Для остальных разделов — рекомендация добавить модель в H1 для единообразия (не обязательно).
7. Dev fee на этих страницах не упоминается; Hotel Fee — по тексту страниц это настраиваемые отчисления части хешрейта на указанный пул, а не комиссия прошивки; в мете не смешивать. В мету dev fee не вносили.

## Сводка

| # | Страница | EN title (длина) | RU title (длина) |
|---|---|---|---|
| 1 | Basic ASIC Miner Configuration | Basic ASIC Miner Setup: IP Address and Pools (44) | Базовая настройка ASIC: IP-адрес и пулы (39) |
| 2 | Хаб: Functionality | Additional Features of BiXBiT Firmware (38) | Дополнительный функционал прошивки BiXBiT (41) |
| 3 | Хаб: Antminer | BiXBiT Firmware for Antminer: Features (38) | Прошивка BiXBiT для Antminer: функции (37) |
| 4 | Antminer: Header | Antminer Firmware: Top Control Panel (36) | Прошивка Antminer: верхняя панель управления (44) |
| 5 | Antminer: Dashboard | Antminer Firmware: Dashboard Section (36) | Прошивка Antminer: раздел Dashboard (35) |
| 6 | Antminer: Settings | Antminer Firmware Settings: Autotune & Pools (44) | Прошивка Antminer: раздел Settings и автотюн (44) |
| 7 | Antminer: IP Settings | Antminer Firmware: IP Settings (DHCP/Static) (44) | Прошивка Antminer: раздел IP Settings (37) |
| 8 | Antminer: Logs | Antminer Firmware: Miner Log Section (36) | Прошивка Antminer: раздел Miner Log (35) |
| 9 | Antminer: System | Antminer Firmware: System Section (33) | Прошивка Antminer: раздел System (32) |
| 10 | Хаб: Whatsminer | BiXBiT Firmware for Whatsminer: Features (40) | Прошивка BiXBiT для Whatsminer: функции (39) |
| 11 | Whatsminer: Status | Whatsminer Firmware: Status Section (35) | Прошивка Whatsminer: раздел Status (34) |
| 12 | Whatsminer: Configuration | Whatsminer Firmware: Configuration Section (42) | Прошивка Whatsminer: раздел Configuration (41) |
| 13 | Whatsminer: System | Whatsminer Firmware: System Section (35) | Прошивка Whatsminer: раздел System (34) |

---

## Страницы

### 1. `/basic_asic_miner_configuration.html`

- EN: https://docs.bixbit.io/basic_asic_miner_configuration.html
- RU: https://docs.bixbit.io/ru/basic_asic_miner_configuration.html
- Слов: EN 1808 / RU 1484 · картинок: 17

| | EN | RU |
|---|---|---|
| title сейчас | `Basic ASIC Miner Configuration \| Documentation` | `Базовая настройка ASIC-майнера \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | Basic ASIC Miner Configuration | Базовая настройка ASIC-майнера |

H1: Хорошо, оставить.

**EN** — `basic_asic_miner_configuration.md`
```yaml
---
title: "Basic ASIC Miner Setup: IP Address and Pools"
description: "Connect an Antminer or Whatsminer, find its IP with WhatsMinerTool or IP Reporter, then set pools and workers in BTC Tools, WhatsMinerTool or the web UI."
head:
  - - meta
    - property: og:title
      content: "Basic ASIC Miner Setup: Find the IP Address and Configure Pools"
  - - meta
    - property: og:description
      content: "Connect an Antminer or Whatsminer, find its IP with WhatsMinerTool or IP Reporter, then set pools and workers in BTC Tools, WhatsMinerTool or the web UI."
---
```
Итоговый `<title>`: **Basic ASIC Miner Setup: IP Address and Pools | BiXBiT Docs** (58) · title 44 · description 153 · og:title 63

**RU** — `ru/basic_asic_miner_configuration.md`
```yaml
---
title: "Базовая настройка ASIC: IP-адрес и пулы"
description: "Подключение Antminer и Whatsminer: поиск IP-адреса в WhatsMinerTool или IP Reporter, настройка пулов и воркеров в BTC Tools, WhatsMinerTool и веб-интерфейсе."
head:
  - - meta
    - property: og:title
      content: "Базовая настройка ASIC-майнера: IP-адрес, пулы и воркеры"
  - - meta
    - property: og:description
      content: "Подключение Antminer и Whatsminer: поиск IP-адреса в WhatsMinerTool или IP Reporter, настройка пулов и воркеров в BTC Tools, WhatsMinerTool и веб-интерфейсе."
---
```
Итоговый `<title>`: **Базовая настройка ASIC: IP-адрес и пулы | BiXBiT Docs** (53) · title 39 · description 157 · og:title 56

### 2. `/functionality_of_the_bixbit_firmware/`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/
- Слов: EN 0 / RU 0 · картинок: 0

| | EN | RU |
|---|---|---|
| title сейчас | `Additional Features of BiXBiT Firmware \| Documentation` | `Дополнительный функционал прошивки BiXBiT \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | — (нет) | — (нет) |
| H1 → | Additional Features of BiXBiT Firmware | Дополнительный функционал прошивки BiXBiT |

H1: H1 нет, 0 слов: добавить H1, 2–3 предложения и список ссылок на Antminer / Whatsminer.

**EN** — `functionality_of_the_bixbit_firmware/index.md`
```yaml
---
title: "Additional Features of BiXBiT Firmware"
description: "Reference for the BiXBiT firmware web interface on Antminer and Whatsminer: dashboard, status, pools, autotune, profiles, network, logs and system settings."
head:
  - - meta
    - property: og:title
      content: "Additional Features of BiXBiT Firmware for Antminer and Whatsminer"
  - - meta
    - property: og:description
      content: "Reference for the BiXBiT firmware web interface on Antminer and Whatsminer: dashboard, status, pools, autotune, profiles, network, logs and system settings."
---
```
Итоговый `<title>`: **Additional Features of BiXBiT Firmware | BiXBiT Docs** (52) · title 38 · description 156 · og:title 66

**RU** — `ru/functionality_of_the_bixbit_firmware/index.md`
```yaml
---
title: "Дополнительный функционал прошивки BiXBiT"
description: "Справочник по веб-интерфейсу прошивки BiXBiT для Antminer и Whatsminer: дашборд, статус, пулы, автотюн, профили разгона, сеть, логи и системные настройки."
head:
  - - meta
    - property: og:title
      content: "Дополнительный функционал прошивки BiXBiT для Antminer и Whatsminer"
  - - meta
    - property: og:description
      content: "Справочник по веб-интерфейсу прошивки BiXBiT для Antminer и Whatsminer: дашборд, статус, пулы, автотюн, профили разгона, сеть, логи и системные настройки."
---
```
Итоговый `<title>`: **Дополнительный функционал прошивки BiXBiT | BiXBiT Docs** (55) · title 41 · description 154 · og:title 67

### 3. `/functionality_of_the_bixbit_firmware/antminer/`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/antminer/
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/antminer/
- Слов: EN 0 / RU 0 · картинок: 0

| | EN | RU |
|---|---|---|
| title сейчас | `Antminer \| Documentation` | `Antminer \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | — (нет) | — (нет) |
| H1 → | BiXBiT Firmware for Antminer: Web Interface | Прошивка BiXBiT для Antminer: веб-интерфейс |

H1: H1 нет, 0 слов: добавить H1, вводный абзац и ссылки на 6 разделов.

**EN** — `functionality_of_the_bixbit_firmware/antminer/index.md`
```yaml
---
title: "BiXBiT Firmware for Antminer: Features"
description: "Guide to the BiXBiT firmware web interface for Antminer: top control panel, Dashboard, Settings with autotune, IP Settings, Miner Log and System sections."
head:
  - - meta
    - property: og:title
      content: "BiXBiT Firmware for Antminer: Web Interface Features"
  - - meta
    - property: og:description
      content: "Guide to the BiXBiT firmware web interface for Antminer: top control panel, Dashboard, Settings with autotune, IP Settings, Miner Log and System sections."
---
```
Итоговый `<title>`: **BiXBiT Firmware for Antminer: Features | BiXBiT Docs** (52) · title 38 · description 154 · og:title 52

**RU** — `ru/functionality_of_the_bixbit_firmware/antminer/index.md`
```yaml
---
title: "Прошивка BiXBiT для Antminer: функции"
description: "Руководство по веб-интерфейсу прошивки BiXBiT для Antminer: верхняя панель управления, Dashboard, Settings с автотюном, IP Settings, Miner Log и System."
head:
  - - meta
    - property: og:title
      content: "Прошивка BiXBiT для Antminer: функции веб-интерфейса"
  - - meta
    - property: og:description
      content: "Руководство по веб-интерфейсу прошивки BiXBiT для Antminer: верхняя панель управления, Dashboard, Settings с автотюном, IP Settings, Miner Log и System."
---
```
Итоговый `<title>`: **Прошивка BiXBiT для Antminer: функции | BiXBiT Docs** (51) · title 37 · description 152 · og:title 52

### 4. `/functionality_of_the_bixbit_firmware/antminer/antminer_header.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/antminer/antminer_header.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/antminer/antminer_header.html
- Слов: EN 119 / RU 96 · картинок: 1

| | EN | RU |
|---|---|---|
| title сейчас | `Device Top Control Panel \| Documentation` | `Верхняя панель управления устройством \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | Device Top Control Panel | Верхняя панель управления устройством |
| H1 → | Antminer: Top Control Panel | Antminer: верхняя панель управления |

H1: Рекомендую добавить модель (единый шаблон «Модель: раздел»).

**EN** — `functionality_of_the_bixbit_firmware/antminer/antminer_header.md`
```yaml
---
title: "Antminer Firmware: Top Control Panel"
description: "Top panel of BiXBiT firmware for Antminer: device status, model, control board and PSU, Locate Miner, Stock FW rollback, factory reset, reboot and sleep."
head:
  - - meta
    - property: og:title
      content: "Top Control Panel of BiXBiT Firmware for Antminer"
  - - meta
    - property: og:description
      content: "Top panel of BiXBiT firmware for Antminer: device status, model, control board and PSU, Locate Miner, Stock FW rollback, factory reset, reboot and sleep."
---
```
Итоговый `<title>`: **Antminer Firmware: Top Control Panel | BiXBiT Docs** (50) · title 36 · description 153 · og:title 49

**RU** — `ru/functionality_of_the_bixbit_firmware/antminer/antminer_header.md`
```yaml
---
title: "Прошивка Antminer: верхняя панель управления"
description: "Верхняя панель прошивки BiXBiT для Antminer: статус и модель устройства, плата управления и БП, поиск майнера, откат на Stock FW, сброс, перезагрузка и сон."
head:
  - - meta
    - property: og:title
      content: "Верхняя панель управления прошивки BiXBiT для Antminer"
  - - meta
    - property: og:description
      content: "Верхняя панель прошивки BiXBiT для Antminer: статус и модель устройства, плата управления и БП, поиск майнера, откат на Stock FW, сброс, перезагрузка и сон."
---
```
Итоговый `<title>`: **Прошивка Antminer: верхняя панель управления | BiXBiT Docs** (58) · title 44 · description 156 · og:title 54

### 5. `/functionality_of_the_bixbit_firmware/antminer/antminer_dashboard.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/antminer/antminer_dashboard.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/antminer/antminer_dashboard.html
- Слов: EN 196 / RU 167 · картинок: 1

| | EN | RU |
|---|---|---|
| title сейчас | `Dashboard Section \| Documentation` | `Раздел Dashboard \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | Dashboard Section | Раздел Dashboard |
| H1 → | Antminer: Dashboard Section | Antminer: раздел Dashboard |

H1: Рекомендую добавить модель.

**EN** — `functionality_of_the_bixbit_firmware/antminer/antminer_dashboard.md`
```yaml
---
title: "Antminer Firmware: Dashboard Section"
description: "Antminer Dashboard in BiXBiT firmware: uptime, real-time and average hashrate, board and chip temps, power, efficiency, fan speed, per-board stats and pools."
head:
  - - meta
    - property: og:title
      content: "Dashboard Section of BiXBiT Firmware for Antminer"
  - - meta
    - property: og:description
      content: "Antminer Dashboard in BiXBiT firmware: uptime, real-time and average hashrate, board and chip temps, power, efficiency, fan speed, per-board stats and pools."
---
```
Итоговый `<title>`: **Antminer Firmware: Dashboard Section | BiXBiT Docs** (50) · title 36 · description 157 · og:title 49

**RU** — `ru/functionality_of_the_bixbit_firmware/antminer/antminer_dashboard.md`
```yaml
---
title: "Прошивка Antminer: раздел Dashboard"
description: "Раздел Dashboard прошивки BiXBiT для Antminer: аптайм, текущий и средний хешрейт, температуры плат и чипов, потребление, эффективность, вентиляторы и пулы."
head:
  - - meta
    - property: og:title
      content: "Раздел Dashboard прошивки BiXBiT для Antminer"
  - - meta
    - property: og:description
      content: "Раздел Dashboard прошивки BiXBiT для Antminer: аптайм, текущий и средний хешрейт, температуры плат и чипов, потребление, эффективность, вентиляторы и пулы."
---
```
Итоговый `<title>`: **Прошивка Antminer: раздел Dashboard | BiXBiT Docs** (49) · title 35 · description 155 · og:title 45

### 6. `/functionality_of_the_bixbit_firmware/antminer/antminer_settings.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/antminer/antminer_settings.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/antminer/antminer_settings.html
- Слов: EN 1192 / RU 1049 · картинок: 6

| | EN | RU |
|---|---|---|
| title сейчас | `Settings Section \| Documentation` | `Раздел Settings \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | Settings Section | Раздел Settings |
| H1 → | Antminer: Settings Section | Antminer: раздел Settings |

H1: Рекомендую добавить модель: «Settings Section» без модели.

**EN** — `functionality_of_the_bixbit_firmware/antminer/antminer_settings.md`
```yaml
---
title: "Antminer Firmware Settings: Autotune & Pools"
description: "Antminer Settings in BiXBiT firmware: operating mode, fan and temperature limits, pools, autotune, Profile Switcher, proxy and Hotel Fee tabs explained."
head:
  - - meta
    - property: og:title
      content: "Settings Section of BiXBiT Firmware for Antminer: Autotune and Pools"
  - - meta
    - property: og:description
      content: "Antminer Settings in BiXBiT firmware: operating mode, fan and temperature limits, pools, autotune, Profile Switcher, proxy and Hotel Fee tabs explained."
---
```
Итоговый `<title>`: **Antminer Firmware Settings: Autotune & Pools | BiXBiT Docs** (58) · title 44 · description 152 · og:title 68

**RU** — `ru/functionality_of_the_bixbit_firmware/antminer/antminer_settings.md`
```yaml
---
title: "Прошивка Antminer: раздел Settings и автотюн"
description: "Раздел Settings прошивки BiXBiT для Antminer: режим работы, вентиляторы и температурные лимиты, пулы, автотюн, Profile Switcher, прокси и Hotel Fee."
head:
  - - meta
    - property: og:title
      content: "Раздел Settings прошивки BiXBiT для Antminer: автотюн и пулы"
  - - meta
    - property: og:description
      content: "Раздел Settings прошивки BiXBiT для Antminer: режим работы, вентиляторы и температурные лимиты, пулы, автотюн, Profile Switcher, прокси и Hotel Fee."
---
```
Итоговый `<title>`: **Прошивка Antminer: раздел Settings и автотюн | BiXBiT Docs** (58) · title 44 · description 148 · og:title 60

### 7. `/functionality_of_the_bixbit_firmware/antminer/antminer_ip_settings.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/antminer/antminer_ip_settings.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/antminer/antminer_ip_settings.html
- Слов: EN 159 / RU 124 · картинок: 1

| | EN | RU |
|---|---|---|
| title сейчас | `IP Settings Section \| Documentation` | `Раздел IP Settings \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | IP Settings Section | Раздел IP Settings |
| H1 → | Antminer: IP Settings Section | Antminer: раздел IP Settings |

H1: Рекомендую добавить модель.

**EN** — `functionality_of_the_bixbit_firmware/antminer/antminer_ip_settings.md`
```yaml
---
title: "Antminer Firmware: IP Settings (DHCP/Static)"
description: "Set DHCP or a static IP on Antminer with BiXBiT firmware: hostname, protocol, IP address, subnet mask, gateway and DNS servers in the IP Settings section."
head:
  - - meta
    - property: og:title
      content: "IP Settings of BiXBiT Firmware for Antminer: DHCP and Static IP"
  - - meta
    - property: og:description
      content: "Set DHCP or a static IP on Antminer with BiXBiT firmware: hostname, protocol, IP address, subnet mask, gateway and DNS servers in the IP Settings section."
---
```
Итоговый `<title>`: **Antminer Firmware: IP Settings (DHCP/Static) | BiXBiT Docs** (58) · title 44 · description 154 · og:title 63

**RU** — `ru/functionality_of_the_bixbit_firmware/antminer/antminer_ip_settings.md`
```yaml
---
title: "Прошивка Antminer: раздел IP Settings"
description: "Как настроить DHCP или статический IP на Antminer с прошивкой BiXBiT: имя хоста, протокол, IP-адрес, маска подсети, шлюз и DNS-серверы в разделе IP Settings."
head:
  - - meta
    - property: og:title
      content: "IP Settings прошивки BiXBiT для Antminer: DHCP и статический IP"
  - - meta
    - property: og:description
      content: "Как настроить DHCP или статический IP на Antminer с прошивкой BiXBiT: имя хоста, протокол, IP-адрес, маска подсети, шлюз и DNS-серверы в разделе IP Settings."
---
```
Итоговый `<title>`: **Прошивка Antminer: раздел IP Settings | BiXBiT Docs** (51) · title 37 · description 157 · og:title 63

### 8. `/functionality_of_the_bixbit_firmware/antminer/antminer_logs.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/antminer/antminer_logs.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/antminer/antminer_logs.html
- Слов: EN 27 / RU 25 · картинок: 0

| | EN | RU |
|---|---|---|
| title сейчас | `Miner Log Section \| Documentation` | `Раздел Miner Log \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | Miner Log Section | Раздел Miner Log |
| H1 → | Antminer: Miner Log Section | Antminer: раздел Miner Log |

H1: Рекомендую добавить модель.

**EN** — `functionality_of_the_bixbit_firmware/antminer/antminer_logs.md`
```yaml
---
title: "Antminer Firmware: Miner Log Section"
description: "Miner Log section of BiXBiT firmware for Antminer: view device logs since the last boot on the Current tab, or download full logs for selected dates."
head:
  - - meta
    - property: og:title
      content: "Miner Log Section of BiXBiT Firmware for Antminer"
  - - meta
    - property: og:description
      content: "Miner Log section of BiXBiT firmware for Antminer: view device logs since the last boot on the Current tab, or download full logs for selected dates."
---
```
Итоговый `<title>`: **Antminer Firmware: Miner Log Section | BiXBiT Docs** (50) · title 36 · description 149 · og:title 49

**RU** — `ru/functionality_of_the_bixbit_firmware/antminer/antminer_logs.md`
```yaml
---
title: "Прошивка Antminer: раздел Miner Log"
description: "Раздел Miner Log прошивки BiXBiT для Antminer: просмотр логов устройства с момента загрузки на вкладке Current и скачивание полных логов за нужные даты."
head:
  - - meta
    - property: og:title
      content: "Раздел Miner Log прошивки BiXBiT для Antminer"
  - - meta
    - property: og:description
      content: "Раздел Miner Log прошивки BiXBiT для Antminer: просмотр логов устройства с момента загрузки на вкладке Current и скачивание полных логов за нужные даты."
---
```
Итоговый `<title>`: **Прошивка Antminer: раздел Miner Log | BiXBiT Docs** (49) · title 35 · description 152 · og:title 45

### 9. `/functionality_of_the_bixbit_firmware/antminer/antminer_system.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/antminer/antminer_system.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/antminer/antminer_system.html
- Слов: EN 88 / RU 75 · картинок: 0

| | EN | RU |
|---|---|---|
| title сейчас | `System Section \| Documentation` | `Раздел System \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | System Section | Раздел System |
| H1 → | Antminer: System Section | Antminer: раздел System |

H1: **Исправить**: дубль H1 с Whatsminer System.

**EN** — `functionality_of_the_bixbit_firmware/antminer/antminer_system.md`
```yaml
---
title: "Antminer Firmware: System Section"
description: "System section of BiXBiT firmware for Antminer: change the web interface password or install stock firmware from a BMU file, with an option to clear logs."
head:
  - - meta
    - property: og:title
      content: "System Section of BiXBiT Firmware for Antminer"
  - - meta
    - property: og:description
      content: "System section of BiXBiT firmware for Antminer: change the web interface password or install stock firmware from a BMU file, with an option to clear logs."
---
```
Итоговый `<title>`: **Antminer Firmware: System Section | BiXBiT Docs** (47) · title 33 · description 154 · og:title 46

**RU** — `ru/functionality_of_the_bixbit_firmware/antminer/antminer_system.md`
```yaml
---
title: "Прошивка Antminer: раздел System"
description: "Раздел System прошивки BiXBiT для Antminer: смена пароля веб-интерфейса и установка заводской прошивки из bmu-файла с очисткой логов (чекбокс Clear logs)."
head:
  - - meta
    - property: og:title
      content: "Раздел System прошивки BiXBiT для Antminer"
  - - meta
    - property: og:description
      content: "Раздел System прошивки BiXBiT для Antminer: смена пароля веб-интерфейса и установка заводской прошивки из bmu-файла с очисткой логов (чекбокс Clear logs)."
---
```
Итоговый `<title>`: **Прошивка Antminer: раздел System | BiXBiT Docs** (46) · title 32 · description 154 · og:title 42

### 10. `/functionality_of_the_bixbit_firmware/whatsminer/`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/whatsminer/
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/whatsminer/
- Слов: EN 0 / RU 0 · картинок: 0

| | EN | RU |
|---|---|---|
| title сейчас | `Whatsminer \| Documentation` | `Whatsminer \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | — (нет) | — (нет) |
| H1 → | BiXBiT Firmware for Whatsminer: Web Interface | Прошивка BiXBiT для Whatsminer: веб-интерфейс |

H1: H1 нет, 0 слов: добавить H1, вводный абзац и ссылки на 3 раздела.

**EN** — `functionality_of_the_bixbit_firmware/whatsminer/index.md`
```yaml
---
title: "BiXBiT Firmware for Whatsminer: Features"
description: "Guide to the BiXBiT firmware web interface for Whatsminer: Status with logs and hardware overview, Configuration with pools and overclocking, and System."
head:
  - - meta
    - property: og:title
      content: "BiXBiT Firmware for Whatsminer: Web Interface Features"
  - - meta
    - property: og:description
      content: "Guide to the BiXBiT firmware web interface for Whatsminer: Status with logs and hardware overview, Configuration with pools and overclocking, and System."
---
```
Итоговый `<title>`: **BiXBiT Firmware for Whatsminer: Features | BiXBiT Docs** (54) · title 40 · description 153 · og:title 54

**RU** — `ru/functionality_of_the_bixbit_firmware/whatsminer/index.md`
```yaml
---
title: "Прошивка BiXBiT для Whatsminer: функции"
description: "Руководство по веб-интерфейсу прошивки BiXBiT для Whatsminer: Status с логами и обзором системы, Configuration с пулами и разгоном, а также раздел System."
head:
  - - meta
    - property: og:title
      content: "Прошивка BiXBiT для Whatsminer: функции веб-интерфейса"
  - - meta
    - property: og:description
      content: "Руководство по веб-интерфейсу прошивки BiXBiT для Whatsminer: Status с логами и обзором системы, Configuration с пулами и разгоном, а также раздел System."
---
```
Итоговый `<title>`: **Прошивка BiXBiT для Whatsminer: функции | BiXBiT Docs** (53) · title 39 · description 154 · og:title 54

### 11. `/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_status.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_status.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_status.html
- Слов: EN 205 / RU 179 · картинок: 10

| | EN | RU |
|---|---|---|
| title сейчас | `Status Section \| Documentation` | `Раздел Status \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | Status Section | Раздел Status |
| H1 → | Whatsminer: Status Section | Whatsminer: раздел Status |

H1: Рекомендую добавить модель: «Status Section» без модели.

**EN** — `functionality_of_the_bixbit_firmware/whatsminer/whatsminer_status.md`
```yaml
---
title: "Whatsminer Firmware: Status Section"
description: "Whatsminer Status in BiXBiT firmware: miner summary, hashboards, pools, errors and events, API, system and miner logs, processes, memory and network overview."
head:
  - - meta
    - property: og:title
      content: "Status Section of BiXBiT Firmware for Whatsminer"
  - - meta
    - property: og:description
      content: "Whatsminer Status in BiXBiT firmware: miner summary, hashboards, pools, errors and events, API, system and miner logs, processes, memory and network overview."
---
```
Итоговый `<title>`: **Whatsminer Firmware: Status Section | BiXBiT Docs** (49) · title 35 · description 158 · og:title 48

**RU** — `ru/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_status.md`
```yaml
---
title: "Прошивка Whatsminer: раздел Status"
description: "Раздел Status прошивки BiXBiT для Whatsminer: сводка, хешплаты, пулы, ошибки и события, логи Miner API, System и Miner, процессы, память и сеть устройства."
head:
  - - meta
    - property: og:title
      content: "Раздел Status прошивки BiXBiT для Whatsminer"
  - - meta
    - property: og:description
      content: "Раздел Status прошивки BiXBiT для Whatsminer: сводка, хешплаты, пулы, ошибки и события, логи Miner API, System и Miner, процессы, память и сеть устройства."
---
```
Итоговый `<title>`: **Прошивка Whatsminer: раздел Status | BiXBiT Docs** (48) · title 34 · description 155 · og:title 44

### 12. `/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_configuration.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_configuration.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_configuration.html
- Слов: EN 2015 / RU 1686 · картинок: 12

| | EN | RU |
|---|---|---|
| title сейчас | `Configuration Section \| Documentation` | `Раздел Configuration \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | Configuration Section | Раздел Configuration |
| H1 → | Whatsminer: Configuration Section | Whatsminer: раздел Configuration |

H1: Рекомендую добавить модель.

**EN** — `functionality_of_the_bixbit_firmware/whatsminer/whatsminer_configuration.md`
```yaml
---
title: "Whatsminer Firmware: Configuration Section"
description: "Whatsminer Configuration in BiXBiT firmware: network, pools, overclock profiles, Profile Switcher, Hotel Fee, PSU control, boards, temp limits and proxy."
head:
  - - meta
    - property: og:title
      content: "Configuration Section of BiXBiT Firmware for Whatsminer"
  - - meta
    - property: og:description
      content: "Whatsminer Configuration in BiXBiT firmware: network, pools, overclock profiles, Profile Switcher, Hotel Fee, PSU control, boards, temp limits and proxy."
---
```
Итоговый `<title>`: **Whatsminer Firmware: Configuration Section | BiXBiT Docs** (56) · title 42 · description 153 · og:title 55

**RU** — `ru/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_configuration.md`
```yaml
---
title: "Прошивка Whatsminer: раздел Configuration"
description: "Раздел Configuration прошивки BiXBiT для Whatsminer: сеть, пулы, профили разгона, Profile Switcher, Hotel Fee, управление БП, платы, температуры и прокси."
head:
  - - meta
    - property: og:title
      content: "Раздел Configuration прошивки BiXBiT для Whatsminer"
  - - meta
    - property: og:description
      content: "Раздел Configuration прошивки BiXBiT для Whatsminer: сеть, пулы, профили разгона, Profile Switcher, Hotel Fee, управление БП, платы, температуры и прокси."
---
```
Итоговый `<title>`: **Прошивка Whatsminer: раздел Configuration | BiXBiT Docs** (55) · title 41 · description 154 · og:title 51

### 13. `/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_system.html`

- EN: https://docs.bixbit.io/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_system.html
- RU: https://docs.bixbit.io/ru/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_system.html
- Слов: EN 58 / RU 53 · картинок: 0

| | EN | RU |
|---|---|---|
| title сейчас | `System Section \| Documentation` | `Раздел System \| Документация` |
| description сейчас | `Documentation` | `Документация` |
| H1 сейчас | System Section | Раздел System |
| H1 → | Whatsminer: System Section | Whatsminer: раздел System |

H1: **Исправить**: дубль H1 с Antminer System.

**EN** — `functionality_of_the_bixbit_firmware/whatsminer/whatsminer_system.md`
```yaml
---
title: "Whatsminer Firmware: System Section"
description: "System section of BiXBiT firmware for Whatsminer: set the device time, time zone and NTP servers, change the account password, and reboot the miner."
head:
  - - meta
    - property: og:title
      content: "System Section of BiXBiT Firmware for Whatsminer"
  - - meta
    - property: og:description
      content: "System section of BiXBiT firmware for Whatsminer: set the device time, time zone and NTP servers, change the account password, and reboot the miner."
---
```
Итоговый `<title>`: **Whatsminer Firmware: System Section | BiXBiT Docs** (49) · title 35 · description 148 · og:title 48

**RU** — `ru/functionality_of_the_bixbit_firmware/whatsminer/whatsminer_system.md`
```yaml
---
title: "Прошивка Whatsminer: раздел System"
description: "Раздел System прошивки BiXBiT для Whatsminer: настройка времени, часового пояса и NTP-серверов, смена пароля учетной записи и перезагрузка устройства."
head:
  - - meta
    - property: og:title
      content: "Раздел System прошивки BiXBiT для Whatsminer"
  - - meta
    - property: og:description
      content: "Раздел System прошивки BiXBiT для Whatsminer: настройка времени, часового пояса и NTP-серверов, смена пароля учетной записи и перезагрузка устройства."
---
```
Итоговый `<title>`: **Прошивка Whatsminer: раздел System | BiXBiT Docs** (48) · title 34 · description 150 · og:title 44

---

## Найденные ошибки в контенте

Только список. «EN+RU» — ошибка в обеих версиях. Номера ①–④ — маркеры на скриншотах.

### Basic ASIC Miner Configuration (`/basic_asic_miner_configuration.html`)
1. EN+RU, «Configuration via WhatsminerTool», шаг 4: в тексте кнопка **[Start Upgrade]**, на скриншоте `image-23.png` — **Start Update**.
2. EN+RU, «Configuration via the Device's WEB Interface»: в тексте путь «Configuration > Miner Configuration», на скриншоте `image-24.png` пункт меню **CGMiner Configuration**. Маркер ④ (Save & Apply) в тексте не упомянут.
3. EN+RU: адрес веб-интерфейса Whatsminer дан как `https://192.168.88.96` `[VERIFY: http или https]`.
4. EN: на фото платы Antminer S19 (`image-21.png`) подписи на русском («Порт для прошивки», «Кнопка Reset», «Красный LED»…) — нужна EN-версия скриншота.
5. EN+RU: текст «Click the [Start] button ①» — на скриншоте IP Reporter (`image-20.png`) маркера ① нет.
6. EN+RU: на скриншоте BTC Tools (`image-25.png`) маркеры ①②③, в тексте они не используются.
7. EN+RU: скриншот заводской прошивки Antminer S21 Pro (`image-29.png`) — с чужим водяным знаком; снять свой.
8. EN: H4 «Configuration via **WhatsminerTool**» — в остальном тексте WhatsMinerTool. RU: H4 «Настройка с помощью **WhatminerTool**» — опечатка.
9. RU: «в двух **впадающих** списках» → «выпадающих».
10. RU: артефакт разметки `②****`, `③****` (поля Start IP, End IP, Pool 1).
11. RU: логин/пароль `root\root` → «root/root» (в EN — root/root).
12. RU: «производ**и**ться» → «производится»; «в соответствующ**ее** поля» → «в соответствующие поля»; «Так же через несколько секунд» → «Также».

### Antminer: Device Top Control Panel (`antminer_header.html`)
13. EN+RU: в тексте функция «Find Device» / «Найти устройство», в интерфейсе (`image-33.png`, маркер 5) — переключатель **Locate miner**.
14. RU: «Restore Factory **Setings**» → «Settings»; «позволяет **выполнять просмотреть**» → «позволяет просматривать».

### Antminer: Settings (`antminer_settings.html`)
15. EN+RU: в тексте «Max delay **on** starting mining», в интерфейсе (`image-35.png`, 5) — «Max delay **before** starting mining (seconds)»; единица измерения (секунды) в тексте не указана.
16. EN+RU: подпись в интерфейсе прошивки «**Rise** profile if temp below» (`setting-profile-switcher-marked.png`) — ошибка в UI («Raise»), текст её повторяет. Передать команде прошивки.
17. RU: «before **emegency** mode» → «emergency».
18. RU: «Функция полезна используется чтобы…» → «Функция полезна, чтобы…»; «на **все** ферме» → «на всей ферме».
19. RU: «произойдет **перезагрузке**» → «перезагрузка»; «температура с сенсоров… **продолжают**» → «температуры… продолжают».
20. RU (Autotune): «Startup voltage… **она** может быть **изменено**» → «оно может быть изменено».
21. RU (Hotel Fee): «в этой **вкладе**» → «вкладке»; «на представленном ниже **скришоте**» → «скриншоте».
22. RU (Proxy): «имя учетной **запись**» → «записи».

### Antminer: System (`antminer_system.html`)
23. RU: «**Passwrod**» → «Password».

### Whatsminer: Configuration (`whatsminer_configuration.html`)
24. EN+RU (Advanced Options): «not to be confused with the board temperature, which is displayed in the web interface in the **ChipTemp** column» — противоречие: ChipTemp — это как раз температура чипов (см. `image-59.png`: отдельные колонки HashBoardTemp и ChipTemp) `[VERIFY: как называется колонка температуры плат в веб-интерфейсе]`.
25. EN+RU (PSU Control): ссылка «More details can be found here» / «Подробнее написано здесь» ведёт на старый хост `bixbit-dev.github.io/bixbit.docs/ru/…`, причём с EN-страницы — на русскую версию. Заменить на внутреннюю ссылку docs.bixbit.io.
26. EN+RU (PSU Control): на скриншоте (`image-62.png`) предупреждение прошивки «Warning! Returning to air-cooled mode will be impossible» после прошивки БП — в тексте этого предупреждения нет. Важно добавить `[VERIFY]`.
27. EN+RU (Env Temp Limits): на скриншоте есть чекбокс **Enabled**, в тексте не описан.
28. EN+RU: скриншоты сняты на разных версиях — в `image-61.png` нет вкладок Env Temp Limits и Cool Temp, в `image-62.png` нет Cool Temp. Для консистентности переснять.
29. EN: «The Restart As Hashrate Error **error** occurs…» — повтор слова.
30. RU: «в **этой** же поле» → «в этом же поле»; «В **большистве** случаев **рекоменудется**» → «В большинстве случаев рекомендуется».
31. RU: «имя **вокера**» → «воркера»; «в этой **вкладе**» → «вкладке»; «**по** время запуска» → «во время».
32. RU: «**Не смотря** на то» → «Несмотря на то»; «во **избежании**» → «во избежание»; «**не штатными** кулерами» → «нештатными».
33. RU: «отключает **использования** мощности» → «использование»; «температуру окружающей среды при **котором**» → «при которой»; «управления работой **устройством**» → «устройства»; «имя учетной **запись**» → «записи».

### Whatsminer: Status (`whatsminer_status.html`)
34. EN+RU: подразделы Summary, Devices, Pools, Errors, Events и Overview (System / Memory / Network) — только скриншоты, ни одного предложения текста. Добавить по 1–2 предложения: что показывает таблица и когда на неё смотреть.

### Хабы и короткие страницы
35. EN+RU: хабы `/functionality_of_the_bixbit_firmware/`, `…/antminer/`, `…/whatsminer/` — пустые (0 слов, нет H1), в индексе это тонкие страницы.
36. EN+RU: `antminer_logs.html` (27 / 25 слов) и `antminer_system.html`, `whatsminer_system.html` (88 / 58 слов) — без скриншотов и почти без текста.

### Приватность на скриншотах (низкий приоритет)
37. Видны MAC-адрес (`fda74569…png`, `7612826c…png`), серийный номер БП (`image-62.png`), серийный номер платы (`image-21.png`) и имя воркера «Valun» (`skrinshot-…-151454.png`). Размыть при следующем обновлении.
