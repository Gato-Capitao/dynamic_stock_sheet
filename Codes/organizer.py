from pandas import DataFrame
from collections import deque
from collector import get_current_price
from yfinance import Ticker

def get_list_of_actions(table:DataFrame) -> deque:
    return deque(table["Name"])

def update_action(table:DataFrame, action_pos:int, action_name:str) -> None:
    connector={
        "Price":get_current_price
    }
    action_ticker = Ticker(action_name)

    for info in connector.keys():
        table.loc[action_pos, info]=connector[info](action_ticker)


    


