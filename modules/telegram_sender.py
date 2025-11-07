import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_message(summary):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=summary)
    print("✅ Prescription summary sent to Telegram.")

if __name__ == "__main__":
    asyncio.run(send_message("This is a test summary from AI Prescription Agent."))
