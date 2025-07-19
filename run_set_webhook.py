import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://your-app-name.onrender.com/webhook"

bot = Bot(BOT_TOKEN)
bot.set_webhook(WEBHOOK_URL)
print("Webhook set successfully!")
