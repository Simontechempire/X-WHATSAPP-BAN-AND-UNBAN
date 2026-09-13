import os
import asyncio
import logging
import threading

from dotenv import load_dotenv
from flask import Flask

from telegram import Update, InputFile
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# ─────────────────────────────────────────────
# ENVIRONMENT
# ─────────────────────────────────────────────

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in the environment.")


# ─────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# RENDER WEB SERVER
# ─────────────────────────────────────────────

web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "WhatsApp Security Simulator is online."


@web_app.route("/health")
def health():
    return "OK"


def run_web_server():
    port = int(os.environ.get("PORT", "10000"))

    web_app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False,
    )


# ─────────────────────────────────────────────
# START
# ─────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⚡ *WhatsApp Security Simulator*\n\n"
        "🧪 This bot is a harm simulation.\n"
        "❌ It cannot ban, hack, exploit, or modify WhatsApp accounts.\n\n"
        "Available commands:\n"
        "🔹 /ban +234xxxxxxxxxx\n"
        "🔹 /unban +234xxxxxxxxxx\n"
        "🔹 /scan +234xxxxxxxxxx\n"
        "🔹 /exploit\n"
        "🔹 /status\n"
        "🔹 /help"
    )

    # Check if startup image exists
    startup_image_path = "images/startup.jpg"
    
    try:
        if os.path.exists(startup_image_path):
            # Send image with caption
            await update.message.reply_photo(
                photo=InputFile(startup_image_path),
                caption=text,
                parse_mode="Markdown",
            )
        else:
            # Fallback to text only if image doesn't exist
            await update.message.reply_text(
                text,
                parse_mode="Markdown",
            )
    except Exception as e:
        logger.error(f"Error sending startup image: {e}")
        # Fallback to text if any error occurs
        await update.message.reply_text(
            text,
            parse_mode="Markdown",
        )


# ─────────────────────────────────────────────
# HELP
# ─────────────────────────────────────────────

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🛠 *COMMANDS*\n\n"
        "`/ban number` — Simulate a ban\n"
        "`/unban number` — Simulate an unban\n"
        "`/scan number` — Simulate a security scan\n"
        "`/exploit` — Run a harm exploit simulation\n"
        "`/status` — Show simulator status\n\n"
        "⚠️ Everything here is fictional."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# BAN SIMULATION
