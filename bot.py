import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Lataa ympäristömuuttujat
print("Ladataan .env-tiedosto...")
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Tarkista avaimet
print(f"TELEGRAM_TOKEN: {TELEGRAM_TOKEN}")
print(f"GEMINI_API_KEY: {GEMINI_API_KEY}")
if not TELEGRAM_TOKEN:
    raise ValueError("Virhe: TELEGRAM_TOKEN puuttuu .env-tiedostosta")
if not GEMINI_API_KEY:
    raise ValueError("Virhe: GEMINI_API_KEY puuttuu .env-tiedostosta")

# Alusta Gemini
print("Alustetaan Gemini AI...")
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    print(f"Gemini-virhe: {str(e)}")
    raise

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Lähettää tervetuloviestin /start-komennolla."""
    await update.message.reply_text("Hei! Olen AI-botti, joka käyttää Geminiä. Kysy mitä tahansa!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Käsittelee käyttäjän viestit ja vastaa Gemini AI:lla."""
    user_message = update.message.text
    try:
        # Kutsu Gemini API:ta
        response = model.generate_content(user_message)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Virhe: {str(e)}")

def main() -> None:
    """Käynnistää botin."""
    print("Käynnistään Telegram-botti...")
    try:
        app = Application.builder().token(TELEGRAM_TOKEN).build()
    except Exception as e:
        print(f"Telegram-virhe: {str(e)}")
        raise

    # Lisää käsittelijät
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Käynnistä botti
    print("Aloitetaan polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
