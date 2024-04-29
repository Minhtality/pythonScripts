
# import googlemaps
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
# GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
# HOME_LOCATION = os.getenv('HOME_LOCATION')
# WORKPLACE_LOCATION = os.getenv('WORK_LOCATION')


def send_text_message(message):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_phone_number = os.getenv('TWILIO_NUMBER')
    my_phone_number = os.getenv('MY_PHONE_NUMBER')
    client = Client(account_sid, auth_token)

    client.messages.create(
        to=my_phone_number, from_=twilio_phone_number, body=message)


# def get_commute_duration():
#     gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
#     directions_result = gmaps.directions(
#         HOME_LOCATION, WORKPLACE_LOCATION, mode="driving", departure_time=datetime.now())
#     first_leg = directions_result[0]['legs'][0]
#     duration = first_leg['duration']['text']
#     return duration


def main():
    # now = datetime.now()
    # duration = (get_commute_duration().split()[0])
    # arrival_time = (now + timedelta(minutes=int(duration))
    #                 ).strftime("%I:%M %p")

    message = f"This is a test message."
    send_text_message(message)


if __name__ == "__main__":
    main()
