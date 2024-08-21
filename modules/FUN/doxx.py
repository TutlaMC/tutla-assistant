from ..Module import * 
from ..Utils import * 
async def doxx_callback(CommandObject,message,self,params,command_data):
    for user in message.mentions:
        await message.channel.send(f"More about {user.mention}:\n- Age: ||Above 0||\n- Location: ||Milkyway Galaxy, Earth||\n- Gender: ||Human||\n- email: ||hosted by sum email service like gmail or sum||\n- Skin Color: ||black,white, or brown||")

doxx_cmd = Command("doxx","Find all details of someone",doxx_callback,FUN,aliases=["kill",'end','spam'],params=["USER PING"],ispremium=True)