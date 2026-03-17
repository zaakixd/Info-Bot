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
    activity = discord.Activity(
        type=discord.ActivityType.listening,
        name="KK"
    )
    await bot.change_presence(activity=activity)
    
    print(f"Logged in as {bot.user}")

@bot.command()
async def info(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)

        embed = discord.Embed(
            title="Discord User Info",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(name="Username", value=user.name)
        embed.add_field(name="User ID", value=user.id)
        embed.add_field(name="Bot", value=user.bot)
        embed.add_field(name="Created", value=user.created_at)

        await ctx.send(embed=embed)

    except:
        await ctx.send("User not found.")

bot.run(TOKEN)
