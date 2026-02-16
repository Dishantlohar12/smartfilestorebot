from pyrogram import Client, filters
from plugins.roles import get_role
from database import files

ALLOWED_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation"
]

@Client.on_message(filters.document)
async def upload_file(client, message):
    role = await get_role(message.from_user.id)

    if role not in ["teacher", "admin"]:
        await message.reply("Only teachers can upload files.")
        return

    doc = message.document

    if doc.mime_type not in ALLOWED_TYPES:
        await message.reply("Only PDF, DOC, and PPT files allowed.")
        return

    await files.insert_one({
        "file_id": doc.file_id,
        "file_name": doc.file_name,
        "uploader": message.from_user.id
    })

    await message.reply("File uploaded successfully.")