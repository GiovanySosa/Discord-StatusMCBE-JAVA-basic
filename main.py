import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from mcstats import mcstats

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.command()
async def status(ctx):
    host = "yourip or subdomain"
    port = 19132  #yourport
    with mcstats(host, port=port, timeout=5) as data:
        online = data.num_players
        max = data.max_players
        status = discord.Embed(title=f"**ip:**{host}  **Puerto:** {port}", description=f"**conectados:** {online} **de:** {max}", color=discord.Color.random())
        await ctx.send(embed=status)




bot.run(TOKEN)
