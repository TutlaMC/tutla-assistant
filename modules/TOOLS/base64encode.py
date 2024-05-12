from ..Module import * 
from ..Utils import *
async def base64encode_callback(CommandObject,message,self,params,command_data):
                    text_to_encode = message.content[len('.base64encode '):]
                    

                    encoded_text = base64.b64encode(text_to_encode.encode()).decode()
                    await message.channel.send(f'Base64 Encoded: `{encoded_text}`')
                    
base64encode_command = Command("base64encode","Enocde in base64",base64encode_callback,TOOLS,aliases=["base64",'64'],params=["TEXT"],isfree=True)