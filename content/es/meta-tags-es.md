# meta-tags-es.md: title / description / H1 для /es/

> **Версия:** 2026-09-28. **Владелец:** international-seo, контент совместно с content-seo.
> **Основа:** живой снимок `/es/` (`page-snapshot.py`, сырой HTML, 2026-09-28), ядро — `content/es/semantic-core-es.md`, данные — `data/dfs-es-semantics-2026-09-28.json`.
> **Язык:** нейтральный латиноамериканский испанский (usted или безличные формы, без vosotros и испанизмов вроде «ordenador»). Код локали `es`.
> **Лимиты:** title ≤ 60 символов, description 140–160; длины посчитаны скриптом (символы Unicode). H1 — до ~65 символов.

## Правила для всех строк

- **Dev fee:** только «comisión de desarrollo transparente». Ставка в мету **не** выводится; в тексте страницы — с пометкой `[VERIFY: tarifa actual]` (по аудиту 2026-09: 2.8%, для M2x 2%). **Запрещено:** «sin comisión», «sin dev fee», «0 %», а также «gratis» рядом с firmware (читается как «без комиссии»).
- **Тех-спеки:** TH/s, %, J/TH, °C и списки моделей в мету не добавляем, пока их не подтвердит команда. Всё, что уже стоит на живых страницах («hasta 80 Th/s», «10-20%», «up to 130 Th/s», «+40%», «up to 90 Th/s»), помечено `[VERIFY]`, см. `content/localization-plan.md` §7.
- **Непереведённые страницы:** мета готова, но ставится **вместе с переводом тела**; только после этого URL попадает в hreflang-кластер и sitemap (hreflang-spec, B5). ES-мета поверх EN-тела хуже текущего состояния.
- Бренд — в конце title через « | BiXBiT» (как на EN-шаблоне); на главной — в начале.
- Бренды конкурентов в ES-мету не ставим.

## Сводка

