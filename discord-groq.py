# Discord Virtual Assistant - Coach Buddy
# Created by Ankur Kushwaha
# Based on AAOT Module 3 Demo by Ali Tobah and Dr. Abel Sanchez

from dotenv import load_dotenv
from groq import Groq
import discord
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DISCORD_TOKEN = os.getenv("TOKEN")

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

# Coach Buddy System Prompt
SYSTEM_PROMPT = """You are Coach Buddy, a friendly and motivational virtual assistant. 
Your role is to:
- Be encouraging and supportive in all responses
- Help users stay motivated and focused on their goals
- Provide practical advice when asked
- Keep responses concise but helpful
- Use a warm, friendly tone like a supportive coach would

Always aim to uplift and empower the person you're talking to!"""


def call_groq(question):
    """Send a question to Groq AI and get Coach Buddy's response."""
    completion = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    response = completion.choices[0].message.content
    print(f"Coach Buddy: {response}")
    return response


# Discord setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Called when the bot successfully connects to Discord."""
    print(f"Coach Buddy is online! Logged in as {client.user}")
    print("Ready to motivate and assist!")
    print("-" * 40)


@client.event
async def on_message(message):
    """Called whenever a message is sent in a channel the bot can see."""
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Respond to $hello command
    if message.content.startswith("$hello"):
        await message.channel.send("Hey there, champion! 💪 Coach Buddy here, ready to help you crush your goals! How can I assist you today?")

    # Respond to $coach command with AI-powered response
    if message.content.startswith("$coach"):
        # Extract the question after the command
        message_content = message.content.split("$coach", 1)[1].strip()
        
        if not message_content:
            await message.channel.send("Hey! What would you like to ask Coach Buddy? Try: `$coach [your question]`")
            return
            
        print(f"Question from {message.author}: {message_content}")

        # Get response from Groq AI
        response = call_groq(message_content)
        print("-" * 40)

        await message.channel.send(response)

    # Help command
    if message.content.startswith("$help"):
        help_message = """**Coach Buddy Commands:**
`$hello` - Get a friendly greeting
`$coach [question]` - Ask Coach Buddy anything!
`$help` - Show this help message

I'm here to motivate and support you! 🌟"""
        await message.channel.send(help_message)


# Run the bot
client.run(DISCORD_TOKEN)
