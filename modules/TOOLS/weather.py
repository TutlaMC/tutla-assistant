from ..Module import * 
from ..Utils import *
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['current_condition'][0]
    else:
        return None

async def weather_callback(CommandObject, message, self, params, command_data):
    city = params[1]
    weather = get_weather(city)
    if weather:
        await message.channel.send(
            f"Weather in {city}:\n"
            f"- Description: {weather['weatherDesc'][0]['value']}\n"
            f"- Temperature: {weather['temp_C']}°C\n"
            f"- Cloud Cover: {weather['cloudcover']}%\n"
            f"- Precipitation: {weather['precipMM']} mm\n"
            f"- Humidity: {weather['humidity']}%\n"
            f"- Wind Direction & Speed: {weather['windspeedKmph']} km/h {weather['winddir16Point']}"
        )
    else:
        await message.channel.send("Failed to retrieve weather data.")

weather_command = Command(
    "weather", 
    "Get weather data of a city", 
    weather_callback, 
    TOOLS, 
    aliases=["city"], 
    params=["CITY"]
)
