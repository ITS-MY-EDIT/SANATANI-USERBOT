# <============================================== IMPORTS =========================================================>
import os
from datetime import datetime

from PIL import Image
from pyrogram import filters
from telegraph import Telegraph, exceptions, upload_file
from ... import *
from ... import app, SUDO_USER

from SHUKLA.modules.SHASHANK.errors import capture_err

# <=======================================================================================================>

TMP_DOWNLOAD_DIRECTORY = "tg-File/"
bname = "YaeMiko_Roxbot"  # ᴅᴏɴ'ᴛ ᴇᴅɪᴛ ᴛʜɪᴀ ʟɪɴᴇ
telegraph = Telegraph()
r = telegraph.create_account(short_name=bname)
auth_url = r["auth_url"]


# <================================================ FUNCTION =======================================================>
@app.on_message(
    filters.command(["tgm"], ".") & (filters.me | filters.user(SUDO_USER))
)
@capture_err
async def telegraph_upload(client, message):
    if message.reply_to_message:
        start = datetime.now()
        r_message = message.reply_to_message
        input_str = message.command[0]
        if input_str in ["tgm", "tmg", "telegraph"]:
            downloaded_file_name = await client.download_media(
                r_message, file_name=TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            h = await message.reply_text(f"❍ ᴡᴀɪᴛ ᴘʟᴇᴀsᴇ  {ms} sᴇᴄ.")
            if downloaded_file_name.endswith(".webp"):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await h.edit_text("Error: " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await h.edit_text(
                    f"""
➼ **ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ [ᴛᴇʟᴇɢʀᴀᴘʜ](https://telegra.ph{media_urls[0]}) in {ms + ms_two} seconds.**\n 
➼ **ᴄᴏᴘʏ ʟɪɴᴋ :** `https://telegra.ph{media_urls[0]}`""",
                    disable_web_page_preview=False,
                )
    else:
        await message.reply_text(
            "❍ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ telegra.ph ʟɪɴᴋ."
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


# <=================================================== HELP ====================================================>
__NAME__ = "Tᴇʟᴇɢʀᴀᴘʜ"
__MENU__ = """
`.tgm` - **ᴘɪᴄ ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ʟɪɴᴋ**
`.ss` - **sᴇɴᴅ ᴀ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ (ɴᴏᴛ sᴇᴄʀᴇᴛ) ᴛᴏ ᴀɴɴᴏʏ ᴏʀ ᴛʀᴏʟʟ ʏᴏᴜʀ ғʀɪᴇɴᴅs.**

"""
# <================================================ END =======================================================>
