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

    @commands.command()
    async def ping(self, ctx, member : discord.Member):
        await ctx.send(f"I ping you, {member}")

    @commands.command(aliases=['print', 'Print'])
    async def _Print(self, ctx):

        x = ctx.message.content
        x = x.lower()

        await ctx.send("Now it's in lowercase")
        await ctx.send(x)

def setup(client):
    client.add_cog(General(client))