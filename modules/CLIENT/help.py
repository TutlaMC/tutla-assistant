from ..Module import *
from ..Utils import version, getCmdCount
async def help_callback(CommandObject,message,self,params,command_data):
                        pages = []
                        req = "------------------------ REQUIREMENT ------------------------\nYou need to join the Tutla Discord (in bio) to use most of the commands"
                        nmessage = f'''```yml\n Hi I'm the Tutla Assistance {version} and can run the following {getCmdCount()} Commands: \n'''
                        
                        def append_page(content,new_line = False):
                            

                            if new_line: content+='\n' 
                            if len(pages) >0 :

                                page = pages[len(pages)-1]
                                if len(page)<= 1500:

                                    pages[len(pages)-1]+=content
                                else: 
                                    pages.append(content)

                            else: 
                                 pages.append(content)
                                 
                                 
                        for category, category_data in commands2.items():
                            display_message = category_data['display']
                            commandsv2 = category_data['commands']
                            append_page(display_message.upper())

                            for command_name, command_object in commandsv2.items():

                                append_page(command_object.toappend,new_line=True)
                        
                        words = message.content.split()
                        if len(params) > 1:
                             if params[1].isdigit():

                                try:

                                    nmessage+=pages[int(params[1])-1]

                                except Exception:
                                    await message.channel.send(f'No page found with number {int(params[1])-1}')

                                nmessage+=f'\n------------------------ PAGE {int(params[1])}/{len(pages)} ------------------------\n'
                                nmessage += req
                                nmessage += '```'

                                await message.channel.send(nmessage)
                             else: 
                                    cmd = get_command(params[1].replace('.',''))
                                    if cmd is not None:
                                        await message.channel.send(cmd.usage+f"\nCommand Usage: `{cmd.usage_format}`")
                                    else: 
                                          await message.channel.send(f'Command "{params[1]}" is not found!')
                                
                        else:

                            nmessage+=pages[0]
                            nmessage+=f'\n------------------------ PAGE 1/{len(pages)} ------------------------\n'
                            nmessage += req
                            nmessage += '```'
                            await message.channel.send(nmessage)

                               
help_command = Command("help","Opens up this menu",help_callback,CLIENT,aliases=['usage','what',"commands","command"],params=['PAGE NUMBER'],usage="The page number must always be an integer or you can enter a command to see it's usage.")