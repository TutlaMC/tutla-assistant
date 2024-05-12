from ..Module import * 
from ..Utils import * #import this if you need utility commands
async def userinfo_callback(CommandObject,message,self,params,command_data):
                    channel = await self.fetch_channel(message.channel.id)
                    if not len(message.mentions) == 0:
                        for server in message.mentions:
                            name = f'User Name: {server.name}\n'
                            sid =  f'User ID: {server.id}\n'
                            count= f'Joined server at: {server.joined_at}\n'
                            cd = f'User Creation Date: {server.created_at}\n'
                            roles = '---Roles---\n'
                            for i in server.roles:
                                roles = roles+i.name+' | '+'\n'
                            roles = roles+'\n'
                            perms = '---Permissions---\n'
                            mg = False
                            mr = False
                            ma = False
                            for i in server.roles: 
                                if i.permissions.manage_guild and not mg:
                                    perms += 'Manage Guild: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not mr:
                                    perms += 'Manage Roles: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not ma:
                                    perms += 'All Perms: True\n'
                                    ma = True
                            highrole = f'Highest role: {server.top_role.name}\n'
                            tcredits = '-----TUTLA CLIENT-----\n This bot is made by tutlamc#0 to support us join link in bio'
                            await channel.send(f'''```yml\n{name}{sid}{count}{cd}{"Token First part: "+convert_to_base64(server.id)}\n{roles}{perms}{highrole}{tcredits}```''')

userinfo_command = Command("userinfo","Check a user out!",userinfo_callback,INFO,aliases=['whois'],params=["USER PING"])