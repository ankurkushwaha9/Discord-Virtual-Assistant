# Discord Virtual Assistant - Coach Buddy 💪

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.0+-5865F2.svg)](https://discordpy.readthedocs.io/)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.3-orange.svg)](https://groq.com/)
[![Status](https://img.shields.io/badge/Status-✅_Live-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)]()

A motivational Discord bot powered by Groq AI (Llama 3.3 70B). Coach Buddy is your friendly virtual assistant designed to encourage, motivate, and help you achieve your goals!

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI-Powered Responses** | Uses Groq's Llama 3.3 70B model for intelligent conversations |
| 💪 **Motivational Personality** | Coach Buddy is designed to be encouraging and supportive |
| ⚡ **Fast Response** | Groq's optimized inference for quick replies |
| 🛠️ **Simple Commands** | Easy to use command structure |

---

## 🎮 Commands

| Command | Description |
|---------|-------------|
| `$hello` | Get a friendly greeting from Coach Buddy |
| `$coach [question]` | Ask Coach Buddy anything! |
| `$help` | Display available commands |

---

## 📸 Demo

### Bot Running Successfully
```
Coach Buddy is online! Logged in as Virtual Assistant#6147
Ready to motivate and assist!
----------------------------------------
```

### Sample Interaction
```
User: $hello
Coach Buddy: Hey there, champion! 💪 Coach Buddy here, ready to help you crush your goals! How can I assist you today?

User: $coach How can I stay motivated while studying?
Coach Buddy: I'm so proud of you for taking the first step towards your goals. To stay motivated while studying, here are a few tips: break your study sessions into smaller, manageable chunks, set achievable goals, and reward yourself after reaching each milestone...
```

---

## 🚀 Setup Instructions

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Discord Bot Token** - [Create one here](https://discord.com/developers/applications)
3. **Groq API Key** - [Get one here](https://console.groq.com/keys)
4. **Git** (optional) - [Download here](https://git-scm.com/downloads)

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

---

## 📁 Project Structure

```
Discord-Virtual-Assistant/
├── discord-groq.py      # Main bot code with Coach Buddy personality
├── .env.example         # Template for environment variables
├── .env                 # Your actual secrets (not tracked by git)
├── .gitignore           # Files to ignore in git
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 🔧 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core programming language |
| discord.py | Discord API wrapper |
| Groq API | AI inference (Llama 3.3 70B) |
| python-dotenv | Environment variable management |

---

## ⚠️ Important Security Note

Never commit your `.env` file to GitHub! It contains sensitive API keys. The `.gitignore` file is configured to prevent this, but always double-check before pushing.

---

## 🙏 Credits

- Based on [AAOT Module 3 Demo](https://github.com/tobah59x/AAOT-Mod3-Demo) by Ali Tobah
- Original Discord bot template by [Dr. Abel Sanchez](https://github.com/abelsan/bot)
- Part of MIT Professional Education: Agentic AI and Open Tools (AAOT) course

---

## 📄 License

This project is for educational purposes as part of the AAOT course.

---

## 🔗 Related Projects

Check out my other AI projects at [ai-learning-os](https://github.com/ankurkushwaha9/ai-learning-os)

---

*Created with ❤️ by [Ankur Kushwaha](https://github.com/ankurkushwaha9)*
