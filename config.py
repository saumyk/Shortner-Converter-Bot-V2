# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "5604474"))
API_HASH = os.environ.get("API_HASH", "45425c2c16f2c177c71b5748fb87c3ad")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6024380614:AAET6k4iKbyJ0mA_XkLsxos9h_L0pQ3Ubkg")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "kinepeb936")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kinepeb936:sakar5555@cluster0.4ojjoud.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "951824622")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(951824622)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001958041628")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "DS_backup") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "False") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
