from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def example_callback(CommandObject,message,self,params,command_data):
                    is_member = command_data['member']
                    premium = command_data['premium']



                    await message.channle.send(CommandObject.description+f"\nWhat you said: {params[1]}")
calc_command = Command("example","Example command for making a PR to the Tutla Asisstance bot, see the Github for more info.",example_callback,CLIENT,aliases=["calculate",'command','ex'],params=["TEST PARAM"],isfree=True)