from ..Module import * 
from ..Utils import *
import requests
from io import BytesIO
from discord import File



async def word_callback(CommandObject,message,self,params,command_data):

        word = params[1]
        e = requests.get(f"https://ftapi.pythonanywhere.com/translate?dl=en&text={word}")

        
        f = e.json()
        final = "Definitions, Examples & Synoyms:\n"
        if not f["definitions"]: await message.channel.send("No word found"); return False
        if len(f["definitions"]) > 1:
            ee = 0
            for definition in f["definitions"]:
                    ee+=1
                    if ee == 4: break
                    final+=f"- {definition['definition']}\n - Example: {definition['example']}\n - Synonyms:\n"
                    if definition['synonyms'] != None:
                        for i in definition['synonyms']['']:
                                final+=f"  - {i}\n"
                    else: final+="No Synonyms found\n"
                    
            await message.channel.send(final)
        else: await message.channel.send("No word found")

async def pronounce_callback(CommandObject,message,self,params,command_data):

        word = message_without_command(params)
        e = requests.get(f"https://ftapi.pythonanywhere.com/translate?dl=en&text={word}")

        
        f = e.json()
        if not f["pronunciation"]: await message.channel.send("No word found"); return False
        thing = f["pronunciation"]['destination-text-audio']

        response = requests.get(thing)
        audio_file = BytesIO(response.content)
                    
        await message.channel.send(file=File(fp=audio_file,filename="balls.mp3"))


pronounce_command = Command("pronounce", 'Get the pronunciation of a word', pronounce_callback, TOOLS, aliases=['pronunce',"hear"],params=['word'])
word_command = Command("word", 'Get Definition, example & synonym of a word', word_callback, TOOLS, aliases=['synonym',"definition","example"],params=['word'])