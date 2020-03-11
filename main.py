import robin_stocks
import datetime
import time
from InvestmentPortfolio import InvestmentPortfolio

robin_stocks.authentication.login(username="hassonatlee@yahoo.com", password="ChiefAt033100", by_sms=True, store_session=True)

initial_investment_capital = float(input("How much money would you like to start with? "))

MyPortfolio = InvestmentPortfolio(initial_investment_capital)

def printHelp():
  print("-h: print list of commands")
  print("-ticker name: print the name of the company associated with the given stock ticker")
  print("-option price")
  print("-q: quit the program")

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
    option_type = input("call or put: ")
    option_price = float((robin_stocks.options.get_option_market_data(option_ticker, expiration_date, strike_price, option_type, 'adjusted_mark_price')))
    print(f"${round(option_price * 100)}")
  elif(userInput == "-q"):
    running = False

    
