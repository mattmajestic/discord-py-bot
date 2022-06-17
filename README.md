# discord-py-bot
A Discord Bot using the discord py package

## Bot Specifications:
- Confirm you are logged into the right server
- Send a message when someone says **discord-bot-example**

```python
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
```