import types
import discord
from cgi import test
import os
import logging
import random
from discord.ext import commands
from dotenv import load_dotenv
from discord import Embed

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

######################################################################################################################################

####################################################################################################
                                      # Replying to Messages #
####################################################################################################

#logging on
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready(self):
    print(f'I am now logged in as {self.user} (ID: {self.user.id})')
    print('------')
        
async def on_message(self, message):
    if message.author.id == self.user.id:
        return

#############################################
                # Messages #
#############################################

    if message.content.startswith('!hello'):
        await message.reply('Hello!', mention_author=True)

    if message.content.startswith('halal'):
        await message.channel.send("is pork halal?")
            
    if "haram" in message.content:
        await message.channel.send("abstain from haram!")
            
    if 'banned word' in message.content:
        await message.channel.send("That word is banned!")
        
    if 'what kinda question is that' in message.content:
        await message.channel.send("I honestly don't know! What an idiot.")
        
             
####################################################################################################
                                            # COMMANDS #
####################################################################################################
   

client = commands.Bot(command_prefix=".")        

@client.command()
async def question(ctx, arg):
    random = ["love", "stop", "no", "hmm... gay", "why?", "is math related to science?"]
    await ctx.send(f"**You asked:** *{arg}* | **and I say**: *{random.choice(random)}*")

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
