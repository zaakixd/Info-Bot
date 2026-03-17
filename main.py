import discord
from discord.ext import commands
import os
from datetime import datetime

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="KK On lowwW !")
    await bot.change_presence(activity=activity)
    print(f"Logged in as {bot.user}")


@bot.command()
async def info(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)

        embed = discord.Embed(
            title="User Information",
            color=discord.Color.from_rgb(255,255,255),  # white border
            timestamp=datetime.utcnow()
        )

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(
            name="Username",
            value=user.name,
            inline=True
        )

        embed.add_field(
            name="Display Name",
            value=user.global_name if user.global_name else "None",
            inline=True
        )

        embed.add_field(
            name="User ID",
            value=user.id,
            inline=False
        )

        embed.add_field(
            name="Account Created",
            value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            inline=False
        )

        embed.add_field(
            name="Profile Picture",
            value=user.display_avatar.url,
            inline=False
        )

        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)

    except:
        await ctx.send("Invalid user ID or user not found.")


bot.run(TOKEN)
