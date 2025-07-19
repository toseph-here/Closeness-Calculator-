import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, Dispatcher, CallbackContext
from telegram.ext.dispatcher import Dispatcher as LegacyDispatcher
from telegram.ext._utils.types import BD
from love_logic import calculate_love_percentage  # Tumhara logic yahan use hoga

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)
bot = Bot(TOKEN)
application = Application.builder().token(TOKEN).build()

@app.route("/")
def home():
    return "Bot is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.update_queue.put_nowait(update)
    return "ok"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Closeness Calculator ❤️!\nUse /love Name1 and Name2 or /love Name1 for Name2")

async def love_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = calculate_love_percentage(user_input)
    await update.message.reply_text(response)

def setup():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("love", love_command))

if __name__ == "__main__":
    setup()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
