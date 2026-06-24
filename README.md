# BiXBiT SEO Automation (Claude Code)

AI-управляемая система SEO-автоматизации для **bixbit.io/en** — B2B-ниша:
прошивки для ASIC (Antminer, Whatsminer), промышленное охлаждение, мониторинг.

Цель: закрыть максимум задач SEO-специалиста автономно через субагентов и
команды Claude Code.

## Быстрый старт

```bash
# 1. Клонируй в репозиторий проекта (или отдельный repo)
cp -r bixbit-seo/ /path/to/your/project/

# 2. Установи Claude Code
npm install -g @anthropic-ai/claude-code

# 3. Настрой доступы
cp .env.example .env   # заполни ключи GSC / GA4 / DataForSEO / PageSpeed

# 4. Подключи DataForSEO MCP (пример)
claude mcp add dataforseo -- npx -y dataforseo-mcp-server

# 5. Запусти Claude Code в папке проекта
claude

# 6. Первый запуск
> Прочитай RUNBOOK.md и выполни первичную настройку
> /full-audit
```

## Структура

```
.
├── CLAUDE.md                 # Контекст бренда/ICP/правила (грузится авто)
├── RUNBOOK.md                # Инструкция для Claude: как действовать
├── .claude/
│   ├── agents/               # 6 субагентов под зоны SEO
│   ├── commands/             # 6 слэш-команд
│   └── settings.json         # Разрешения инструментов
├── .github/workflows/        # Автоматизация по расписанию + PR-проверки
├── data/                     # Снапшоты/baseline, структура сайта
├── content/                  # Кластеры, брифы, контент-план
└── reports/                  # Аудиты и отчёты
```

## Команды

| Команда | Назначение |
|---|---|
| `/full-audit` | Полный аудит: technical + content + backlinks + GEO |
| `/page-optimize [url] [kw]` | On-page оптимизация страницы |
| `/new-cluster [тема]` | Топик-кластер → брифы → перелинковка |
| `/weekly-drift` | Drift-мониторинг регрессий |
| `/competitor-gap [конкурент]` | Gap против Braiins/Vnish/LuxOS/ePIC |
| `/geo-check` | AI-видимость бренда в LLM |

## Важно
- Система **не выдумывает данные** — нужны реальные доступы к GSC/GA4/DataForSEO.
- Тех-факты о прошивках помечаются `[VERIFY]` для проверки человеком.
- Только белые методы SEO.

См. `RUNBOOK.md` для деталей и `CLAUDE.md` для контекста.
