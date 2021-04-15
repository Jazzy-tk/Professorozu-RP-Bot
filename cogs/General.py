import discord

from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('At your service!')

    @commands.command()
    async def Works(self, ctx):
        await ctx.send('Worked!')

def setup(client):
    client.add_cog(General(client))