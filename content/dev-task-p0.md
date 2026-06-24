# Developer Task: SEO P0 Fixes — bixbit.io/en
**Дата:** 2026-06-17
**Приоритет:** P0 — критично, деплой на этой неделе
**Источники:** full-audit-2026-06-17.md, page-optimize/firmwares-antminer.md, seo-fixes/*

---

## 1. Контекст и ожидаемый эффект

Технический SEO-аудит выявил пять критических отсутствий на всех страницах `/en/*`:

| Проблема | Страниц затронуто | Текущий эффект |
|---|---|---|
| Нет `<meta name="description">` | 32 из 32 | Google генерирует сниппеты из случайного текста → низкий CTR |
| Нет `<link rel="canonical">` | 32 из 32 | UTM-варианты и trailing-slash дублируют PageRank |
| Нет hreflang | 32 из 32 | Google не знает целевую локаль, может показывать /ru/ англоязычным пользователям |
| Нет `<title>` в static HTML на /firmwares/antminer | 1 | Title рендерится через JS — Googlebot может не видеть его при первом краулинге |
| Нет JSON-LD schema | все страницы | Нет eligibility для rich results; AI-системы хуже распознают сущности |

**Ключевое:** `/en/firmwares/antminer` сейчас удерживает **позицию 1** в Google по запросу
"custom firmware for Antminer" — без единого meta-тега и без H1. Позиция держится на авторитете
домена, но уязвима: любой конкурент (Braiins, D-Central) с нормально оптимизированной страницей
может её занять. Правки ниже — прежде всего **защитные**.

**Ожидаемый эффект после деплоя:**
- Рост CTR на firmware-страницах (мета описания + правильные SERP сниппеты)
- Устранение риска потери позиции 1 по главному коммерческому запросу
- Eligibility для FAQ Rich Results на `/en/firmwares/antminer` (7 FAQ-пар в JSON-LD)
- Правильная сигнализация локали Google (после деплоя hreflang)

---

## 2. Порядок внедрения

Соблюдай последовательность — есть зависимости:

```
Фаза 1 (независимые, деплой сразу)
├── 3.1 Canonical теги — все 32 страницы (шаблон)
├── 3.2 Meta descriptions — все 32 страницы (контент CMS)
└── 3.5 robots.txt — явные разрешения для AI-краулеров

Фаза 2 (после Фазы 1)
├── 3.3 /en/firmwares/antminer — Title (static), H1, JSON-LD
└── 3.4 301 redirect: /en/firmwares/asic-S17-S17Pro → /asic-s17-s17pro

Фаза 3 (только после VERIFY — см. раздел 5)
└── 3.5 Hreflang теги — все 32 страницы
    ⚠️  Деплоить ТОЛЬКО после подтверждения списка /ru/* страниц.
    Hreflang с несуществующим /ru/ URL → ошибка в GSC.
```

---

## 3. Правки

---

### 3.1 Canonical теги — все 32 страницы

**Способ 1 — шаблон (рекомендуется):** добавить один тег в `<head>` шаблон CMS/фреймворка.
Переменная `canonical_path` = текущий URL страницы без UTM-параметров, без trailing slash.

```html
<!-- Canonical — в <head> шаблон -->
<link rel="canonical" href="https://bixbit.io{{ canonical_path }}">
```

**Способ 2 — статические теги на каждую страницу** (если CMS не поддерживает переменные):

#### Firmware

```html
<!-- /en/firmwares -->
<link rel="canonical" href="https://bixbit.io/en/firmwares">

<!-- /en/firmwares/antminer -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/antminer">

<!-- /en/firmwares/whatsminer-all-series -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-all-series">

<!-- /en/firmwares/whatsminer-series-m6x -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m6x">

<!-- /en/firmwares/whatsminer-series-m5x -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m5x">

<!-- /en/firmwares/whatsminer-series-m3x -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">

<!-- /en/firmwares/whatsminer-series-m2x -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/whatsminer-series-m2x">

<!-- /en/firmwares/asic-s19 -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-s19">

<!-- /en/firmwares/asic-S17-S17Pro → указывает на LOWERCASE preferred URL -->
<!-- Одновременно добавить 301: /en/firmwares/asic-S17-S17Pro → /en/firmwares/asic-s17-s17pro -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-s17-s17pro">

<!-- /en/firmwares/asic-S17-plus -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-S17-plus">

<!-- /en/firmwares/asic-T17-plus -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-T17-plus">

<!-- /en/firmwares/asic-T17 -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-T17">

<!-- /en/firmwares/asic-T9-plus -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-T9-plus">

<!-- /en/firmwares/asic-s9-s9j-s9i -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/asic-s9-s9j-s9i">
```

#### Cooling

```html
<!-- /en/asics-cooling -->
<link rel="canonical" href="https://bixbit.io/en/asics-cooling">

<!-- /en/asics-cooling/hydro-systems -->
<link rel="canonical" href="https://bixbit.io/en/asics-cooling/hydro-systems">

<!-- /en/asics-cooling/immersion-systems -->
<link rel="canonical" href="https://bixbit.io/en/asics-cooling/immersion-systems">

<!-- /en/products -->
<link rel="canonical" href="https://bixbit.io/en/products">

<!-- /en/products/rack -->
<link rel="canonical" href="https://bixbit.io/en/products/rack">

<!-- /en/products/rack-hydro -->
<link rel="canonical" href="https://bixbit.io/en/products/rack-hydro">

<!-- /en/products/server -->
<link rel="canonical" href="https://bixbit.io/en/products/server">

<!-- /en/products/container -->
<link rel="canonical" href="https://bixbit.io/en/products/container">

<!-- /en/products/container-hydro -->
<link rel="canonical" href="https://bixbit.io/en/products/container-hydro">

<!-- /en/products/container-1k -->
<link rel="canonical" href="https://bixbit.io/en/products/container-1k">

<!-- /en/products/cell -->
<link rel="canonical" href="https://bixbit.io/en/products/cell">

<!-- /en/products/coolant -->
<link rel="canonical" href="https://bixbit.io/en/products/coolant">
```

#### Monitoring, Homepage, Other

```html
<!-- /en/ams -->
<link rel="canonical" href="https://bixbit.io/en/ams">

<!-- /en/ams/connect — noindex, страница незапущенной формы, не индексировать -->
<link rel="canonical" href="https://bixbit.io/en/ams/connect">
<meta name="robots" content="noindex, nofollow">

<!-- /en -->
<link rel="canonical" href="https://bixbit.io/en">

<!-- /en/about -->
<link rel="canonical" href="https://bixbit.io/en/about">

<!-- /en/contacts -->
<link rel="canonical" href="https://bixbit.io/en/contacts">

<!-- /en/sustainability -->
<link rel="canonical" href="https://bixbit.io/en/sustainability">
```

---

### 3.2 Meta descriptions — все 32 страницы

Добавить в `<head>` каждой страницы. Все описания: 130–155 символов, технический B2B-тон.

#### Homepage & Firmware

```html
<!-- /en -->
<meta name="description" content="BiXBiT: custom ASIC firmware, immersion cooling, and fleet monitoring for large-scale Antminer and Whatsminer mining operations. Free 30-day trial.">

<!-- /en/firmwares -->
<meta name="description" content="BiXBiT custom firmware for Antminer and Whatsminer ASICs: overclocking, autotuning, Farm Protect antivirus. 30-day free trial for all supported models.">

<!-- /en/firmwares/antminer -->
<meta name="description" content="BiXBiT custom firmware for Antminer: overclocking, autotuning, and efficiency tuning for S21, S19, T21. Try free 30 days — no commitment.">

<!-- /en/firmwares/whatsminer-all-series -->
<meta name="description" content="BiXBiT custom firmware for all Whatsminer series — M2x, M3x, M5x, M6x. Overclocking, autotuning, Farm Protect antivirus. Free 30-day trial.">

<!-- /en/firmwares/whatsminer-series-m6x -->
<meta name="description" content="BiXBiT firmware for Whatsminer M6x series: overclocking and autotuning for M60S, M63S, M66S miners. Download free — 30-day trial, no commitment.">

<!-- /en/firmwares/whatsminer-series-m5x -->
<meta name="description" content="BiXBiT firmware for Whatsminer M5x series: overclocking and autotuning for M50, M50S, M53, M56S miners. Download free — 30-day trial, no commitment.">

<!-- /en/firmwares/whatsminer-series-m3x -->
<meta name="description" content="BiXBiT firmware for Whatsminer M3x series — M30, M31, M32: overclocking, autotuning, efficiency tuning. Download free — 30-day trial, no commitment.">

<!-- /en/firmwares/whatsminer-series-m2x -->
<meta name="description" content="BiXBiT firmware for Whatsminer M20S and M21S: overclocking and efficiency tuning for M2x-series MicroBT miners. Free 30-day trial, no commitment.">

<!-- /en/firmwares/asic-s19 -->
<meta name="description" content="BiXBiT custom firmware for Antminer S19 series: overclocking, autotuning, efficiency tuning for S19 Pro, S19j, S19 XP, and T19 miners. Free trial.">

<!-- /en/firmwares/asic-S17-S17Pro -->
<meta name="description" content="BiXBiT overclock firmware for Antminer S17 and S17 Pro: frequency tuning and performance optimization. Farm Protect antivirus. Free 30-day trial.">

<!-- /en/firmwares/asic-S17-plus -->
<meta name="description" content="BiXBiT custom firmware for Antminer S17+: overclocking, underclocking, and efficiency tuning for S17 Plus miners. Free 30-day trial download.">

<!-- /en/firmwares/asic-T17-plus -->
<meta name="description" content="BiXBiT firmware for Antminer T17+: overclocking and autotuning for T17 Plus ASIC miners. Improve efficiency and hashrate stability. Free trial.">

<!-- /en/firmwares/asic-T17 -->
<meta name="description" content="BiXBiT custom firmware for Antminer T17: overclocking, underclocking, and autotuning for T17 miners. Download free — 30-day trial, no commitment.">

<!-- /en/firmwares/asic-T9-plus -->
<meta name="description" content="BiXBiT overclock firmware for Antminer T9+: hashrate boosting and efficiency tuning for T9 Plus miners. Free 30-day download, no commitment.">

<!-- /en/firmwares/asic-s9-s9j-s9i -->
<meta name="description" content="BiXBiT overclock firmware for Antminer S9, S9j, and S9i: maximize hashrate and extend lifecycle of legacy miners. Free 30-day trial download.">
```

#### Cooling

```html
<!-- /en/asics-cooling -->
<meta name="description" content="Industrial cooling solutions for Bitcoin ASIC miners: immersion cooling, hydro systems, and air-to-liquid racks for large-scale mining operations.">

<!-- /en/asics-cooling/hydro-systems -->
<meta name="description" content="BiXBiT hydro cooling racks for ASIC miners: liquid-to-air heat exchange for high-density Antminer and Whatsminer installations. Contact for configuration.">

<!-- /en/asics-cooling/immersion-systems -->
<meta name="description" content="BiXBiT immersion cooling systems for ASIC miners: single-phase dielectric fluid submersion for Antminer S21, S19, and Whatsminer M-series.">

<!-- /en/products -->
<meta name="description" content="BiXBiT industrial cooling equipment for ASIC miners: immersion tanks, hydro racks, server cooling, containers, and dielectric coolant. Request a quote.">

<!-- /en/products/rack -->
<meta name="description" content="BiXBiT ASIC mining rack: high-density air-cooled rack for Antminer and Whatsminer miners. Engineered for large-scale mining farm deployments.">

<!-- /en/products/rack-hydro -->
<meta name="description" content="BiXBiT hydro rack: liquid-cooled ASIC mining rack with integrated coolant distribution for high-density Antminer deployments. Contact for specifications.">

<!-- /en/products/server -->
<meta name="description" content="BiXBiT immersion cooling for servers and GPU rigs: single-phase dielectric fluid cooling for data center and co-location deployments.">

<!-- /en/products/container -->
<meta name="description" content="BiXBiT mining container: self-contained ASIC mining facility with integrated cooling and power distribution for industrial deployments. Contact for specs.">

<!-- /en/products/container-hydro -->
<meta name="description" content="BiXBiT hydro container: turnkey Bitcoin mining container with integrated liquid cooling for high-density ASIC deployments. Contact for specifications.">

<!-- /en/products/container-1k -->
<meta name="description" content="BiXBiT large-capacity mining container: integrated cooling and power distribution for industrial Bitcoin mining farms. Contact for capacity and pricing.">

<!-- /en/products/cell -->
<meta name="description" content="BiXBiT Cell: immersion cooling kit for Antminer S19 and S21. Retrofit air-cooled miners for single-phase dielectric immersion. Contact for availability.">

<!-- /en/products/coolant -->
<meta name="description" content="BiXBiT dielectric coolant for ASIC immersion cooling: engineered for Antminer and Whatsminer single-phase immersion systems. Order online or contact.">
```

#### Monitoring & Other

```html
<!-- /en/ams -->
<meta name="description" content="BiXBiT AMS: cloud fleet monitoring for ASIC mining farms. Real-time hashrate, alerts, power metrics, and remote control for Antminer and Whatsminer.">

<!-- /en/ams/connect — meta description НЕ добавлять, страница noindex -->

<!-- /en/about -->
<meta name="description" content="BiXBiT designs custom ASIC firmware, industrial cooling, and fleet monitoring software for large-scale Bitcoin mining operations worldwide.">

<!-- /en/contacts -->
<meta name="description" content="Contact BiXBiT for custom ASIC firmware, immersion cooling systems, and fleet monitoring. Sales, technical support, and partnership inquiries.">

<!-- /en/sustainability -->
<meta name="description" content="BiXBiT's approach to sustainable Bitcoin mining: energy efficiency, heat recycling, and environmental impact reduction in industrial ASIC operations.">
```

---

### 3.3 Страница /en/firmwares/antminer — title, H1, JSON-LD

Это единственная страница с дополнительными точечными правками помимо canonical и meta desc.

#### 3.3.1 Title — перенести из JS в static HTML

**Проблема:** текущий `<title>` рендерится через JavaScript. Googlebot может не получить его
при первом краулинге. Перенести тег в серверный `<head>` шаблон для этой страницы.

```html
<!-- Заменить JS-рендеренный title на статический в <head> -->
<title>Custom Firmware for Antminer | BiXBiT</title>
```

#### 3.3.2 H1 — добавить на страницу

**Проблема:** H1 на странице отсутствует. Текущий H2 "Custom firmware BiXBiT for Antminer"
выполняет роль заголовка, но H1 — сильнейший on-page ranking-сигнал.

Добавить как первый элемент основного контента страницы (до product-selector и feature-списка):

```html
<h1>Custom Firmware for Antminer by BiXBiT</h1>
```

Текущий H2 "Custom firmware BiXBiT for Antminer" — убрать или переработать в вводный абзац.

#### 3.3.3 Первый абзац (AI/LLM citation-ready)

Добавить сразу после H1, до product selector:

```html
<p>
  BiXBiT custom firmware for Antminer is a third-party ASIC firmware developed for
  industrial Bitcoin mining operations, supporting Antminer S21, S19, T21, L7, and
  L9 series devices. It replaces stock Bitmain firmware to deliver overclocking,
  automatic frequency tuning (autotuning), and energy efficiency optimization.
  Key differentiators include integrated Farm Protect antivirus, native AMS fleet
  monitoring, and dedicated immersion and hydro cooling profiles — with a 30-day free
  trial and a 2.8% developer fee.
</p>
```

> ⚠️ Перед публикацией подтвердить: dev fee = 2.8% актуален (см. раздел 5, п. 3).

#### 3.3.4 JSON-LD Schema — добавить в `<head>`

Два типа: `SoftwareApplication` + `FAQPage`. Вставить оба как один `<script>` блок.

```html
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "BiXBiT Custom Firmware for Antminer",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Antminer ASIC (Bitmain)",
    "description": "Third-party custom firmware for Antminer ASIC miners. Supports overclocking, autotuning, efficiency tuning, Farm Protect antivirus, and AMS fleet monitoring integration. Compatible with Antminer S21, S19, T21, T19, L7, and L9 series.",
    "url": "https://bixbit.io/en/firmwares/antminer",
    "publisher": {
      "@type": "Organization",
      "name": "BiXBiT",
      "url": "https://bixbit.io"
    },
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD",
      "description": "30-day free trial. Developer fee: 2.8% of mining revenue after trial.",
      "url": "https://bixbit.io/en/firmwares/antminer"
    },
    "featureList": [
      "Overclocking and underclocking",
      "Automatic frequency tuning (autotuning)",
      "Efficiency tuning (J/TH optimization)",
      "Farm Protect antivirus",
      "Immersion and hydro cooling profiles",
      "AMS fleet monitoring integration"
    ],
    "downloadUrl": "https://bixbit.io/en/firmwares/antminer",
    "releaseNotes": "https://bixbit.io/en/documentation"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is custom firmware for Antminer?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Custom firmware for Antminer is third-party software that replaces the stock Bitmain operating system on Antminer ASIC miners. It unlocks advanced controls — including overclocking, underclocking, and automatic frequency tuning (autotuning) — to improve hashrate output and energy efficiency beyond factory defaults."
        }
      },
      {
        "@type": "Question",
        "name": "Is BiXBiT firmware safe to use?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "BiXBiT firmware includes Farm Protect, an integrated antivirus module that scans for malware and unauthorized pool redirects."
        }
      },
      {
        "@type": "Question",
        "name": "Which Antminer models does BiXBiT firmware support?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "BiXBiT firmware supports Antminer S21, S21 Pro, S21 XP, S21 XP Hyd., S21 Hyd., S21 Immersion, S19, S19i, S19a Pro, S19 Pro-A, S19 Pro, S19j Pro, S19j Pro+, S19j+, S19k Pro, S19 XP, S19 XP+, S19j XP, S19 Hydro, S19 Pro Hyd., T21, T19, L7, and L9 series."
        }
      },
      {
        "@type": "Question",
        "name": "What is the developer fee for BiXBiT firmware?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "BiXBiT firmware uses a 2.8% developer fee, meaning 2.8% of your miner's work is directed to BiXBiT pool addresses after the 30-day free trial period."
        }
      },
      {
        "@type": "Question",
        "name": "Can I use BiXBiT firmware with immersion or hydro cooling?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. BiXBiT firmware includes dedicated operating profiles for immersion cooling and hydro cooling configurations, including support for Antminer S21 XP Hyd., S21 Hyd., S19 Hydro, and S19 Pro Hyd. models."
        }
      },
      {
        "@type": "Question",
        "name": "Does BiXBiT firmware integrate with AMS monitoring?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Devices running BiXBiT firmware gain open access to BiXBiT AMS (Advanced Mining System), a cloud-based fleet monitoring dashboard for centralized management across all flashed devices."
        }
      },
      {
        "@type": "Question",
        "name": "How do I roll back to stock Antminer firmware?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "BiXBiT firmware supports rollback to original Bitmain stock firmware. See the documentation at https://bixbit.io/en/documentation for rollback steps."
        }
      }
    ]
  }
]
</script>
```

> ⚠️ Заменить `"REPLACE_WITH_CURRENT_VERSION"` на реальный номер версии прошивки перед деплоем.

---

### 3.3.5 /en/ams/connect — noindex

**Причина:** страница содержит незапущенную форму и не несёт SEO-ценности.
Добавить в `<head>` страницы:

```html
<meta name="robots" content="noindex, nofollow">
```

**Следствия:**
- Meta description для этой страницы **не добавлять**
- Hreflang теги для этой страницы **не добавлять**
- Canonical тег добавить (уже включён в п. 3.1 — он не мешает noindex)

---

### 3.4 Hreflang — все 32 страницы

**⛔ НЕ ДЕПЛОИТЬ до выполнения VERIFY п. 2 (список /ru/* страниц).**

Hreflang с несуществующим `/ru/` URL генерирует ошибки в GSC и может навредить ранжированию.

**Шаблонный вариант** (если CMS поддерживает переменные):

```html
<!-- Hreflang — в <head> шаблон, только если /ru{{ page_path }} существует -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en{{ page_path }}">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru{{ page_path }}">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en{{ page_path }}">
```

**Статические теги** (копировать блок для каждой страницы после подтверждения /ru/*):

```html
<!-- /en → /ru [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en">

<!-- /en/firmwares → /ru/firmwares [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares">

<!-- /en/firmwares/antminer → /ru/firmwares/antminer [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer">

<!-- /en/firmwares/whatsminer-all-series [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-all-series">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-all-series">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-all-series">

<!-- /en/firmwares/whatsminer-series-m6x [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m6x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m6x">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m6x">

<!-- /en/firmwares/whatsminer-series-m5x [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m5x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m5x">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m5x">

<!-- /en/firmwares/whatsminer-series-m3x [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m3x">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">

<!-- /en/firmwares/whatsminer-series-m2x [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m2x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m2x">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m2x">

<!-- /en/firmwares/asic-s19 [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-s19">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-s19">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-s19">

<!-- /en/firmwares/asic-S17-S17Pro → lowercase preferred после редиректа [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-s17-s17pro">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-s17-s17pro">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-s17-s17pro">

<!-- /en/firmwares/asic-S17-plus [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-S17-plus">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-S17-plus">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-S17-plus">

<!-- /en/firmwares/asic-T17-plus [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-T17-plus">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-T17-plus">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-T17-plus">

<!-- /en/firmwares/asic-T17 [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-T17">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-T17">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-T17">

<!-- /en/firmwares/asic-T9-plus [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-T9-plus">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-T9-plus">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-T9-plus">

<!-- /en/firmwares/asic-s9-s9j-s9i [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/asic-s9-s9j-s9i">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/asic-s9-s9j-s9i">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/asic-s9-s9j-s9i">

<!-- /en/asics-cooling [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/asics-cooling">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/asics-cooling">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/asics-cooling">

<!-- /en/asics-cooling/hydro-systems [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/asics-cooling/hydro-systems">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/asics-cooling/hydro-systems">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/asics-cooling/hydro-systems">

<!-- /en/asics-cooling/immersion-systems [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/asics-cooling/immersion-systems">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/asics-cooling/immersion-systems">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/asics-cooling/immersion-systems">

<!-- /en/products [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products">

<!-- /en/products/rack [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/rack">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/rack">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/rack">

<!-- /en/products/rack-hydro [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/rack-hydro">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/rack-hydro">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/rack-hydro">

<!-- /en/products/server [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/server">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/server">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/server">

<!-- /en/products/container [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/container">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/container">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/container">

<!-- /en/products/container-hydro [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/container-hydro">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/container-hydro">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/container-hydro">

<!-- /en/products/container-1k [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/container-1k">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/container-1k">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/container-1k">

<!-- /en/products/cell [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/cell">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/cell">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/cell">

<!-- /en/products/coolant [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products/coolant">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products/coolant">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products/coolant">

<!-- /en/ams [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/ams">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/ams">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/ams">

<!-- /en/about [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/about">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/about">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/about">

<!-- /en/contacts [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/contacts">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/contacts">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/contacts">

<!-- /en/sustainability [VERIFY] -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/sustainability">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/sustainability">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/sustainability">
```

> **Правило:** hreflang — симметричный. На `/ru/firmwares/antminer` должны быть **те же три тега**,
> что и на `/en/firmwares/antminer`. Если `/ru/*` страница существует, добавить туда зеркальные теги.

---

### 3.5 robots.txt — явные разрешения для AI-краулеров

**Контекст:** GEO-аудит (2026-06-18) подтвердил, что все AI-краулеры уже разрешены через
общий `User-agent: *`. Явные блоки ниже делают разрешение недвусмысленным и добавляют
мета-директивы для новых AI-протоколов.

**Добавить в конец файла `robots.txt`** (корень сайта, `https://bixbit.io/robots.txt`):

```
# AI crawlers — explicit allow
ai-train: yes
search: yes
ai-input: yes

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

> **Примечание:** `ai-train: yes`, `search: yes`, `ai-input: yes` — мета-директивы
> для AI-сервисов, сигнализирующие о согласии на индексацию и обучение. Не являются
> стандартом W3C, но распознаются рядом LLM-платформ.
> Добавлять **после** существующих директив, не заменяя их.

---

## 4. Чеклист разработчика после деплоя

### Фаза 1 (canonical + meta desc + robots.txt)

- [ ] `curl -s https://bixbit.io/robots.txt | grep -A2 "GPTBot\|ClaudeBot\|PerplexityBot\|ai-train"` — убедиться что новые блоки присутствуют
- [ ] Открыть `view-source:https://bixbit.io/en/firmwares/antminer` — убедиться что `<link rel="canonical">` и `<meta name="description">` видны в **static HTML**, не в JS-рендеренном DOM
- [ ] Проверить 5 случайных страниц через `curl -s https://bixbit.io/en/ams | grep -i "canonical\|description"` — теги должны присутствовать
- [ ] Google Search Console → Coverage → проверить нет ли новых ошибок через 24–48 ч

### Фаза 2 (/en/firmwares/antminer)

- [ ] `view-source:https://bixbit.io/en/firmwares/antminer` → `<title>Custom Firmware for Antminer | BiXBiT</title>` присутствует в static HTML
- [ ] На странице виден `<h1>Custom Firmware for Antminer by BiXBiT</h1>` в DOM
- [ ] JSON-LD валиден: проверить через [Google Rich Results Test](https://search.google.com/test/rich-results) по URL `https://bixbit.io/en/firmwares/antminer`
  - Ожидаемый результат: **SoftwareApplication** детектируется без ошибок
  - Ожидаемый результат: **FAQ** детектируется, 7 вопросов видны
- [ ] `softwareVersion` в JSON-LD заменён на реальный номер версии (не `REPLACE_WITH_CURRENT_VERSION`)
- [ ] 301 редирект `/en/firmwares/asic-S17-S17Pro` → `/en/firmwares/asic-s17-s17pro`: проверить через `curl -I https://bixbit.io/en/firmwares/asic-S17-S17Pro` — ожидаемый ответ `301`

### Фаза 3 (hreflang — после VERIFY)

- [ ] Открыть `view-source:` на 3 разных `/en/*` страницах — убедиться что все три hreflang тега присутствуют
- [ ] Google Search Console → International Targeting → Language → убедиться нет hreflang-ошибок (проверить через 3–5 дней после деплоя)
- [ ] На соответствующих `/ru/*` страницах добавлены зеркальные hreflang теги (без этого GSC выдаст ошибку "Missing return tags")

---

## 5. VERIFY — уточнить до деплоя

Эти пункты требуют ответа от команды продукта/маркетинга **перед** деплоем конкретных элементов.

| # | Что уточнить | Где используется | Блокирует деплой |
|---|---|---|---|
| ~~1~~ | ~~`/en/ams/connect`~~  | ~~Canonical 3.1~~  | ✅ **Решено:** добавлен noindex (п. 3.3.5), meta desc и hreflang убраны |
| 2 | **Список `/ru/*` страниц** — какие из 32 путей реально существуют и индексируются? Прогнать через краулер или GSC | Hreflang 3.4 (весь блок) | Да, для Фазы 3 |
| 3 | **Dev fee = 2.8%** — актуальный процент? | Meta desc `/en/firmwares/antminer`, JSON-LD offers.description, первый абзац | Да, перед деплоем п. 3.3 |
| 4 | **`softwareVersion`** — текущая версия прошивки (строка для JSON-LD) | JSON-LD SoftwareApplication | Да, перед деплоем п. 3.3.4 |
| 5 | **Модели Whatsminer M6x** — полный список поддерживаемых моделей (M60S, M63S, M66S — верно?) | Meta desc `/en/firmwares/whatsminer-series-m6x` | Желательно |
| 6 | **Модели Whatsminer M5x** — M50, M50S, M53, M56S верно? | Meta desc `/en/firmwares/whatsminer-series-m5x` | Желательно |
| 7 | **Модели Whatsminer M2x** — M20S, M21S верно? | Meta desc `/en/firmwares/whatsminer-series-m2x` | Желательно |
| 8 | **`/en/products/container-1k`** — страница существует? Верен ли слаг? | Canonical 3.1 (есть в sitemap с пробелом в URL) | Да |
| 9 | **`x-default`** — подтвердить что `/en/` является дефолтной локалью для hreflang | Hreflang 3.4 (x-default для всех страниц) | Да, для Фазы 3 |
| 10 | **Farm Protect** — есть ли публичные security-детали (audit, certifications) для добавления в FAQ "Is BiXBiT firmware safe?" | JSON-LD FAQPage | Нет (FAQ работает и без этого) |

---

*Документ сгенерирован: 2026-06-17*
*Источники: full-audit-2026-06-17.md, page-optimize/firmwares-antminer.md, seo-fixes/canonical-all-pages.md, seo-fixes/hreflang-all-pages.md, seo-fixes/meta-descriptions-all-pages.md*
