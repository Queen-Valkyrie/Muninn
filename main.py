import os
import discord
from dotenv import load_dotenv

# Load the environment variables (only works if running locally)
load_dotenv()

# Get the token from the environment variable
bot_token = os.getenv("DISCORD_TOKEN")

# Set up the bot with basic permissions
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content if needed

client = discord.Client(intents=intents)

# Confirm when the bot is online
@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.content == "!hello":
        await message.channel.send("Hello! 👋 I'm here and working!")


# Run the bot using the token
client.run(bot_token)

