from ..Module import * 
from assistantdata import db
async def xp_callback(CommandObject,message,self,params,command_data):
    if len(message.mentions) == 0: message.mentions.append(message.author)
    for i in message.mentions:
        await message.channel.send(f"{i.mention} Your Level: {str(int(db.getData(i.id,'xp')/1000))}\nXP: {str(int(db.getData(i.id,'xp')))}",silent=True)
    
xp_command = Command("xp", 'Gets your xp/level', xp_callback, ECONOMY, aliases=['currency',"cash"])