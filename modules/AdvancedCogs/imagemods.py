
from ..Module import *
from ..Utils import * 
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from io import BytesIO
from discord import File
from collections import defaultdict
import rembg

# Functionality matters, not if I used ai or not to geenrate the code (only for this one and .caption i swear) 
# PS: I debugged it & added a few things so erm i take all credit


    

def blur(image_bytes, x, y, width, height, blur_radius):
    image = Image.open(BytesIO(image_bytes))

    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    blur_radius = float(blur_radius)
    image_width, image_height = image.size
    x = max(0, min(x, image_width - width))
    y = max(0, min(y, image_height - height))
    
    region = (x, y, x + width, y + height)
    region_image = image.crop(region)
    
    blurred_region = region_image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    image.paste(blurred_region, region)
    output = BytesIO()
    image.save(output, format='PNG')
    output.seek(0)
    return output


class PhotoshopGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    group = app_commands.Group(name="photoshop", description="Image editing commands")

    
    
    @premium_command
    @group.command(name="getcolors", description="Get all colors in an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def getcolors(self,ctx: discord.Interaction, image: discord.Attachment):
        await ctx.response.send_message("Geting colors..",ephemeral=True)
        image = Image.open(BytesIO(await image.read())).convert("RGBA")
        datas = image.getdata()

        unique_colors = set(datas)

        color_list = []
        for color in unique_colors:
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            color_list.append(hex_color)
        
        
        final="Colors found in image:\n"
        buffer = BytesIO()
        string_to_append = str(color_list)
        buffer.write(string_to_append.encode('utf-8'))
        buffer.seek(0)
        await ctx.followup.send(final,file=File(fp=buffer,filename="colors.txt"))
    
    @premium_command
    @group.command(name="extract_text", description="Extract taxt from an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def textfimage_callback(self,ctx:discord.Interaction,image:discord.Attachment):
        await ctx.response.send_message("Extracting text...")
        api_url = 'https://api.api-ninjas.com/v1/imagetotext'
        image_data = await image.read()
        image_file_like = BytesIO(image_data)
        files = {'image': ('image.png', image_file_like, 'image/png')}
        r = requests.post(api_url, files=files)
        data = r.json()





        def get_tens(value):
            return value // 10 * 10

        grouped = defaultdict(list)

        for item in data:
            y1 = item['bounding_box']['y1']
            text = item['text']
            tens = get_tens(y1)
            grouped[tens].append(text)

        e = dict(sorted(grouped.items()))
        
        final = ""
        for y, texts in e.items():
            for text in texts:
                final+=text+" "
                print(y,text)
            final +="\n"
        await ctx.followup.send(final)

    

    @premium_command
    @group.command(name="kernel",description="Burn an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def kernel_callback(self,ctx: discord.Interaction, image: discord.Attachment, level: int):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read()))

        kernel_5x5 = [-2,  0, -1,  0,  0,
                0, -2, -1,  0,  0,
                -1, -1,  1,  1,  1,
                0,  0,  1,  2,  0,
                0,  0,  1,  0,  2]

        for i in range(len(kernel_5x5)):
            kernel_5x5[i] *= level

        output_image = image.filter(ImageFilter.Kernel((5, 5), kernel_5x5, 1, 0))


        image_binary = BytesIO()
        output_image.save(image_binary, format='PNG')
        image_binary.seek(0)

        await ctx.followup.send(file=File(fp=image_binary, filename='image_with_filtered_kernel.png'))

    
    @group.command(name="removewhite",description="Converts white to a transparent part")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def w2t_callback(self,ctx: discord.Interaction, image: discord.Attachment):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read())).convert("RGBA")
        datas = image.getdata()

        new_data = []
        for item in datas:
            # Check if the pixel is white (R=255, G=255, B=255)
            if item[:3] == (255, 255, 255):
                # Make it transparent (R=255, G=255, B=255, A=0)
                new_data.append((255, 255, 255, 0))
            else:
                # Leave it as it is
                new_data.append(item)

        image.putdata(new_data)
        image_binary = BytesIO()
        image.save(image_binary, "PNG")
        image_binary.seek(0)

        await ctx.followup.send(file=File(fp=image_binary, filename='image_with_filtered_kernel.png'))
    
    @premium_command
    @group.command(name="removebackground",description="Removes background")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def bgr_callback(self,ctx: discord.Interaction, image:discord.Attachment):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read()))

        input_image_bytes = BytesIO()
        image.save(input_image_bytes, format='PNG')
        input_image_bytes.seek(0)
        output_image_bytes = rembg.remove(input_image_bytes.getvalue())


        output = BytesIO(output_image_bytes)

    
        output.seek(0)
        with BytesIO() as image_binary:
            image_binary.write(output.getvalue())
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary, filename='image_with_removed_bg.png'))

    @premium_command
    @group.command(name="text",description="Add text to an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def addtext(self,ctx: discord.Interaction, image:discord.Attachment, text:str, size: int = 32, y_position: int = 0, x_position: int = 0, r: int = 255, g: int = 255, b: int = 255, font: str = "roboto"):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read()))
        draw = ImageDraw.Draw(image)


        if font in fonts:  font = ImageFont.truetype(f"data/fonts/font.ttf", size=size)
        else: 
            await ctx.followup.send("Select a valid font (Case Sensitive)! (/list fonts)\nExample: `roboto`, `gta`, `Bubble-Letters`",ephemeral=True)
            return
        text_color = (r,g,b)  
        position = (y_position, x_position)

        draw.text(position, text, fill=text_color, font=font)


        output = BytesIO()
        image.save(output, format='PNG')
        output.seek(0)

        with BytesIO() as image_binary:
            image_binary.write(output.getvalue())
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary, filename='image_with_text.png'))

    @premium_command
    @group.command(name="image",description="Add an image to an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def addtext(self,ctx: discord.Interaction, image:discord.Attachment, overlay:discord.Attachment, y_position: int, x_position: int,  size: int = 32):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read()))
        image2 = Image.open(BytesIO(await overlay.read()))
        image2=image2.convert('RGBA')
        image.paste(image2,(x_position,y_position),image2)

        output = BytesIO()
        image.save(output, format='PNG')
        output.seek(0)

        with BytesIO() as image_binary:
            image_binary.write(output.getvalue())
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary, filename='image_with_text.png'))


    @group.command(name="placeholder", description="Generate a placeholder image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def placeholder(self,ctx:discord.Interaction, width:int,height:int):
            await ctx.response.send_message("Creating image placeholder...",ephemeral=True)
            f1 = width
            f2 = height
            api_url = f'https://fakeimg.pl/{f1}x{f2}'
            r = requests.get(api_url)
            await ctx.followup.send(file=File(fp=BytesIO(r.content),filename='placeholder.jpg'))

    @group.command(name="convert", description="Change filetype (image)")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def file_callback(self,ctx: discord.Interaction, image:discord.Attachment, filetype: str = "gif"):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read()))
        output = BytesIO()
        image.save(output, format=filetype.upper())
        output.seek(0)

        with BytesIO() as image_binary:
            image_binary.write(output.getvalue())
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary,filename=f"out.{filetype}"))




    @group.command(name="resize", description="Resize an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def resize_callback(self,ctx: discord.Interaction, image:discord.Attachment, width: int, height: int):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read()))

        image = image.resize((width,height))


        output = BytesIO()
        image.save(output, format='PNG')
        output.seek(0)

        with BytesIO() as image_binary:
            image_binary.write(output.getvalue())
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary, filename='image_with_blur.png'))

    @group.command(name="rotate", description="Rotate an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def rotate_callback(self,ctx: discord.Interaction, image:discord.Attachment, degree: int):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image = Image.open(BytesIO(await image.read()))

        blurred_region = image.rotate(degree)

        image.paste(blurred_region)
        output = BytesIO()
        image.save(output, format='PNG')
        output.seek(0)

        with BytesIO() as image_binary:
            image_binary.write(output.getvalue())
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary, filename='image_with_blur.png'))

    @group.command(name="blur", description="Blur an image")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def file_callback(self,ctx: discord.Interaction, image:discord.Attachment, blur_radius: int, width:int=50,height:int=50, x: int = 50, y:int=50):
        await ctx.response.send_message("Editing Image....",ephemeral=True)
        image_bytes = await image.read()
        new_image = blur(image_bytes, x, y, width, height, blur_radius)
        
        with BytesIO() as image_binary:
            image_binary.write(new_image.getvalue())
            image_binary.seek(0)
            await ctx.followup.send(file=File(fp=image_binary, filename='image_with_blur.png'))

async def setup(bot: commands.Bot):
    await bot.add_cog(PhotoshopGroup(bot))