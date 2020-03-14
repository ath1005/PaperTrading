import robin_stocks

def printHelp():
    print("-h: Print list of commands")
    print("-ticker name: Print the name of the company associated with the given stock ticker")
    print("-option price: Get the current price of 1 option contract with the given information")
    print("-buy option: Purchase option contract(s)")
    print("-buying power: Print the current buying power in the Investment Portfolio")
    print("-q: Quit the program")

def getStockTicker(ticker):
  return robin_stocks.stocks.get_name_by_symbol(ticker)

def getOptionPrice(stock_ticker, expiration_date, strike_price, option_type):
  price = robin_stocks.options.get_option_market_data(stock_ticker, expiration_date, strike_price, option_type, 'adjusted_mark_price')
  if price != None:
    return float(price)
  else:
    return False