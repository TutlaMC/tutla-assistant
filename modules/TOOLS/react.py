from ..Module import * 
import random
from unicodedata import lookup
async def react_callback(CommandObject,message,self,params,command_data):
                        result = []
                        inside_quotes = False
                        ae = message.content.replace('.react ','')
                        ae = ae.replace(' ','')
                        ae = ae.replace('"','')
                        ae = ae.replace("'",'')

                        for char in ae.lower():
                            result.append(char)
                        variables_list = []

                        start_letter = ord('A')
                        end_letter = ord('Z')

                        for letter_code in range(start_letter, end_letter + 1):
                            letter = chr(letter_code)
                            variable_value = f'{letter.lower()}'
                            variables_list.append(variable_value)
                        if message.reference:
                            nm1 = message.reference.message_id
                            nm = await message.channel.fetch_message(nm1)

                            for i in result:
                                ascii_value = ord(i)
                                

                                position = ascii_value - ord('a')

                                if variables_list[position]:
                                    await nm.add_reaction(lookup("REGIONAL INDICATOR SYMBOL LETTER %s" % variables_list[position]))
async def reacto_callback(CommandObject,message,self,params,command_data):
                        words = message.content.split()
                        if len(words) > 3:
                            thechannel = await self.fetch_channel(int(words[1]))

                            themsg = await thechannel.fetch_message(int(words[2]))
                            ae = message.content.replace('.reacto ','')
                            
                            ae = ae.replace('"','')
                            ae = ae.replace("'",'')
                            ae = ae.replace(words[1],'')
                            ae = ae.replace(words[2],'')
                            ae = ae.replace(' ','')

                            result = []
                            inside_quotes = False
                            

                            for char in ae.lower():
                                result.append(char)
                            variables_list = []

                            start_letter = ord('A')
                            end_letter = ord('Z')

                            for letter_code in range(start_letter, end_letter + 1):
                                letter = chr(letter_code)
                                variable_value = f'{letter.lower()}'
                                variables_list.append(variable_value)


                            for i in result:
                                    ascii_value = ord(i)

                                    position = ascii_value - ord('a')

                                    
                                    await themsg.add_reaction(lookup("REGIONAL INDICATOR SYMBOL LETTER %s" % variables_list[position]))

                                
                        else: await message.channel.send('Incorrect usage, message needs [channelID] & [messageID]\nCorrect Usage:```.reacto [channelID] [messageID] [content]')
async def reactemoji(CommandObject,message,self,params,command_data):
        
                        result = []
                        inside_quotes = False
                        ae = message.content.replace('.reactemoji ','')
                        ae = ae.replace(' ','')
                        ae = ae.replace('"','')
                        ae = ae.replace("'",'')

                        for char in ae.lower():
                            result.append(char)

                        nm1 = message.reference.message_id
                        nm = await message.channel.fetch_message(nm1)

                        for i in result:
                                    await nm.add_reaction(i)
async def reactemojito(CommandObject,message,self,params,command_data): 
                        words = message.content.split()
                        if len(words) > 3:
                            thechannel = await self.fetch_channel(int(words[1]))
                            themsg = await thechannel.fetch_message(int(words[2]))
                            ae = message.content.replace('.reactemojito ','')
                            
                            ae = ae.replace('"','')
                            ae = ae.replace("'",'')
                            ae = ae.replace(words[1],'')
                            ae = ae.replace(words[2],'')
                            ae = ae.replace(' ','')

                            result = []
                            inside_quotes = False
                            
                            print(ae)
                            
                            for char in ae.lower():
                                result.append(char)
                            print(result)
                            for i in result:
                                
                                    await themsg.add_reaction(i)

                                
                        else: await message.channel.send('Incorrect usage, message needs [channelID] & [messageID]\nCorrect Usage:```.reacto [channelID] [messageID] [emoji]```')

react_command = Command("react", 'React on a message with ease via replying', react_callback, TOOLS, aliases=['visualsay'],params=["TEXT"])
reacto_command = Command("reacto", 'React to a message which you cannot reply to', reacto_callback, TOOLS, aliases=['reactto'],params=[ "channelID", "messageID" ,"TEXT"])
reactemoji_command = Command("reactemoji", 'React with emojis', reactemoji, TOOLS, aliases=['reactmoji'],params=["EMOJI"])
reactemojito_command = Command("reactemojito",'React with emoji on a message you cannot reply to',reactemojito,TOOLS,aliases=['reactmojito'],params=[ "channelID", "messageID" ,"emoji"])