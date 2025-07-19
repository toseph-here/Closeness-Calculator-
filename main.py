import os
import requests
from flask import Flask, request
from love_logic import calculate_love_percentage

TOKEN = os.getenv("BOT_TOKEN")
BOT_URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 Love Calculator Bot is alive!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text.startswith("/start"):
            reply = "Welcome to Closeness Calculator ❤️!\nUse /love Name1 and Name2 or /love Name1 for Name2"
        elif text.startswith("/love"):
            reply = calculate_love_percentage(text)
        else:
            reply = "Sorry, I didn't understand that. Use /love."

        send_message(chat_id, reply)

    return "ok"

def send_message(chat_id, text):
    url = f"{BOT_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()
