import discord

import os

from discord import message

import asyncio

from discord.ext import commands

import random

from Token import *

client = commands.Bot(command_prefix = '£', activity = discord.Game(name = "I'm alive!"))
client.remove_command("help")

@client.event
async def on_ready():

    while True:
        await asyncio.sleep(60)

        Activities = ["UwU",
        "OwO",
        "At your service!",
        ">.>",
        ":3",
        "O-O",
        "^^"
        "._.",
        "<3",
        "T-T",
        "?-?"]

        await client.change_presence(activity = discord.Game(name = f'{random.choice(Activities)}'))

@client.event
async def on_message(message):

    if message.author.id == 515629373567664138: #Aka Gabriel
        await message.delete()

        print(message.content)

        responses = ["Naaah",
        "You shall not text!",
        "I said no!",
        "Message deleted",
        "Cry about it",
        "This is Dark Souls rl",
        "Shhhhhhhh child. Silence",
        "Are you still trying?",
        "Oh did you ask tell me to stop? Well, I can't see the message :3"]

        await message.channel.send(f'{random.choice(responses)}', delete_after = 2)

@client.command(pass_context = True, aliases = ['Help', 'help'])
async def _Help(ctx):
    #author = ctx.message.author #Defines the author for future code

    embed = discord.Embed(colour = discord.Colour.from_rgb(0, 0, 0), 
    title = "This is the title", 
    description = "Description of the title"
    )

    embed.set_author(name = "Jazzy",
    icon_url = "https://cdn.discordapp.com/attachments/832271440769449994/843121612454887474/355c04882628d11a068a2fbdb3d5c2d8.png"
    )

    embed.add_field(name = "Field 1", value = "Field 1 Thing")

    embed.add_field(name ="Field 2",  value = "Field 2 Thing")

    embed.add_field(name = "Field 3", value = "Field 3 thing")

    message = await ctx.send(embed=embed)
    
    heart_yellow = "💛"
    heart_red = "❤️"
    heart_orange = "🧡"
    heart_black = "🖤"
    heart_white = "🤍"

    await message.add_reaction(heart_yellow)
    await message.add_reaction(heart_orange)
    await message.add_reaction(heart_red) 
    await message.add_reaction(heart_black)
    await message.add_reaction(heart_white)

    @client.event
    async def on_reaction_add(reaction, user):

        if user == client.user:
            return

        no_rgb = ctx.message.content

        no_rgb = no_rgb.replace("£help", " ")

        Yellow_embed = discord.Embed(title="Yellow embed",
        colour = discord.Colour.from_rgb(252, 236, 3)
        )

        Yellow_embed.add_field(name="Return", value="react with 🖤 to reset the help message")

        if reaction.emoji == heart_yellow:
            await message.edit(embed = Yellow_embed)
            await message.remove_reaction(heart_yellow, user)

        Orange_embed = discord.Embed(title="Ornage embed",
        colour = discord.Colour.from_rgb(255, 132, 0)
        )

        Orange_embed.add_field(name="Return", value="react with 🖤 to reset the help message")

        if reaction.emoji == heart_orange:
            await message.edit(embed = Orange_embed)
            await message.remove_reaction(heart_orange, user)

        Red_embed = discord.Embed(title="Red embed",
        colour = discord.Colour.from_rgb(255, 0, 60)
        )

        Red_embed.add_field(name="Return", value="react with 🖤 to reset the help message")

        if reaction.emoji == heart_red:
            await message.edit(embed = Red_embed)
            await message.remove_reaction(heart_red, user)
        
        if reaction.emoji == heart_black:
            await message.edit(embed=embed)
            await message.remove_reaction(heart_black, user)
            
        if reaction.emoji == heart_white and no_rgb.isspace() == True:
            error_white = discord.Embed(colour = discord.Colour.from_rgb(252, 3, 28),
            title = "Error. Either there is no RGB code or it's written wrong",
            description = "It has to be written with 3 numbers, a comma and white space in between and numbers that go up to 255"
            )
            error_white.add_field(name = "For example", value = "-help 234, 54, 54")
            error_white.add_field(name="Return", value="react with 🖤 to reset the help message")
            await message.edit(embed = error_white)
            await message.remove_reaction(heart_white, user)

        if reaction.emoji == heart_white:

            color = ctx.message.content

            color = color.replace("£help ", "")

            color = color.replace(" ", "")

            color = color.split(",")

            color = [int(i) for i in color]

            r, g, b = color

            White_embed = discord.Embed(title="Your color embed",
            colour = discord.Colour.from_rgb(r, g, b)
            )

            await message.edit(embed = White_embed)
            await message.remove_reaction(heart_white, user)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)