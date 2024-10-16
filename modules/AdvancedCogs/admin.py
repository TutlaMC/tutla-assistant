from ..Module import * 
import datetime

#from ..Utils import * #import this if you need utility commands

def convert_time(time_str: str) -> datetime.timedelta:
    unit = time_str[-1]
    time_value = int(time_str[:-1])
    
    if unit == 's':
        return datetime.timedelta(seconds=time_value)
    elif unit == 'm':
        return datetime.timedelta(minutes=time_value)
    elif unit == 'h':
        return datetime.timedelta(hours=time_value)
    elif unit == 'd':
        return datetime.timedelta(days=time_value)
    else:
        raise ValueError("Invalid time format. Use 's' for seconds, 'm' for minutes, 'h' for hours, or 'd' for days.")

class AdminGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    group = app_commands.Group(name="admin", description="Admin Level Commands")
    cgroup = app_commands.Group(name="create", description="Create channels")

    @group.command(name="kick",description="Kick a user")
    @commands.has_permissions(kick_members=True)
    @app_commands.check(commandCheck)
    async def kick_callback(self, ctx: discord.Interaction, user:discord.Member, reason:str):
        if user.top_role >= ctx.user.top_role: await ctx.response.send_message("You cannot permof this action to the specified user because the users role is heigher than yours"); return False
        if not ctx.user.guild_permissions.kick_members: 
            await ctx.response.send_message("You cannot execute this!",ephemeral=True)
            return False
        try:
            if reason!=None: await user.kick()
            else: await user.kick(reason=reason)
            await ctx.response.send_message(f'Successfully kicked {user.mention}')
        except Exception as e: await ctx.response.send_message('I do not have permission to kick users')

    @group.command(name="ban",description="Ban a user")
    @commands.has_permissions(ban_members=True)
    @app_commands.check(commandCheck)
    async def ban_callback(self, ctx: discord.Interaction, user: discord.Member, reason: str=None):
        if user.top_role >= ctx.user.top_role: await ctx.response.send_message("You cannot perfom this action to the specified user because the users role is heigher than yours"); return False
        if ctx.user.guild_permissions.ban_members:
            try:
                if reason!=None: await user.ban()
                else: await user.ban(reason=reason)
                await ctx.response.send_message(f'Successfully banned {user.mention}')
            except Exception as e: 
                print(e)
                await ctx.response.send_message('I do not have permission to ban users')
        else:await ctx.response.send_message(f'You do not have permission to ban users')

    
    @group.command(name="purge", description="Delete messages in bulk")
    @app_commands.check(commandCheck)
    async def purge(self, interaction: discord.Interaction, amount: int,  skip_user: discord.User = None, focus_user: discord.User = None, after: int = 0):
        if not interaction.user.guild_permissions.manage_messages: await interaction.response.send_message("You cannot execute this!",ephemeral=True); return False
        def check(message):
            if skip_user and message.author == skip_user:
                return False
            if focus_user and message.author != focus_user:
                return False
            return True

        await interaction.response.send_message(f'Deleting {str(amount)} messages.', ephemeral=True)

        after_message = None
        if after > 0:
            messages = await interaction.channel.history(limit=after).flatten()
            if messages:
                after_message = messages[-1]  

        deleted = await interaction.channel.purge(limit=amount, check=check, after=after_message)
        
        await interaction.followup.send(f'Deleted {len(deleted)} messages.', ephemeral=True)


    @group.command(name="role",description="Give a user a role")
    @app_commands.check(commandCheck)
    async def role_callback(self, ctx: discord.Interaction, user: discord.Member, role: discord.Role):
            if user.top_role >= ctx.user.top_role: await ctx.response.send_message("You cannot perfom this action to the specified user because the users role is heigher than yours"); return False
            if not ctx.user.guild_permissions.manage_roles: 
                await ctx.response.send_message("You cannot execute this!",ephemeral=True)
                return False
            try:
                await user.add_roles(role)
                await ctx.response.send_message('Added roles to user')
            except Exception as e:
                await ctx.response.send_message(f'I do not have permission to add roles to members, error log:```python\n{e}```')

    @group.command(name="timeout",description="Times out the user")
    @app_commands.check(commandCheck)
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, duration: str, reason: str = None):
        if not interaction.user.guild_permissions.moderate_members: await interaction.response.send_message("You cannot execute this!",ephemeral=True); return False
        if member.top_role >= interaction.user.top_role: await interaction.response.send_message("You cannot perfom this action to the specified user because the users role is heigher than yours"); return False
        if not interaction.guild.me.guild_permissions.moderate_members:
            await interaction.response.send_message("I don't have permission to timeout members.", ephemeral=True)
            return
        try:
            timeout_duration = convert_time(duration)
        except ValueError as e:
            await interaction.response.send_message(str(e), ephemeral=True)
            return
        print("weeb")
        await member.timeout(timeout_duration, reason=reason)
        await interaction.response.send_message(f"{member.mention} has been timed out for {duration}.")

    @group.command(name="delete", description="Delete something")
    @commands.has_permissions(manage_channels=True)
    async def delete_callback(self, interaction: discord.Interaction, text_channel:discord.TextChannel=None, voice_channel:discord.VoiceChannel=None, forum:discord.ForumChannel=None,role:discord.Role=None):
        if not interaction.user.guild_permissions.manage_channels: 
                await interaction.response.send_message("You cannot execute this!",ephemeral=True)
                return False
        
        if not interaction.guild.me.guild_permissions.manage_channels:
                await interaction.response.send_message("I don't have permission to manage channels.", ephemeral=True)
                return

        if text_channel:
            await text_channel.delete()
        elif voice_channel:
            await voice_channel.delete()
        elif forum:
            await forum.delete()
        elif role:
            await role.delete()
        else: 
            await interaction.response.send_message("Spcify a parameter to delete!",ephemeral=True)
            return False
        await interaction.response.send_message("Successfully deleted!")


    @cgroup.command(name="textchannel", description="Create a text channel")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(
        name="Name of the channel",
        emoji="Emoji to prepend to the channel name",
        separator="Separator between emoji and name",
        see_role="Roles that can access the text channel",
        blocked_role="Roles that cannot access the text channel",
        messages_role = "Can send messages",
        no_messages_role = "Cannot send messages"
    )
    async def create_text(self, interaction: discord.Interaction, name: str, emoji: str = None, separator: str = '｜', see_role: discord.Role = None, blocked_role: discord.Role = None, messages_role: discord.Role = None, no_messages_role: discord.Role = None):
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channels.", ephemeral=True)
            return
        if not interaction.user.guild_permissions.manage_channels: 
            await interaction.response.send_message("You cannot execute this!",ephemeral=True)
            return False
        await interaction.response.send_message("Creating Channel...",ephemeral=True)

        if emoji:
            name = f"{emoji}{separator}{name}"

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False)
        }

        if see_role:
                overwrites[see_role] = discord.PermissionOverwrite(read_messages=True)

        if blocked_role:
                overwrites[blocked_role] = discord.PermissionOverwrite(read_messages=False)

        if messages_role:
                overwrites[messages_role] = discord.PermissionOverwrite(send_messages=True)

        if no_messages_role:
                overwrites[no_messages_role] = discord.PermissionOverwrite(send_messages=False)

        channel = await interaction.guild.create_text_channel(name, overwrites=overwrites)
        await interaction.followup.send(f"Text channel {channel.mention} created.")



    @cgroup.command(name="category", description="Create a category")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(
        name="Name of the category",
        emoji="Emoji to prepend to the category name",
        separator="Separator between emoji and name",
        see_role="Roles that can access the category",
        blocked_role="Roles that cannot access the category",
        messages_role = "Can send messages",
        no_messages_role = "Cannot send messages"
    )
    async def create_category(self, interaction: discord.Interaction, name: str, emoji: str = None, separator: str = '｜', see_role: discord.Role = None, blocked_role: discord.Role = None, messages_role: discord.Role = None, no_messages_role: discord.Role = None):
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channels.", ephemeral=True)
            return
        if not interaction.user.guild_permissions.manage_channels: 
            await interaction.response.send_message("You cannot execute this!",ephemeral=True)
            return False
        await interaction.response.send_message("Creating Channel...",ephemeral=True)

        if emoji:
            name = f"{emoji}{separator}{name}"

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False)
        }

        if see_role:
                overwrites[see_role] = discord.PermissionOverwrite(read_messages=True)

        if blocked_role:
                overwrites[blocked_role] = discord.PermissionOverwrite(read_messages=False)

        if messages_role:
                overwrites[messages_role] = discord.PermissionOverwrite(send_messages=True)

        if no_messages_role:
                overwrites[no_messages_role] = discord.PermissionOverwrite(send_messages=False)

        category = await interaction.guild.create_category(name, overwrites=overwrites)
        await interaction.followup.send(f"Category {category.name} created.")




    @cgroup.command(name="voicechannel", description="Create a voice channel")
    @commands.has_permissions(manage_channels=True)
    @app_commands.describe(
        name="Name of the channel",
        emoji="Emoji to prepend to the channel name",
        separator="Separator between emoji and name"
    )
    async def create_voice(self, interaction: discord.Interaction, name: str, emoji: str = None, separator: str = '｜'):
        if not interaction.user.guild_permissions.manage_channels: 
            await interaction.response.send_message("You cannot execute this!",ephemeral=True)
            return False
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channels.", ephemeral=True)
            return

        if emoji:
            name = f"{emoji} {separator} {name}"

        channel = await interaction.guild.create_voice_channel(name)
        await interaction.response.send_message(f"Voice channel {channel.mention} created.")




    @cgroup.command(name="emoji", description="Create an emoji/sticker")
    @app_commands.describe(
        name="Name of emoji",
        emoji="Emoji file"
    )
    async def create_emoji(self, interaction: discord.Interaction, name: str, emoji: discord.Attachment,sticker:bool=False, description:str="",sticker_emoji:str=""):
        if not interaction.user.guild_permissions.manage_emojis_and_stickers: 
                await interaction.response.send_message("You cannot execute this!",ephemeral=True)
                return False
        if not interaction.guild.me.guild_permissions.manage_emojis_and_stickers:
                await interaction.response.send_message("I don't have permission to manage expressions.", ephemeral=True)
                return
        if not sticker:
            

            moji = await interaction.guild.create_custom_emoji(name=name,image=await emoji.read())
            await interaction.response.send_message(f"Emoji <:{moji.name}:{moji.id}> created.")
        else:
            if not description or sticker_emoji:
                await interaction.response.send_message("Sticker creation requires `description` (desc for sticker) and `sticker_emoji` (emoji related to the sticker).")
            else:
                moji = await interaction.guild.create_sticker(name=name,file=await emoji.read(),description=description,emoji=sticker_emoji)
                await interaction.response.send_message(f"Sticker created created.")

async def setup(bot: commands.Bot):
    await bot.add_cog(AdminGroup(bot))
