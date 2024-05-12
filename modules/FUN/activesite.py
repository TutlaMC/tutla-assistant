from ..Module import * 
#from ..Utils import * #import this if you need utility commands
async def activesite_callback(CommandObject,message,self,params,command_data):
    if params[1]:
        await message.channel.send(f'Most active site {params[1]} is on: || the p hub (100% real data) :skull: ||')
    else: 
        await message.channel.send(f'Most active site {message.author.mention} is on: || the p hub (100% real data) :skull: ||')
calc_command = Command("activesite","See the site your most active on, with 100% real data",activesite_callback,FUN,aliases=["site",'latestsite'],params=["Optional: USER PING"],isfree=True)