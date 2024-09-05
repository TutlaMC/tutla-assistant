from ..Module import * 
from ..Utils import *
from assistantdata import db

async def afk_callback(CommandObject,message,self,params,command_data):
    reason = message_without_command(params)
    print(reason)
    if not message.author.id in afk_users:
        afk_users[message.author.id] = reason
        await message.channel.send("You are now afk!")
        if params[0].replace(".","") == "iamfucking":
            await message.channel.send("""You are now also fucking!\n.     😩
🫲 👕 🫱
      👖
.      😏
👊👕👊
.      💄
.      👖

       😩
🫲 👕 🫱
       👖
       😩
🫲 👕 🫱
       👖

.     😆
👊👕👊
.     💄
.     👖

🍆 😲
👈👕👈
. 🦵 🦵""")
    else: 
        afk_users.remove(message.author.id)
        await message.channel.send("You are no longer in afk")
    

afk_command = Command("afk","Set your status as AFK",afk_callback,TOOLS,aliases=["iamfucking","unafk"])

