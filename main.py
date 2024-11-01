import os
import discord
from dotenv import load_dotenv


# Emoji to language code mapping
emoji_to_language = {
    '🇪🇸': 'ES',  # Spanish
    '🇫🇷': 'FR',  # French
    '🇩🇪': 'DE',  # German
    '🇮🇹': 'IT',  # Italian
    '🇳🇱': 'NL',  # Dutch
    '🇧🇷': 'PT',  # Portuguese
}


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
async def on_reaction_add(reaction, user):
    # Check if the emoji is in our dictionary and is not from the bot itself
    if str(reaction.emoji) in emoji_to_language and user != client.user:
        # Get the language code based on the emoji
        target_language = emoji_to_language[str(reaction.emoji)]
        
        # Get the original message content to translate
        original_text = reaction.message.content
        
        # Call a function to translate the text
        translated_text = translate_text(original_text, target_language)
        
        # Send the translated message with auto-delete after 10 seconds
        if translated_text:
            await reaction.message.channel.send(
                f"{user.mention} Translation: {translated_text}",
                delete_after=10  # Delete after 10 seconds for testing
            )
        else:
            await reaction.message.channel.send(
                "Sorry, I couldn't translate that message.",
                delete_after=10  # Delete error message after 10 seconds for testing
            )



@client.event
async def on_message(message):
    if message.content == "!hello":
        await message.channel.send("Hello! 👋 I'm here and working!")

def translate_text(text, target_language):
    # Placeholder function for translation
    # TODO: Add API call to DeepL or another translation service here
    return f"[Translated {target_language} version of: {text}]"

# Run the bot using the token
client.run(bot_token)

