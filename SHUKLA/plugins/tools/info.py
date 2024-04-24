from asyncio import gather
from os import remove

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
from ... import *
from SHUKLA.modules.SHASHANK.PyroHelpers import ReplyCheck
from SHUKLA.plugins.tools.profile import extract_user



@app.on_message(cdz(["info"]) & filters.me)
async def who_is(client: Client, message: Message):
    user_id = await extract_user(message)
    ex = await message.edit_text("`❍ ᴘʀᴏᴄᴇssɪɴɢ . . .`")
    if not user_id:
        return await ex.edit(
            "**❍ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ɢᴇᴛ ᴛʜᴀᴛ ᴜsᴇʀ ɪɴғᴏ.**"
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""<b>❍ 𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡:</b>

❍ <b>ᴜsᴇʀ ɪᴅ :</b> <code>{user.id}</code>
❍ <b>ғɪʀsᴛ ɴᴀᴍᴇ :</b> {first_name}
❍ <b>ʟᴀsᴛ ɴᴀᴍᴇ :</b> {last_name}
❍ <b>ᴜsᴇʀɴᴀᴍᴇ :</b> {username}
❍ <b>ᴅᴄ ɪᴅ :</b> <code>{dc_id}</code>
❍ <b>ɪs ʙᴏᴛ :</b> <code>{user.is_bot}</code>
❍ <b>ɪs sᴄᴀᴍ :</b> <code>{user.is_scam}</code>
❍ <b>ʀᴇsᴛʀɪᴄᴛᴇᴅ :</b> <code>{user.is_restricted}</code>
❍ <b>ᴠᴇʀɪғɪᴇᴅ :</b> <code>{user.is_verified}</code>
❍ <b>ᴘʀᴇᴍɪᴜᴍ :</b> <code>{user.is_premium}</code>
❍ <b>ᴜsᴇʀ ʙɪᴏ :</b> {bio}

❍ <b>sᴀᴍᴇ ɢʀᴏᴜᴘs sᴇᴇɴ :</b> {len(common)}
❍ <b>ʟᴀsᴛ sᴇᴇɴ :</b> <code>{status}</code>
❍ <b>ᴜsᴇʀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ :</b> <a href='tg://user?id={user.id}'>{fullname}</a>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                ex.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await ex.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await ex.edit(f"**❍ ɪɴғᴏ:** `{e}`")


@app.on_message(cdz(["chatinfo"]) & filters.me)
async def chatinfo_handler(client: Client, message: Message):
    ex = await message.edit_text("`❍ ᴘʀᴏᴄᴇssɪɴɢ...`")
    try:
        if len(message.command) > 1:
            chat_u = message.command[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await message.edit(
                    f"❍ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜɪɴ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴜsᴇ ᴄʜᴀᴛɪɴғᴏ [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ]`"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""<b>❍ 𝗖𝗛𝗔𝗧 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡:</b>

❍ <b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{chat.id}</code>
❍ <b>ᴛɪᴛʟᴇ :</b> {chat.title}
❍ <b>ᴜsᴇʀɴᴀᴍᴇ :</b> {username}
❍ <b>ᴛʏᴘᴇ :</b> <code>{type}</code>
❍ <b>ᴅᴄ ɪᴅ :</b> <code>{dc_id}</code>
❍ <b>ɪs sᴄᴀᴍ :</b> <code>{chat.is_scam}</code>
❍ <b>ɪs ғᴀᴋᴇ :</b> <code>{chat.is_fake}</code>
❍ <b>ᴠᴇʀɪғɪᴇᴅ :</b> <code>{chat.is_verified}</code>
❍ <b>ʀᴇsᴛʀɪᴄᴛᴇᴅ :</b> <code>{chat.is_restricted}</code>
❍ <b>ᴘʀᴏᴛᴇᴄᴛᴇᴅ :</b> <code>{chat.has_protected_content}</code>

❍ <b>ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs :</b> <code>{chat.members_count}</code>
❍ <b>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ :</b>
<code>{description}</code>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                ex.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await ex.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await ex.edit(f"**❍ 𝗜𝗡𝗙𝗢:** `{e}`")




__NAME__ = " Iɴғᴏ "
__MENU__ = """
`.info` **ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀ ɪɴғᴏ ᴡɪᴛʜ ғᴜʟʟ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.**
`.chatinfo` **ɢᴇᴛ ɢʀᴏᴜᴘ ɪɴғᴏ ᴡɪᴛʜ ғᴜʟʟ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.**
`.id` ** ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀ ɪᴅ ᴅᴇᴛᴀɪʟ**
"""
