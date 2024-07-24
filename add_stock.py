# Code heavily inspired by example code on https://api-ninjas.com/api/stockprice

import requests

def stock_data_microservice(symbol, YOUR_API_KEY):
    """
    Fetch data from API from a certain stock

    Args:
        symbol: ticker of stack you want to get data from
        YOUR_API_KEY: API Key needed to access the API
    """

    api_url = f'https://api.api-ninjas.com/v1/stockprice?ticker={symbol}'

    # API request
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})

    # If request goes through, print the data of the stock, else give error message
    if response.status_code == requests.codes.ok:
        data = response.text

        # Put stock data into a txt file
        with open('stock.txt', 'w') as file:
            file.write(data)
        return data             # To see in CLI

    else:
        print("Error")
        return