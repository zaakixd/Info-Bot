import discord
from discord.ext import commands
import os
from datetime import datetime

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="KK On Low !")
    await bot.change_presence(activity=activity)
    print(f"Logged in as {bot.user}")


@bot.command()
async def info(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)
        member = ctx.guild.get_member(user_id)

        embed = discord.Embed(
            title="Discord User Lookup",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )

        # Avatar
        embed.set_thumbnail(url=user.display_avatar.url)

        # Username
        embed.add_field(name="Username", value=user.name, inline=True)

        # Global name
        embed.add_field(name="Display Name", value=user.global_name, inline=True)

        # Tag
        embed.add_field(name="Tag", value=f"{user}", inline=True)

        # User ID
        embed.add_field(name="User ID", value=user.id, inline=False)

        # Status (only if in server)
        if member:
            embed.add_field(name="Status", value=str(member.status), inline=True)
        else:
            embed.add_field(name="Status", value="Not in this server", inline=True)

        # Avatar link
        embed.add_field(name="Avatar", value=user.display_avatar.url, inline=False)

        # Banner
        if user.banner:
            embed.add_field(name="Banner", value=user.banner.url, inline=False)
            embed.set_image(url=user.banner.url)
        else:
            embed.add_field(name="Banner", value="No banner", inline=False)

        # Nitro guess
        nitro = "Unknown"
        if user.banner or user.display_avatar.is_animated():
            nitro = "Possible"

        embed.add_field(name="Nitro", value=nitro, inline=True)

        embed.add_field(
            name="Profile Link",
            value=f"https://discord.com/users/{user.id}",
            inline=False
        )

        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)

    except:
        await ctx.send("User not found or invalid ID.")


bot.run(TOKEN)
