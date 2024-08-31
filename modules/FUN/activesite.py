from ..Module import * 
from ..Utils import * 
async def activesite_callback(CommandObject,message,self,params,command_data):
    
    
    if len(params) == 2:
        if str(message.mentions[0].id) not in premium_list:
            await message.channel.send(f'Most active site {params[1]} is on: || the p hub (100% real data) :skull: ||')
        else: 
            await message.channel.send(f'Most active site {params[1]} is on: || x.com (good boi) ||')
    else: 
        if str(message.author.id) not in premium_list:
            await message.channel.send(f'Most active site {message.author.mention} is on: || the p hub (100% real data) :skull: ||')
        else: 
            await message.channel.send(f'Most active site {message.author.mention} is on: || x.com (good boi)||')
calc_command = Command("activesite","See the site your most active on, with 100% real data",activesite_callback,FUN,aliases=["site",'latestsite'],params=["Optional: USER PING"])