from ..Module import * 
from ..Utils import *
from assistantdata import db
import sys
from collections import deque


class PrintLogger:
    def __init__(self, logfile, max_logs=50):
        self.logfile = logfile
        self.log_queue = deque(maxlen=max_logs)
        self._original_stdout = sys.stdout
        sys.stdout = self

    def write(self, message):
        if message.strip():
            lines = message.splitlines()
            for line in lines:
                self.log_queue.append(line + "\n")
        self._original_stdout.write(message)

    def flush(self):
        pass

    def save_to_file(self):
        with open(self.logfile, 'w') as f:
            f.writelines(self.log_queue)

logger = PrintLogger('log.log')




        
async def console_callback(CommandObject,message,self,params,command_data):
    if getAdminLevel(message.author.id) > 0:
        if params[1] == "log" and getAdminLevel(message.author.id) ==4:
            logger.save_to_file()
            with open("log.log", "r") as f:
                await message.channel.send(f"```python\n{f.read()}```")
        elif params[1] == "shell" and getAdminLevel(message.author.id) ==4:
            execution = message_without_command(params).replace("shell ","")
            await message.channel.send(f"```python\nTutla Shell >{execution}\n{execute(execution)}```")
        elif params[1] == "premium" and getAdminLevel(message.author.id) >=2:
            if params[2] == "add":
                db.edit_user(message.mentions[0].id,premium=True)
                premium_reload()
                await message.channel.send(f"Gave {message.mentions[0].mention} premium!")
            elif params[2] == "remove":
                db.edit_user(message.mentions[0].id,premium=False)
                premium_reload()
                await message.channel.send(f"Revoked premium off {message.mentions[0].mention}!")
        elif params[1] == "ban" and getAdminLevel(message.author.id) >=3:
            if params[2] == "add":
                db.edit_user(message.mentions[0].id,banned=True)
                ban_reload()
                await message.channel.send(f"Banned {message.mentions[0].mention}")
            elif params[2] == "remove":
                db.edit_user(message.mentions[0].id,banned=False)
                ban_reload()
                await message.channel.send(f"Unbanned {message.mentions[0].mention}!")
        elif params[1] == "db" and getAdminLevel(message.author.id) > 3:
            if params[2] == "edit":
                if params[4] == "xp":
                    db.edit_user(int(params[3]),xp=int(params[5]))
                elif params[4] == "aura":
                    db.edit_user(int(params[3]),aura=int(params[5]))
                elif params[4] == "premium":
                    db.edit_user(int(params[3]),premium=bool(params[5]))
                elif params[4] == "last_command":
                    db.edit_user(int(params[3]),premium=params[5])
                elif params[4] == "coins": db.edit_user(int(params[3]),coins=int(params[5]))
                



    
console_command = Command("console", 'Tutla Assistance Control Panel', console_callback, CLIENT, aliases=['cpanel', 'panel'])