| URL | Статус | Title (длина) | Description (длина) | H1 |
|---|---|---|---|---|
| `/es` | переведена, можно ставить | BiXBiT: firmware ASIC, monitoreo AMS y refrigeración (52) | Firmware personalizado para Antminer y Whatsminer, monitoreo AMS, refrigeración por inmersión e hidro y PDU para granjas de minería de Bitcoin a escala. (152) | Software y hardware para la minería industrial de Bitcoin |
| `/es/firmwares` | переведена, можно ставить | Firmware ASIC personalizado: Antminer y Whatsminer \| BiXBiT (59) | Firmware ASIC para Antminer y Whatsminer: autotuning, overclocking y underclocking, control remoto en AMS y una comisión de desarrollo transparente. (148) | Firmware personalizado BiXBiT para Antminer y Whatsminer |
| `/es/firmwares/antminer` | переведена, можно ставить | Firmware para Antminer: autotuning y overclock \| BiXBiT (55) | Firmware Antminer de BiXBiT para S19 y S21: autotuning, overclock y modo de bajo consumo, monitoreo en AMS y comisión de desarrollo transparente. (145) | Firmware personalizado para Antminer de BiXBiT |
| `/es/firmwares/whatsminer-all-series` | **сначала перевод** | Firmware Whatsminer M2x, M3x, M5x y M6x \| BiXBiT (48) | Firmware Whatsminer de BiXBiT para las series M2x, M3x, M5x y M6x: overclocking, protección contra sobrecalentamiento e instalación con WhatsMinerTool. (151) | Firmware personalizado para Whatsminer |
| `/es/firmwares/whatsminer-series-m2x` | **сначала перевод** | Firmware Whatsminer M20S y M21S (serie M2x) \| BiXBiT (52) | Firmware alternativo de BiXBiT para Whatsminer M2x (M20S, M21S): overclocking, ASICBoost, protección contra ataques y comisión de desarrollo transparente. (154) | Firmware para Whatsminer serie M2x |
| `/es/firmwares/whatsminer-series-m3x` | **сначала перевод** | Firmware Whatsminer M30, M31 y M32 (serie M3x) \| BiXBiT (55) | Firmware Whatsminer M3x de BiXBiT para M30, M31 y M32: overclocking, protección contra sobrecalentamiento, monitoreo remoto e instalación sencilla. (147) | Firmware para Whatsminer serie M3x |
| `/es/firmwares/whatsminer-series-m5x` | **сначала перевод** | Firmware Whatsminer serie M5x: descarga y overclock \| BiXBiT (60) | Firmware Whatsminer M5x de BiXBiT: overclocking, ASICBoost, protección contra ataques y modos para refrigeración por inmersión. Descarga e instalación. (151) | Firmware para Whatsminer serie M5x |
| `/es/firmwares/whatsminer-series-m6x` | **сначала перевод** | Firmware alternativo para Whatsminer serie M6x \| BiXBiT (55) | Firmware alternativo de BiXBiT para Whatsminer M6x: ASICBoost, protección contra ataques y modos para refrigeración por inmersión. Descarga e instalación. (154) | Firmware para Whatsminer serie M6x |
| `/es/ams` | переведена, можно ставить | Monitoreo de mineros ASIC: software AMS de BiXBiT (49) | BiXBiT AMS: software de monitoreo para granjas de minería con ASIC. Estadísticas en tiempo real, alertas y control remoto de equipos Antminer y Whatsminer. (155) | Sistema de monitoreo automatizado para mineros ASIC |
| `/es/ams/connect` | переведена, можно ставить | Conectar sus ASIC a BiXBiT AMS: registro y clave API (52) | Regístrese en BiXBiT AMS, seleccione los modelos de sus equipos ASIC y conéctelos mediante una clave API para monitorear su granja de minería en tiempo real. (157) | Conecte sus equipos ASIC a BiXBiT AMS |
| `/es/asics-cooling` | переведена, можно ставить | Refrigeración para minería ASIC: inmersión e hidro \| BiXBiT (59) | Sistemas de refrigeración para mineros ASIC: inmersión e hidro (líquida) para granjas de minería de Bitcoin. Menor temperatura, menos ruido y más estabilidad. (158) | Sistemas de refrigeración de alto rendimiento para mineros ASIC |
| `/es/asics-cooling/immersion-systems` | **сначала дочистить перевод** | Refrigeración por inmersión para minería ASIC \| BiXBiT (54) | Refrigeración por inmersión para mineros ASIC: tanques, líquido dieléctrico y circuito de enfriamiento para granjas de minería de Bitcoin de BiXBiT. (148) | Sistemas de refrigeración por inmersión para mineros ASIC |
| `/es/asics-cooling/hydro-systems` | **сначала дочистить перевод** | Refrigeración líquida (hidro) para mineros ASIC \| BiXBiT (56) | Refrigeración líquida (hidro) para ASIC Antminer y Whatsminer con enfriamiento por agua: racks y contenedores de BiXBiT para granjas de minería de Bitcoin. (155) | Sistemas de refrigeración líquida (hidro) para mineros ASIC |
| `/es/products/pdu` | переведена, можно ставить | PDU inteligente para minería ASIC \| BiXBiT Smart PDU (52) | BiXBiT Smart PDU: unidad de distribución de energía administrable para granjas de minería con ASIC. Control remoto de tomas y monitoreo del consumo. (148) | BiXBiT Smart PDU: distribución de energía para minería ASIC |
| `/es/products/server` | **сначала перевод** | Refrigeración por inmersión para servidores \| BiXBiT (52) | Refrigeración por inmersión de BiXBiT para servidores y centros de datos: menor consumo en refrigeración, más vida útil del hardware y reutilización del calor. (159) | Refrigeración por inmersión para servidores y centros de datos |
| `/es/faq` | переведена, можно ставить | Preguntas frecuentes: firmware, AMS y refrigeración \| BiXBiT (60) | Respuestas sobre el firmware BiXBiT para Antminer y Whatsminer, la comisión de desarrollo transparente, el monitoreo AMS y los sistemas de refrigeración. (153) | Preguntas frecuentes |

## По страницам: было и стало

### `/es` (переведена, можно ставить)

