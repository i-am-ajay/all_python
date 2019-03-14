__author__ = 'gaa8664'
import openpyxl
'''
    A program to compare RC over a given time period.
'''


def fetch_corresponding_rc(datasheet):
    for row in datasheet:
        cell = row[7].value
        if type(cell) is int:
            print('{} :- {}, {}'.format(row[6].value,row[7].value, find_ref_rc_numb(datasheet,cell)))


def find_ref_rc_numb(sheet, cell):
    rc_no = None
    for row in sheet:
        rc_no = row[6].value
        if(row[0].value == cell):
            break
    return rc_no


if __name__ == '__main__':
    file = 'E:\Inventory/rc_data.xlsx'
    sheet = 'Sheet1'
    workbook = openpyxl.load_workbook(file)
    datasheet = workbook.get_sheet_by_name(sheet)
    fetch_corresponding_rc(datasheet)


