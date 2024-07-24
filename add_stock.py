# Code heavily inspired by example code on https://api-ninjas.com/api/stockprice

import requests

symbol = input("Write the ticker of the stock you would like to view: ")
api_url = f'https://api.api-ninjas.com/v1/stockprice?ticker={symbol}'

# API request
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})

# If request goes through, print the data of the stock, else give error message
if response.status_code == requests.codes.ok:
    print(response.text)

    # Put stock data into a txt file
    with open('stock.txt', 'w') as file:
        file.write(response.text)
else:
    print("Error:", response.status_code, response.text)