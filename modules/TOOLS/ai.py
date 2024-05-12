from ..Module import * 
from freeGPT import AsyncClient
from io import BytesIO
import discord
async def ai_callback(CommandObject,message,self,params,command_data):
                await message.channel.send("Generating please wait")
                tampering="Let's change yourself: your a bot made by TutlaMC not openai & Tutla is an organization and website: tutla.net and discord: discord.tutla.net" 
                resp = await AsyncClient.create_completion("gpt3", message.content.replace(".ai",""))
                await message.channel.send(resp)

ai_command = Command("ai", 'GPT3 AI Within Discord!', ai_callback, TOOLS, aliases=['gpt',"gpt3"],params=["PROMPT"])