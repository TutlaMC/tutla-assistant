from ..Module import * 
import random
import requests
from bs4 import BeautifulSoup
#from ..Utils import * #import this if you need utility commands
url = "https://thepleasantconversation.com/shower-thoughts/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

thoughts_list = []


for index, li_element in enumerate(soup.find_all('li')):
    text = li_element.get_text(strip=True)

    thoughts_list.append(text)

    if index == 542:
        break
async def showerthought_callback(CommandObject,message,self,params,command_data):
    await message.channel.send(random.choice(thoughts_list))
showerthought_command = Command("showerthought","Get a fun shower thought!",showerthought_callback,FUN,aliases=["shower","thought"],params=["Optional: USER PING"])