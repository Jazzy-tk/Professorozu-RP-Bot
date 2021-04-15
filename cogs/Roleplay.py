import discord

from discord.ext import commands

class Roleplay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Good morning!', 'good morning!'])
    async def Gm(self, ctx):
        await ctx.send('*Good morning master... How was you sleep?~*')

def setup(client):
    client.add_cog(Roleplay(client))