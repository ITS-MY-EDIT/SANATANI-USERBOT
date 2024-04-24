import asyncio
from html import escape

import aiohttp
from pyrogram import filters, Client 
from pyrogram.types import Message
from ... import *

from pyrogram import enums

@app.on_message(cdz(["weather"])   & filters.me)
async def get_weather(bot: Client, message: Message):
    if len(message.command) == 1:
        await message.edit("Usage: `.weather Maldives`")
        await asyncio.sleep(3)
        await message.delete()

    if len(message.command) > 1:
        location = message.command[1]
        headers = {"user-agent": "httpie"}
        url = f"https://wttr.in/{location}?mnTC0&lang=en"
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url) as resp:
                    data = await resp.text()
        except Exception:
            await message.edit("❍ ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ғᴏʀᴇᴄᴀsᴛ")

        if "❍ ᴡᴇ ᴘʀᴏᴄᴇssᴇᴅ ᴍᴏʀᴇ ᴛʜᴀɴ 1ᴍ ʀᴇǫᴜᴇsᴛs ᴛᴏᴅᴀʏ" in data:
            await message.edit("`❍ sᴏʀʀʏ, ᴡᴇ ᴄᴀɴɴᴏᴛ ᴘʀᴏᴄᴇss ᴛʜɪs ʀᴇǫᴜᴇsᴛ ᴛᴏᴅᴀʏ..!`")
        else:
            weather = f"<code>{escape(data.replace('report', 'Report'))}</code>"
            await message.edit(weather, parse_mode=enums.ParseMode.MARKDOWN)


__NAME__ = "Wᴇᴀᴛʜᴇʀ"
__MENU__ = """
`.weather` - **ɢᴇᴛs ᴡᴇᴀᴛʜᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀ ᴘʀᴏᴠɪᴅᴇᴅ ʟᴏᴄᴀᴛɪᴏɴ..**
"""

