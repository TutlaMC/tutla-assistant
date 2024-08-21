from . import mod
import json
EMod = mod.Mod("E Event Mod","E Counter")
with open("mods/data/e.json","r") as f:
            global to_update
            to_update = json.load(f)

async def recieve_message(message):
    if message.content.startswith(".ecounter"):
        with open("mods/data/e.json","r") as f:
            e = json.load(f)
        with open("mods/data/e.json","w") as f:
            json.dump(to_update,f)
            
        await message.channel.send("Global Count: "+str(to_update['global']))
    elif message.content.startswith(".ecount"):
         for user in message.mentions:
            if str(user.id) in to_update: await message.channel.send("Your E Count: "+str(to_update[str(user.id)]))
            else: await message.channel.send("No e :(")
            
    elif message.content == ".eleaderboard":
        final="# E LEADERBOARD\n"
        sortedup = sorted(to_update.items(), key=lambda x: x[1], reverse=True)

        for id, val in sortedup:
            if not id == "global": 
                user = await EMod.bot.fetch_user(int(id))
                final+=''.join(f'{str(user.display_name)}: {val}')+'\n'
        await message.channel.send(final)
    elif message.content == "e":
        if str(message.author.id) in to_update: to_update[str(message.author.id)] +=1
        else: to_update[str(message.author.id)] = 1
        to_update["global"] +=1



EMod.on_message(recieve_message)