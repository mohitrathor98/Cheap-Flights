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
            "location_types": "airport"
        }
        response = requests.get(url=f"{self.tequila_url}/locations/query", headers=self.tequila_header, params=query)
        response.raise_for_status
        response = response.json()

        for location in response['locations']:
            if location['timezone'] == "Asia/Kolkata":
                return location['city']['code']
    
    def search_flights(self, dest):

        tomorrow = datetime.now() + timedelta(1)
        six_months = datetime.now() + timedelta(180)
        query = {
            "fly_from": "PAT",
            "fly_to": dest,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "curr": "INR",
            "partner_market": "in"
        }
        url = f"{self.tequila_url}/v2/search"
        response = requests.get(url=url, headers=self.tequila_header, params=query)
        response.raise_for_status
        return response.json()['data']