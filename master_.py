import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('haram'):
        await message.channel.send("abstain from haram!")
        

client.run('OTY3OTMwMjAzNzk4MTE4NDQx.YmXdPw.g9xyKrJdurqk74w-p3T4oNXDHeQ')
