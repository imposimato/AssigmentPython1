import httplib2


def stock_prices_evaluator(url, list_return=5):
    """This Function receives an URL with a CSV file from the historical Stock Prices form a given company
    Calculates the average price and prints the following options:
    1 = Best six months,
    2 = Worst six months,
    3 = Best six years,
    4 = Worst six years,
    Any orther value will return all the months."""

    


stock_prices_evaluator("http://mf2.dit.ie/googleprices.csv", 2)
