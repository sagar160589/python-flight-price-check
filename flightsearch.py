import requests,os,datetime as dt

FLIGHT_SEARCH_ENDPOINT_API= 'https://api.tequila.kiwi.com/v2/search?'
FLIGHT_API_TOKEN = os.getenv('FLIGHT_TOKEN')

class FlightSearch:
    def __init__(self):
        self.fly_from = ''
        self.fly_to = '',
        self.date_from = self.get_current_date()
        self.date_to = self.get_future_date()
        self.search_params = {
            'apikey': FLIGHT_API_TOKEN
        }
        self.my_price=''
        self.city_from = ''


    def get_future_date(self):
        future_date = dt.datetime.now()+dt.timedelta(days=15)
        return future_date.date().strftime('%d/%m/%Y')

    def get_current_date(self):
        return dt.datetime.now().date().strftime('%d/%m/%Y')

    def search_flight(self, fly_from, fly_to):
        # search_flight_response = requests.get(f"FLIGHT_SEARCH_ENDPOINT_API?fly_from={self.fly_from}&fly_to={self.fly_to}&dateFrom={self.date_from}&dateTo={self.date_to}",
        #                                       headers=self.search_params)
        params = {
            'fly_from': self.fly_from,
            'fly_to': self.fly_to,
            'dateFrom': self.date_from,
            'dateTo': self.date_to

        }
        search_flight_response = requests.get(FLIGHT_SEARCH_ENDPOINT_API, params=params, headers=self.search_params)

        return search_flight_response.json()

    def check_prices(self,flight_data_list,my_price):
        for data in flight_data_list:
            if data['price'] <= int(my_price):
                return data



