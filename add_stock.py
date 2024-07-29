# Code heavily inspired by example code on https://api-ninjas.com/api/stockprice and CS361 Assignment 4

import requests
import zmq
import os
from dotenv import load_dotenv

def stock_data_microservice(symbol):
    """
    Fetch data from API from a certain stock

    Args:
        symbol: ticker of stack you want to get data from
        YOUR_API_KEY: API Key needed to access the API
    """

    api_url = f'https://api.api-ninjas.com/v1/stockprice?ticker={symbol}'

    # Get API key from .env file and request API
    load_dotenv()
    API_KEY = os.getenv('YOUR_API_KEY')
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    # If request goes through, print the data of the stock, else give error message
    if response.status_code == requests.codes.ok:
        data = response.text

        # Put stock data into a txt file
        with open('stock.txt', 'a') as file:
            file.write("\n" + data)
        return data             # To see in CLI
    else:
        error_mess = "Error: Could not retrieve data."
        return error_mess

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Receive JSON message, extract info, fetch ticker info, and send data back to client
while True:
    message = socket.recv_json()
    symbol = message['symbol']
    stock_data = stock_data_microservice(symbol)
    socket.send_string(stock_data)