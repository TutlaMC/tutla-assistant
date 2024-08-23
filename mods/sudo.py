from . import mod

Linux = mod.Mod("Linux","$ sudo apt install tutla-ast-linux-mod")
cdable = ['/home','/home/gyatt.txt',''
          "/yourmom","/yourmom/pics",
          '/private','/private/feetpics',"/private/furry",'/private/furry/vids','/private/passwords.txt',"/private/parts","/private/parts/not_found.txt"]
cdableFiles = {
    '/home/gyatt.txt': "I am weeb",
    "/private/passwords.txt" : "crap forgot em all\n4hn29384hn (Def not a tutla shop coupon code cuz u found dis secret)",
    "/private/parts/not_found.txt": "there are websites for this, why u gotta use me. i got none, its not found, born with none live with none die with none - Tutla Assistance"
}
global cd
cd = "/"
def termify(val): return f"```ansi\n{val}```"
async def terminal(message):
    global cd
    params = message.content.split()
    if len(params) < 1: return False
    if params[0] == "sudo":
        if params[1] == "cd":
            folders = params[2].split('/') if params[2].split('/')[1:] != "" else params[2].split('/')[1:]
            if not folders[len(folders)-1][-4:] in [".htm",".txt",".css",".mp4",".mp3"]:
                file = None
            else: file =  folders[len(folders)-1]
            if params[2] in cdable:
                if file == None:
                    cd = params[2]+'/' if params[2][1:] != '/' else params[2]
                    await message.channel.send(termify(f"$ {cd}"))
                else: await message.channel.send(termify(f"{params[2]} is a file"))
            else:
                await message.channel.send(termify(f"{params[2]} not found"))
        elif params[1] in ["cat","tail"]:
            folders = params[2].split('/') if params[2].split('/')[1:] != "" else params[2].split('/')[1:]
            if folders[len(folders)-1][-4:] in [".htm",".txt",".css",".mp4",".mp3"]:
                    cd = cd
                    e = cd+params[2].replace(cd,"") if cd != "/" else cd+params[2]
                    e = e.replace("//","/")
                    if e in cdableFiles:
                        print(cdableFiles[e])
                        await message.channel.send(termify(cdableFiles[e]))
                    else:
                        await message.channel.send(termify(f"e not found"))
            else:
                await message.channel.send(termify(f"{params[2]} is not a file"))
        elif params[1] == "ls":
            if cd == "/": 
                await message.channel.send(termify("ain mewing"))
                return False
            final = ""
            for i in cdable:
                if cd in i:
                    print(i[-4:])
                    if i[-4:] in [".htm",".txt",".css",".mp4",".mp3"]:
                        final+=i+" "
                    else:
                        final+=f"\u001b[0;33m{i}\u001b[0;0m "
            await message.channel.send(termify(final))
Linux.on_message(terminal)