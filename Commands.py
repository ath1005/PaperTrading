import robin_stocks

def printHelp():
  """
  Prints a help menu with all defined commands and a description for each
  """
  print("-h: Print list of commands")
  print("-ticker name: Print the name of the company associated with the given stock ticker")
  print("-option price: Get the current price of 1 option contract with the given information")
  print("-buy option: Purchase option contract(s)")
  print("-buying power: Print the current buying power in the Investment Portfolio")
  print("-q: Quit the program")

def getStockName(ticker):
  """
  Gets the name of the stock associated with the given ticker

  Returns
  -------
  str
    stock name
  """
  return robin_stocks.stocks.get_name_by_symbol(ticker)

def getOptionPrice(stock_ticker, expiration_date, strike_price, option_type):
  """
  Gets the current price of a given option

  Parameters
  ----------
  stock_ticker : str
    stock ticker associated with the option
  expiration_date : str
    expiration date of the contract (YYYY-MM-DD)
  strike_price : float
    strike price of the option
  option_type : str
    call or put

  Returns
  -------
  bool or float
    price of option if it exists, False otherwise
  """
  price = robin_stocks.options.get_option_market_data(stock_ticker, expiration_date, strike_price, option_type, 'adjusted_mark_price')
  if price != None:
    return float(price)
  else:
    return False