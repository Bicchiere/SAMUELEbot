import discord
from discord.ext import *
class SAMUELE(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return
        elif message.author.bot:
            pass
        author_id = str(message.author.id)
        await message.channel.send(f"SAMUELE")

def setup(client):
    client.add_cog(SAMUELE(client))