from ..Module import *
from PIL import Image, ImageDraw
import io
from discord import File

# https://chatgpt.com/share/7e26357e-f1d7-43a7-b9eb-a56c437ec5cf

async def gradient_callback(CommandObject, message, self, params, command_data):
    try:
        width = int(params[1])
        height = int(params[2])
        color1 = params[3]
        color2 = params[4]

        img = Image.new('RGB', (width, height), color1)
        draw = ImageDraw.Draw(img)

        for i in range(width):
            r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // width
            g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // width
            b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // width
            draw.line([(i, 0), (i, height)], fill=(r, g, b))

        with io.BytesIO() as output:
            img.save(output, format="PNG")
            output.seek(0)
            await message.channel.send(file=File(fp=output, filename="gradient.png"))

    except Exception as e:
        await message.channel.send(f"Error: {str(e)}")
gradient_command = Command(
    "gradient", 
    "Generates a gradient image.", 
    gradient_callback, 
    CLIENT, 
    aliases=['linear'], 
    params=["Width", "Height", "Color1 (hex)", "Color2 (hex)"],
    isfree=True
)
