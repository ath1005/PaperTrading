class InvestmentPortfolio:
  __buying_power = None;
  __options = dict;

  def __init__(self, starting_capital):
    self.__buying_power = starting_capital

  def getBuyingPower(self):
    return self.__buying_power

  def buyOption(stock_option, individual_price, quantity):
    total_price = 