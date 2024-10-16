from main import client
from ..Module import *
from ..Utils import *
from discord.ui import View, Button
import discord,requests,re,aiohttp,wikipedia
from io import BytesIO
from bs4 import BeautifulSoup

def search_web(query, results):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    related_topics = data['RelatedTopics'][:results]
    results_list = []
    final = f"## Results for `{query}`:\n"
    for topic in related_topics:
        if 'Name' in  topic:
            final += f"### {topic['Name']}\n"
            for ntopic in topic['Topics']:
                if 'Text' in topic:
                    results_list.append({
                        "t": topic['Text'],
                        "u": topic['FirstURL']
                    })
                    final += f" - [{topic['Text']}](<{topic['FirstURL']}>)\n"
            final+="\n"
        elif 'Text' in topic:
            results_list.append({
                "t": topic['Text'],
                "u": topic['FirstURL']
            })
            final += f"[{topic['Text']}](<{topic['FirstURL']}>)\n"


    return final

def search_wikipedia(query, results=3):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": results
    }
    response = requests.get(url, params=params)
    data = response.json()
    search_results = data['query']['search']
    
    summaries = []
    for result in search_results:
        page_id = result['pageid']
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_id}"
        summary_response = requests.get(summary_url)
        summary_data = summary_response.json()
        dlog(summary_data)
        summaries.append({
            "title": summary_data['title'],
            "summary": summary_data['extract']
        })
    
    return summaries
def search_images(query, results):
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srlimit": results,
        "srnamespace": 6  
    }
    response = requests.get(url, params=params)
    data = response.json()
    search_results = data['query']['search']
    
    images = []
    for result in search_results:
        image_title = result['title']
        image_info_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={image_title}&prop=imageinfo&iiprop=url&format=json"
        image_info_response = requests.get(image_info_url)
        image_info_data = image_info_response.json()
        pages = image_info_data['query']['pages']
        for page_id in pages:
            image_url = pages[page_id]['imageinfo'][0]['url']
            images.append(image_url)
    
    return images

def b2t(b):
    return ''.join(chr(int(byte, 2)) for byte in b.split())
def t2b(text):
    return ' '.join(format(ord(char), '08b') for char in text)
def convert_to_string(data):
    result = []
    for key, value in data.items():
        spaced_key = re.sub(r'(?<!^)(?=[A-Z])', ' ', key).title()
        result.append(f"{spaced_key}: {value}")
    return "\n".join(result)
errors = [
    """```python
Traceback (most recent call last):
  File "universe.py", line 507, in _life
    await getGirl(*args, **kwargs)
  File "universe.py", line 175, in getGirl
    await girl.CheckSize([E])
  File "unverse/human.py", line 55, in CheckSize
    Req = Average.Length - [E].Psize()
LengthError: 2 Inches```
""",

"""```lua
lua: universe.lua:2: attempt to perform arithmetic on local '[E]' (a nil value)
stack traceback:
	universe.lua:205: in function 'getObject'
	universe.lua:5: in main chunk
	[C]: ?```
""",

"""```java
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "[E].get()" because "[E]" is null
    at com.universe.Life.find[E](Life.java:34)
    com.universe.Main.get[E]([E].java:24)
    at com.universe.Main.main(Main.java:10)```
""",

"""```lua
[E] = random.Person(Union[Character.Types.IDIOT,Character.Types.Retarded], SIGMA=false, Life=nil)
[E]:ShutUp()

from internet.SocialMedia import Discord

SigmaMaleDiscordMod = Discord:login(MainCharacter)
ThisServer = SigmaMaleDiscordMod:getServer()
ThisServer:ban([E], time=Time.Eternity) -- The Sigma Male makes the idiot [E] shut up```
""",

"""```lua
[E].AURA -= Utils.INFINITY
console.log([E].SIGMA)
================================
Error in Line 1, Script "life.py": Cannot subtract None from [E] as local variable [E].AURA is a constant of None
while Exception.NOAURA was running another error at Line 2: Cannot log [E].SIGMA as constant SIGMA is a NoneType```
""",

"""```lua
from CharcterTypes import Bitch, Idiot, Stupid, Illiterate
[E] = Random.Person("[E]", Type=[Bitch.Max(), Idiot.Retarded, Stupid.max(), illiterate.max()], "got his application rejected for getting his non existant brain back")

ardtyss@ [E]:smash()
ardtyss@ [E]:touch()
[E]:setColor(Skintone.BLACK)
[E] = Idiot```
"""
]



class ComputingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="base64",description="Base64 Encode/Decode")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def base64_callback(self,ctx: discord.Interaction, text: str, decode: bool = False):
        if decode:       
            try:
                decoded_text = base64.b64decode(text).decode()
                await ctx.response.send_message(f'Base64 Decoded: `{decoded_text}`')

            except base64.binascii.Error:
                await ctx.response.send_message('Invalid base64 encoding.')
        else:   await ctx.response.send_message(f'Base64 Encoded: `{base64.b64encode(text).decode()}`')

    @app_commands.command(name="binary",description="Binary Encode/Decode")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def binary_callback(self,ctx: discord.Interaction, text:str,decode:bool=False):
        if decode:
            await ctx.response.send_message(b2t(text))
        else: await ctx.response.send_message(t2b(text))

    @app_commands.command(name="calculate",description="Meth")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def calc_callback(self,ctx: discord.Interaction, question:str):
                        x = 1
                        y = 1
                        values_to_calc = question
                        values_to_calc = values_to_calc.replace(' ','')
                        try:
                            await ctx.response.send_message('Answer: `'+str(eval(values_to_calc))+'`')
                        except Exception as e:
                            await ctx.response.send_message('Invalid Numbers')

    
    @app_commands.command(name="coderoast", description="Roast in code")
    @app_commands.describe(template="Select a template")
    @app_commands.choices(template=[
        app_commands.Choice(name="Egg Plant Length", value="length"),
        app_commands.Choice(name="Object can't reduced/increase because it doesn't exist", value="nil"),
        app_commands.Choice(name="Cannot get object", value="java"),
        app_commands.Choice(name="stfu", value="stfu"),
        app_commands.Choice(name="No Sigma & Aura", value="sigma"),
        app_commands.Choice(name="Programmically expresses the fact that you are idiotic", value="idiot")
    ])
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def coderoast_callback(self,ctx: discord.Interaction, template:str, roast: str):
            if template == "length":
                await ctx.response.send_message(errors[0].replace('[E]',roast))
            elif template == "nil":
                await ctx.response.send_message(errors[1].replace('[E]',roast))
            elif template in ["java",'null','not','invoke']:
                await ctx.response.send_message(errors[2].replace('[E]',roast))
            elif template == "stfu":
                await ctx.response.send_message(errors[3].replace('[E]',roast))
            elif template in ["sigma","aura"]:
                await ctx.response.send_message(errors[4].replace('[E]',roast))
            elif template in ["roast","retard","retarded","idiot"]:
                await ctx.response.send_message(errors[5].replace('[E]',roast))


    @app_commands.command(name="github",description="Get a github repo")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def github_callback(self,ctx: discord.Interaction, repository: str, owner:str):

        url = f"https://api.github.com/repos/{owner}/{repository}"
        headers = {
            'User-Agent': 'YourAppName',
            'Accept': 'application/vnd.github.v3+json'
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    repo_info = await response.json()
                    response_message = (
                        f"**Repository Name:** {repo_info['name']}\n"
                        f"**Description:** {repo_info['description']}\n"
                        f"**Stars:** {repo_info['stargazers_count']}\n"
                        f"**Forks:** {repo_info['forks_count']}\n"
                        f"**Open Issues:** {repo_info['open_issues_count']}\n"
                        f"**Watchers:** {repo_info['watchers_count']}\n"
                        f"**Language:** {repo_info['language']}\n"
                        f"**License:** {repo_info['license']['name'] if repo_info['license'] else 'None'}\n"
                        f"**Default Branch:** {repo_info['default_branch']}\n"
                        f"**Owner:** {repo_info['owner']['login']}\n"
                        f"**Repository URL:** {repo_info['html_url']}\n"
                        f"**Created At:** {repo_info['created_at']}\n"
                        f"**Last Pushed At:** {repo_info['pushed_at']}\n"
                        f"**Size:** {repo_info['size']} KB"
                    )
                    await ctx.response.send_message(response_message)
                else:
                    await ctx.response.send_message(f"Repository not found. Status code: {response.status}")

    @app_commands.command(name="program",description="Program something")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def program_callback(self,ctx: discord.Interaction,lang:str,file_extension:str,code:str):
            await ctx.response.defer()
            await ctx.followup.send("Compiling...",ephemeral=True)
            payload = {
                "language": lang,
                "files": [
                    {
                        "name": f"index.{file_extension}",
                        "content":code
                    }
                ]
            }
            e = requests.post("https://onecompiler-apis.p.rapidapi.com/api/v1/run", json=payload, headers={
                "x-rapidapi-key": rapid_api_key,
                "x-rapidapi-host": "onecompiler-apis.p.rapidapi.com",
                "Content-Type": "application/json"
            })
            e = e.json()
            await ctx.followup.send(f"Code Execution: `{e['status']}`\nStderr:```{lang}\n{str(e['stderr']) if 'stderr' in e else 'None'}```\nStdout:```{lang}\n{str(e['stdout'])}```")

    @app_commands.command(name="qr",description="Generate a QR Code")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def qr_callback(self,ctx: discord.Interaction, url: str):
        
        api_url = f'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={url.replace(" ","%20")}'
        r = requests.get(api_url)

        await ctx.response.send_message(file=discord.File(fp=BytesIO(r.content),filename='qr.jpg'))

    @app_commands.command(name="whois",description="Get a domain whois data")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def whois_callback(self,ctx: discord.Interaction, domain:str):
        
        e = api('https://whois40.p.rapidapi.com/whois','whois40.p.rapidapi.com',{"q":domain})
        await ctx.response.send_message(f"```yaml\n{convert_to_string(e.json())}```")

    @app_commands.command(name="ip",description="Get the info of an IP address")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def ipinfo_callback(ctx:discord.Interaction, ip:str):
        ip_address = ip
        ip_address = ip_address.replace("https://","")
        ip_address = ip_address.replace("http://","")
        ip_address = ip_address.replace(' ','')
        url = f"http://ipinfo.io/{ip_address}"
        
        response = requests.get(f"http://ipinfo.io/{domain_to_ip(ip_address)}")
        data = response.json()
        location = f"{data.get('ip', 'N/A')}: {data.get('country', 'N/A')}, {data.get('region', 'N/A')}, {data.get('city', 'N/A')}"
        if data.get("country","N/A")=='N/A' and not data.get("ip","N/A").isdigit(): 
            response = requests.get(f"http://ipinfo.io/{domain_to_ip(ip_address)}")
            data = response.json()
            location = f"{data.get('ip', 'N/A')}: {data.get('country', 'N/A')}, {data.get('region', 'N/A')}, {data.get('city', 'N/A')}"
            
        await ctx.response.send_message(f'{ip_address}:```{location}```')

    @app_commands.command(name="search", description="Search the web")
    @app_commands.describe(engine="Select a search engine")
    @app_commands.choices(engine=[
        app_commands.Choice(name="DuckDuckGo", value="ddg"),
        app_commands.Choice(name="Tutla Website",value="tutla"),
        app_commands.Choice(name="Wikimedia", value="wm"),
        app_commands.Choice(name="Wikipedia", value="wiki"),
        app_commands.Choice(name="Universities in a country", value="uns"),
    ])
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def wiki_callback(self,ctx:discord.Interaction, engine:str, search:str, results: int=3):
        await ctx.response.send_message("Searching 🔎...",ephemeral=True)
        if engine == "ddg":
            e = search_web(search, results)
            await ctx.followup.send(e)
        elif engine == 'wm':
            
            e = search_images(search, results)
            f  = f"Results for `{search}`:\n"
            for i in e:
                f += f'[Image]({i})\n'
            await ctx.followup.send(f)
        elif engine == "wiki":
            e = wikipedia.summary(search, results)
            await ctx.followup.send(e)
        elif engine == "uns":
            url = f"http://universities.hipolabs.com/search?country={search.replace(' ','%20').lower()}"
            response = requests.get(url)
            universities = response.json()
            final = f"Universities in {search}:\n"
            count = 5
            for i in universities:
                
                final += f"- [{i['name']}](<{i['web_pages'][0]}>)\n"
                count-=1
                if count<=0: break
        
            await ctx.followup.send(final)

        elif engine == "tutla":

            r = requests.get(f"https://tutla.net/?s={search.replace(' ','+')}")
            soup = BeautifulSoup(r.content, 'html.parser')
            results = []
            target_class = "columns-3 wp-block-post-template is-layout-grid wp-container-core-post-template-is-layout-1 wp-block-post-template-is-layout-grid"
            e = soup.find('ul', class_=target_class)

            if e:
                for li in e.find_all('li'):
                    div_inside_li = li.find('div')
                    if div_inside_li:
                        h2_element = div_inside_li.find('h2', class_='wp-block-post-title has-medium-font-size')
                        if h2_element:
                            a_element = h2_element.find('a')
                            if a_element:
                                a_text = a_element.get_text(strip=True)
                                a_href = a_element['href']
                                results.append([a_text, a_href])

            final = f'### __Search Results for "{search}":__\n'
            for i in results:
                weeb = i[0].replace("']","").replace("['","")
                final+=f"- {weeb}: <{i[1]}>\n"
            await ctx.followup.send(final)

async def setup(bot: commands.Bot):
    await bot.add_cog(ComputingCog(bot))