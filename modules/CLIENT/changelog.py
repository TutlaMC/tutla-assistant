from ..Module import * 
from ..Utils import message_without_command
import requests

url = "https://raw.githubusercontent.com/TutlaMC/tutla-assistant/main/changelog.md"
response = requests.get(url)
changelog = response.text

async def changelog_callback(CommandObject,message,self,params,command_data):
    await message.channel.send(changelog)
changelog_command = Command("changelog", 'Outputs the changelog', changelog_callback, CLIENT, aliases=['log'])