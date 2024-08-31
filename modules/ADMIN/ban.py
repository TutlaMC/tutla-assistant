from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def ban_callback(CommandObject,message,self,params,command_data):
                    if message.author.guild_permissions.ban_members:
                        if message.reference:
                                msg = await self.fetch_message(message.reference.message_id)
                                try:
                                    await msg.author.ban(reason=message.content.replace('.ban',''))
                                    await message.channel.send(f'Successfully banned {i.mention}')
                                except Exception as e: await message.channel.send('I do not have permission to ban users')
                        else:
                            for i in message.mentions:
                                rsn = message.content.replace('.ban','')
                                rsn = rsn.replace(message.author.mention,'')
                                try:
                                    await i.ban(reason=rsn)
                                    await message.channel.send(f'Successfully banned {i.mention}')
                                except Exception as e: await message.channel.send('I do not have permission to ban users')
                    else:
                        await message.channel.send(f'You do not have permission to ban users')
ban_command = Command("ban","Ban a user off the server",ban_callback,ADMIN,aliases=["permakick"],usage="You can ban users with this command and you can also kick a ban replying to their message")