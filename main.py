#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData

# TODO:
# uncomment below lines
# pass spreadsheet.sheet_data in check_prices

# spreadsheet = DataManager()
# spreadsheet.insert_iata()

flight = FlightData()
flight.check_prices(['DEL','BOM','BLR','HYD'])

