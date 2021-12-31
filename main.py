from data_manager import DataManager
from flight_data import FlightData

# TODO:
# export all the tokens and ids in form of string dictionary
# and use json.loads to convert it back

# make for foreign flights
# make for connecting flights
spreadsheet = DataManager()
flight = FlightData()

print("Welcome to Cheepest Flight Search\nWe find the best deals and email you.\n")
choice = input("Please choose:\n1) Add a subscriber\n2) Run a search\n")
if choice == "1":

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
        
elif choice == "2":    
    dept_city = input("Enter departure city: ")
    print("Running search....")
    spreadsheet.insert_iata()
    flight.check_prices(dept_city, spreadsheet.flight_sheet_data, spreadsheet.user_data)


