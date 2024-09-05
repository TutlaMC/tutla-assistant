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
    for i in params[8:]:
        text+=i+" "
    if params[7] in fonts:  font = ImageFont.truetype(f"assistantdata/fonts/{params[7]}.ttf", size=int(params[1]))
    else: font = ImageFont.truetype("assistantdata/fonts/roboto.ttf", size=int(params[1]))
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




async def kernel_callback(CommandObject, message, self, params, command_data):

    image = Image.open(BytesIO(await message.attachments[0].read()))

    kernel_5x5 = [-2,  0, -1,  0,  0,
              0, -2, -1,  0,  0,
             -1, -1,  1,  1,  1,
              0,  0,  1,  2,  0,
              0,  0,  1,  0,  2]

    for i in range(len(kernel_5x5)):
        kernel_5x5[i] *= int(params[1])

    output_image = image.filter(ImageFilter.Kernel((5, 5), kernel_5x5, 1, 0))


    image_binary = BytesIO()
    output_image.save(image_binary, format='PNG')
    image_binary.seek(0)

    await message.channel.send(file=File(fp=image_binary, filename='image_with_filtered_kernel.png'))


async def w2t_callback(CommandObject, message, self, params, command_data):

    image = Image.open(BytesIO(await message.attachments[0].read())).convert("RGBA")
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

    await message.channel.send(file=File(fp=image_binary, filename='image_with_filtered_kernel.png'))

async def filtercolor_callback(CommandObject, message, self, params, command_data):

    tofilter = params[-1:]
    print(tofilter)
    if not len(tofilter) >= 1: return False
    image = Image.open(BytesIO(await message.attachments[0].read())).convert("RGBA")
    datas = image.getdata()

    new_data = []
    tofilter_rgb = [(int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)) for color in tofilter]

    for item in datas:
        if item[:3] in tofilter_rgb:
            new_data.append(item)
        else:
            new_data.append((item[0], item[1], item[2], 0))



    image.putdata(new_data)
    image_binary = BytesIO()
    image.save(image_binary, "PNG")
    image_binary.seek(0)

    await message.channel.send(file=File(fp=image_binary, filename='image_with_filtered.png'))

async def getcolors_callback(CommandObject, message, self, params, command_data):

    image = Image.open(BytesIO(await message.attachments[0].read())).convert("RGBA")
    datas = image.getdata()

    unique_colors = set(datas)

    color_list = []
    for color in unique_colors:
        # Convert the color to hexadecimal
        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        color_list.append(hex_color)
    
    
    final="Colors found in image:\n"
    buffer = BytesIO()
    string_to_append = str(color_list)
    buffer.write(string_to_append.encode('utf-8'))
    buffer.seek(0)
    await message.channel.send(final,file=File(fp=buffer,filename="balls.txt"))

async def speechbubble_callback(CommandObject, message, self, params, command_data):
    image = Image.open(BytesIO(await message.attachments[0].read())).convert("RGBA")
    bubble_image = Image.open('assistantdata/bubble.png').convert("RGBA")

    bubble_width = image.width
    bubble_height = int(image.height/4)
    bubble_image = bubble_image.resize((bubble_width, bubble_height), Image.LANCZOS)

    # Paste the bubble onto the top of the base image without changing the canvas size
    image.paste(bubble_image, (0, 0), bubble_image)
    image = image.resize((int(image.width*1.5),image.height))

    image_binary = BytesIO()
    image.save(image_binary, "PNG")
    image_binary.seek(0)

    await message.channel.send(file=File(fp=image_binary, filename='image_with_filtered.png'))
speechbubble_command = Command("speechbubble", "Appends a speechbubble to the image", speechbubble_callback, IMAGES, aliases=["bubble","🗣️"])
getcolors_command = Command("getcolors", "Gets all the colors in an image", getcolors_callback, IMAGES, aliases=["colors","findcolors"])
filtercolor_command = Command("filtercolor", "Returns the image with only the specified color in it", filtercolor_callback, IMAGES, aliases=["filter","extractcolor"])
w2t_command = Command("w2t", "Remove the white from an image (and converts it to transparent)", w2t_callback, IMAGES, aliases=["white2transparent","transparent","removewhite","blacklivesmatter","black>white"])
kernel_command = Command("kernel", "Fry an image", kernel_callback, IMAGES, aliases=["cook","fry","deepfry"],ispremium=True)
bg_command = Command("bg", "Remove bg from an Image", bgr_callback, IMAGES, aliases=['rembg',"rmvbg","bgremove","bgremv","bgr"], ispremium=True)
text_command = Command("imgtext", "Add text to an Image", text_callback, IMAGES, aliases=['textonimage',"addtext"], params=["SIZE","X","Y","R","G","B","TEXT","Optional:FONT"], ispremium=True)
convert_command = Command("convert", "Convert an image to [png, jpg, jpeg, gif or other image filetypes]", convert_callback, IMAGES, aliases=['imagefile'], params=["FILETYPE"])
resize_command = Command("resize", "Resize an image", resize_callback, IMAGES, aliases=['imagesize'], params=["HEIGHT","WIDTH"])
rotate_command = Command("rotate", "Add blur to an image", rotate_callback, IMAGES, aliases=['rotateimage'], params=["ANGLE"])
blur_command = Command("blur", "Add blur to an image", blur_callback, IMAGES, aliases=['addblur', 'censor'], params=["X", "Y", "WIDTH", "HEIGHT", "BLUR"], ispremium=True)
