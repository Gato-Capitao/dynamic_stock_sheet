from yfinance import Ticker

def get_price(action:Ticker) -> float:
    price = action.info["currentPrice"]
    return price

print(get_price(Ticker("MXRF11.SA")))
