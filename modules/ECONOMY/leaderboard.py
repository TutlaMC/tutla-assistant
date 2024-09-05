from ..Module import * 
from assistantdata import db
async def leaderboard_callback(CommandObject,message,self,params,command_data):
    xpl = db.get_column_data("xp")
    coinsl = db.get_column_data("coins")
    sorted_xp = dict(sorted((item for item in xpl.items() if item[1] is not None), key=lambda item: item[1], reverse=True))
    sorted_coins = dict(sorted((item for item in coinsl.items() if item[1] is not None), key=lambda item: item[1], reverse=True))

    if len(params) >1:
        if params[1] == "coins":
            final = "COINS LEADERBOARD\n"
            ee = 0
            for i in sorted_coins:
                ee+=1
                final+=f"#{str(ee)} <@{str(i)}>: {sorted_coins[i]}\n"
            await message.channel.send(final,silent=True)
        elif params[1] == "xp":
            final = "XP LEADERBOARD\n"
            ee = 0
            for i in sorted_xp:
                ee+=1
                print(i)
                final+=f"#{str(ee)} <@{str(i)}>: {sorted_xp[i]}\n"
            await message.channel.send(final,silent=True)
        else: await message.channel.send(CommandObject.usage)
    else: await message.channel.send(CommandObject.usage)


    
leaderboard_command = Command("leaderboard", 'Tutla Leaderboard', leaderboard_callback, ECONOMY, aliases=['lb'],params=["coins|xp"])