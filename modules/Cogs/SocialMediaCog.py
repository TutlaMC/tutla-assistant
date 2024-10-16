
from ..Module import *
from ..Utils import *
import discord
from discord import File
import requests
from io import BytesIO
from bs4 import BeautifulSoup
def gInstaData(data,name,key):
    if key in data:
        return f"{name}: {str(data[key])}"
    else: return f"{name}: Not Specified"
def mod_embed(data):
        embed  = discord.Embed(title=data['title'],description=data['description'],color=discord.Colour.green())
        embed.add_field(name="Downloads",value=data['downloads'])
        embed.add_field(name="Followers",value=data['followers'])
        embed.add_field(name="Published On",value=data['published'])
        embed.add_field(name="Last Updated",value=data['updated'])
        embed.add_field(name="Status",value=data['status'].capitalize())
        embed.add_field(name="License",value=data.get('license',{'name':'No License'})['name'],inline=True)
        
        categories = ""
        for cat in data['categories']:
            categories+=f'`{cat}` '

        loaders = ""
        for loader in data.get("loaders",[]):
            loader+=f'`{loader}` '
        versions = ""
        for version in data.get("game_versions",[]):
            versions+=f'`{version}` '
        
        embed.add_field(name="Categories",value=categories,inline=True)
        embed.add_field(name="Loaders",value=loaders,inline=True)
        embed.add_field(name="Versions",value=versions,inline=True)
        embed.add_field(name="URL",value=f"https://modrinth.com/mod/{data.get('slug')}",inline=True)
        embed.set_thumbnail(url=data['icon_url'])
        return embed
