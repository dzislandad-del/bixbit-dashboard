---
description: Построить топик-кластер из seed-темы — семантика, hub-and-spoke, брифы, матрица перелинковки.
argument-hint: "[seed тема, напр. 'Antminer firmware']"
---

Построй топик-кластер вокруг seed-темы: **$ARGUMENTS**. Действуй по `RUNBOOK.md`/`CLAUDE.md` и `docs/agent-knowledge.md` (актуальные факты и особенности данных).
Помни приоритет тем (CLAUDE.md §3): firmware Antminer/Whatsminer — первыми, затем
cooling, monitoring, PDU.

## Шаги (делегирует `content-seo`)
1. Расширь семантику от seed (skills `seo-cluster`, `searchfit-seo:keyword-clustering`).
   Объёмы/частотности — **только из DataForSEO** (US + нужные рынки; СНГ — Kazakhstan 2398, Labs не знает RU/BY),
   для n/d — показы из GSC (`./scripts/gsc-query.py`). Нет доступа → скажи, не выдумывай.
   Приоритет — не по объёму: CPC, текущая позиция, GEO-разрыв, показы GSC (урок `reports/cluster-repriorization-2026-09-25.md`).
2. SERP-overlap кластеризация + классификация интента (informational/commercial/transactional).
3. Спроектируй **hub-and-spoke**: 1 pillar + spokes. **Сначала сопоставь с существующими URL**
   (`data/site-structure.md`) — оптимизировать живую страницу лучше, чем плодить дубль. Тонкие споки с n/d —
   секцией, а не отдельным URL. Учти дыры конкурентов (Braiins, Vnish, ePIC, EMCD, Awesome Miner).
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

## После кластера
Предложи 3–5 ключей кластера в `data/rank-tracking/keywords.md` (утверждает человек), чтобы `/rank-check` их отслеживал.
