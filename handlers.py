# handlers.py
from telegram import Update
from telegram.ext import CallbackContext
import database  # Import database functions

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to the BGMI Tournament Bot!\n"
        "Commands:\n"
        "/register - Register your team\n"
        "/status - Check registration status\n"
        "/schedule - Get match schedule\n"
        "/help - Get help"
    )

def register(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Please enter your team name, player names, and contact info separated by commas.\n"
        "Example: TeamName, Player1, Player2, Player3, Player4, Contact"
    )
    return "REGISTER"

def handle_registration(update: Update, context: CallbackContext):
    user_data = update.message.text.split(", ")
    team_name, players, contact = user_data[0], user_data[1:-1], user_data[-1]
    
    # Save to database
    database.save_team(team_name, players, contact)
    update.message.reply_text(f"Team {team_name} registered successfully!")

def status(update: Update, context: CallbackContext):
    team_name = context.args[0] if context.args else "Unknown Team"
    status = database.get_status(team_name)
    update.message.reply_text(f"Your current registration status is: {status}")

def schedule(update: Update, context: CallbackContext):
    schedule_info = "Match Schedule:\nRound 1: Date, Time\nRound 2: Date, Time"
    update.message.reply_text(schedule_info)