from organizer import get_list_of_actions, update_action, update_columns_datatype
from pandas import read_excel

path=input("The path to the spreadsheet: ")
name=input("The name of the sheet: ")

table = read_excel(path, sheet_name=name)

print("The sheet read:\n", table)

if __name__ == "__main__":
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