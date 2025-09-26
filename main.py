import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def announce(ctx, *, message: str):
    embed = discord.Embed(
        title="📢 Announcement",
        description=message,
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"By {ctx.author.display_name}")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    keep_alive()
    bot.run(os.getenv("TOKEN"))
