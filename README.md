# tutla-assistant
Official Tutla Assistant Bot source code

## The Bot
The Tutla Assitant bot has been a project I've worked on for a long time. Today, I decided to share this project.
Tutla Assistant is a Discord Selfbot that has many QOL & Helpful commands, you can see all the commands by running `/help` on any channel.

## UPDATE V2
See https://github.com/TutlaMC/tutla-assistant/blob/main/changelog.md



## Installation
You require:
- Python 3.8+

Python Libraries: `requirements.txt`

**YOU DO NOT NEED DISCORD INSTALLED, IT USES DISCORD's API TO SEND AND GET REQUESTS**

To install this you will first install Python 3.8+ with it in the environment variables. After that you may want to install each of the libraries as follows:
`pip install -r requirements.txt`

Once successfully installing the libraries you would want to make some changes in the `config`, here's how to:
(`data/config.json`)
```json
{
    "version":"v2", // version
    "dev_mode":false, // developer mode
    "feed":true, // if you want subscribers to your feed
    "logging_channel": 0,// The channel (id in INT) where you'll store the QOTD, Bugs & Suggestions in
    "phrases":{
        "discords": "YOUR DISCORD SERVER LINKS",
        "about": "ABOUT YOUR BOT",
        "TOS":"https://github.com/TutlaMC/tutla-assistant/blob/main/TOS.md OR YOUR CUSTOM TOS"
    }
}
```
Change these accordingly or use the prebuilt one we've provided (but do change the `logging_channel` var).

Then you may proceed to adding the account you want to run the assistant program on. You must get the token of the account and create an environmental vairable called "TOKEN" and "rapid_api_key" (get it at the rapid api website).

### 24/7 running
You'll first need a host that uses (Windows is fine but we're using an `sh` file here)
We have also added `run.sh` (for linux) that will restart the file when it crashes (it sometimes crashes). You will need to change `python3.9 main.py` to whatever suits you. That line is the command to run the script with `python3.9` being your python executable command and the following file is your code. 

Run `./run.sh` to get it started

# Docs

## Creating a Command
Open up the modules folder and in one of the section create your file. It doesn't need to be in any of the categories, it just needs the ability to import `Module.py`.

After that you can follow this example if it's in my command structure:
```python
from ..Module import *
from ..Utils import *
import discord
class YourCogCommands(commands.Cog): # (Optional, you can use the cogs we've already provided) 
    def __init__(self, bot):
        self.bot = bot

    @premium_command # (Optional) Decorator to make it a premium command
    @app_commands.command(name="dm",description="DM a user") # Create the Command
    @app_commands.check(commandCheck) # (Reccomended) (Optional) Check for reject command for banned users and TOS requirement
    @app_commands.user_install() # (Optional) Make it a User Install command
    async def dm_callback(self,interaction: discord.Interaction,user:discord.User,text:str): # Paramaters
        await user.send(text)
        await interaction.response.send_message("Sent!",ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(YourCogCommands(bot))
```


1. `from ..Module import *` This code automatically import all the neccasary libraries
2. Next we have the decorators which as you see in the comments makes it a premium, user installable command which is named "dm" and can "Dm a user". The command check checks for several things and which I definetly reccomend using
3. Next we come to the asynchronous function, you can name it anything and requires the `self` and `interaction` parameters
4. Inside the command we send the `user` a message (`text`) and then respond to the `interaction` by telling you've sent the message
5. the `setup` and Cog declaration is used for creating the Cog tohandle the commands. You can use any of the cogs I've alreayd provided for it.

*AdvancedCogs are group commands, `group = app_commands.Group(name="groupName", description="groupDesc")` they have almost no difference apart from the fact that they can't be used as a user_install command, commands are not cerated with `app_commands.command` but with `group.command` and you can create subcommands by just adding a `parent=group` to the parent group.*
    

## Database 
`from data import db`, uses `sqllite3`

```yaml
Func initalize_db(): Intializes DB
Func printDB(): Returns DB Contents

Func add_user(user_id: int, member=False, premium=False, banned=False, mod=0, aura=1000, slowmode=None, last_command=" ",daily=None,xp=10): Adds a user to the DB
Func edit_user(user_id: int, member=False, premium=False, banned=False, mod=0, aura=1000, slowmode=None, last_command=" ",daily=None,xp=10): Edit a user's data
Func user_exists(user_id): Returns if a user's data is stored or not
Func get_data(user_id, column_name): Get a specific user data
```

```yaml
Func initalize_db(): Intializes DB
Func printDB(): Returns DB Contents

Func add_server(server_id: int, **kwargs): Adds a server to the DB
Func edit_server(server_id: int, **kwargs): Edit a server's data
Func server_exists(server_id): Returns if a server's data is stored or not
Func get_data(server_id, column_name): Get a specific server data
```


## Utils 


`from modules import Utils`

Globals
```yaml
List premium_list []: Premium users
List banlist []: Banned Users 

# config.json load

Var version: Current Version
Var dev_mode [bool]: Debug Mode
Var feed [bool]: Enables subscribption
Var logging_channel: Channel for storing data

Var about: About your bot
Var discords: Your discords
Var TOS: TOS

Var true: True
Var false: False

Func premium_reload: Reloads all premium users (premium_list)
Func ban_reload: Reloads all banned users (banlist)
Func getCmdCount: Returns total command count
```

Logging
```yaml
Class Logger(name:str): Creates a Logger to print neat output (intead of print)
    log(text, style="normal|warning|error|execution|success"): Main print function
Func dlog(text): Debug logger

ModuleLogger: Logger("module")
HTTPLogger: Logger("http")
ModLogger: Logger("mod")
DBLogger: Logger("database")
MainLogger: Logger("main")
ShellLogger: Logger("shell")
DebugLogger: Logger("debug")
```

Command-Based Functions:
```yaml
Func isInSlowmode(user_id,time): Checks if user's slow mode exceeds time (time in seconds)
Func getSlowmode(user_id): Get's user's slowmode-ctime diff

Func getAdminLevel(user_id): Returns user's Tutla Admin Level (0-4)
Func message_without_command(params:List[message.content.split()]): Returns the message without it's initial execution command as a string
```

Utility Functions:
```yaml
Func ai(prompt): Generates AI Response
Func execute(command): Executes Tutla Shell Prompts
```


## Modding
Modding in Tutla Assistance is an alternative to making commands and is way more flexible and has much more use than a command. If you want to create something simple try a command but a complex project like a SnipeBot or a ChatBot.

```python
class Mod:
    def __init__(self,name,description):
        self.name = name
        self.description = description

        self.initial = None # Intialization Command
        self.onMessage = None # On Message trigger
        self.onDelete = None # On message_delete trigger

        self.bot = None # Bot Access, discord.Client

    async def initial_executor(self,function): # Sets your initialization function, triggered within 15 seconds of bot mainloop.
        self.initial = function
        await function()
    def on_message(self, function): # Sets your message trigger
        self.onMessage = function
    def on_delete(self,function): # Sets your delete trigger
        self.onDelete = function
```