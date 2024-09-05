from ..Module import *
import os
from discord import FFmpegPCMAudio,utils
from yt_dlp import YoutubeDL
import io

def download_audio_to_bytes(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'temp_audio.%(ext)s',
        'quiet': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    with open('temp_audio.mp3', 'rb') as f:
        buffer = io.BytesIO(f.read())
    
    os.remove('temp_audio.mp3')
    
    buffer.seek(0)
    return buffer

async def play_callback(CommandObject, message, self, params, command_data):
    if message.author.voice:
        channel = message.author.voice.channel
        voice_client = utils.get(self.voice_clients, guild=message.guild)
        
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()
        
        voice_client = await channel.connect()

        url = params[1]
        await message.channel.send("Please wait while we load the song")
        audio_buffer = download_audio_to_bytes(url)

        voice_client.play(FFmpegPCMAudio(audio_buffer, pipe=True))
        await message.channel.send(f'Now playing: {url}')
    else:
        await message.channel.send("You need to be in a voice channel to play music.")

play_command = Command(
    "play","Play song/vid from a YouTube in a VC",play_callback,CLIENT,aliases=['p'],params=["YOUTUBE LINK"],ispremium=True)
