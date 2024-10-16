
from ..Module import *
from ..Utils import *
from io import BytesIO
import os
from discord import FFmpegPCMAudio,utils
import youtube_dl
import io
voice_clients={}
async def download_audio(url):
    url = url.replace("https",'').replace('http','').replace('://','').replace('youtu.be','').replace('www.','').replace('youtube.com','').replace('/','').replace('watch?v=','')
    e=api("https://yt-api.p.rapidapi.com/dl","yt-api.p.rapidapi.com",{'id':url})
    e = e.json()
    dlog(e)
    response = requests.get(e['adaptiveFormats'][12]['url'], stream=True)
    if response.status_code == 200:
        video_data = BytesIO()

        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                video_data.write(chunk)
        video_data.seek(0)
    else:
        HTTPLogger.log("Failed to download video:"+ response.status_code+ response.text,style='error')
    return video_data

class PlayerGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    group = app_commands.Group(name="player", description="Music/Video Player")

    @premium_command
    @group.command(name="play",description="Play a song/mp3 in VC")
    @app_commands.check(commandCheck)
    async def play(self,ctx:discord.Interaction, vc: discord.VoiceChannel, *, url: str):
        await ctx.response.defer()
        await ctx.followup.send("Downloading...",ephemeral=True)
        if vc.id not in voice_clients:
            voice_client = await vc.connect()
            voice_clients[vc.id] = voice_client
        else:
            voice_client = voice_clients[vc.id]


        url2 = await download_audio(url)
        source = discord.FFmpegPCMAudio(url2,pipe=True)
        await ctx.followup.send(f"[Playing]({url}) in VC...")
        voice_client.play(source)

    @premium_command
    @group.command(name="stop", description="Stop playing a video")
    @app_commands.check(commandCheck)
    async def stop(self,ctx:discord.Interaction, vc: discord.VoiceChannel):
        if vc.id in voice_clients:
            await voice_clients[vc.id].disconnect()
            del voice_clients[vc.id]
            await ctx.response.send_message("Disconnected")

async def setup(bot: commands.Bot):
    await bot.add_cog(PlayerGroup(bot))