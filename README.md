# Microservice A: Adding Stock Info
This microservice aims to gather stock info from a user inputed ticker, making an API call to do so. The stock info for the specific ticker will be gathered
and displayed in the CLI while being saved into the stock.txt file.

## Required Installation/Set-Up

Users will need to install the following:

```bash
pip install requests pyzmq python-dotenv
```
Users will also need to input their API key into the provided .env file.

## How to programmatically REQUEST data

Users will need to rurn the request.py file in order to programmantically REQEST data. This code will send a request to add_stock.py. Below is an example call 
using the AAPL ticker (Normally, the user will need to enter a ticker):

```python
import zmq

# Create zmq context, a socket to send, and connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Confirm or exit program input
confirmation = input("Would you like to request data from the Stock Data Microservice? 1 for YES, 2 for NO: ")

# Enter ticker to be viewed in CLI and added to txt file
if confirmation == "1":
    sym_input = "AAPL"
    socket.send_json({"symbol": sym_input})     # Ticker from user sent in JSON format
    stock_data = socket.recv_string()           # Receive data from specified ticker
    print(stock_data)
elif confirmation == "2":
    print("Exiting program")
```
