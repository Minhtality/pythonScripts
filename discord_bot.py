import requests
from discord import SyncWebhook
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

discord_url = os.getenv('DISCORD_URL')
forex_api_key = os.getenv('FOREX_API_KEY')
webhook = SyncWebhook.from_url(discord_url)

today = datetime.datetime.now()


def send_reminder_check():
    if today.day == 1:
        message = f"@here, Your rent is due."
        webhook.send(content=message)


def get_usd_to_yen():
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=JPY&base=USD"
    payload = {}
    headers = {
        "apikey": forex_api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        return data['rates']['JPY']
    else:
        return None


if __name__ == "__main__":
    send_reminder_check()

    # Call the function to get the yen to USD exchange rate
    yen_to_usd_rate = get_usd_to_yen()

    if yen_to_usd_rate is not None:
        todayFormat = today.strftime("%m/%d/%Y")
        webhook.send(
            content=f"@here Today ({todayFormat}) USD to YEN exchange rate: {yen_to_usd_rate}")
