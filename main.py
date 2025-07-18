from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Command List
COMMANDS = {
    "love": "Calculate love percentage between two people.",
    "hate": "Measure the hate level between two people.",
    "crush": "Check how much one person has a crush on another.",
    "jealousy": "See the jealousy level between two people.",
    "anger": "Find out how angry one person is at another.",
    "friend": "Check how friendly two people are.",
    "bestfriend": "Measure the closeness of best friendship.",
    "fear": "Check the fear level one has for another.",
    "disappointment": "Calculate the disappointment between two people.",
    "doubt": "See how much doubt exists between two people.",
}

def parse_names(text):
    text = text.strip()
    plus = 0

    if ' and ' in text:
        parts = text.split(' and ')
        name1 = parts[0].strip()
        name2 = parts[1].strip().replace('#', '').replace('##', '')
    elif ' for ' in text:
        parts = text.split(' for ')
        name1 = parts[0].strip()
        name2 = parts[1].strip().replace('#', '').replace('##', '')
        if text.endswith('##'):
            plus = 14
        elif text.endswith('#'):
            plus = 7
    else:
        return None, None, 0

    return name1, name2, plus

async def generic_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text.split()[0][1:].lower()
    query = update.message.text[len(command)+2:].strip()

    if command not in COMMANDS:
        await update.message.reply_text("Invalid command.")
        return

    name1, name2, bonus = parse_names(query)
    if not name1 or not name2:
        await update.message.reply_text("❗ Please enter names in correct format. Use /infobot to see help.")
        return

    result = random.randint(10, 90) + bonus
    if result > 100:
        result = 100

    await update.message.reply_text(
        f"🔍 *{command.capitalize()} Score between {name1} and {name2}*: {result}%",
        parse_mode='Markdown'
    )

async def infobot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    description = (
        "🤖 *What is this bot?*\n"
        "This bot helps you analyze emotional connections between two people in a fun and entertaining way.\n\n"

        "📌 *How to use:*\n"
        "Use the following commands followed by names in proper format:\n\n"
    )

    for cmd, desc in COMMANDS.items():
        description += f"/{cmd} — {desc}\n"

    description += (
        "\n📊 *Format Examples:*\n"
        "`/love Alice and Bob` — for mutual love check\n"
        "`/love Rahul for Priya #` — Rahul wants to check for Priya (girl name last)\n"
        "`/love Priya for Rahul ##` — Priya wants to check for Rahul (girl name first)\n"
        "`/love Arjun for Kabir` — friendship/neutral check\n\n"

        "⚠️ *Note:* This bot does not reveal any real emotions. It's just a trick-based fun generator.\n"
        "🛡️ *Privacy Policy:* We do NOT collect or store your data. So chill and enjoy the fun! 😄"
    )

    await update.message.reply_text(description, parse_mode='Markdown')

def main():
    import os
    TOKEN = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("infobot", infobot))

    for cmd in COMMANDS:
        app.add_handler(CommandHandler(cmd, generic_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
