import os
import asyncio
from telegram.ext import Application, CommandHandler
from love_logic import calculate_love_percentage  # if this is in another file

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not set in environment variables!")

async def start(update, context):
    await update.message.reply_text("Welcome! Use /love Name1 and Name2")

async def love(update, context):
    input_text = " ".join(context.args)
    response = calculate_love_percentage(input_text)
    await update.message.reply_text(response)

async def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("love", love))
    
    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    main()
