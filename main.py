from data_manager import DataManager
from flight_data import FlightData

# TODO:
# export all the tokens and ids in form of string dictionary
# and use json.loads to convert it back

# ask user departure city name

spreadsheet = DataManager()
spreadsheet.insert_iata()

flight = FlightData()
flight.check_prices(spreadsheet.sheet_data)

