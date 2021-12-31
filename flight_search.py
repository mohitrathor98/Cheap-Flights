import requests
from datetime import datetime,timedelta
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.tequila_url = "https://tequila-api.kiwi.com"
        self.tequila_header = {"apikey": "YOUR TEQUILA TOKEN"}
        
    def get_iata(self, city):
        
        query = {
            "term": city,
            "location_types": "airport"
        }
        response = requests.get(url=f"{self.tequila_url}/locations/query", headers=self.tequila_header, params=query)
        response.raise_for_status
        response = response.json()

        for location in response['locations']:
            if location['city']['name'] == city.title():
                return location['city']['code']
    
    def search_flights(self, dept, dest):

        tomorrow = datetime.now() + timedelta(1)
        six_months = datetime.now() + timedelta(180)
        query = {
            "fly_from": dept,
            "fly_to": dest,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "curr": "INR",
            "partner_market": "in",
            "max_stopovers": 2
        }
        url = f"{self.tequila_url}/v2/search"
        response = requests.get(url=url, headers=self.tequila_header, params=query)
        response.raise_for_status
        return response.json()['data']