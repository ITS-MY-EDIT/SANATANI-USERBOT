import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))
OWNER_ID = int(getenv("OWNER_ID", "5959548791"))
OWNER_USERNAME = getenv("OWNER_USERNAME", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5959548791").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/c646ef909ec110103d3b7.jpg")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**◎ ʜᴇʟʟᴏ ᴍʏ ᴅᴇᴀʀ sɪʀ | ᴍɪss \n\n◎ ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴘᴏᴡᴇʀ\n    ғᴜʟʟ ᴜsᴇʀʙᴏᴛ | ᴀɪ ʙᴀsᴇᴅ\n\n◎ ɪ ᴀᴍ ᴘʀᴏᴛᴇᴄᴛɪɴɢ ᴍʏ ᴏᴡɴᴇʀ\n\n◎ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴍᴇssᴀɢᴇ ᴡɪᴛʜᴜᴛ\n    ʜɪs ᴘᴇʀᴍɪssɪᴏɴ\n\nɪғ ʏᴏᴜ sᴘᴀᴍ ɪ ᴡɪʟʟ ʙʟᴏᴄᴋ ʏᴏᴜ**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/c646ef909ec110103d3b7.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("main")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

