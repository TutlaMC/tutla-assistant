from ..Module import * 
from ..Utils import * 
from io import BytesIO
from discord import File
import requests
import random
async def scale_callback(CommandObject,message,self,params,command_data):
    if paramExists(params,1) and paramExists(params,2):
        f1 = params[1]
        f2 = params[2]
        api_url = f'https://fakeimg.pl/{f1}x{f2}'
        r = requests.get(api_url)

        await message.channel.send(file=File(fp=BytesIO(r.content),filename='scale.jpg'))
    else: await message.channel.send(CommandObject.usage)
         
scale_command = Command("scale","Generate a QR Code",scale_callback,TOOLS,aliases=['imgsize'],params=['WIDTH',"HEIGHT"])