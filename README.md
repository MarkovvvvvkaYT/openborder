# Openborder

Openborder is an educational Telegram bot from the Movavi Python course. It helps a small community navigate course information and stores user roles in a local SQLite database.

## What it demonstrates

- Telegram menus and callback buttons with `pyTelegramBotAPI`;
- role-based flows for tutors and teachers;
- SQLite persistence for user roles;
- Docker-based local deployment;
- environment-based secret management.

## Stack

Python · pyTelegramBotAPI · SQLite · Docker

## Run with Docker

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Set `TELEGRAM_BOT_TOKEN` in `.env`.
3. Start the bot:

   ```bash
   docker compose up --build
   ```

The SQLite database is created at `static/data.db` on first run. The `static/` folder is mounted as a volume so local data survives container restarts.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN='your-token'  # PowerShell
python main.py
```

Set `DATABASE_PATH` if you want to store the local database elsewhere.

## Security and project status

Real tokens, databases, logs and Python cache files are intentionally excluded from Git. This is a course/portfolio project; the bot is not presented as a production service.

---

# Openborder — русская версия

Учебный Telegram-бот из курса Movavi. Он показывает меню для кураторов и преподавателей, хранит роли пользователей в локальной SQLite-базе и запускается в Docker.

Скопируйте `.env.example` в `.env`, задайте `TELEGRAM_BOT_TOKEN` и выполните `docker compose up --build`. Настоящие токены, базы и кэш Python в репозиторий не попадают.