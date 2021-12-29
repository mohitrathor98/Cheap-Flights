from flight_search import FlightSearch


class FlightData:
    #This class is responsible for structuring the flight data.
***REMOVED***
        self.flight_api = FlightSearch()
    
    
    def compare_prices(self, flight_data):
        for data in flight_data:
            print(f"{data['cityTo']} : {data['price']}", end=' ')
            if len(data['route']) > 1:
                print("connecting")
    ***REMOVED***
                print()
            

    def check_prices(self, sheet_data):
        # TODO:
        # do sheet_data['prices'] here
        # in search_flights do city['iataCode']
        for city in sheet_data:
            flight_data = self.flight_api.search_flights(city)
            self.compare_prices(flight_data)