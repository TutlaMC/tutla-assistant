from ..Module import * 

from ..Utils import *
import os

class ListGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    group = app_commands.Group(name="list", description="List command")

    @group.command(name="premium_users", description="List all premium users")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def listpu(self, interaction: discord.Interaction):
                premium_reload()
                nmessage = "__Premium Users__\n"
                for i in premium_list:nmessage += f"- @<{str(i)}>\n"
                await interaction.response.send_message(nmessage,ephemeral=True)
    
    @group.command(name="premium_commands", description="List all premium commands")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def listpc(self, interaction: discord.Interaction):
                final = ""
                for category, category_data in commands2.items():                    
                        for command_name, command_object in category_data['commands'].items():
                                if command_object.ispremium: final+=f"{command_object.name}: {command_object.description}\n"
                await interaction.response.send_message(f"```yaml\nPremium Commands:\n{final}```")



    @group.command(name="mods", description="List all mods")
    @app_commands.user_install()
    async def listmods(self, interaction: discord.Interaction):
        nmessage = 'Mods:\n```yaml\n'
        for i in mod.mods:
            nmessage+=f'- {i.name}: {i.description}\n'
        nmessage+='```'
        await interaction.response.send_message(nmessage)

    @group.command(name="fonts", description="List all fonts")
    @app_commands.user_install()
    async def listfonts(self, interaction: discord.Interaction):
        nmessage = 'Fonts:\n```yaml\n'
        for i in fonts:nmessage+='- '+i+'\n'
        nmessage+='```'
        await interaction.response.send_message(nmessage)

async def setup(bot: commands.Bot):
    await bot.add_cog(ListGroup(bot))
