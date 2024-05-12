from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def voicechannel_callback(CommandObject,message,self,params,command_data):
                    words = message.content.split()
                    if message.author.guild_permissions.manage_channels:
                        if len(words) > 2:
                            cn = f'{words[2]}｜{words[1]}'
                            try:
                                nchannel = await message.guild.create_voice_channel(cn)
                                await message.channel.send(f'Created Voice Channel: {nchannel.jump_url}')
                            except Exception as e:
                                await message.channel.send(f'I do not have permissions to voice create channel error log:```python\n{e}```')

                        else:
                            await message.channel.send('Invalid usage do: ```.voicechannel [name] [emoji] ```')
                    else: await message.channel.send('You do not have permissions to do this!')
txtchannel_command = Command("voicechannel","Create a voice channel.",voicechannel_callback,ADMIN,aliases=["vc","voicechat"],isfree=True)