from ..Module import * 
from ..Utils import * 
from io import BytesIO
from discord import File
import requests
async def cartoon_callback(CommandObject,message,self,params,command_data):
    
    api_url = f'https://robohash.org/:{message_without_command(params).replace(" ","%20")}'
    r = requests.get(api_url)

    await message.channel.send(f"Your cartoon avatar:\n-# Prompt: {message.content}",file=File(fp=BytesIO(r.content),filename='cartoon_avatar.png'))
         
cartoon_command = Command("cartoon","Create a cartoon avatar",cartoon_callback,IMAGES,aliases=['character'])