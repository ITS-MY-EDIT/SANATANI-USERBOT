import asyncio
from ... import *
from pyrogram import Client, filters
from pyrogram.types import Message

from SHUKLA.modules.SHASHANK.utility import get_arg



@app.on_message(filters.me & filters.command(["q", "quotly"], "."))
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**❍ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ**")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("`❍ ᴍᴀᴋɪɴɢ ᴀ ǫᴜᴏᴛᴇ . . .`")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**❍ ғᴀɪʟᴇᴅ ᴛᴏ ᴄʀᴇᴀᴛᴇ ǫᴜᴏᴛʟʏ sᴛɪᴄᴋᴇʀ**")





__NAME__ = "Qᴜᴏʟᴛʏ"
__MENU__ = """
`.q` - **ᴍᴀᴋᴇ ᴀ ᴍᴇssᴀɢᴇ ɪɴᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴡɪᴛʜ ᴛʜᴇ ᴄᴜsᴛᴏᴍ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴄᴏʟᴏʀ ɢɪᴠᴇɴ.**

"""
