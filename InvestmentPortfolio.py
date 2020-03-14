from StockOption import getOptionPrice

class InvestmentPortfolio:
  buying_power = None;
  options = {};

  def __init__(self, starting_capital):
    self.buying_power = starting_capital

  def getBuyingPower(self):
    return self.buying_power

  def buyOption(self, stock_option, individual_price, quantity):
    total_price = individual_price * float(quantity) * 100
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
    for key, value in self.options.items():
      print ("\nOption: "+ str(key) + "\nQuantity: " + str(value))

  def getPortfolioValue(self):
    total = 0.0
    for key, value in self.options.items():
      total += getOptionPrice(getattr(key, 'stock_ticker'), getattr(key, 'expiration_date'), getattr(key, 'strike_price'), getattr(key, 'option_type')) * 100.0
    return total + self.buying_power