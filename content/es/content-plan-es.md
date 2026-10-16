# content-plan-es.md: что переводить и создавать на bixbit.io/es

> **Версия:** 2026-09-28. **Владелец:** international-seo, контент совместно с content-seo.
> **Основа:** `content/es/semantic-core-es.md` (ядро), `content/es/meta-tags-es.md` (мета), `content/localization-plan.md` §6–7 (глоссарий, правила перевода, юр-флаги), `content/hreflang-spec.md` (кластеры и sitemap), архитектура v2 (`reports/content-architecture-2026-09-25.md`).
> **Данные:** `data/dfs-es-semantics-2026-09-28.json`, GSC 28 дней (2026-08-29 … 2026-09-25), снимок `/es/` 2026-09-28.
> **Принцип:** существующие URL важнее новых. Новые ES-страницы — только зеркала EN-страниц v2 после их выхода.

---

## 0. Блокер

**Q1 из `content/localization-plan.md`:** `/es/` — публичная локаль или тихий запуск? Кто переводит и делает тех-ревью? Есть ли поддержка и sales на испанском?
Пока решения нет, делать можно только P0-1 (мета на уже переведённых страницах) и P0-4 (ошибки). Остальное ждёт Q1.

---

## 1. Состояние /es/ (снимок 2026-09-28, 17 URL, все 200)

| Группа | URL | Состояние |
|---|---|---|
| Переведены | `/es`, `/es/firmwares`, `/es/firmwares/antminer`, `/es/ams`, `/es/ams/connect`, `/es/asics-cooling`, `/es/faq`, `/es/about`, `/es/contacts` | тело на es; description есть не везде (`/es/asics-cooling` пустой), часть длиннее 160 |
| Переведены, но мета пустые | `/es/products/pdu` | title и description пустые |
| **Не переведены** | `/es/firmwares/whatsminer-all-series`, `-m2x`, `-m3x`, `-m5x`, `-m6x`, `/es/products/server` | title/description/тело на EN, у Whatsminer H1 пустой |
| Смесь языков | `/es/asics-cooling/immersion-systems`, `/es/asics-cooling/hydro-systems` | description пустой; H1 hydro «Hidroeléctrica» — ошибка |
| Пустой хаб | `/es/documentation` | 55 слов, пустой FAQPage |
| 404 | `/es/products/*` (кроме pdu, server), `/es/calc`, `/es/blog`, `/es/sustainability` | — |

hreflang на ES-страницах нет, в sitemap `/es/` нет (hreflang-spec B4).
GSC: 32 клика / 1 030 показов на 11 ES-URL; небрендовые ES-запросы уходят на EN-страницы.

---

## 2. План по приоритетам

### P0 (спринт 1): мета, ошибки, перевод Whatsminer

| # | Задача | Почему | Ключи | Оценка |
|---|---|---|---|---|
| P0-1 | **Мета на переведённых страницах** по `meta-tags-es.md`: `/es`, `/es/firmwares`, `/es/firmwares/antminer`, `/es/ams`, `/es/ams/connect`, `/es/asics-cooling`, `/es/products/pdu`, `/es/faq` | пустые или обрезанные description; бренд VE (170/мес, 720 показов) уходит на `/en` | bixbit, firmware asic, firmware antminer, monitoreo asic, pdu inteligente | content 0.5 дня + dev 0.5 дня [оценка] |
| P0-2 | **Перевести 5 страниц Whatsminer** (`whatsminer-all-series`, `-m2x`, `-m3x`, `-m5x`, `-m6x`), около 650 слов каждая, около 3 250 слов всего (текст шаблона во многом общий) | самый большой ES-разрыв: `whatsminer firmware` 746 показов в VE/AR/CO на поз. 4–5 и 0 кликов; ES-версии сейчас на английском | firmware whatsminer, whatsminer firmware, firmware whatsminer m30s / m50, whatsminer tool | перевод 1.5 дня + тех-ревью 0.5–1 день [оценка] |
| P0-3 | **После P0-2** включить переведённые URL в hreflang-кластеры и sitemap (`hreflang-spec` §6.1); до перевода Whatsminer в кластер **не** включать | без hreflang Google отдаёт LatAm EN/RU-страницы | — | dev: входит в P0-1/P0-4 localization-plan |
| P0-4 | **Ошибки шаблона:** H1 `/es/firmwares` «BiXBiTpara» → «BiXBiT para»; пустой FAQPage на `/es/firmwares` (наполнить или убрать); H1 hydro «Hidroeléctrica» → «refrigeración líquida (hidro)»; H1 `/es/ams/connect` | качество ES-выдачи и schema | — | dev 0.5 дня |

