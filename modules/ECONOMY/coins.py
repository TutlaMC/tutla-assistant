from ..Module import * 
from assistantdata import db
async def coins_callback(CommandObject,message,self,params,command_data):
    if len(message.mentions) == 0: message.mentions.append(message.author)
    for i in message.mentions:
        await message.channel.send(f"{i.mention} Coins: {str(int(db.getData(i.id,'coins')))}",silent=True)
    
coins_command = Command("coins", 'Gets your coins', coins_callback, ECONOMY, aliases=['coins',"currency"])