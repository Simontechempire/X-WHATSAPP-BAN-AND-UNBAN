# ⚡ WhatsApp Security Simulator

A Telegram bot that provides **fictional WhatsApp security and ban simulations** for demonstrations and entertainment.

> ⚠️ **Important:** This project does not interact with WhatsApp, ban accounts, hack devices, exploit services, or modify real accounts.

## 🚀 Quick Start

<a href="https://t.me/Iriscene1Bot" target="_blank">
  <img src="https://img.shields.io/badge/Telegram-@Iriscene1Bot-0088cc?logo=telegram&logoColor=white&style=for-the-badge" alt="Start Bot on Telegram">
</a>

**Click the button above to start using the bot on Telegram!**

Or search for `@Iriscene1Bot` in your Telegram app.

---

## 🚀 Features

- `/start` — Start the bot and see the startup image
- `/help` — Show available commands
- `/ban` — Simulate a ban
- `/unban` — Simulate an unban
- `/scan` — Simulate a security scan
- `/exploit` — Run a harmless exploit simulation
- `/status` — Show simulator status

## 📸 Startup Image

When users run `/start`, the bot displays a custom image alongside the welcome message. Place your startup image at `images/startup.jpg` to customize it!

**Image specifications:**
- Filename: `startup.jpg`
- Location: `images/` directory
- Format: JPG, PNG, or other Telegram-supported formats
- Size: Recommended 800x600 pixels or larger
- Max size: 20 MB (keep under 5 MB for best performance)

## 📁 Project Structure

```text
X-WHATSAPP-BAN-AND-UNBAN/
├── bot.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
├── Dockerfile
├── render.yaml
├── images/
│   ├── README.md
│   └── startup.jpg (your custom image)
└── .github/
    └── workflows/
```

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Simontechempire/X-WHATSAPP-BAN-AND-UNBAN.git
cd X-WHATSAPP-BAN-AND-UNBAN
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file locally:

```
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

Never publish your bot token.

## ▶️ Run

```bash
python bot.py
```

## 📝 Adding Your Startup Image

1. Navigate to the `images/` folder
2. Replace or add `startup.jpg` with your image
3. Commit and push to GitHub:
   ```bash
   git add images/startup.jpg
   git commit -m "Add custom startup image"
   git push
   ```
4. Restart the bot to use the new image

## 🤖 Example Usage

```
/ban +234xxxxxxxxxx
```

The bot displays a simulated ban sequence and clearly reports that no real WhatsApp action occurred.

## ⚠️ Disclaimer

This project is strictly a simulation.

- It does not provide real WhatsApp banning, hacking, exploitation, account access, or unauthorized actions
- All images and messages are fictional
- Use it responsibly for testing, demonstrations, and entertainment

## 📜 License

MIT License

See [LICENSE](LICENSE) for more details.
