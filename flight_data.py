from flight_search import FlightSearch
from notification_manager import NotificationManager


class FlightData:
    #This class is responsible for structuring the flight data.
***REMOVED***
        self.flight_api = FlightSearch()
        self.notifi_api = NotificationManager()
    
    
    def compare_prices(self, flight_data, cutoff_price, user_data):
        
***REMOVED***
            for data in flight_data:
                if data['price'] < cutoff_price and len(data['route']) == 1:
                    day = data['local_departure'].split('T')
                    day = day[0]
                    self.notifi_api.send_notification({ 
                        "dep_city":data['cityFrom'], 
                        "dep_city_code":data['cityCodeFrom'], 
                        "dest_city":data['cityTo'], 
                        "dest_city_code":data['cityCodeTo'], 
                        "price":data['price'], 
                        "day":day 
                    }, user_data)
                    break
***REMOVED***
            # no flight data is present
***REMOVED***

    def check_prices(self, sheet_data, user_data):
        for city in sheet_data['prices']:
            flight_data = self.flight_api.search_flights(city['iataCode'])
            self.compare_prices(flight_data, city['lowestPrice'], user_data) 