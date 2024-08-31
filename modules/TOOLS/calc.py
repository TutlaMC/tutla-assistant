from ..Module import *
from ..Utils import * 
from math import *
x = 1 # improper cannot complain now
y=1
async def calc_callback(CommandObject,message,self,params,command_data):
                    con = command_data['member']
                    premium = command_data['premium']



                    values_to_calc = message_without_command(params)
                    values_to_calc = values_to_calc.replace(' ','')
                    try:
                        await message.channel.send('Answer: `'+str(eval(values_to_calc))+'`')
                    except Exception as e:
                        await message.channel.send('Invalid Numbers')
                    if not con : free_access = True
calc_command = Command("calc","Calculate what you want",calc_callback,TOOLS,aliases=["calculate",'math','int'],params=["NUMBER OR PYTHON MATH FUNCTION"])