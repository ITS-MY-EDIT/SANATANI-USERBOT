import os
import shutil
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from ... import app, SUDO_USER
from ... import *

@app.on_message(cdz(["restart"]) & (filters.me | filters.user(SUDO_USER)))
async def restart(client: Client, message: Message):
    reply = await message.reply_text("**ʀᴇsᴛᴀʀᴛɪɴɢ...**")
    await message.delete()
    await reply.edit_text("sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ sᴀɴᴀᴛᴀɴɪ ʙᴏᴛ...\n\n ᴡᴀɪᴛ 1-2 ᴍɪɴᴜᴛᴇs\n ʟᴏᴀᴅ ᴘʟᴜɢɪɴs...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m SACHINxSANATANI")
  

__NAME__ = "Rᴇsᴛᴀʀᴛ"
__MENU__ = """
`.restart` **ʜᴇʀᴏᴋᴜ ʙᴏᴛ ʀᴇsᴛᴀʀᴛ **
`.upload` **ᴜᴘʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ sʏsᴛᴇᴍ ғɪʟᴇ ᴘᴀᴛʜ**
"""
