from ..Module import * 
import random
from bs4 import BeautifulSoup
import requests
async def rizz_callback(CommandObject,message,self,params,command_data):
    url = 'https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    rizz = [li.text for li in soup.find_all('li')]
    await message.channel.send(random.choice(rizz))
rizz_command = Command("rizz", 'Be the #1 Rizzler', rizz_callback, TOOLS, aliases=['getrizz'])