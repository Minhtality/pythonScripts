from discord import SyncWebhook
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

discord_url = os.getenv('DISCORD_URL')
webhook = SyncWebhook.from_url(discord_url)

# if date is first day of the month

today = datetime.date.today()
if today.day == 1:
    message = "@here Your rent is due."
    webhook.send(message)
