from ..Module import * 
from ..Utils import * #import this if you need utility commands
async def userinfo_main(user, channel):
                            name = f'User Name: {user.name}\n'
                            sid =  f'User ID: {user.id}\n'
                            count= f'Joined user at: {user.joined_at}\n'
                            cd = f'User Creation Date: {user.created_at}\n'
                            roles = '---Roles---\n'
                            for i in user.roles:
                                roles = roles+i.name+' | '+'\n'
                            roles = roles+'\n'
                            perms = '---Permissions---\n'
                            mg = False
                            mr = False
                            ma = False
                            for i in user.roles: 
                                if i.permissions.manage_guild and not mg:
                                    perms += 'Manage Guild: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not mr:
                                    perms += 'Manage Roles: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not ma:
                                    perms += 'All Perms: True\n'
                                    ma = True
                            highrole = f'Highest role: {user.top_role.name}\n'
                            tcredits = '-----TUTLA CLIENT-----\n This bot is made by tutlamc#0 to support us join link in bio'
                            await channel.send(f'''```yml\n{name}{sid}{count}{cd}Is Bot: {'True' if user.bot else 'False'}\n{"Token First part: "+convert_to_base64(user.id)}\n{roles}{perms}{highrole}{tcredits}```''')
      
async def userinfo_callback(CommandObject,message,self,params,command_data):
                    channel = await self.fetch_channel(message.channel.id)
                    for user in message.mentions:
                            await userinfo_main(user,message.channel)
                    if len(message.mentions) is 0:
                            await userinfo_main(message.author, message.channel)
                            


userinfo_command = Command("userinfo","Check a user out!",userinfo_callback,INFO,aliases=['whois'],params=["USER PING"])