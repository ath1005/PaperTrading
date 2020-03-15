import robin_stocks
import datetime
import time
from StockOption import StockOption
from InvestmentPortfolio import InvestmentPortfolio
from Commands import printHelp, getStockName, getOptionPrice

try:
  robin_stocks.authentication.login()
except:
  print("Invalid login!")
else:
  f = open("out.txt", "r")
  if f.mode == "r":
    capital = float(f.readline())
    options = dict(f.readline())
    MyPortfolio = InvestmentPortfolio(capital, options)
  else:
    initial_investment_capital = float(input("How much money would you like to start with? "))
    MyPortfolio = InvestmentPortfolio(initial_investment_capital)

  running = True
  while running:
    userInput = input("Please enter a command, or type -h for help: ")

    if(userInput == "-h"):
      printHelp()

    elif(userInput == "-ticker name"):
      ticker = input("Enter stock ticker: ")
      stock_name = getStockName(ticker)
      if(stock_name == ""):
        print("Invalid stock ticker!")
      else:
        print(stock_name)

    elif(userInput == "-option price"):
      option_ticker = input("Stock ticker: ")
      expiration_date = input("Expiration date: ")
      strike_price = input("Strike price: ")
      option_type = input("Option type: ")
      if(getStockName(option_ticker) == ""):
        print("Invalid stock ticker!")
      else:
        option_price = getOptionPrice(option_ticker, expiration_date, strike_price, option_type)
        print(f"${round(option_price * 100)}")

    elif(userInput == "-buy option"):
      option_ticker = input("Stock ticker: ")
      expiration_date = input("Expiration date: ")
      strike_price = input("Strike price: ")
      option_type = input("Option type: ")
      quantity = input("Number of contracts: ")
      if(getStockName(option_ticker) == ""):
        print("Invalid stock ticker!")
      else:
        option_price = getOptionPrice(option_ticker, expiration_date, strike_price, option_type)
        if(option_price):
          option = StockOption(option_ticker, expiration_date, strike_price, option_type)
          if(MyPortfolio.buyOption(option, option_price, quantity)):
            print("Transaction successful!")
          else:
            print("Transaction unsuccessful: \nYou do not have enough buying power to purchase the requested number of option contracts")
            print(f"Buying power: ${MyPortfolio.getBuyingPower():.4f}")

    elif(userInput == "-sell option"):
      option_ticker = input("Stock ticker: ")
      expiration_date = input("Expiration date: ")
      strike_price = input("Strike price: ")
      option_type = input("Option type: ")
      quantity = input("Number of contracts: ")
      if(getStockName(option_ticker) == ""):
        print("Invalid stock ticker!")
      else:
        option = StockOption(option_ticker, expiration_date, strike_price, option_type)
        option_price = getOptionPrice(option_ticker, expiration_date, strike_price, option_type)
        if(MyPortfolio.sellOption(option, option_price, quantity)):
          print("Transaction successful!")
        else:
          print(f"Transaction unsuccessful: \nYou do not have own enough contracts of: {option}")


    elif(userInput == "-p"):
      MyPortfolio.printOptions()

    elif(userInput == "-buying power"):
      print(f"${MyPortfolio.getBuyingPower():.4f}")

    elif(userInput == "-portfolio value"):
      print(f"Portfolio value: ${MyPortfolio.getPortfolioValue():.4f}")

    elif(userInput == "-q"):
      robin_stocks.authentication.logout()
      f = open("out.txt","w+")
      f.write(str(MyPortfolio.getBuyingPower()) + '\n')
      f.write(str(MyPortfolio.getOptions()))
      f.close()
      running = False

    else:
      print("Invalid command; enter -h for help")