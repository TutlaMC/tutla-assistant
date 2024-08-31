# tutla-assistant
Official Tutla Assistant Bot source code

## The Bot
The Tutla Assitant bot has been a project I've worked on for a long time. Today, I decided to share this project.
Tutla Assistant is a Discord Selfbot that has many QOL & Helpful commands, you can see all the commands by running `.help` on any channel.

## UPDATE 1.5
See https://github.com/TutlaMC/tutla-assistant/blob/main/changelog.md


## Note
This is a selfbot and break Discord's TOS, use it knowing the risks. Secondly, the source code provided is raw and has not been modified for your installation. You willl manually have to change the invite links and so on, you may want to change:
- The Admin Command Roles
- Invite
- Support Links
- Custom Discord server configurations
- Ballsdex pings for myself

## Installation
You require:
- Python 3.8+

Python Libraries: `requirements.txt`

**YOU DO NOT NEED DISCORD INSTALLED, IT USES DISCORD's API TO SEND AND GET REQUESTS**

To install this you will first install Python 3.8+ with it in the environment variables. After that you may want to install each of the libraries as follows:
`pip install -r requirements.txt`

Once successfully installing the libraries you would want to make some changes in the file as it has many advertisements to our Discord and more which have been listed in the notice above.

Then you may proceed to adding the account you want to run the assistant program on. You must get the token of the account and create an environmental vairable called "TA_TOKEN".
Once the installation is complete you can follow this **optional** method that keeps it 24/7/365:

### Running as a SelfBot (Beta)
You can run Tutla Assistance as a Selfbot on your own user by setting the `self_bot` variable in `modules/Utils.py` to `True`. It disables anyone other than the user token from using it. 

### 24/7 running
We have also added `run.sh` (for linux) that will restart the file when it crashes (it sometimes crashes). You will need to change `python3.9 main.py` to whatever suits you. That line is the command to run the script with `python3.9` being your python eecutable command and the following file is your code. 

Run `./run.sh` to get it started

# Docs

## Creating a Command
Open up the modules folder and in one of the section create your file. It doesn't need to be in any of the categories, it just needs the ability to import `Module.py`.

After that you can follow this example if it's in my command structure:
```python
from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def example_callback(CommandObject,message,self,params,command_data):
                    premium = command_data['premium']
                    await message.channle.send(CommandObject.description+f"\nWhat you said: {params[1]}")
ex_command = Command("example","Example command for making a PR to the Tutla Asisstance bot, see the Github for more info.",example_callback,CLIENT,aliases=['command','ex'],params=["TEST PARAM"])
```


1. `from ..Module import *` will give you the Command Class and a few categories to start with. Change this line to your file structure
2. Next we come to the asynchronous function, you can name it anything but it must be updated in the Command declaration. This function must take 5 parameters.
3. Inside the command we can get the "member" variable off the command_data. You can use this to check if the member is a part of your server, similiarly of premium. Then finally we send a message with the description of the command and the first parameter.
4. Finally we will declare the command with it's name, description, function to execute it and category. Additionally we are also giving aliases to for easier remembrance and parameters (this does not give functionality, it only displays on the help menu) and finally we are making this command free allowing anyone to use it.

**NOTE:** Aliases are needed as they will trigger for every command if not applied, this is a bug and will be fixed next update.
**NOTE:** The category template can be declared in Module.py and you can pass ina  string for the category if not declaring in Module.py

## Database 
`from assistantdata import db`, uses `sqllite3`

```yaml
Func initalize_db(): Intializes DB
Func printDB(): Returns DB Contents

Func add_user(user_id: int, member=False, premium=False, banned=False, mod=0, aura=1000, slowmode=None, last_command=" ",daily=None,xp=10): Adds a user to the DB
Func edit_user(user_id: int, member=False, premium=False, banned=False, mod=0, aura=1000, slowmode=None, last_command=" ",daily=None,xp=10): Edit a user's data
Func user_exists(user_id): Returns if a user's data is stored or not
Func get_data(user_id, column_name): Get a specific user data
```


## Utils 


`from modules import Utils`

Globals
```yaml
List premium_list []: Premium users
List banlist []: Banned Users 

Var version: Current Version
Var dev_mode [true/false]: Debug Mode
Var self_bot [true/false]: Selfbot Mode

Var true: True
Var false: False

Func premium_reload: Reloads all premium users (premium_list)
Func ban_reload: Reloads all banned users (banlist)
Func getCmdCount(): Returns total command count
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
Func ai(text): Generates AI Response
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