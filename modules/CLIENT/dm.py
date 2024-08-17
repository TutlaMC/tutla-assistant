from ..Module import * 
from ..Utils import message_without_command
async def dm_callback(CommandObject,message,self,params,command_data):
    if message.author != self.user:
        user = await self.fetch_channel(message.mentions[0].dm_channel.id)
        await message.mentions[0].create_dm()
        await user.send(message_without_command(params).replace(str(message.mentions[0].id),"").replace("<@>",""))
        await message.channel.send("Sent User Message in DMs")
     
dm_command = Command("dm", 'DM a user something', dm_callback, CLIENT, aliases=['tell'],params=["TEXT"],ispremium=True)