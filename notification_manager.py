from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.sid = "YOUR TWILIO SID"
        self.token = "YOUR TWILIO TOKEN"
        self.from_num = 'YOUR TWILIO SENDING NUMBER'
        self.to_num = 'YOUR PHONE NUMBER SETUP ON TWILIO'
        
    def create_message(self, message_dict):
        message = f"Low Price Alert!\nonly Rs.{message_dict['price']} to fly from {message_dict['dep_city']}-{message_dict['dep_city_code']} to {message_dict['dest_city']}-{message_dict['dest_city_code']} on {message_dict['day']}"
        if message_dict['connecting']:
            message += f"\nFlight is connecting via {message_dict['stoppage']}"
        return message

    def send_mails(self, message, dest_city, recipient):
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="YOUR SENDING MAIL", password="YOUR MAIL PASSWORD")
                connection.sendmail(
                    from_addr = "YOUR SENDING MAIL", 
                    to_addrs = recipient, 
                    msg = f"Subject:Flight to {dest_city}\n\n{message}"
                )
        except Exception as e:
            print("Can't send mail due to ", e)

    def send_notification(self, message_dict, user_data):
        try:
            message = self.create_message(message_dict)
            client = Client(self.sid, self.token)
            response = client.messages.create(body=message, from_=self.from_num, to=self.to_num)
        except Exception as e:
            print(e)
        else:
            print(response)
        
        # sending mails
        for user in user_data['users']:
            self.send_mails(message, message_dict['dest_city'], user['email'])