from ..Module import * 
from ..Utils import * 
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from io import BytesIO
from discord import File
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

async def blur_callback(CommandObject, message, self, params, command_data):
    image_bytes = await message.attachments[0].read()
    x, y, width, height, blur_radius = map(float, params[1:6])
    new_image = blur(image_bytes, int(x), int(y), int(width), int(height), blur_radius)
    
    with BytesIO() as image_binary:
        image_binary.write(new_image.getvalue())
        image_binary.seek(0)
        await message.channel.send(file=File(fp=image_binary, filename='image_with_blur.png'))
async def rotate_callback(CommandObject, message, self, params, command_data):
    image = Image.open(BytesIO(await message.attachments[0].read()))

    blurred_region = image.rotate(int(params[1]))

    image.paste(blurred_region)
    output = BytesIO()
    image.save(output, format='PNG')
    output.seek(0)

    with BytesIO() as image_binary:
        image_binary.write(output.getvalue())
        image_binary.seek(0)
        await message.channel.send(file=File(fp=image_binary, filename='image_with_blur.png'))


async def resize_callback(CommandObject, message, self, params, command_data):
    image = Image.open(BytesIO(await message.attachments[0].read()))

    image = image.resize((int(params[1]),int(params[2])))


    output = BytesIO()
    image.save(output, format='PNG')
    output.seek(0)

    with BytesIO() as image_binary:
        image_binary.write(output.getvalue())
        image_binary.seek(0)
        await message.channel.send(file=File(fp=image_binary, filename='image_with_blur.png'))
async def convert_callback(CommandObject, message, self, params, command_data):

    image = Image.open(BytesIO(await message.attachments[0].read()))
    output = BytesIO()
    image.save(output, format=params[1].upper())
    output.seek(0)

    with BytesIO() as image_binary:
        image_binary.write(output.getvalue())
        image_binary.seek(0)
        await message.channel.send(file=File(fp=image_binary,filename=f"out.{params[1]}"))

async def text_callback(CommandObject, message, self, params, command_data):

    image = Image.open(BytesIO(await message.attachments[0].read()))
    draw = ImageDraw.Draw(image)


    text = ""
    for i in params[7:]:
        text+=i+" "
    font = ImageFont.truetype("arial.ttf", size=int(params[1]))
    text_color = (int(params[4]), int(params[5]), int(params[6]))  
    position = (int(params[2]), int(params[3]))

    draw.text(position, text, fill=text_color, font=font)


    output = BytesIO()
    image.save(output, format='PNG')
    output.seek(0)

    with BytesIO() as image_binary:
        image_binary.write(output.getvalue())
        image_binary.seek(0)
        await message.channel.send(file=File(fp=image_binary, filename='image_with_blur.png'))

async def bgr_callback(CommandObject, message, self, params, command_data):

    image = Image.open(BytesIO(await message.attachments[0].read()))

    input_image_bytes = BytesIO()
    image.save(input_image_bytes, format='PNG')
    input_image_bytes.seek(0)
    output_image_bytes = rembg.remove(input_image_bytes.getvalue())


    output = BytesIO(output_image_bytes)

 
    output.seek(0)
    with BytesIO() as image_binary:
        image_binary.write(output.getvalue())
        image_binary.seek(0)
        await message.channel.send(file=File(fp=image_binary, filename='image_with_removed_bg.png'))

bg_command = Command("bg", "Remove bg from an Image", bgr_callback, IMAGES, aliases=['rembg',"rmvbg","bgremove","bgremv","bgr"], ispremium=True)
text_command = Command("imgtext", "Add text to an Image", text_callback, IMAGES, aliases=['textonimage',"addtext"], params=["SIZE","X","Y","R","G","B","TEXT"], ispremium=True)
convert_command = Command("convert", "Convert an image to [png, jpg, jpeg, gif or other image filetypes]", convert_callback, IMAGES, aliases=['imagefile'], params=["FILETYPE"], ispremium=True)
resize_command = Command("resize", "Resize an image", resize_callback, IMAGES, aliases=['imagesize'], params=["HEIGHT","WIDTH"], ispremium=True)
rotate_command = Command("rotate", "Add blur to an image", rotate_callback, IMAGES, aliases=['rotateimage'], params=["ANGLE"], ispremium=True)
blur_command = Command("blur", "Add blur to an image", blur_callback, IMAGES, aliases=['addblur', 'censor'], params=["X", "Y", "WIDTH", "HEIGHT", "BLUR"], ispremium=True)
