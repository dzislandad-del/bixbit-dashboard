# docs.bixbit.io: «Installing and Updating BiXBiT Firmware on Whatsminer»: теги и ALT

**Дата:** 2026-09-29 · **Движок:** VitePress 2.0.0-alpha.17
**Страницы:**
- EN — https://docs.bixbit.io/installing_and_updating_bixbit_firmware/whatsminer.html
- RU — https://docs.bixbit.io/ru/installing_and_updating_bixbit_firmware/whatsminer.html

**Как проверено:** сырой HTML обеих страниц. Все 7 изображений скачаны и просмотрены, ALT написаны по содержимому скриншотов и тексту шага.

---

## 1. Что сейчас

| Элемент | EN | RU | Проблема |
|---|---|---|---|
| `<title>` | `Whatsminer \| Documentation` | `Whatsminer \| Документация` | Нет бренда и действия, одно слово; «Documentation» дописывается ко всем страницам |
| `description` | `Documentation` | `Документация` | Одинаковое на всём сайте документации, не описывает страницу |
| `og:title` / `og:description` | `Whatsminer` / нет | то же | Превью ссылки в мессенджерах и LLM-источниках пустое |
| H1 | Installing and Updating BiXBiT Firmware on Whatsminer Devices | Установка и обновление прошивки BiXBiT на устройствах Whatsminer | **Хорошо, оставить** |
| canonical | на себя | на себя | ОК |
| hreflang EN↔RU | нет | нет | Добавить пару (см. §4) |
| ALT у 7 изображений | `image.png` у всех | `image.png` у всех | Имя файла вместо описания |

---

## 2. Мета: готово к вставке (frontmatter VitePress)

### Вариант A (рекомендую): общий шаблон в `.vitepress/config`
Один раз на весь сайт, и суффикс «| Documentation» больше не съедает длину title:

```js
// .vitepress/config.(js|ts)
export default {
  titleTemplate: ':title | BiXBiT Docs',
  locales: {
    root: { lang: 'en-US', titleTemplate: ':title | BiXBiT Docs' },
    ru:   { lang: 'ru-RU', titleTemplate: ':title | BiXBiT Docs' }
  }
}
```

Затем в самих страницах.

**EN** — `installing_and_updating_bixbit_firmware/whatsminer.md`:
```yaml
---
title: "Install & Update Whatsminer Firmware"
description: "Step-by-step guide to installing and updating BiXBiT firmware on Whatsminer: WhatsMinerTool for H3, H6 and H6os boards, PhoenixCard SD card for H616."
head:
  - - meta
    - property: og:title
      content: "Install & Update BiXBiT Firmware on Whatsminer"
  - - meta
    - property: og:description
      content: "Step-by-step guide to installing and updating BiXBiT firmware on Whatsminer: WhatsMinerTool for H3, H6 and H6os boards, PhoenixCard SD card for H616."
---
```
Итоговый `<title>`: **Install & Update Whatsminer Firmware | BiXBiT Docs** (50 символов). Description — 149 символов.

**RU** — `ru/installing_and_updating_bixbit_firmware/whatsminer.md`:
```yaml
---
title: "Установка и обновление прошивки Whatsminer"
description: "Пошаговая инструкция: установка и обновление прошивки BiXBiT на Whatsminer через WhatsMinerTool (платы H3, H6, H6os) и SD-карту PhoenixCard (H616)."
head:
  - - meta
    - property: og:title
      content: "Установка и обновление прошивки BiXBiT на Whatsminer"
  - - meta
    - property: og:description
      content: "Пошаговая инструкция: установка и обновление прошивки BiXBiT на Whatsminer через WhatsMinerTool (платы H3, H6, H6os) и SD-карту PhoenixCard (H616)."
---
```
Итоговый `<title>`: **Установка и обновление прошивки Whatsminer | BiXBiT Docs** (56 символов). Description — 147 символов.

### Вариант B: без общего шаблона, только на этой странице
Добавить `titleTemplate: false` во frontmatter и полный title:
- EN — `Install & Update BiXBiT Firmware on Whatsminer` (46);
- RU — `Установка и обновление прошивки BiXBiT на Whatsminer` (52).

