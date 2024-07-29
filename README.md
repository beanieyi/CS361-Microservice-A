# Microservice A: Adding Stock Info
This microservice aims to gather stock info from a user inputed ticker, making an API call to do so. The stock info for the specific ticker will be gathered
and displayed in the CLI while being saved into the stock.txt file.

## Required Installation

Users will need to install the following:

```bash
pip install requests pyzmq python-dotenv
```

Users will need to import the following in their request file:

```python
import zmq
```

## How to programmatically RECEIVE data

Within the .env file, users will need to enter their API key. An example is shown below:

```.env
YOUR_API_KEY ="Enter Your API Key"
```

Once users have entered their API key within .env, they must then run the add_stock.py program. This must be done PRIOR to running their request file.

## How to programmatically REQUEST data

Users will need to **run a request file in order to programmantically REQUEST data**. Again, add_stock.py must be running PRIOR to this step. 
The code shown below will send a request to add_stock.py, which you will add to your project:

```python
# Create zmq context, a socket to send, and connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

sym_input = input("Enter the ticker of stock you would like to see: ")                    
socket.send_json({"symbol": sym_input})     # Ticker from user sent in JSON format
stock_data = socket.recv_string()           # Receive data from specified ticker
print(stock_data)
```
"sym_input" is be where the code will ask for a ticker from the user. The user will be asked and will enter the ticker within the CLI.

An example call would look like this:

```python
    sym_input = "AAPL"                  
    socket.send_json({"symbol": sym_input})     # Ticker from user sent in JSON format
    stock_data = socket.recv_string()           # Receive data from specified ticker
    print(stock_data)
```

## UML sequence diagram 


