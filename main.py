import robin_stocks
from InvestmentPortfolio import InvestmentPortfolio

robin_stocks.authentication.login(username="hassonatlee@yahoo.com", password="ChiefAt033100", by_sms=True, store_session=True)

initial_investment_capital = float(input("How much money would you like to start with? "))

MyPortfolio = InvestmentPortfolio(initial_investment_capital)

def printHelp():
  print("-h : print list of commands")
  print("-ticker name: print the name of the company associated with the given stock ticker")

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
  elif(userInput == "-q"):
    running = False

    
