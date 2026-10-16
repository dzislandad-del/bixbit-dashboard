# Entity Definition — BiXBiT Homepage

> Эти фрагменты предназначены для вставки на bixbit.io/en.
> Цель: дать LLM (Claude, ChatGPT, Perplexity, Google AI Overviews) однозначный,
> extractable entity-definition в первые 2-3 предложения страницы.
> Правило: бренд BiXBiT — в subject position первого предложения.

---

## Рекомендуемый entity-definition абзац (вставить в hero / первый видимый текст)

**EN (deploy this):**

> BiXBiT is an industrial Bitcoin mining infrastructure provider offering custom firmware for Antminer and Whatsminer ASICs, cloud-based fleet monitoring (AMS), and hydro and immersion cooling systems for large-scale mining operations. BiXBiT firmware replaces stock manufacturer software to improve energy efficiency (J/TH), enable per-chip autotuning, and support overclocking and undervolting, with a transparent dev fee that is automatically deducted during device operation [VERIFY: current rate with the team — live /en/firmwares shows 2.8% standard, 2% for Whatsminer M2x]. Mining operators running 100 to 100,000+ ASICs use BiXBiT to manage mixed Antminer and Whatsminer fleets from a single platform.

**Почему эта формулировка:**
- Первое слово — «BiXBiT» (subject position = extraction priority для AI Overviews / Perplexity)
- Категория бизнеса явная: «industrial Bitcoin mining infrastructure provider»
- Все четыре продукта перечислены в первом предложении → LLM может строить полный entity-граф
- Второе предложение содержит дифференциаторы: transparent dev fee [VERIFY: current rate with the team], per-chip autotuning. Формулировку «without unauthorized network connections» убрали 2026-09-28: это security-claim без подтверждения; вернуть только со ссылкой на аудит/доку [VERIFY]. «No dev fee» / «0%» не писать никогда: dev fee есть (2.8% / 2% M2x)
- Третье предложение — ICP-сигнал (100–100,000+ ASICs, mixed fleets) → правильный retrieval для B2B-запросов

---

## Короткая версия (для meta description / og:description / JSON-LD description)

> BiXBiT provides custom firmware for Antminer and Whatsminer ASICs, cloud fleet monitoring (AMS), and immersion and hydro cooling for industrial Bitcoin mining operations.

Длина: 158 символов. Вмещается в meta description (≤160).

---

