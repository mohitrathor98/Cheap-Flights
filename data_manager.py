import requests

from flight_search import FlightSearch
class DataManager:
    # interacting with sheety apis
***REMOVED***
        self.sheety_url = "https://api.sheety.co/407a967edb3e231ee6c7f637d95bbfb6/flightDeals/prices"
        self.sheety_header = { "Authorization": "Bearer igotyoumoonlightyouremystarlight21323cmmondancewithme" }
        self.flight_api = FlightSearch()
        self.sheet_data = None
        
    def read_from_sheet(self):
        response = requests.get(url=self.sheety_url, headers=self.sheety_header)
        response.raise_for_status
        self.sheet_data = response.json()
    
    def insert_iata(self):
        self.read_from_sheet()
        body = {
            "price": {
                "iataCode": None
            }
        }
        for index,city in enumerate(self.sheet_data['prices']):
            if city['iataCode'] == '':
                iata = self.flight_api.get_iata(city['city'])
                self.sheet_data['prices'][index]['iataCode'] = iata
                
                # put iata to sheety
                body['price']['iataCode'] = iata
                response = requests.put(url=f"{self.sheety_url}/{city['id']}", headers=self.sheety_header, json=body)
                response.raise_for_status
        
            
