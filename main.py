import discord
from discord.ext import commands

TOKEN = "MTQ4MzUwMjU0NTk2NzI1MTYyNw.GhwMIQ.yOTZT2sAL-b4qb0j1CpJwBU7PfSk49nwSyjs7E"

intents = discord.Intents.default()
intents.members = True
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

        embed.add_field(name="Username", value=f"{user.name}#{user.discriminator}", inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Bot", value=user.bot, inline=True)
        embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Avatar URL", value=user.display_avatar.url, inline=False)

        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)

    except:
        await ctx.send("User not found or invalid ID.")

bot.run(TOKEN)