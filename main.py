import discord
import random as ran
from discord.ext import tasks
from math import *
import os


from assistantdata import db

from modules.Utils import *
ModLogger.log("Importing Mods",style="execution")

import mods.ClickCrystalsBot
import mods.SniperMod
import mods.EMod
import mods.sudo
from mods import mod

MainLogger.log("Loading all modules",style="execution")

from modules.TUTLA import tutlasearch

from modules.CLIENT import admin
from modules.CLIENT import changelog
from modules.CLIENT import help
from modules.CLIENT import join
from modules.CLIENT import premium
from modules.CLIENT import listcmd
from modules.CLIENT import reload
from modules.CLIENT import report
from modules.CLIENT import say
from modules.CLIENT import version

from modules.ECONOMY import coins
from modules.ECONOMY import daily
from modules.ECONOMY import leaderboard
from modules.ECONOMY import rob
from modules.ECONOMY import xp

from modules.INFO import ipinfo
from modules.INFO import serverinfo
from modules.INFO import userinfo
from modules.INFO import tokenfirstpart
from modules.INFO import wiki
from modules.INFO import wordinfo

from modules.TOOLS import afk
from modules.TOOLS import ai
from modules.TOOLS import ansiformat
from modules.TOOLS import ball
from modules.TOOLS import base
from modules.TOOLS import binary
from modules.TOOLS import calc
from modules.TOOLS import ccs
from modules.TOOLS import code
from modules.TOOLS import coinflip
from modules.TOOLS import currency
from modules.TOOLS import dice
from modules.TOOLS import freaky
from modules.TOOLS import giveaway
from modules.TOOLS import hex
from modules.TOOLS import player
from modules.TOOLS import poll
from modules.TOOLS import qr
from modules.TOOLS import random
from modules.TOOLS import react
from modules.TOOLS import regional
from modules.TOOLS import rgb
from modules.TOOLS import rizz
from modules.TOOLS import translate
from modules.TOOLS import unsplash
from modules.TOOLS import weather
from modules.TOOLS import yt

from modules.IMAGES import caption
from modules.IMAGES import cartoon
from modules.IMAGES import colorblind
from modules.IMAGES import gradient
from modules.IMAGES import imagemods
from modules.IMAGES import scale
from modules.IMAGES import tfi

from modules.FUN import activesite
from modules.FUN import antinpc
from modules.FUN import chatded
from modules.FUN import doxx
from modules.FUN import facts
from modules.FUN import fox
from modules.FUN import joshify
from modules.FUN import ghostping
from modules.FUN import infinitecraft
from modules.FUN import infiniterps
from modules.FUN import lmao
from modules.FUN import minigames
from modules.FUN import nuke
from modules.FUN import racism
from modules.FUN import showerthought

from modules.ADMIN import role, timeout, kick, ban, purge, textchannel, voice_channel 

from modules.Module import *

import threading

MainLogger.log(f"Successfully loaded all modules, mods & {str(cmd_count)} commands!", style="success")



def tutlashell_input():
    MainLogger.log("Loading Tutla Shell",style="execution")
    while True:
        cmd = input("Tutla Shell > ")
        ShellLogger.log(execute(cmd)) # Utils command



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

            



