from pandas import DataFrame
from collections import deque
from collector import get_current_price, get_average, get_currency, get_div_rate, get_div_yields, get_industry_type, get_price_to_earnings, get_sector
from yfinance import Ticker

def get_list_of_actions(table:DataFrame) -> deque:
    return deque(table["Name"])

def update_action(table:DataFrame, action_pos:int, action_name:str) -> None:
    connector={
        "Sector":get_sector,
        "Price":get_current_price,
        "Industry":get_industry_type,
        "Currency":get_currency,
        "Fifity day average":get_average,
        "Div rate":get_div_rate,
        "Div yield":get_div_yields,
        "PE":get_price_to_earnings
    }
    action_ticker = Ticker(action_name)

    for info in connector.keys():
        try:
            table.loc[action_pos, info]=connector[info](action_ticker)
        except KeyError:
            table.loc[action_pos, info]="NF"


    


