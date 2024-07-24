from add_stock import stock_data_microservice

sym_input = input("Enter the ticker of stock you would like to see: ")
api_input = input("Enter your API key: ")

gather_stock = stock_data_microservice(sym_input, api_input)
print(gather_stock)