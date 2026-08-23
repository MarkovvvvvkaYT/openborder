import os

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ADMINS = [6734010707, 5159190765]
db_name = os.getenv("DATABASE_PATH", "static/data.db")
os.makedirs(os.path.dirname(db_name) or ".", exist_ok=True)