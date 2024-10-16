
from ..Module import *
from ..Utils import *
from discord.ui import View, Button
import discord,requests,re,aiohttp,random
from io import BytesIO
from bs4 import BeautifulSoup
from discord import File


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['current_condition'][0]
    else:
        return None
freaky = {'a': '𝓪',
 'b': '𝓫',
 'c': '𝓬',
 'd': '𝓭',
 'e': '𝓮',
 'f': '𝓯',
 'g': '𝓰',
 'h': '𝓱',
 'i': '𝓲',
 'j': '𝓳',
 'k': '𝓴',
 'l': '𝓵',
 'm': '𝓶',
 'n': '𝓷',
 'o': '𝓸',
 'p': '𝓹',
 'q': '𝓺',
 'r': '𝓻',
 's': '𝓼',
 't': '𝓽',
 'u': '𝓾',
 'v': '𝓿',
 'w': '𝔀',
 'x': '𝔁',
 'y': '𝔂',
 'z': '𝔃',
 'A': '𝓐',
 'B': '𝓑',
 'C': '𝓒',
 'D': '𝓓',
 'E': '𝓔',
 'F': '𝓕',
 'G': '𝓖',
 'H': '𝓗',
 'I': '𝓘',
 'J': '𝓙',
 'K': '𝓚',
 'L': '𝓛',
 'M': '𝓜',
 'N': '𝓝',
 'O': '𝓞',
 'P': '𝓟',
 'Q': '𝓠',
 'R': '𝓡',
 'S': '𝓢',
 'T': '𝓣',
 'U': '𝓤',
 'V': '𝓥',
 'W': '𝓦',
 'X': '𝓧',
 'Y': '𝓨',
 'Z': '𝓩'}

class AnsiTutorialEmbed(View):
    @discord.ui.button(label="Usage Tutorial", style=discord.ButtonStyle.secondary)
    async def button_callback(self, button: Button, interaction: discord.Interaction):
        await interaction.response.send_message("""Here's a small explanation: [(text)[<color></color><highlight></highlight>|<bold></bold><underline></underline>]]  | Converts your text into cool ansi text: Usage (HTML like usage):
<red></red><green></green><blue></blue><yellow></yellow><pink></pink><cyan></cyan><gray></gray>
Background Colors: <firefly-dark-blue></firefly-dark-blue><orange></orange><marble-blue></marble-blue><greyish-turquoise></greyish-turquoise><gray></gray><indigo></indigo><light-gray></light-gray><white></white>
Other Formats: <bold></bold> <highlight></highlight) -> (for background)     <underline></underline>
                                                                                         
Ex: <blue>Weeb</blue> I'm <bold><underline>Cool</bold></underline>""")
        
def convert_currency(amt, from_cur, to_cur):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][to_cur]
        return amt * rate
    else:
        return None


class ToolsCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="ansiformat",description="Format in ANSI Text")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def ansi_callback(self,ctx:discord.Interaction,text:str):
                        formatted_message = text

                        text_color_mapping = {
                            '30': 'gray',
                            '31': 'red',
                            '32': 'green',
                            '33': 'yellow',
                            '34': 'blue',
                            '35': 'pink',
                            '36': 'cyan',
                            '37': 'white'
                        }

                        background_color_mapping = {
                            '40': 'firefly-dark-blue',
                            '41': 'orange',
                            '42': 'marble-blue',
                            '43': 'greyish-turquoise',
                            '44': 'gray',
                            '45': 'indigo',
                            '46': 'light-gray',
                            '47': 'white'
                        }

                        current_fg_color = None  
                        current_bg_color = None 

                        for code, color in background_color_mapping.items():
                            formatted_message = formatted_message.replace(f'<bg-{color}>', f'\033[{code}m')
                            current_bg_color = code  


                        for code, color in text_color_mapping.items():
                            formatted_message = formatted_message.replace(f'<{color}>', f'\033[{code}m')
                            current_fg_color = code 
                            formatted_message = formatted_message.replace(f'</{color}>', f'\033[{current_fg_color}m')


                        formatted_message = formatted_message.replace('<bold>', '\033[1m') \
                                                            .replace('</bold>', '\033[0m') \
                                                            .replace('<underline>', '\033[4m') \
                                                            .replace('</underline>', '\033[0m') \
                                                            .replace('<highlight>', '\033[7m') \
                                                            .replace('</highlight>', '\033[0m')
                        
                        embd = AnsiTutorialEmbed()
                        await ctx.response.send_message(f'```ansi\n{formatted_message}\033[0m```',view=embd)

    @app_commands.command(name="afk",description="Set your afk")
    @app_commands.check(commandCheck)
    async def afk_callback(self,ctx:discord.Interaction,reason:str):
        if reason == "": reason = "No reason specified"
        if not ctx.user.id in afk_users:
            afk_users[ctx.user.id] = reason
            await ctx.response.send_message("You are now afk!")
        else:
            afk_users.pop(ctx.user.id,None)
            await ctx.response.send_message("You are no longer in afk")

    @app_commands.command(name="8ball",description="Ultimate Decision Maker")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def ball_callback(self,ctx:discord.Interaction, question:str):
                            if not question.endswith('?'):await ctx.response.send_message(random.choice(["No 100%",
                                                                    "Yes bruh",
                                                                    "Roll **harder**",
                                                                    "wtf",
                                                                    "Obviously",
                                                                    "none of the above",
                                                                    "provide mroe context",
                                                                    "sounds like smth ur gramma would say",
                                                                    'no talk ez yas',
                                                                    'nah','no dude',
                                                                    'yas :thumbsup:',
                                                                    ":thumbsdown:",
                                                                    "*yeets balls over face*",
                                                                    "prolly nah",
                                                                    "you forgot to press my *buttons*",
                                                                    "yes if there's e innit",
                                                                    "ain cool, so no",
                                                                    "if mexican yes",
                                                                    "kys ||keep yourself safe :thumbsup:||",
                                                                    f"Yes definetly",
                                                                    f"No ofc not you dumbahh",
                                                                    "that's gaytdom",
                                                                    "the one that supports gaytdom",                                                              "If taco man yes",
                                                                    "sounds like autism ",
                                                                    "option 1",
                                                                    "whatever your gut says",
                                                                    "all mine",
                                                                    "ain sigma",
                                                                    "ouf",
                                                                    "# 🇬🇦🇾🇹🇩🇴🇲",
                                                                    "[idc](https://media.discordapp.net/stickers/1193539237153357885.png?size=160&name=idc)",
                                                                    "[measf](https://media.discordapp.net/stickers/1201906160622637157.png?size=160&name=measf)",
                                                                    "[mate](https://media.discordapp.net/stickers/1256231390576381952.gif?size=160&name=mate)",
                                                                    "[notsupport](https://media.discordapp.net/stickers/1192829101547991220.png?size=160&name=notsupport)"])+f"\n-# Question: {question}")
                            else: await ctx.response.send_message(f"No 100%\n-# Question: {question}")     

    @app_commands.command(name="coinflip",description="Unbiased coinflip")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def coinflip_callback(self,ctx:discord.Interaction, coins:int = None):
        def hot(roll): return f"{'Heads' if roll == 1 else 'Tails'}"
        if not coins==None:
                if hasCoins(ctx.user.id,coins):
                    roll = random.randint(1,2)
                    if roll == random.randint(1,2):
                        db.add_coins(ctx.user.id,coins*2)
                        await ctx.response.send_message(f"You got {hot(roll)} and won {str(coins*2)}")
                    else: 
                        db.add_coins(ctx.user.id,-coins)
                        await ctx.response.send_message(f"You rolled {hot(roll)} and lost it all :(")
                else: await ctx.response.send_message(f"You do not have {str(coins)} coins to bet")
        else: await ctx.response.send_message(f"{hot(random.randint(1,2))}")

    @app_commands.command(name="dice",description="Roll a dice!")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def dice_callback(self,ctx:discord.Interaction, coins:int=None):
        await ctx.response.send_message("Rolling",ephemeral=True)
        if coins != None:
                coins = int(coins)
                if hasCoins(ctx.user.id,coins):
                    roll = random.randint(1,6)
                    if roll == random.randint(1,6):
                        db.add_coins(ctx.user.id,coins*4)
                        await ctx.followup.send(f"You rolled {str(roll)} and won {str(coins*4)}")
                    else: 
                        db.add_coins(ctx.user.id,-coins)
                        await ctx.followup.send(f"You rolled {str(roll)} and lost it all :(")
                else: await ctx.followup.send(f"You do not have {coins} coins to bet")
        else: await ctx.followup.send(f"Dice Roll: {str(random.randint(1,6))}")

    @app_commands.command(name="convert",description="Convert different units")
    @app_commands.describe(mtype="Select a measurement type")
    @app_commands.choices(mtype=[
        app_commands.Choice(name="Currency", value="currency"),
        app_commands.Choice(name="Length", value="length"),
        app_commands.Choice(name="Weight", value="weight"),
        app_commands.Choice(name="Area", value="area"),
        app_commands.Choice(name="Volume", value="volume"),
        app_commands.Choice(name="Temperature", value="temperature"),
        app_commands.Choice(name="Speed", value="speed"),
        app_commands.Choice(name="Pressure",value="pressure")
    ])
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def convert_callback(self,ctx:discord.Interaction,mtype:str,from_unit:str,to_unit:str, amount:int):
        await ctx.response.send_message("Converting...",ephemeral=True)
        if mtype !="currency":
            
            e1=api("https://unit-measurement-conversion.p.rapidapi.com/list","unit-measurement-conversion.p.rapidapi.com",{})
            e1  = e1.json()
            for i in e1:
                for measurement in i:
                    for thing in measurement['measurements']:
                        if thing['abbr'] == from_unit:
                            from_unit = thing['unit']
                        if thing['abbr'] == to_unit:
                            to_unit = thing['unit']


            try:
                    e = api("https://unit-measurement-conversion.p.rapidapi.com/convert","unit-measurement-conversion.p.rapidapi.com",{"type":mtype,"fromUnit":from_unit,"toUnit":to_unit,"fromValue":amount})

                    await ctx.followup.send(f"{e.json()['value']} {e.json()['abbreviation']}s")
            except Exception as er:
                    await ctx.followup.send(f"Error in Object:\n```json\n{str(er)}```\n```json\n{e.json()}```")
        else:
            amt = float(amount)
            from_cur = from_unit.upper()
            to_cur = to_unit.upper()
            converted_amt = convert_currency(amt, from_cur, to_cur)
            if converted_amt:
                await ctx.followup.send(
                    f"{amt} {from_cur} is equal to {converted_amt:.2f} {to_cur}"
                )
            else:
                await ctx.followup.send("smoll error, report bug if it happens again")

    @app_commands.command(name="emoji",description="Use an emoji anywhere")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def fakemoji_callback(self,ctx:discord.Interaction,emoji:str):
        emoji_id = emoji.split(':')[-1].strip('>')
        emoji_url = f'https://cdn.discordapp.com/emojis/{emoji_id}.png'


        await ctx.response.send_message(f"Copy the text below and send it (ANYWHERE ON DISCORD) to use it as an emoji: ```[.]({emoji_url})```")
                        
    @app_commands.command(name="pokemon",description="Get a pokemon character's data")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def pokemon_callback(self,ctx:discord.Interaction,pokemon:str):
        await ctx.response.send_message("Exploring the poke-world...",ephemeral=True)
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
        response = requests.get(url)
        
        if response.status_code != 200:
            return f"Error: Pokémon '{pokemon}' not found."
        
        data = response.json()
        
        weight = f"__INFO__\n**Weight:** {data['weight'] / 10}kg"
        height = f"**Height:** {data['height'] / 10}m"
        
        abilities = ', '.join([ability['ability']['name'] for ability in data['abilities']])
        abilities_str = f"**Abilities:** {abilities}"
        
        types = ', '.join([type_info['type']['name'] for type_info in data['types']])
        types_str = f"**Type:** {types}"
        
        stats = ', '.join([f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}" for stat in data['stats']])
        stats_str = f"\n__Stats__\n"
        for stat in data['stats']:
            stats_str+=f"**{stat['stat']['name'].capitalize()}:** {stat['base_stat']}\n"
        
        moves = ', '.join([move['move']['name'] for move in data['moves']])  # limit to 5 moves for simplicity
        moves_str = f"**Moves**: {moves}"
        
        await ctx.followup.send(f"`{pokemon}`:\n {weight}\n{height}\n{abilities_str}\n{types_str}\n{stats_str}\n{moves_str}")

    @app_commands.command(name="freaky",description="Freaky text")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def freaky_callback(self,ctx:discord.Interaction,text:str):
        ntext = ''
        for i in text:
            if i in freaky: ntext+=freaky[i]
            else: ntext+=i
        ntext+=f'\n-# Text: {text}'
        await ctx.response.send_message(ntext,silent=True)

    @app_commands.command(name="poll",description="Create a poll")
    @app_commands.describe(options="Options must be seperated with commas")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def poll_callback(self,ctx:discord.Interaction,question:str,options:str):
        
        await ctx.response.send_message("Creating poll")
        def number_to_emoji(number):
            num_str = str(number)
            emoji_map = {
                '0': '0️⃣',
                '1': '1️⃣',
                '2': '2️⃣',
                '3': '3️⃣',
                '4': '4️⃣',
                '5': '5️⃣',
                '6': '6️⃣',
                '7': '7️⃣',
                '8': '8️⃣',
                '9': '9️⃣'
            }
            return ''.join(emoji_map[digit] for digit in num_str)
        e = options.split(',')
        question = e[0]
        if len(e) <= 6:
            final = f"## Poll 📊\n**Question: {question}**\n"
            count = 0
            for i in e[1:]:
                count+=1
                final+=f"#{str(count)}: {i}\n"
            msg = await ctx.followup.send(final)
            for i in range(count):
                
                await msg.add_reaction(number_to_emoji(i+1))
        else: await ctx.followup.send("Too many options (Max 6)")

    @app_commands.command(name="random",description="Random choice")
    @app_commands.describe(type="Select random type")
    @app_commands.choices(type=[
        app_commands.Choice(name="Number", value="number"),
        app_commands.Choice(name="User", value="user"),
        app_commands.Choice(name="Image", value="image"),
        app_commands.Choice(name="ProfilePicture", value="pfp"),
        app_commands.Choice(name="Burger",value="burger")
    ])
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def random_callback(self,ctx:discord.Interaction, type:str, range_start:int=0, range_end:int=100,mention:bool=False):

                            if type == 'number':
                                await ctx.response.send_message('Selected: ' +str(random.randint(range_start,range_end))) 
                            elif type == 'user':
                                if ctx.channel.guild: 

                                    channels = await ctx.guild.fetch_channels()
                                    members = await ctx.guild.fetch_members(channels=channels, force_scraping=True, cache=False)
                                    if mention:
                                            if members[0]:
                                                await ctx.response.send_message('Selected: '+random.choice(members).mention)
                                            else: await ctx.response.send_message('No members in guild')
                                    else:
                                            if members[0]:
                                                await ctx.response.send_message('Selected: '+random.choice(members).name)
                                            else: await ctx.response.send_message('No members in guild')

                                else: await ctx.response.send_message('Guild not found.')
                            elif type == "image":
                                api_url = f'https://picsum.photos/512/512'
                                r = requests.get(api_url)

                                await ctx.response.send_message(f"Random Image:",file=File(fp=BytesIO(r.content),filename='image.jpg'))
                            elif type == "pfp":
                                api_url = f'https://loremflickr.com/320/240'
                                r = requests.get(api_url)

                                await ctx.response.send_message(f"Random PFP:",file=File(fp=BytesIO(r.content),filename='pfp.jpg'))
                            elif type=="burger":
                                r = requests.get("https://foodish-api.com/api/images/burger")
                                r = r.json()['image']
                                await ctx.response.send_message(r)

    @app_commands.command(name="regional",description="Create regional text")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def regional_callback(self,ctx:discord.Interaction,text:str):
                        stuff = text
                        newm = ''
                        variables_list = []

                        start_letter = ord('A')
                        end_letter = ord('Z')

                        for letter_code in range(start_letter, end_letter + 1):
                                letter = chr(letter_code)
                                variable_value = f':regional_indicator_{letter.lower()}:'
                                variables_list.append(variable_value)
                        for i in stuff:
                            
                            nletter = i.lower()
                            ascii_value = ord(nletter)

                            position = ascii_value - ord('a')
                            if i == ' ':
                                    newm+='      '
                            try:
                                newm += variables_list[position]+" "
                            except Exception:
                                pass
                                

                        await ctx.response.send_message(newm)

    

    @app_commands.command(name="roast",description="Roast/Insult")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def roast_callback(self,ctx:discord.Interaction,user:discord.User):
        r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        r = r.json()
        await ctx.response.send_message(f'{user.mention} {r["insult"]}')

    @app_commands.command(name="time",description="Convert timezones")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def convert_time(self,interaction: discord.Interaction, time: str, from_tz: str, to_tz: str):
            url = f"https://www.timeapi.io/api/conversion/converttimezone"
            params = {
                "fromTimeZone": from_tz,
                "toTimeZone": to_tz,
                "dateTime": time,
                "dstAmbiguity": ""
            }

            response = requests.post(url, params=params,headers={'accept': 'application/json', 'Content-Type': 'application/json'})
            print(response.json())
            if response.status_code == 200:
                data = response.json()
                converted_time = data['convertedDateTime']
                await interaction.response.send_message(f"Converted time: {converted_time}")
            else:
                await interaction.response.send_message("Failed to convert time!. Time zone must be `Continent/Country` for example `Asia/Kolkata` and time must be `Y-M-D H:M:S` -> Military time, digits must always be 2 (03 for march for example).\nEx command: ``")

    @app_commands.command(name="brain",description="Make ppl use their brain")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def brain(self,ctx:discord.Interaction):
         await ctx.response.send_message("""
## Use your brain
1. **[Don't ask to ask](https://dontasktoask.com)**
2. **Google it**
-# Any information I give you will likely be the first search result I find on google. So just do us both a favor and do it yourself. It will also save you time, as you don't have to wait for me to respond! 
3. **[Don't just say hello in chat](<https://nohello.net>)**. Instead, __Just ask the question__! 🤯😊👏🏻
4. Use proper channels  
-# Do not ask in someone's DMs if there is a valid support channel or ticket system in your server of origin. Asking in DMs makes it harder for other people to find a solution to the same problem. Unless your problem may potentialy reveal private information, always use publicly available support channels.                                     
5. Ask about the problem not your solution
Guy> `How do I increase the font size in my header?`
Dev> `Add a "font-size:" tag to your header class`
Dev> `Why do you want to increase it?`
Guy> `Im trying to make it stand out`
Dev> `Got it. Consider using a larger font size and maybe some styling effects like bold or color to make it stand out even more`
Guy> `Ah, thank you! I didn't think about that.`

Make sure to always share the bigger picture, and provide detail. If someone asks for more information, please provide it    

Taken from [trouper.me](<https://trouper.me>)                        
""")

    @app_commands.command(name="translate",description="Translate text")
    @app_commands.describe(from_language="Can be 'detect' or lanuage code")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def translate_callback(self,ctx:discord.Interaction,from_language:str,to_language:str,text:str):
            await ctx.response.send_message("Translating...",ephemeral=True)

            lang = from_language.upper()
            lang2 = to_language.upper()

            if lang == "detect":
                e = requests.get(f"https://ftapi.pythonanywhere.com/translate?dl={lang2}&text={text}")
            else: 
                e = requests.get(f"https://ftapi.pythonanywhere.com/translate?sl={lang}&dl={lang2}&text={text}")

            await ctx.followup.send(f'`{lang}` to `{lang2}`: {str(e.json()["translations"]["possible-translations"][0])}\n-# Source Text: {text}')

    @app_commands.command(name="urlshortner",description="Shorten a url")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def urlshortner_callback(self,ctx:discord.Interaction,url:str):
        await ctx.response.send_message("Shortening url...",ephemeral=True)
        headers = {
            "x-rapidapi-key": rapid_api_key,
            "x-rapidapi-host": "fast-url-shortener1.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        e = requests.post("https://fast-url-shortener1.p.rapidapi.com/shorten", json={ "url": url }, headers=headers)
        await ctx.followup.send(e.json()['shortened'])

    @app_commands.command(name="weather",description="Get a city's weather data")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def weather_callback(self,ctx:discord.Interaction,city:str):
        await ctx.followup.send("Getting weather data from city...",ephemeral=True)
        weather = get_weather(city)
        if weather:
            await ctx.followup.send(
                f"Weather in {city}:\n"
                f"- Description: {weather['weatherDesc'][0]['value']}\n"
                f"- Temperature: {weather['temp_C']}°C\n"
                f"- Cloud Cover: {weather['cloudcover']}%\n"
                f"- Precipitation: {weather['precipMM']} mm\n"
                f"- Humidity: {weather['humidity']}%\n"
                f"- Wind Direction & Speed: {weather['windspeedKmph']} km/h {weather['winddir16Point']}"
            )
        else:
            await ctx.followup.send("Failed to retrieve weather data.")

    
async def setup(bot: commands.Bot):
    await bot.add_cog(ToolsCommandsCog(bot))