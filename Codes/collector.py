from yfinance import Ticker

def sum(num1:int, num2:int) -> int:
    return num1+num2

def get_price(symbol:str) -> float:
    price = Ticker(symbol)
    input()
get_price("MXRF11.SA")
