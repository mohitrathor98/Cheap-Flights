from data_manager import DataManager
from flight_data import FlightData

# TODO:
# export all the tokens and ids in form of string dictionary
# and use json.loads to convert it back

# ask user departure city name

spreadsheet = DataManager()
# spreadsheet.insert_iata()

# flight = FlightData()
# flight.check_prices(spreadsheet.sheet_data)

print("Welcome to Cheepest Flight Search\nWe find the best deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
counter = 0
while counter<3:
    email = input("What is your email?\n").lower()
    confirm_email = input("Type your email again.\n").lower()
    if email == confirm_email:
        break
    counter += 1
    print("\nCan't validate email\n")
    
if counter==3:
    print("We can't validate your email. Sorry")
else:
    spreadsheet.post_user_data(first_name, last_name, email)
    print("You're registered.")
