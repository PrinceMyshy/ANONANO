from http import client
from discord import Client
import nextcord
from nextcord import interactions
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.BOT(command_prefix = '!', intents = intents) 

@client.event
async def on_ready():
    print("The bot is now ready for use")
    

client.run('')