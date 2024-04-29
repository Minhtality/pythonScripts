from discord import SyncWebhook
import os

discord_url = os.getenv('DISCORD_URL')
webhook = SyncWebhook.from_url(discord_url)
webhook.send("Hello World")
