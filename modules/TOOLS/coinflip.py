from ..Module import * 
from ..Utils import *
import random as ran

def hot(roll): return f"{'Heads' if roll == 1 else 'Tails'}"
async def coinflip_callback(CommandObject,message,self,params,command_data):
    if paramExists(params,1):
        if params[1].isdigit():
            coins = int(params[1])
            if hasCoins(message.author.id,coins):
                roll = ran.randint(1,2)
                if roll == ran.randint(1,2):
                    db.add_coins(message.author.id,coins*2)
                    await message.channel.send(f"You got {hot(roll)} and won {str(coins*4)}")
                else: 
                    db.add_coins(message.author.id,-coins)
                    await message.channel.send(f"You rolled {hot(roll)} and lost it all :(")
            else: await message.channel.send(f"You do not have {params[1]} coins to bet")
        else: await message.channel.send(f"{hot(ran.randint(1,2))}")
    else: await message.channel.send(f"{hot(ran.randint(1,2))}")

coinflip_command = Command("coinflip", "You're broke so you decided to use one tof the best coinflipping bots in the world.", coinflip_callback, TOOLS, aliases=['cf',"bet"])