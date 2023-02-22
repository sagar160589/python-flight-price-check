import requests,os,json
SHEETY_API_ENDPOINT_URL = 'https://api.sheety.co/a0e8dc7d825de4056cc1e10ae8de2e47/myFlightSearch/prices'
SHEETY_TOKEN = os.getenv('SHEETY_API_TOKEN')


class FlightData:

    def __init__(self):
        self.city = ''
        self.iata_code = ''
        self.low_price = ''
        self.params = {
            'Authorization': SHEETY_TOKEN
        }
        self.flight_data = ''

    def get_user_ip_from_city(self):
        user_from_city_input = input("From which city you want to take the flight? ")
        with open("iatacodes.json", mode='r') as iata:
            iata_codes = json.load(iata)
        return {user_from_city_input:iata_codes[user_from_city_input]}

    def get_flight_data(self):
        flight_data_response = requests.get(SHEETY_API_ENDPOINT_URL, headers=self.params)
        return flight_data_response.json()

    def update_flight_data(self):
        with open('flight_data.json', mode='r') as data:
            self.flight_data = json.load(data)
            for data1 in self.flight_data['prices']:
                post_param = {
                    "price":{
                        'city': data1['city'],
                        'iataCode': data1['iataCode'],
                        'lowestPrice': data1['lowestPrice']
                    }

                }
                post_resp = requests.post(SHEETY_API_ENDPOINT_URL, json=post_param, headers=self.params)
                print(post_resp.text)



