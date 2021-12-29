#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

spreadsheet = DataManager()
flight = FlightSearch()

spreadsheet.insert_iata()
flight.search_flights(spreadsheet.sheet_data)