- **Основной ключ:** bixbit. **Вторичные:** software minería bitcoin, firmware ASIC, refrigeración por inmersión.
- **Сейчас:** title «Soluciones de minería Bitcoin BiXBiT – Herramientas para mineros» (64 зн.); description 196 зн.; H1 «Minería de Bitcoin Software y hardware».

```html
<title>BiXBiT: firmware ASIC, monitoreo AMS y refrigeración</title>
<meta name="description" content="Firmware personalizado para Antminer y Whatsminer, monitoreo AMS, refrigeración por inmersión e hidro y PDU para granjas de minería de Bitcoin a escala.">
<h1>Software y hardware para la minería industrial de Bitcoin</h1>
```

- Бренд: 170/мес в VE (Google Ads), 720 показов GSC из VE уходят на `/en`. Текущий description 201 зн. — обрезается.

### `/es/firmwares` (переведена, можно ставить)

- **Основной ключ:** firmware asic. **Вторичные:** firmware personalizado asic, bixbit firmware, overclocking asic, asic custom firmware.
- **Сейчас:** title «Firmware ASIC personalizado de minería BiXBiT» (45 зн.); description 158 зн.; H1 «Firmware personalizado BiXBiTpara Whatsminer y Antminer».

```html
<title>Firmware ASIC personalizado: Antminer y Whatsminer | BiXBiT</title>
<meta name="description" content="Firmware ASIC para Antminer y Whatsminer: autotuning, overclocking y underclocking, control remoto en AMS y una comisión de desarrollo transparente.">
<h1>Firmware personalizado BiXBiT para Antminer y Whatsminer</h1>
```

- Исправить опечатку в H1: «BiXBiTpara» → «BiXBiT para». Пустой FAQPage убрать или наполнить (FAQ «¿Dónde descargar el firmware?» — по GSC есть клики на такие вопросы). Текущий description содержит «hasta 80 Th/s» и «10-20%» — [VERIFY], в новую мету не переносим.

### `/es/firmwares/antminer` (переведена, можно ставить)

- **Основной ключ:** firmware antminer. **Вторичные:** antminer firmware, firmware antminer s19 / s21, overclock antminer, autotuning antminer, modo de bajo consumo.
- **Сейчас:** title «Firmware para Antminer de BiXBiT – Tu firmware personalizado» (60 зн.); description 172 зн.; H1 «Firmware personalizado de BiXBiT para Antminer».

```html
<title>Firmware para Antminer: autotuning y overclock | BiXBiT</title>
<meta name="description" content="Firmware Antminer de BiXBiT para S19 y S21: autotuning, overclock y modo de bajo consumo, monitoreo en AMS y comisión de desarrollo transparente.">
<h1>Firmware personalizado para Antminer de BiXBiT</h1>
```

- [VERIFY: список моделей — S19 и S21 взяты из EN-позиционирования; S9 и L7/L9 не упоминать до подтверждения поддержки]. Текущий description 177 зн. — обрезается.

### `/es/firmwares/whatsminer-all-series` (**сначала перевод**)

- **Основной ключ:** firmware whatsminer. **Вторичные:** whatsminer firmware, whatsminer tool, M2x / M3x / M5x / M6x.
- **Сейчас:** title «Whatsminer firmware | Download software for M2x, M3x, M5x, M6 ASICs» (67 зн.); description 158 зн.; H1 «».

```html
<title>Firmware Whatsminer M2x, M3x, M5x y M6x | BiXBiT</title>
<meta name="description" content="Firmware Whatsminer de BiXBiT para las series M2x, M3x, M5x y M6x: overclocking, protección contra sobrecalentamiento e instalación con WhatsMinerTool.">
<h1>Firmware personalizado para Whatsminer</h1>
```

- **Сначала перевод** (тело, title, description на EN, H1 пустой). Самый большой ES-разрыв: `whatsminer firmware` — 746 показов GSC (VE/AR/CO), поз. 4–5, 0 кликов. EN-цифру «up to 130 Th/s» в мету не переносить до [VERIFY].

