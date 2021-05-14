import discord

from discord.ext import commands

import random

class Roleplay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['good', 'Good'])
    async def Good_morning(self, ctx):

        MessageContent = ctx.message.content
        MessageContent = MessageContent.lower()

        responses = ['I think something went wrong with the code...',
            'Are you sure you know what you are doing?',
            'Failed. Again. How original',
            'I believe in you. Kind of',
            'My my, this is difficult is it not?',
            'My father did better than you. Wait, you are my father',
            'Soon, soon you should be done',
            'Pathetic.',
            'It is so easy to code, but you still fail at it',
            'I will stop bullying you, for now. Of course I am joking! I will never stop bullying you!',
            'Can you just get done and write more code? This is so tedious.',
            'Faaaaaster, this is so boring!',
            'Stonie: *Makes 20 lines of code that works* meanwhile Jazzy: *Spends 3 days on 1 line of code that does not work*',
            'Programmers be like: Ohno, it did not work',
            'Brain power? Hah, you do not have it',
            'XXXtentacle']

        if 'morning' and 'how' and 'was' in MessageContent:
            await ctx.send('My morning was good... As usual. Now what are we up for today?')

        elif 'morning' and 'how' in MessageContent:
            await ctx.send('Good morning to you too! I am good. How are you?')

        elif 'morning' in MessageContent:
            await ctx.send('Good... morning?')

        else:
            await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(Roleplay(client))