from pyrogram import filters
from strings import get_command
from BlinkMusix import app
from BlinkMusix.misc import SUDOERS

# Commands
ID_COMMAND = "/id"

@app.on_message(filters.command(ID_COMMAND))
async def id_command(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await message.reply_text(f"Your user ID: {user_id}\nThis chat's ID: {chat_id}")
