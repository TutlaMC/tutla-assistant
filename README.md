# tutla-assistant
Official Tutla Assistant Bot source code

## The Bot
The Tutla Assitant bot has been a project I've worked on for a long time. Today, I decided to share this project.
Tutla Assistant is a Discord Selfbot that has many QOL & Helpful commands, you can see all the commands by running `.help` on any channel.

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

  Python Libraries:
- discord.py-self
- wikipedia
- freegpt
- BeautifulSoup
- pillow

**YOU DO NOT NEED DISCORD INSTALLED, IT USES DISCORD's API TO SEND AND GET REQUESTS**

To install this you will first install Python 3.8+ with it in the environment variables. After that you may want to install each of the libraries as follows:
`pip install discord.py-self wikipedia freegpt beautifulsoup4 pillow`

Once successfully installing the libraries you would want to make some changes in the file as it has many advertisements to our Discord and more which have been listed in the notice above.

Then you may proceed to adding the account you want to run the assistant program on. You must get the token of the account and paste it into `assistantdata/token.txt`. You may cofigure premium account in `premium.txt` and banned users in `bans.txt` both in `assistantdata`.
Once the installation is complete you can follow this **optional** method that keepsit 24/6/365:

### 24/7 running
We have also added `run.sh` (for linux) that will restart the file when it crashes (it sometimes crashes). You will need to change `python3.9 main.py` to whatever suits you. That line is the command to run the script with `python3.9` being your python eecutable command and the following file is your code. 

Run `./run.sh` to get it started


## Creating a Command
Open up the modules folder and in one of the section create your file. It doesn't need to be in any of the categories, it just needs the ability to import `Module.py`.

After that you can follow this example if it's in my command structure:
```python
from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def example_callback(CommandObject,message,self,params,command_data):
                    is_member = command_data['member']
                    premium = command_data['premium']



                    await message.channle.send(CommandObject.description+f"\nWhat you said: {params[1]}")
ex_command = Command("example","Example command for making a PR to the Tutla Asisstance bot, see the Github for more info.",example_callback,CLIENT,aliases=['command','ex'],params=["TEST PARAM"],isfree=True)
```

1. `from ..Module import *` will give you the Command Class and a few categories to start with. Change this line to your file structure
2. Next we come to the asynchronous function, you can name it anything but it must be updated in the Command declaration. This function must take 5 parameters.
3. Inside the command we can get the "member" variable off the command_data. You can use this to check if the member is a part of your server, similiarly of premium. Then finally we send a message with the description of the command and the first parameter.
4. Finally we will declare the command with it's name, description, function to execute it and category. Additionally we are also giving aliases to for easier remembrance and parameters (this does not give functionality, it only displays on the help menu) and finally we are making this command free allowing anyone to use it.

**NOTE:** Aliases are needed as they will trigger for every command if not applied, this is a bug and will be fixed next update.
**NOTE:** The category template can be declared in Module.py and you can pass ina  string for the category if not declaring in Module.py
