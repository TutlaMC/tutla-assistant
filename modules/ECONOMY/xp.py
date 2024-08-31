from ..Module import * 
from assistantdata import db
async def xp_callback(CommandObject,message,self,params,command_data):
    if len(message.mentions) == 0: message.mentions.append(message.author)
    for i in message.mentions:
        await message.channel.send(f"{i.mention} XP: {str(db.getData(i.id,'xp'))}",silent=True)
    
reload_command = Command("xp", 'Gets your xp', xp_callback, ECONOMY, aliases=['v'])