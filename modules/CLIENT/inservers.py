from ..Module import * 
async def inservers_callback(CommandObject,message,self,params,command_data):
     con = command_data['member']
     premium = command_data['premium']


     nmessage = 'In servers:\n```yaml\n'
     for i in self.guilds:
                    nmessage+='- '+i.name+'\n'
     nmessage+='```'
     await message.channel.send(nmessage)
inservers_command = Command("inservers", 'Lists all servers user is in', inservers_callback, CLIENT, aliases=['ls', 'servers'],isfree=True)