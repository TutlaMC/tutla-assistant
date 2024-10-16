
from ..Module import *
from ..Utils import *
from discord.ui import View, Button
import discord,requests,re,aiohttp,random
from io import BytesIO
from bs4 import BeautifulSoup

url = 'https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
rizz = [li.text for li in soup.find_all('li')]

def remove_match_char(list1, list2):
 
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
 
                # remove character from the list
                list1.remove(c)
                list2.remove(c)
 
                # concatenation of two list elements with *
                # * is act as border mark here
                list3 = list1 + ["*"] + list2
 
                # return the concatenated list with True flag
                return [list3, True]
 
    # no common characters is found
    # return the concatenated list with False flag
    list3 = list1 + ["*"] + list2
    return [list3, False]

suffixes = ['s','a','i','o',"ly","er","es","ant","ance","ve","ary","tion","ation","ed","ing","dom","er","ful","ous","ship","wards","al","ate","ion","y","acy"]
def ransuffix():
      return random.choice(suffixes)

facts = [
    "Honey never spoils.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries aren't.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "There are more stars in the universe than grains of sand on Earth.",
    "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    "Humans share 60% of their DNA with bananas.",
    "A single strand of spaghetti is called a 'spaghetto'.",
    "The shortest war in history lasted 38 minutes.",
    "A group of flamingos is called a 'flamboyance'.",
    "The longest time between two twins being born is 87 days.",
    "The inventor of the Pringles can is now buried in one.",
    "A jiffy is an actual unit of time: 1/100th of a second.",
    "A blue whale's heart is the size of a small car.",
    "Some cats are allergic to humans.",
    "The unicorn is the national animal of Scotland.",
    "A snail can sleep for three years.",
    "There are more fake flamingos in the world than real ones.",
    "A crocodile cannot stick its tongue out.",
    "The world's smallest reptile was discovered in 2021.",
    "The moon has moonquakes.",
    "Goosebumps are meant to ward off predators.",
    "Humans are the only animals that blush.",
    "The wood frog can hold its pee for up to eight months.",
    "The hottest spot on the planet is in Libya.",
    "Only two mammals like spicy food: humans and the tree shrew.",
    "The longest wedding veil was longer than 63 football fields.",
    "The inventor of the microwave appliance received only \$2 for his discovery.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "There's a fruit that tastes like chocolate pudding.",
    "More people visit France than any other country.",
    "A chef's hat has 100 pleats.",
    "The world's longest place name is 85 letters long.",
    "The unicorn is the national animal of Scotland.",
    "Bees sometimes sting other bees.",
    "The total weight of ants on earth once equaled the total weight of people.",
    "E is the most common letter and appears in 11 percent of all English words.",
    "A dozen bodies were once found in Benjamin Franklin's basement.",
    "The healthiest place in the world is in Panama.",
    "A pharaoh once lathered his slaves in honey to keep bugs away from him.",
    "Some people have an extra bone in their knee (and it's getting more common).",
    "Pringles aren't actually potato chips.",
    "There's a giant fish with a transparent head.",
    "The first computer was invented in the 1940s.",
    "Space smells like seared steak.",
    "The longest hiccuping spree lasted 68 years.",
    "The shortest commercial flight in the world is in Scotland.",
    "The longest musical performance lasted 639 years.",
    "The world's largest grand piano was built by a 15-year-old."
]

url = "https://thepleasantconversation.com/shower-thoughts/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

thoughts_list = []


for index, li_element in enumerate(soup.find_all('li')):
    text = li_element.get_text(strip=True)

    thoughts_list.append(text)

    if index == 542:
        break

