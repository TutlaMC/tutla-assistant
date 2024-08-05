from ..Module import * 
from ..Utils import *
async def regional_callback(CommandObject,message,self,params,command_data):
                    stuff = message_without_command(params)
                    newm = ''
                    variables_list = []

                    start_letter = ord('A')
                    end_letter = ord('Z')

                    for letter_code in range(start_letter, end_letter + 1):
                            letter = chr(letter_code)
                            variable_value = f':regional_indicator_{letter.lower()}:'
                            variables_list.append(variable_value)
                    for i in stuff:
                        
                        nletter = i.lower()
                        ascii_value = ord(nletter)

                        position = ascii_value - ord('a')
                        if i == ' ':
                                newm+='      '
                        try:
                            newm += variables_list[position]+" "
                        except Exception:
                            pass
                            

                    await message.channel.send(newm)




regional_command = Command("regional","REGIONAL TEXT",regional_callback,TOOLS,aliases=["toregional"],params=["TEXT"],isfree=True)