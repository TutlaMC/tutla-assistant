from ..Module import *
import random
#from ..Utils import * #import this if you need utility commands
async def joshify_callback(CommandObject,message,self,params,command_data):
                    input = message.content.replace(".joshify","")
                    words = input.split(' ')
                    transformed_words = []
                    for word in words:
                        random_number = random.random()
                        transformed_word = ''
                        if random_number < 0.7:
                            if word.endswith('ed'):
                                transformed_word = word[:-2] + 'ing'
                            elif word.endswith('ing'):
                                transformed_word = word[:-3] + 'ed'
                            elif word.endswith('s'):
                                transformed_word = word[:-1]
                            else:
                                transformed_word = word + 's'
                        else:
                            if word.endswith('ly'):
                                transformed_word = word[:-2] + 'y'
                            else:
                                transformed_word = ''.join(char for char in word if char.lower() not in 'iou')
                        transformed_words.append(transformed_word)
                    transformed_sentence = ' '.join(transformed_words)
                    await message.channel.send(transformed_sentence)
joshify_command = Command("joshify","Joshify text, also known as the latest geenration of grammar",joshify_callback,FUN,aliases=["grammar","grammarly"],isfree=True)