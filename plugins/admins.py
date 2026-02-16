from pyrogram import Client, filters
from config import ADMINS
from plugins.roles import set_role

@Client.on_message(filters.command("addteacher") & filters.user(ADMINS))
async def add_teacher(client, message):
    if len(message.command) < 2:
        await message.reply("Usage: /addteacher user_id")
        return

    user_id = int(message.command[1])
    await set_role(user_id, "teacher")
    await message.reply("Teacher added.")

@Client.on_message(filters.command("removeteacher") & filters.user(ADMINS))
async def remove_teacher(client, message):
    if len(message.command) < 2:
        await message.reply("Usage: /removeteacher user_id")
        return

    user_id = int(message.command[1])
    await set_role(user_id, "student")
    await message.reply("Teacher removed.")