**Правила перевода P0-2** (из localization-plan §6–7):
- `firmware`, `overclocking`, `underclocking`, `ASICBoost`, названия моделей — не переводить; `autotuning` при первом упоминании — «autotuning (ajuste automático)».
- Цифры с EN-страниц («up to 130 Th/s», «up to 90 Th/s», «+40% hashrate») переносятся **как есть** с `[VERIFY]` в брифе перевода. Переводчик их не пересчитывает и не округляет.
- Dev fee: «comisión de desarrollo transparente» `[VERIFY: tarifa actual]` (по аудиту: 2.8%, M2x — 2%; на сайте противоречие, P0-4 dev-task). EN «free download» переводить как «descarga» без «gratis».
- Требования к установке (WhatsMinerTool, версии прошивки) — из EN как есть, `[VERIFY]`.

### P1 (спринты 2–3): усиление существующих страниц и инструкции

| # | Задача | Почему | Ключи | Оценка |
|---|---|---|---|---|
| P1-1 | **`/es/firmwares/antminer`: H2 и FAQ** (около 600–900 новых слов): «Overclocking y underclocking», «Autotuning (ajuste automático)», «Modo de bajo consumo», «Modelos compatibles» [VERIFY], «¿Cómo instalar o actualizar el firmware?» (коротко, со ссылкой на инструкцию), «Comisión de desarrollo transparente» [VERIFY: tarifa actual], FAQ «¿Cuál es el mejor firmware para Antminer?» (без сравнения с конкурентами, только критерии) | в MX мы #6 с EN-страницей; ES-конкурент hashcore.com/es — #3; GSC: `firmware antminer` / `antminer firmware` 314 показов, поз. 10–17 | firmware antminer, overclock antminer (s19, s9), autotuning antminer, underclock / undervolt antminer, antminer modo bajo consumo, firmware antminer s19 / s21 | content 1–1.5 дня + тех-ревью 0.5 дня |
| P1-2 | **Дочистить `/es/asics-cooling/immersion-systems` и `/hydro-systems`**, перевести `/es/products/server` (тело и H1) | смесь языков; единственные ES-страницы под общий спрос `refrigeracion por inmersion` (ES 70, MX 40) | refrigeración por inmersión, tanque de inmersión, refrigeración líquida asic, antminer hydro | перевод около 1.5–2.5k слов [оценка] + тех-ревью 0.5 дня |
| P1-3 | **ES-документация, 1 глава:** «Actualizar el firmware de Whatsminer con WhatsMinerTool» (перевод EN-главы `/en/documentation/user-guide-for-whatsminer-asic/4-1-update-the-firmware-using-the-utility-whatsminertool`) | `whatsminer tool descargar`: 491 показ по сайту, поз. 10–53, только EN; VE — 70/мес по `whatsminer tool` | whatsminer tool, whatsminer tool descargar, actualizar firmware whatsminer | перевод 0.5 дня; **до этого** решить, где живёт документация (P0-5 localization-plan, docs.bixbit.io) и кто переключает slug-и (hreflang из связи переводов в CMS) |
| P1-4 | **`/es/ams`: LSI-блоки** «Monitoreo de temperatura y hashrate», «Alertas», «Gestión remota de la granja», «Compatibilidad con Antminer y Whatsminer» [VERIFY функции по EN] | ES-спрос на мониторинг — бренды конкурентов (`minerstat` 20–90, `hive os` 20–70); родовые n/d. Страница должна отвечать на «software de monitoreo minería» | monitoreo asic, software de monitoreo minería, software de minería, monitoreo de mineros | content 0.5–1 день |
| P1-5 | **Перелинковка внутри /es/**: `/es` → `/es/firmwares`, `/es/firmwares/whatsminer-all-series`, `/es/ams`; `/es/firmwares` ↔ `/antminer` ↔ Whatsminer-хаб ↔ модели; охлаждение → прошивка (режимы для inmersión); прошивка → `/es/ams`. Ссылки только на ES-страницы со статусом 200 и переведённым телом | сейчас ES-страницы почти не связаны; хаб Whatsminer — сирота и в EN | — | content 0.5 дня |
| P1-6 | **Замер ES-позиций:** 8–10 ES-ключей в rank-tracking (MX и VE): firmware antminer, antminer firmware, firmware whatsminer, whatsminer firmware, overclock antminer, whatsminer tool descargar, refrigeracion por inmersion mineria, monitoreo asic, bixbit (VE) | базовая линия до и после P0 | — | около $0.2 за съём (`serp-rank.py`, $0.018/ключ) |

### P2 (квартал): новые страницы после EN v2 и решений команды

| # | Задача | Условие старта | Ключи |
|---|---|---|---|
| P2-1 | `/es/firmwares/comparison`: сравнение прошивок по критериям (dev fee, autotuning, модели, поддержка, мониторинг) | EN-страница вышла, слаг утверждён [VERIFY] | mejor firmware antminer, mejor firmware para antminer s9 [VERIFY: S9], braiins os (ES 20, VE 30), vnish firmware (10–30), luxos firmware, hiveon asic |
| P2-2 | `/es/firmwares/dev-fee`: «Comisión de desarrollo transparente» | EN-страница и ставка подтверждены | comisión de desarrollo, dev fee firmware |
| P2-3 | `/es/ams/comparison` | EN-страница вышла | minerstat, hive os, awesome miner (бренды — в тексте, не в title) |
| P2-4 | ES-страница кодов ошибок Whatsminer | решение P0-5 (docs.bixbit.io, дубли 93–94%) | codigos de error whatsminer, errores whatsminer (VE 30), error whatsminer |
| P2-5 | `/es/documentation/<instalación de firmware Antminer>` | EN-страница v2 вышла | instalar / actualizar firmware antminer, btc tools |
| P2-6 | `/es/products/container` (сейчас 404) | sales подтверждает поставки в LatAm [VERIFY] | contenedor de minería (10 во всех 5 странах) |
| P2-7 | ES-блог | **не рекомендуем** сейчас: ES-спрос информационный и B2C (`mineria de bitcoins` 880), ICP не совпадает | — |

---

## 3. LSI-термины по страницам

Термины из ядра (Google Ads, Labs, GSC) и отраслевая лексика. Писать естественно, без переспама; цифры и модели — только подтверждённые.

| Страница | Основной ключ | LSI и вторичные |
|---|---|---|
| `/es` | bixbit | minería de Bitcoin industrial, granja de minería, firmware ASIC, monitoreo AMS, refrigeración por inmersión, refrigeración líquida (hidro), PDU, Antminer, Whatsminer |
| `/es/firmwares` | firmware asic | firmware personalizado, firmware para ASIC, custom firmware, autotuning (ajuste automático), overclocking, underclocking, eficiencia J/TH, hashrate, comisión de desarrollo transparente, control remoto, descarga del firmware, Antminer, Whatsminer |
| `/es/firmwares/antminer` | firmware antminer | antminer firmware, firmware para antminer, firmware personalizado antminer, Antminer S19 / S19 Pro / S19j Pro / S19 XP / S21 / S21 Pro [VERIFY: список], overclock antminer, underclock, undervolt, modo de bajo consumo, autotuning, eficiencia energética, consumo (W), temperatura de chips, hashboard, ASICBoost [VERIFY], actualizar firmware, instalar firmware, restaurar firmware de fábrica (stock), ruido |
| `/es/firmwares/whatsminer-all-series` | firmware whatsminer | whatsminer firmware, firmware alternativo, M2x / M3x / M5x / M6x, WhatsMinerTool, overclocking, protección contra sobrecalentamiento, ASICBoost, protección contra ataques (hacking), refrigeración por inmersión, actualizar firmware whatsminer |
| `-m2x` / `-m3x` / `-m5x` / `-m6x` | firmware whatsminer + модель | Whatsminer M20S / M21S; M30S / M31S / M32; M50 / M53 / M56; M60 / M63 / M66 [VERIFY: какие модели реально поддерживаются], hashrate TH/s, consumo, modo inmersión, WhatsMinerTool, errores whatsminer |
| `/es/ams` | monitoreo asic | software de monitoreo minería, monitoreo de mineros, software de minería de Bitcoin, gestión de la granja, panel en la nube (dashboard), alertas, temperatura, hashrate, tiempo de inactividad (downtime), control remoto, clave API, Antminer, Whatsminer |
| `/es/ams/connect` | ams bixbit | registro, clave API, conectar equipos, modelos de ASIC |
| `/es/asics-cooling` | refrigeración para minería | enfriamiento de mineros ASIC, refrigeración por inmersión, refrigeración líquida, disipación de calor, temperatura, ruido, granja de minería, rig de minería |
| `/es/asics-cooling/immersion-systems` | refrigeración por inmersión | refrigeración por inmersión para minería / para ASIC, enfriamiento por inmersión, tanque de inmersión, líquido dieléctrico, aceite dieléctrico, intercambiador de calor, torre de enfriamiento / dry cooler [VERIFY состав], overclocking en inmersión, vida útil del equipo |
| `/es/asics-cooling/hydro-systems` | refrigeración líquida asic | refrigeración líquida (hidro), enfriamiento por agua, Antminer Hydro (S19 Hydro, S21 XP Hydro), Whatsminer hydro (M-series hydro) [VERIFY], rack hidro, contenedor hidro, circuito de refrigerante |
| `/es/products/pdu` | pdu minería | PDU inteligente, PDU administrable, unidad de distribución de energía, control remoto de tomas, monitoreo del consumo, reinicio remoto de ASIC [VERIFY функции], trifásico, voltaje / corriente [VERIFY спеки] |
| `/es/products/server` | refrigeración por inmersión para servidores | centros de datos, servidores, eficiencia energética, reutilización del calor, PUE [VERIFY: не давать цифр PUE без подтверждения] |
| `/es/faq` | — | comisión de desarrollo transparente, instalación del firmware, compatibilidad, AMS, garantía [LEGAL-REVIEW] |

**Термины, которых избегаем:** «sin comisión», «gratis» рядом с firmware, «rentabilidad garantizada», «ganancias», «el mejor país para minar», любые обещания по доходности и тарифам на электроэнергию; испанизмы (ordenador, vosotros).

---

## 4. Региональная адаптация (без юр-гарантий)

| Рынок | Что учитываем | Флаг |
|---|---|---|
| Венесуэла | больше всего ES-кликов (140 кликов, 1 144 показа за 28 дней по стране); бренд 170/мес; тема электричества и субсидированных тарифов чувствительна | тарифы, «легальность майнинга», импорт оборудования — **не пишем**; `[LEGAL-REVIEW]` для страниц с оплатой и доставкой |
| Мексика | единственная страна, где `/es` уже получает брендовые клики (9 из 61 показа); ES-конкурент hashcore.com/es в топ-3 | валюта и доставка — `[VERIFY с sales]` |
| Аргентина, Колумбия | спрос почти целиком на англоязычные формулировки (`whatsminer firmware`, `antminer firmware`) | цены в USD `[VERIFY с sales]` |
| Парагвай | 7 кликов / 161 показ; гидроэнергетика — не использовать как рекламный аргумент без проверки | `[LEGAL-REVIEW]` |
| Испания | общий спрос на `refrigeracion por inmersion` (70) выше, чем в LatAm; отдельная версия `es-ES` не нужна | локаль остаётся `es`, нейтральный LatAm-испанский |

Контакты на ES-страницах: честно указать языки поддержки. Если испанского нет, писать EN/RU (localization-plan §6).

---

## 5. Порядок работ и зависимости

```
Q1 (решение команды)
 ├─ P0-1 мета (можно до Q1) ─┐
 ├─ P0-4 ошибки (можно до Q1)┤
 └─ P0-2 перевод Whatsminer ──┴─> P0-3 hreflang + sitemap ─> P1-6 замер позиций
                                   ├─> P1-1 /es/firmwares/antminer
                                   ├─> P1-2 охлаждение + server
                                   ├─> P1-4 /es/ams
                                   └─> P1-5 перелинковка
P0-5 localization-plan (docs.bixbit.io) ─> P1-3 WhatsMinerTool ─> P2-4 коды ошибок
EN v2 (comparison, dev-fee, ams/comparison, install) ─> P2-1…P2-5
```

**Суммарно P0–P1:** около 6–8k слов перевода и нового текста, 2–3 дня тех-ревью, около 1.5 дня dev [оценка].

## 6. Как поймём, что сработало (через 28 и 56 дней после P0-3)

- ES-URL с показами: больше 11 (сейчас 11); клики ES-локали выше 32 за 28 дней.
- `whatsminer firmware` / `firmware whatsminer` в VE/AR/CO: показы на ES-URL вместо EN и CTR выше 0 (сейчас 746 показов и 0 кликов на EN).
- `firmware antminer` (MX, VE): `/es/firmwares/antminer` вместо `/en/firmwares/antminer` в выдаче, позиция не хуже #6 (MX, снимок 2026-09-28, volatile).
- Брендовые запросы из VE: доля кликов на `/es` вместо `/en`.
- Сделки или лиды из LatAm в CRM — `[VERIFY с sales]`: только это подтверждает, что ES-трафик — ICP.

## 7. [VERIFY] для человека

- Q1: статус `/es/`, поддержка и sales на испанском.
- Поддержка Antminer S9 и L7/L9; полный список моделей Antminer и Whatsminer.
- Цифры на живых и переводимых страницах: «hasta 80 Th/s», «10-20%», «up to 130 / 90 Th/s», «+40%».
- Ставка dev fee (2.8%, M2x 2%) и противоречие на EN FAQ.
- Функции PDU и AMS для ES-текстов; состав решений по охлаждению.
- Подозрительно одинаковые показы GSC в VE/AR/CO (возможно, автоматические запросы).
