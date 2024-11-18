# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20789690"))
API_HASH = getenv("API_HASH", "fb532f92355084d89668977d7ceb7b9e")
BOT_TOKEN = getenv("BOT_TOKEN", "7314814493:AAGCorL-WpPOOGGc-VnM4ITiTl_p2OAeoBo")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://kajaldhakad80:r7TQgw792ubhx0EN@cluster0.ubq2r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