**Под какие запросы:** установка и обновление прошивки Whatsminer, WhatsMinerTool upgrade, плата H616 / SD-карта / PhoenixCard. В Bing сайт уже получает показы по `bixbit whatsminer firmware sd card`, `whatsminer phoenixcard firmware … sd card` и `can you flash a whatsminer with bixbit over the network`. GSC по `docs.bixbit.io` не подключён: наш ресурс в GSC — только `https://bixbit.io/`.

---

## 3. ALT: готово к вставке (markdown)

Картинки 3, 6 и 7 — это один и тот же скриншот в трёх файлах. ALT у них разный: он описывает шаг, для которого скриншот стоит на странице.

### EN
| # | Раздел | Файл | ALT (длина) |
|---|---|---|---|
| 1 | Проверка модели платы | `/images/image-127.png` | WhatsMinerTool Monitoring tab: Version Info shows the control board model (H616) and firmware date in yyyymmdd format (117) |
| 2 | Проверка модели платы | `/images/image-128.png` | Whatsminer web interface Status page: Hardware Info shows the control board model (H616), Firmware Version shows its date (121) |
| 3 | H3 / H6 / H6os | `/images/image-2.png` | WhatsMinerTool Upgrade for H3/H6/H6os boards: Select File, choose Whatsminer-ALL-Models .bin, tick the miner, Start Upgrade (123) |
| 4 | ≤ 1.7.X.X, этап 1 | `/images/image-3.png` | WhatsMinerTool Upgrade: selecting the intermediate file Whatsminer-ALL-Models_CustomCleanupBefore1.8_h616.bin, steps 1–6 (120) |
| 5 | ≤ 1.7.X.X, этап 1 | `/images/image-5.png` | WhatsMinerTool list: status Success and the CustomNeedUpgrade suffix in Version Info after the intermediate firmware (116) |
| 6 | ≤ 1.7.X.X, этап 2 | `/images/image-4.png` | WhatsMinerTool Upgrade, stage 2: selecting the main Whatsminer-ALL-Models .bin firmware file, steps 1–6 (103) |
| 7 | Поверх 1.8.0.X | `/images/image-6.png` | WhatsMinerTool Upgrade: updating BiXBiT firmware 1.8.0.x with the Whatsminer-ALL-Models .bin file, steps 1–6 (108) |

```md
![WhatsMinerTool Monitoring tab: Version Info shows the control board model (H616) and firmware date in yyyymmdd format](/images/image-127.png)
![Whatsminer web interface Status page: Hardware Info shows the control board model (H616), Firmware Version shows its date](/images/image-128.png)
![WhatsMinerTool Upgrade for H3/H6/H6os boards: Select File, choose Whatsminer-ALL-Models .bin, tick the miner, Start Upgrade](/images/image-2.png)
![WhatsMinerTool Upgrade: selecting the intermediate file Whatsminer-ALL-Models_CustomCleanupBefore1.8_h616.bin, steps 1–6](/images/image-3.png)
![WhatsMinerTool list: status Success and the CustomNeedUpgrade suffix in Version Info after the intermediate firmware](/images/image-5.png)
![WhatsMinerTool Upgrade, stage 2: selecting the main Whatsminer-ALL-Models .bin firmware file, steps 1–6](/images/image-4.png)
![WhatsMinerTool Upgrade: updating BiXBiT firmware 1.8.0.x with the Whatsminer-ALL-Models .bin file, steps 1–6](/images/image-6.png)
```

### RU
В RU-версии первые два скриншота свои, с подписями «Модель КПУ» и «ГГГГ ММ ДД», остальные общие с EN.

