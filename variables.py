import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

PICS = os.environ.get("PICS", "https://telegra.ph/file/54719212c505f89953c39.jpg").split()

ADMIN = os.environ.get("ADMIN", "5696423555")

DB_URL = os.environ.get("DB_URL", "")

DB_NAME = os.environ.get("DB_NAME", "")

RemoveBG_API = os.environ.get("RemoveBG_API", "")

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
 
log_channel = environ.get("LOG_CHANNEL")

LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

LOG_TEXT = """<i><u>ποΈβπ¨οΈUSER DETAILS</u>

β ID : <code>{id}</code>
β DC : <code>{dc_id}</code>
β First Name : <code>{first_name}<code>
β UserName : @{username}

By = {bot}</i>"""












