import discord
from math import *
import sys 
import mods.ClickCrystalsBot
import mods.SniperMod
import mods.EMod
import mods.sudo
from mods import mod

from modules.CLIENT import dm
from modules.CLIENT import help
from modules.CLIENT import inservers
from modules.CLIENT import join
from modules.CLIENT import premium
from modules.CLIENT import listmods
from modules.CLIENT import reload
from modules.CLIENT import say
from modules.CLIENT import version


from modules.INFO import serverinfo
from modules.INFO import userinfo
from modules.INFO import tokenfirstpart
from modules.INFO import wiki

from modules.TOOLS import ai
from modules.TOOLS import ansiformat
from modules.TOOLS import binary
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
from modules.FUN import doxx
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

import threading

sys.dont_write_bytecode = True

def tutlashell_input():
    while True:
        cmd = input("Tutla Shell > ")
        if cmd == "exit":
             exit()
tutlashellThread = threading.Thread(target=tutlashell_input).start()

      
premium_reload() # Util Command to get all premium users
ban_reload()  



class Client(discord.Client):
    timelimit = [1180058692960399442]
    timelimitcount=[0]

    async def on_ready(self): # Throws an AD into Status
        global dev_mode
        print("Tutla Assistance Initialized")
        #game = discord.Streaming(name="discord.tutla.net",game="discord.tutla.net",url="https://discord.tutla.net") 
        #await client.change_presence(status=discord.Status.idle, activity=game)

        for mode in mod.mods: # Mod Intializer
            mode.bot = self
            if mode.initial != None:
                await mode.initial()


    
    async def on_message(self,message): 
        global premium_list       
        for mode in mod.mods: # Mod On Message

            if mode.onMessage != None:
                await mode.onMessage(message)

        ############## User Checks ##############
        thisguild = await self.fetch_guild(1189449885615927296)
        con = False
        try:
            boimember = await thisguild.fetch_member(message.author.id)
            if boimember:
                con = True
        except Exception as e:
            con = False
       
       
        
        if str(message.author.id) in premium_list: premium = True
        else: premium=False
        if str(message.author.id) in banlist:banned=True
        else: banned = False
        ##############             ##############
        
        
        
        
        if not banned: # Now the Actual Code
            command_data = { # Retrives all the Users Checks
                 'banned':banned,
                 'premium':premium, 
                 'member':con
            }
            done = False # no clue why this exists
            if message.content.startswith('.'): # checks for prefix
                for category, category_data in commands2.items():  # loops through commands, "commands" doesnt not exist. only commands2
                    display_message = category_data['display'] # Display message is basically the title of the category
                    commands = category_data['commands']
                    
                    for command_name, command_object in commands.items(): # Loops through all the commands (even i dont understand my code)

                        params = message.content.split() 
                        if str(message.content.split()[0].lower().replace('.','')) in command_object.aliases:  # 1. Gets The first word in lowercase 2. Removes the "." 3. Finds it in aliases as the command name is also in aliases
                            if command_object.ispremium: # Checks if commadn and user are in premium
                                if premium:
                                    await command_object.run(message, self, message.content.split(),command_data)
                                    done = True
                                else:
                                 await message.channel.send("Did you just try a premium command? No way!")
                            elif not con and not command_object.isfree: # If it's not a "free" command
                                 await message.channel.send("This is a Tutla Member only command!")
                            else: 
                                 await command_object.run(message, self, message.content.split(),command_data)
                                 done = True
                            try:  await message.delete() 
                            except Exception as e: pass # Removed Annoying message No Permission Error
                             
            if message.content == ".balls":
                 await message.channel.send("https://tenor.com/view/balls-gif-22045792")
                        
        else:
             for category, category_data in commands2.items(): # See previous loop
                    display_message = category_data['display']
                    commands = category_data['commands']
                    
                    for command_name, command_object in commands.items():

                        params = message.content.split()
                        if str(message.content.split()[0].lower().replace('.','')) in command_object.aliases:  # Checks if command exists so it can roast
                            await message.channel.send('You are banned off Tutla Assistance, you cannot use this') # *roasts* *audience laughs*
                        
        try:
                
                if "counting" in message.channel.name: # OMG COUNTING SIMULATOR V2 11!!11!!!!!!!1!11!!
                    mc = message.content
                    number = int(mc)
                    
                    if message.author.id != client.user.id :
                        if  message.channel.id == 1127010732668620800: await message.channel.send(str(number+1))
                        if message.channel.id == 1189449887151042654: await message.channel.send(str(number+1))
        except Exception as e:
                pass # forgot to add n before pass
                # print(e) # we dont need errors . we too cool for errors  
        if message.content.startswith('.tutlaban'):
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
                        
        
        premium = False # cuz it's global (idk maybe or atleast used to, since V1.1 or 1.2)
        con = False 
    async def on_message_delete(self,message):
         for module in mod.mods: # Mod Intializer
            if module.onDelete != None:
                await module.onDelete(message) 
with open('assistantdata/token.txt','r') as f:
        token = f.read()
# print(token)
client = Client()
client.run(token)