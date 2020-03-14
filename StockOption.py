import robin_stocks

class StockOption:
  strike_price = 0.0
  stock_ticker = ""
  option_type = ""
  expiration_date = ""

  def __init__(self, stock_ticker, expiration_date, strike_price, option_type):
    self.strike_price = float(strike_price)
    self.stock_ticker = stock_ticker
    self.option_type = option_type
    self.expiration_date = expiration_date

  def __hash__(self):
    return hash(str(self))

  def __eq__(self, candidate):
    return (self.strike_price, self.stock_ticker, self.option_type, self.expiration_date) == (candidate.strike_price, candidate.stock_ticker, candidate.option_type, candidate.expiration_date)

  def __str__(self):
    return (f"Stock ticker: {self.stock_ticker}\nOption type: {self.option_type}\nStrike price: {self.strike_price}\nExpiration date: {self.expiration_date}")

  def getCurrentPrice(self):
    return getOptionPrice(self.stock_ticker, self.expiration_date, self.strike_price, self.option_type)
