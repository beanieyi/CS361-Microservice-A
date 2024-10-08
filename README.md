# Microservice A: Adding Stock Info
This microservice aims to gather stock info from a user inputed ticker, making an API call to do so. The stock info for the specific ticker will be gathered
and displayed in the CLI while being saved into the stock.txt file.

## Required Installation, Imports, and API

Users will need to install the following:

```bash
pip install requests pyzmq python-dotenv
```

Users will need to import the following in the file containing the request code:

```python
import zmq
```

Users wil also need to get an API Key from https://api-ninjas.com/api/stockprice. Users must make an account on the given site to obtain an API key.

## How to programmatically RECEIVE data

Within the .env file, users will need to enter their API key. An example is shown below:

```.env
YOUR_API_KEY ="Enter Your API Key"
```

Once users have entered their API key within .env, they must then run the add_stock.py microservice. The microservice calls an API to retreive data associated with the user inputted stock ticker.

The microservice can be run using the following in the Terminal:
```bash
python add_stock.py
```

## How to programmatically REQUEST data

Users will need to **run a file containing the below request code in order to programmantically REQUEST data**. Note, add_stock.py must be running PRIOR to this step. After running the add_stock.py microservice, users will need to open a new terminal and run their request code.

This is the request code that you will add to your project:

```python
# Create zmq context, a socket to send, and connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

sym_input = input("Enter the ticker of stock you would like to see: ")                    
socket.send_json({"symbol": sym_input})     # Ticker sent via JSON to microservice
stock_data = socket.recv_string()           # Receive data from microservice
print(stock_data)
```
"sym_input" is where the code will ask for a ticker from the user. The user will be asked and will enter the ticker within the CLI.

An example call would look like this:

```python
    sym_input = "AAPL"                  
    socket.send_json({"symbol": sym_input})     # Ticker sent via JSON to microservice
    stock_data = socket.recv_string()           # Receive data from microservice
    print(stock_data)
```

## UML Sequence Diagram 

![UMLSCREENSHOT](https://github.com/user-attachments/assets/c63edd2c-2c98-4cf2-9139-83d40292ce13)

