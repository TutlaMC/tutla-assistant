from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def racism_callback(CommandObject,message,self,params,command_data):
    await message.channel.send(message.author.mention+' bro really tried being racist')
racisim_command = Command("racism","Bypasses any antiswear and types the n word in chat.",racism_callback,FUN,aliases=["racisim"],isfree=True)