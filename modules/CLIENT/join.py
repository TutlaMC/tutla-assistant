from ..Module import * 
async def join_callback(CommandObject,message,self,params,command_data):
                        invite = message.content.replace('.join ','')

                        await self.accept_invite(invite)
                        await message.channel.send("Joined guild")

     
join_command = Command("join", 'Join a discord server', join_callback, CLIENT, aliases=['js'],params=["server invite"],ispremium=True)