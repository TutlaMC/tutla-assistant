from . import mod
from assistantdata import db
from modules import Utils
auraMod = mod.Mod("aura","Aura time")

aura_loss = []
aura_loss_words = []
def aurareload():
    with open("assistantdata/mods/data/aura.txt","r") as f:
        e = f.readlines()
        for i in e: 
            aura_loss.append(i.replace("\n",""))
            if len(i.split()) == 1:
                aura_loss_words.append(i.replace("\n",""))
aurareload()
get_aura = ["whats my aura","my aura","how to get my aura","aura","whats aura","get aura","aura"]
async def aura(number,message):
    if message.author.bot: return False
    if message.author.id == auraMod.bot.user.id: return False
    if not db.userExists(message.author.id): db.add_user(message.author.id)
    db.edit_user(message.author.id,aura=db.getData(message.author.id,"aura")-number)
    await message.channel.send(f"-{number} aura")

async def aura_command(message):
    
    if message.content.lower() in aura_loss:
        await aura(1000, message)
    elif message.content.lower().replace("'","") in get_aura:
        if not db.userExists(message.author.id): db.add_user(message.author.id)
        await message.channel.send(f"{message.author.mention} has {db.getData(message.author.id,'aura')} aura")
    if message.content.startswith("aura"):
        if Utils.getAdminLevel(message.author.id) > 3:
            if message.content.split()[1] == "phrase":
                with open("assistantdata/mods/data/aura.txt","r") as f:
                    e = f.readlines()
                with open("assistantdata/mods/data/aura.txt","w") as f:
                    e.append(message.content.replace("aura phrase ","")+"\n")
                    f.writelines(e)
                    aura_loss.append(message.content.replace("aura phrase ",""))
                    await message.channel.send("Added aura phrase")
                    
                    aurareload()
                    
    for i in aura_loss_words:
        if i in message.content:
            await aura(500,message)

auraMod.on_message(aura_command)