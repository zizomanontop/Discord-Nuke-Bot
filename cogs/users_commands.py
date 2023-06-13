# coding: utf-8
import os
import time

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
import subprocess
import datetime
'''

from utils import *
from os import system, name
from discord.ext.commands.core import cooldown
from discord import Permissions

from discord.ext import (
    commands,
    tasks
)


class User(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['kick_a', 'k_all', 'k_l'])
    @commands.check(black_check)
    @commands.check(white_check)
    @commands.cooldown(1, command_cooldown_time, commands.BucketType.user)
    async def kick_all(self, ctx):
        try:
            await ctx.message.delete()

            for m in ctx.guild.members:
                try:
                    await m.kick()
                except:
                    continue
        except Exception as e: print(e)


    @commands.command(aliases=['ban_a', 'b_all', 'b_l'])
    @commands.check(black_check)
    @commands.check(white_check)
    @commands.cooldown(1, command_cooldown_time, commands.BucketType.user)
    async def ban_all(self, ctx):
        try:
            await ctx.message.delete()

            for member in ctx.guild.members:
                try:
                    await member.ban()
                except:
                    continue
        except Exception as e: print(e)


def setup(client):
    client.add_cog(User(client))