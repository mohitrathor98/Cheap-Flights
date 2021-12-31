import json
import requests

from flight_search import FlightSearch
class DataManager:
    # interacting with sheety apis
    def __init__(self) -> None:
        self.sheety_url = "URL FOR SHEETY SPREADSHEET"
        self.sheety_header = { "Authorization": "Bearer SHEETY_TOKEN" }
        self.flight_api = FlightSearch()
        self.flight_sheet_data = None
        self.user_data = None
        
    def read_flight_data(self):
        response = requests.get(url=f"{self.sheety_url}/prices", headers=self.sheety_header)
        response.raise_for_status
        self.flight_sheet_data = response.json()
    
    def get_user_data(self):
        response = requests.get(url=f"{self.sheety_url}/users", headers=self.sheety_header)
        response.raise_for_status
        self.user_data = response.json()
    
    def insert_iata(self):
        self.read_flight_data()
        self.get_user_data()
        body = {
            "price": {
                "iataCode": None
            }
        }
        for index,city in enumerate(self.flight_sheet_data['prices']):
            if city['iataCode'] == '':
                iata = self.flight_api.get_iata(city['city'])
                self.flight_sheet_data['prices'][index]['iataCode'] = iata
                
                # put iata to sheety
                body['price']['iataCode'] = iata
                response = requests.put(url=f"{self.sheety_url}/prices/{city['id']}", headers=self.sheety_header, json=body)
                response.raise_for_status
                
    def post_user_data(self, first_name, last_name, email):
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=f"{self.sheety_url}/users", headers=self.sheety_header, json=body)
        response.raise_for_status
        