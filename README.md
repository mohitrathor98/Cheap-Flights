# Cheap-Flights
Project searches for flights costing less than given rate and sends details as SMS and mail.

---
**Add all required API authentication data in the program.**</br>
---
</br>
Users are provided with two options:</br>
1) To subscribe, where users will be mailed whenever a cheap flight is avialable<br>
2) To search for a cheap flight</br>
</br>
Two Sheets are being used:</br>
1) Prices sheet: This contains destination city, iata code and cutoff price.</br>
2) Users sheet: This contains First name, Last name and emails of subscribed users.
</br>

## APIs Required

### Posting data to spreadsheet
1) Program uses <a href="https://sheety.co/">Sheety APIs</a> to post data on google spreadsheet.
2) Sheety needs to be connected with google account with read and write permissions.
3) Bearer TOKEN and SHEET_POINT is required.

### Searching Flights
1) Program uses <a href="https://tequila.kiwi.com/portal/docs/tequila_api">Tequila APIs</a> to 
   search for flights
2) Tequila token is required

### Sending Notifications
1) Program uses <a href="https://www.twilio.com/docs/sms">Twilio API</a> to send notifications.
2) Twilio SID, Token, from and to numbers are required.
  