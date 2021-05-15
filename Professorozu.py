import discord

import os

from discord import message

from discord.ext import commands

#import asyncio

client = commands.Bot(command_prefix = '-')
client.remove_command("help")

@client.command(pass_context = True, aliases = ['Help', 'help'])
async def _Help(ctx):
    #author = ctx.message.author #Defines the author for future code

    embed = discord.Embed(colour = discord.Colour.from_rgb(235, 26, 57), 
    title = "This is the title", 
    description = "Description of the title"
    )

    embed.set_author(name = "Jazzy",
    icon_url = "https://cdn.discordapp.com/attachments/832271440769449994/843121612454887474/355c04882628d11a068a2fbdb3d5c2d8.png"
    )

    embed.add_field(name = "Field 1", value = "Field 1 Thing")

    embed.add_field(name ="Field 2",  value = "Field 2 Thing")

    embed.add_field(name = "Field 3", value = "Field 3 thing")

    """
    #await author.send(embed=embed) #To send a dm

    msg = await ctx.send("I've sent you a pm with the help menu! :3")
    await asyncio.sleep(5)
    await msg.delete() #Delete the message after 5 seconds
    """
    message = await ctx.send(embed=embed)
    
    heart_yellow = "💛"
    heart_red = "❤️"
    heart_orange = "🧡"

    await message.add_reaction(heart_red)
    await message.add_reaction(heart_yellow)
    await message.add_reaction(heart_orange)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Token')