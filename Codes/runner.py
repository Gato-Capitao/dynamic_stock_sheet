"""
Hello :)

This project makes it possible to take various information about actions and add them to a spreadsheet, it is also extremely flexible where you can use different information and in variable ways.

GitHub: https://github.com/Gato-Capitao/dynamic_stock_sheet
Python: 3.11
"""

from organizer import get_list_of_actions, update_action, update_columns_datatype
from pandas import read_excel


if __name__ == "__main__":
    #Read the table
    path=input("The path to the spreadsheet: ")
    name=input("The name of the sheet: ")

    table = read_excel(path, sheet_name=name)
    print("The sheet read:\n", table)#Show a preview

    #Update the columns data type
    update_columns_datatype(table)

    #Update the actions
    deque_actions = get_list_of_actions(table, "Name")

    for pos, action_name in enumerate(deque_actions):
        update_action(table, pos, action_name)
    
    #Convert to a xlsx format
    path=path[:-5]+"_updated"+".xlsx"

    table.to_excel(path, index=False)

    #Show a preview of the table
    print("The updated sheet:\n", table)