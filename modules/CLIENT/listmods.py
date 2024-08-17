from ..Module import * 
from ..Utils import *
async def listmods_callback(CommandObject,message,self,params,command_data):
     nmessage = 'Mods:\n```yaml\n'
     for i in mod.mods:
                    nmessage+='- '+i.name+'\n'
     nmessage+='```'
     await message.channel.send(nmessage)
listmods_command = Command("listmods", 'Lists all mods installed on Tutla Assistance', listmods_callback, CLIENT, aliases=['lm', 'mods'],isfree=True)