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

  def __hash__(self):
    return hash(str(self))

  def __eq__(self, candidate):
    return (self.__strike_price, self.__stock_ticker, self.__option_type, self.__expiration_date) == (candidate.__strike_price, candidate.__stock_ticker, candidate.__option_type, candidate.__expiration_date)

  def __str__(self):
    return (f"Stock ticker: {self.__stock_ticker}\nOption type: {self.__option_type}\nStrike price: {self.__strike_price}\nExpiration date: {self.__expiration_date}")