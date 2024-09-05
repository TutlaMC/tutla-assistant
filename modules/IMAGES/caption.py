from ..Module import * 
from ..Utils import * 
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from discord import File
def add_caption_to_image(image_data, caption, box_height):
    font_path = "assistantdata/fonts/font.ttf"
    image = Image.open(BytesIO(image_data))
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



async def caption_callback(CommandObject,message,self,params,command_data):
    new_image = add_caption_to_image(await message.attachments[0].read(), message_without_command(params), 80)
    with BytesIO() as image_binary:
            new_image.save(image_binary, 'GIF')
            image_binary.seek(0)
            await message.channel.send(file=File(fp=image_binary, filename='image_with_caption.png'))

caption_command = Command("caption","Add caption to an image",caption_callback,IMAGES,aliases=['addcaption'],params=["TEXT"])

