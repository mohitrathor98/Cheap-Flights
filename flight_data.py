from flight_search import FlightSearch


class FlightData:
    #This class is responsible for structuring the flight data.
***REMOVED***
        self.flight_api = FlightSearch()
    
    
    def compare_prices(self, flight_data):
        
        for data in flight_data:
            if data['price'] < 5000 and len(data['route']) == 1:
                date_time = data['local_departure'].split('T')
                date_time = date_time[0] + " " + date_time[1][:-5]
                print(f"{data['cityFrom']} : {data['cityCodeFrom']} : {data['cityTo']} : {data['cityCodeTo']} : {data['price']} : {date_time}")
            

    def check_prices(self, sheet_data):
        # TODO:
        # do sheet_data['prices'] here
        # in search_flights do city['iataCode']
        for city in sheet_data:
            flight_data = self.flight_api.search_flights(city)
            self.compare_prices(flight_data)