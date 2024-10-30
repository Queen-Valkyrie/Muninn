import discord

# Insert your bot token directly here
bot_token = "MTMwMTEwMTA3NzkyNzU2MzI5NQ.GJvObH.JnWhB7nQaDbtXFlvY0Pc99IcQS81uRFd1HqPuc
"

# Set up the bot client
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to read message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

# Start the bot
client.run(bot_token)
