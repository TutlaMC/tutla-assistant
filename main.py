import discord
import time
import requests
import random
from bs4 import BeautifulSoup
import base64
from datetime import datetime
import wikipedia
import re
from freeGPT import AsyncClient
from PIL import Image
from io import BytesIO
from unicodedata import lookup
from math import *
from datetime import timedelta
import os
import socket


from asyncio import run
ai_API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=65b242c79c2a22e31b1b90a0&org=c5bc6bfa-be03-4432-9131-a3a27734c5cf"
ai_headers = {'Authorization':
			 'Bearer 3282febe-5061-48f1-84ca-d8e680e57612',
			 'Content-Type': 'application/json'
		}

def ai_query(payload):
 response = requests.post(ai_API_URL, headers=ai_headers, json=payload)
 return response.json()
def domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve the domain."



def get_highlighted_answer(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        highlighted_element = soup.find('div', class_='BNeawe s3v9rd AP7Wnd')
        highlighted_answer = highlighted_element.text.strip() if highlighted_element else None
        return highlighted_answer
    except Exception as e:
        print(f"Error extracting highlighted answer: {e}")
        return None



def convert_to_base64(number):

    byte_representation = str(number).encode('utf-8')


    base64_representation = base64.b64encode(byte_representation)

    result = base64_representation.decode('utf-8')

    return result


url = "https://thepleasantconversation.com/shower-thoughts/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

thoughts_list = []


for index, li_element in enumerate(soup.find_all('li')):
    text = li_element.get_text(strip=True)

    thoughts_list.append(text)

    if index == 542:
        break
commandnames = []
commands = []
version = 'V1.1'
dev_mode = False
premium_list = []
promochannels = [1095082017214971925]
banlist=[]
def premium_reload():
        with open('assistantdata/premium.txt','r') as f:
                lines = f.readlines()
                for line in lines: 
                    line = line.replace('\n','')
                    premium_list.append(line)
def ban_reload():
    global banlist
    with open('assistantdata/bans.txt','r') as f:
            lines = f.readlines()
            for line in lines:banlist.append(line)
            
premium_reload()
ban_reload()
class Client(discord.Client):
    timelimit = [1180058692960399442]
    timelimitcount=[0]

    async def on_ready(self):
        global dev_mode
        global promochannels
        print("ready")
        game = discord.Streaming(name="discord.tutla.net",game="discord.tutla.net",url="https://discord.tutla.net")
        await client.change_presence(status=discord.Status.idle, activity=game)



        


    def make_command(name,description,params=[],isfree=False):
        global commandnames
        global commands
        commandnames.append(name)
        toappend = name+' '
        for i in params:
            toappend+= ' ['+i+'] '
        if isfree:
             toappend+= '| (FREE COMMAND)'
        toappend+= ' | '+description
        commands.append(toappend+'\n')
    
    commands.append('----- CLIENT COMMANDS -----\n')
    make_command('.help','Opens this page',params=['page'],isfree=True)
    make_command('.premium','Shows your premium status',params=['[USER]'],isfree=True)
    commands.append('----- INFO COMMANDS -----\n')
    make_command('.inservers',"Shows all serevrs this bot is in",isfree=True)
    make_command('.ai',"Runs Tutla AI",isfree=True)
    make_command('.image',"Runs Tutla image AI (Premium)",isfree=False,params=['[PROMPT]'])
    make_command('.serverinfo',"Gets Server Info",isfree=True,params=['[PROMPT]'])
    make_command('.userinfo',"Gets User Info",params=['USER_PING'])
    make_command('.nuke',"Get Nuke contact")
    make_command('.calc','Calculates',params=['numerals|python-math-functions'],isfree=True)
    make_command('.wiki','Wikipedia',params=['thing'],isfree=True)
    make_command('.base64encode','Base64 Encode a code',params=['text'],isfree=True)
    make_command('.base64decode','Base64 Decode a code',params=['text'],isfree=True)

    make_command('.tokenfirstpart','Reveals user token first part',params=['USER_PING'])
    make_command('.iptranslate','Translates IP or Domain to location',params=['IP'])
    make_command('.ansiformat','Converts your text into cool ansi text: Usage (HTML like usage):\n<red></red>\n<green></green><blue></blue><yellow></yellow><pink></pink><cyan></cyan><gray></gray>\nBackground Colors: <firefly-dark-blue></firefly-dark-blue><orange></orange><marble-blue></marble-blue><greyish-turquoise></greyish-turquoise><gray></gray><indigo></indigo><light-gray></light-gray><white></white>\nOther Formats: <bold></bold> <highlight></highlight) -> (for background)\t <underline></underline>\nYeah so now make ansi text!',params=['(text)[<color></color>|<highlight></highlight>|<bold></bold>|<underline></underline>]'])

    commands.append('----- FUN COMMANDS -----\n')
    make_command('.l','LMAO')
    make_command('.racism','types in n-word in chat',isfree=True)

    make_command('.chatded','Chat ded - 2024')
    make_command('.rizz','Get rizzed up - ardtyss')
    make_command('.toregional','Converts text to regional emojis',params=['text'])
    make_command('.toemoji','Converts text to emoji',params=['text'])
    make_command('.showerthought','Thoughts when ur in the shower')
    make_command('.activesite','Tell most active site your on 100% real stats - ardtyss',isfree=True)

    
    commands.append('----- TASK COMMANDS -----\n')
    make_command('.join','Joins server of your server',params=['invite'])
    make_command('.random','Selects random of param',params=['number|user', 'number1 (for randnum)', 'number2 (for randnum)','-mention (for randuser)'])
    commands.append('----- DISCORD TASK COMMMANDS -----\n')
    make_command('.react','Reacts to the replied message ',params=['text'])
    make_command('.reacto','Reacts to your given message ',params=['channelID','messageID','text'])
    make_command('.reactemoji','Reacts to the replied message with your emoji',params=['emoji'])
    make_command('.reactemojito','Reacts to your given message with your emoji)',params=['channelID','messageID','emoji'])
    make_command('.say','Say smth (use this in an argument)',params=['text'])
    commands.append('----- DISCORD ADMIN COMMANDS -----\n')
    make_command('.textchannel','Creates text channel',params=['channel_name','emoji'],isfree=True)
    make_command('.lockedtextchannel','Creates a locked text channel',params=['channel_name','emoji','optional:roles'])
    make_command('.hiddentextchannel','Creates a hidden text channel',params=['channel_name','emoji','optional:roles'])
    make_command('.voicechannel','Creates a voice channel',params=['channel_name','emoji'],isfree=True)
    make_command('.timeout','Times out users',params=['USER_MENTIONS'],isfree=True)
    make_command('.purge','Purges messages',params=['number'])
    make_command('.ban','Bans user (you can reply to a message to use this aswell)',params=['user','reason'],isfree=True)
    make_command('.kick','Kicks user (you can reply to a message to use this aswell)',params=['user','reason'],isfree=True)
    make_command('.role','Give roles to multiple users or a user',params=['users','roles'],isfree=True)
    make_command('.life','Ghost pings user and then bans (PREMIUM COMMAND)',params=['users'])
    

    commands.append('----- TUTLA ADMIN COMMANDS -----\n')
    make_command('.broadcastserver','Broadcasts a message to all members in the server the command was ran on',params=['message'])
    make_command('.broadcast','Broadcasts a message to all memberson the notification list [AVAILABLE WITH PREMIUM]',params=['message'])
    make_command('.superbroadcast','Broadcasts to everyone whom it has recivied a message from in the current run',params=['message'])
    make_command('.shutdown','Shuts the Bot down')
    
    free_commands = []
    
    
    

         
    async def on_message(self,message): 
        global premium_list
        global thoughts_list
        global version

        
        
        if message.author.id == 999736048596816014 and 'A wild' in message.content and message.channel.id != 1117881344391913514: await message.channel.send('<@1142511163821801493> <@1158452261538771055> yo ball here')
        
        

        thisguild = await self.fetch_guild(1189449885615927296)
        con = False
        try:
            boimember = await thisguild.fetch_member(message.author.id)
            if boimember:
                con = True
        except Exception as e:
            print(e)
            con = False
       
        
        if str(message.author.id) in premium_list:
            premium = True
        else:
            premium=False
        if str(message.author.id) in banlist:
             banned=True
        else:
             banned = False
        try:
                
                if "counting" in message.channel.name:
                    mc = message.content
                    number = int(mc)
                    
                    if message.author.id != client.user.id :
                        if  message.channel.id == 1127010732668620800: await message.channel.send(str(number+1))
                        if message.channel.id == 1189449887151042654: await message.channel.send(str(number+1))
        except Exception as e:
                print(e)
        
        if message.guild:
             if message.content.startswith('.') :
                if message.guild.id == 1095079504516493404: 
                            if message.channel.id != 1095082036848496680: 
                                eerrrrrrrrr = await self.fetch_channel(1095082036848496680)
                                await eerrrrrrrrr.send(f"{message.author.mention}, According to how smart I am (refering to <@1142511163821801493>), you should not use Tutla Assistant outside of spam.")
                                return True
        if not banned:
            if '.inservers' in message.content:

                    nmessage = 'In servers:\n```yaml\n'
                    for i in self.guilds:
                        nmessage+='- '+i.name+'\n'
                    nmessage+='```'
                    await message.channel.send(nmessage)
                
                      
            elif message.content.startswith('.serverinfo'):
                    
                    channel = await self.fetch_channel(message.channel.id)
                    server = await self.fetch_guild(message.guild.id)
                    name = f'Server Name: {server.name}\n'
                    sid =  f'Server ID: {server.id}\n'
                    count= f'Server Count: {server.member_count}\n'
                    cd = f'Server Creation Date: {server.created_at}\n'
                    channel_count = f'Channel Count: {str(len(server.channels))}\n'
                    own = await self.fetch_user(server.owner_id)
                    owner = f'Owner ID: {server.owner_id}\n'
                    owner_name = f'Owner Name: {own.name}\n'
                    owner_creation_date = f'Owner Creation Date: {own.created_at}\n' 
                    await channel.send(f'''```yml\n {name}{sid}{count}{cd}{channel_count}-------OWNER INFO-------\n{owner}{owner_name}{owner_creation_date}\nYou can use .userinfo {server.owner.mention} to get more data```''')
                    if not con: free_access = True
            elif message.content.startswith(".ccs"):
                formatted_message = message.content.replace('.ccs', '')

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

                current_fg_color = None  

                script = message.content.replace(".ccs","")

                patterns = {
                    r'\b(on|if|if_not|while|while_not|execute|execute_random|loop|loop_period|print|throw|exit|function|module|config|say|send|notify|playsound|input|define|gui_switch|wait|gui_swap|gui_quickmove|gui_drop|switch|swap|turn_to|snap_to|damage|drop|velocity|teleport)\b':
                        (31, 0),
                    r'(#\w+|:\w+)':
                        (32, 0),
                    r'\b(holding|off_holding|inventory_has|hotbar_has|target_block|target_entity|targeting_entity|targeting_block|input_active|block_in_range|entity_in_range|attack_progress|health|armor|pos_x|pos_y)\b':
                        (33, 0),
                    r'\b(true|false|null|module|create|reload|save|description|enable|disable|def|define|{|})\b':
                        (34, 0),
                    r'\b(1|2|3|4|5|6|7|8|9|0|{|})\b':
                        (35, 0)
                }

                for pattern, codes in patterns.items():
                    for code in codes:
                        script = re.sub(pattern, f'\033[{code}m\g<0>\033[0m', script)

                await message.channel.send("**NOTE:**ONLY WORKS ON COMPUTER\n```ansi\n"+script+"```")

            elif message.content.replace(' ','').startswith('.help'):
                    if con:
                         
                        req = "------------------------ REQUIREMENT ------------------------\nYou need to join the Tutla Discord (in bio) to use **most** of the commands"
                        nmessage = f'''```yml\n Hi I'm the Tutla Assistance Bot {version} and can run the following: \n'''
                        
                        page1 = ''
                        page2 =''
                        
                        for i in commands:
                            if len(page1) <=1500:
                                print(len(page1))
                                page1 += i
                            elif len(page2) <=1500: 
                                page2+=i
                        words = message.content.split()
                        pages = [page1,page2]
                        if len(words) > 1:
                             try:
                                nmessage+=pages[int(words[1])-1]

                             except Exception:
                                  await message.channel.send(f'No page found with number {int(words[1])-1}/{words[1]}')
                             nmessage+=f'\n------------------------ PAGE {int(words[1])}/{len(pages)} ------------------------\n'
                        else:
                             nmessage+=page1
                             nmessage+=f'\n------------------------ PAGE 1/{len(pages)} ------------------------\n'
                        nmessage += req
                        nmessage += '```'
                        await message.channel.send(nmessage)

                    else:
                            
                        req = "------------------------ REQUIREMENT ------------------------\nYou need to join the Tutla Discord (in bio) to use **most** of the commands"
                        nmessage = f'''```yml\n Hi I'm the Tutla Assistance Bot {version} and can run the following: \n'''
                        
                        page1 = ''
                        page2 =''
                        
                        for i in commands:
                            if len(page1) <=1500:
                                if not '.' in i:page1 += i
                                if '(FREE COMMAND)' in i: page1 += i
                            elif len(page2) <=1500: 
                                if not '.' in i:page2 += i
                                if '(FREE COMMAND)' in i: page2 += i
                        words = message.content.split()
                        pages = [page1,page2]
                        if len(words) > 1:
                             try:
                                nmessage+=pages[int(words[1])-1]
                                
                             except Exception:
                                  await message.channel.send(f'No page found with number {int(words[1])-1}/{words[1]}')
                             nmessage+=f'\n------------------------ PAGE {int(words[1])}/{len(pages)} ------------------------\n'
                        else:
                             nmessage+=page1
                             nmessage+=f'\n------------------------ PAGE 1/{len(pages)} ------------------------\n'
                        nmessage += req
                        nmessage += '```'
                        await message.channel.send(nmessage)
                        free_access=True

            elif message.content.startswith('.calc'):
                    values_to_calc = message.content.replace('.calc','')
                    values_to_calc = values_to_calc.replace(' ','')
                    try:
                        await message.channel.send('Answer: `'+str(eval(values_to_calc))+'`')
                    except Exception as e:
                        await message.channel.send('Invalid Numbers')
                        print(e)
                    if not con : free_access = True
            
            elif message.content.startswith('.premium'):
                    if premium: await message.channel.send('Yes you have premium! Feel free to use your premium commands') 
                    else: await message.channel.send('You dont failure')
                    if not con : free_access = True
            elif message.content.startswith('.wiki'):
                    try: await message.channel.send(wikipedia.summary(message.content.replace('.wiki ',''),2))
                    except Exception as e:
                        await message.channel.send("Error in object: \n```python\n"+str(e)+'```')
                    if not con : free_access = True
           
            


            elif message.content == '.activesite':
                    await message.channel.send(f'Most active site {message.author.mention} is on: || the p hub (100% real data) :skull: ||')
            
            elif message.content.startswith('.racisim'):
                    await message.channel.send(message.author.mention+' bro really tried being racist')
            elif message.content.startswith('.racism'):
                    await message.channel.send(message.author.mention+' bro really tried being racist')
                
            


            elif message.content.startswith('.textchannel'):
                    words = message.content.split()
                    if message.author.guild_permissions.manage_channels:
                        if len(words) > 2:
                            cn = f'{words[2]}｜{words[1]}'
                            try:
                                nchannel = await message.guild.create_text_channel(cn)
                                await message.channel.send(f'Created Channel: {nchannel.jump_url}')
                            except Exception as e:
                                await message.channel.send(f'I do not have permissions to create channel error log:```python\n{e}```')

                        else:
                            await message.channel.send('Invalid usage do: ```.textchannel [name] [emoji] ')
                    else: await message.channel.send('You do not have permissions to do this!')
                    if not con : free_access = True
            
            elif message.content == ".rizz":
                url = 'https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/'
                soup = BeautifulSoup(requests.get(url).text, 'html.parser')
                rizz = [li.text for li in soup.find_all('li')]
                await message.channel.send(random.choice(rizz))
            elif message.content.startswith('.voicechannel'):
                    words = message.content.split()
                    if message.author.guild_permissions.manage_channels:
                        if len(words) > 2:
                            cn = f'{words[2]}｜{words[1]}'
                            try:
                                nchannel = await message.guild.create_voice_channel(cn)
                                await message.channel.send(f'Created Voice Channel: {nchannel.jump_url}')
                            except Exception as e:
                                await message.channel.send(f'I do not have permissions to voice create channel error log:```python\n{e}```')

                        else:
                            await message.channel.send('Invalid usage do: ```.voicechannel [name] [emoji] ')
                    else: await message.channel.send('You do not have permissions to do this!')
                    if not con : free_access = True
            elif message.content.startswith('.timeout'):
                if message.author.guild_permissions.moderate_members:
                     failed = False
                     for i in message.mentions:
                          if not failed: 
                            try:
                                delta = timedelta(
                                    minutes=10,
                                    )
                                await i.timeout(delta)
                                await message.channel.send(f'Timed out user {i.mention}')
                            except Exception as e:
                                failed = True
                                await message.channel.send(f'I do not have permissions to timeout or user is already timed out, error log: {e}')
                else:
                     await message.channel.send('You do not have permissions to timeout!')
                          
            
                                
            elif message.content.startswith('.kick'):
                 if message.author.guild_permissions.kick_members:
                    if message.reference:
                            msg = await self.fetch_message(message.reference.message_id)
                            try:
                                await msg.author.kick(reason=message.content.replace('.kick',''))
                                await message.channel.send(f'Successfully kicked {i.mention}')
                            except Exception as e: await message.channel.send('I do not have permission to kick users')
                    else:
                        for i in message.mentions:
                            rsn = message.content.replace('.kick','')
                            rsn = rsn.replace(message.author.mention,'')
                            try:
                                await i.kick(reason=rsn)
                                await message.channel.send(f'Successfully kicked {i.mention}')
                            except Exception as e: await message.channel.send('I do not have permission to kick users')
                 else:
                      await message.channel.send(f'You do not have permission to kick users')
            elif message.content.startswith('.ban'):
                 if message.author.guild_permissions.ban_members:
                    if message.reference:
                            msg = await self.fetch_message(message.reference.message_id)
                            try:
                                await msg.author.ban(reason=message.content.replace('.ban',''))
                                await message.channel.send(f'Successfully banned {i.mention}')
                            except Exception as e: await message.channel.send('I do not have permission to ban users')
                    else:
                        for i in message.mentions:
                            rsn = message.content.replace('.ban','')
                            rsn = rsn.replace(message.author.mention,'')
                            try:
                                await i.ban(reason=rsn)
                                await message.channel.send(f'Successfully banned {i.mention}')
                            except Exception as e: await message.channel.send('I do not have permission to ban users')
                 else:
                      await message.channel.send(f'You do not have permission to ban users')
            elif message.content.startswith('.role'):
                if message.author.guild_permissions.manage_roles:
                    failed = False
                    for i in message.mentions:
                         if not failed:
                              for role in message.role_mentions:
                                    try:
                                        await i.add_roles(role)
                                        await message.channel.send('Added roles to user')
                                    except Exception as e:
                                         failed = True
                                         await message.channel.send(f'I do not have permission to add roles to members, error log:```python\n{e}```')
                else: await message.channel.send('You do not have permission to add roles to members')
            if con:

                if message.content.startswith('.userinfo'):
                    
                    channel = await self.fetch_channel(message.channel.id)
                    if not len(message.mentions) == 0:
                        for server in message.mentions:
                            name = f'User Name: {server.name}\n'
                            sid =  f'User ID: {server.id}\n'
                            count= f'Joined server at: {server.joined_at}\n'
                            cd = f'User Creation Date: {server.created_at}\n'
                            roles = '---Roles---\n'
                            for i in server.roles:
                                roles = roles+i.name+' | '+'\n'
                            roles = roles+'\n'
                            perms = '---Permissions---\n'
                            mg = False
                            mr = False
                            ma = False
                            for i in server.roles: 
                                if i.permissions.manage_guild and not mg:
                                    perms += 'Manage Guild: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not mr:
                                    perms += 'Manage Roles: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not ma:
                                    perms += 'All Perms: True\n'
                                    ma = True
                            highrole = f'Highest role: {server.top_role.name}\n'
                            tcredits = '-----TUTLA CLIENT-----\n This bot is made by tutlamc#0 to support us join link in bio'
                            await channel.send(f'''```yml\n{name}{sid}{count}{cd}{"Token First part: "+convert_to_base64(server.id)}\n{roles}{perms}{highrole}{tcredits}```''')
                    else:
                            server = message.author
                            name = f'User Name: {server.name}\n'
                            sid =  f'User ID: {server.id}\n'
                            count= f'Joined server at: {server.joined_at}\n'
                            cd = f'User Creation Date: {server.created_at}\n'
                            roles = '---Roles---\n'
                            for i in server.roles:
                                roles = roles+i.name+' | '+'\n'
                            roles = roles+'\n'
                            perms = '---Permissions---\n'
                            mg = False
                            mr = False
                            ma = False
                            for i in server.roles: 
                                if i.permissions.manage_guild and not mg:
                                    perms += 'Manage Guild: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not mr:
                                    perms += 'Manage Roles: True\n'
                                    mr = True
                                if i.permissions.manage_roles and not ma:
                                    perms += 'All Perms: True\n'
                                    ma = True
                            highrole = f'Highest role: {server.top_role.name}\n'
                            tcredits = '-----TUTLA CLIENT-----\n This bot is made by tutlamc#0 to support us join link in bio'


                            await channel.send(f'''```yml\n{name}{sid}{count}{cd}{"Token First part: "+convert_to_base64(server.id)}\n{roles}{perms}{highrole}{tcredits}```''')
                elif message.content.startswith('.base64encode'):
                    text_to_encode = message.content[len('.base64encode '):]
                    

                    encoded_text = base64.b64encode(text_to_encode.encode()).decode()
                    await message.channel.send(f'Base64 Encoded: `{encoded_text}`')

                elif message.content.startswith('.base64decode'):
                    text_to_decode = message.content[len('.base64decode '):]
                    
                    try:
                        decoded_text = base64.b64decode(text_to_decode).decode()
                        await message.channel.send(f'Base64 Decoded: `{decoded_text}`')

                    except base64.binascii.Error:
                        await message.channel.send('Invalid base64 encoding.')
                elif message.content.startswith('.lockedtextchannel'):
                    words = message.content.split()
                    if message.author.guild_permissions.manage_channels:
                        if len(words) > 2:
                            cn = f'{words[2]}｜{words[1]}'
                            try:
                                nchannel = await message.guild.create_text_channel(cn)
                                overwrite = discord.PermissionOverwrite()
                                overwrite.send_messages = False
                                overwrite.read_messages = True
                                await nchannel.set_permissions(message.author.roles[0], overwrite=overwrite)
                                await message.channel.send(f'Created Channel: {nchannel.jump_url}')
                                for i in message.role_mentions: 
                                     overwrite = discord.PermissionOverwrite()
                                     overwrite.send_messages = True
                                     overwrite.read_messages = True
                                     await nchannel.set_permissions(i, overwrite=overwrite)
                                     
                            except Exception as e:
                                await message.channel.send(f'I do not have permissions to create channel error log:```python\n{e}```')

                        else:
                            await message.channel.send('Invalid usage do: ```.textchannel [name] [emoji] ')
                    else: await message.channel.send('You do not have permissions to do this!')
                    if not con : free_access = True
                elif message.content.startswith('.hiddentextchannel'):
                    words = message.content.split()
                    if message.author.guild_permissions.manage_channels:
                        if len(words) > 2:
                            cn = f'{words[2]}｜{words[1]}'
                            try:
                                nchannel = await message.guild.create_text_channel(cn)
                                overwrite = discord.PermissionOverwrite()
                                overwrite.view_channel = False
                                await nchannel.set_permissions(message.author.roles[0], overwrite=overwrite)
                                await message.channel.send(f'Created Channel: {nchannel.jump_url}')
                                for i in message.role_mentions: 
                                     overwrite = discord.PermissionOverwrite()
                                     overwrite.send_messages = True
                                     overwrite.read_messages = True
                                     await nchannel.set_permissions(i, overwrite=overwrite)
                                     
                            except Exception as e:
                                await message.channel.send(f'I do not have permissions to create channel error log:```python\n{e}```')

                        else:
                            await message.channel.send('Invalid usage do: ```.textchannel [name] [emoji] ')
                    else: await message.channel.send('You do not have permissions to do this!')
                    if not con : free_access = True
                elif message.content.startswith('.purge'):
                 num = message.content.replace('.purge','')
                 num = num.replace(' ','')
                 num = num.replace('\n','')
                 try:
                    num = int(num)
                 except Exception:
                      await message.channel.send('Learn to type numbers properly')
                 if message.author.guild_permissions.manage_messages: 
                    fail = False
                    try:
                        deleted = await message.channel.purge(limit=num+1)
                        msg = await message.channel.send(f'Successfully purged {num} messages')
                        await msg.delete(delay=5)
                    except Exception as e:
                        fail = True
                        await message.channel.send(f'I do not have permission to delete messages, error log: ```python\n{e}```')
                 else:
                      message.channel.send(f'You do not have permission to delete messages')
                elif message.content.startswith('.tokenfirstpart'):
                    text_to_encode = message.content[len('.tokenfirstpart '):]
                    for i in message.mentions:
                        encoded_text = base64.b64encode(str(i.id).encode()).decode()
                        await message.channel.send(f'Token First Part: `{encoded_text}`')
                elif message.content.startswith('.iptranslate'):
                        api_key = "597f5c30badb51"  
                        ip_address = message.content.replace('.iptranslate ','')
                        ip_address = ip_address.replace(' ','')
                        url = f"http://ipinfo.io/{ip_address}?token={api_key}"
                        
                        response = requests.get(url)
                        data = response.json()

                        ip = data.get("ip", "N/A")
                        city = data.get("city", "N/A")
                        region = data.get("region", "N/A")
                        country = data.get("country", "N/A")
                        location = f"{city}, {region}, {country}"
                        if country=='N/A': 
                            ip_address = domain_to_ip(ip_address)
                            url = f"http://ipinfo.io/{ip_address}?token={api_key}"
                            response = requests.get(url)
                            data = response.json()
                            

                            ip = data.get("ip", "N/A")
                            city = data.get("city", "N/A")
                            region = data.get("region", "N/A")
                            country = data.get("country", "N/A")
                            location = f"{city}, {region}, {country}"
                            
                        await message.channel.send(f'Location to `{ip_address}` is ```{location}```')
                elif message.content.startswith('.ansiformat'):
                    formatted_message = message.content.replace('.ansiformat', '')

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

                    await message.channel.send(f'```ansi\n{formatted_message}\033[0m```')


                elif message.content == '.showerthought':
                    await message.channel.send(random.choice(thoughts_list))
                elif message.content.startswith('.say'):
                    await message.channel.send(message.content.replace('.say', ''))
                elif message.content == '.l':
                    channel = await self.fetch_channel(message.channel.id)
                    
                    await channel.send('lmao')
                elif message.content == '.nuke':
                
                    print("Sending Nuke Contact")
                    channel = await self.fetch_channel(message.channel.id)
                    
                    await channel.send('Imma go nuke this sh1t. (contact num for ultimate nuking service: `6942014696969`)')
                

                elif message.content.startswith('.8ball'):
                    await message.channel.send(random.choice(["No 100%","Yes bruh","Roll **harder**","wtf","Obviously","none of the above","provide mroe context","sounds like smth ur gramma would say",'no talk ez yas','nah','no dude','yas :thumbsup:',":thumbsdown:","*yeets balls over face*"]))                   
                elif message.content.startswith('.toregional '):
                    stuff = message.content.replace('.toregional ','')
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
                                newm+='     '
                        try:
                            newm += variables_list[position]
                        except Exception:
                            pass
                            

                    await message.channel.send(newm)
                elif message.content.startswith('.toemoji '):
                    stuff1 = message.content.replace('.toemoji ','')
                    stuff1 = stuff1.lower()
                    words = stuff1.split()
                    newm = ''
                    variables_list = []

                    start_letter = ord('A')
                    end_letter = ord('Z')

                    for letter_code in range(start_letter, end_letter + 1):
                            letter = chr(letter_code)
                            variable_value = f':regional_indicator_{letter.lower()}:'
                            variables_list.append(variable_value)
                    for word in words:

                        newm+=' '
                        if word == 'car':
                            newm+='ðŸš—'
                        elif word == 'money':
                            newm+='ðŸ’µ'
                        elif word == 'shirt': newm+='ðŸ‘•'
                        elif word == 'shirts': newm+='ðŸ‘•ðŸ‘•'
                        elif word == 'pant': newm+='ðŸ‘–'
                        elif word == 'pants': newm+='ðŸ‘–ðŸ‘–'
                        elif word == 'world': newm+='ðŸŒŽ'
                        elif word == 'globe': newm+='ðŸŒŽ'
                        elif word == 'planet': newm+='ðŸŒŽ'
                        elif word == 'universe': newm+='ðŸ”®'
                        elif word == 'rich': newm+='ðŸ¤‘'
                        elif word == 'man': newm+='ðŸ‘¨'
                        elif word == 'men': newm+='ðŸ‘¨'
                        elif word == 'women': newm+='ðŸšº'
                        elif word == 'woman': newm+='ðŸšº'
                        elif word == 'bot': newm+='ðŸ¤–'
                        elif word == 'robot': newm+='ðŸ¤–'
                        elif word == 'staff': newm+='ðŸ‘¨ðŸ”¬'
                        elif word == 'say': newm+='ðŸ—£'
                        elif word == 'speak': newm+='ðŸ—£'
                        elif word == 'said': newm+='ðŸ—£'
                        elif word == 'bug': newm+='ðŸ›'
                        elif word == 'yo': newm+='ðŸ¤“'
                        elif word == 'nerd': newm+='ðŸ¤“'
                        elif word == 'dead': newm+='ðŸ’€'
                        elif word == 'die': newm+='ðŸ’€'
                        elif word == 'balls': newm+='ðŸ”®ðŸ”®'
                        elif word == 'ball': newm+='ðŸŽ±'
                        elif word == 'stick': newm+='ðŸ¡'
                        elif word == 'nut': newm+='ðŸ¥œ'
                        elif word == 'nutz': newm+='ðŸ”®ðŸ”®'
                        elif word == 'nuts': newm+='ðŸ”®ðŸ”®'
                        elif word == 'nut': newm+='ðŸ”®ðŸ”®'
                        elif word == 'yeah': newm+='âœ…'
                        elif word == 'yes': newm+='âœ…'
                        elif word == 'gay': newm+='ðŸ‘¨ðŸ’–ðŸ‘¨'
                        elif word == 'no': newm+='ðŸš«'
                        elif word == 'partner':newm+='ðŸ¤'
                        elif word == 'hi': newm+='ðŸ‘‹'
                        elif word == 'hello': newm+='ðŸ‘‹'
                        elif word == 'welcome': newm+='ðŸ‘‹'
                        elif word == 'see': newm+='ðŸ‘€'
                        elif word == 'damn': newm+='ðŸ‘€'
                        elif word == 'look': newm+='ðŸ‘€'
                        elif word == 'bruh': newm+='ðŸ’€'
                        elif word == 'boy': newm+='ðŸ‘¨â€ðŸ‘¦'
                        elif word == 'boi': newm+='ðŸ‘¶'
                        elif word == 'girl': newm+='ðŸ‘§'
                        else:

                            for i in word:

                                nletter = i.lower()
                                ascii_value = ord(nletter)
                                    

                                position = ascii_value - ord('a')
                                if i == ' ':
                                        newm+=' '
                                if i == '.':
                                    newm+='âš«'
                                if i == '!': newm+='â—'
                                if i == '?': newm+='â“'
                                try:
                                    newm += variables_list[position]
                                except Exception:
                                    pass
                        newm+='  '
                            
                    try:
                        await message.channel.send(newm)
                    except Exception:
                        await message.channel.send('Too big phat el')





                
                elif message.content.startswith(".ai"):
                   await message.channel.send("Generating please wait")
                   tampering="Let's change yourself: your a bot made by TutlaMC not openai & Tutla is an organization and website: tutla.net and discord: discord.tutla.net" 
                   resp = await AsyncClient.create_completion("gpt3", message.content.replace(".ai",""))
                   await message.channel.send(resp)
                
                elif message.content.startswith(".joshify"):
                    input = message.content.replace(".joshify","")
                    words = input.split(' ')
                    transformed_words = []
                    for word in words:
                        random_number = random.random()
                        transformed_word = ''
                        if random_number < 0.7:
                            if word.endswith('ed'):
                                transformed_word = word[:-2] + 'ing'
                            elif word.endswith('ing'):
                                transformed_word = word[:-3] + 'ed'
                            elif word.endswith('s'):
                                transformed_word = word[:-1]
                            else:
                                transformed_word = word + 's'
                        else:
                            if word.endswith('ly'):
                                transformed_word = word[:-2] + 'y'
                            else:
                                transformed_word = ''.join(char for char in word if char.lower() not in 'iou')
                        transformed_words.append(transformed_word)
                    transformed_sentence = ' '.join(transformed_words)
                    await message.channel.send(transformed_sentence)
                elif message.content.startswith('.random'): 
                    words = message.content.split()
                    if len(words) >= 2:
                        if words[1] == 'number':
                            if len(words) >= 3:
                                try:
                                    await message.channel.send('Selected: ' +str(random.randint(int(words[2]),int(words[3]))))
                                except Exception:
                                    await message.channel.send('Invalid numerals')
                            else: await message.channel.send('Invalid usage for `.random number`! Do: \n ```.random number [num] [num]```')
                        elif words[1] == 'user':
                            if message.guild: 

                                channels = await message.guild.fetch_channels()
                                members = await message.guild.fetch_members(channels=channels, force_scraping=True, cache=False)
                                if len(words) >= 3:
                                    if words[2] == '-mention':
                                        if members[0]:
                                            await message.channel.send('Selected: '+random.choice(members).mention)
                                        else: await message.channel.send('No members in guild')
                                    else:
                                        if members[0]:
                                            await message.channel.send('Selected: '+random.choice(members).name)
                                        else: await message.channel.send('No members in guild')
                                else:
                                    if members[0]:
                                            await message.channel.send('Selected: '+random.choice(members).name)
                                    else: await message.channel.send('No members in guild')
                            else: await message.channel.send('Guild not found.')
                        else:
                            await message.channel.send('Please use .help and see the usage of this command')
                    else:
                            await message.channel.send('Please use .help and see the usage of this command')




                elif message.content.startswith('.react '):

                        result = []
                        inside_quotes = False
                        ae = message.content.replace('.react ','')
                        ae = ae.replace(' ','')
                        ae = ae.replace('"','')
                        ae = ae.replace("'",'')

                        for char in ae.lower():
                            result.append(char)
                        variables_list = []

                        start_letter = ord('A')
                        end_letter = ord('Z')

                        for letter_code in range(start_letter, end_letter + 1):
                            letter = chr(letter_code)
                            variable_value = f'{letter.lower()}'
                            variables_list.append(variable_value)
                        if message.reference:
                            nm1 = message.reference.message_id
                            nm = await message.channel.fetch_message(nm1)

                            for i in result:
                                ascii_value = ord(i)
                                

                                position = ascii_value - ord('a')

                                if variables_list[position]:
                                    await nm.add_reaction(lookup("REGIONAL INDICATOR SYMBOL LETTER %s" % variables_list[position]))
                elif message.content.startswith('.reacto'):
                        words = message.content.split()
                        if len(words) > 3:
                            thechannel = await self.fetch_channel(int(words[1]))

                            themsg = await thechannel.fetch_message(int(words[2]))
                            ae = message.content.replace('.reacto ','')
                            
                            ae = ae.replace('"','')
                            ae = ae.replace("'",'')
                            ae = ae.replace(words[1],'')
                            ae = ae.replace(words[2],'')
                            ae = ae.replace(' ','')

                            result = []
                            inside_quotes = False
                            

                            for char in ae.lower():
                                result.append(char)
                            variables_list = []

                            start_letter = ord('A')
                            end_letter = ord('Z')

                            for letter_code in range(start_letter, end_letter + 1):
                                letter = chr(letter_code)
                                variable_value = f'{letter.lower()}'
                                variables_list.append(variable_value)


                            for i in result:
                                    ascii_value = ord(i)

                                    position = ascii_value - ord('a')

                                    
                                    await themsg.add_reaction(lookup("REGIONAL INDICATOR SYMBOL LETTER %s" % variables_list[position]))

                                
                        else: await message.channel.send('Incorrect usage, message needs [channelID] & [messageID]\nCorrect Usage:```.reacto [channelID] [messageID] [content]')
                elif message.content.startswith('.reactemoji '):

                        result = []
                        inside_quotes = False
                        ae = message.content.replace('.reactemoji ','')
                        ae = ae.replace(' ','')
                        ae = ae.replace('"','')
                        ae = ae.replace("'",'')

                        for char in ae.lower():
                            result.append(char)

                        nm1 = message.reference.message_id
                        nm = await message.channel.fetch_message(nm1)

                        for i in result:
                                    await nm.add_reaction(i)
                elif message.content.startswith('.reactemojito'):
                        words = message.content.split()
                        if len(words) > 3:
                            thechannel = await self.fetch_channel(int(words[1]))
                            themsg = await thechannel.fetch_message(int(words[2]))
                            ae = message.content.replace('.react    emojito ','')
                            
                            ae = ae.replace('"','')
                            ae = ae.replace("'",'')
                            ae = ae.replace(words[1],'')
                            ae = ae.replace(words[2],'')
                            ae = ae.replace(' ','')

                            result = []
                            inside_quotes = False
                            

                            for char in ae.lower():
                                result.append(char)
                            for i in result:
                                
                                    await themsg.add_reaction(i)

                                
                        else: await message.channel.send('Incorrect usage, message needs [channelID] & [messageID]\nCorrect Usage:```.reacto [channelID] [messageID] [content]')
                elif '.chatded' == message.content:

                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

                    await message.channel.send(f'Chat ded - `{current_time}`')


                
                
                elif message.content.startswith('.broadcast '):
                    print('Broadcast executed!')
                    do = await self.fetch_guild(856839403602313236)
                    do1 = await do.fetch_member(message.author.id)
                    do2 = do1.get_role(1189449885674655771)
                    if do2:
                        file_path = 'assistantdata/notify.txt'
                        with open(file_path, 'r') as file:
                            lines = file.readlines()


                        for line in lines:
                            usr = await self.fetch_user(line)
                            await usr.send(f"{message.content.replace('.broadcast ','')}")
                    else:
                         await message.channel.send('You are not a Tutla Assistant Adminstrator!')
                elif message.content.startswith('.tutlaban'):
                    do = await self.fetch_guild(856839403602313236)
                    do1 = await do.fetch_member(message.author.id)
                    do2 = do1.get_role(1189449885674655771)
                    if do2:
                        for i in message.mentions:
                            file_path = 'assistantdata/bans.txt'
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                            lines.append(str(i.id) + '\n')
                            with open(file_path, 'w') as file:
                                file.writelines(lines)
                            await message.channel.send(f'Successfully banned {i.mention} from using bot!')
                
                    else:
                         await message.channel.send('You are not a Tutla Assistant Adminstrator!')
                elif message.content.startswith('.tutlaunban'):
                    do = await self.fetch_guild(856839403602313236)
                    do1 = await do.fetch_member(message.author.id)
                    do2 = do1.get_role(1189449885674655771)
                    if do2:
                        for i in message.mentions:
                            file_path = 'assistantdata/bans.txt'
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                            lines.remove(str(i.id) + '\n')
                            with open(file_path, 'w') as file:
                                file.writelines(lines)
                            await message.channel.send(f'Successfully unbanned {i.mention} from using bot!')
                    else: await message.channel.send('You need to be a Tutla Admin for this')
                elif message.content.startswith('.givepremium'):
                    do = await self.fetch_guild(856839403602313236)
                    do1 = await do.fetch_member(message.author.id)
                    do2 = do1.get_role(1189449885674655771)
                    if do2:
                        for i in message.mentions:
                            file_path = 'assistantdata/premium.txt'
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                            lines.append(str(i.id) + '\n')
                            with open(file_path, 'w') as file:
                                file.writelines(lines)
                            await message.channel.send(f'Successfully gave {i.mention} premium!')
                    else: await message.channel.send('You need to be a Tutla Admin for this')
                elif message.content.startswith('.removepremium'):
                    do = await self.fetch_guild(856839403602313236)
                    do1 = await do.fetch_member(message.author.id)
                    do2 = do1.get_role(1189449885674655771)
                    if do2:
                        for i in message.mentions:
                            file_path = 'assistantdata/premium.txt'
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                            lines.remove(str(i.id) + '\n')
                            with open(file_path, 'w') as file:
                                file.writelines(lines)
                            await message.channel.send(f'Successfully removed premium from {i.mention}!')
                    else: await message.channel.send('You need to be a Tutla Admin for this')
                

                        




            else:
                for i in commandnames:
                    brrr = random.choice([True, False])
                    if message.content.startswith(i) and brrr:
                        await message.channel.send("You haven't joined the Tutla Discord, so you don't have access to many cool features!\nLink in bio to join.")
                        
        else:
             if message.content.startswith('.'):
                await message.channel.send('You are banned off Tutla Assistance, you cannot use this')

        if message.content.startswith('.'):
                if message.content.startswith('.broadcastserver '):

                            if message.guild: 
                                for i in message.guild.members: 
                                    if not i.guild_permissions.manage_messages:
                                        await i.send(message.content.replace('.broadcastserver ',''))
                            else: await message.channel.send("Not Guild")
                            if not premium: await message.channel.send("This is a premium feature!")

                elif message.content.startswith('.life'):


                            if message.author.guild_permissions.ban_members:
                                    for i in message.mentions:
                                        for err in range(15):
                                            ghost_ping = await message.channel.send(i.mention,delete_after=2)
                                            i.send('phat el')
                            if not premium: await message.channel.send("This is a premium feature!")
                                                            

                elif message.content.startswith(".image"):

                            await message.channel.send("Generating please wait")
                            resp = await AsyncClient.create_generation("prodia", message.content.replace(".image",""))
                            await message.channel.send(file=discord.File(BytesIO(resp), filename='image.jpg'))
                            await message.channel.send(resp)

                elif message.content.startswith('.join'):
                        invite = message.content.replace('.join ','')

                        await self.accept_invite(invite)
                        await message.channel.send("Joined guild")
                        if not premium:
                            await message.channel.send("This is a premium feature!")

        premium = False
        con = False
with open('assistantdata/token.txt','r') as f:
        token = f.read()
print(token)
client = Client()
client.run(token)