class Client(discord.Client):

    async def on_ready(self): # Throws an AD into Status
        global tutlaguild, bot
        bot = self
        MainLogger.log("Initializing Tutla Assistance",style="execution")

        premium_reload() # Util Command to get all premium users
        ban_reload()  
        DBLogger.log(db.printDB(),style="execution")

        #await self.change_presence(status=discord.Status.idle, activity=discord.CustomActivity(name="join4join.xyz"))# j4j farm fr
        
        ModLogger.log("Initializing Mods",style="execution")
        for mode in mod.mods: # Mod Intializer
            mode.bot = self
            if mode.initial != None:
                await mode.initial()
        ModLogger.log("Sucessfully Intialized Mods",style="success")

        tutlashellThread = threading.Thread(target=tutlashell_input).start()
        
        mainloop.start(eself=self)
        MainLogger.log("Initialized Mainloop",style="success")
        
        MainLogger.log("Successfully Initialized Tutla Assistance!",style="success")



    
    async def on_message(self,message): 
        global premium_list       
        if message.author.id != self.user.id and self_bot: return False
        for mode in mod.mods: # Mod On Message
            if mode.onMessage != None:
                await mode.onMessage(message)

        ############## User Checks ##############

       
       
        
        if message.author.id in premium_list: premium = True
        else: premium=False
        if message.author.id in banlist:banned=True
        else: banned = False
        ##############             ##############
        
        
        
        
        if not banned: # Now the Actual Code
            
            
            if message.content.startswith('.'): # checks for prefix
                command_data = { # Retrives all the Users Checks
                 'banned':banned,
                 'premium':premium
                }

                

                for category, category_data in commands2.items():  # loops through commands, "commands" doesnt not exist. only commands2
                    display_message = category_data['display'] # Display message is basically the title of the category
                    commands = category_data['commands']
                    
                    for command_name, command_object in commands.items(): # Loops through all the commands (even i dont understand my code)

                        params = message.content.split() 
                        if str(message.content.split()[0].lower().replace('.','')) in command_object.aliases:  # 1. Gets The first word in lowercase 2. Removes the "." 3. Finds it in aliases as the command name is also in aliases
                            if not db.userExists(message.author.id):
                                db.add_user(message.author.id,premium=premium,banned=banned,mod=getAdminLevel(message.author.id),coins=0)
                            else: db.edit_user(message.author.id,premium=premium,banned=banned,mod=getAdminLevel(message.author.id))
                            

                            await message.channel.typing()
                            if command_object.ispremium: # Checks if command and user are in premium
                                if premium:
                                    await command_object.run(message, self, message.content.split(),command_data)
                                    done = True
                                else:
                                 await message.channel.send("Did you just try a premium command? No way!")
                            else: 
                                 await command_object.run(message, self, message.content.split(),command_data)
                                 done = True
                            
                            try:  await message.delete() 
                            except Exception as e: pass # Removed Annoying message No Permission Error
                            xp = db.getData(message.author.id,"xp")
                            if xp == None: db.edit_user(message.author.id,xp=0)
                            db.edit_user(message.author.id,last_command=command_name,slowmode=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),xp=db.getData(message.author.id,"xp")+1)
                             
            if message.content == ".balls":
                 await message.channel.send("https://tenor.com/view/balls-gif-22045792")
                        
        else:
             for category, category_data in commands2.items(): # See previous loop
                    display_message = category_data['display']
                    commands = category_data['commands']
                    
                    for command_name, command_object in commands.items():

                        if str(message.content.split()[0].lower().replace('.','')) in command_object.aliases:  # Checks if command exists so it can flare
                            await message.channel.send('You are banned off Tutla Assistance, you cannot use this')
                        
        try:
                
                if "counting" in message.channel.name and message.channel.guild.member_count < 2000: # OMG COUNTING SIMULATOR V2 11!!11!!!!!!!1!11!!
                    mc = message.content
                    number = int(mc)
                    
                    if message.author.id != client.user.id :
                        await message.channel.send(str(number+1))
        except Exception as e:
                pass 

                        
        
        premium = False # cuz it's global (idk maybe or atleast used to, since V1.1 or 1.2)
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
        if ran.randint(1,500) == 2: await message.channel.send("my pee pee isnt poo poo")


        

    async def on_message_delete(self,message):
         for module in mod.mods: # Mod on_delete
            if module.onDelete != None:
                await module.onDelete(message) 
    async def on_message_edit(self,before,after):
         for module in mod.mods: # Mod on_edit
            if module.onEdit != None:
                await module.onEdit(before,after) 

token = os.getenv("TA_TOKEN")
client = Client()
client.run(token)