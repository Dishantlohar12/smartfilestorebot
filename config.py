import os

API_ID = int(os.getenv("API_ID", "26590590"))
API_HASH = os.getenv("API_HASH", "4805ee1d57b1be7f5135e736c816a2d1")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8563648313:AAEvDqOEyhk3T3TvlTpJLxeGDDGw08_GjTY")

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://nshubh345:1FmseyW0TKaWNMNo@cluster0.pgewb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

ADMINS = [int(x) for x in os.getenv("ADMINS", "5904478052").split() if x]
