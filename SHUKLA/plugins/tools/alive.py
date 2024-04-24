import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from ... import app, SUDO_USER
from ... import *

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@app.on_message(cdz(["alive"])  & (filters.me | filters.user(SUDO_USER)))
async def alive(client: Client, message: Message):
    r = await message.reply_text("**🇸ᴀ ɴ ᴀ ᴛ ᴀ ɴ ɪ ₰**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f" 𝗦𝝙𝗡𝝙𝗧𝝙𝗡𝗜 || 𝗦𝗣𝝙𝗠 \n\n"
        f"ᴠᴇʀsɪᴏɴ ➠ 2.0.1\n"
        f"ᴘɪɴɢ  ➠ {ping * 1000:.3f}ᴍs\n"
        f"ᴜᴘᴛɪᴍᴇ ➠ {uptime}\n"
        f"ᴘʏᴛʜᴏɴ ➠ {python_version()}`\n"
        f"ᴘʏʀᴏɢʀᴀᴍ ➠ {__version__}\n"
        f"ᴏᴡɴᴇʀ ➠ {client.me.mention}"    
    )

@app.on_message(cdz(["ping"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("** 𝗦𝝙𝗡𝝙𝗧𝝙𝗡𝗜 || 𝗦𝗣𝝙𝗠 **")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f" 𝗦𝝙𝗡𝝙𝗧𝝙𝗡𝗜 || 𝗦𝗣𝝙𝗠 \n\n"
        f"ᴘɪɴɢ  ➠ {ping * 1000:.3f}ᴍs\n"
        f"ᴜᴘᴛɪᴍᴇ  ➠ {uptime}\n"
        f"ᴏᴡɴᴇʀ ➠ {client.me.mention}\n"
              )
@app.on_message(cdz(["ISSSSSSSrepo"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**𝐑ᴇᴘᴏ**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"𝗥𝗘𝗣𝗢 ➠\n\n"
        f"[✦ ʀᴇᴘᴏ ✦](https://t.me/all_sanatani_bot)\n"
    )    


__NAME__ = " Aᴄᴛɪᴠᴇ "
__MENU__ = """
`.ping` - **ᴄʜᴇᴄᴋ ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ
ᴏғ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ sᴇʀᴠᴇʀ.**

`.alive` - **ᴄʜᴇᴄᴋ ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ
ᴏғ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ sᴇʀᴠᴇʀ.**
"""
