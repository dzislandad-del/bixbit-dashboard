---
description: Построить топик-кластер из seed-темы — семантика, hub-and-spoke, брифы, матрица перелинковки.
argument-hint: "[seed тема, напр. 'Antminer firmware']"
---

Построй топик-кластер вокруг seed-темы: **$ARGUMENTS**. Действуй по `RUNBOOK.md`/`CLAUDE.md`.
Помни приоритет тем (CLAUDE.md §3): firmware Antminer/Whatsminer — первыми, затем
cooling, monitoring, PDU.

## Шаги (делегирует `content-seo`)
1. Расширь семантику от seed (skills `seo-cluster`, `searchfit-seo:keyword-clustering`).
   Объёмы/частотности — **только из DataForSEO**, нет доступа → скажи, не выдумывай.
2. SERP-overlap кластеризация + классификация интента (informational/commercial/transactional).
3. Спроектируй **hub-and-spoke**: 1 pillar + spokes. Учти дыры конкурентов
   (Braiins, Vnish, LuxOS, ePIC).
4. Сгенерируй **брифы** на pillar и spokes (skill `searchfit-seo:content-brief`):
   интент, структура H1–Hn, целевые сущности/термины, FAQ, E-E-A-T-сигналы,
   внутренние ссылки. Тех-спеки прошивок (J/TH/°C/совместимость) → `[VERIFY: ...]`.
5. Построй **матрицу внутренней перелинковки** кластера (skill `searchfit-seo:internal-linking`).
6. Согласуй с `technical-seo` рекомендованную schema по типам страниц.

## Правила
Технический B2B-английский, без воды, цифры подкреплены или `[VERIFY]`. Никаких
инвест-советов/доходности. Только белые методы.

## Артефакты (в content/)
- `content/clusters/<slug>.md` — карта кластера (hub + spokes, интенты, приоритет).
- `content/briefs/<slug>-*.md` — брифы по каждой странице.
- `content/internal-linking.md` — обновлённая матрица перелинковки.
В чат — структура кластера + что ушло в `[VERIFY]` + что недоступно по данным.
