from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def role_callback(CommandObject,message,self,params,command_data):
    if message.author.guild_permissions.manage_roles:
                    failed = False
                    for i in message.mentions:
                         if not failed:
                              for role in message.role_mentions:
                                    try:
                                        await i.add_roles(role)
                                        await message.channel.send('Added roles to user')
                                    except Exception as e:
                                         failed = True
                                         await message.channel.send(f'I do not have permission to add roles to members, error log:```python\n{e}```')
    else: await message.channel.send('You do not have permission to add roles to members')
role_command = Command("role","role a user off the server",role_callback,ADMIN,aliases=["giverole"],usage="Give multiple roles to multiple users irrespecitvely",isfree=True)