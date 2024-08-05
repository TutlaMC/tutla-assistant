# Utils
import base64
import socket
premium_list = []
banlist=[]
version = 'V1.4'
true = True
false = False

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
        with open('assistantdata/premium.txt','r') as f:
                lines = f.readlines()
                for line in lines: 
                    line = line.replace('\n','')
                    premium_list.append(line)
def ban_reload():
    global banlist
    with open('assistantdata/bans.txt','r') as f:
            lines = f.readlines()
            for line in lines:banlist.append(line)
def message_without_command(params):
    message = ""
    for param in params[1:]: message += param+" "
    return message