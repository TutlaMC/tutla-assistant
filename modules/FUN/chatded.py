from ..Module import * 
from datetime import datetime
#from ..Utils import * #import this if you need utility commands
async def chatded_callback(CommandObject,message,self,params,command_data):
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

    await message.channel.send(f'Chat ded - `{current_time}`')
chatded_command = Command("chatded","Chat ded - 2024",chatded_callback,FUN,aliases=["chatdead"])