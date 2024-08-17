from ..Module import * 
#from ..Utils import * #import this if you need utility commands

# First Ever Command

async def lmao_callback(CommandObject,message,self,params,command_data):
    await message.channel.send('lmao')
lmao_command = Command("l","LMAO",lmao_callback,FUN,aliases=["lmao"])