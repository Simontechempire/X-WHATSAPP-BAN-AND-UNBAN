import os
import asyncio
import logging
import threading

from dotenv import load_dotenv
from flask import Flask

from telegram import (
    Update,
    InputFile,
    BotCommand,
    MenuButtonCommands,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ─────────────────────────────────────────────
# ENVIRONMENT
# ─────────────────────────────────────────────

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in the environment.")


# ─────────────────────────────────────────────
# FORCE-JOIN CHANNELS
# ─────────────────────────────────────────────

REQUIRED_CHANNELS = [
    ("🌍 MISS TYLA TECH", "@simontech2027", "https://t.me/simontech2027"),
    ("⚡ SIMON TECH 1", "@missarcond", "https://t.me/missarcond"),
    ("🔥 SIMON TECH 2", "@babyupdategc", "https://t.me/babyupdategc"),
    ("𝕏 X BAN", "@mrdarkingdev1", "https://t.me/mrdarkingdev1"),
]


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
# OWNER
# ─────────────────────────────────────────────

def is_owner(update: Update) -> bool:
    return (
        update.effective_user is not None
        and OWNER_ID != 0
        and update.effective_user.id == OWNER_ID
    )


async def owner_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not is_owner(update):
        await update.message.reply_text("❌ Owner only.")
        return

    await update.message.reply_text(
        "👑 OWNER ACCESS GRANTED\n\n"
        "🟢 Owner system is active."
    )


# ─────────────────────────────────────────────
# FORCE-JOIN CHECK
# ─────────────────────────────────────────────

async def is_joined(
    user_id: int,
    context: ContextTypes.DEFAULT_TYPE,
) -> bool:
    for _, channel, _ in REQUIRED_CHANNELS:
        try:
            member = await context.bot.get_chat_member(
                chat_id=channel,
                user_id=user_id,
            )

            if member.status in ("left", "kicked"):
                return False

        except Exception as exc:
            logger.warning(
                "Could not check %s: %s",
                channel,
                exc,
            )
            return False

    return True


# ─────────────────────────────────────────────
# FORCE-JOIN KEYBOARD
# ─────────────────────────────────────────────

def join_keyboard():
    buttons = []

    for title, _, url in REQUIRED_CHANNELS:
        buttons.append(
            [InlineKeyboardButton(title, url=url)]
        )

    buttons.append(
        [
            InlineKeyboardButton(
                "🔓 CHECK JOIN",
                callback_data="check_join",
            )
        ]
    )

    return InlineKeyboardMarkup(buttons)


# ─────────────────────────────────────────────
# STARTUP MENU TEXT
# ─────────────────────────────────────────────

WELCOME_TEXT = (
    "🌍⃝⃘‌‌‌━⋆─⋆──❂\n"
    "┊ ┊ ┊ ┊ ┊\n"
    "┊ ┊ ✫ ˚㋛ ⋆｡ ❀\n"
    "┊ ☠︎︎\n"
    "✧ 𓂃✍︎𝄞\n"
    "╰────────────────❂\n\n"

    "┏━━━━━━━━━━━━━❥❥❥\n"
    "┃ ❌ X BAN\n"
    "┃\n"
    "┃ 👑 WELCOME\n"
    "┃\n"
    "┃ ⚡ X BAN\n"
    "┃ 🛡️ SECURITY SIMULATOR\n"
    "┗━━━━━━━━━━━━━❥❥❥\n\n"

    "┏━━━━━━━━━━━━━❥❥❥\n"
    "┃ 🚪 FORCE JOIN\n"
    "┃\n"
    "┃ 📢 Join our required\n"
    "┃ channels to continue.\n"
    "┃\n"
    "┃ 🔓 CHECK JOIN\n"
    "┗━━━━━━━━━━━━━❥❥❥\n\n"

    "┏━「 ⤵️ 」\n"
    "┃\n"
    "┃ ⚡ Fake Security Features\n"
    "┃\n"
    "┃ 🔨 Ban Simulation\n"
    "┃ 🔓 Unban Simulation\n"
    "┃ 🔍 Security Scan\n"
    "┃ ⚡ Exploit Simulation\n"
    "┃\n"
    "┃ 🧪 SIMULATION ONLY\n"
    "┗━━━━━━━━━━━━━❥❥❥\n\n"

    "</>  X BAN"
)


# ─────────────────────────────────────────────
# START
# ─────────────────────────────────────────────

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    user = update.effective_user

    if user is None:
        return

    joined = await is_joined(user.id, context)

    if not joined:
        gate_text = (
            "🚪 FORCE JOIN GATE\n\n"
            "📢 Please join all required channels below.\n\n"
            "After joining them, press:\n"
            "🔓 CHECK JOIN\n\n"
            "⚠️ You must join all required channels "
            "before using the bot."
        )

        await update.message.reply_text(
            gate_text,
            reply_markup=join_keyboard(),
        )
        return

    startup_image_path = "assets/start.jpg"

    try:
        if os.path.exists(startup_image_path):
            await update.message.reply_photo(
                photo=InputFile(startup_image_path),
                caption=WELCOME_TEXT,
            )

        else:
            await update.message.reply_text(
                WELCOME_TEXT
            )

    except Exception as exc:
        logger.error(
            "Error sending startup image: %s",
            exc,
        )

        await update.message.reply_text(
            WELCOME_TEXT
        )


# ─────────────────────────────────────────────
# CHECK JOIN CALLBACK
# ─────────────────────────────────────────────

async def check_join(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    if query is None or query.from_user is None:
        return

    await query.answer()

    joined = await is_joined(
        query.from_user.id,
        context,
    )

    if not joined:
        await query.answer(
            "❌ You have not joined all required channels.",
            show_alert=True,
        )
        return

    await query.message.reply_text(
        "✅ ACCESS GRANTED\n\n"
        "🎉 You have joined all required channels.\n"
        "⚡ Welcome to X BAN Security Simulator!"
    )

    startup_image_path = "assets/start.jpg"

    try:
        if os.path.exists(startup_image_path):
            await query.message.reply_photo(
                photo=InputFile(startup_image_path),
                caption=WELCOME_TEXT,
            )
        else:
            await query.message.reply_text(
                WELCOME_TEXT
            )

    except Exception as exc:
        logger.error(
            "Startup image error: %s",
            exc,
        )

        await query.message.reply_text(
            WELCOME_TEXT
        )


# ─────────────────────────────────────────────
# ACCESS CHECK FOR COMMANDS
# ─────────────────────────────────────────────

async def require_join(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> bool:

    user = update.effective_user

    if user is None:
        return False

    if await is_joined(user.id, context):
        return True

    await update.message.reply_text(
        "🚫 ACCESS LOCKED\n\n"
        "📢 You must join all required channels first.",
        reply_markup=join_keyboard(),
    )

    return False


# ─────────────────────────────────────────────
# HELP
# ─────────────────────────────────────────────

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not await require_join(update, context):
        return

    text = (
        "🛠 COMMANDS\n\n"
        "/ban number — Simulate a ban\n"
        "/unban number — Simulate an unban\n"
        "/scan number — Simulate a security scan\n"
        "/exploit — Harmless simulation\n"
        "/status — Show simulator status\n"
        "/owner — Owner access\n\n"
        "⚠️ Everything here is fictional."
    )

    await update.message.reply_text(text)


# ─────────────────────────────────────────────
# BAN SIMULATION
# ─────────────────────────────────────────────

async def ban(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not await require_join(update, context):
        return

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/ban +234xxxxxxxxxx"
        )
        return

    number = " ".join(context.args)

    message = await update.message.reply_text(
        "⚡ BAN SIMULATION STARTED\n\n"
        f"📱 Target: {number}\n"
        "🔍 Initializing simulation..."
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
            "⚡ BAN SIMULATION\n\n"
            f"📱 Target: {number}\n"
            f"{step}"
        )

    await message.edit_text(
        "🚫 SIMULATED BAN COMPLETE\n\n"
        f"📱 Target: {number}\n\n"
        "🧪 Result: real BAN\n"
        "❌ real WhatsApp account was banned.\n"
        "✅ Simulation only."
    )


# ─────────────────────────────────────────────
# UNBAN SIMULATION
# ─────────────────────────────────────────────

async def unban(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not await require_join(update, context):
        return

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/unban +234xxxxxxxxxx"
        )
        return

    number = " ".join(context.args)

    message = await update.message.reply_text(
        "🔄 UNBAN SIMULATION\n\n"
        f"📱 Target: {number}\n"
        "Processing..."
    )

    for progress in [
        "▰▱▱▱▱ 20%",
        "▰▰▰▱▱ 60%",
        "▰▰▰▰▰ 100%",
    ]:
        await asyncio.sleep(0.8)

        await message.edit_text(
            "🔄 UNBAN SIMULATION\n\n"
            f"📱 Target: {number}\n"
            f"Progress: {progress}"
        )

    await message.edit_text(
        "✅ SIMULATED UNBAN COMPLETE\n\n"
        f"📱 Target: {number}\n\n"
        "🧪 Simulation ban.\n"
        "❌  real WhatsApp account was changed."
    )


# ─────────────────────────────────────────────
# SECURITY SCAN
# ─────────────────────────────────────────────

async def scan(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not await require_join(update, context):
        return

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/scan +234xxxxxxxxxx"
        )
        return

    number = " ".join(context.args)

    message = await update.message.reply_text(
        "🔍 SECURITY SCAN\n\n"
        f"📱 Target: {number}\n"
        "Starting simulated scan..."
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
            "🔍 SECURITY SCAN\n\n"
            f"📱 Target: {number}\n"
            f"{step}"
        )

    await message.edit_text(
        "📊 SIMULATED SCAN REPORT\n\n"
        f"📱 Target: {number}\n"
        "🟢 Connection: Simulated\n"
        "🟢 Security: Simulated\n"
        "🟢 Restrictions:  detected\n\n"
        "⚠️ Fictional data only."
    )


# ─────────────────────────────────────────────
# EXPLOIT SIMULATION
# ─────────────────────────────────────────────

async def exploit(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not await require_join(update, context):
        return

    message = await update.message.reply_text(
        "⚡ EXPLOIT SIMULATOR\n\n"
        "Initializing harmful simulation..."
    )

    stages = [
        "🔧 Loading fictional module...",
        "🔍 Searching simulated environment...",
        "🧪 Running harmful test...",
        "📡 Simulating response...",
        "🛡 Simulation stopped badly...",
    ]

    for stage in stages:
        await asyncio.sleep(0.9)

        await message.edit_text(
            "⚡ EXPLOIT SIMULATOR\n\n"
            f"{stage}"
        )

    await message.edit_text(
        "✅ SIMULATION COMPLETE\n\n"
        "🧪  exploit was executed.\n"
        "🔒 devices or account was accessed.\n"
        "🛡  real WhatsApp action was performed."
    )


# ─────────────────────────────────────────────
# STATUS
# ─────────────────────────────────────────────

async def status(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not await require_join(update, context):
        return

    await update.message.reply_text(
        "🟢 SIMULATOR ONLINE\n\n"
        "⚡ Engine: Online\n"
        "🧪 Mode: Simulation\n"
        "🛡 Real exploitation: enable\n"
        "📱 WhatsApp access: None\n"
        "🚫 Real bans: enable"
    )


# ─────────────────────────────────────────────
# BOT MENU
# ─────────────────────────────────────────────

async def setup_menu(application: Application):
    commands = [
        BotCommand("start", "🚀 Start the bot"),
        BotCommand("ban", "🚫 Simulate a ban"),
        BotCommand("unban", "✅ Simulate an unban"),
        BotCommand("scan", "🔍 Security scan"),
        BotCommand("exploit", "⚡ Harmful simulation"),
        BotCommand("status", "📊 Simulator status"),
        BotCommand("help", "🛠️ Help"),
        BotCommand("owner", "👑 Owner access"),
    ]

    await application.bot.set_my_commands(commands)

    await application.bot.set_chat_menu_button(
        menu_button=MenuButtonCommands()
    )

    logger.info("Telegram menu configured.")


# ─────────────────────────────────────────────
# ERROR HANDLER
# ─────────────────────────────────────────────

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):
    logger.error(
        "Exception while processing update:",
        exc_info=context.error,
    )


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(setup_menu)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        CommandHandler("ban", ban)
    )

    application.add_handler(
        CommandHandler("unban", unban)
    )

    application.add_handler(
        CommandHandler("scan", scan)
    )

    application.add_handler(
        CommandHandler("exploit", exploit)
    )

    application.add_handler(
        CommandHandler("status", status)
    )

    application.add_handler(
        CommandHandler("owner", owner_command)
    )

    application.add_handler(
        CallbackQueryHandler(
            check_join,
            pattern="^check_join$",
        )
    )

    application.add_error_handler(
        error_handler
    )

    logger.info(
        "X WhatsApp Ban/Unban simulator is starting..."
    )

    web_thread = threading.Thread(
        target=run_web_server,
        daemon=True,
    )

    web_thread.start()

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
