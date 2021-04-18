import discord

from discord.ext import commands

import random

class Roleplay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='Good')
    async def Gm(self, ctx, *, context):
        context = ['morning Professorozu!',
                'morning professorozu! how are you?']
        responses = ['Good morning master... How was your sleep?',
                'Good morning master... My sleep was very bad...',
                'Good morning master! Are we up for programming today?']

        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(Roleplay(client))