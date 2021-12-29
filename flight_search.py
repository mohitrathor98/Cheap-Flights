import requests
from datetime import datetime,timedelta
import json
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
***REMOVED***
        self.tequila_url = "https://tequila-api.kiwi.com"
        self.tequila_header = {"apikey": "e4X5g2dGr4YXwfUgIbAs92hVwAPhS7e0"}
        
    def get_iata(self, city):
        query = {
            "term": city,
            "location_types": "airport",
            "limit": 5
        }
        response = requests.get(url=f"{self.tequila_url}/locations/query", headers=self.tequila_header, params=query)
        response.raise_for_status
        response = response.json()
        return response['locations'][0]['city']['code']
    
    def search_flights(self, sheet_data):
        
        tomorrow = datetime.now() + timedelta(1)
        six_months = datetime.now() + timedelta(180)
        query = {
            "fly_from": "PAT",
            "fly_to": None,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y")
        }
        url = f"{self.tequila_url}/v2/search"
        for city in sheet_data['prices']:
            query["fly_to"] = city['iataCode']
            response = requests.get(url=url, headers=self.tequila_header, params=query)
            response.raise_for_status
            with open('data.json', "w+") as file:
                json.dump(response.json(), file, indent=4)