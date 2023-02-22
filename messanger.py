import os
from twilio.rest import Client

twilio_account_sid = os.getenv("twilio_sid")
twilio_auth_token = os.getenv("twilio_token")
twilio_phone_number = os.getenv("twilio_phone")


class Messenger:
    def __init__(self):
        self.client = Client(twilio_account_sid, twilio_auth_token)

    #Send SMS details of stock difference and stock news via twilio api
    def send_sms(self, fly_from, fly_to, departure_date, arrival_date, price):
        message = self.client.messages.create(from_=twilio_phone_number,
                                              to="your phone number",
                                              body=f"Low Price alert!.Book your flight tickets now from {fly_from} to {fly_to} "
                                                   f"at €{price} between {departure_date} and {arrival_date}")

