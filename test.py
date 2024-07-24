from add_stock import stock_data_microservice

confirmation = input("Would you like to request data from the Stock Data Microservice? 1 for YES, 2 for NO: ")

if confirmation == "1":
    sym_input = input("Enter the ticker of stock you would like to see: ")
    api_input = input("Enter your API key: ")

    gather_stock = stock_data_microservice(sym_input, api_input)
    print(gather_stock)
elif confirmaton == "2":
    print("Exiting program")
