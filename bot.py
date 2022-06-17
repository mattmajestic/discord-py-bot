# bot.py
import os

import discord
from dotenv import load_dotenv

import nest_asyncio
nest_asyncio.apply()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('discord-bot-example'):
        await message.channel.send(f'We coded this response in Python for you {message.author}')

client.run(TOKEN)