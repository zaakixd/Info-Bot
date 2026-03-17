import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def info(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)

        embed = discord.Embed(
            title="User Information",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Bot Account", value=user.bot, inline=True)
        embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Avatar", value=user.display_avatar.url, inline=False)

        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send("User not found or invalid ID.")

bot.run(TOKEN)
