from datetime import date
import requests
import json
***REMOVED***

***REMOVED***
    # SMS API
***REMOVED***
***REMOVED***
        self.sid = "ACee548b3d3a3ca065d5d5b9fb1365b68a"
        self.token = "19db7675835fb06950fdc10868061867"
        self.from_num = '+17577932654'
        self.to_num = '+917322995777'
        
***REMOVED***
***REMOVED***
***REMOVED***

    def send_notification(self, message_dict):
        message = self.create_message(message_dict)
        print(message)