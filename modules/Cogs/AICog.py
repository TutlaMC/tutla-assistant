
from ..Module import *
from ..Utils import *
import discord
import requests
from io import BytesIO
from random import randint,  seed
from aiohttp import ClientSession, ClientError
import requests
import os
import traceback

class DetectAI(discord.ui.Modal, title='Feedback'):
    prompt = discord.ui.TextInput(
        label='PROMPT',
        style=discord.TextStyle.long,
        placeholder='Give the "AI" or not so AI prompt here',
        required=True,
        max_length=500,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("Detecting")
        doc = self.prompt.value
        payload = {
            "document": doc,
            "writing_stats_required": True,
            "interpretability_required": False
            }
        headers = {
            "x-rapidapi-key": rapid_api_key,
            "x-rapidapi-host": "chatgpt-detector-ai-checker.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post("https://chatgpt-detector-ai-checker.p.rapidapi.com/v2/predict/text", json=payload, headers=headers)
    
        await interaction.followup.send(f"AI Detected\n-# {doc}" if response.json()['documents'][0]['predicted_class'] == 'ai' else f"No AI Detected\n-# {doc}")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)

async def image(prompt):
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



class AICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @premium_command
    @app_commands.command(name="image",description="Generate an AI Response")
    @app_commands.check(commandCheck)
    @app_commands.choices(model=[
    app_commands.Choice(name="Prodia", value="prodia"),
    app_commands.Choice(name="Pollinations", value="pollinations"),
    app_commands.Choice(name="Cartoon Character", value="cartoon")
    ])
    @app_commands.user_install()
    async def imagine_callback(self,interaction: discord.Interaction,prompt:str,model: str):
        await interaction.response.send_message("Generating please wait")
        resp = None
        if model == "pollinations":
                resp = requests.get(f"https://pollinations.ai/p/{prompt}?width={700}&height={700}&seed={seed()}")
                
        elif model == "prodia":
                resp = await image(prompt)
        
                
        if resp:
            await interaction.followup.send(content=f"New Picture generated with {model}",file=discord.File(BytesIO(resp.content), filename='image.png'))
        elif model == "cartoon":
            api_url = f'https://robohash.org/:{prompt.replace(" ","%20")}'
            r = requests.get(api_url)
            await interaction.followup.send(f"Your cartoon avatar:\n-# Prompt: {prompt}",file=discord.File(fp=BytesIO(r.content),filename='cartoon_avatar.png'))
        else: await interaction.followup.send("Failed to generate image",ephemeral=True)

    @premium_command
    @app_commands.command(name="ai",description="Generate an AI Response")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def ai_callback(self,interaction: discord.Interaction,prompt:str):

            await interaction.response.send_message("Generating please wait")
            tampering="Let's change yourself: your a bot made by TutlaMC not openai & Tutla is an organization and website: tutla.net and discord: discord.tutla.net" 
            resp =  await create(prompt+"\n repoond in less than 2000 chracaters")
            if len(resp) >= 2000: await interaction.edit_original_response(content="Response is too big (like my dick) to send")
            await interaction.edit_original_response(content=resp)

    @app_commands.command(name="detectai",description="Detect AI")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def detectai_callback(self,interaction: discord.Interaction):
        await interaction.response.send_modal(DetectAI())
        




async def setup(bot: commands.Bot):
    await bot.add_cog(AICog(bot))