### `/es/firmwares/whatsminer-series-m2x` (**сначала перевод**)

- **Основной ключ:** firmware whatsminer m20s [n/d]. **Вторичные:** whatsminer m20s, m21s.
- **Сейчас:** title «Whatsminer M20s Firmware – Download & Update M21s Software» (58 зн.); description 134 зн.; H1 «».

```html
<title>Firmware Whatsminer M20S y M21S (serie M2x) | BiXBiT</title>
<meta name="description" content="Firmware alternativo de BiXBiT para Whatsminer M2x (M20S, M21S): overclocking, ASICBoost, protección contra ataques y comisión de desarrollo transparente.">
<h1>Firmware para Whatsminer serie M2x</h1>
```

- **Сначала перевод.** Dev fee для M2x по аудиту 2% [VERIFY: tarifa actual] (сайт сам противоречив: Pricing 2.8% против FAQ 2%). EN «Free … download» не переводить как «gratis». «Boost up to 90 Th/s» — [VERIFY], в мету не ставить.

### `/es/firmwares/whatsminer-series-m3x` (**сначала перевод**)

- **Основной ключ:** firmware whatsminer m30s. **Вторичные:** whatsminer m30s, m31s, m32.
- **Сейчас:** title «Whatsminer M3x Firmware – Download for M30, M31, M32 ASICs» (58 зн.); description 143 зн.; H1 «».

```html
<title>Firmware Whatsminer M30, M31 y M32 (serie M3x) | BiXBiT</title>
<meta name="description" content="Firmware Whatsminer M3x de BiXBiT para M30, M31 y M32: overclocking, protección contra sobrecalentamiento, monitoreo remoto e instalación sencilla.">
<h1>Firmware para Whatsminer serie M3x</h1>
```

- **Сначала перевод.** Модели M30/M31/M32 — из текущего EN title. «up to 130 Th/s» — [VERIFY], в мету не ставить. Эта страница уже ранжируется в AR/CO по `whatsminer firmware` (EN-версия, поз. 4.2–4.3).

### `/es/firmwares/whatsminer-series-m5x` (**сначала перевод**)

- **Основной ключ:** firmware whatsminer m50. **Вторичные:** whatsminer m50.
- **Сейчас:** title «Whatsminer M5x Firmware – Download and Update M5x Software» (58 зн.); description 134 зн.; H1 «».

```html
<title>Firmware Whatsminer serie M5x: descarga y overclock | BiXBiT</title>
<meta name="description" content="Firmware Whatsminer M5x de BiXBiT: overclocking, ASICBoost, protección contra ataques y modos para refrigeración por inmersión. Descarga e instalación.">
<h1>Firmware para Whatsminer serie M5x</h1>
```

- **Сначала перевод.** «+40% hashrate» из EN — [VERIFY], в мету не ставить.

### `/es/firmwares/whatsminer-series-m6x` (**сначала перевод**)

- **Основной ключ:** firmware whatsminer m60 [n/d]. **Вторичные:** whatsminer m60.
- **Сейчас:** title «Whatsminer M6x Firmware | Download and update M6x software» (58 зн.); description 134 зн.; H1 «».

```html
<title>Firmware alternativo para Whatsminer serie M6x | BiXBiT</title>
<meta name="description" content="Firmware alternativo de BiXBiT para Whatsminer M6x: ASICBoost, protección contra ataques y modos para refrigeración por inmersión. Descarga e instalación.">
<h1>Firmware para Whatsminer serie M6x</h1>
```

- **Сначала перевод.** В EN-description M6x нет заявлений про разгон, поэтому в title нет «overclock».

### `/es/ams` (переведена, можно ставить)

- **Основной ключ:** monitoreo asic. **Вторичные:** software de monitoreo minería, monitoreo de mineros, software de minería.
- **Сейчас:** title «Software de monitoreo para ASIC – BiXBiT AMS» (44 зн.); description 179 зн.; H1 «Sistema de monitoreo automatizado para ASIC».

