from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8513812946:AAHFNNFlWq9q8dJRw_OrxlhJmmc2av5ZGxc"

async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(ChatJoinRequestHandler(auto_approve))

app.run_polling()
