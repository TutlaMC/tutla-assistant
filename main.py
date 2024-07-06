import discord
import time
import requests
import random
from bs4 import BeautifulSoup
import base64
from datetime import datetime
import re
from PIL import Image
from io import BytesIO
from math import *
import os
import socket
from asyncio import run


from modules.CLIENT import help
from modules.CLIENT import premium
from modules.CLIENT import inservers
from modules.CLIENT import say
from modules.CLIENT import join

from modules.INFO import serverinfo
from modules.INFO import userinfo
from modules.INFO import tokenfirstpart
from modules.INFO import wiki

from modules.TOOLS import ai
from modules.TOOLS import ansiformat
from modules.TOOLS import calc
from modules.TOOLS import ccs
from modules.TOOLS import ball
from modules.TOOLS import base64encode
from modules.TOOLS import base64decode
from modules.TOOLS import ipinfo
from modules.TOOLS import random
from modules.TOOLS import react
from modules.TOOLS import regional
from modules.TOOLS import rizz

from modules.FUN import activesite
from modules.FUN import chatded
from modules.FUN import joshify
from modules.FUN import life
from modules.FUN import lmao
from modules.FUN import nuke
from modules.FUN import racism
from modules.FUN import showerthought

from modules.ADMIN import role, timeout, kick, ban, purge, textchannel, voice_channel 

from modules.example import example

from modules.Module import *
from modules.Utils import *
          
premium_reload()
ban_reload()

                



class Client(discord.Client):
    timelimit = [1180058692960399442]
    timelimitcount=[0]

    async def on_ready(self):
        global dev_mode
        print("Tutla Assistance Initialized")
        game = discord.Streaming(name="discord.tutla.net",game="discord.tutla.net",url="https://discord.tutla.net")
        await client.change_presence(status=discord.Status.idle, activity=game)


         
    async def on_message(self,message): 
        global premium_list
        global thoughts_list

        
        
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
            command_data = {
                 'banned':banned,
                 'premium':premium, 
                 'member':con
            }
            done = False
            if message.content.startswith('.'):
                for category, category_data in commands2.items():
                    display_message = category_data['display']
                    commands = category_data['commands']
                    
                    for command_name, command_object in commands.items():

                        params = message.content.split()
                        if str(message.content.split()[0].lower().replace('.','')) in command_object.aliases: 
                            if command_object.ispremium:
                                if premium:
                                    await command_object.run(message, self, message.content.split(),command_data)
                                    done = True
                                else:
                                 await message.channel.send("Did you just try a premium command? No way!")
                            elif not con and not command_object.isfree:
                                 await message.channel.send("This is a Tutla Member only command!")
                            else: 
                                 await command_object.run(message, self, message.content.split(),command_data)
                                 done = True
                             
            if message.content == ".balls":
                 await message.channel.send("https://tenor.com/view/balls-gif-22045792")

                        



                        
        else:
             for category, category_data in commands2.items():
                    display_message = category_data['display']
                    commands = category_data['commands']
                    
                    for command_name, command_object in commands.items():

                        params = message.content.split()
                        if str(message.content.split()[0].lower().replace('.','')) in command_object.aliases: 
                            await message.channel.send('You are banned off Tutla Assistance, you cannot use this')
                        
        if message.content.startswith('.broadcast '):
                        print('Broadcast executed!')
                        do = await self.fetch_guild(1189449885615927296)
                        do1 = await do.fetch_member(message.author.id)
                        do2 = do1.get_role(1218819695260602428)
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
                        ban_reload()
                        do = await self.fetch_guild(1189449885615927296)
                        do1 = await do.fetch_member(message.author.id)
                        do2 = do1.get_role(1218819695260602428)
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
                        ban_reload()
                        do = await self.fetch_guild(1189449885615927296)
                        do1 = await do.fetch_member(message.author.id)
                        do2 = do1.get_role(1218819695260602428)
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
                        ban_reload()
                        premium_reload()
                        do = await self.fetch_guild(1189449885615927296)
                        do1 = await do.fetch_member(message.author.id)
                        do2 = do1.get_role(1218819695260602428)
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
                        premium_reload()
                        do = await self.fetch_guild(1189449885615927296)
                        do1 = await do.fetch_member(message.author.id)
                        do2 = do1.get_role(1218819695260602428)
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

        elif message.content.startswith('.broadcastserver '):

                            if message.guild: 
                                for i in message.guild.members: 
                                    if not i.guild_permissions.manage_messages:
                                        await i.send(message.content.replace('.broadcastserver ',''))
                            else: await message.channel.send("Not Guild")
                            if not premium: await message.channel.send("This is a premium feature!")
                        

        premium = False
        con = False
with open('assistantdata/token.txt','r') as f:
        token = f.read()
print(token)
client = Client()
client.run(token)