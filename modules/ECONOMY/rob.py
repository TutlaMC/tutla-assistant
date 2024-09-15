from ..Module import * 
from assistantdata import db
import random as rand
async def rob_callback(CommandObject,message,self,params,command_data):
    if len(message.mentions) > 0:
        user = message.mentions[0]
        if db.userExists(user.id):
            coins = db.getData(user.id,"coins")
            print(coins)
            mycoins = db.getData(message.author.id,"coins")
            if db.getData(user.id,"coins") in [None,0]: 
                await message.channel.send("User is broke")
                return False
            
            if rand.randint(1,10) <10:
                db.add_coins(message.author.id,coins=-int((mycoins-(int(mycoins/10)))))
                web = rand.choice(["HOLY SHI! You lost all the coins because you escaped the police using a lawnmover","You managed to break in, but your non existant mom called you bcack for chores and you forgot to turn on do not disturb mode","you sneezed they heared you, the police came 2 seconds later","you fell asleep","they had a dog","your tail fell off","you managed to steal it but everyone saw you steal it. L rizz"])
                await message.channel.send(f"YOU **FAILED** stealing <@{user.id}>!:\nReason: `{web}`\nYou lost 10% of your coins")
            else:
                cash = rand.randint(1,int(coins))
                if command_data['premium']: cash*=1.5
                db.add_coins(user.id,coins=-cash)
                db.add_coins(message.author.id,coins=cash)
                await message.channel.send(f"{user.mention} You managed to steal {str(cash)} off {user.mention}! W Rizz")
    else: await message.channel.send("You must ping someone to rob!")
    
rob_command = Command("rob", 'Gets your rob', rob_callback, ECONOMY, aliases=['rob',"steal"])