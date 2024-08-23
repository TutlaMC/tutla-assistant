from ..Module import * 
from pytube import YouTube
from io import BytesIO
from discord import File
import yt_dlp
import subprocess
async def yt_callback(CommandObject,message,self,params,command_data):
    url = params[1]

    video_bytes = BytesIO()

    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'outtmpl': '-',  # Output to stdout
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl_process = subprocess.Popen(
            ['yt-dlp', '-f', 'best', '-o', '-', url],
            stdout=subprocess.PIPE
        )
        video_bytes.write(ydl_process.stdout.read())
        ydl_process.stdout.close()

    video_bytes.seek(0)



    

    await message.channel.send(file=File(fp=video_bytes, filename='video.mp4'))


dl_command = Command("dl", 'Download youtube videos', yt_callback, TOOLS, aliases=['yt',"youtube","download"],params=["URL"], ispremium=True)