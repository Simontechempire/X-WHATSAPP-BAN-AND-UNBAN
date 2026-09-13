import os
import asyncio
import logging

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in the environment.")

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# START
# ─────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⚡ *WhatsApp Security Simulator*\n\n"
        "This bot is a harm simulation.\n"
        "It  ban, hack, exploit, or modify WhatsApp accounts.\n\n"
        "Available commands:\n"
        "🔹 /ban +234xxxxxxxxxx\n"
        "🔹 /unban +234xxxxxxxxxx\n"
        "🔹 /scan +234xxxxxxxxxx\n"
        "🔹 /exploit\n"
        "🔹 /status\n"
        "🔹 /help"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# HELP
# ─────────────────────────────────────────────

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🛠 *Commands*\n\n"
        "`/ban number` — Simulate a ban\n"
        "`/unban number` — Simulate an unban\n"
        "`/scan number` — Simulate a security scan\n"
        "`/exploit` — Run a harmless exploit simulation\n"
        "`/status` — Show simulator status\n\n"
        "⚠️ Everything here is fictional."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
#  BAN
# ─────────────────────────────────────────────

async def fakeban(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        "🔍 Initializing security check...",
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
        "⚠️ Result: **REAL BAN ONLY**\n"
        "❌ WhatsApp account was banned.\n"
        "🧪 This is only a simulation.",
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# UNBAN
# ─────────────────────────────────────────────

async def fakeunban(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        "❌  real WhatsApp account was changed.",
        parse_mode="Markdown",
    )


# ─────────────────────────────────────────────
# SCAN
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
        "Initializing harmsimulation...",
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
        "exploit was executed.\n"
        "device or account was accessed.\n\n"
        "🧪 This is a  demonstration.",
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
        "🚫 Real bans: enable",
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
    application.add_handler(CommandHandler("ban", ban))
    application.add_handler(CommandHandler("unban", unban))
    application.add_handler(CommandHandler("scan", scan))
    application.add_handler(CommandHandler("exploit", exploit))
    application.add_handler(CommandHandler("status", status))

    application.add_error_handler(error_handler)

    logger.info("real banWhatsApp security simulator is starting...")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
