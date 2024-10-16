from ..Module import *

from ..Utils import version

url = "https://raw.githubusercontent.com/TutlaMC/tutla-assistant/main/TOS.md"
response = requests.get(url)
tos_text = response.text
    
class HelpMenu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="About the bot", description="Bot basic info, details and credits", emoji="❓",value="about"),
            discord.SelectOption(label="Adding the bot", description="How to add the bot", emoji="➕", value="add"),
            discord.SelectOption(label="Terms & Conditions", description="Usage Policies for Tutla Assistance", emoji="📜",value="tos")

        ]
        super().__init__(placeholder="Choose an option...", min_values=1, max_values=1, options=options)

    async def callback(self, ctx: discord.Interaction):
        if self.values[0] == "about":
            await ctx.response.send_message(about,ephemeral=True)
        elif self.values[0] == "add":
            await ctx.response.send_message("Use me and get to use cool tools, fun commands, music playing, economy, and more!",view=AddBot())
        elif self.values[0] == "tos":
            await ctx.response.send_message(f'Here is the TOS: {TOS}',ephemeral=True)


class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpMenu())

class AddBot(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(label="Use me anywhere", style=discord.ButtonStyle.link, url="https://discord.com/oauth2/authorize?client_id=1285609530633490533&integration_type=1&scope=applications.commands"))
        self.add_item(discord.ui.Button(label="Use me in your server", style=discord.ButtonStyle.link, url="https://discord.com/oauth2/authorize?client_id=1285609530633490533&permissions=8&integration_type=0&scope=applications.commands+bot"))
        self.add_item(discord.ui.Button(label="Add without permissions", style=discord.ButtonStyle.link, url="https://discord.com/oauth2/authorize?client_id=1285609530633490533&integration_type=0&scope=applications.commands+bot"))
    

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add",description="Add the bot")
    @app_commands.user_install()
    async def add_callback(self,interaction: discord.Interaction):
        await interaction.response.send_message("Use me and get to use cool tools, fun commands, music playing, economy, and more!",view=AddBot())

    @app_commands.command(name="help",description="List commands or get info about a command")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def help_callback(self,ctx: discord.Interaction, page: int = 1, command: str = None):
        pages = []

        def append_page(content, new_line=False):
            if new_line:
                content += '\n'
            if pages:
                if len(pages[-1].description) <= 1500:
                    pages[-1].description += content
                else:
                    new_embed = discord.Embed(description=content,color=discord.Color.blue())
                    pages.append(new_embed)
            else:
                new_embed = discord.Embed(description=content)
                pages.append(new_embed)

        def commandify(cmd, sub=False):
            if isinstance(cmd, discord.app_commands.Group): 
                return f'### {cmd.name.upper()}'

            final = f"**/{cmd.name}"
            if hasattr(cmd, "parent") and cmd.parent is not None:
                final = f"/{cmd.parent.name} {cmd.name}"

            for i in cmd.parameters:
                final += f" `[{'' if i.required else 'Optional: '}{i.name}]`"

            if hasattr(cmd, 'premium'):
                final += " 🔮"
            
            final += f"**\n {cmd.description}\n"
            return final
        
        def collect_cog_commands(bot):
            cog_commands = []
            for cog in bot.cogs.values():
                if isinstance(cog, commands.Cog):
                    for app_cmd in cog.__cog_app_commands__:
                        cog_commands.append(app_cmd)
            return cog_commands
        epic_list = collect_cog_commands(ctx.client)
        for cmd in list(ctx.client.tree.walk_commands()): epic_list.append(cmd)
        for cmd in epic_list:
            dlog(cmd.name)
            if isinstance(cmd, app_commands.Group):
                append_page(commandify(cmd), new_line=True)
            elif hasattr(cmd,"parent"):
                
                append_page(commandify(cmd), new_line=True)
            else:
                append_page(commandify(cmd), new_line=True)

        nmessage = f"Hi, I'm the Tutla Assistance {version} and can run the following {len(list(ctx.client.tree.walk_commands()))} Commands:"
        if command == None:
            if len(pages) < page:
                await ctx.response.send_message(f'No page found with number {str(page)}')
            else:
                nmessage += f'\n\n------------------------ PAGE {str(page)}/{len(pages)} ------------------------\n'
                await ctx.response.send_message(nmessage, view=HelpView(),embed=pages[page-1])
        else:
            cmd = ctx.client.tree.get_command(command)
            if cmd:
                await ctx.response.send_message(commandify(cmd))
            else:
                await ctx.response.send_message(f'Command "{command}" is not found!')
    
async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCog(bot))