import time
from urllib.parse import urlparse
import os
import asyncio
import requests
import wget
import yt_dlp
from youtubesearchpython import SearchVideos
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from pyrogram import filters
from pyrogram.types import *
from ... import *
from ... import app, SUDO_USER

#-------------------


# ------------------------------------------------------------------------------- #

@app.on_message(
    filters.command(["song"], ".") & (filters.me | filters.user(SUDO_USER))
)
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("**❍ sᴇᴀʀᴄʜɪɴɢ... **")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results[0]["views"]
        channel_name = results[0]["channel"]

    except Exception as e:
        m.edit("**❍ ɴᴏ ʀᴇsᴜʟᴛs ᴡᴇʀᴇ ғᴏᴜɴᴅ. ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴛʏᴘᴇᴅ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ sᴏɴɢ ɴᴀᴍᴇ**")
        print(str(e))
        return
    m.edit("**❍ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**❍ ᴜᴘʟᴏᴀᴅɪɴɢ...**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}\nRᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➪{message.from_user.mention}\nVɪᴇᴡs➪ {views}\nCʜᴀɴɴᴇʟ➪ {channel_name}",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
    
 # -----------------------------------
 
 

                                                    

# ------------------------------------------------------------------------------- #

###### INSTAGRAM REELS DOWNLOAD


@app.on_message(
    filters.command(["ig"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def download_instareels(c: app, m: Message):
    try:
        reel_ = m.command[1]
    except IndexError:
        await m.reply_text("❍ ɢɪᴠᴇ ᴍᴇ ᴀɴ ʟɪɴᴋ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪᴛ...")
        return
    if not reel_.startswith("https://www.instagram.com/reel/"):
        await m.reply_text("❍ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ᴏʙᴛᴀɪɴ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ʀᴇᴇʟ, ᴀ ᴠᴀʟɪᴅ ʟɪɴᴋ ɪs ɴᴇᴄᴇssᴀʀʏ. ᴋɪɴᴅʟʏ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ᴡɪᴛʜ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ʟɪɴᴋ.")
        return
    OwO = reel_.split(".",1)
    Reel_ = ".dd".join(OwO)
    try:
        await m.reply_video(Reel_)
        return
    except Exception:
        try:
            await m.reply_photo(Reel_)
            return
        except Exception:
            try:
                await m.reply_document(Reel_)
                return
            except Exception:
                await m.reply_text("❍ ɪ ᴀᴍ ᴜɴᴀʙʟᴇ ᴛᴏ ʀᴇᴀᴄʜ ᴛᴏ ᴛʜɪs ʀᴇᴇʟ.")



######









@app.on_message(
    filters.command(["reel"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def instagram_reel(client, message):
    if len(message.command) == 2:
        url = message.command[1]
        response = requests.post(f"https://lexica-api.vercel.app/download/instagram?url={url}")
        data = response.json()

        if data['code'] == 2:
            media_urls = data['content']['mediaUrls']
            if media_urls:
                video_url = media_urls[0]['url']
                await message.reply_video(f"{video_url}")
            else:
                await message.reply("❍ ɴᴏ ᴠɪᴅᴇᴏ ғᴏᴜɴᴅ ɪɴ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ. ᴍᴀʏ ʙᴇ ᴀᴄᴄᴏᴜɴᴛʙɪs ᴘʀɪᴠᴀᴛᴇ.")
        else:
            await message.reply("❍ ʀᴇǫᴜᴇsᴛ ᴡᴀs ɴᴏᴛ sᴜᴄᴄᴇssғᴜʟ.")
    else:
        await message.reply("❍ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ɪɴsᴛᴀɢʀᴀᴍ ᴜʀʟ ᴜsɪɴɢ ᴛʜᴇ /reel ᴄᴏᴍᴍᴀɴᴅ.")



# --------------

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(
    filters.command(["yt"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def ytmusic(client, message: Message):
    urlissed = get_text(message)
    await message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(message.chat.id, f"❍ sᴇᴀʀᴄʜɪɴɢ, ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    if not urlissed:
        await pablo.edit(
            "❍ sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ ᴏɴ ʏᴏᴜᴛᴜʙᴇ.\n\n» ᴀᴘᴍᴇ ɢᴀʟᴛ ʟɪᴋʜᴀ ʜᴀɪ ғɪʀ sᴇ ᴛʀʏ ᴋɪᴊɪʏᴇ..!!"
        )
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            round(infoo["duration"] / 60)
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"**ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ.** \n**ᴇʀʀᴏʀ :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"❍ **ᴛɪᴛʟᴇ :** [{thum}]({mo})\n❍**ᴄʜᴀɴɴᴇʟ :** {thums}\n❍ **sᴇᴀʀᴄʜᴇᴅ :** {urlissed}\n❍ **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {chutiya}"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress_args=(
            pablo,
            c_time,
            f"» ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...\n\nᴜᴩʟᴏᴀᴅɪɴɢ `{urlissed}` ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ sᴇʀᴠᴇʀs...",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


__NAME__ = "Dᴏᴡɴʟᴏᴀᴅ"
__MENU__ = """
`.song` - , **sᴇᴀʀᴄʜ sᴏɴɢs ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ..**
`.ig .reel` - **ʟɪɴᴋ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɢ ʀᴇᴇʟ**
`.yt` - **ʟɪɴᴋ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜ-ᴛᴜʙᴇ ᴠɪᴅᴇᴏ **



"""
