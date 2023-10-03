from organizer import get_list_of_actions, update_action
from pandas import read_excel

path="D:\Codes\Projetos Github\Planilha-de-renda-variavel-inteligente\Codes\data_table.xlsx"
name="Sheet1"

table = read_excel(path, sheet_name=name)
print(table["Preço"])

if __name__ == "__main__":

    deque_actions = get_list_of_actions(table)

    for pos, action_name in enumerate(deque_actions):
        update_action(table, pos, action_name)
    
    print(table["Preço"])
   

