from ..Module import * 
from ..Utils import *
import requests
async def ipinfo_callback(CommandObject,message,self,params,command_data):
                        ip_address = params[1]
                        ip_address = ip_address.replace("https://","")
                        ip_address = ip_address.replace("http://","")
                        ip_address = ip_address.replace(' ','')
                        url = f"http://ipinfo.io/{ip_address}"
                        
                        response = requests.get(f"http://ipinfo.io/{domain_to_ip(ip_address)}")
                        data = response.json()
                        location = f"{data.get('ip', 'N/A')}: {data.get('country', 'N/A')}, {data.get('region', 'N/A')}, {data.get('city', 'N/A')}"
                        if data.get("country","N/A")=='N/A' and not data.get("ip","N/A").isdigit(): 
                            response = requests.get(f"http://ipinfo.io/{domain_to_ip(ip_address)}")
                            data = response.json()
                            location = f"{data.get('ip', 'N/A')}: {data.get('country', 'N/A')}, {data.get('region', 'N/A')}, {data.get('city', 'N/A')}"
                            
                        await message.channel.send(f'{params[1]}:```{location}```')
                    
ipinfo_command = Command("iptranslate","Check the location of the specified IP address",ipinfo_callback,TOOLS,aliases=["iptransalate","ipinfo",'ip'],params=["IP/DOMAIN"])