# Hreflang Tags — все страницы /en/*
**Источник:** data/site-structure.md (краул 2026-06-17)
**Статус сайта:** hreflang отсутствует на всех страницах (P0 из full-audit)
**Деплой:** добавить все три тега в `<head>` шаблон каждой страницы

> ⚠️ **[VERIFY] перед деплоем:**
> 1. Подтвердить, что каждая `/ru/*` страница **существует и индексируется** (не noindex).
>    Если `/ru/*` нет — убрать соответствующий hreflang="ru" тег.
> 2. Подтвердить `x-default` — `/en/` как дефолтная локаль (рекомендуется для B2B с
>    английским как основным языком экспансии).
> 3. Для `/en/ams/connect` — сначала решить вопрос noindex; если noindex, hreflang не нужен.

---

## Как читать этот файл

Каждый блок ниже — три строки для вставки в `<head>` конкретной страницы.
Все теги с пометкой `[VERIFY: /ru/... существует?]` требуют подтверждения ru-зеркала.

---

## Homepage

### /en
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru"> <!-- [VERIFY: /ru/ существует?] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en">
```

---

## Firmware

### /en/firmwares
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares">
```

### /en/firmwares/antminer
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer">
```

### /en/firmwares/whatsminer-all-series
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-all-series">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-all-series"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-all-series">
```

### /en/firmwares/whatsminer-series-m6x
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m6x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m6x"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m6x">
```

### /en/firmwares/whatsminer-series-m5x
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m5x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m5x"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m5x">
```

### /en/firmwares/whatsminer-series-m3x
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m3x"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">
```

### /en/firmwares/whatsminer-series-m2x
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m2x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m2x"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m2x">
```

### /en/firmwares/asic-s19
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-s19">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-s19"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-s19">
```

### /en/firmwares/asic-S17-S17Pro
> ⚠️ URL с заглавными буквами — после деплоя 301-редиректа на `/asic-s17-s17pro` обновить на lowercase.
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-s17-s17pro">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-s17-s17pro"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-s17-s17pro">
```

### /en/firmwares/asic-S17-plus
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-S17-plus">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-S17-plus"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-S17-plus">
```

### /en/firmwares/asic-T17-plus
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-T17-plus">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-T17-plus"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-T17-plus">
```

### /en/firmwares/asic-T17
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-T17">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-T17"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-T17">
```

### /en/firmwares/asic-T9-plus
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-T9-plus">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-T9-plus"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-T9-plus">
```

### /en/firmwares/asic-s9-s9j-s9i
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-s9-s9j-s9i">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-s9-s9j-s9i"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-s9-s9j-s9i">
```

---

## Cooling

### /en/asics-cooling
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/asics-cooling">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/asics-cooling"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/asics-cooling">
```

### /en/asics-cooling/hydro-systems
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/asics-cooling/hydro-systems">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/asics-cooling/hydro-systems"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/asics-cooling/hydro-systems">
```

### /en/asics-cooling/immersion-systems
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/asics-cooling/immersion-systems">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/asics-cooling/immersion-systems"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/asics-cooling/immersion-systems">
```

### /en/products
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products">
```

### /en/products/rack
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/rack">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/rack"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/rack">
```

### /en/products/rack-hydro
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/rack-hydro">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/rack-hydro"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/rack-hydro">
```

### /en/products/server
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/server">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/server"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/server">
```

### /en/products/container
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/container">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/container"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/container">
```

### /en/products/container-hydro
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/container-hydro">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/container-hydro"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/container-hydro">
```

### /en/products/container-1k
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/container-1k">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/container-1k"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/container-1k">
```

### /en/products/cell
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/cell">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/cell"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/cell">
```

### /en/products/coolant
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/coolant">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/coolant"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/coolant">
```

---

## Monitoring / AMS

### /en/ams
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/ams">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/ams"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/ams">
```

### /en/ams/connect
> ⚠️ Сначала решить: noindex или SEO landing page? Если noindex — hreflang не нужен.
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/ams/connect">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/ams/connect"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/ams/connect">
```

---

## About / Other

### /en/about
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/about">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/about"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/about">
```

### /en/contacts
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/contacts">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/contacts"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/contacts">
```

### /en/sustainability
```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/sustainability">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/sustainability"> <!-- [VERIFY] -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/sustainability">
```

---

## Шаблонная реализация (один фрагмент для всего сайта)

Если CMS поддерживает динамические переменные:

```html
<!-- Hreflang — вставить в <head> шаблон -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en{{ page_path }}">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru{{ page_path }}"> <!-- только если /ru{{ page_path }} существует -->
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en{{ page_path }}">
```

**Важно:** теги hreflang на странице /en/... и соответствующей /ru/... должны быть **идентичными зеркалами** друг друга — каждая ссылается на обе версии.
