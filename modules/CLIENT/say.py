from ..Module import *
from better_profanity import profanity
import re
profanity.load_censor_words()
profanity.add_censor_words(["nigga","nigger","skibidi","fanum"])
async def say_callback(CommandObject,message,self,params,command_data):
     if "rizz" in message.content:
          await message.channel.send(f"{message.author.mention} you got NO rizz")
     if message.author != self.user:
          to_say = message.content.replace('.say', '')
          for word in ["ban","kick","timeout","fuck","nigga","nigger","niger","niga"] : 
               if word in to_say:
                    await message.channel.send("Flagged Text, cannot be executed")
                    return False
          if len(to_say) <=3:
               await message.channel.send("Too small")
               return False
          if to_say[0] in [".","!","?",",","/","*","^","$","#","@"]:
               await message.channel.send("Command Cannot be executed")

          e = ""
          for word in to_say.split():
               erm = False
               for i in word: 
                    if not i.isascii():
                         erm= True
               if not erm: 
                    e+=word+" "
          v2 = e
          if profanity.censor(v2) != e: 
               await message.channel.send("Flagged Text, cannot send")
               return False
          await message.channel.send(profanity.censor(e),silent=True)
     
say_command = Command("say", 'Say something', say_callback, CLIENT, aliases=['repeat'],params=["TEXT"],ispremium=True)