from pyrogram import Client, filters
from database import files

@Client.on_message(filters.command("files"))
async def list_files(client, message):
    text = "Available files:\n\n"
    async for f in files.find():
        text += f["file_name"] + "\n"

    await message.reply(text or "No files available.")