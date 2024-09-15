from modules.Utils import MainLogger
commands2={

}
cmd_count = 0
TOOLS = "Utilities/Tools"
INFO = "Info"
AI = "AI"
ADMIN = "ADMIN"
FUN = "Fun"
CLIENT = "Client"
TUTLA_ADMIN = "TUTLA ADMIN"
IMAGES = "IMAGES"
ECONOMY = "Economy"
TUTLA = "Tutla"

def section_add(name,command):
    global commands2
    name = name.upper()
    section_name = "------- "+name+" --------\n"
    
    if name in commands2:        
        commands2[name]['commands'].update({command.name:command})
    else:

        commands2[name]={
             "display":section_name,
             "commands":{command.name:command}
        }

def get_command(command):
    final = False
    for category, category_data in commands2.items():
                            display_message = category_data['display']
                            commandsv2 = category_data['commands']
                            for command_name, command_object in commandsv2.items():

                                if command in command_object.aliases:
                                      final = True
                                      return command_object
    if not final: return None
class Command:
    def __init__(self,name,description, method,category,aliases=[], params=[],isadmin =False,ispremium=False,usage=None):
        global cmd_count
        self.name = name
        self.description = description
        self.method = method
        self.category = category
        self.ispremium = ispremium
        self.aliases=aliases
        self.params = []
        for param in params:
            self.params.append(f"[{param}]")

        self.aliases.append(self.name)
        self.toappend = name+' '
        for i in self.params:
                self.toappend+= i.upper()
        if self.ispremium: self.toappend+= '| (PREMIUM ONLY)'
        self.toappend+= ' | '+self.description
        
        self.usage_format = f".{self.name} {' '.join(param for param in self.params)}"
        if usage == None: 
            usage = "**The Usage has not been specified, so this is the usage built by the system:\n"
            usage+="This Command "+self.description.lower()+"**\n"
        self.usage = usage+f"\n.{self.name} {' '.join(param for param in self.params)}\n"+ f"Aliases:\n{chr(10).join(self.aliases)}"

            

        
        section_add(category,self)
        cmd_count +=1
        

        
    async def run(self,message,discord_client,params,command_data):
        MainLogger.log(f"Executing Command {params[0]}")
        await self.method(self,message,discord_client,params,command_data)



