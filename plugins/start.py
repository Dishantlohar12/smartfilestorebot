from pyrogram import Client, filters

START_TEXT = '''
Welcome to the Educational Resource Bot.

Options:
• Upload notes (teachers)
• Search study materials
• Download subject files
'''

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(START_TEXT)