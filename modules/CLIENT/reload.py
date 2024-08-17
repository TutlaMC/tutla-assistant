from ..Module import * 
from ..Utils import *
async def reload_callback(CommandObject,message,self,params,command_data):
    premium_reload()
    ban_reload()
reload_command = Command("reload", 'Refreshes Tutla Assitsance Data', reload_callback, CLIENT, aliases=['preload', 'load',"premiumload","premiumreload","banload","banreload"],ispremium=True)