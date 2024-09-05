from ..Module import * 
import requests
import json
async def translate_callback(CommandObject,message,self,params,command_data):
    if len(params) > 3:
        text = ""
        for i in params[3:]:
            text+=i+" "
        print(text)
        lang = params[1]
        lang2 = params[2]

        if lang == "detect":
            e = requests.get(f"https://ftapi.pythonanywhere.com/translate?dl={lang2}&text={text}")
        else: 
            e = requests.get(f"https://ftapi.pythonanywhere.com/translate?sl={lang}&dl={lang2}&text={text}")

        await message.channel.send(f'`{lang}` to `{lang2}`: {str(e.json()["translations"]["possible-translations"][0])}\n-# Source Text: {text}')
    else: 
        await message.channel.send(CommandObject.usage)
translate_command = Command("translate", 'Translate one language from on to another', translate_callback, TOOLS, aliases=['transalate'],params=['CurrentLang|detect|auto',"ToConvertTo"])