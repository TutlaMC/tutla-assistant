from ..Module import * 
from ..Utils import *
async def list_callback(CommandObject,message,self,params,command_data):
    if len(params) >= 2:
        if params[1] == "mods":
            nmessage = 'Mods:\n```yaml\n'
            for i in mod.mods:
                            nmessage+=f'- {i.name}: {i.description}\n'
            nmessage+='```'
            await message.channel.send(nmessage)
        elif params[1] == "premium":
            if len(params) < 3: 
                   await message.channel.send("Check `.list premium commands` or `.list premium users`, please see `.usage list`")
                   return False
            if params[2] == "users":
                premium_reload()
                nmessage = "__Premium Users__\n"
                for i in premium_list:nmessage += f"- <@{str(i)}>\n"
                print(premium_list)
                await message.channel.send(nmessage,silent=true)
            elif params[2] in ["cmds","commands","modules"]:
                final = ""
                for category, category_data in commands2.items():                    
                        for command_name, command_object in category_data['commands'].items():
                                if command_object.ispremium: final+=f"{command_object.name}: {command_object.description}\n"
                await message.channel.send(f"```yaml\nPremium Commands:\n{final}```")
            else: 
                await message.channel.send("Check `.list premium commands` or `.list premium users`, please see `.usage list`")

        elif params[1] in ["servers","inservers"]:
                nmessage = 'In servers:\n```yaml\n'
                for i in self.guilds:
                            nmessage+='- '+i.name+'\n'
                nmessage+='```'
                await message.channel.send(nmessage)
        else: await message.channel.send(CommandObject.usage)
    else: await message.channel.send(CommandObject.usage)
list_command = Command("list", 'Lists specific features on Tutla Assistance', list_callback, CLIENT, aliases=['inservers', 'mods,"ls',"lm","lpc","servers"],usage="""List: [premium|mods|servers/inservers]\nPremium: [users|modules/cmd/commands]""")