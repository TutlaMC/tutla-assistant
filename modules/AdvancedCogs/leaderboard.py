from ..Module import * 
from data import db

class LeaderBoardGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    group = app_commands.Group(name="leaderboard", description="Leaderboard")

    @group.command(name="coins",description="Coins Leaderboard")
    @app_commands.check(commandCheck)
    async def leaderboardC_callback(self,ctx: discord.Interaction):
        coinsl = db.get_column_data("coins")
        sorted_coins = dict(sorted((item for item in coinsl.items() if item[1] is not None), key=lambda item: item[1], reverse=True))

        final = "COINS LEADERBOARD\n"
        ee = 0
        for i in list(sorted_coins.keys())[:10]:
            ee+=1
            final+=f"#{str(ee)} <@{str(i)}>: {sorted_coins[i]}\n"
        final+=f"\n======================\nYour Position: {list(sorted_coins.keys()).index(ctx.user.id) + 1}"
        await ctx.response.send_message(final,silent=True)
        await ctx.response.send_message(final,silent=True)

    @group.command(name="xp",description="XP Leaderboard")
    @app_commands.check(commandCheck)
    async def leaderboardX_callback(self,ctx: discord.Interaction):
        xpl = db.get_column_data("xp")
        sorted_xp = dict(sorted((item for item in xpl.items() if item[1] is not None), key=lambda item: item[1], reverse=True))
        final = "XP LEADERBOARD\n"
        ee = 0
        for i in list(sorted_xp.keys())[:10]:
            ee+=1
            final+=f"#{str(ee)} <@{str(i)}>: {sorted_xp[i]}\n"
        final+=f"\n======================\nYour Position: {list(sorted_xp.keys()).index(ctx.user.id) + 1}"
        await ctx.response.send_message(final,silent=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(LeaderBoardGroup(bot))