```html
<title>Monitoreo de mineros ASIC: software AMS de BiXBiT</title>
<meta name="description" content="BiXBiT AMS: software de monitoreo para granjas de minería con ASIC. Estadísticas en tiempo real, alertas y control remoto de equipos Antminer y Whatsminer.">
<h1>Sistema de monitoreo automatizado para mineros ASIC</h1>
```

- Функции (alertas, control remoto) — [VERIFY] по актуальной `/en/ams`. Текущий description 184 зн. — обрезается.

### `/es/ams/connect` (переведена, можно ставить)

- **Основной ключ:** ams bixbit (навигационный). **Вторичные:** conectar AMS, clave API.
- **Сейчас:** title «Conectar AMS BiXBiT» (19 зн.); description 111 зн.; H1 «Sí, tengo una cuenta».

```html
<title>Conectar sus ASIC a BiXBiT AMS: registro y clave API</title>
<meta name="description" content="Regístrese en BiXBiT AMS, seleccione los modelos de sus equipos ASIC y conéctelos mediante una clave API para monitorear su granja de minería en tiempo real.">
<h1>Conecte sus equipos ASIC a BiXBiT AMS</h1>
```

- H1 «Sí, tengo una cuenta» — подпись формы, а не заголовок страницы. Страница-вход: index оставить, отдельно не продвигать.

### `/es/asics-cooling` (переведена, можно ставить)

- **Основной ключ:** refrigeración para minería. **Вторичные:** enfriamiento minería bitcoin, refrigeración para rig de minería.
- **Сейчас:** title «Sistemas de refrigeración de alto rendimiento para mineros ASIC» (63 зн.); description 0 зн.; H1 «Sistemas de refrigeración de alto rendimiento para mineros ASIC».

```html
<title>Refrigeración para minería ASIC: inmersión e hidro | BiXBiT</title>
<meta name="description" content="Sistemas de refrigeración para mineros ASIC: inmersión e hidro (líquida) para granjas de minería de Bitcoin. Menor temperatura, menos ruido y más estabilidad.">
<h1>Sistemas de refrigeración de alto rendimiento para mineros ASIC</h1>
```

- Description сейчас **пустой**. «Menor temperatura, menos ruido» — качественное утверждение без цифр; °C не добавлять без [VERIFY].

### `/es/asics-cooling/immersion-systems` (**сначала дочистить перевод**)

- **Основной ключ:** refrigeración por inmersión. **Вторичные:** tanque de inmersión, líquido dieléctrico, refrigeración por inmersión minería / ASIC.
- **Сейчас:** title «Sistemas de refrigeración por inmersión» (39 зн.); description 0 зн.; H1 «Sistemas de refrigeración por inmersión».

```html
<title>Refrigeración por inmersión para minería ASIC | BiXBiT</title>
<meta name="description" content="Refrigeración por inmersión para mineros ASIC: tanques, líquido dieléctrico y circuito de enfriamiento para granjas de minería de Bitcoin de BiXBiT.">
<h1>Sistemas de refrigeración por inmersión para mineros ASIC</h1>
```

- **Сначала дочистить перевод** (смесь языков). Description сейчас **пустой**. Состав решения (tanques, líquido, circuito) — [VERIFY] по EN-странице.

### `/es/asics-cooling/hydro-systems` (**сначала дочистить перевод**)

- **Основной ключ:** refrigeración líquida asic. **Вторичные:** antminer hydro, whatsminer hydro, refrigeración líquida minería.
- **Сейчас:** title «Sistemas de Refrigeración Hidroeléctrica» (40 зн.); description 0 зн.; H1 «Sistemas de Refrigeración Hidroeléctrica».

```html
<title>Refrigeración líquida (hidro) para mineros ASIC | BiXBiT</title>
<meta name="description" content="Refrigeración líquida (hidro) para ASIC Antminer y Whatsminer con enfriamiento por agua: racks y contenedores de BiXBiT para granjas de minería de Bitcoin.">
<h1>Sistemas de refrigeración líquida (hidro) para mineros ASIC</h1>
```

