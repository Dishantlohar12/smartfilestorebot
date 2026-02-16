import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")

ADMINS = [int(x) for x in os.getenv("ADMINS", "").split() if x]