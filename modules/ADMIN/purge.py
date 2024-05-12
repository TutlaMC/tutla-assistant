from ..Module import * 

async def purge_callback(CommandObject,message,self,params,command_data):

                 if params[1].isdigit():
                    params[1] = int(params[1])
                    if message.author.guild_permissions.manage_messages: 

                            
                            
                                fail = False
                                try:
                                    deleted = await message.channel.purge(limit=params[1]+1)
                                    msg = await message.channel.send(f'Successfully purged {params[1]} messages')
                                    await msg.delete(delay=5)
                                except Exception as e:
                                    fail = True
                                    await message.channel.send(f'I do not have permission to delete messages, error log: ```python\n{e}```')

                    else:
                                message.channel.send(f'You do not have permission to delete messages')
                 else: await message.channel.send('Learn to type numbers properly')
                         
       
purge_command = Command("purge","Purge Messages.",purge_callback,ADMIN,aliases=["delete"],params=["COUNT"])