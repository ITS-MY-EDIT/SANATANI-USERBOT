from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["rsm", "resume"]) & ~filters.private)
@sudo_users_only
async def resume_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a.status == "paused":
            await call.resume_stream(chat_id)
            await eor(message, "**❍ sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ..!**")
        elif a.status == "playing":
            await eor(message, "**❍ ᴀʟʀᴇᴀᴅʏ ᴘʟᴀʏɪɴɢ..!**")
        elif a.status == "not_playing":
            await eor(message, "**❍ ɴᴏᴛʜɪɴɢ sᴛʀᴇᴀᴍɪɴɢ..!**")
    except GroupCallNotFound:
        await eor(message, "**❍ ɪ ᴀᴍ ɴᴏᴛ ɪɴ ᴠᴄ..!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["crsm", "cresume"]))
@sudo_users_only
async def resume_stream_chat(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**❍ ɴᴏ sᴛʀᴇᴀᴍ ᴄʜᴀᴛ sᴇᴛ**"
    )
    try:
        a = await call.get_call(chat_id)
        if a.status == "paused":
            await call.resume_stream(chat_id)
            await eor(message, "**❍ sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ..!**")
        elif a.status == "playing":
            await eor(message, "**❍ ᴀʟʀᴇᴀᴅʏ ᴘʟᴀʏɪɴɢ..!**")
        elif a.status == "not_playing":
            await eor(message, "**❍ ɴᴏᴛʜɪɴɢ sᴛʀᴇᴀᴍɪɴɢ..!**")
    except GroupCallNotFound:
        await eor(message, "**❍ ɪ ᴀᴍ ɴᴏᴛ ɪɴ ᴠᴄ..!**")
    except Exception as e:
        print(f"Error: {e}")

  
