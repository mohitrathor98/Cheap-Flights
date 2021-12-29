import requests
class DataManager:
    
***REMOVED***
        self.sheety_url = "https://api.sheety.co/407a967edb3e231ee6c7f637d95bbfb6/flightDeals/prices"
        self.sheety_header = { "Authorization": "Bearer igotyoumoonlightyouremystarlight21323cmmondancewithme" } 
        self.tequila_url = "https://tequila-api.kiwi.com"
        self.tequila_header = {"apikey": "e4X5g2dGr4YXwfUgIbAs92hVwAPhS7e0"}
        
    def read_from_sheet(self):
        #{'prices': [{'city': 'Mumbai', 'iataCode': '', 'lowestPrice': 3000, 'id': 2}, {'city': 'Bangalore', 'iataCode': '', 'lowestPrice': 3000, 'id': 3},
        # {'city': 'Delhi', 'iataCode': '', 'lowestPrice': 2000, 'id': 4}, {'city': 'Hyderabad', 'iataCode': '', 'lowestPrice': 3000, 'id': 5}]}
        response = requests.get(url=self.sheety_url, headers=self.sheety_header)
        response.raise_for_status
        return response.json()
    
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
    
    def insert_iata(self):
        sheet_values = {
            'prices': [
                {'city': 'Mumbai', 'iataCode': '', 'lowestPrice': 3000, 'id': 2}, 
                {'city': 'Bangalore', 'iataCode': '', 'lowestPrice': 3000, 'id': 3},
                {'city': 'Delhi', 'iataCode': '', 'lowestPrice': 2000, 'id': 4}, 
                {'city': 'Hyderabad', 'iataCode': '', 'lowestPrice': 3000, 'id': 5}
                ]
            }
        
        for city in sheet_values['prices']:
            iata = self.get_iata(city['city'])
            
