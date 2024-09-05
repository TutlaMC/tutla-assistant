from ..Module import * 
from ..Utils import * 
import random
async def giveaway_callback(CommandObject,message,self,params,command_data):
    item = message_without_command(params)
    weebs = ''
    for i in message.mentions: 
        weebs+=i.mention+','
        item.replace(i.mention)
    weebs+=message.author.mention
    
    e = await message.channel.send(f"## Giveaway!\n`{item}`\nBy {weebs}\n-# ID {str(random.randint(1,100)+100)}TUTLAGWID")
    await e.add_reaction("🎉")

async def gend_callback(CommandObject,message,self,params,command_data):
    if message.reference:
        msg = await message.channel.fetch_message(message.reference.message_id)
        if str(message.author.id) not in msg.content: return False
        if msg.content.endswith("TUTLAGWID") and msg.content.startswith("## Giveaway!") and msg.author.id == self.user.id:
            for i in msg.reactions:
                if i.emoji == "🎉":
                    users = [user async for user in i.users()]
                    winner = random.choice(users)
                    if len(users) >= 2:
                        while winner.id == self.user.id:
                            winner = random.choice(users)
                        await message.channel.send(f"Winner is {winner.mention}")
                    else: await message.channel.send("Giveaway needs atleast 1 user to end!")
        
        
giveaway_command = Command("giveaway", 'Run giveaways with Tutla Assistance', giveaway_callback, TOOLS, aliases=['gw',"gcreate"],params=["ITEM"])
        
giveaway_command = Command("gend", 'End a giveaway', gend_callback, TOOLS, aliases=['gwend',"end"],params=["ReferenceMessage"])