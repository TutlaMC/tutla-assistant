from ..Module import * 
from ..Utils import *
from assistantdata import db
import random as ran

async def dice_callback(CommandObject,message,self,params,command_data):
    if paramExists(params,1):
        if params[1].isdigit():
            coins = int(params[1])
            if hasCoins(message.author.id,coins):
                roll = ran.randint(1,6)
                if roll == ran.randint(1,6):
                    db.add_coins(message.author.id,coins*4)
                    await message.channel.send(f"You rolled {str(roll)} and won {str(coins*4)}")
                else: 
                    db.add_coins(message.author.id,-coins)
                    await message.channel.send(f"You rolled {str(roll)} and lost it all :(")
            else: await message.channel.send(f"You do not have {params[1]} coins to bet")
        else: await message.channel.send(f"Dice Roll: {str(ran.randint(1,6))}")
    else: await message.channel.send(f"Dice Roll: {str(ran.randint(1,6))}")
dice_command = Command("dice", "Non-biased dice roll, you can use .random for numbers", dice_callback, TOOLS, aliases=['droll',"roll"],params=["Optional: Coins"])