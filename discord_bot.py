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


def get_usd_exchange_rate():
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=JPY%2CKRW&base=USD"
    payload = {}
    headers = {
        "apikey": forex_api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        return data['rates']['JPY'], data['rates']['KRW']
    else:
        return None


if __name__ == "__main__":
    send_reminder_check()

    # Call the function to get the yen to USD exchange rate
    exchange_rate = get_usd_exchange_rate()
    if exchange_rate:
        jpy, krw = exchange_rate
        message = f"@here: \n JPY to USD: {round(jpy,2)}\n KRW to USD: {round(krw,2)}"
        webhook.send(content=message)
    else:
        message = "Failed to get the exchange rate."
        webhook.send(content=message)
