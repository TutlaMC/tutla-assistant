from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def kick_callback(CommandObject,message,self,params,command_data):
                    if message.author.guild_permissions.kick_members:
                        if message.reference:
                                msg = await self.fetch_message(message.reference.message_id)
                                try:
                                    await msg.author.kick(reason=message.content.replace('.kick',''))
                                    await message.channel.send(f'Successfully kicked {i.mention}')
                                except Exception as e: await message.channel.send('I do not have permission to kick users')
                        else:
                            for i in message.mentions:
                                rsn = message.content.replace('.kick','')
                                rsn = rsn.replace(message.author.mention,'')
                                try:
                                    await i.kick(reason=rsn)
                                    await message.channel.send(f'Successfully kicked {i.mention}')
                                except Exception as e: await message.channel.send('I do not have permission to kick users')
                    else:
                        await message.channel.send(f'You do not have permission to kick users')
kick_command = Command("kick","Kick a user off the server",kick_callback,ADMIN,aliases=["kickout"],isfree=True,usage="You can kick users with this command and you can also kick a user replying to their message")