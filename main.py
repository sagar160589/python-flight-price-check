from flightdata import FlightData
from flightsearch import FlightSearch
import datetime as dt
from messanger import Messenger

flight_data = FlightData()
flight_data_details_resp = flight_data.get_flight_data()
flight_data_list = flight_data_details_resp['prices']
flight_search = FlightSearch()
messanger = Messenger()
flight_search.fly_from = flight_data.get_user_ip_from_city()
for (city,iata) in flight_search.fly_from.items():
    flight_search.city_from = city
    flight_search.fly_from = iata
for flight in flight_data_list:
    flight_search.fly_to = flight['iataCode']
    flight_search.my_price = flight['lowestPrice']
    flight_search_response = flight_search.search_flight(flight_search.fly_from, flight_search.fly_to)
    cheap_price_details = flight_search.check_prices(flight_search_response['data'],flight_search.my_price)
    if cheap_price_details is not None:
        print(f"Lowest price found for {cheap_price_details['price']}")
        lowest_price = cheap_price_details['price']
        departure_date = cheap_price_details['utc_departure'].split("T")[0]
        arrival_date = cheap_price_details['utc_arrival'].split("T")[0]
        messanger.send_sms(flight_search.city_from,flight['city'],departure_date,arrival_date, lowest_price)

