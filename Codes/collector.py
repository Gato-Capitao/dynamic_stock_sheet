from yfinance import Ticker

def get_current_price(action:Ticker) -> float:
    """
    action: the action object of type Ticker of the yfinance library that has all the information about the action.

    This function will return the current price of the action in float.
    """
    price = action.info["currentPrice"]
    return price

def get_currency(action:Ticker) -> str:
    currency = action.info["currency"]

    return currency

def get_industry_type(action:Ticker) -> str:
    industry=action.info["industry"]

    return industry

def get_sector(action:Ticker) -> str:
    sector = action.info["sector"]

    return sector

def get_average(action:Ticker) -> float:
    fifty_average = action.info["fiftyDayAverage"]

    return fifty_average

def get_div_rate(action:Ticker) -> float:
    rate=action.info["dividendRate"]

    return rate

def get_div_yields(action:Ticker) -> float:
    yields = action.info["dividendYield"]

    return yields

def get_price_to_earnings(action:Ticker) -> float:
    pe = action.info["trailingPE"]

    return pe

def get_book_value(action:Ticker) -> float:
    book_value = action.info["bookValue"]

    return book_value

