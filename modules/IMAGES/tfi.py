from ..Module import * 
from ..Utils import * 
from io import BytesIO
import requests
from collections import defaultdict
async def textfimage_callback(CommandObject,message,self,params,command_data):
    
    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    image_data = await message.attachments[0].read()
    image_file_like = BytesIO(image_data)
    files = {'image': ('image.png', image_file_like, 'image/png')}
    r = requests.post(api_url, files=files)
    data = r.json()





    def get_tens(value):
        return value // 10 * 10

    grouped = defaultdict(list)

    for item in data:
        y1 = item['bounding_box']['y1']
        text = item['text']
        tens = get_tens(y1)
        grouped[tens].append(text)

    e = dict(sorted(grouped.items()))
    
    final = ""
    print(e)
    for y, texts in e.items():
        for text in texts:
            final+=text+" "
            print(y,text)
        final +="\n"
    await message.channel.send(final)
         
textfimage_command = Command("tfi","Exctracts text from an image",textfimage_callback,IMAGES,aliases=['textfromimage',"extracttext","extractext","getext","gettext"])