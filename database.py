# database.py
from pymongo import MongoClient
from config import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client['tournament_bot']

def save_team(team_name, players, contact):
    db.teams.insert_one({
        "team_name": team_name,
        "players": players,
        "contact": contact,
        "status": "Pending Verification"
    })

def get_status(team_name):
    team = db.teams.find_one({"team_name": team_name})
    return team.get("status", "Not Registered") if team else "Not Registered"
