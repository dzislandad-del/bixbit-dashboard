# Canonical Tags — все страницы /en/*
**Источник:** data/site-structure.md (краул 2026-06-17, 32 страницы)
**Статус сайта:** canonical отсутствует на всех страницах (P0 из full-audit)
**Деплой:** добавить в `<head>` шаблон CMS/фреймворка — один тег на страницу

> ⚠️ **Примечание по /en/firmwares/asic-S17-S17Pro:** URL содержит заглавные буквы.
> Canonical указывает на предпочтительный lowercase-URL. Добавить 301-редирект
> с `/en/firmwares/asic-S17-S17Pro` → `/en/firmwares/asic-s17-s17pro` (P2 из full-audit).

---

## Firmware

| URL | Canonical tag |
|---|---|
| /en/firmwares | `<link rel="canonical" href="https://bixbit.io/en/firmwares">` |
| /en/firmwares/antminer | `<link rel="canonical" href="https://bixbit.io/en/firmwares/antminer">` |
| /en/firmwares/whatsminer-all-series | `<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-all-series">` |
| /en/firmwares/whatsminer-series-m6x | `<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m6x">` |
| /en/firmwares/whatsminer-series-m5x | `<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m5x">` |
| /en/firmwares/whatsminer-series-m3x | `<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">` |
| /en/firmwares/whatsminer-series-m2x | `<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m2x">` |
| /en/firmwares/asic-s19 | `<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-s19">` |
| /en/firmwares/asic-S17-S17Pro | `<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-s17-s17pro">` ⚠️ lowercase preferred |
| /en/firmwares/asic-S17-plus | `<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-S17-plus">` |
| /en/firmwares/asic-T17-plus | `<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-T17-plus">` |
| /en/firmwares/asic-T17 | `<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-T17">` |
| /en/firmwares/asic-T9-plus | `<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-T9-plus">` |
| /en/firmwares/asic-s9-s9j-s9i | `<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-s9-s9j-s9i">` |

## Cooling

| URL | Canonical tag |
|---|---|
| /en/asics-cooling | `<link rel="canonical" href="https://bixbit.io/en/asics-cooling">` |
| /en/asics-cooling/hydro-systems | `<link rel="canonical" href="https://bixbit.io/en/asics-cooling/hydro-systems">` |
| /en/asics-cooling/immersion-systems | `<link rel="canonical" href="https://bixbit.io/en/asics-cooling/immersion-systems">` |
| /en/products | `<link rel="canonical" href="https://bixbit.io/en/products">` |
| /en/products/rack | `<link rel="canonical" href="https://bixbit.io/en/products/rack">` |
| /en/products/rack-hydro | `<link rel="canonical" href="https://bixbit.io/en/products/rack-hydro">` |
| /en/products/server | `<link rel="canonical" href="https://bixbit.io/en/products/server">` |
| /en/products/container | `<link rel="canonical" href="https://bixbit.io/en/products/container">` |
| /en/products/container-hydro | `<link rel="canonical" href="https://bixbit.io/en/products/container-hydro">` |
| /en/products/container-1k | `<link rel="canonical" href="https://bixbit.io/en/products/container-1k">` |
| /en/products/cell | `<link rel="canonical" href="https://bixbit.io/en/products/cell">` |
| /en/products/coolant | `<link rel="canonical" href="https://bixbit.io/en/products/coolant">` |

## Monitoring / AMS

| URL | Canonical tag |
|---|---|
| /en/ams | `<link rel="canonical" href="https://bixbit.io/en/ams">` |
| /en/ams/connect | `<link rel="canonical" href="https://bixbit.io/en/ams/connect">` ⚠️ рассмотреть noindex |

## Homepage & Other

| URL | Canonical tag |
|---|---|
| /en | `<link rel="canonical" href="https://bixbit.io/en">` |
| /en/about | `<link rel="canonical" href="https://bixbit.io/en/about">` |
| /en/contacts | `<link rel="canonical" href="https://bixbit.io/en/contacts">` |
| /en/sustainability | `<link rel="canonical" href="https://bixbit.io/en/sustainability">` |

---

## Реализация в шаблоне (пример — один фрагмент на все страницы)

Если CMS поддерживает динамические URL, достаточно одного тега в `<head>`:

```html
<!-- Canonical — вставить в <head> шаблон, URL = текущий канонический путь страницы -->
<link rel="canonical" href="https://bixbit.io{{ canonical_path }}">
```

Где `{{ canonical_path }}` — переменная текущей страницы без UTM-параметров и trailing slash.
Для статических страниц — подставить URL из таблицы выше.
