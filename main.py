# Import necessary libraries
from dotenv import load_dotenv
import os
import discord

# Load the .env file
load_dotenv()

# Get the token from the .env file
bot_token = os.getenv("DISCORD_TOKEN")

# Initialize the bot client
intents = discord.Intents.default()
intents.message_content = True  # Enable permissions for reading messages
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

# Run the bot
client.run(bot_token)
