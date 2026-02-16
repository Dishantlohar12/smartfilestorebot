from database import subjects

async def add_subject(name):
    await subjects.insert_one({"name": name})

async def list_subjects():
    result = []
    async for s in subjects.find():
        result.append(s["name"])
    return result