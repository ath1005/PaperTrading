import robin_stocks

robin_stocks.authentication.login(username="hassonatlee@yahoo.com", password="ChiefAt033100", by_sms=True, store_session=True)

initial_investment_capital = float(input("How much money would you like to start with? "))

print(f"Your account will start with ${initial_investment_capital}")