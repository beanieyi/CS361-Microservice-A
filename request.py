import zmq

# Create zmq context, a socket to send, and connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Confirm or exit program input
confirmation = input("Would you like to request data from the Stock Data Microservice? 1 for YES, 2 for NO: ")

# Enter ticker to be viewed in CLI and added to txt file
if confirmation == "1":
    sym_input = input("Enter the ticker of stock you would like to see: ")
    socket.send_json({"symbol": sym_input})     # Ticker from user sent in JSON format
    stock_data = socket.recv_string()           # Receive data from specified ticker
    print(stock_data)
elif confirmation == "2":
    print("Exiting program")
