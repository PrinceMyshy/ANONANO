from cgi import test
import os
import discord

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('DISCORD_TOKEN')


#import logging

#logging on
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
                
client.run(token)

#logs
'''
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
'''