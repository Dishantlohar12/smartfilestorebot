from database import users

async def set_role(user_id, role):
    await users.update_one(
        {"user_id": user_id},
        {"$set": {"role": role}},
        upsert=True
    )

async def get_role(user_id):
    user = await users.find_one({"user_id": user_id})
    if user:
        return user.get("role", "student")
    return "student"