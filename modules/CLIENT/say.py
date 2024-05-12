from ..Module import * 
async def say_callback(CommandObject,message,self,params,command_data):
     await message.channel.send(message.content.replace('.say', ''))
     
say_command = Command("say", 'Say something', say_callback, CLIENT, aliases=['tell'],params=["TEXT"],ispremium=True)