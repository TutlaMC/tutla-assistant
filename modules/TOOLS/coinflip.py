from ..Module import * 
import random as ran

async def coinflip_callback(CommandObject,message,self,params,command_data):
    await message.channel.send(f"{'Heads' if ran.randint(1,2) == 1 else 'Tails'}")
coinflip_command = Command("coinflip", "You're broke so you decided to use one tof the best coinflipping bots in the world.", coinflip_callback, TOOLS, aliases=['cf',"bet"])