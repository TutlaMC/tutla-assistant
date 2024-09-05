from ..Module import * 
from ..Utils import *
def number_to_emoji(number):
    num_str = str(number)
    emoji_map = {
        '0': '0️⃣',
        '1': '1️⃣',
        '2': '2️⃣',
        '3': '3️⃣',
        '4': '4️⃣',
        '5': '5️⃣',
        '6': '6️⃣',
        '7': '7️⃣',
        '8': '8️⃣',
        '9': '9️⃣'
    }
    return ''.join(emoji_map[digit] for digit in num_str)
async def poll_callback(CommandObject,message,self,params,command_data):
    e = message_without_command(params).split(',')
    question = e[0]
    if len(e) <= 6:
        final = f"## Poll 📊\n**Question: {question}**\n"
        count = 0
        for i in e[1:]:
            count+=1
            final+=f"#{str(count)}: {i}\n"
        msg = await message.channel.send(final)
        for i in range(count):
            
            await msg.add_reaction(number_to_emoji(i+1))
    else: await message.channel.send("Too many options (Max 6)")

poll_command = Command("poll", 'Ultimate pollization. Choose between poll users and number.', poll_callback, TOOLS, aliases=['rand'],params=["number/user","if word 1 is number: NUMBER","optional: -mention"])