from ..Module import * 
import random
phrases = ["bazinga!🤣 this video sure did tickle my funny bone!😂🦴 i absolutely need to show this to my book club!😅📚 #wap🍷",
"That's not the assignment young man 📏💥🧓🏽 I better not catch you off task in my messages again ❌✏️📜🙏🏼 or else task wont be the only thing taken off today 😱🙏🏼🙅🏼‍♂️🙅🏼‍♂️",
"Careful with whatchu say 🙏🗣️🗣️🙏 the COCK is watching 🤞🤞🐔🐔 and he ain’t take NO prisoners 🙅‍♂️🙅‍♂️🤫🤫 keep them cheeks TIGHT",
"Bettah zip up yo keyboard like you zip up those pants before i 💦 and swing my 🔮 🔮 across yo 🤓 like a grandfather clock 🕰️ 🙏 🙏",
"Better watch yo mouth👨🏿‍🦲🤞🏻🙊 RANDY is listening in my comments section 👁️‍🗨️🙀👂🏿 and he won't just be taking your candy if he catches you again ❌🍬🍭",
"You old ragged little stocking 🙏 🧦 dont ever let my Rudolph detect you with his nose 🔴 or coals wont be the only thing inside of you this christmas 🔥 🗣️ 🎅 🐠",
"Nice try you scrawny octopus 🐙 🌊 but next time you dive near me 🪸 I'll make sure the tip will be all over you 💦 🐡 🍆",
"Nevah let me catch you commenting again lil bro 🙏 🙏 you have interupted my edging sesson and now you will pay 😏 💀 🔥",
"Spanksgiving👋🏻🦃🌽 is right around the corner you dirty slut😈😏😛 R u a sexy lil pilgrim?😈🎩🏃 or a naked native¿¿👹😵 GOBBLE🦃GOBBLE🦃🅱️ITCH🐕!!! It's 🦡SKANKS-GIVING😜!!!",
"vorp vorp shawty   p s    c  s  cju 👽 🙏🏻",
"I noticed that you used “😭” in your comment. Just wanted to say, don’t give up anything in your life. I don’t know what you’re going through but I’m always here to help.",
"are 🤨 you 👁️👄👁️are 🤨 you 👁️👄👁️coming 🚶🏾‍♀️to ✌🏾 the 💖💅 tree ✨🌲✨🌳",
    "𝔁𝓾𝓮🥶𝓱𝓾𝓪🧚‍♀️𝓹𝓲𝓪𝓸😻𝓹𝓲𝓪𝓸🗿𝓫𝓮𝓲👺𝓯𝓮𝓷𝓰🤩𝔁𝓲𝓪𝓸😼𝔁𝓲𝓪𝓸",
    "𝓻𝓮𝓶𝓮𝓶𝓫𝓮𝓻 🤔𝓽𝓱𝓮 ✨𝓽𝓲𝓶𝓮𝓼⌛️𝔀𝓮🤞🏾𝓱𝓪𝓭😪𝓽𝓱𝓮 😭 𝓽𝓲𝓶𝓮𝓼 ⏰ 𝓽𝓱𝓪𝓽🤥𝔂𝓸𝓾 👧 𝓪𝓷𝓭😴𝓶𝓮👦 𝓱𝓪𝓭😰",
    "Martha😁was🥰an🙃average🐕dog. She went💨aërf🍒&🤕ærph😪&👻EEEER🤠when👧🏻she👄ate🤏🏻some🤖alphabet👽soup,🐶then🧦what🌸happened🌚was🌈bizarre🧽",
    "R-R-R-Roll💿up⬆️to2️⃣the🤩party🥳with🧶my🧚🏽‍♀️crazy🤪pink💝wig💇‍♀️",
    "Anyway, here’s the recipe for brownies: 1/2cup butter, 2eggs, 1cup sugar, 1/3cup cocoa powder, 2teaspoon vanilla extract, 1/2cup flour",
    "ᵇᵒⁱ🐿️ʷʰᵃᵗ🐿️ᵗʰᵉ🐿️ʰᵉˡˡ🐿️ᵇᵒⁱ🐿️",
    "🦧ʙᴏɪ🦧ɪғ🦧ʏᴏᴜ🦧ᴅᴏɴᴛ🦧ɢᴇᴛ🦧ʏᴏᴜʀ🦧sǫᴜɪɢɢʟʏ🦧ᴅɪɢɢʟʏ🦧ʜᴇᴀᴅ🦧",
    "You don’t have this emoji😅⃤",
    "Careful with whatchu say 🙏🗣️🗣️🙏 the COCK is watching 🤞🤞🐔🐔 and he ain’t take NO prisoners 🙅‍♂️🙅‍♂️🤫🤫 keep them cheeks TIGHT",
    "Hey pal!👋👋, listen friendo, when I saw your message, I immediately started violently touching myself, hope I can touch you next. Over and out!😳",
    "I noticed that you used “😭” in your comment. Just wanted to say, don’t give up anything in your life. I don’t know what you’re going through but I’m always here to help."]
async def antinpc_callback(CommandObject,message,self,params,command_data):
    await message.channel.send(random.choice(phrases))
    
antinpc_command = Command("antinpc","Deal wth NPCs Pro Max Viral TZ7008X Edition (2nd Ever command btw)",antinpc_callback,FUN,aliases=["npc"])