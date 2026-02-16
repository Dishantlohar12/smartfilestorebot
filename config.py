import os

API_ID = int(os.getenv("API_ID", "267324"))
API_HASH = os.getenv("API_HASH", "4805ee1d57b1be7f5135e736c816a2d1")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8563648313:AAEvDqOEyhk3T3TvlTpJLxeGDDGw08_GjTY")

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")

ADMINS = [int(x) for x in os.getenv("ADMINS", "").split() if x]
