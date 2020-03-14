from Commands import getOptionPrice

class InvestmentPortfolio:
  """
  A class used to represent the user's assets

  Attributes
  ----------
  buying_power : float
    current capital the user has available to invest
  options : dict
    a dictionary of all options the user owns as keys, and the number of contracts for that option as the value
  """
  buying_power : float;
  options : {};

  def __init__(self, starting_capital):
    """
    Parameters
    ----------
    starting_capital : float
      the user's starting capital
    """
    self.buying_power = starting_capital
    self.options = {}

  def getBuyingPower(self):
    """
    Returns
    -------
    float
      current buying power
    """
    return self.buying_power

  def buyOption(self, stock_option, individual_price, quantity):
    """Attempts to purchase options contract(s)
    Parameters
    ----------
    stock_option : StockOption
      option contract(s) to be purchased
    individual_price : float
      price of one contract of the requested option
    quantity : int
      number of options contracts to be purchased
    
    Returns
    -------
    bool
      True if purchase was successful, False otherwise
    """
    total_price = individual_price * quantity * 100
    if(total_price > self.buying_power):
      return False
    else:
      if(stock_option in self.options.keys()):
        current_quantity = self.options.get(stock_option)
        self.options[stock_option] = int(quantity) + int(current_quantity)
      else:
        self.options[stock_option] = int(quantity)
      self.buying_power -= total_price
      return True

  def sellOption(self, stock_option, individual_price, quantity):
    """Attempts to sell option contract(s)

    Parameters
    ----------
    stock_option : StockOption
      option contract(s) to be sold
    individual_price : float
      price of one contract of the requested option
    quantity : int
      number of options contracts to be sold
    
    Returns
    -------
    bool
      True if sale was successful, False otherwise
    """
    portfolio_quantity = self.options.get(stock_option)
    if(portfolio_quantity == None or portfolio_quantity < int(quantity)):
      return False
    else:
      if(portfolio_quantity == int(quantity)):
        del self.options[stock_option]
      else:
        self.options[stock_option] = portfolio_quantity - int(quantity)
      self.buying_power += individual_price * float(quantity) * 100
      return True

  def printOptions(self):
    """Prints all options contracts currently owned, and the quantity of each contract
    """

    for key, value in self.options.items():
      print ("\nOption: "+ str(key) + "\nQuantity: " + str(value))

  def getPortfolioValue(self):
    """Gets the value of the user's portfolio

    Returns
    -------
    float
      value of all owned options and current buying power
    """

    total = 0.0
    for key, value in self.options.items():
      total += getOptionPrice(getattr(key, 'stock_ticker'), getattr(key, 'expiration_date'), getattr(key, 'strike_price'), getattr(key, 'option_type')) * 100.0
    return total + self.buying_power