# Microservice A: Adding Stock Info
This microservice aims to gather stock info from a user inputed ticker, making an API call to do so. The stock info for the specific ticker will be gathered
and displayed in the CLI while being saved into the stock.txt file.

## Required Installation

Users will need to install the following:

```bash
pip install requests pyzmq python-dotenv
```

## How to programmatically RECEIVE data

Within the .env file, users will need to enter their API key. An example is shown below:

```.env
YOUR_API_KEY ="Enter Your API Key"
```

Once users have entered their API key within .env, they must then run the add_stock.py program. This must be done PRIOR to running request.py

## How to programmatically REQUEST data

Users will need to **run the request.py file in order to programmantically REQUEST data**. This code will send a request to add_stock.py. Below is an example call 
using the AAPL ticker (Normally, the user will need to enter a ticker):

```python
sym_input = "AAPL"
socket.send_json({"symbol": sym_input})     # Ticker from user sent in JSON format
stock_data = socket.recv_string()           # Receive data from specified ticker
print(stock_data)
```
"sym_input" will, in actual practice, be where the program will ask for a ticker from the user. The user will be asked and will enter the ticker within the CLI.


