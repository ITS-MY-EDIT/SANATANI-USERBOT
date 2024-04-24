from pyrogram import filters, Client
from pyrogram.types import *
import os
import sys
import asyncio
from random import choice
OWNER_ID = 5959548791
from pyrogram import Client, filters
from pyrogram.types import Message
from SHUKLA.modules.SHASHANK.data import *
from ... import app, SUDO_USER
from ... import *

SUDO_USERS = SUDO_USER
Usage = f"**❍ ᴡʀᴏɴɢ ᴜsᴀɢᴇ ** \n ❍ ᴛʏᴘᴇ : `.help dmspam`"


@app.on_message(cdz(["dmraid"])  & (filters.me | filters.user(SUDO_USER))
)
async def dmraid(xspam: Client, e: Message):
      """ Module: Dm Raid """
      Zaid = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Zaid) == 2:
          ok = await xspam.get_users(Zaid[1])
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"❍ ᴛʜɪs ɪs ᴠᴇʀɪғɪᴇᴅ ᴜsᴇʀ..!!"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"❍ ᴛʜɪs ɪs sᴜᴅᴏ ᴜsᴇʀ -:- ᴍʏ ᴏᴡɴᴇʀ..!!"
                await e.reply_text(text)
          else:
              counts = int(Zaid[0])
              await e.reply_text("`❍ ᴅᴍ ʀᴀɪᴅ sᴛʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"❍ ᴛʜɪs ɪs ᴠᴇʀɪғɪᴇᴅ ᴜsᴇʀ...!!"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"❍ ᴛʜɪs ɪs sᴜᴅᴏ ᴜsᴇʀ -:- ᴍʏ ᴏᴡɴᴇʀ..!!"
                await e.reply_text(text)
          else:
              counts = int(Zaid[0])
              await e.reply_text("❍ ᴅᴍ ʀᴀɪᴅ sᴛʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)

@app.on_message(cdz(["dmspam"])  & (filters.me | filters.user(SUDO_USER))
)
async def dmspam(spam: Client, e: Message):
      text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      Zaid = text[1:]
      if len(Zaid) == 2:
          msg = str(Zaid[1])
          ok = await spam.get_users(text[0])
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"❍ ᴛʜɪs ɪs ᴠᴇʀɪғɪᴇᴅ ᴜsᴇʀ..!!"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"❍ ᴛʜɪs ɪs sᴜᴅᴏ ᴜsᴇʀ -:- ᴍʏ ᴏᴡɴᴇʀ..!!"
                await e.reply_text(text)
          else:
              counts = int(Zaid[0])
              await e.reply_text("❍ ᴅᴍ sᴘᴀᴍ sᴛʀᴀᴛᴇᴅ")
              for _ in range(counts):
                    await spam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await spam.get_users(user_id)
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"❍ ᴛʜɪs ɪs ᴠᴇʀɪғɪᴇᴅ ᴜsᴇʀ..!!"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"❍ ᴛʜɪs ɪs sᴜᴅᴏ ᴜsᴇʀ -:- ᴍʏ ᴏᴡɴᴇʀ..!!"
                await e.reply_text(text)
          else:
              counts = int(text[0])
              msg = str(Zaid[0])
              await e.reply_text("❍ ᴅᴍ sᴘᴀᴍ sᴛʀᴀᴛᴇᴅ")
              for _ in range(counts):
                    await spam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("❍ ᴜsᴀɢᴇ : .ᴅᴍsᴘᴀᴍ ᴜsᴇʀɴᴀᴍᴇ ᴄᴏᴜɴᴛ ᴍᴇssᴀɢᴇ")





__NAME__ = " Dᴍ Rᴀɪᴅs "
__MENU__ = """
`.dmraid` - **ᴄʜᴇᴄᴋ ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ
ᴏғ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ sᴇʀᴠᴇʀ.**

`.alive` - **ᴄʜᴇᴄᴋ ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ
ᴏғ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ sᴇʀᴠᴇʀ.**
"""
