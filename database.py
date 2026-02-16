from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)
db = client.education_bot

users = db.users
files = db.files
subjects = db.subjects