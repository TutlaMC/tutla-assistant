from ..Module import * 
from ..Utils import * 
import requests
from bs4 import BeautifulSoup

#from ..Utils import * #import this if you need utility commands
async def tutla_callback(CommandObject,message,self,params,command_data):
    main = message_without_command(params)
    r = requests.get(f"https://tutla.net/?s={main.replace(' ','+')}")
    soup = BeautifulSoup(r.content, 'html.parser')
    results = []
    target_class = "columns-3 wp-block-post-template is-layout-grid wp-container-core-post-template-is-layout-1 wp-block-post-template-is-layout-grid"
    e = soup.find('ul', class_=target_class)

    if e:
        for li in e.find_all('li'):
            div_inside_li = li.find('div')
            if div_inside_li:
                h2_element = div_inside_li.find('h2', class_='wp-block-post-title has-medium-font-size')
                if h2_element:
                    a_element = h2_element.find('a')
                    if a_element:
                        a_text = a_element.get_text(strip=True)
                        a_href = a_element['href']
                        results.append([a_text, a_href])

    final = f'### __Search Results for "{main}":__\n'
    for i in results:
        weeb = i[0].replace("']","").replace("['","")
        final+=f"- {weeb}: <{i[1]}>\n"
    await message.channel.send(final)
tutla_command = Command("tsearch","Search the tutla website",tutla_callback,TUTLA,aliases=["tutlasearch"])