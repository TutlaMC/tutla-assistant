from ..Module import *
import random
#from ..Utils import * #import this if you need utility commands
suffixes = ['s','a','i','o',"ly","er","es","ant","ance","ve","ary","tion","ation","ed","ing","dom","er","ful","ous","ship","wards","al","ate","ion","y","acy"]
def ransuffix():
      return random.choice(suffixes)
async def joshify_callback(CommandObject,message,self,params,command_data):
                    input = message.content.replace(".joshify","")
                    words = input.split(' ')
                    transformed_words = []
                    for word in words:
                        random_number = random.random()
                        transformed_word = ''
                        if True:
                            if word.endswith('ed'):
                                transformed_word = word[:-2] + 'ing'
                            elif word.endswith('ing'):
                                transformed_word = word[:-3] + 'ed'
                            elif word.endswith('s'):
                                if random.random() > 0.7:
                                      transformed_word = word[:-1]
                                else:
                                    transformed_word = word+ransuffix()
                            elif word.lower() in ['the',"an","is","and"]:
                                  transformed_word = "a"
                            
                            elif word.endswith('ly'):
                                transformed_word = word[:-2] + ransuffix()
                            elif word.lower() in ["at","on","the","that","these","those"]:
                                transformed_word = "in"
                            elif word.lower() in ["you","who","whom","me"]: 
                                  transformed_word = "your"
                            elif word.lower() in ["i","us"]:
                                  transformed_word = "me"
                            elif word.lower() in ["he","she","it","her","him","it's","his"]:
                                  transformed_word = "its"
                            elif word.lower().replace("'","") in ["didnt","no","not","aint"]:
                                  transformed_word = "didn't"
                            elif "," in word:
                                  transformed_word = word.replace(",",".")
                            elif word.lower() == "an":
                                  transformed_word = "a"
                            elif word.lower() in ["in","that","these","those","is",'a']:
                                  transformed_word = "it"
                            elif word.lower() in ["will","do","make","want","to"]:
                                  transformed_word = "shall"
                            elif word.lower().replace("'","") in ["your","youre","yours"]:
                                  transformed_word = "you"
                            elif any(word.lower().endswith(suffix) for suffix in suffixes) and len(word) > 4:
                                for suffix in ["ly","er","es","ant","ance","ary","tion","ation","ed","ing","dom","er","ful","ous","ship","wards","al","ate","acy"]:
                                    if word.lower().endswith(suffix):
                                        word = word.replace(suffix,"")
                                        transformed_word = word+ ransuffix()
                            else:
                                if random.random() > 0.9:
                                      transformed_word = ''.join(char for char in word if char.lower() not in 'iou' and len(word)>3)
                                elif random.random() < 0.1: 
                                      transformed_word+=word+random.choice([",","."," a","!"])
                                else: transformed_word = word
                                
                        transformed_words.append(transformed_word)
                    transformed_sentence = ' '.join(transformed_words)
                    await message.channel.send(transformed_sentence)
joshify_command = Command("joshify","Joshify text, also known as the latest geenration of grammar",joshify_callback,FUN,aliases=["grammar","grammarly"],isfree=True)