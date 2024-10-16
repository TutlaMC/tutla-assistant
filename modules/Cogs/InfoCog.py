
from ..Module import *
from ..Utils import *
import discord
import requests
from io import BytesIO

async def userinfo_main(ctx:discord.Interaction,user:discord.User):
                            name = f'User Name: {user.global_name}\n'
                            sid =  f'User ID: {user.id}\n'
                            count= f'Joined user at: {user.joined_at}\n'
                            cd = f'User Creation Date: {user.created_at}\n'
                            cd+= f'Token (First Part): {base64.b64encode(str(user.id).encode()).decode()}\n'
                            roles = '---Roles---\n'
                            for i in user.roles:
                                roles = roles+i.name+' | '+'\n'
                            roles = roles+'\n'
                            perms = '---Permissions---\n'
                            mg = False
                            mr = False
                            ma = False
                            if hasattr(user, "roles"):
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
                            else: highrole = "Highest Role: None\n"
                            tcredits = '-----TUTLA CLIENT-----\n This bot is made by Tutla'
                            await ctx.response.send_message(f'''```yml\n{name}{sid}{count}{cd}Is Bot: {'True' if user.bot else 'False'}\n{"Token First part: "+convert_to_base64(user.id)}\n{roles}{perms}{highrole}{tcredits}```[Avatar:]({user.avatar.url})''')




class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="server", description="Get server data")
    @app_commands.check(commandCheck)
    async def serverinfo_callback(self,ctx:discord.Interaction,invite:str=None,id:int=None):
                        if invite:
                                inv = await ctx.client.fetch_invite(invite)
                                server = inv.guild
                        elif id:
                            server = await ctx.client.fetch_guild(id)
                        else:server = ctx.channel.guild
                                    
                        name = f'Server Name: {server.name}\n'
                        sid =  f'Server ID: {server.id}\n'
                        cd = f'Server Creation Date: {server.created_at}\n'
                        members = f'Members: {str(server.member_count)}\n'
                        channel_count = f'Channel Count: {str(len(server.channels))}\n'
                        own = await ctx.client.fetch_user(server.owner_id)
                        owner = f'Owner ID: {server.owner_id}\n'
                        owner_name = f'Owner Name: {own.name}\n'
                        owner_creation_date = f'Owner Creation Date: {own.created_at}\n' 
                        await ctx.response.send_message(f'''```yml\n{name}{sid}{members}{cd}{channel_count}-------OWNER INFO-------\n{owner}{owner_name}{owner_creation_date}\nYou can use /userinfo <@{own.id}> to get more data```\n[Icon]({server.icon.url})''')

    @app_commands.command(name="userinfo", description="Get user data")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def userinfo_callback(self,ctx:discord.Interaction,user:discord.User):
        await userinfo_main(ctx,user)

    @app_commands.command(name="word", description="Get info about a word")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def word_callback(self,ctx:discord.Interaction, word:str):
            await ctx.response.send_message("Getting word...",ephemeral=True)
            e = requests.get(f"https://ftapi.pythonanywhere.com/translate?dl=en&text={word}")

            
            f = e.json()
            final = "Definitions, Examples & Synoyms:\n"
            if not f["definitions"]: await ctx.followup.send("No word found"); return False
            if len(f["definitions"]) > 1:
                ee = 0
                for definition in f["definitions"]:
                        ee+=1
                        if ee == 4: break
                        final+=f"- {definition['definition']}\n - Example: {definition['example']}\n - Synonyms:\n"
                        if definition['synonyms'] != None:
                            for i in definition['synonyms']['']:
                                    final+=f"  - {i}\n"
                        else: final+="No Synonyms found\n"


                final+f'Characters: {str(len(word))}\n'
                final+=f"To hear pronounciation try `/say phrase:{word} hear:True`"
                await ctx.followup.send(final)
            else: await ctx.followup.send("No word found")




async def setup(bot: commands.Bot):
    await bot.add_cog(InfoCog(bot))