from . import mod
import json
EMod = mod.Mod("E Event Mod","E Counter")
with open("assistantdata/mods/data/e.json","r") as f:
            global to_update
            to_update = json.load(f)

async def recieve_message(message):
    if message.content.startswith(".ecounter"):
        with open("assistantdata/mods/data/e.json","r") as f:
            e = json.load(f)
        with open("assistantdata/mods/data/e.json","w") as f:
            json.dump(to_update,f)
            
        await message.channel.send("Global Count: "+str(to_update['global']))
    elif message.content.startswith(".ecount"):
         for user in message.mentions:
            if str(user.name) in to_update: await message.channel.send("Your E Count: "+str(to_update[str(user.name)]))
            else: await message.channel.send("No e :(")
            
    elif message.content == ".eleaderboard":
        await message.channel.send("E Event is over. Create a ticket, mention TutlaMC or contact a staff member for your reward")
    elif message.content == "e":

        if str(message.author.name) in to_update: 
            to_update[str(message.author.name)] +=1
        else:
             to_update[str(message.author.name)] = 1
             
        to_update["global"] +=1



EMod.on_message(recieve_message)