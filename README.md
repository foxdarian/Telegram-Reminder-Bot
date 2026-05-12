# Telegram Reminder Bot

An asynchronous Telegram bot that allows users to set reminders for tasks. The bot uses a modern Python stack with async/await and stores reminders in a SQLite database.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![aiogram](https://img.shields.io/badge/aiogram-v3.0%2B-blue?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🛠️ Tech Stack

- **aiogram** — asynchronous framework for Telegram Bot API
- **aiosqlite** — asynchronous SQLite database driver
- **python-dotenv** — environment variable management

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/telegram-notification-bot.git
cd telegram-notification-bot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
TOKEN=your_telegram_token_from_botfather
```

> 💡 **How to get a token?**
> 1. Open Telegram and find the **@BotFather** bot
> 2. Send the `/newbot` command
> 3. Follow the instructions and copy your token

### 5. Run the bot

```bash
python main.py
```

## 📱 Usage

1. Open Telegram and find your bot
2. Send the `/start` command
3. Enter your task description
4. Enter the time in minutes for the reminder
5. Receive a reminder after the specified time! ⏰

## 🏗️ Project Structure

```
telegram-notification-bot/
├── main.py              # Main bot file
├── db.py                # Database operations
├── forms.py             # FSM states for task management
├── handlers/
│   └── routes.py        # Message handlers
├── middleware/
│   └── rate_limit.py    # Rate limiting middleware
├── README.md            # This file
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore rules
└── requirements.txt     # Project dependencies
```

## 📖 Documentation

- [aiogram Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [aiosqlite Documentation](https://aiosqlite.omnilib.dev/)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
