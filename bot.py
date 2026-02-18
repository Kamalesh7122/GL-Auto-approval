import os

print("TOKEN RAW:", repr(os.getenv("8513812946:AAGx28rW17Lr4mh1HzECks1Fkxmv84Fs7mM")))

from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = os.getenv("8513812946:AAGx28rW17Lr4mh1HzECks1Fkxmv84Fs7mM")

print("Token:", BOT_TOKEN)

async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(ChatJoinRequestHandler(auto_approve))

app.run_polling()
