# coding: utf-8
import os
import json
import aiohttp
import asyncio
import discord
import subprocess
import datetime
from utils import *
from os import system, name
from discord.ext.commands.core import cooldown
from discord import Permissions

from discord.ext import (
    commands,
    tasks
)

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.command()
async def spam_send(ctx, count):
    try:
        with open(spam_text_file, 'r') as spam_text_n:
            spam_text = spam_text_n.read()
        await ctx.send(spam_text.strip('\"'))
    except Exception as e: print(e)

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 848621214935154738:
        client.load_extension(f"cogs {extension}")
        await ctx.send("Cogs loaded!")
    else:
        await ctx.send("You are not a bot developer.")


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 848621214935154738:
        client.unload_extension(f"cogs {extension}")
        await ctx.send("Cogs unloaded!")
    else:
        await ctx.send("You are not a bot developer.")


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 848621214935154738:
        client.unload_extension(f"cogs {extension}")
        client.load_extension(f"cogs {extension}")
        await ctx.send("Cogs reloaded!")
    else:
        await ctx.send("You are not a bot developer.")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(token)