__author__ = 'gaa8664'
'''
    Class provides various excel operations.
'''
import openpyxl

sheet = None
workbook = None


def load_excel(workbook_path, sheet_name):
    global workbook,sheet
    workbook = openpyxl.load_workbook(workbook_path)
    sheet = workbook[sheet_name]


def get_header_row(row_sheet=sheet):
    try:
        return row_sheet.rows.__next__()
    except AttributeError:
        print('No sheet is available to get data row')

def get_first_data_row(row_sheet=sheet):
    try:
        row_sheet.rows.__next__() # ignore first row considering it's header row
        row = row_sheet.rows.__next__()
        return row
    except AttributeError:
        print('No sheet is available to get data row')


def get_column(column_index, sheet_for_col=sheet, start_from_zero=True):
    col = None
    try:
        cols_list = list(sheet_for_col.cols)
        if start_from_zero:
            col = cols_list[column_index]
        else:
            col = cols_list[column_index-1]
        return col
    except AttributeError:
        print('No sheet is available to get column.')
