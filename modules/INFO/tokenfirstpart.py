from ..Module import * 
from ..Utils import * #import this if you need utility commands
async def tokenfirstpart_callback(CommandObject,message,self,params,command_data):
                    text_to_encode = message.content[len('.tokenfirstpart '):]
                    for i in message.mentions:
                        encoded_text = base64.b64encode(str(i.id).encode()).decode()
                        await message.channel.send(f'Token First Part: `{encoded_text}`')

tokenfirstpart_command = Command("tokenfirstpart","Get the token of a user",tokenfirstpart_callback,INFO,aliases=['token','gettoken'],params=["USER PING"])