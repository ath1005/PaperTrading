import robin_stocks
import datetime
import time
from StockOption import StockOption
from InvestmentPortfolio import InvestmentPortfolio

robin_stocks.authentication.login(username="hassonatlee@yahoo.com", password="ChiefAt033100", by_sms=True, store_session=True)

initial_investment_capital = float(input("How much money would you like to start with? "))

MyPortfolio = InvestmentPortfolio(initial_investment_capital)

def printHelp():
  print("-h: Print list of commands")
  print("-ticker name: Print the name of the company associated with the given stock ticker")
  print("-option price: Get the current price of 1 option contract with the given information")
  print("-buy option: Purchase option contract(s)")
  print("-buying power: Print the current buying power in the Investment Portfolio")
  print("-q: Quit the program")

def getOptionPrice(stock_ticker, expiration_date, strike_price, option_type):
  return float((robin_stocks.options.get_option_market_data(option_ticker, expiration_date, strike_price, option_type, 'adjusted_mark_price')))

running = True
while running:
  userInput = input("Please enter a command, or type -h for help: ")

  if(userInput == "-h"):
    printHelp()

  elif(userInput == "-ticker name"):
    ticker = input("Enter stock ticker: ")
    stock_name = robin_stocks.stocks.get_name_by_symbol(ticker)
    if(stock_name == ""):
      print("Invalid stock ticker!")
    else:
      print(stock_name)

  elif(userInput == "-option price"):
    option_ticker = input("Stock ticker: ")
    expiration_date = input("Expiration date (YYYY-MM-DD): ")
    strike_price = input("Strike price: ")
    option_type = input("Option type:")
    option_price = getOptionPrice(option_ticker, expiration_date, strike_price, option_type)
    print(f"${round(option_price * 100)}")

  elif(userInput == "-buy option"):
    option_ticker = input("Stock ticker: ")
    expiration_date = input("Expiration date: ")
    strike_price = input("Strike price: ")
    option_type = input("Option type: ")
    quantity = input("Number of contracts: ")
    option_price = getOptionPrice(option_ticker, expiration_date, strike_price, option_type)
    option = StockOption(option_ticker, expiration_date, strike_price, option_type)
    if(MyPortfolio.buyOption(option, option_price, quantity)):
      print("Transaction successful!")
      print(option)
    else:
      print("Transaction unsuccessful: You do not have enough buying power to purchase the requested number of option contracts")
      print(f"Buying power: {MyPortfolio.getBuyingPower()}")

  elif(userInput == "-p"):
    MyPortfolio.printOptions()

  elif(userInput == "-buying power"):
    print(MyPortfolio.getBuyingPower())

  elif(userInput == "-q"):
    running = False

    
