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

client = discord.Client()
intents = discord.Intents.all()

bot = commands.Bot(command_prefix = ".")

######################################################################################################################################

####################################################################################################
                                      # Replying to Messages #
####################################################################################################

#logging on

@client.event
async def on_ready():
    print('------')
    print('I am now logged in as {0.user}'.format(client))
    print('------')
     
async def on_message(message):
    if message.author == client.user:
        return

#############################################
                # Messages #
#############################################

    elif message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('halal'):
        await message.channel.send("is pork halal?")
            
    elif "haram" in message.content:
        await message.channel.send("abstain from haram!")
            
    elif 'banned word' in message.content:
        await message.channel.send("That word is banned!")
        
    elif 'what kinda question is that' in message.content:
        await message.channel.send("I honestly don't know! What an idiot!")

    await bot.process_commands(message)

####################################################################################################
                                            # COMMANDS #
####################################################################################################

  
client = discord.Client(intents=intents)  
        

@bot.command()
async def question(ctx, arg):
    random = ["love", "stop", "no", "hmm... gay", "why?", "is math related to science?"]
    await ctx.send(f"**You asked:** *{arg}* | **and I say**: *{random.choice(random)}*")

@bot.command()
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