- **Сначала дочистить перевод.** H1 «Hidroeléctrica» — ошибка (это «гидроэлектрический»), заменить. Description **пустой**. Racks/contenedores hydro — [VERIFY]: `/es/products/rack-hydro` и `container-hydro` сейчас 404, ссылаться на EN или не ссылаться.

### `/es/products/pdu` (переведена, можно ставить)

- **Основной ключ:** pdu minería [n/d]. **Вторичные:** pdu inteligente, pdu administrable, pdu para minería.
- **Сейчас:** title «» (0 зн.); description 0 зн.; H1 «BiXBiT Smart PDU».

```html
<title>PDU inteligente para minería ASIC | BiXBiT Smart PDU</title>
<meta name="description" content="BiXBiT Smart PDU: unidad de distribución de energía administrable para granjas de minería con ASIC. Control remoto de tomas y monitoreo del consumo.">
<h1>BiXBiT Smart PDU: distribución de energía para minería ASIC</h1>
```

- Title и description сейчас **пустые**. Функции (control remoto de tomas, monitoreo del consumo) — [VERIFY] по `/en/products/pdu`. Напряжение и ток (например, 380 V) в мету не добавлять без спеки.

### `/es/products/server` (**сначала перевод**)

- **Основной ключ:** — (ES-спрос не измерен). **Вторичные:** refrigeración por inmersión para servidores, centros de datos.
- **Сейчас:** title «Refrigeración por inmersión BiXBiT para servidores y centros de datos» (69 зн.); description 174 зн.; H1 «Prefab Data Centers Cooling Solutions».

```html
<title>Refrigeración por inmersión para servidores | BiXBiT</title>
<meta name="description" content="Refrigeración por inmersión de BiXBiT para servidores y centros de datos: menor consumo en refrigeración, más vida útil del hardware y reutilización del calor.">
<h1>Refrigeración por inmersión para servidores y centros de datos</h1>
```

- **Сначала перевод** (тело и H1 на EN). Мета сохраняет смысл текущего ES description, но короче (сейчас 179 зн.).

### `/es/faq` (переведена, можно ставить)

- **Основной ключ:** — (служебная). **Вторичные:** comisión de desarrollo transparente, firmware, AMS.
- **Сейчас:** title «FAQ preguntas frecuentes» (24 зн.); description 94 зн.; H1 «».

```html
<title>Preguntas frecuentes: firmware, AMS y refrigeración | BiXBiT</title>
<meta name="description" content="Respuestas sobre el firmware BiXBiT para Antminer y Whatsminer, la comisión de desarrollo transparente, el monitoreo AMS y los sistemas de refrigeración.">
<h1>Preguntas frecuentes</h1>
```

- Не коммерческая, но здесь честнее всего дать нейтральный ответ про dev fee: «comisión de desarrollo transparente» + [VERIFY: tarifa actual]. До перевода ответа сверить противоречие на EN FAQ (1.8–2.8% против 2.8% / 2%). Текущий description — шаблонная заглушка (99 зн.).

## Не делаем сейчас

- `/es/documentation`: пустой хаб (55 слов) с пустым FAQPage. Мету не трогаем; по hreflang-spec — `noindex` до наполнения [VERIFY решение].
- `/es/about`, `/es/contacts`: не коммерческие, мета приемлемая; менять при общем проходе по локали.
- Новые страницы (`/es/firmwares/comparison`, `/es/firmwares/dev-fee`, `/es/ams/comparison`, ES-документация): мета после EN-версий и утверждения слагов.

## Проверка перед выкладкой

1. `./scripts/page-snapshot.py --urls <ES URL через запятую> --out data/page-snapshot-es-<дата>.json --compare <предыдущий снимок>`: title, description и H1 изменились, canonical прежний.
2. Длины при правках пересчитать: title ≤ 60, description 140–160.
3. В ES-шаблонах нет «sin comisión», «gratis», «0 %».
4. После перевода Whatsminer и охлаждения включить эти URL в hreflang-кластеры и sitemap (`content/hreflang-spec.md` §6.1) и прогнать `./scripts/hreflang-check.py <снимок> --langs en,ru,es`.
