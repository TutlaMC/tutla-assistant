from ..Module import * 
import asyncio
#from ..Utils import * #import this if you need utility commands
async def nuke_callback(CommandObject,message,self,params,command_data):
    
    await message.channel.send('Imma go nuke this sh1t. (contact num for ultimate nuking service: `6942014696969`)')
    asyncio.sleep(2)
    await message.channel.send("Nuking server....")
nuke_command = Command("nuke","Nuke the server.",nuke_callback,FUN,aliases=["bomb"],isfree=True)