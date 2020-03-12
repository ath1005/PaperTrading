from StockOption import getOptionPrice

class InvestmentPortfolio:
  __buying_power = None;
  __options = {};

  def __init__(self, starting_capital):
    self.__buying_power = starting_capital

  def getBuyingPower(self):
    return self.__buying_power

  def buyOption(self, stock_option, individual_price, quantity):
    total_price = individual_price * float(quantity) * 100
    if(total_price > self.__buying_power):
      return False
    else:
      if(stock_option in self.__options.keys()):
        current_quantity = self.__options.get(stock_option)
        self.__options[stock_option] = int(quantity) + int(current_quantity)
      else:
        self.__options[stock_option] = int(quantity)
      self.__buying_power -= total_price
      return True

  def printOptions(self):
    for key, value in self.__options.items():
      print ("\nOption: "+ str(key) + "\nQuantity: " + str(value))

  def getPortfolioValue(self):
    total = 0.0
    for key, value in self.__options.items():
      total += getOptionPrice(getattr(key, 'stock_ticker'), getattr(key, 'expiration_date'), getattr(key, 'strike_price'), getattr(key, 'option_type')) * 100.0
    return total + self.__buying_power