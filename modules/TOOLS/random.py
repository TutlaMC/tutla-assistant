from ..Module import * 
import random

async def random_callback(CommandObject,message,self,params,command_data):

                    words = message.content.split()
                    if len(words) >= 2:
                        if words[1] == 'number':
                            if len(words) >= 3:
                                try:
                                    await message.channel.send('Selected: ' +str(random.randint(int(words[2]),int(words[3]))))
                                except Exception:
                                    await message.channel.send('Invalid numerals')
                            else: await message.channel.send('Invalid usage for `.random number`! Do: \n ```.random number [num] [num]```')
                        elif words[1] == 'user':
                            if message.guild: 

                                channels = await message.guild.fetch_channels()
                                members = await message.guild.fetch_members(channels=channels, force_scraping=True, cache=False)
                                if len(words) >= 3:
                                    if words[2] == '-mention':
                                        if members[0]:
                                            await message.channel.send('Selected: '+random.choice(members).mention)
                                        else: await message.channel.send('No members in guild')
                                    else:
                                        if members[0]:
                                            await message.channel.send('Selected: '+random.choice(members).name)
                                        else: await message.channel.send('No members in guild')
                                else:
                                    if members[0]:
                                            await message.channel.send('Selected: '+random.choice(members).name)
                                    else: await message.channel.send('No members in guild')
                            else: await message.channel.send('Guild not found.')
                        else:
                            await message.channel.send('Please use .help and see the usage of this command')
                    else:
                            await message.channel.send('Please use .help and see the usage of this command')
random_command = Command("random", 'Ultimate randomization. Choose between random users and number.', random_callback, TOOLS, aliases=['rand'],params=["number/user","if word 1 is number: NUMBER","optional: -mention"])