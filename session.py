import os

os.system("pip3 install tgcrypto pyrogram")
os.system("clear")
from pyrogram import Client

# guide them

intro = """
@V_VIP_OWNER ᴄᴏʀᴘᴏʀᴀᴛɪᴏɴ
ɢᴇᴛ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʟᴜᴇs ʙʏ ʟᴏɢɢɪɴɢ ᴛᴏ,

https://my.telegram.org

Required:
  
  1. API_ID
  2. API_HASH
  3. PHONE NUMBER (WITH COUNTRY CODE)
  
"""


print(intro)


API_ID = input("\nEnter your API_ID: ")

while not (API_ID.isdigit() and len(API_ID) == 7):
    print("\n\nPlease enter a 7 digit API_ID.\n\n")
    API_ID = input("Enter your API_ID (1234567): ")


# hexadecimal number
API_HASH = input("\nEnter API HASH: ")


# create a new pyrogram session
with Client("in_memory=True", api_id=int(API_ID), api_hash=API_HASH) as app:
    app.send_message(
        "me",
        f"ᴛʜɪs ɪs ʏᴏᴜʀ sᴀɴᴀᴛᴀɴɪ ᴜsᴇʀʙᴏᴛ • [ `SESSION` ]\n\n```{app.export_session_string()}```\n\n⚠️• ᴅᴏɴ'ᴛ sʜᴀʀᴇ ᴛʜɪs ᴡɪᴛʜ ᴀɴʏᴏɴᴇ !!\n\n ᴄʀᴇᴀᴛᴇ ᴀɢᴀɪɴ •)",
        disable_web_page_preview=True,
    )
    print(
        "ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ sᴀᴠᴇᴅ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ sᴀᴠᴇᴅ (ᴄʟᴏᴜᴅ) ᴍᴇssᴀɢᴇs !! ᴅᴏɴ'ᴛ sʜᴀʀᴇ ɪᴛ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ!! ᴀɴʏᴏɴᴇ ʜᴀᴠɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴄᴀɴ ᴜsᴇ (ʜᴀᴄᴋ) ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ !"
    )
