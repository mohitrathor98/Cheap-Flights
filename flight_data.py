from flight_search import FlightSearch
from notification_manager import NotificationManager


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.flight_api = FlightSearch()
        self.notifi_api = NotificationManager()
    
    
    def compare_prices(self, flight_data, cutoff_price, user_data):
        
        try:
            for data in flight_data:
                if data['price'] < cutoff_price:
                    connecting = False
                    stoppage = None
                    if len(data['route']) > 1:
                        connecting = True
                        stoppage = data['route'][0]["cityTo"]
                    
                    day = data['local_departure'].split('T')
                    day = day[0]
                    self.notifi_api.send_notification({ 
                        "dep_city":data['cityFrom'], 
                        "dep_city_code":data['cityCodeFrom'], 
                        "dest_city":data['cityTo'], 
                        "dest_city_code":data['cityCodeTo'], 
                        "price":data['price'], 
                        "day":day ,
                        "connecting": connecting,
                        "stoppage": stoppage
                    }, user_data)
                    break
                
        except Exception as e:
            # no flight data is present
            print(e)

    def check_prices(self, dept_city, sheet_data, user_data):
        for city in sheet_data['prices']:
            flight_data = self.flight_api.search_flights(dept_city, city['iataCode'])
            self.compare_prices(flight_data, city['lowestPrice'], user_data) 