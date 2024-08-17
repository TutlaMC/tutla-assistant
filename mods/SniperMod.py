from . import mod
import asyncio
SnipeMod = mod.Mod("Sniper","Some Random Snipe Bot")

sniped = {

}
sniped_users = {

}

async def snipe_record(message):
    global sniped, sniped_users
    sniped[message.channel.id] = message
    sniped_users[message.author.id] = message
    
async def snipe_command(message):
    if message.content.startswith(".snipe"): 
        if len(message.mentions) <=0:
            sniped_message = sniped[message.channel.id]
            if sniped_message.author == SnipeMod.bot: return False
            await message.channel.send(f"========= SNIPE MOD V1 ============\n{sniped_message.content}\n===================================\n-# By {sniped_message.author.mention}")
        else:
            sniped_message = sniped_users[message.mentions[0].id]
            if sniped_message.author == SnipeMod.bot: return False
            await message.channel.send(f"========= SNIPE MOD V1 ============\n{sniped_message.content}\n===================================\n-# By {sniped_message.author.mention}")

SnipeMod.on_delete(snipe_record)
SnipeMod.on_message(snipe_command)