from ..Module import * 
from datetime import timedelta
#from ..Utils import * #import this if you need utility commands
async def timeout_callback(CommandObject,message,self,params,command_data):
                    if message.author.guild_permissions.moderate_members:
                     failed = False
                     for i in message.mentions:
                          if not failed: 
                            try:
                                delta = timedelta(
                                    minutes=10,
                                    )
                                await i.timeout(delta)
                                await message.channel.send(f'Timed out user {i.mention}')
                            except Exception as e:
                                failed = True
                                await message.channel.send(f'I do not have permissions to timeout or user is already timed out, error log: {e}')
                    else:
                     await message.channel.send('You do not have permissions to timeout!')
timeout_command = Command("timeout","Timeout a user.",timeout_callback,ADMIN,aliases=["mute"],isfree=True)