from ..Module import * 
from ..Utils import * 
from io import BytesIO
from discord import File
import requests
import random
async def qr_callback(CommandObject,message,self,params,command_data):
    
    api_url = f'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={message_without_command(params).replace(" ","%20")}'
    r = requests.get(api_url)

    await message.channel.send(file=File(fp=BytesIO(r.content),filename='qr.jpg'))
         
qr_command = Command("qr","Generate a QR Code",qr_callback,TOOLS,aliases=['qrcode'],params=['DATA/LINK'])