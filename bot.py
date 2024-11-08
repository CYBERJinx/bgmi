# bot.py
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from config import BOT_TOKEN
import handlers  # Import command handlers

updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher

# Add conversation handler for registration
registration_handler = ConversationHandler(
    entry_points=[CommandHandler("register", handlers.register)],
    states={
        "REGISTER": [MessageHandler(Filters.text & ~Filters.command, handlers.handle_registration)],
    },
    fallbacks=[CommandHandler("start", handlers.start)],
)

# Add command handlers
dispatcher.add_handler(CommandHandler("start", handlers.start))
dispatcher.add_handler(CommandHandler("help", handlers.start))
dispatcher.add_handler(CommandHandler("status", handlers.status))
dispatcher.add_handler(CommandHandler("schedule", handlers.schedule))

# Register conversation handler
dispatcher.add_handler(registration_handler)

# Start the bot
updater.start_polling()
updater.idle()
