from ..Module import * 
from ..Utils import * 
from io import BytesIO
from discord import File
import requests
import random
async def fox_callback(CommandObject,message,self,params,command_data):
    
    api_url = f'https://randomfox.ca/images/{str(random.randint(1,123))}.jpg'
    r = requests.get(api_url)

    await message.channel.send(file=File(fp=BytesIO(r.content),filename='fox.jpg'))
         
fox_command = Command("fox","Get a random fox pic",fox_callback,FUN,aliases=['furry'])