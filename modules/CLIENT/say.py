from ..Module import * 
async def say_callback(CommandObject,message,self,params,command_data):
     if message.author != self.user:
          to_say = message.content.replace('.say', '')
          for word in ["ban","kick","timeout","fuck","nigga","nigger","niger","niga"] : 
               if word in to_say:
                    await message.channel.send("Flagged Text, cannot be executed")
                    return False
          if len(to_say.split()) <=1:
               await message.channel.send("Too small")
               return False
          if to_say[0] in [".","!","?",",","/","*","^","$","#","@"]:
               await message.channel.send("Command Cannot be executed")
          if len(message.mentions) > 0:
               await message.channel.send("Cannot mention user, use .life instead")
               return False
          await message.channel.send(to_say)
     
say_command = Command("say", 'Say something', say_callback, CLIENT, aliases=['repeat'],params=["TEXT"],ispremium=True)