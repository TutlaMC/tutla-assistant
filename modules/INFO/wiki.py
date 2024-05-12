from ..Module import * 
import wikipedia
#from ..Utils import * #import this if you need utility commands
async def wiki_callback(CommandObject,message,self,params,command_data):
                    try: await message.channel.send(wikipedia.summary(message.content.replace('.wiki ',''),2))
                    except Exception as e:
                        await message.channel.send("Error in object: \n```python\n"+str(e)+'```')

wiki_command = Command("wiki","Look something off wikipedia.",wiki_callback,INFO,aliases=["wikipedia",'what','whatis'],params=["WIKIPEDIA PROMPT"])