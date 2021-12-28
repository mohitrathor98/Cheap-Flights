import requests
class DataManager:
    
***REMOVED***
        self.sheety_url = "https://api.sheety.co/407a967edb3e231ee6c7f637d95bbfb6/flightDeals/prices"
        self.sheety_header = { "Authorization": "Bearer igotyoumoonlightyouremystarlight21323cmmondancewithme" } 
        self.tequila_url = "https://tequila-api.kiwi.com"
        self.tequila_key = "e4X5g2dGr4YXwfUgIbAs92hVwAPhS7e0"
        
    def read_from_sheet(self):
        response = requests.get(url=self.sheety_url, headers=self.sheety_header)
        response.raise_for_status
        return response.json()
