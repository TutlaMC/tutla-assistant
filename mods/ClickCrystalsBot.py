from . import mod
import asyncio
ClickCrystalsMod = mod.Mod("ClickCrystals","ClickCrystals Mod")

 
async def recieve_message(message):
   params = message.content.split()
   if len(params) < 2 and message.content.startswith(",help"):
      
      await message.channel.send(f"""> {message.author.mention} ClickCrystalsBot help commands:
> - `rat`
> - `menu`
> - `reload`
> - `wiki`/`ccs`
> - `get`/`download`
> - `crash`""")
   else:
      if not message.content.startswith(",help"): return False
      if params[1] in ["wiki","ccs"]:
         await message.channel.send(f"""> {message.author.mention} Here's a full CCS tutorial:
Wiki: https://bit.ly/ccs-wiki

Content:
- Downloading and installing ClickCrystals
- Locating the .minecraft folder, and the .clickcrystals folder
- Reloading your scripts or the entire client
- Writing and running your own scripts

Your script ain working?

- After opening the editor and pasting your script click "Save and Reload" on the left pane of the CCS Editor
- Type in `,reload` and `,ccs reload` into chat
- If it still doesn't work (if you see an error in chat) use an updated script @ https://clickcrysatls.xyz/scripts or try to fix it on your own
- After all of this it doesn't work contact a CCS Scripter or a Helper
""")
      elif params[1] == "rat":
         await message.channel.send(f"""> {message.author.mention}> ClickCrystals is not a rat. The downloads here, Modrinth, PlanetMC, Github, and [Our Site](https://itzispyder.github.io/clickcrystals) are entirely safe to download! Be sure not to get ClickCrystals from any site other than the ones listed here, there are a lot of fake copies of ClickCrystals out there, so stay safe!
> 
> Read [this](https://itzispyder.github.io/clickcrystals/wiki) for more info!""")
      elif params[1] == "reload":
         await message.channel.send("""To add and reload scripts in your ClickCrystals Client:

1) Type `,folder` in chat - file explorer should open
2) Open the folder `scripts`
3) Create new `.txt` file
4) Paste script

Need pre-made scripts? https://clickcrystals.xyz/scripts

5) Save file and go back in game
6) Type `,reload` in chat

When you see the message "Reloaded ClickCrystals Client!" open up your Custom Made screen and enable the newly added module.
*Please note that the default command prefix is a comma not a period*""")
      elif params[1] == "menu":
         await message.channel.send(f"""> {message.author.mention} To open the ClickCrystals GUI menu on 1.20.x , press the apostrophe `'` key. If you wish to bind this key to something else, execute the command `,keybinds` with a comma. If you are still on 1.19.x, just update your game. :update:
> 
> Read [this](https://itzispyder.github.io/clickcrystals/wiki) for more info!""")
      elif params[1] in ["get","download","install"]:
         await message.channel.send("""> Official Download Sites\n- [Official Website](https://clickcrystals.xyz/download)\n- [Github](<https://github.com/clickcrystals-development/ClickCrystals/releases>)\n- [CurseForge](<https://www.curseforge.com/minecraft/mc-mods/clickcrystals>)\n- [PlanetMC](<https://www.planetminecraft.com/mod/clickcrystal/>)\n- [Modrinth (Deprecated)](<https://modrinth.com/mod/clickcrystals>)\n\n- [Instant Download Latest Version](https://clickcrystals.xyz/get)""")
      elif params[1] in ["crash"]:
         await message.channel.send("ClickCrystals Crashed? Solutions:\n- Update MC & CC to Latest\n- Make sure your MC version is compatible with CC\n- Is [Fabric API](<https://modrinth.com/mod/fabric-api/>) is installed?\n- Read our [FAQ](<https://clickcrystals.xyz/help>)\n- May be incompatible with other mods, try a different modpack\n- Reinstall ClickCrystals from an Official Source\n\n If none of these work, contact a mod **with your crash report**")
      else: await message.channel.send("Incorrect Usage")
ClickCrystalsMod.on_message(recieve_message)