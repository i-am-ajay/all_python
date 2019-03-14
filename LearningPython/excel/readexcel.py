from excel import Globals
from pprint import pprint

__author__ = 'gaa8664'
import openpyxl

# read given foxpro salary master
def read_excel(file):
    excel_file = openpyxl.load_workbook(filename=file)
    sheet = excel_file.get_sheet_by_name('Mar2017')
    count = 0
    for row in sheet:
        if(count == 0):
            set_fox_col_map(row)
            count += 1
        else:
            for cell in row:
                print(cell.value)
            print("\n")
            if count == 1:
                break
            count += 1

# insert column heads in map
def set_fox_col_map(row):
    count = 0
    for cell in row:
        Globals.FOXPRO_MAP[count] = cell.value
        count += 1



if __name__ == "__main__":
    read_excel('D:\\Software\\Software\\HR Module\\Salary\\Sal_Mar_2017.xlsx')
    pprint(Globals.FOXPRO_MAP)