# ─────────────────────────────────────────────

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage:\n`/ban +234xxxxxxxxxx`",
            parse_mode="Markdown",
        )
        return

    number = " ".join(context.args)

    message = await update.message.reply_text(
        "⚡ *BAN SIMULATION STARTED*\n\n"
        f"📱 Target: `{number}`\n"
        "🔍 Initializing simulation...",
        parse_mode="Markdown",
    )

    steps = [
        "🔎 Checking simulated account...",
        "🛰 Connecting to simulation engine...",
        "🔐 Analyzing fictional security data...",
        "⚙️ Processing simulated request...",
        "████████████████ 100%",
    ]

    for step in steps:
        await asyncio.sleep(0.8)

        await message.edit_text(
            "⚡ *BAN SIMULATION*\n\n"
            f"📱 Target: `{number}`\n"
            f"{step}",
            parse_mode="Markdown",
        )

    await asyncio.sleep(0.5)

    await message.edit_text(
        "🚫 *SIMULATED BAN COMPLETE*\n\n"
        f"📱 Target: `{number}`\n\n"
        "🧪 Result: *account executed BAN*\n"
        "❌ No real WhatsApp account was banned.\n"
        "✅ Simulation only.",
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# UNBAN SIMULATION
# ─────────────────────────────────────────────

async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage:\n`/unban +234xxxxxxxxxx`",
            parse_mode="Markdown",
        )
        return

    number = " ".join(context.args)

    message = await update.message.reply_text(
        "🔄 *UNBAN SIMULATION*\n\n"
        f"📱 Target: `{number}`\n"
        "Processing...",
        parse_mode="Markdown",
    )

    for progress in [
        "▰▱▱▱▱ 20%",
        "▰▰▰▱▱ 60%",
        "▰▰▰▰▰ 100%",
    ]:
        await asyncio.sleep(0.8)

        await message.edit_text(
            "🔄 *UNBAN SIMULATION*\n\n"
            f"📱 Target: `{number}`\n"
            f"Progress: {progress}",
            parse_mode="Markdown",
        )

    await message.edit_text(
        "✅ *SIMULATED UNBAN COMPLETE*\n\n"
        f"📱 Target: `{number}`\n\n"
        "🧪 Simulation finished.\n"
        "❌ No real WhatsApp account was changed.",
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# SECURITY SCAN
# ─────────────────────────────────────────────

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage:\n`/scan +234xxxxxxxxxx`",
            parse_mode="Markdown",
        )
        return

    number = " ".join(context.args)

    message = await update.message.reply_text(
        "🔍 *SECURITY SCAN*\n\n"
        f"📱 Target: `{number}`\n"
        "Starting simulated scan...",
        parse_mode="Markdown",
    )

    scan_steps = [
        "🔍 Checking fictional metadata...",
        "🧩 Checking simulated security flags...",
        "🛡 Checking fictional restrictions...",
        "📊 Generating simulated report...",
    ]

    for step in scan_steps:
        await asyncio.sleep(0.8)

        await message.edit_text(
            "🔍 *SECURITY SCAN*\n\n"
            f"📱 Target: `{number}`\n"
            f"{step}",
            parse_mode="Markdown",
        )

    await message.edit_text(
        "📊 *SIMULATED SCAN REPORT*\n\n"
        f"📱 Target: `{number}`\n"
        "🟢 Connection: Simulated\n"
        "🟢 Security: Simulated\n"
        "🟢 Restrictions: None detected\n\n"
        "⚠️ This report contains fictional data only.",
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# EXPLOIT SIMULATION
# ─────────────────────────────────────────────

async def exploit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await update.message.reply_text(
        "⚡ *EXPLOIT SIMULATOR*\n\n"
        "Initializing harm simulation...",
        parse_mode="Markdown",
    )

    stages = [
        "🔧 Loading fictional module...",
        "🔍 Searching simulated environment...",
        "🧪 Running harm test...",
        "📡 Simulating response...",
        "🛡 Simulation stopped safely...",
    ]

    for stage in stages:
        await asyncio.sleep(0.9)

        await message.edit_text(
            "⚡ *EXPLOIT SIMULATOR*\n\n"
            f"{stage}",
            parse_mode="Markdown",
        )

    await message.edit_text(
        "✅ *SIMULATION COMPLETE*\n\n"
        "🧪 No exploit was executed.\n"
        "🔒 No real device or account was accessed.\n"
        "🛡 No real WhatsApp action was performed.",
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# STATUS
# ─────────────────────────────────────────────

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 *SIMULATOR ONLINE*\n\n"
        "⚡ Engine: Online\n"
        "🧪 Mode: Simulation\n"
        "🛡 Real exploitation: Disabled\n"
        "📱 WhatsApp access: None\n"
        "🚫 Real bans: Disabled",
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# ERROR HANDLER
# ─────────────────────────────────────────────

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(
        "Exception while processing update:",
        exc_info=context.error,
    )


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Commands now use the functions named ban() and unban()
    application.add_handler(CommandHandler("ban", ban))
    application.add_handler(CommandHandler("unban", unban))

    application.add_handler(CommandHandler("scan", scan))
    application.add_handler(CommandHandler("exploit", exploit))
    application.add_handler(CommandHandler("status", status))

    application.add_error_handler(error_handler)

    logger.info("WhatsApp security simulator is starting...")

    # Start Render HTTP server
    web_thread = threading.Thread(
        target=run_web_server,
        daemon=True,
    )
    web_thread.start()

    # Start Telegram bot
    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
