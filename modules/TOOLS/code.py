from ..Module import * 
from ..Utils import *
from assistantdata import db
import random as ran
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
async def code_callback(CommandObject,message,self,params,command_data):
    if paramExists(params, 2):
        if params[1] == "length":
            await message.channel.send(errors[0].replace('[E]',params[2]))
        elif params[1] == "nil":
            await message.channel.send(errors[1].replace('[E]',params[2]))
        elif params[1] in ["java",'null','not','invoke']:
            await message.channel.send(errors[2].replace('[E]',params[2]))
        elif params[1] == "stfu":
            await message.channel.send(errors[3].replace('[E]',params[2]))
        elif params[1] in ["sigma","aura"]:
            await message.channel.send(errors[4].replace('[E]',params[2]))
        elif params[1] in ["roast","retard","retarded","idiot"]:
            await message.channel.send(errors[5].replace('[E]',params[2]))
    else: await message.channel.send(CommandObject.usage)
code_command = Command("code", "Learn programming in a fun and easy way!", code_callback, TOOLS, aliases=["program"],params=["Sample:length|nil|java/null/not/invoke|stfu|sigma/aura|roast/retard/retarded/idiot","Object"])