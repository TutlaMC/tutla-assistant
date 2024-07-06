from ..Module import *
async def serverinfo_callback(CommandObject,message,self,params, command_data):
                    con = command_data['member']
                    premium = command_data['premium']

                    channel = message.channel
                    
                    if len(params) < 2:
                        server = message.channel.guild
                        
                    else: 
                            if params[1].isdigit():
                                server = await self.fetch_guild(int(params[1]))
                            elif "discord.gg" in params[1]:
                                inv = await self.fetch_invite(params[1])
                                server = inv.guild
                    name = f'Server Name: {server.name}\n'
                    sid =  f'Server ID: {server.id}\n'
                    cd = f'Server Creation Date: {server.created_at}\n'
                    members = f'Members: {str(server.online_count)}/{str(server.member_count)} Online\n'
                    channel_count = f'Channel Count: {str(len(server.channels))}\n'
                    own = await self.fetch_user(server.owner_id)
                    owner = f'Owner ID: {server.owner_id}\n'
                    owner_name = f'Owner Name: {own.name}\n'
                    owner_creation_date = f'Owner Creation Date: {own.created_at}\n' 
                    await channel.send(f'''```yml\n {name}{sid}{members}{cd}{channel_count}-------OWNER INFO-------\n{owner}{owner_name}{owner_creation_date}\nYou can use .userinfo <@{own.id}> to get more data```''')
                    if not con: free_access = True

serverinfo_command = Command("serverinfo", 'Lists information about the server', serverinfo_callback, INFO, aliases=['serverinfo', 'server',"inviteinfo"])