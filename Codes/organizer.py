from pandas import read_excel, DataFrame

def get_list_of_actions(path:str, sheet:str) -> DataFrame:
    table = read_excel(path, sheet_name=sheet)
    
    return table.columns

