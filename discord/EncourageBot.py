import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello2'):
        await message.channel.send('Hello!')

client.run('ODA2MzM0MzM5MzM0Nzk5NDEw.YBn7Xw.FVPlbRmUfl9EeAKzJPqLXeFrMZQ')