from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from ... import app, SUDO_USER, spam_chats
from ... import *

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@app.on_message(cdz(["utag"]) & (filters.me | filters.user(SUDO_USER)))
async def mentionall(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**❍ sᴇɴᴅ ᴍᴇ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ..!**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 4:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(cdz(["cancel"]) & (filters.me | filters.user(SUDO_USER)))
async def cancel_spam(client: Client, message: Message):
    if not message.chat.id in spam_chats:
        return await message.edit("**❍ ɪᴛ sᴇᴇᴍs ᴛʜᴇʀᴇ ɪs ɴᴏ ᴛᴀɢᴀʟʟ ʜᴇʀᴇ.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**❍ ᴄᴀɴᴄᴇʟʟᴇᴅ.**")


__NAME__ = "Tᴀɢᴀʟʟ"
__MENU__ = """
`.utag` - **.utag (ᴍᴇssᴀɢᴇ) - ᴛᴏ sᴛᴀʀᴛ ᴜsᴇʀᴛᴀɢɢᴇʀ**
`.cancel` - **ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢᴇʀ**
`.tagall` - **.tagall - ᴛᴏ sᴛᴀʀᴛ ᴛᴀɢᴀʟʟ**
`.tagallstop` - **ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢᴇʀ**
`.vctag` - **ᴠᴏɪᴄᴇ ᴍsɢ ᴛᴀɢᴀʟʟ**
`.vctagstop` - **ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢᴇʀ**
.gntag` - **ɢᴏᴏᴅ ɴɪɢʜᴛ ᴍsɢ ᴛᴀɢᴀʟʟ**
`.gntop` - **ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢᴇʀ**
`.gmtag` - **ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛᴀɢᴀʟʟ**
`.gmstop` - **ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢᴇʀ**
`.shayari` - **ɢᴏᴏᴅ ɴɪɢʜᴛ ᴍsɢ ᴛᴀɢᴀʟʟ**
`.shayaristop` - **ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢᴇʀ**

"""
