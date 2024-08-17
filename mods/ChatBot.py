from . import mod
import asyncio
ChatBotMod = mod.Mod("ChatBot","Some Random Snipe Bot")

 
async def recieve_message(message):
   if message.content == "hi": await message.channel.send("reeee")
ChatBotMod.on_message(recieve_message)