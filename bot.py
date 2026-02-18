import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = os.getenv("8513812946:AAFFUpuhqpXiaXsIZ_Q0tJgV8updiphYTiE")

print("Token:", BOT_TOKEN)

async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(ChatJoinRequestHandler(auto_approve))

app.run_polling()
