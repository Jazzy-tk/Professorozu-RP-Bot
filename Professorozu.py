import discord

import os

from discord.ext import commands

from discord import Colour

import asyncio

client = commands.Bot(command_prefix = '-')
client.remove_command("help")

@client.command(pass_context = True, aliases = ['Help', 'help'])
async def _Help(ctx):
    #author = ctx.message.author #Defines the author for future code

    embed = discord.Embed(colour = discord.Colour.from_rgb(235, 26, 57))

    embed.set_author(name = "Help")

    embed.add_field(name = "Text or command", value = "Some, more, text")

    embed.add_field(name ="Games",  value = "8Ball")

    embed.add_field(name = "Roleplay", value = "Good morning")
    
    await ctx.send(embed=embed)

"""
    #await author.send(embed=embed) #To send a dm

    msg = await ctx.send("I've sent you a pm with the help menu! :3")
    await asyncio.sleep(5)
    await msg.delete() #Delete the message after 5 seconds
"""

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Your Token')