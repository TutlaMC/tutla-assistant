
from ..Module import *
from ..Utils import *
from discord.ui import View, Button
import discord,requests,re,aiohttp,random
from io import BytesIO

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="coins",description="Gets your coins")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def coins_callback(self,ctx: discord.Interaction, user: discord.User = None):
        user = user or ctx.user
        await ctx.response.send_message(f"Coins: {str(int(db.getData(user.id,'coins')))}",silent=True)

    @app_commands.command(name="daily",description="Tutla Assistance daily")
    @app_commands.checks.cooldown(1, 60, key=lambda i: i.user.id)
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def daily_callback(self,ctx: discord.Interaction):
        last_daily = db.getData(ctx.user.id,"daily")
        now = datetime.now()
        
        format_str = '%Y-%m-%d %H:%M:%S'
        if last_daily == None: dt=datetime.now()
        passe = false
        try:
            dt = datetime.strptime(last_daily, format_str)
            passe = True
        except Exception: passe = False
        if passe == false: dt = datetime.strptime(last_daily, '%Y-%m-%d %H:%M:%S.%f')
        
        
        time_difference = now - dt
        
        seconds_diff = time_difference.total_seconds()
        if last_daily == None: seconds_diff = 100000
        if int(time_difference.total_seconds())<10: seconds_diff = 100000
        dlog(seconds_diff)
        if seconds_diff > 43200:
            nxp =20+random.randint(1,2000)
            ncs = 100+random.randint(1,1000)

            chance = 99999 if random.randint(1,10000) == 1 else 0
            if ctx.user.id in premium_list: 
                nxp+=1500
                ncs+=2000
            if chance != 0:
                f = "\n:peach: **BY RARE LUCK (0.01% chance) YOU GOT +99999 COINS** :peach:"
                db.add_coins(ctx.user.id,chance)
            else: f=""
            eaura = db.getData(ctx.user.id,"aura")
            db.add_coins(ctx.user.id,ncs)
            db.edit_user(ctx.user.id,xp= db.getData(ctx.user.id,"xp")+nxp,daily=now)
            e = '\n> Bonus: 1500 for premium' if ctx.user.id in premium_list else ''
            await ctx.response.send_message(f"> **Your daily:**\n> XP:{str(nxp)}> {e}{f}")
        else: await ctx.response.send_message(f"You have already claim your daily, you can claim again in {str(int(((43200-seconds_diff)/60)/60))} hours")
    @app_commands.command(name="pay",description="Pay a user in cash")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def give_callback(self,ctx: discord.Interaction, user: discord.User, cash: int):
                togive=cash
                if db.userExists(user.id):
                    mycoins = db.getData(ctx.user.id,"coins")
                    if mycoins < togive: 
                        await ctx.response.send_message("You don't have enough money to give!")
                        return False
                    else:
                        db.add_coins(user.id,coins=togive)
                        await ctx.response.send_message(f"Succesfully paid {user.mention} {str(togive)}!")
    @premium_command
    @app_commands.command(name="rob",description="Steal from someone")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def rob_callback(self,ctx: discord.Interaction, user: discord.User):
            if db.userExists(user.id):
                coins = db.getData(user.id,"coins")
                mycoins = db.getData(ctx.user.id,"coins")
                
                if coins in [None,0]: 
                    await ctx.response.send_message("User is broke")
                    return False
                if mycoins < coins/10: 
                    await ctx.response.send_message("You need atleast 10% of the users coins to rob them!")
                    return False
                if random.randint(1,10) <10:
                    db.add_coins(ctx.user.id,coins=-int((mycoins-(int(mycoins/10)))))
                    web = random.choice(["HOLY SHI! You lost all the coins because you escaped the police using a lawnmover","You managed to break in, but your non existant mom called you bcack for chores and you forgot to turn on do not disturb mode","you sneezed they heared you, the police came 2 seconds later","you fell asleep","they had a dog","your tail fell off","you managed to steal it but everyone saw you steal it. L rizz"])
                    await ctx.response.send_message(f"YOU **FAILED** stealing <@{user.id}>!:\nReason: `{web}`\nYou lost 10% of your coins")
                else:
                    cash = random.randint(1,int(coins))
                    if user.id in premium_list: cash*=1.5
                    db.add_coins(user.id,coins=-cash)
                    db.add_coins(ctx.user.id,coins=cash)
                    await ctx.response.send_message(f"{user.mention} You managed to steal {str(cash)} off {user.mention}! W Rizz")
    @app_commands.command(name="xp",description="Gets your XP")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def xp_callback(self,ctx: discord.Interaction, user: discord.User=None):
        user = user or ctx.user
        await ctx.response.send_message(f"XP: {str(int(db.getData(user.id,'xp')))}",silent=True)
async def setup(bot: commands.Bot):
    await bot.add_cog(EconomyCog(bot))