| # | Файл | ALT (длина) |
|---|---|---|
| 1 | `/images/image.png` | WhatsMinerTool, вкладка Monitoring: в Version Info видна модель платы управления (H616) и дата прошивки в формате ГГГГММДД (122) |
| 2 | `/images/image-1.png` | Веб-интерфейс Whatsminer, Status: в Hardware Info — модель платы управления (H616), в Firmware Version — дата прошивки (119) |
| 3 | `/images/image-2.png` | WhatsMinerTool, Upgrade для плат H3/H6/H6os: Select File, файл Whatsminer-ALL-Models .bin, отметить майнер, Start Upgrade (121) |
| 4 | `/images/image-3.png` | WhatsMinerTool, Upgrade: выбор промежуточного файла Whatsminer-ALL-Models_CustomCleanupBefore1.8_h616.bin, шаги 1–6 (115) |
| 5 | `/images/image-5.png` | WhatsMinerTool: статус Success и приписка CustomNeedUpgrade в Version Info после установки промежуточной прошивки (113) |
| 6 | `/images/image-4.png` | WhatsMinerTool, Upgrade, этап 2: выбор основного файла прошивки Whatsminer-ALL-Models .bin, шаги 1–6 (100) |
| 7 | `/images/image-6.png` | WhatsMinerTool, Upgrade: обновление прошивки BiXBiT 1.8.0.x файлом Whatsminer-ALL-Models .bin, шаги 1–6 (103) |

```md
![WhatsMinerTool, вкладка Monitoring: в Version Info видна модель платы управления (H616) и дата прошивки в формате ГГГГММДД](/images/image.png)
![Веб-интерфейс Whatsminer, Status: в Hardware Info — модель платы управления (H616), в Firmware Version — дата прошивки](/images/image-1.png)
![WhatsMinerTool, Upgrade для плат H3/H6/H6os: Select File, файл Whatsminer-ALL-Models .bin, отметить майнер, Start Upgrade](/images/image-2.png)
![WhatsMinerTool, Upgrade: выбор промежуточного файла Whatsminer-ALL-Models_CustomCleanupBefore1.8_h616.bin, шаги 1–6](/images/image-3.png)
![WhatsMinerTool: статус Success и приписка CustomNeedUpgrade в Version Info после установки промежуточной прошивки](/images/image-5.png)
![WhatsMinerTool, Upgrade, этап 2: выбор основного файла прошивки Whatsminer-ALL-Models .bin, шаги 1–6](/images/image-4.png)
![WhatsMinerTool, Upgrade: обновление прошивки BiXBiT 1.8.0.x файлом Whatsminer-ALL-Models .bin, шаги 1–6](/images/image-6.png)
```

---

## 4. Что ещё нашлось на странице

| # | Приоритет | Что | Сделать |
|---|---|---|---|
| 1 | **P1: ошибка в инструкции** | «Stage 1. Installing the Intermediate Firmware Version», шаг 3: текст велит выбрать `bixbit_before_1.8.bin`, а скриншот и абзац выше называют `Whatsminer-ALL-Models_CustomCleanupBefore1.8_h616.bin`. В RU то же самое | Исправить имя файла в шаге 3 на обеих версиях [VERIFY: какое имя сейчас в архиве прошивки] |
| 2 | P2 | hreflang между EN и RU не выводится | В VitePress: `head` с `link rel="alternate" hreflang="en" / "ru" / "x-default"` через `transformHead` в конфиге — для всех страниц |
| 3 | P2 | Для платы H616 (SD-карта, PhoenixCard) скриншотов нет, хотя это самый сложный путь | Добавить 2–3 скриншота PhoenixCard с ALT |
| 4 | P3 | На скриншотах 3/6/7 видна русская папка `D:\тесты 01.04` в EN-документации | При следующем обновлении снять скриншот заново |
| 5 | P3 | `robots.txt` на docs.bixbit.io отдаёт 404; sitemap есть (`/sitemap.xml`) | Добавить `robots.txt` со строкой `Sitemap: https://docs.bixbit.io/sitemap.xml` |
| 6 | — | Эта же инструкция есть и на bixbit.io: `/en/documentation/new-user-guide-for-whatsminer-asic/4-firmware-installation-and-update` | Решение команды по docs.bixbit.io (основной хост или дубль) — `content/localization-plan.md`. Теги и ALT нужны при любом решении |
