from ..Module import * 
from ..Utils import *
async def premium_callback(CommandObject,message,self,params,command_data):
                    premium_reload()
                    ban_reload()
                    con = command_data['member']
                    premium = command_data['premium']

                    if premium: await message.channel.send('Yes you have premium! Feel free to use your premium commands') 
                    else: await message.channel.send('You dont failure')
premium_command = Command("premium","Checks if you have premium",premium_callback,CLIENT,aliases=["ispremium",'vip','isvip'],isfree=True)