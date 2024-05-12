from ..Module import * 
from ..Utils import *
import requests
async def ipinfo_callback(CommandObject,message,self,params,command_data):
                        api_key = "ENTER YOUR API KEY HERE"  
                        ip_address = message.content.replace('.iptranslate ','')
                        ip_address = ip_address.replace("https://","")
                        ip_address = ip_address.replace("http://","")
                        ip_address = ip_address.replace(' ','')
                        url = f"http://ipinfo.io/{ip_address}?token={api_key}"
                        
                        response = requests.get(url)
                        data = response.json()

                        ip = data.get("ip", "N/A")
                        city = data.get("city", "N/A")
                        region = data.get("region", "N/A")
                        country = data.get("country", "N/A")
                        location = f"{city}, {region}, {country}"
                        if country=='N/A': 
                            ip_address = domain_to_ip(ip_address)
                            url = f"http://ipinfo.io/{ip_address}?token={api_key}"
                            response = requests.get(url)
                            data = response.json()
                            

                            ip = data.get("ip", "N/A")
                            city = data.get("city", "N/A")
                            region = data.get("region", "N/A")
                            country = data.get("country", "N/A")
                            location = f"{city}, {region}, {country}"
                            
                        await message.channel.send(f'Location to `{ip_address}` is ```{location}```')
                    
ipinfo_command = Command("iptranslate","Check the location of the specified IP address",ipinfo_callback,TOOLS,aliases=["iptransalate","ipinfo",'ip'],params=["IP/DOMAIN"])