from ..Module import * 
import random
async def ball_callback(CommandObject,message,self,params,command_data):
                    if len(params) >= 2:
                        await message.channel.send(random.choice(["No 100%",
                                                                "Yes bruh",
                                                                "Roll **harder**",
                                                                "wtf",
                                                                "Obviously",
                                                                "none of the above",
                                                                "provide mroe context",
                                                                "sounds like smth ur gramma would say",
                                                                'no talk ez yas',
                                                                'nah','no dude',
                                                                'yas :thumbsup:',
                                                                ":thumbsdown:",
                                                                "*yeets balls over face*",
                                                                "prolly nah",
                                                                "you forgot to press my *buttons*",
                                                                "yes if there's e innit",
                                                                "ain cool, so no",
                                                                "if mexican yes",
                                                                "kys ||keep yourself safe :thumbsup:||",
                                                                f".activesite {message.author.mention}",
                                                                "that's gaytdom",
                                                                "the one that supports gaytdom",                                                              "If taco man yes",
                                                                "sounds like autism ",
                                                                "option 1",
                                                                "whatever your gut says",
                                                                "all mine",
                                                                "ain sigma",
                                                                "ouf",
                                                                "# 🇬🇦🇾🇹🇩🇴🇲",
                                                                "[idc](https://media.discordapp.net/stickers/1193539237153357885.png?size=160&name=idc)",
                                                                "[measf](https://media.discordapp.net/stickers/1201906160622637157.png?size=160&name=measf)",
                                                                "[mate](https://media.discordapp.net/stickers/1256231390576381952.gif?size=160&name=mate)",
                                                                "[notsupport](https://media.discordapp.net/stickers/1192829101547991220.png?size=160&name=notsupport)"])+f"\n-# Prompt: {message.content}")
                    else: await message.channel.send("Invalid Argument for `.8ball`")                   
ball_command = Command("8ball","Ultimate Decision Making Solution",ball_callback,TOOLS,aliases=["decide"],params=["STATEMENT"],isfree=True)