# Utils
import socket, json, base64, sqlite3, asyncio, os, requests
from mods import mod
from data import db
from datetime import datetime
from aiohttp import ClientSession, ClientError
from discord.ext import tasks
premium_list = []
banlist=[]
afk_users = {}
fonts= []

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
        text = str(text)
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

# SETTINGS

MainLogger.log("Loading Config",style="execution")
with open('data/config.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

version = data['version']
dev_mode = data['dev_mode']
feed = data['feed']
logging_channel = data['logging_channel']

about = data['phrases']['about']
discords = data['phrases']['discords']
TOS = data['phrases']['TOS']

question_otd = ""

rapid_api_key = os.getenv('rapid_api_key')

true = True
false = False

for i in os.listdir('data/fonts'):
       fonts.append(i.replace('.ttf',''))





async def channel_log(self,log):
    logto = await self.fetch_channel(logging_channel)
    await logto.send(log)
async def sendToSubScribers(bot, message,embed=None):
    if not feed: return false 
    with open('data/subscribed.txt','r') as f:
        e  = f.readlines()
    for i in e:
        try:
            z = await bot.fetch_channel(int(i))
            if embed:
                await z.send(message,embed=embed)
            else: await z.send(message)
        except Exception:
            MainLogger.log("Can't send feed to subscribed channel",style="warning")

def dlog(text):
    if dev_mode: DebugLogger.log(text)

def domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve the domain."
def api(url, host, query):
    return requests.get(url, headers={
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": host
    }, params=query)

def convert_to_base64(number):

    byte_representation = str(number).encode('utf-8')


    base64_representation = base64.b64encode(byte_representation)

    result = base64_representation.decode('utf-8')

    return result
def premium_reload():
    global premium_list
    MainLogger.log("Loading Premium Users")
    connection = sqlite3.connect('data/users.db')
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
    connection = sqlite3.connect('data/users.db')
    cursor = connection.cursor()
    
    query = "SELECT user_id FROM users WHERE banned = 1"
    cursor.execute(query)
    
    banned_user_ids = cursor.fetchall()
    
    cursor.close()
    connection.close()

    for user_id in banned_user_ids:
        banlist.append(user_id) 

def getAdminLevel(user_id):
    0 # User
    1 # Can add/remove premium
    2 # Can View execute various admin commands
    3 # Can ban users
    4 # Can reboot
    l1 = []
    l2 = [1175455408538800205]
    l3 = []
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
async def ai(prompt):
    HTTPLogger.log("Fetching AI Response", style="execution")
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
    if cmd == "sp":
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
    else: return False
def hasCoins(user_id, coins):
    if db.getData(user_id,"coins") >= coins: return True
    else: return False