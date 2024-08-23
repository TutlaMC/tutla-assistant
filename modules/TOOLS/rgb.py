from ..Module import *
from PIL import Image, ImageDraw, ImageFont
import io
from discord import File
async def rgb_image_callback(CommandObject, message, self, params, command_data):
    try:
        r = int(params[1])
        g = int(params[2])
        b = int(params[3])

        width, height = 200, 100
        img = Image.new('RGB', (width, height), (r, g, b))

        


        with io.BytesIO() as output:
            img.save(output, format="PNG")
            output.seek(0)
            await message.channel.send(file=File(fp=output, filename="rgb_color.png"))

    except Exception as e:
        await message.channel.send(f"Error: ```yaml{str(e)}```")
rgb_image_command = Command("rgb", "Displays RGB", rgb_image_callback, CLIENT, aliases=['rgbcolor'], params=["Red", "Green", "Blue"],)