phrases = ["bazinga!🤣 this video sure did tickle my funny bone!😂🦴 i absolutely need to show this to my book club!😅📚 #wap🍷",
"That's not the assignment young man 📏💥🧓🏽 I better not catch you off task in my messages again ❌✏️📜🙏🏼 or else task wont be the only thing taken off today 😱🙏🏼🙅🏼‍♂️🙅🏼‍♂️",
"Careful with whatchu say 🙏🗣️🗣️🙏 the COCK is watching 🤞🤞🐔🐔 and he ain’t take NO prisoners 🙅‍♂️🙅‍♂️🤫🤫 keep them cheeks TIGHT",
"Bettah zip up yo keyboard like you zip up those pants before i 💦 and swing my 🔮 🔮 across yo 🤓 like a grandfather clock 🕰️ 🙏 🙏",
"Better watch yo mouth👨🏿‍🦲🤞🏻🙊 RANDY is listening in my comments section 👁️‍🗨️🙀👂🏿 and he won't just be taking your candy if he catches you again ❌🍬🍭",
"You old ragged little stocking 🙏 🧦 dont ever let my Rudolph detect you with his nose 🔴 or coals wont be the only thing inside of you this christmas 🔥 🗣️ 🎅 🐠",
"Nice try you scrawny octopus 🐙 🌊 but next time you dive near me 🪸 I'll make sure the tip will be all over you 💦 🐡 🍆",
"Nevah let me catch you commenting again lil bro 🙏 🙏 you have interupted my edging sesson and now you will pay 😏 💀 🔥",
"Spanksgiving👋🏻🦃🌽 is right around the corner you dirty slut😈😏😛 R u a sexy lil pilgrim?😈🎩🏃 or a naked native¿¿👹😵 GOBBLE🦃GOBBLE🦃🅱️ITCH🐕!!! It's 🦡SKANKS-GIVING😜!!!",
"vorp vorp shawty   p s    c  s  cju 👽 🙏🏻",
"I noticed that you used “😭” in your comment. Just wanted to say, don’t give up anything in your life. I don’t know what you’re going through but I’m always here to help.",
"are 🤨 you 👁️👄👁️are 🤨 you 👁️👄👁️coming 🚶🏾‍♀️to ✌🏾 the 💖💅 tree ✨🌲✨🌳",
    "𝔁𝓾𝓮🥶𝓱𝓾𝓪🧚‍♀️𝓹𝓲𝓪𝓸😻𝓹𝓲𝓪𝓸🗿𝓫𝓮𝓲👺𝓯𝓮𝓷𝓰🤩𝔁𝓲𝓪𝓸😼𝔁𝓲𝓪𝓸",
    "𝓻𝓮𝓶𝓮𝓶𝓫𝓮𝓻 🤔𝓽𝓱𝓮 ✨𝓽𝓲𝓶𝓮𝓼⌛️𝔀𝓮🤞🏾𝓱𝓪𝓭😪𝓽𝓱𝓮 😭 𝓽𝓲𝓶𝓮𝓼 ⏰ 𝓽𝓱𝓪𝓽🤥𝔂𝓸𝓾 👧 𝓪𝓷𝓭😴𝓶𝓮👦 𝓱𝓪𝓭😰",
    "Martha😁was🥰an🙃average🐕dog. She went💨aërf🍒&🤕ærph😪&👻EEEER🤠when👧🏻she👄ate🤏🏻some🤖alphabet👽soup,🐶then🧦what🌸happened🌚was🌈bizarre🧽",
    "R-R-R-Roll💿up⬆️to2️⃣the🤩party🥳with🧶my🧚🏽‍♀️crazy🤪pink💝wig💇‍♀️",
    "Anyway, here’s the recipe for brownies: 1/2cup butter, 2eggs, 1cup sugar, 1/3cup cocoa powder, 2teaspoon vanilla extract, 1/2cup flour",
    "ᵇᵒⁱ🐿️ʷʰᵃᵗ🐿️ᵗʰᵉ🐿️ʰᵉˡˡ🐿️ᵇᵒⁱ🐿️",
    "🦧ʙᴏɪ🦧ɪғ🦧ʏᴏᴜ🦧ᴅᴏɴᴛ🦧ɢᴇᴛ🦧ʏᴏᴜʀ🦧sǫᴜɪɢɢʟʏ🦧ᴅɪɢɢʟʏ🦧ʜᴇᴀᴅ🦧",
    "You don’t have this emoji😅⃤",
    "Careful with whatchu say 🙏🗣️🗣️🙏 the COCK is watching 🤞🤞🐔🐔 and he ain’t take NO prisoners 🙅‍♂️🙅‍♂️🤫🤫 keep them cheeks TIGHT",
    "Hey pal!👋👋, listen friendo, when I saw your message, I immediately started violently touching myself, hope I can touch you next. Over and out!😳",
    "I noticed that you used “😭” in your comment. Just wanted to say, don’t give up anything in your life. I don’t know what you’re going through but I’m always here to help."]



class TrollCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="antinpc", description="Deal with NPCs")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def antinpc_callback(self,ctx: discord.Interaction):
        await ctx.response.send_message(random.choice(phrases))

    
    @app_commands.command(name="fact", description="Get a random fact")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def fact(self, ctx: discord.Interaction):
        fact = random.choice(facts)
        await ctx.response.send_message(f"Did you know? {fact}")


    @app_commands.command(name="kanye", description="Get a Kanye West quote")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def kanye(self, ctx: discord.Interaction):
        r = requests.get('https://api.kanye.rest')
        r = r.json()['quote']
        await ctx.response.send_message(r)

    @app_commands.command(name="catfact", description="Get a random cat fact")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def catfact(self, ctx: discord.Interaction):
        fact = requests.get('https://catfact.ninja/fact')
        await ctx.response.send_message(fact.json()['fact'])

    @app_commands.command(name="qotd", description="Get the question of the day")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def qotd(self, ctx: discord.Interaction):
        from ..Utils import question_otd
        await ctx.response.send_message(question_otd)

    @app_commands.command(name="joke", description="Get a random joke")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def joke(self, ctx: discord.Interaction):
        joke = requests.get(random.choice(['https://v2.jokeapi.dev/joke/Dark', 'https://v2.jokeapi.dev/joke/Misc']))
        joke = joke.json()
        if 'joke' in joke:
            await ctx.response.send_message(joke['joke'])
        else:
            await ctx.response.send_message(joke['setup'])
            await asyncio.sleep(5)
            await ctx.followup.send(joke['delivery'])

    @app_commands.command(name="chatded", description="Show current time with chat ded message")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def chatded(self, ctx: discord.Interaction):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        await ctx.response.send_message(f'Chat ded - `{current_time}`')

    @app_commands.command(name="advice", description="Get random advice")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def advice(self, ctx: discord.Interaction):
        advice = requests.get('https://api.adviceslip.com/advice')
        advice = advice.json()
        await ctx.response.send_message(advice['slip']['advice'])

    @app_commands.command(name="furry", description="Get a random furry/fox picture")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def furry(self, ctx: discord.Interaction):
        await ctx.response.send_message("Getting furry pic...", ephemeral=True)
        api_url = f'https://randomfox.ca/images/{str(random.randint(1, 123))}.jpg'
        r = requests.get(api_url)
        await ctx.followup.send("Furry Pic\n:warning: REAL FURRY :warning:\n-# Click To see:",
                                file=discord.File(fp=BytesIO(r.content), filename='fox.jpg', spoiler=True))

    @app_commands.command(name="showerthought", description="Get a random shower thought")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def showerthought(self, ctx: discord.Interaction):
        await ctx.response.send_message(random.choice(thoughts_list))

    @app_commands.command(name="racisim", description="Call out attempted racism")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def racisim(self, ctx: discord.Interaction):
        await ctx.response.send_message(ctx.user.mention + ' bro really tried being racist')
    
    @app_commands.command(name="gay", description="Find out how gay a user is")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def gay(self, ctx: discord.Interaction, user: discord.User):
        await ctx.response.send_message(f"{user.name} is {str(sum(ord(char) for char in user.name) % 101)}% gay")

    @app_commands.command(name="activesite", description="Find the most visited site of a user")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def activesite(self, ctx: discord.Interaction, user: discord.User):
        await ctx.response.send_message("Finding more about user 🔍...", ephemeral=True)
        if str(user.id) not in premium_list:
            await ctx.followup.send(f'Most active site {user.global_name} is on: || the p hub (100% real data) :skull: ||', silent=True)
        else:
            await ctx.followup.send(f'Most active site {user.global_name} is on: || x.com (good boi) ||', silent=True)

    @app_commands.command(name="doxx", description="Doxx a user with fun facts")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def doxx(self, ctx: discord.Interaction, user: discord.User):
        await ctx.response.send_message("Finding more about user 🔍...", ephemeral=True)
        gender = requests.get(f'https://api.genderize.io?name={user.display_name}').json()['gender']
        await ctx.followup.send(f"More about {user.mention}:\n- Age: ||Above 0||\n- Location: ||Milkyway Galaxy, Earth||\n- Gender: ||{gender}||\n- email: ||hosted by sum email service like gmail or sum||\n- Skin Color: ||black, yellow, white, or brown||")

    @app_commands.command(name="sex", description="Find out the gender/sex of a user")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def sex(self, ctx: discord.Interaction, user: discord.User):
        gender = requests.get(f'https://api.genderize.io?name={user.display_name}').json()['gender']
        await ctx.response.send_message(f"{user.mention}'s Gender: {gender}")
        await ctx.followup.send("WHAT ARE YOU DOING????!\nhttps://tenor.com/view/freak-freaky-tongue-out-sticking-gif-10627789")

    @app_commands.command(name="match", description="FLAMES matching based on user names")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def match(self, ctx: discord.Interaction, user: discord.User, match: discord.User):
        await ctx.response.send_message("Matching users 🔍...", ephemeral=True)
        user1 = ''.join([char for char in user.display_name if char.isalpha()])
        user2 = ''.join([char for char in match.display_name if char.isalpha()])
        proceed = True
        p1_list = list(user1)
        p2_list = list(user2)
        while proceed:
            ret_list = remove_match_char(p1_list, p2_list)
            con_list = ret_list[0]
            proceed = ret_list[1]

            star_index = con_list.index("*")
            p1_list = con_list[:star_index]
            p2_list = con_list[star_index + 1:]

        count = len(p1_list) + len(p2_list)
        result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

        while len(result) > 1:
            split_index = (count % len(result) - 1)
            if split_index >= 0:
                right = result[split_index + 1:]
                left = result[:split_index]
                result = right + left
            else:
                result = result[:len(result) - 1]

        await ctx.followup.send(f"{user1} + {user2}: {result[0]}")


    @app_commands.command(name="joshify", description="Ruin grammar")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def joshify_callback(self,ctx: discord.Interaction, input:str):
                        words = input.split(' ')
                        transformed_words = []
                        for word in words:
                            random_number = random.random()
                            transformed_word = ''
                            if True:
                                if word.endswith('ed'):
                                    transformed_word = word[:-2] + 'ing'
                                elif word.endswith('ing'):
                                    transformed_word = word[:-3] + 'ed'
                                elif word.endswith('s'):
                                    if random.random() > 0.7:
                                        transformed_word = word[:-1]
                                    else:
                                        transformed_word = word+ransuffix()
                                elif word.lower() in ['the',"an","is","and"]:
                                    transformed_word = "a"
                                
                                elif word.endswith('ly'):
                                    transformed_word = word[:-2] + ransuffix()
                                elif word.lower() in ["at","on","the","that","these","those"]:
                                    transformed_word = "in"
                                elif word.lower() in ["you","who","whom","me"]: 
                                    transformed_word = "your"
                                elif word.lower() in ["i","us"]:
                                    transformed_word = "me"
                                elif word.lower() in ["he","she","it","her","him","it's","his"]:
                                    transformed_word = "its"
                                elif word.lower().replace("'","") in ["didnt","no","not","aint"]:
                                    transformed_word = "didn't"
                                elif "," in word:
                                    transformed_word = word.replace(",",".")
                                elif word.lower() == "an":
                                    transformed_word = "a"
                                elif word.lower() in ["in","that","these","those","is",'a']:
                                    transformed_word = "it"
                                elif word.lower() in ["will","do","make","want","to"]:
                                    transformed_word = "shall"
                                elif word.lower().replace("'","") in ["your","youre","yours"]:
                                    transformed_word = "you"
                                elif any(word.lower().endswith(suffix) for suffix in suffixes) and len(word) > 4:
                                    for suffix in ["ly","er","es","ant","ance","ary","tion","ation","ed","ing","dom","er","ful","ous","ship","wards","al","ate","acy"]:
                                        if word.lower().endswith(suffix):
                                            word = word.replace(suffix,"")
                                            transformed_word = word+ ransuffix()
                                else:
                                    if random.random() > 0.9:
                                        transformed_word = ''.join(char for char in word if char.lower() not in 'iou' and len(word)>3)
                                    elif random.random() < 0.1: 
                                        transformed_word+=word+random.choice([",","."," a","!"])
                                    else: transformed_word = word
                                    
                            transformed_words.append(transformed_word)
                        transformed_sentence = ' '.join(transformed_words)
                        await ctx.response.send_message(transformed_sentence)


    @app_commands.command(name="l", description="LMAO")
    @app_commands.user_install()
    async def lmao_callback(self,ctx: discord.Interaction):
        await ctx.response.send_message('lmao')

    @app_commands.command(name="nuke", description="Nuke the server")
    @app_commands.user_install()
    async def nuke_callback(self,ctx: discord.Interaction):
        
        await ctx.response.send_message('Imma go nuke this sh1t. (contact num for ultimate nuking service: `6942014696969`)')
        await asyncio.sleep(2)
        await ctx.followup.send("Nuking server....")

    @app_commands.command(name="rizz",description="Pickup lines uwu~s")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def rizz_callback(self,ctx:discord.Interaction):
        
        await ctx.response.send_message(random.choice(rizz))
async def setup(bot: commands.Bot):
    await bot.add_cog(TrollCommandsCog(bot))