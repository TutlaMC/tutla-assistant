from ..Module import * 
from ..Utils import *
async def infiniterps_callback(CommandObject,message,self,params,command_data):

        out = await ai(f"Make the choice a 50/50 .Imagine your playing RPS but with ABSOULTETLY ANYTHING. Now you select a random item of the dictionary & make sure its a 50/50 on who wins as your play and then decide the winner. Format of respnse:\nYour Item: {message_without_command(params)}\nMy Item: [THE ITEM YOU SELECTED]\nReason: [explain how won] (DISPLAY **WINNER!** NEXT TO THE SLEETCED ITEMS & make winner 50/50)\n\nRESPOND ONLY WITH THE WINNER & YOUR ITEM AND MY ITEM IN THE ABOVE FORMAT. AND LASTLY A SENTENCE (reason) ON HOW THEY WON IN LESS THAN 15 WORDS. YOU CANNOT ASK FOR ANYTHING YOU CAN RESPOND WITH NOTHING OTHER THAN THE OUTPUT IN THAT FORMAT",message)
        await message.channel.send(out)
    

infiniterps_command = Command("infiniterps","Play Infiniterps on Discord!",infiniterps_callback,FUN,aliases=["rps"],ispremium=True)