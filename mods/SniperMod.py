from . import mod
SnipeMod = mod.Mod("Sniper","Some Random Snipe Bot")

sniped = {

}
sniped_users = {

}

async def snipe_record(message):
    global sniped, sniped_users
    channel_id = message.channel.id
    author_id = message.author.id

    if channel_id not in sniped:
        sniped[channel_id] = { "1": None, "2": None, "3": None }
    
    sniped[channel_id]["3"] = sniped[channel_id]["2"]
    sniped[channel_id]["2"] = sniped[channel_id]["1"]
    sniped[channel_id]["1"] = message
    
    sniped_users[author_id] = message


async def sniper_send(sniped_message,message):
    if sniped_message.reference:
        er = await sniped_message.channel.fetch_message(sniped_message.reference.message_id)
        e = f" to {er.jump_url}"
    else: e = ""
    await message.channel.send(f"========= SNIPE MOD V2 ============\n{sniped_message.content}\n===================================\n-# By {sniped_message.author.mention}{e} @ {sniped_message.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}")

async def esniper_send(sniped_message1, sniped_message2, message):
    if sniped_message1.reference:
        er = await sniped_message1.channel.fetch_message(sniped_message1.reference.message_id)
        e = f" to {er.jump_url}"
    else: e = ""
    await message.channel.send(f"========= BEFORE SNIPE MOD V2 BEFORE ============\n{sniped_message1.content}\n===================================\n-# @ {sniped_message1.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    await message.channel.send(f"========= AFTER  SNIPE MOD V2 AFTER  ============\n{sniped_message2.content}\n===================================\n-# By {sniped_message1.author.mention}{e} Edited @ {sniped_message2.edited_at.strftime('%Y-%m-%d %H:%M:%S UTC')}")

async def snipe_command(message):
    if message.content.startswith(".snipe"): 
        await message.channel.typing()
        if len(message.mentions) <=0:

            beem = False
            if len(message.content.split()) > 1:
                if message.content.split()[1] in ["1","2","3"]:
                    if sniped[message.channel.id][message.content.split()[1]] != None:
                        sniped_message = sniped[message.channel.id][message.content.split()[1]]
                    else: beem = True
                else: beem = True
            else: beem = True

            if beem: sniped_message = sniped[message.channel.id]['1']


            if sniped_message.author == SnipeMod.bot: return False
            await sniper_send(sniped_message,message)
        else:
            sniped_message = sniped_users[message.mentions[0].id]
            if sniped_message.author == SnipeMod.bot: return False
            await sniper_send(sniped_message,message)

    if message.content.startswith(".esnipe"): 
        await message.channel.typing()
        if len(message.mentions) <=0:
            sniped_message = esniped[message.channel.id]
            if sniped_message[0].author == SnipeMod.bot: return False
            await esniper_send(sniped_message[0],sniped_message[1],message)
        else:
            sniped_message = esniped_users[message.mentions[0].id]
            if sniped_message[0].author == SnipeMod.bot: return False
            await esniper_send(sniped_message[0],sniped_message[1],message)

esniped = {

}
esniped_users = {

}
async def esnipe_record(before,after):
    global esniped, esniped_users
    esniped[before.channel.id] = [before,after]
    esniped_users[before.author.id] = [before,after]

    

SnipeMod.on_edit(esnipe_record)
SnipeMod.on_delete(snipe_record)
SnipeMod.on_message(snipe_command)