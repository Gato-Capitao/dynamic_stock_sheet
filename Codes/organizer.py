from pandas import DataFrame
from collections import deque

def get_list_of_actions(table:DataFrame) -> deque:
    return deque(table["Nome"])


