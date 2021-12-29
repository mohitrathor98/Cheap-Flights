from flight_search import FlightSearch


class FlightData:
    #This class is responsible for structuring the flight data.
***REMOVED***
        self.flight_api = FlightSearch()
    
    
    def check_prices(self, sheet_data):
        
        for city in sheet_data['prices']:
            self.flight_api.search_flights(city['iataCode'])