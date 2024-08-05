from ..Module import * 
from ..Utils import *
async def ansi_callback(CommandObject,message,self,params,command_data):
                    formatted_message = message_without_command(params)

                    text_color_mapping = {
                        '30': 'gray',
                        '31': 'red',
                        '32': 'green',
                        '33': 'yellow',
                        '34': 'blue',
                        '35': 'pink',
                        '36': 'cyan',
                        '37': 'white'
                    }

                    background_color_mapping = {
                        '40': 'firefly-dark-blue',
                        '41': 'orange',
                        '42': 'marble-blue',
                        '43': 'greyish-turquoise',
                        '44': 'gray',
                        '45': 'indigo',
                        '46': 'light-gray',
                        '47': 'white'
                    }

                    current_fg_color = None  
                    current_bg_color = None 

                    for code, color in background_color_mapping.items():
                        formatted_message = formatted_message.replace(f'<bg-{color}>', f'\033[{code}m')
                        current_bg_color = code  


                    for code, color in text_color_mapping.items():
                        formatted_message = formatted_message.replace(f'<{color}>', f'\033[{code}m')
                        current_fg_color = code 
                        formatted_message = formatted_message.replace(f'</{color}>', f'\033[{current_fg_color}m')


                    formatted_message = formatted_message.replace('<bold>', '\033[1m') \
                                                        .replace('</bold>', '\033[0m') \
                                                        .replace('<underline>', '\033[4m') \
                                                        .replace('</underline>', '\033[0m') \
                                                        .replace('<highlight>', '\033[7m') \
                                                        .replace('</highlight>', '\033[0m')

                    await message.channel.send(f'```ansi\n{formatted_message}\033[0m```')
ansi_command = Command("ansiformat","Format text in color with ansi!",ansi_callback,TOOLS,aliases=["ansi","ansify"],params=["TEXT"],usage="""
I'm gay so I can't make an entire tutorial but here's a small explanation: [(text)[<color></color><highlight></highlight>|<bold></bold><underline></underline>]]  | Converts your text into cool ansi text: Usage (HTML like usage):
<red></red><green></green><blue></blue><yellow></yellow><pink></pink><cyan></cyan><gray></gray>
Background Colors: <firefly-dark-blue></firefly-dark-blue><orange></orange><marble-blue></marble-blue><greyish-turquoise></greyish-turquoise><gray></gray><indigo></indigo><light-gray></light-gray><white></white>
Other Formats: <bold></bold> <highlight></highlight) -> (for background)     <underline></underline>""")