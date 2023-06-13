# coding: utf-8
import os

try:
    import json
except:
    os.system('pip install json')
    import json
try:
    import aiohttp
except:
    os.system('pip install aiohttp')
    import aiohttp
try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio
try:
    import discord
except:
    os.system('pip install discord.py==1.7.3')
    import discord
try:
    import subprocess
except:
    os.system('pip install subprocess')
    import subprocess
try:
    import datetime
except:
    os.system('pip install datetime')
    import datetime

'''
import json
import aiohttp
import asyncio
import discord
import datetime
import subprocess
'''
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


def token_check():
    with open("json/config.json") as f:
        config = json.load(f)
    token = config.get("token")
    try:
        client.run(token)
    except Exception as e: 
        print(e)
        while True:
            token = input(f"{r}[X] {wh}Enter token your bot: ")
            #config["token"] = token
            #with open("json/config.json", "w") as f:
            #    json.dump(config, f)
            try:
                client.run(token)
                break
            except Exception as e: 
                print(e)


@client.command()
async def load(ctx, extension):
    if ctx.author.id in developer_list:
        client.load_extension(f"cogs {extension}")
        await ctx.send("Cogs loaded!")
    else:
        await ctx.send("You are not a bot developer.")


@client.command()
async def unload(ctx, extension):
    if ctx.author.id in developer_list:
        client.unload_extension(f"cogs {extension}")
        await ctx.send("Cogs unloaded!")
    else:
        await ctx.send("You are not a bot developer.")


@client.command()
async def reload(ctx, extension):
    if ctx.author.id in developer_list:
        client.unload_extension(f"cogs {extension}")
        client.load_extension(f"cogs {extension}")
        await ctx.send("Cogs reloaded!")
    else:
        await ctx.send("You are not a bot developer.")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

token_check()
