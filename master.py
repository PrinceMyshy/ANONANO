import discord

client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('OTY3OTMwMjAzNzk4MTE4NDQx.YmXdPw.9mBQqJjqo5N0RdHc6i86CdTApNw')
