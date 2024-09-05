from ..Module import * 
from ..Utils import * 
from assistantdata import db
async def ghostping_callback(CommandObject,message,self,params,command_data):

    if isInSlowmode(message.author.id,15) and db.getData(message.author.id,"last_command") == "ghostping":
        await message.channel.send(f"You are being rate limited, you can execute this again in {str(getSlowmode(message.author.id))}")
    else:
        for i in message.mentions:
            for err in range(5):
                await message.channel.send(i.mention,delete_after=1)
    

    

ghostping_cmd = Command("ghostping","Oblitirate someone by ghost pinging them and spamming their dms. IK evil",ghostping_callback,FUN,aliases=["kill",'end','spam',"life"],params=["USER PING"],ispremium=True)