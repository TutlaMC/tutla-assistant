from ..Module import * 
import random
async def ball_callback(CommandObject,message,self,params,command_data):
                    await message.channel.send(random.choice(["No 100%","Yes bruh","Roll **harder**","wtf","Obviously","none of the above","provide mroe context","sounds like smth ur gramma would say",'no talk ez yas','nah','no dude','yas :thumbsup:',":thumbsdown:","*yeets balls over face*"]))                   
ball_command = Command("8ball","Ultimate Decision Making Solution",ball_callback,TOOLS,aliases=["decide"],params=["STATEMENT"],isfree=True)