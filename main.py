import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from love_logic import calculate_love_percentage

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)
bot = Bot(TOKEN)
application = Application.builder().token(TOKEN).build()

# Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Closeness Calculator ❤️!\nUse /love Name1 and Name2 or /love Name1 for Name2")

async def love_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = calculate_love_percentage(user_input)
    await update.message.reply_text(response)

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("love", love_command))

@app.route("/")
def home():
    return "Bot is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.create_task(application.process_update(update))
    return "ok"

if __name__ == "__main__":
    # Start Flask only
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
