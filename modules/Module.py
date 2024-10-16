from modules.Utils import MainLogger
from discord import app_commands
import discord
from discord.ext import commands
from discord.app_commands import CommandOnCooldown
from typing import Tuple, Dict
from data import db
from modules.Utils import *
import traceback

class TermsButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
    async def accept(self, ctx: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await ctx.response.send_message("You have accepted the terms and conditions. You may now execute your command. Have fun with the bot!", ephemeral=True)
        self.stop()

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline(self, ctx: discord.Interaction, button: discord.ui.Button):
        self.value = False
        await ctx.response.send_message("You have declined the terms and conditions.", ephemeral=True)
        self.stop()

async def commandCheck(ctx: discord.Interaction):
        
        command_name = ctx.command.name
        params = ctx.namespace   

        MainLogger.log(f"Executing Command {command_name}")

        if ctx.user.id in premium_list: premium = True
        else: premium=False
        if ctx.user.id in banlist:banned=True
        else: banned = False
        if getAdminLevel(ctx.user.id) >= 2: premium = True; banned = False

        cmd = ctx.client.tree.get_command(command_name)
        if cmd:
            if hasattr(cmd, 'premium') and premium == False:
                await ctx.response.send_message("This is a premium command!",ephemeral=True)
                return False
        
        if banned: 
            await ctx.response.send_message("**You are banned** from using Tutla Assistance, therefore you cannot use this.",ephemeral=True)
            return False
        
        if not db.userExists(ctx.user.id):
            view = TermsButton()
            await ctx.response.send_message(f"Please accept the [terms and conditions](<{TOS}>) to continue", view=view)
            await view.wait()

            if view.value is None:
                await ctx.response.send_message("No response received.")
            elif view.value:
                db.add_user(ctx.user.id,premium=premium,banned=banned,mod=getAdminLevel(ctx.user.id),xp=1)
            else:
                await ctx.response.send_message("You declined the terms, you cannot proceed.")
                return False
            
        else: db.edit_user(ctx.user.id,premium=premium,banned=banned,mod=getAdminLevel(ctx.user.id),xp=db.getData(ctx.user.id,"xp")+1)
        
            
        return True



def premium_command(command):
    command.premium = True
    return command

def section_add(name,command):
    global commands2
    name = name.upper()
    section_name = "------- "+name+" --------\n"
    
    if name in commands2:        
        commands2[name]['commands'].update({command.name:command})
    else:

        commands2[name]={
             "display":section_name,
             "commands":{command.name:command}
        }

def get_command(command):
    final = False
    for category, category_data in commands2.items():
                            display_message = category_data['display']
                            commandsv2 = category_data['commands']
                            for command_name, command_object in commandsv2.items():

                                if command in command_object.aliases:
                                      final = True
                                      return command_object
    if not final: return None
'''
class Command:
    def __init__(self,name,description, method,category,aliases=[], params=[],isadmin =False,ispremium=False,usage=None):
        global cmd_count
        self.name = name
        self.description = description
        self.method = method
        self.category = category
        self.ispremium = ispremium
        self.aliases=aliases
        self.params = []
        for param in params:
            self.params.append(f"[{param}]")

        self.aliases.append(self.name)
        self.toappend = f"> - .{name} "
        for i in self.params:
                self.toappend+= f'`{i.upper()}` '
        if self.ispremium: self.toappend+= '🔮'
        self.toappend+= '\n> -# '+self.description
        
        
        self.usage_format = f".{self.name} {' '.join(param for param in self.params)}"
        if usage == None: 
            usage = "**The Usage has not been specified, so this is the usage built by the system:\n"
            usage+="This Command "+self.description.lower()+"**\n"
        self.usage = usage+f"\n.{self.name} {' '.join(param for param in self.params)}\n"+ f"Aliases:\n{chr(10).join(self.aliases)}"

            

        
        section_add(category,self)
        cmd_count +=1



        
    async def run(self,message,discord_client,params,command_data):
        MainLogger.log(f"Executing Command {params[0]}")
        await self.method(self,message,discord_client,params,command_data)



'''