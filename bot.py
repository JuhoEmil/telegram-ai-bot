import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def start(bot, update):
    update.message.reply_text("Hello! I'm a bot powered by Gemini AI.")

def handle_message(bot, update):
    text = update.message.text
    try:
        # Generate response with Gemini
        response = model.generate_content(text)
        update.message.reply_text(response.text)
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    print("Starting Telegram bot...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