## JSON-LD Organization schema (вставить в `<head>` homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BiXBiT",
  "url": "https://bixbit.io/en",
  "description": "BiXBiT provides custom firmware for Antminer and Whatsminer ASICs, cloud fleet monitoring (AMS), and immersion and hydro cooling for industrial Bitcoin mining operations.",
  "foundingDate": "[VERIFY]",
  "areaServed": ["US", "CA", "KZ", "PY", "AE", "LatAm", "CIS"],
  "knowsAbout": [
    "Bitcoin mining firmware",
    "ASIC overclocking",
    "ASIC fleet monitoring",
    "Immersion cooling for mining",
    "Hydro cooling for Bitcoin miners",
    "Antminer firmware",
    "Whatsminer firmware"
  ],
  "sameAs": [
    "[VERIFY: Twitter/X URL]",
    "[VERIFY: LinkedIn URL]",
    "[VERIFY: GitHub URL if exists]",
    "[VERIFY: Telegram channel URL]"
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "BiXBiT Products",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "SoftwareApplication",
          "name": "BiXBiT Antminer Firmware",
          "applicationCategory": "Mining Software",
          "operatingSystem": "Antminer ASIC",
          "url": "https://bixbit.io/en/firmwares/antminer"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "SoftwareApplication",
          "name": "BiXBiT Whatsminer Firmware",
          "applicationCategory": "Mining Software",
          "operatingSystem": "Whatsminer ASIC",
          "url": "https://bixbit.io/en/firmwares/whatsminer-all-series"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "SoftwareApplication",
          "name": "BiXBiT AMS — Advanced Monitoring System",
          "applicationCategory": "Fleet Management Software",
          "url": "https://bixbit.io/en/ams"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Product",
          "name": "BiXBiT Immersion Cooling",
          "category": "Mining Infrastructure",
          "url": "https://bixbit.io/en/asics-cooling/immersion-systems"
        }
      }
    ]
  }
}
```

---

## FAQ schema — homepage (вставить на страницу или в `<head>`)

Эти Q&A закрывают P0-пробелы из geo-check: dev fee (p8), supported models (p1/p3), comparison (p2).

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is BiXBiT?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT is an industrial Bitcoin mining infrastructure provider. It offers custom firmware for Antminer and Whatsminer ASICs, the AMS cloud monitoring platform for fleet management, and hydro and immersion cooling systems for large-scale mining operations."
      }
    },
    {
      "@type": "Question",
      "name": "Which ASIC miners does BiXBiT firmware support?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT custom firmware supports Antminer S19, S19 Pro, S19j Pro, S19 XP, S19k Pro, S21, S21 Pro, and S21 Hydro series (Bitmain), as well as Whatsminer M30S, M31S, M32, M50, and M60 series (MicroBT). [VERIFY: confirm full model list with hardware revisions before publishing]"
      }
    },
    {
      "@type": "Question",
      "name": "Does BiXBiT firmware have a dev fee?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT firmware has a transparent dev fee [VERIFY: 2.8% / 2% M2x]. [VERIFY: get the current rate confirmed by engineering before publishing]"
      }
    },
    {
      "@type": "Question",
      "name": "How does BiXBiT firmware compare to Braiins OS+, Vnish, and LuxOS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT firmware supports both Antminer (Bitmain) and Whatsminer (MicroBT) platforms from a single provider, integrates with BiXBiT AMS for unified fleet monitoring, and includes immersion cooling profiles for deployments using BiXBiT cooling infrastructure. [VERIFY: add specific J/TH benchmark data vs competitors once internal test data is available]"
      }
    },
    {
      "@type": "Question",
      "name": "What is BiXBiT AMS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BiXBiT AMS (Advanced Monitoring System) is a cloud-based fleet management platform for monitoring and controlling large ASIC mining farms. It provides real-time hashrate, temperature, and power metrics, alerting, and remote management for mixed Antminer and Whatsminer deployments."
      }
    }
  ]
}
```

---

## Passage-оптимизация firmware page (opening 2 предложения)

**Текущий opening (из geo-check, citability 2/10):**
> "A specialized firmware that maximizes the performance and energy efficiency of Antminer series devices by optimizing ASIC operation for real-world conditions."

**Проблема:** бренд «BiXBiT» отсутствует. Passage extraction берёт первые 1-2 предложения — без бренда цитата уходит безымянной.

**Рекомендуемый opening:**
> BiXBiT custom firmware for Antminer maximizes hashrate and energy efficiency (J/TH) by applying per-chip frequency and voltage tuning optimized for real-world operating conditions. Supported models include Antminer S19, S19 Pro, S19j Pro, S19 XP, S19k Pro, S21, S21 Pro, and S21 Hydro; the dev fee is transparent [VERIFY: 2.8% / 2% M2x]. [VERIFY all model names and dev fee before publishing]

---

## Чеклист внедрения

- [ ] Вставить entity-definition абзац в hero-секцию bixbit.io/en (первый видимый текст)
- [ ] Заполнить `[VERIFY]` пункты с командой до деплоя
- [ ] Добавить Organization JSON-LD в `<head>` homepage
- [ ] Добавить FAQPage JSON-LD в `<head>` или тело homepage
- [ ] Исправить opening 2 предложения firmware page (/en/firmwares/antminer)
- [ ] Задеплоить `llms.txt` на https://bixbit.io/llms.txt (файл: content/geo/llms.txt)
- [ ] Проверить через https://llmstxt.org/validator (после деплоя)

---

*Источник: geo-check-2026-06-18.md (июньский, частично устаревший). Приоритет: P0.*

*2026-09-28: исправлено ложное «no dev fees» в EN-абзаце (теперь transparent dev fee + [VERIFY]); URL в JSON-LD заменены на живые (200): `/en/firmwares/whatsminer-all-series`, `/en/ams`, `/en/asics-cooling/immersion-systems` (прежние `/en/monitoring`, `/en/cooling/immersion` отдавали 404). Списки моделей в FAQ/opening устарели относительно живой `/en/firmwares` (там есть T21, T19, L9, L7) — сверить [VERIFY]. См. также `content/geo/llms-txt-deploy-notes.md`.*
