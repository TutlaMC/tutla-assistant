import discord
from discord import app_commands
import random as ran
from discord.ext import tasks,commands
from math import *
import traceback




class Client(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        super().__init__(intents=intents,command_prefix='.')

    async def setup_hook(self):
        MainLogger.log("Loading all modules",style="execution")
        for filename in os.listdir('modules/Cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'modules.Cogs.{filename[:-3]}')
        
        for filename in os.listdir('modules/AdvancedCogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'modules.AdvancedCogs.{filename[:-3]}')
        await client.load_extension(f'modules.CLIENT.help')
        await self.tree.sync()

        MainLogger.log(f"Successfully loaded all modules, mods & {str(len(list(client.tree.walk_commands())))} commands!", style="success")
        
        



    async def on_ready(self):
        global bot
        bot = self
        
        
        MainLogger.log("Initializing Tutla Assistance",style="execution")
        
        premium_reload() # Util Command to get all premium users
        ban_reload()  
        DBLogger.log(db.printDB(),style="execution")

        await self.change_presence(status=discord.Status.idle, activity=discord.CustomActivity(name="tutla.net"))# j4j farm fr
        
        ModLogger.log("Initializing Mods",style="execution")
        for mode in mod.mods: # Mod Intializer
            mode.bot = self
            if mode.initial != None:
                await mode.initial()
        ModLogger.log("Sucessfully Intialized Mods",style="success")
        tutlashellThread = threading.Thread(target=tutlashell_input).start()
        mainloop.start(eself=self)
        if not dev_mode:
            dailyLoad.start(eself=self)
        MainLogger.log("Successfully Initialized Tutla Assistance!",style="success")



    
    async def on_message(self,message:discord.Message): 
        global premium_list       
        
        for mode in mod.mods: # Mod On Message
            if mode.onMessage != None:
                await mode.onMessage(message)

        
        
        if message.content == ".balls":
            await message.channel.send("https://tenor.com/view/balls-gif-22045792")
                        
  
        try:
            for i in message.mentions:
                if i.id in afk_users: await message.channel.send(f"<@{i.display_name}> is afk, for `{afk_users[i.id]}`",silent=True)
            if ran.randint(1,3) == 2:
                if message.content == f'<@{str(self.user.id)}>':
                        cc = ["CC Hack: You can get powerful hacks on the CC Scripting Forum that bypass various Minecraft anticheats such as Grim and Astro","CC Hack: Try `on tick on tick say 'blue screen'` in CCS to see a blue screen","CC Hack: You can easily get a cape by applying for mod @ the CC Discord (you'd get accepted if you weren't autistic)","CC Hack: Use the I-No-oNe's AutoCC Updater to automatically update ClickCrystals",'CC Hack: You can make CC a ghostclient with I-No-oNe CC Addon']
                        life = ["Lifehack: To getter jawline you can start mewing.", "Lifehack: Meditate when on you're on bed. It'll be a win-win.","Lifehack: To make yourself harder you can try kegel exercises","Lifehack: Get a clean pant-hook by folding up thrice and then that fold downwards until inside.","Lifehack: Mentally curing yourself (by imagining your being cured as if your drank a medicine) is the cheapest, natural and best option","Lifehack: You can increase the size of yo gyatt by doin gyatt exercises",
                                "Lifehack: Add a 'because' to a request, it increases it's approval by 30% ","Lifehack: To get rid of acne, don't touch it","Lifehack: Keep your spine erect (same applies down at the corridor). It's better for growth, displays confidence and increases self esteem",'Lifehack: To find out if soeone is lying, get them in a neutral state (by asking a few simple boring questions) and then ask a question related to the lie. See their reaction']
                        ta = ["Tutla Hack: Reduce 25% on Shop- You can save a lot of money on Tutla Premium by buying Tutla Perks to get a 25% coupon.","Tutla Hack: You can get Tutla Assistance Premium by begging @tutlaasssistance","Tutla Hack: Save 10 seconds opening a calculator orusing your retarded brain trying to claculate by using `.calc`","Tutla Hack: You can get a full stock by trading with a Tutla Owner","Tutla Hack: You can get 5 Members to your Discord server by trading out your Tutla XP/5 for every 5 J4J Coins"
                            "Tutla Easter Egg: Theres only one command with a special character in it","Tutla Easter Egg: There are only two racist commands","Tutla Hack: You can check your aura by saying `whats my aura` in chat","Tutla Hack: Some commands have aliases that are one character like `.l` and `.v`","Tutla Easter Egg: Underlines hacks when pinging @tutlaassistance are VERY rare (0.4% chance & 0.1% in earlier ones), there are 3 of the rare ones"]
                        all = [cc, life, ta]
                        if ran.randint(1,250) == 69: await message.channel.send(ran.choice(["__Tutla Hack: You an suck deez nutz via tutla.fuck.tutlamc.cock:suck(hard=True, spit=5, time=Time.Seconds(69)*420)__","__Life Hack: You can become Andrew Tate through various methods:\n- Becoming one of doz Dropshipping Ytbers\n- Selling your kidneys\n- Selling someone\n- Ripping parts of someone (and sellin em ofc)__",'__When someone is white and you wanna call them an N, use a W instead 🗣️__']))
                        else: await message.channel.send(ran.choice(ran.choice(all)))
            
                if ran.randint(1,(message.guild.member_count/2)) == 2 or self.user in message.mentions: 
                    await message.reply(requests.get("https://thesimpsonsquoteapi.glitch.me/quotes").json()[0]['quote'])
        except Exception: MainLogger.log("No yap",style="warning" )
    
    

        
       

        

    async def on_message_delete(self,message):
         for module in mod.mods: # Mod on_delete
            if module.onDelete != None:
                await module.onDelete(message) 
    async def on_message_edit(self,before,after):
         for module in mod.mods: # Mod on_edit
            if module.onEdit != None:
                await module.onEdit(before,after) 

client = Client()


from data import db

from modules.Utils import *
ModLogger.log("Importing Mods",style="execution")
if __name__ == "__main__":
    import mods.ClickCrystalsBot
    import mods.SniperMod
    import mods.sudo
    from mods import mod



import threading






def tutlashell_input():
    MainLogger.log("Loading Tutla Shell",style="execution")
    while True:
        cmd = input("Tutla Shell > ")
        ShellLogger.log(execute(cmd)) # Utils command

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 2)
        await ctx.send(
            f"This command is on cooldown. Try again in {retry_after} seconds.",
            ephemeral=True
        )
    else:

        await ctx.response.send_message(f'Oops! Something went wrong.\n```python{str(error)}```', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)

@tasks.loop(minutes=5)
async def mainloop(eself):
        MainLogger.log("Refreshing Tutla Assistance", style="execution")
        self = eself

        # Mods
        MainLogger.log("Running Mod mainloops", style="execution")
        for mode in mod.mods: 
            if mode.mainloop != None:
                await mode.mainloop(self)
        
        # Data
        premium_reload()
        ban_reload()


        MainLogger.log("Refreshed Tutla Assistance", style="success")

@tasks.loop(hours=24)
async def dailyLoad(eself):
    global question_otd
    MainLogger.log("Intializing Daily Load",style="debug")
    self = eself
    reporto = await self.fetch_channel(logging_channel)
    f = True
    async for msg in reporto.history(limit=20):
        if "qotd" in msg.content.lower() and f:
            question_otd = msg.content
            await msg.delete()
            f = False
        if not f: break

    await sendToSubScribers(self,question_otd)
    MainLogger.log("Done with daily load",style="success")


if __name__ == "__main__":
    client.run(os.getenv('TOKEN'))
