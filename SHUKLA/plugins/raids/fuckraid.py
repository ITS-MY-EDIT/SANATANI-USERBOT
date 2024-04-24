from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["fr", "rr", "rraid", "fuckraid"]))
@sudo_users_only
async def add_fuck_raid(client, message):
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
                "**❍ ʜᴏᴡ ғᴏᴏʟ, ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ʏᴏᴜʀ ᴏᴡɴᴇʀ ɪ'ᴅ**"
            )
        
        fraid = await add_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜɪs ᴜsᴇʀ.**"
            )
        return await aux.edit(
            "**❍ ʜᴇʏ, ʀᴇᴘʟʏ ʀᴀɪᴅ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ ᴏɴ ᴛʜɪs ᴜsᴇʀ**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dfr", "drr", "drraid", "dfuckraid"]))
@sudo_users_only
async def del_fuck_raid(client, message):
    try:
        aux = await eor(message, "**❍ ᴘʀᴏᴄᴇssɪɴɢ ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**❍ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ.**"
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
                "**❍ ʜᴏᴡ ғᴏᴏʟ, ᴡʜᴇɴ ɪ ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ʏᴏᴜʀ ɪ'ᴅ**"
            )
        
        fraid = await del_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**❍ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ғʀᴏᴍ ᴛʜɪs ᴜsᴇʀ.**"
            )
        return await aux.edit(
            "**❍ ʜᴇʏ, ʀᴇᴘʟʏ ʀᴀɪᴅ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏɴ ᴛʜɪs ᴜsᴇʀ**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return
