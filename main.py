import robin_stocks
from InvestmentPortfolio import InvestmentPortfolio

robin_stocks.authentication.login(username="hassonatlee@yahoo.com", password="ChiefAt033100", by_sms=True, store_session=True)

initial_investment_capital = float(input("How much money would you like to start with? "))

MyPortfolio = InvestmentPortfolio(initial_investment_capital)