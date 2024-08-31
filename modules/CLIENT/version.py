from ..Module import * 
from ..Utils import version
async def version_callback(CommandObject,message,self,params,command_data):
    await message.channel.send(version)
reload_command = Command("version", 'Tutla Assistance Version', version_callback, CLIENT, aliases=['v'])