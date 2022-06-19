import re
from dotenv import load_dotenv
from os import getenv

load_dotenv()

id_pattern = re.compile(r'^.\d+$')

# Bot information
session = getenv('SESSION')
SESSION = session if session else 'media_finder_bot'
user_session = getenv('USER_SESSION')
USER_SESSION = user_session if user_session else 'user_bot'
API_ID = int(getenv('API_ID'))
API_HASH = getenv('API_HASH')
BOT_TOKEN = getenv('BOT_TOKEN')
userbot_string_session = getenv('USERBOT_STRING_SESSION')
USERBOT_STRING_SESSION = userbot_string_session if userbot_string_session else 'userbot_bot'

# Bot settings
cache_time = int(getenv('CACHE_TIME'))
CACHE_TIME = cache_time if cache_time else 300 # 5 minutes
use_caption_filter = bool(getenv('USE_CAPTION_FILTER'))
USE_CAPTION_FILTER = use_caption_filter if use_caption_filter else False

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in getenv('ADMINS').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in getenv('CHANNELS').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in getenv('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = getenv('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = getenv('DATABASE_URI')
DATABASE_NAME = getenv('DATABASE_NAME')
COLLECTION_NAME = getenv('COLLECTION_NAME', 'telegram_files')

# Messages
default_start_msg = """
**Hi 🤖 I'm Media Finder bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

start_msg = getenv('START_MSG')
START_MSG = start_msg if start_msg else default_start_msg
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
invite_msg = getenv('INVITE_MSG')
INVITE_MSG = invite_msg if invite_msg else 'Please join my channel @media_finder_bot'