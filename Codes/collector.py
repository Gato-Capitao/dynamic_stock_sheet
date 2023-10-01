from yfinance import Ticker

def get_current_price(action:Ticker) -> float:
    """
    action: the action object of type Ticker of the yfinance library that has all the information about the action.

    This function will return the current price of the action in float.
    """
    price = action.info["currentPrice"]
    return price



print(get_current_price(Ticker("MXRF11.SA")))
