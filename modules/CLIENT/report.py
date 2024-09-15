from ..Module import * 
from ..Utils import * 
import random
async def report_callback(CommandObject,message,self,params,command_data):
    bug = message_without_command(params)
    reporto = await self.fetch_channel(1281180657233428481)
    id = random.randint(10000,99999)
    await message.channel.send(":warning: Spamming Bug/False Reports will result in a Tutla Assistance Ban!:warning:")
    await reporto.send(f"Bug #{str(id)}:\n```yaml\n{bug}```\nReported By {message.author.mention}")
    await message.channel.send(f"Reported Bug ID: {str(id)}\n```yaml\n{bug}```")
async def bugs_callback(CommandObject,message,self,params,command_data):
    reporto = await self.fetch_channel(1281180657233428481)
    final = "Bugs:\n"
    async for bug in reporto.history(limit=200):
        final+=f"- {bug.content}\n"

    await message.channel.send(final,silent=True)
report_command = Command("report","Report a bug on Tutla Assistance",report_callback,CLIENT,aliases=['bug'])
bugs_command = Command("bugs","Lists all the Tutla Assistance bugs",bugs_callback,CLIENT,aliases=['reports'])