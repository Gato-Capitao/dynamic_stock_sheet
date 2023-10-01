from pandas import read_excel, DataFrame

def read_sheet(path:str, sheet:str) -> DataFrame:
    table = read_excel(path, sheet_name=sheet)
    
    return table