# Utils
import base64
import socket
from mods import mod
from assistantdata import db
from datetime import datetime
import sqlite3
import asyncio
import os
from aiohttp import ClientSession, ClientError

premium_list = []
banlist=[]
afk_users = {}
fonts= []

# SETTINGS
version = 'V1.5.5'
dev_mode = True
self_bot = False

logging_channel = 1281476804909203529


true = True
false = False

for i in os.listdir('assistantdata/fonts'):
       fonts.append(i.replace('.ttf',''))

def getCmdCount():
    from modules.Module import cmd_count
    return cmd_count

class Logger:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def __init__(self,name,subexecution=None):
        self.name = f"[{name.upper()}]"
        self.seb = subexecution
    def log(self, text, style="normal"):
        if style == "warning":
            prefix = Logger.WARNING+"WARNING "+self.name+Logger.END
        elif style == "error":
            prefix = Logger.FAIL+"FAIL "+self.name+Logger.END
        elif style == "success":
            prefix = Logger.OKGREEN+"SUCCESS "+self.name+Logger.END
        elif style == "fatal":
            prefix = Logger.FAIL+Logger.BOLD+"FATAL "+self.name+Logger.END
        elif style == "execution":
            prefix = Logger.OKBLUE+self.name+Logger.END
        else: prefix = self.name
        prefix+=": "
        text = prefix+text
        print(text)
        if self.seb != None: asyncio.run(self.seb())

ModuleLogger = Logger("module")
HTTPLogger = Logger("http")
ModLogger = Logger("mod")
DBLogger = Logger("database")
MainLogger = Logger("main")
ShellLogger = Logger("shell")
DebugLogger = Logger("debug")


async def channel_log(self,log):
    logto = await self.fetch_channel(logging_channel)
    await logto.send(log)

def dlog(text):
    if dev_mode: DebugLogger.log(text)

def domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve the domain."
def convert_to_base64(number):

    byte_representation = str(number).encode('utf-8')


    base64_representation = base64.b64encode(byte_representation)

    result = base64_representation.decode('utf-8')

    return result
def premium_reload():
    global premium_list
    MainLogger.log("Loading Premium Users")
    connection = sqlite3.connect('assistantdata/users.db')
    cursor = connection.cursor()
    
    query = "SELECT user_id FROM users WHERE premium = 1"
    cursor.execute(query)
    
    premium_user_ids = cursor.fetchall()
    
    cursor.close()
    connection.close()
    for i in premium_list:
        premium_list.clear()
    for user_id in premium_user_ids:
        premium_list.append(int(user_id[0])) 

def ban_reload():
    global banlist
    MainLogger.log("Loading banned Users")
    connection = sqlite3.connect('assistantdata/users.db')
    cursor = connection.cursor()
    
    query = "SELECT user_id FROM users WHERE banned = 1"
    cursor.execute(query)
    
    banned_user_ids = cursor.fetchall()
    
    cursor.close()
    connection.close()

    for user_id in banned_user_ids:
        banlist.append(user_id) 
def message_without_command(params):
    message = ""
    for param in params[1:]: message += param+" "
    return message
def getAdminLevel(user_id):
    0 # User
    1 # Can add/remove premium
    2 # Can View execute various admin commands
    3 # Can ban users
    4 # Can reboot
    l1 = []
    l2 = [1246345221210509333, 1175455408538800205]
    l3 = [827820322706292736]
    l4 = [1142511163821801493, 1158452261538771055]
    if user_id in l1: return 1
    elif user_id in  l2: return 2
    elif user_id in l3: return 3
    elif user_id in l4: return 4
    else: return 0


def isInSlowmode(user_id,time):
    time_str = db.getData(user_id,"slowmode")
    format_str = '%Y-%m-%d %H:%M:%S'
    dt = datetime.strptime(time_str, format_str)
    now = datetime.now()
    time_difference = now - dt
    seconds_diff = time_difference.total_seconds()

    if seconds_diff > time: return False
    else: return True
def getSlowmode(user_id):
    time_str = db.getData(user_id,"slowmode")
    format_str = '%Y-%m-%d %H:%M:%S'

    dt = datetime.strptime(time_str, format_str)
    now = datetime.now()
    time_difference = now - dt

    seconds_diff = time_difference.total_seconds()

    return seconds_diff
async def ai(prompt,message):
    HTTPLogger.log("Fetching AI Response", style="execution")
    await message.channel.typing()
    async with ClientSession() as session:
            try:
                async with session.post(
                    url="https://api.binjie.fun/api/generateStream",
                    headers={
                        "origin": "https://chat18.aichatos8.com/",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
                    },
                    json={
                        "prompt": prompt+"\n respond in under 3500 characters",
                        "system": "Always talk in English.",
                        "withoutContext": True,
                        "stream": False,
                    },
                ) as resp:
                    return await resp.text()
            except ClientError as exc:
                raise ClientError("Unable to fetch the response.") from exc
            






def execute(cmd):
    if cmd == "exit":
            exit()
    elif cmd.startswith("execute"):
            toex = cmd.replace("execute ", "")
            ShellLogger.log("Executing Shell Command: "+toex)
            try:
                return exec(toex)
            except Exception as e: 
                ShellLogger.log("Failed shell execution", style="fatal")
                return e
    elif cmd.startswith("ldb"):
            return db.printDB()
    else:
         return f"`{cmd}` not found"
def paramExists(p,n):
    if len(p) >= n+1:
        return True
    elif len(p) >= n: return True
    else: return False
def hasCoins(user_id, coins):
    if db.getData(user_id,"coins") >= coins: return True
    else: return False