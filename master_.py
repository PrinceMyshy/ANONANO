from cgi import test
import os
import discord
import logging
import random

import asyncio
import collections
import inspect
import importlib.util
import sys
import traceback
import types

import discord

from .core import GroupMixin
from .view import StringView
from .context import Context
from . import errors
from .help import HelpCommand, DefaultHelpCommand
from .cog import Cog


from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('DISCORD_TOKEN')


#import logging 

#logging on
client = discord.Client()


@client.event
async def on_ready():
    print('I am logged in now as {0.user}'.format(client))

#responging to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('halal'):
        await message.channel.send("is pork halal?")
        
    if "haram" in message.content:
        await message.channel.send("abstain from haram!")
        
    if 'banned word' in message.content:
        await message.channel.send("That word is banned!")
    
    if 'what kinda question is that' in message.content:
        await message.channel.send("I honestly don't know! What an idiot.")
        

client = commands.Bot(command_prefix=".")        

@client.command()
async def question(ctx, ask: ctx.message):
    random = ["love", "stop", "no", "hmm... gay", "why?", "is math related to science?"]
    await ctx.send(f"**You asked:** *{ask}* | **and I say**: *{random.choice(random)}*")

@client.command()
async def ship(ctx, member_1: discord.Member, member_2: discord.Member):
    """Ship 2 members"""
    from random import randint
    rate = randint(1, 100)
    await ctx.send(f"""**{member_1}** | :heart: {rate}% :heart: | **{member_2}**""")

                
client.run(token)

'''
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
'''

'''intents = discord.Intents.default()        
client = discord.Client(intents=intents) 
'''
