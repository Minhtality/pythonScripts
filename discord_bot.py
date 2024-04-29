from discord import SyncWebhook
from dotenv import load_dotenv
import os

load_dotenv()

discord_url = os.getenv('DISCORD_URL')
webhook = SyncWebhook.from_url(discord_url)
webhook.send("@everyone This is a test message.")