class Dropdown(discord.ui.Select):
    def __init__(self, mods):
        options = []
        for mod in mods:
            emoji = ''
            if 'combat' in mod['display_categories']: emoji = '⚔️'
            elif 'models' in mod['display_categories']: emoji = '🎠'
            elif 'utility' in mod['display_categories']:  emoji = '🧵'
            elif 'vanilla-like' in mod['display_categories']: emoji = '👀'
            elif 'lightweight' in mod['display_categories']: emoji = '🪶'
            elif 'fabric' in mod['display_categories']: emoji = '📜'
            elif 'forge' in mod['display_categories']: emoji = '🔨'
            else: emoji = "🤔"
            options.append(discord.SelectOption(label=mod.get('title'), description=mod['description'][:90]+'...',emoji=emoji,value=mod.get("project_id")))

        super().__init__(placeholder="Choose a mod", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        mod = self.values[0]

        response = requests.get(f"https://api.modrinth.com/v2/project/{mod}", headers={'User-Agent': 'Mozilla/5.0'})
        data = response.json()
    
        
        await interaction.response.send_message(data['title'],embed=mod_embed(data))


class DropdownView(discord.ui.View):
    def __init__(self, mods):
        super().__init__()
        self.add_item(Dropdown(mods))




async def download_video(url):
    url = url.replace("https",'').replace('http','').replace('://','').replace('youtu.be','').replace('www.','').replace('youtube.com','').replace('/','').replace('watch?v=','')
    e=api("https://yt-api.p.rapidapi.com/dl","yt-api.p.rapidapi.com",{'id':url})
    e = e.json()
    response = requests.get(e['formats'][0]['url'], stream=True)
    if response.status_code == 200:
        video_data = BytesIO()

        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                video_data.write(chunk)
        video_data.seek(0)
    else:
        HTTPLogger.log("Failed to download video:"+ response.status_code+ response.text,style='error')
    return video_data

async def download_audio(url):
    url = url.replace("https",'').replace('http','').replace('://','').replace('youtu.be','').replace('www.','').replace('youtube.com','').replace('/','').replace('watch?v=','')
    e=api("https://yt-api.p.rapidapi.com/dl","yt-api.p.rapidapi.com",{'id':url})
    e = e.json()
    dlog(e)
    response = requests.get(e['adaptiveFormats'][12]['url'], stream=True)
    if response.status_code == 200:
        video_data = BytesIO()

        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                video_data.write(chunk)
        video_data.seek(0)
    else:
        HTTPLogger.log("Failed to download video:"+ response.status_code+ response.text,style='error')
    return video_data
    

class YoutubeVideoDownloadButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Download", style=discord.ButtonStyle.secondary)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id in premium_list:  # Make sure premium_list is defined
            await interaction.response.send_message("Downloading...", ephemeral=True)
            print(interaction.message.content)
            vid = await download_video(interaction.message.content)
            if isinstance(vid, BytesIO):
                await interaction.followup.send(file=File(fp=vid, filename='video.mp4'))
            else:
                await interaction.followup.send("Failed to download the video.", ephemeral=True)
        else: await interaction.response.send_message("Your not a premium user!",ephemeral=True)

class YoutubeVideoDownloadMP3Button(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Download MP3", style=discord.ButtonStyle.secondary)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id in premium_list:  # Make sure premium_list is defined
            await interaction.response.send_message("Downloading...", ephemeral=True)
            print(interaction.message.content)
            vid = await download_audio(interaction.message.content)
            if isinstance(vid, BytesIO):
                await interaction.followup.send(file=File(fp=vid, filename='video.mp3'))
            else:
                await interaction.followup.send("Failed to download the audio.", ephemeral=True)
        else: await interaction.response.send_message("Your not a premium user!",ephemeral=True)

class YoutubeVideoChannelButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Channel Info", style=discord.ButtonStyle.blurple)

    async def callback(self, interaction: discord.Interaction):
            await interaction.response.send_message("Getting channels...", ephemeral=True)
            url = interaction.message.content.replace("https",'').replace('http','').replace('://','').replace('youtu.be','').replace('www.','').replace('youtube.com','').replace('/','').replace('watch?v=','')
            e=api("https://yt-api.p.rapidapi.com/dl","yt-api.p.rapidapi.com",{'id':url})
            e =e.json()
            e=api("https://yt-api.p.rapidapi.com/channel/home","yt-api.p.rapidapi.com",{'id':e['channelId']})
            e=e.json()
            embed = discord.Embed(title=e['meta']['title'],description=e['meta']['description'])
            embed.set_thumbnail(url=e['meta']['avatar'][0]['url'])
            embed.set_image(url=e['meta']['banner'][0]['url'])
            embed.add_field(name='Handle',value=e['meta']['channelHandle'])
            embed.add_field(name='Subscribers',value=e['meta']['subscriberCountText'])
            embed.add_field(name='Video Count',value=e['meta']['videosCountText'])
            await interaction.followup.send("Channel Found!",embed=embed)

class YoutubeVideoView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(YoutubeVideoDownloadButton())
        self.add_item(YoutubeVideoDownloadMP3Button())
        self.add_item(YoutubeVideoChannelButton())







class SocialMediaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="instagram",description="Get an Instagram user's info ")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def instagram_callback(self,ctx:discord.Interaction, username:str):
        await ctx.response.send_message("Getting data...",ephemeral=True)
        e = api("https://instagram-scraper-api2.p.rapidapi.com/v1/info","instagram-scraper-api2.p.rapidapi.com",{"username_or_id_or_url":username})
        dlog(e.json())
        data = e.json()['data']
        e =data


        embed  = discord.Embed(title=username,description=data.get('biography','No Bio'),color=discord.Colour.purple())
        embed.set_thumbnail(url=data['profile_pic_url'])
        embed.add_field(name="Full Name",value=data.get('full_name'))
        embed.add_field(name="Bio Links",value=f"{', '.join(link['url'] for link in e['bio_links'])}")
        embed.add_field(name="Category",value=data.get('category','-'))
        embed.add_field(name="Linked",value=data.get('external_url','-'))
        embed.add_field(name="Followers",value=data.get('follower_count','-'))
        embed.add_field(name="Following",value=data.get('following_count','-'))

        embed.add_field(name="Country",value=gInstaData(e['about'],"Country","country") if e['about'] != None else '-')
        embed.add_field(name="Date Joined",value=gInstaData(e['about'],"Date Joined","date_joined") if e['about'] != None else '-')
        embed.add_field(name="Former Usernames",value=gInstaData(e['about'],"Former Usernames","former_usernames") if e['about'] != None else '-')

        embed.add_field(name="Phone Number",value=data.get("contact_phone_number",'-'))
        embed.add_field(name="Buisness Account",value=data.get("is_business",'-'))


        await ctx.followup.send(f"{username}",embed=embed)

    @app_commands.command(name="modrinth",description="Search Modrinth mods")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def modrinth_callback(self,ctx:discord.Interaction,mod:str,direct:bool=False):
        if not direct:
            await ctx.response.send_message("Fetching modrinth mods....")
            query = mod
            url = f"https://api.modrinth.com/v2/search?query={query}&limit=8"
            headers = {'User-Agent': 'Mozilla/5.0'}

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                mods = data.get('hits', [])

                if mods:

                    embed = discord.Embed(title=f"'{query}' Mods on Modrinth",color=discord.Color.green())
                    for mod in mods:
                        title = mod.get('title', 'No Title')
                        link = f"https://modrinth.com/mod/{mod.get('slug', '')}"
                        desc = mod.get('description', 'No description')
                        author = mod.get('author', 'Unknown Author')
                        downloads = mod.get('downloads', 'No downloads')
                        embed.add_field(name=f'{title} by {author}',value=f'{desc} [Get here!]({link})',inline=False)
                    view = DropdownView(mods)
                        
                    await ctx.followup.send('Found Mods',embed=embed,view=view)
                else:
                    await ctx.followup.send(f"No mods found for '{query}'")
            else:
                await ctx.followup.send("Failed to get mod data")
        else:
            await ctx.response.send_message("Fetching mod...",ephemeral=True)
            response = requests.get(f"https://api.modrinth.com/v2/project/{mod}", headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                await ctx.followup.send("Modrinth",embed=mod_embed(response.json()))
            else:
                await ctx.followup.send(f"Mod with slug `{mod}` not found",ephemeral=True)

    @app_commands.command(name="youtube", description="Download a YouTube video")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def yt_callback(self,ctx: discord.Interaction, query_or_url: str, search: bool = False):
        q = query_or_url
        if not search:
            await ctx.response.send_message("Getting YouTube video...", ephemeral=True)

            response = requests.get(query_or_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            def get_meta_content(soup, name=None, itemprop=None, content=None):
                tag = soup.find('meta', {'itemprop': itemprop})
                if content!=None:tag = soup.find('meta', {'itemprop': itemprop,'content':content})
                elif tag['content'] =='IE=edge': tag = soup.find('meta', {'name': name})
                
                print(tag)
                return tag['content'] if tag else 'N/A'

            title = get_meta_content(soup, name='title')
            description = get_meta_content(soup, name='description')
            view_count = get_meta_content(soup, itemprop='interactionCount')
            channel_name = soup.find('link', {'itemprop': 'name'})['content'] if soup.find('link', {'itemprop': 'name'}) else 'N/A'
            upload_date = get_meta_content(soup, itemprop='uploadDate')
            like_count = get_meta_content(soup, itemprop='interactionCount', content='UserLikes')
            dislike_count = get_meta_content(soup, itemprop='interactionCount', content='UserDislikes')
            duration = get_meta_content(soup, itemprop='duration').replace('PT','')
            keywords = get_meta_content(soup, name='keywords')
            category = get_meta_content(soup, itemprop='genre')
            comment_count = soup.find('yt-formatted-string', {'class': 'count-text style-scope ytd-comments-header-renderer'}).text if soup.find('yt-formatted-string', {'class': 'count-text style-scope ytd-comments-header-renderer'}) else 'N/A'

            embed = discord.Embed(title=title, description=description, color=discord.Color.red())
            embed.add_field(name="Views", value=view_count)
            embed.add_field(name="Channel", value=channel_name)
            embed.add_field(name="Uploaded at", value=upload_date)
            embed.add_field(name="Likes", value=like_count)
            embed.add_field(name="Dislikes", value=dislike_count)
            embed.add_field(name="Duration", value=duration)
            embed.add_field(name="Keywords", value=keywords)
            embed.add_field(name="Category", value=category)
            embed.add_field(name="Comment Count", value=comment_count)


            view = YoutubeVideoView()
            await ctx.followup.send(query_or_url, embed=embed, view=view)
        else:
            await ctx.response.send_message("Searching 🔎...",ephemeral=True)
            e=api("https://yt-api.p.rapidapi.com/search","yt-api.p.rapidapi.com",{'query':query_or_url})
            e =e.json()
            embed = discord.Embed(title=f'"{query_or_url} Videos"',color=discord.Colour.red())
            for i in e['data']:
                if not 'videoId' in i: break
                embed.add_field(name=i['title']+f" by {i.get('channelTitle',' Anyonymous')}",value=f"https://youtube.com/watch?v={i['videoId']}")
            await ctx.followup.send("Videos found",embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(SocialMediaCog(bot))