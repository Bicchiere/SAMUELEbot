import discord
from discord.ext import commands
import os
client = commands.Bot(command_prefix = "p!")
client.remove_command("help")


@client.event
async def on_ready():
            print("SAMUELE")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("TOKEN QUA")