
from ..Module import *
from ..Utils import *
from discord.ui import View, Button
import discord,requests,re,aiohttp,random
from io import BytesIO
from discord import File
from PIL import Image, ImageDraw, ImageFont
import sys

async def tobruh(file,ctx):
    
    def get_pixel_hex(x, y):
        r, g, b = img.getpixel((x, y))
        hex_value = "{:02x}{:02x}{:02x}".format(r, g, b)
        
        return hex_value
    if file.size > 80000: 
        await ctx.response.send_message("File is too big!")
        return False

    img = Image.open(BytesIO(await file.read()))
    img = img.convert('RGB')

    width, height = img.size

    bwidth = width.to_bytes(length=4, byteorder=sys.byteorder)
    bheight = height.to_bytes(length=4, byteorder=sys.byteorder)

    bruh = bwidth + bheight

    iy = 0
    while iy < height:
        ix = 0
        while ix < width:
            hex = get_pixel_hex(ix, iy)
            bruh = bruh + hex.encode('utf-8')
            ix += 1
        iy += 1
        if not iy == height:
            bruh = bruh + "\n".encode('utf-8')
    return BytesIO(bruh)


async def debruh(file):
    
    def hex_to_rgb(hex_color):
        if len(hex_color) != 6:
            raise ValueError(f"Invalid hex color: {hex_color}. Expected format: RRGGBB.")
        
        try:
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        except ValueError:
            raise ValueError(f"Invalid characters in hex color: {hex_color}.")
        
    def set_pixel_color(x, y, hex_color):
        rgb_color = hex_to_rgb(hex_color)
        img.putpixel((x, y), rgb_color)
        
    def split_every_6_chars(string):
        return [string[i:i+6] for i in range(0, len(string), 6)]

    bruh = BytesIO(await file.read())
    size = bruh.read(8)

    width = int.from_bytes(size[0:4], byteorder=sys.byteorder)
    height = int.from_bytes(size[4:8], byteorder=sys.byteorder)
    size = (width, height)

    bruh.seek(8)
    bruh_data = str(bruh.read(), encoding='utf-8').splitlines()
    img = Image.new("RGB", size)

    iy = 0
    while iy < height:
        ix = 0
        while ix < width:
            hex = bruh_data[iy]
            hex = split_every_6_chars(hex)[ix]
            set_pixel_color(ix, iy, hex)
            ix += 1
        iy += 1

    image_binary = BytesIO()
    img.save(image_binary, "PNG")
    image_binary.seek(0)
    return image_binary

def add_caption_to_image(image_data, caption, box_height):
    font_path = "data/fonts/font.ttf"
    image = Image.open(image_data)
    draw = ImageDraw.Draw(image)

    font_size = 1
    font = ImageFont.truetype(font_path, font_size)

    while True:
        bbox = draw.textbbox((0, 0), caption, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if text_height > box_height or text_width > image.width * 0.9:
            break
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)

    new_image_height = image.height + box_height
    new_image = Image.new('RGB', (image.width, new_image_height), (255, 255, 255))

    draw = ImageDraw.Draw(new_image)
    draw.text(((new_image.width - text_width) / 2, (box_height - text_height) / 2), caption, font=font, fill=(0, 0, 0))

    new_image.paste(image, (0, box_height))

    return new_image 


class ImageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @premium_command
    @app_commands.command(name="bruh", description="Bruh/Debruh a File")
    @app_commands.check(commandCheck)
    async def bruhify(self,ctx: discord.Interaction, file:discord.Attachment, bruh: bool = True):
        if bruh:
            await ctx.response.send_message("Made by <@914245831748632636> | [Github](<https://github.com/Tycho10101/bruh-python/>)",file=File(fp=await tobruh(file,ctx), filename='image.bruh'))
        else:
            await ctx.response.send_message("Made by <@914245831748632636> | [Github](<https://github.com/Tycho10101/bruh-python/>)",file=File(fp=await debruh(file), filename='image.png'))
    
    @app_commands.command(name="caption", description="Add caption to an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def caption_callback(self,ctx:discord.Interaction,image: discord.Attachment,text:str):
        new_image = add_caption_to_image(BytesIO(await image.read()), text, 80)
        
        with BytesIO() as image_binary:
                new_image.save(image_binary, 'GIF')
                image_binary.seek(0)
                await ctx.response.send_message(file=File(fp=image_binary, filename='image_with_caption.png'))

    @app_commands.command(name="color", description="Generate a color/gradient")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def color(self,ctx: discord.Interaction, hex_1: str, hex_2: str = None, r: int = None, g: int = None, b: int=None,length:int = 512):
        if hex_2:
            try:
                width = length
                height = 512
                color1 = hex_1
                color2 = hex_2

                img = Image.new('RGB', (width, height), color1)
                draw = ImageDraw.Draw(img)

                for i in range(width):
                    r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // width
                    g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // width
                    b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // width
                    draw.line([(i, 0), (i, height)], fill=(r, g, b))

                with BytesIO() as output:
                    img.save(output, format="PNG")
                    output.seek(0)
                    await ctx.response.send_message(file=File(fp=output, filename="gradient.png"))

            except Exception as e:
                await ctx.response.send_message(f"Error: {str(e)}")
        elif r and g and b:
            try:
                width, height = 200, 100
                img = Image.new('RGB', (width, height), (r, g, b))

                


                with BytesIO() as output:
                    img.save(output, format="PNG")
                    output.seek(0)
                    await ctx.response.send_message("#{:02x}{:02x}{:02x}".format(r,g,b),file=File(fp=output, filename="rgb_color.png"))

            except Exception as e:
                await ctx.response.send_message(f"Error: ```yaml{str(e)}```")
        else:
            try:
                hex_color = hex_1
                if not hex_color.startswith('#'):
                    hex_color = f"#{hex_color}"
                
                r = int(hex_color[1:3], 16)
                g = int(hex_color[3:5], 16)
                b = int(hex_color[5:7], 16)

                width, height = 200, 100
                img = Image.new('RGB', (width, height), (r, g, b))
                draw = ImageDraw.Draw(img)
                


                with BytesIO() as output:
                    img.save(output, format="PNG")
                    output.seek(0)
                    await ctx.response.send_message(f"IN RGB: {r}, {g}, {b}",file=File(fp=output, filename="hex_color.png"))

            except Exception as e:
                await ctx.response.send_message(f"Error: {str(e)}")
    @app_commands.command(name="color", description="Generate a color/gradient")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def color(self,ctx: discord.Interaction, hex_1: str, hex_2: str = None, r: int = None, g: int = None, b: int=None,length:int = 512):
        if hex_2:
            try:
                width = length
                height = 512
                color1 = hex_1
                color2 = hex_2

                img = Image.new('RGB', (width, height), color1)
                draw = ImageDraw.Draw(img)

                for i in range(width):
                    r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // width
                    g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // width
                    b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // width
                    draw.line([(i, 0), (i, height)], fill=(r, g, b))

                with BytesIO() as output:
                    img.save(output, format="PNG")
                    output.seek(0)
                    await ctx.response.send_message(file=File(fp=output, filename="gradient.png"))

            except Exception as e:
                await ctx.response.send_message(f"Error: {str(e)}")
        elif r and g and b:
            try:
                width, height = 200, 100
                img = Image.new('RGB', (width, height), (r, g, b))

                


                with BytesIO() as output:
                    img.save(output, format="PNG")
                    output.seek(0)
                    await ctx.response.send_message("#{:02x}{:02x}{:02x}".format(r,g,b),file=File(fp=output, filename="rgb_color.png"))

            except Exception as e:
                await ctx.response.send_message(f"Error: ```yaml{str(e)}```")
        else:
            try:
                hex_color = hex_1
                if not hex_color.startswith('#'):
                    hex_color = f"#{hex_color}"
                
                r = int(hex_color[1:3], 16)
                g = int(hex_color[3:5], 16)
                b = int(hex_color[5:7], 16)

                width, height = 200, 100
                img = Image.new('RGB', (width, height), (r, g, b))
                draw = ImageDraw.Draw(img)
                


                with BytesIO() as output:
                    img.save(output, format="PNG")
                    output.seek(0)
                    await ctx.response.send_message(f"IN RGB: {r}, {g}, {b}",file=File(fp=output, filename="hex_color.png"))

            except Exception as e:
                await ctx.response.send_message(f"Error: {str(e)}")

    @app_commands.command(name="colorblind", description="See in colorblind (CC)")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def colorblind_callback(self,ctx: discord.Interaction, image:discord.Attachment,level:int=1):

        image = Image.open(BytesIO(await image.read()))
        rgb = image.split()
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if level < 6:
            if level == 0:
                image = Image.merge("RGB", (r,g,b))
            elif level == 1:
                image = Image.merge("RGB",(r,b,g))
            elif level == 2:
                image = Image.merge("RGB",(b,r,g))
            elif level == 3:
                image = Image.merge("RGB",(b,g,r))
            elif level == 4:
                image = Image.merge("RGB",(g,b,r))
            elif level == 5:
                image = Image.merge("RGB",(g,r,b))
            else: image = Image.merge("RGB", (g,b,r))
        else: await ctx.response.send_message("Level must be between 0-5")
        output = BytesIO()
        image.save(output, format="PNG")
        output.seek(0)

        with BytesIO() as image_binary:
            image_binary.write(output.getvalue())
            image_binary.seek(0)
            await ctx.response.send_message(file=File(fp=image_binary,filename=f"output.png"))
    @app_commands.command(name="bubble", description="Add a bubble to image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def bubble_callback(self,ctx: discord.Interaction, image: discord.Attachment):
            await ctx.response.send_message("Editing Image....",ephemeral=True)
            image = Image.open(BytesIO(await image.read())).convert("RGBA")
            bubble_image = Image.open('data/bubble.png').convert("RGBA")

            bubble_width = image.width
            bubble_height = int(image.height/4)
            bubble_image = bubble_image.resize((bubble_width, bubble_height), Image.LANCZOS)
            image.paste(bubble_image, (0, 0), bubble_image)
            image = image.resize((int(image.width*1.5),image.height))

            image_binary = BytesIO()
            image.save(image_binary, "GIF")
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary, filename='bubble.gif'))
async def setup(bot: commands.Bot):
    await bot.add_cog(ImageCog(bot))
