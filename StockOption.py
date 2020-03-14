import robin_stocks
from Commands import getOptionPrice

class StockOption:
  """
  A class used to represent an option contract

  Attributes
  ----------
  stock_ticker : str
    stock ticker associated with the option
  expiration_date : str
    expiration date of the contract (YYYY-MM-DD)
  strike_price : float
    strike price of the option
  option_type : str
    call or put
  """
  stock_ticker : str
  expiration_date : str
  strike_price : float
  option_type : str

  def __init__(self, stock_ticker, expiration_date, strike_price, option_type):
    """
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
    """
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
    """Gets the real-time price of the option contract

    Returns
    -------
    float
      price of the option in real-time
    """
    return getOptionPrice(self.stock_ticker, self.expiration_date, self.strike_price, self.option_type)
