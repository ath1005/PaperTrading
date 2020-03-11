class InvestmentPortfolio:
  __buying_power = None;

  def __init__(self, starting_capital):
    self.__buying_power = starting_capital

  def getBuyingPower(self):
    return self.__buying_power