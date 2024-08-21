from ..Module import * 
from ..Utils import message_without_command
from discord.errors import CaptchaRequired
from discord import HTTPException
async def dm_callback(CommandObject,message,self,params,command_data):
    if message.author != self.user:
        user = await message.mentions[0].create_dm()
        await message.mentions[0].dm_channel.send(message_without_command(params).replace(str(message.mentions[0].id),"").replace("<@>",""))
      
        await message.channel.send("Sent User Message in DMs")
    
dm_command = Command("dm", 'DM a user something', dm_callback, CLIENT, aliases=['tell'],params=["TEXT"],ispremium=True)