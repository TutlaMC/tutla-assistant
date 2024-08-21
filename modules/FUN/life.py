from ..Module import * 
from ..Utils import * 
async def life_callback(CommandObject,message,self,params,command_data):
    con = command_data['member']
    premium = command_data['premium']

    for i in message.mentions:
        for err in range(5):
            ghost_ping = await message.channel.send(i.mention,delete_after=1)

life_cmd = Command("life","Oblitirate someone by ghost pinging them and spamming their dms. IK evil",life_callback,FUN,aliases=["kill",'end','spam'],params=["USER PING"],ispremium=True)