from pandas import DataFrame
from collections import deque
from collector import get_current_price, get_average, get_currency, get_div_rate, get_div_yields, get_industry_type, get_price_to_earnings, get_sector, get_book_value
from yfinance import Ticker

def get_list_of_actions(table:DataFrame, collum_name:str) -> deque:
    """
    This function will return a deque with the name of all actions.

    table: the data frame of pandas from the sheets.
    collum_name: the name of the collum with the name of all actions.
    """
    return deque(table[collum_name])

def update_action(table:DataFrame, action_pos:int, action_name:str) -> None:
    """
    This function will update infos of the action on the data frame.

    Args:
        table: the data frame of pandas from the sheets.
        action_pos: the Y position of the cell on the data frame.
        action_name: the name of the action.

    Operation: The code cycles through each key(column) in the connector dictionary and then uses the function to which the column is connected to get the information and add it to the column.
    """
    connector={
        "Sector":get_sector,
        "Price":get_current_price,
        "Industry":get_industry_type,
        "Currency":get_currency,
        "Fifity day average":get_average,
        "Div rate":get_div_rate,
        "Div yield":get_div_yields,
        "PE":get_price_to_earnings,
        "Book value":get_book_value
    }
    action_ticker = Ticker(action_name)

    for info in connector.keys():
        try:
            table.loc[action_pos, info]=connector[info](action_ticker)
        except KeyError:
            continue


    


