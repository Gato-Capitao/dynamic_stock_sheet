from organizer import get_list_of_actions
from pandas import read_excel

path="D:\Codes\Projetos Github\Planilha-de-renda-variavel-inteligente\Codes\data_table.xlsx"
name="Sheet1"

table = read_excel(path, sheet_name=name)

if __name__ == "__main__":
    deque_actions = get_list_of_actions(table)

    for action_name in deque_actions:
        pass

