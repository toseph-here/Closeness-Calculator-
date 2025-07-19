import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Love calculator function
def calculate_love_percentage(name1, name2):
    combined = (name1 + name2).lower().replace(" ", "")
    counts = {}
    for char in combined:
        counts[char] = counts.get(char, 0) + 1
    numbers = [str(count) for count in counts.values()]
    while len(numbers) > 2:
        temp = []
        for i in range(len(numbers) // 2):
            total = int(numbers[i]) + int(numbers[-(i + 1)])
            temp.append(str(total))
        if len(numbers) % 2 == 1:
            temp.append(numbers[len(numbers) // 2])
        numbers = temp
    return int("".join(numbers))

# /love command handler
async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) >= 3 and args[-2].lower() == "and":
            name1 = " ".join(args[:-2])
            name2 = args[-1]
            percentage = calculate_love_percentage(name1, name2)
            response = f"❤️ Love percentage between {name1} and {name2} is {percentage}%"
        else:
            response = "❌ Use the format: /love Name1 and Name2"
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# Main function
async def main():
    from telegram.ext import ApplicationBuilder
    import asyncio

    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("love", love))

    print("Bot is running...")
    await app.run_polling()

# Entry point
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
