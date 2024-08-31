from ..Module import * 
from ..Utils import *
async def premium_callback(CommandObject,message,self,params,command_data):
                    premium_reload()
                    ban_reload()
                    premium = command_data['premium']
                    if len(message.mentions) == 0: 
                        if premium: await message.channel.send('Yes you have premium! Feel free to use your premium commands',silent=True) 
                        else: 
                                await message.channel.send("You do not have premium & your missing out on so much!",silent=True)
                                await message.channel.send("Get premium now at the [shop for **5$**](https://tutla.net/shop/discord/tutla-assistance-premium/)",silent=True)

                    else: 
                            for user in message.mentions:
                                    if user.id in premium_list: await message.channel.send(f'{user.mention} has premium.',silent=True) 
                                    else: await message.channel.send(f'{user.mention} does not have premium. He should jump off a cliff',silent=True)
                    
                                    
premium_command = Command("premium","Checks if you have premium",premium_callback,CLIENT,aliases=["ispremium",'vip','isvip'])