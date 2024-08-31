from ..Module import * 
from ..Utils import *
async def infinitecraft_callback(CommandObject,message,self,params,command_data):
    if len(params)-1 >= 1 and len(params)-1 <= 4 and "," in message.content: 
      
        out = await ai(f"Imagine your a crafting table, craft {params[1:]}. RESPOND ONLY WITH THE CRAFTED OUTPUT IN LESS THAN 3 WORDS NOTHING ELSE. YOU CANNOT ASK FOR ANYTHING JUST RESPOND WITH ONE POSSIBLE THING THAT COULD BE CRAFTED WITH THESE TWO OBJECTS. YOU CAN RESPOND WITH NOTHING OTHER THAN THE OUTPUT",message)
        await message.channel.send(f"Your table ({message_without_command(params).replace(',',',').replace(' ','')}): "+out)
    else: await message.channel.send("Your crafting table must use a maximum of 4 and minimum of 1 word(s) & the objects must be seperated with a ,")

infinitecraft_command = Command("infinitecraft","Play Infinitecraft on Discord!",infinitecraft_callback,FUN,aliases=["craft"],ispremium=True)