from ..Module import * 
from ..Utils import *
def b2t(b):
    return ''.join(chr(int(byte, 2)) for byte in b.split())
def t2b(text):
    return ' '.join(format(ord(char), '08b') for char in text)

binary_input = '00101110 01100010 01101001 01101110 01100001 01110010 01111001'
async def binary_callback(CommandObject,message,self,params,command_data):

    await message.channel.send(b2t(message_without_command(params)))
async def tobinary_callback(CommandObject,message,self,params,command_data):

    await message.channel.send(t2b(message_without_command(params)))

binary_command = Command("binary2text","Decode Binary",binary_callback,TOOLS,aliases=["binary","frombinary","b2t"],params=["BINARY"])
tobinary_command = Command("text2binary","Encode Binary",tobinary_callback,TOOLS,aliases=["tobinary","t2b"],params=["TEXT"])
