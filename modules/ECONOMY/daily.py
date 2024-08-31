from ..Module import * 
from ..Utils import *
from assistantdata import db
from random import randint
async def daily_callback(CommandObject,message,self,params,command_data):
    last_daily = db.getData(message.author.id,"daily")
    now = datetime.now()
    
    format_str = '%Y-%m-%d %H:%M:%S'
    if last_daily == None: dt=datetime.now()
    passe = false
    try:
        dt = datetime.strptime(last_daily, format_str)
        passe = True
    except Exception: passe = False
    if passe == false: dt = datetime.strptime(last_daily, '%Y-%m-%d %H:%M:%S.%f')

    
        
    
    time_difference = now - dt
    
    seconds_diff = time_difference.total_seconds()
    if last_daily == None: seconds_diff = 100000
    if int(time_difference.total_seconds())<10: seconds_diff = 100000
    print(seconds_diff)
    if seconds_diff > 43200:
        nxp =20+randint(1,2000)
        nar = 1000+randint(1,2000)
        db.edit_user(message.author.id,aura= db.getData(message.author.id,"aura")+nar,xp= db.getData(message.author.id,"xp")+nxp,daily=now)
        await message.channel.send(f"Your daily:\nAura: {str(nar)}\nXP:{str(nxp)}\n")
    else: await message.channel.send(f"You have already claim your daily, you can claim again in {str(int(((43200-seconds_diff)/60)/60))} hours")
reload_command = Command("daily", 'Tutla Assistance daily', daily_callback, ECONOMY, aliases=['v'])