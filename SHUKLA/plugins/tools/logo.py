from pyrogram.types import Message
import random
from pyrogram import Client, filters, idle
import pyrogram, asyncio, random, time
from pyrogram.errors import FloodWait
from pyrogram.types import *
import requests
from ... import app, SUDO_USER, spam_chats
from ... import *

def calculate_gay_percentage():
    # Simple random gay percentage calculation for fun
    return random.randint(1, 100)


def generate_gay_response(gay_percentage):
    # Define random texts and emojis for different gay percentage ranges
    if gay_percentage < 30:
        return "❍ ʏᴏᴜ'ʀᴇ sᴛʀᴀɪɢʜᴛ ᴀs ᴀɴ ᴀʀʀᴏᴡ"
    elif 30 <= gay_percentage < 70:
        return "❍ ʏᴏᴜ ᴍɪɢʜᴛ ʜᴀᴠᴇ ᴀ ʙɪᴛ ᴏғ ᴀ ʀᴀɪɴʙᴏᴡ ɪɴ ʏᴏᴜ"
    else:
        return "❍ ʏᴏᴜ'ʀᴇ sʜɪɴɪɴɢ ᴡɪᴛʜ ʀᴀɪɴʙᴏᴡ ᴄᴏʟᴏʀs"

@app.on_message(cdz(["kiner"]) & (filters.me | filters.user(SUDO_USER)))
def gay_calculator_command(client, message: Message):
    # Calculate gay percentage
    gay_percentage = calculate_gay_percentage()

    # Generate gay response
    gay_response = generate_gay_response(gay_percentage)

    # Send the gay response as a message
    message.reply_text(f"❍ ɢᴀʏ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ : {gay_percentage}%\n{gay_response}")




@app.on_message(cdz(["logo"]) & (filters.me | filters.user(SUDO_USER)))
async def logo(app, msg: Message):
    if len(msg.command) == 1:
       return await msg.reply_text("❍ ᴜsᴀɢᴇ :\n\n /logo SANATANI")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.sdbots.tech/logohq?text={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}")

@app.on_message(cdz(["animelogo"]) & (filters.me | filters.user(SUDO_USER)))
async def logo(app, msg: Message):
    if len(msg.command) == 1:
       return await msg.reply_text("❍ ᴜsᴀɢᴇ :\n\n /animelogo SANATANI")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.sdbots.tech/anime-logo?name={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}")
  
__NAME__ = "Lᴏɢᴏ"
__MENU__ = """
`.logo` - ***:* .ʟᴏɢᴏ SANATANI.**
`.animelogo` - **.animelogo SANATANU**
`.kiner` - ***:* .ɢᴀʏ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ **
"""
