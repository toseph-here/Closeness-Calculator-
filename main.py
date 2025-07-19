# main.py

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from love_logic import calculate_love_percentage

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Closeness Calculator ❤️!\nUse /love Name1 and Name2 or /love Name1 for Name2")

async def love_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = calculate_love_percentage(user_input)
    await update.message.reply_text(response)

def main():
    if not TOKEN:
        print("❌ BOT_TOKEN not found in environment!")
        return

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("love", love_command))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
