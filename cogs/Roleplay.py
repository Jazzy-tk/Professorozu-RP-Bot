import discord

from discord.ext import commands

import random

class Roleplay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Good'])
    async def Greeting(self, ctx, *context):
    async def on_message(message):
    
        if message.content.includes('Morning'):
            await ctx.send('good morning!')

        if message.contains(['evening', 'evening!', 'evening.']):
            await ctx.send('Good evening!')

def setup(client):
    client.add_cog(Roleplay(client))