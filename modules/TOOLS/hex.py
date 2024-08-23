from ..Module import *
from PIL import Image, ImageDraw, ImageFont
import io
from discord import File

async def hex_image_callback(CommandObject, message, self, params, command_data):
    try:
        hex_color = params[1]
        if not hex_color.startswith('#'):
            hex_color = f"#{hex_color}"
        
        # Convert hex to RGB
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        width, height = 200, 100
        img = Image.new('RGB', (width, height), (r, g, b))
        draw = ImageDraw.Draw(img)
        


        with io.BytesIO() as output:
            img.save(output, format="PNG")
            output.seek(0)
            await message.channel.send(file=File(fp=output, filename="hex_color.png"))

    except Exception as e:
        await message.channel.send(f"Error: {str(e)}")
hex_image_command = Command("hex","Generates an image with the specified hex color.",hex_image_callback, CLIENT, aliases=['color'],params=["HEX"])
