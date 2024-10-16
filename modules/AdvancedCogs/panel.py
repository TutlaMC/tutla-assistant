from ..Module import * 
from ..Utils import *

from data import db
import sys
from collections import deque


class PrintLogger:
    def __init__(self, logfile, max_logs=50):
        self.logfile = logfile
        self.log_queue = deque(maxlen=max_logs)
        self._original_stdout = sys.stdout
        sys.stdout = self

    def write(self, message):
        if message.strip():
            lines = message.splitlines()
            for line in lines:
                self.log_queue.append(line + "\n")
        self._original_stdout.write(message)

    def flush(self):
        pass

    def save_to_file(self):
        with open(self.logfile, 'w') as f:
            f.writelines(self.log_queue)

logger = PrintLogger('log.log')



class PanelGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    group = app_commands.Group(name="panel", description="Tutla Assistance Admin Panel")

    @group.command(name="log", description="Log")
    @app_commands.user_install()
    async def log(self, interaction: discord.Interaction):
        if getAdminLevel(interaction.user.id) ==4:
            logger.save_to_file()
            with open("log.log", "r") as f:
                await interaction.response.send_message(f"```python\n{f.read()}```")

    @group.command(name="shell", description="Tutla Shell")
    @app_commands.user_install()
    async def shell(self, interaction: discord.Interaction, execution: str):
        if getAdminLevel(interaction.user.id) ==4:
            await interaction.response.send_message(f"```python\nTutla Shell >{execution}\n{execute(execution)}```")
    
    @group.command(name="premium", description="Change premium")
    @app_commands.user_install()
    async def premiuM(self, interaction: discord.Interaction, user: discord.User):
        if getAdminLevel(interaction.user.id) >=2:
            premium_reload()
            pstat = db.getData(user.id,"premium")
            if not pstat:
                db.edit_user(user.id,premium=True)
                premium_reload()
                await interaction.response.send_message(f"Gave {user.mention} premium!",ephemeral=True)
            else:
                db.edit_user(user.id,premium=False)
                premium_reload()
                await interaction.response.send_message(f"Revoked premium off {user.mention}!",ephemeral=true)

    @group.command(name="ban", description="Change ban status")
    @app_commands.user_install()
    async def banneD(self, interaction: discord.Interaction, user: discord.User):
        if getAdminLevel(interaction.user.id) >=2:
            premium_reload()
            pstat = db.getData(user.id,"banned")
            if not pstat:
                db.edit_user(user.id,banned=True)
                premium_reload()
                await interaction.response.send_message(f"Banned {user.mention}",ephemeral=True)
            else:
                db.edit_user(user.id,baned=False)
                premium_reload()
                await interaction.response.send_message(f"Unbanned {user.mention}!",ephemeral=true)

    @group.command(name="edit", description="Edit user data")
    @app_commands.user_install()
    async def ediT(self, interaction: discord.Interaction, user: discord.User, data: str, changed: str):
        if getAdminLevel(interaction.user.id) ==4:
                if data == "xp":
                    db.edit_user(int(user.id),xp=int(changed))
                elif data == "aura":
                    db.edit_user(int(user.id),aura=int(changed))
                elif data == "premium":
                    db.edit_user(int(user.id),premium=bool(changed))
                elif data == "last_command":
                    db.edit_user(int(user.id),premium=changed)
                elif data == "coins": db.edit_user(int(user.id),coins=int(changed))
                await interaction.response.send_message(f"Edited {data} for {user.mention} to {changed} if the selected data exists",ephemeral=True)
    


async def setup(bot: commands.Bot):
    await bot.add_cog(PanelGroup(bot))

