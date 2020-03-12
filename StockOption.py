class StockOption:
  __strike_price = None
  __stock_ticker = None
  __option_type = None
  __expiration_date = None

  def __init__(self, stock_ticker, expiration_date, strike_price, option_type):
    self.__expiration_date = expiration_date
    self.__stock_ticker = stock_ticker
    self.__option_type = option_type
    self.__expiration_date = expiration_date