# bot.py
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters
import handlers
from config import BOT_TOKEN

# Create the Application instance
app = Application.builder().token(BOT_TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", handlers.start))
app.add_handler(CommandHandler("help", handlers.start))
app.add_handler(CommandHandler("status", handlers.status))
app.add_handler(CommandHandler("schedule", handlers.schedule))

# Conversation handler for registration
registration_handler = ConversationHandler(
    entry_points=[CommandHandler("register", handlers.register)],
    states={
        "REGISTER": [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_registration)],
    },
    fallbacks=[CommandHandler("start", handlers.start)],
)

# Register conversation handler
app.add_handler(registration_handler)

# Start the bot with polling
if __name__ == "__main__":
    app.run_polling()
