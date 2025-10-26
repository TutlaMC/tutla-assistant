
from ..Module import *
from ..Utils import *
from discord.ui import View, Button
from PIL import Image
import discord
import requests
import random
from io import BytesIO

url = "https://raw.githubusercontent.com/TutlaMC/tutla-assistant/main/changelog.md"
response = requests.get(url)
changelog = response.text






class ClientInfoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="changelog",description="What's new?")
    @app_commands.user_install()
    async def changelog(self,interaction: discord.Interaction):
        await interaction.response.send_message(changelog)


    

    @premium_command
    @app_commands.command(name="dm",description="DM a user")
    @app_commands.user_install()
    async def dm_callback(self,interaction: discord.Interaction,user:discord.User,text:str):
        await user.send(text)
        await interaction.response.send_message("Sent!",ephemeral=True)

    @app_commands.command(name="ping",description="Check the bot's latency")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def ping_callback(self,interaction: discord.Interaction):
        latency = interaction.client.latency * 1000  
        await interaction.response.send_message(f'Pong! Latency is {latency:.2f}ms')

    @app_commands.command(name="premium",description="Check if you're premium")
    @app_commands.user_install()
    async def premium_callback(self,interaction: discord.Interaction, user: discord.User = None):
            premium_reload()
            ban_reload()
            if user == None: user = interaction.user
            if user.id in premium_list: premium = true
            else: premium = False

            if premium: await interaction.response.send_message(f'{user.mention} has premium. Try out some cool premium commands!',silent=True) 
            else: await interaction.response.send_message(f'{user.mention} does not have premium & your missing out on so much! Get it [here for **5$**](https://tutla.net/shop/discord/tutla-assistance-premium/)',silent=True)
    @premium_command
    @app_commands.command(name="reload",description='Reload the bot data')
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def reload_callback(self,interaction: discord.Interaction):
        premium_reload()
        ban_reload()

    @app_commands.command(name="report",description='Report a bug/suggest')
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def report_callback(self,interaction: discord.Interaction, bug: str):
        reporto = await interaction.client.fetch_channel(logging_channel)
        id = random.randint(10000,99999)
        await reporto.send(f"Bug/Suggestion #{str(id)}:\n```yaml\n{bug}```\nReported By {interaction.user.mention}")
        await interaction.response.send_message(f":warning: Spamming Suggestions/Bug or False Reports will result in a Tutla Assistance Ban!:warning:\n Reported Bug ID: {str(id)}\n```yaml\n{bug}```")

    @app_commands.command(name="bugs",description='Lists bugs in the bot')
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def bugs_callback(self,interaction: discord.Interaction):
        reporto = await interaction.client.fetch_channel(logging_channel)
        final = "Bugs:\n"
        async for bug in reporto.history(limit=200):
            if "Bug/Suggestion" in bug.content:
                final+=f"- {bug.content}\n"

        await interaction.response.send_message(final,ephemeral=True)

    @premium_command
    @app_commands.command(name="say",description='Say something')
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def say_callback(self,ctx: discord.Interaction,phrase: str,hear:bool=False,user:discord.User=None,old:bool=False):
        await ctx.response.defer()
        if not hear:
            if "rizz" in phrase:
                await ctx.followup.send(f"{ctx.user.mention} you got NO rizz")
            if not user:
                to_say = phrase.replace('.say', '')
                for word in ["ban","kick","timeout","fuck","nigga","nigger","niger","niga"] : 
                        if word in to_say:
                            await ctx.followup.send("Flagged Text, cannot be executed")
                            return False
                if len(to_say) <=3:
                        await ctx.followup.send("Too small")
                        return False
                if to_say[0] in [".","!","?",",","/","*","^","$","#","@"]:
                        await ctx.response.send_message("Command Cannot be executed")
                        return False

                e = ""
                for word in to_say.split():
                        erm = False
                        for i in word: 
                            if not i.isascii():
                                erm= True
                        if not erm: 
                            e+=word+" "
                v2 = e
                censored = api("https://community-purgomalum.p.rapidapi.com/json","community-purgomalum.p.rapidapi.com",{"text":v2}).json()['result']
                censored = censored.replace('*','#')
                await ctx.followup.send(censored,silent=True)
            else:
                await ctx.followup.send("Sending message...",ephemeral=True)
                to_say = phrase.replace('.say', '')
                for word in ["ban","kick","timeout","fuck","nigga","nigger","niger","niga"] : 
                        if word in to_say:
                            await ctx.followup.send("Flagged Text, cannot be executed")
                            return False
                if len(to_say) <=3:
                        await ctx.followup.send("Too small")
                        return False
                if to_say[0] in [".","!","?",",","/","*","^","$","#","@"]:
                        await ctx.followup.send("Command Cannot be executed")
                        return False

                e = ""
                for word in to_say.split():
                        erm = False
                        for i in word: 
                            if not i.isascii():
                                erm= True
                        if not erm: 
                            e+=word+" "
                v2 = e
                censored = api("https://community-purgomalum.p.rapidapi.com/json","community-purgomalum.p.rapidapi.com",{"text":v2}).json()['result']
                censored = censored.replace('*','#')
                if old:
                    webhook = await ctx.channel.create_webhook(name=user.name, avatar=await user.avatar.read())
                    await webhook.send(content=censored, username=user.name, avatar_url=user.avatar.url, silent=True)
                    await webhook.delete()
                else:
                    params = {
                        "name": user.name,
                        "color": "white",
                        "time": f"Today at {datetime.now().strftime('%I:%M %p')}",
                        "avatar": user.avatar.url,
                        "text": censored
                    }

                    response = requests.get("https://tools.tutla.net/api/message", params=params)

                    image = Image.open(BytesIO(response.content))
                    width, height = image.size
                    crop_height = int(height * 0.85)
                    cropped = image.crop((0, 0, width, height - crop_height))

                    buffer = BytesIO()
                    cropped.save(buffer, format="PNG")
                    buffer.seek(0)

                    file = discord.File(buffer, filename="message.png")
                    await ctx.followup.send(file=file)

        else:
            word = phrase
            await ctx.followup.send("Getting pronounciation",ephemeral=True)
            e = requests.get(f"https://ftapi.pythonanywhere.com/translate?dl=en&text={word}")

            f = e.json()
            if not f["pronunciation"]: await ctx.response.send("No word found"); return False
            thing = f["pronunciation"]['source-text-audio']

            response = requests.get(thing)
            audio_file = BytesIO(response.content)
                            
            await ctx.followup.send(file=discord.File(fp=audio_file,filename="balls.mp3"))

    @app_commands.command(name="subscribe",description='Subscribe to Tutla feed')
    @app_commands.check(commandCheck)
    async def subscribe(self,interaction: discord.Interaction):
        
        message = interaction.message
        if interaction.user.guild_permissions.manage_guild or interaction.user.guild_permissions.manage_channels or getAdminLevel(interaction.user.id) >= 2:
            with open('data/subscribed.txt','r') as f:
                weeb = f.read()
            if str(interaction.channel_id) not in weeb:
                with open('data/subscribed.txt','w') as f:
                    weeb += str(interaction.channel_id)+'\n'
                    f.write(weeb)
                await interaction.response.send_message("Subscribed channel to Tutla Assistance Feed!")
            else: 
                with open('data/subscribed.txt','w') as f:
                    weeb = weeb.replace(str(interaction.channel_id),'')
                    weeb = weeb.replace('\n\n','')
                    f.write(weeb)
                await interaction.response.send_message("Unsubscribed channel to Tutla Assistance Feed!")
        else: await interaction.response.send_message("You need to have manage guild/channels permissions or be a Tutla Admin to subscribe this channel to tutla assistance")

        @app_commands.command(name="version",description='Tutla Assistance Version')
        @app_commands.user_install()
        async def version(self,interaction: discord.Interaction):
            await interaction.response.send_message(version)



async def setup(bot: commands.Bot):
    await bot.add_cog(ClientInfoCommands(bot))