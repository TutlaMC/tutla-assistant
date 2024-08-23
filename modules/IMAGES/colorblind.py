from ..Module import * 
from ..Utils import * 
from PIL import Image
from io import BytesIO
from discord import File
async def colorblind_callback(CommandObject, message, self, params, command_data):

    image = Image.open(BytesIO(await message.attachments[0].read()))
    rgb = image.split()
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    if len(params) > 1:
        if params[1] == '0':
            image = Image.merge("RGB", (r,g,b))
        elif params[1] == '1':
            image = Image.merge("RGB",(r,b,g))
        elif params[1] == '2':
            image = Image.merge("RGB",(b,r,g))
        elif params[1] == '3':
            image = Image.merge("RGB",(b,g,r))
        elif params[1] == "4":
            image = Image.merge("RGB",(g,b,r))
        elif params[1] == "5":
            image = Image.merge("RGB",(g,r,b))
        else: image = Image.merge("RGB", (g,b,r))
    else: image = Image.merge("RGB", (g,b,r))
    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)

    with BytesIO() as image_binary:
        image_binary.write(output.getvalue())
        image_binary.seek(0)
        await message.channel.send(file=File(fp=image_binary,filename=f"output.png"))
    

colorblind_command = Command("colorblind", "colorblind", colorblind_callback, IMAGES, aliases=['remix'], params=["0|1|2|4|5"])

