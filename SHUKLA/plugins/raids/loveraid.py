from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["lr", "lraid", "loveraid"]))
@sudo_users_only
async def add_love_raid(client, message):
    try:
        aux = await eor(message, "**❍ ᴘʀᴏᴄᴇssɪɴɢ ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**❍ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id

        if user_id == message.from_user.id:
            return await aux.edit(
                "**❍ ʜᴏᴡ ғᴏᴏʟ, ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ʏᴏᴜʀ ᴏᴡɴᴇʀ ɪᴅ**"
            )
        
        lraid = await add_loveraid_user(user_id)
        if lraid:
            return await aux.edit(
                "**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜɪs ᴜsᴇʀ.**"
            )
        return await aux.edit(
            "**❍ ʜᴇʏ, ʟᴏᴠᴇ ʀᴀɪᴅ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ ᴏɴ ᴛʜɪs ᴜsᴇʀ**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dlr", "dlraid", "dloveraid"]))
@sudo_users_only
async def del_love_raid(client, message):
    try:
        aux = await eor(message, "**❍ ᴘʀᴏᴄᴇssɪɴɢ ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**❍ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            return await aux.edit(
                "**❍ ʜᴏᴡ ғᴏᴏʟ, ᴡʜᴇɴ ɪ ᴀᴄᴛɪᴠᴀᴛᴇ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ʏᴏᴜʀ ɪ'ᴅ**"
            )
        
        lraid = await del_loveraid_user(user_id)
        if lraid:
            return await aux.edit(
                "**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ʟᴏᴠᴇ ʀᴀɪᴅ ғʀᴏᴍ ᴛʜɪs ᴜsᴇʀ.**"
            )
        return await aux.edit(
            "**❍ ʜᴇʏ, ʟᴏᴠᴇ ʀᴀɪᴅ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏɴ ᴛʜɪs ᴜsᴇʀ**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return

