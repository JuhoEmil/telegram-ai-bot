<<<<<<< HEAD
import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import google.generativeai as genai
=======
(.venv) juhoemil@Hardestmotherfucker:~/telegram-ai-bot$ cd ~/telegram-ai-bot
source .venv/bin/activate
python bot.py
/home/juhoemil/telegram-ai-bot/bot.py:36: DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
Starting Telegram bot...
Traceback (most recent call last):
  File "/home/juhoemil/telegram-ai-bot/.venv/lib/python3.13/site-packages/telegram/ext/_application.py", line 1047, in __run
    loop.run_until_complete(self._bootstrap_initialize(max_retries=bootstrap_retries))
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/asyncio/base_events.py", line 701, in run_until_complete
    self._check_running()
    ~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.13/asyncio/base_events.py", line 637, in _check_running
    raise RuntimeError('This event loop is already running')
RuntimeError: This event loop is already running
>>>>>>> 47d5e4215f8fe90763cea83adb2f8723589fad84

During handling of the above exception, another exception occurred:

<<<<<<< HEAD
# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm a bot powered by Gemini AI.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        # Generate response with Gemini
        response = model.generate_content(text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Starting Telegram bot...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
=======
Traceback (most recent call last):
  File "/home/juhoemil/telegram-ai-bot/bot.py", line 40, in <module>
    loop.run_until_complete(main())
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/usr/lib/python3.13/asyncio/base_events.py", line 725, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/home/juhoemil/telegram-ai-bot/bot.py", line 33, in main
    await app.run_polling(close_loop=False)
          ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/juhoemil/telegram-ai-bot/.venv/lib/python3.13/site-packages/telegram/ext/_application.py", line 837, in run_polling
    return self.__run(
           ~~~~~~~~~~^
        updater_coroutine=self.updater.start_polling(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<9 lines>...
        close_loop=close_loop,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/juhoemil/telegram-ai-bot/.venv/lib/python3.13/site-packages/telegram/ext/_application.py", line 1072, in __run
    loop.run_until_complete(self.shutdown())
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/asyncio/base_events.py", line 701, in run_until_complete
    self._check_running()
    ~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.13/asyncio/base_events.py", line 637, in _check_running
    raise RuntimeError('This event loop is already running')
RuntimeError: This event loop is already running
<sys>:0: RuntimeWarning: coroutine 'Application._bootstrap_initialize' was never awaited
<sys>:0: RuntimeWarning: coroutine 'Application.shutdown' was never awaited
>>>>>>> 47d5e4215f8fe90763cea83adb2f8723589fad84
