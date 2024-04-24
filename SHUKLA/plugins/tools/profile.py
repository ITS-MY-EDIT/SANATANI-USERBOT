import os
from asyncio import sleep
import os
import sys
from re import sub
from time import time
from ... import app, SUDO_USER
from ... import *

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from ... import *
from SHUKLA.modules.SHASHANK.PyroHelpers import ReplyCheck


flood = {}
profile_photo = "cache/pfp.jpg"


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]

@app.on_message(cdz(["unblock"]) & (filters.me | filters.user(SUDO_USER))
)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`❍ ᴘʀᴏᴄᴇssɪɴɢ . . .`")
    if not user_id:
        return await message.edit(
            "❍ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜɴʙʟᴏᴄᴋ."
        )
    if user_id == client.me.id:
        return await tex.edit("❍ ᴏᴋ ᴅᴏɴᴇ.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴʙʟᴏᴄᴋᴇᴅ** {umention}")

@app.on_message(cdz(["block"]) & (filters.me | filters.user(SUDO_USER))
)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`❍ ᴘʀᴏᴄᴇssɪɴɢ . . .`")
    if not user_id:
        return await tex.edit_text(
            "❍ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʟᴏᴄᴋ."
        )
    if user_id == client.me.id:
        return await tex.edit_text("❍ ᴏᴋ ᴅᴏɴᴇ")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ʙʟᴏᴄᴋᴇᴅ** {umention}")


@app.on_message(cdz(["setname"]) & (filters.me | filters.user(SUDO_USER))
)
async def setname(client: Client, message: Message):
    tex = await message.reply_text("`❍ ᴘʀᴏᴄᴇssɪɴɢ . . .`")
    if len(message.command) == 1:
        return await tex.edit(
            "❍ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʏᴏᴜʀ ɴᴀᴍᴇ."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(f"**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʏᴏᴜʀ ɴᴀᴍᴇ ᴛᴏ** `{name}`")
        except Exception as e:
            await tex.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
    else:
        return await tex.edit(
            "❍ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʏᴏᴜʀ ɴᴀᴍᴇ."
        )

@app.on_message(cdz(["setbio"]) & (filters.me | filters.user(SUDO_USER))
)
async def set_bio(client: Client, message: Message):
    tex = await message.edit_text("`❍ ᴘʀᴏᴄᴇssɪɴɢ . . .`")
    if len(message.command) == 1:
        return await tex.edit("❍ ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʙɪᴏ.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʙɪᴏ ᴛᴏ** `{bio}`")
        except Exception as e:
            await tex.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
    else:
        return await tex.edit("❍ ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʙɪᴏ.")


@app.on_message(cdz(["setpfp"]) & (filters.me | filters.user(SUDO_USER))
)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("**❍ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.**")
    else:
        await message.reply_text(
            "❍ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ sᴇᴛ ᴀs ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ"
        )
        await sleep(3)
        await message.delete()


@app.on_message(cdz(["ypfp"]) & (filters.me | filters.user(SUDO_USER))
)
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.reply_text("❍ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ ɴᴏᴛ ғᴏᴜɴᴅ..!")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)



__NAME__ = "Pʀᴏғɪʟᴇ"
__MENU__ = """
`.block` **ᴛᴏ ʙʟᴏᴄᴋ sᴏᴍᴇᴏɴᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ**
`.unblock` **ᴛᴏ ᴜɴʙʟᴏᴄᴋ sᴏᴍᴇᴏɴᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ**
`.setname` **sᴇᴛ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ɴᴀᴍᴇ.**
`.setpfp` **ʀᴇᴘʟʏ ᴡɪᴛʜ ɪᴍᴀɢᴇ ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘɪᴄ.**
`.vpfp` **
`.setbio` **sᴇᴛ ᴀɴ ʙɪᴏ.**ʀᴇᴘʟʏ ᴡɪᴛʜ ᴠɪᴅᴇᴏ ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ.***   
"""
