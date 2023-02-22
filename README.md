# python-flight-price-check

This project focuses on checking the flight prices for next 15 days and gives back the low price alert response.
1.Here first we create a Goggle Spreadsheet and post the data containing the city we want to travel, the IATA code of the city and our price that we want to using Sheety API. This is one time activity and data is posted through Sheety API from flight_data.json file.
2.Later on the code focuses on using tequila-kiwi flights api to search for flights from the city we want to travel to the citites mentioned in the Googlespreadsheet.
3.The city we want to travel is a user input which is taken from the iatacodes.json file.
4.The response that we get from the tequila-kiwi flights search api gives us back the response for all the flights travelling within 15 days and then the prices along with that.
5.The prices are compared with our prices from the google spreadsheet and the prices from the response which is lower than or equal to our price is the low alert price for us.
6.This low alert price message is then sent to us via Twilio account SMS with the flight details.
