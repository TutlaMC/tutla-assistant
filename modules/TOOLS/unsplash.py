from ..Module import *
from ..Utils import *
import requests
from bs4 import BeautifulSoup

async def unsplash_callback(CommandObject, message, self, params, command_data):
    if params[1].isdigit():
        count = int(params[1])
        unsplash_query = message_without_command(params[1:])
    else: 
        count = 1
        unsplash_query = message_without_command(params)
    
    url = f"https://unsplash.com/s/photos/{unsplash_query.replace(' ', '-')}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.findAll('img', {'class': 'I7OuT'})
        c2 = 0
        for img_tag in img_tags:
            c2+=1
            if c2==count+1: break
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                await message.channel.send(image_url)
        if len(img_tags) < 2:
            await message.channel.send("No image found.")
    else:
        await message.channel.send(f"Failed to fetch results. Status code: {response.status_code}")

unsplash_command = Command("unsplash", "Searches for an image from Unsplash and sends the first result.", unsplash_callback, TOOLS, aliases=['unsplashimage', 'img'], params=["SEARCH_QUERY"], ispremium=True)
