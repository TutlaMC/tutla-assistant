import re
from ..Module import *


async def ccs_callback(CommandObject,message,self,params,command_data): 
                formatted_message = message.content.replace('.ccs', '')

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

                current_fg_color = None  

                script = message.content.replace(".ccs","")

                patterns = {
                    r'\b(on|if|if_not|while|while_not|execute|execute_random|loop|loop_period|print|throw|exit|function|module|config|say|send|notify|playsound|input|define|gui_switch|wait|gui_swap|gui_quickmove|gui_drop|switch|swap|turn_to|snap_to|damage|drop|velocity|teleport)\b':
                        (31, 0),
                    r'(#\w+|:\w+)':
                        (32, 0),
                    r'\b(holding|off_holding|inventory_has|hotbar_has|target_block|target_entity|targeting_entity|targeting_block|input_active|block_in_range|entity_in_range|attack_progress|health|armor|pos_x|pos_y)\b':
                        (33, 0),
                    r'\b(true|false|null|module|create|reload|save|description|enable|disable|def|define|{|})\b':
                        (34, 0),
                    r'\b(1|2|3|4|5|6|7|8|9|0|{|})\b':
                        (35, 0)
                }

                for pattern, codes in patterns.items():
                    for code in codes:
                        script = re.sub(pattern, f'\033[{code}m\g<0>\033[0m', script)

                await message.channel.send("**NOTE:**ONLY WORKS ON COMPUTER\n```ansi\n"+script+"```")
ccs_command = Command("ccs", 'Format your CCS Script with color using ANSI Escape Codes!', ccs_callback, TOOLS, aliases=['ccs_format',"ccsify","clickcrystalsscript"])
 