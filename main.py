#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData

spreadsheet = DataManager()
spreadsheet.insert_iata()

flight = FlightData()
flight.check_prices(spreadsheet.sheet_data)

