# Discord Virtual Assistant - Coach Buddy 💪

A motivational Discord bot powered by Groq AI (Llama 3.3). Coach Buddy is your friendly virtual assistant designed to encourage, motivate, and help you achieve your goals!

## Features

- **AI-Powered Responses** - Uses Groq's Llama 3.3 70B model for intelligent conversations
- **Motivational Personality** - Coach Buddy is designed to be encouraging and supportive
- **Simple Commands** - Easy to use command structure

## Commands

| Command | Description |
|---------|-------------|
| `$hello` | Get a friendly greeting from Coach Buddy |
| `$coach [question]` | Ask Coach Buddy anything! |
| `$help` | Display available commands |

## Setup Instructions

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Discord Bot Token** - [Create one here](https://discord.com/developers/applications)
3. **Groq API Key** - [Get one here](https://console.groq.com/keys)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ankurkushwaha9/Discord-Virtual-Assistant.git
   cd Discord-Virtual-Assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create your `.env` file:**
   ```bash
   cp .env.example .env
   ```

4. **Edit `.env` with your actual keys:**
   ```
   TOKEN=your_discord_bot_token_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the bot:**
   ```bash
   python discord-groq.py
   ```

## Usage Example

Once the bot is running and added to your Discord server:

```
You: $hello
Coach Buddy: Hey there, champion! 💪 Coach Buddy here, ready to help you crush your goals!

You: $coach How can I stay motivated while studying?
Coach Buddy: [AI-powered motivational response]
```

## Project Structure

```
Discord-Virtual-Assistant/
├── discord-groq.py      # Main bot code
├── .env.example         # Template for environment variables
├── .env                 # Your actual secrets (not tracked by git)
├── .gitignore           # Files to ignore in git
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Important Security Note ⚠️

Never commit your `.env` file to GitHub! It contains sensitive API keys. The `.gitignore` file is configured to prevent this, but always double-check before pushing.

## Credits

- Based on [AAOT Module 3 Demo](https://github.com/tobah59x/AAOT-Mod3-Demo) by Ali Tobah
- Original Discord bot template by [Dr. Abel Sanchez](https://github.com/abelsan/bot)

## License

This project is for educational purposes as part of the AAOT course.

---

*Created by Ankur Kushwaha*
