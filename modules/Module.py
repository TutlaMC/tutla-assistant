commands2={

}
TOOLS = "Utilities/Tools"
INFO = "Info"
AI = "AI"
ADMIN = "ADMIN"
FUN = "Fun"
CLIENT = "Client"
TUTLA_ADMIN = "TUTLA ADMIN"




def section_add(name,command):
    global commands2
    section_name = "------- "+name+" --------\n"
    
    if name in commands2:
        print("yes")
        
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
    def __init__(self,name,description, method,category,aliases=[], params=[],isadmin =False,isfree=False,ispremium=False,usage=None):
        self.name = name
        self.description = description
        self.method = method
        self.isfree=isfree
        self.category = category
        self.ispremium = ispremium
        self.aliases=aliases
        self.params = []
        for param in params:
            self.params.append(f"[{param}]")

        self.aliases.append(self.name)
        self.toappend = name+' '
        for i in self.params:
                self.toappend+= ' ['+i+'] '
        if self.isfree:
                self.toappend+= '| (FREE COMMAND)'
        elif self.ispremium: self.toappend+= '| (PREMIUM ONLY)'
        else: self.toappend+= '| (SERVER MEMBER ONLY)'
        self.toappend+= ' | '+self.description
        
        self.usage_format = f".{self.name} {' '.join(param for param in self.params)}"
        if usage == None: 
            usage = "The Usage has not been specified, so this is the usage built by the system:\n"
            usage+="This Command "+self.description.lower()+"\n"
            usage+=f".{self.name} {' '.join(param for param in self.params)}\n"
            usage += f"Aliases:\n{chr(10).join(self.aliases)}"
        self.usage = usage

            

        
        section_add(category,self)
        

        
    async def run(self,message,discord_client,params,command_data):

        await self.method(self,message,discord_client,params,command_data)



