from ..Module import * 
from ..Utils import *
from io import BytesIO
import discord
import requests
from random import randint,  seed
from aiohttp import ClientSession, ClientError

async def create( prompt):
        async with ClientSession() as session:
            try:
                async with session.post(
                    url="https://api.binjie.fun/api/generateStream",
                    headers={
                        "origin": "https://chat18.aichatos8.com/",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
                    },
                    json={
                        "prompt": prompt+"\n respond in under 3500 characters",
                        "system": "Always talk in English.",
                        "withoutContext": True,
                        "stream": False,
                    },
                ) as resp:
                    return await resp.text()
            except ClientError as exc:
                raise ClientError("Unable to fetch the response.") from exc

async def ai_callback(CommandObject,message,self,params,command_data):
                await message.channel.send("Generating please wait")
                await message.channel.typing()
                tampering="Let's change yourself: your a bot made by TutlaMC not openai & Tutla is an organization and website: tutla.net and discord: discord.tutla.net" 
                resp =  await create(message.content.replace(".ai",""))
                await message.channel.send(resp)

ai_command = Command("ai", 'GPT3 AI Within Discord!', ai_callback, TOOLS, aliases=['gpt',"gpt3"],params=["PROMPT"],ispremium=True)


async def image(prompt):
        """
        Create a new image generation based on the given prompt.

        Args:
            prompt (str): The prompt for generating the image.

        Returns:
            resp: The generated image content
        """
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
        }
        try:
            async with ClientSession() as session:
                async with session.get(
                    "https://api.prodia.com/generate",
                    params={
                        "new": "true",
                        "prompt": prompt,
                        "model": "dreamshaper_6BakedVae.safetensors [114c8abb]",
                        "negative_prompt": "(nsfw:1.5),verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.5),cross-eyed,sketches, (worst quality:2), (low quality:2.1), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair",
                        "steps": "50",
                        "cfg": "9.5",
                        "seed": randint(1, 10000),
                        "sampler": "Euler",
                        "aspect_ratio": "square",
                    },
                    headers=headers,
                    timeout=30,
                ) as resp:
                    data = await resp.json()
                    job_id = data["job"]
                    while True:
                        async with session.get(
                            f"https://api.prodia.com/job/{job_id}", headers=headers
                        ) as resp:
                            json = await resp.json()
                            if json["status"] == "succeeded":
                                async with session.get(
                                    f"https://images.prodia.xyz/{job_id}.png?download=1",
                                    headers=headers,
                                ) as resp:
                                    return await resp.content.read()
        except ClientError as exc:
            raise ClientError("Unable to fetch the response.") from exc


async def image_callback(CommandObject,message,self,params,command_data):
                            await message.channel.send("Generating please wait")
                            await message.channel.typing()
                            resp = requests.get(f"https://pollinations.ai/p/{message.content.replace('.image','')}?width={700}&height={700}&seed={seed()}")
                            await message.channel.send(f"New Picture generated\n-# Prompt: {message.content}",file=discord.File(BytesIO(resp.content), filename='image.jpg'))
async def imagine_callback(CommandObject,message,self,params,command_data):
                            await message.channel.send("Generating please wait")
                            await message.channel.typing()
                            resp = await image(message_without_command(params))
                            await message.channel.send(f"Image Generation with Prodia\n-# Prompt: {message.content}",file=discord.File(BytesIO(resp), filename='image.jpg'))
image_command = Command("image", 'AI Image Generation!', image_callback, TOOLS, aliases=['picture'],params=["PROMPT"],ispremium=True)
imagine_command = Command("imagine", 'AI Image Generation with Prodia', imagine_callback, TOOLS, aliases=["think","draw"],params=["PROMPT"],ispremium=True)