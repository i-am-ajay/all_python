__author__ = 'gaa8664'
'''
    A class that makes a create table statement by getting table structure from data.
'''

__author__ = 'ajay'

import openpyxl
import datetime
import reports.excel_operations.excel_processing as excel_processing

working_sheet = None
workbook = None


def create_table_structure(header_row, data_column_row):
    col_datatype_map = {}
    count = 0
    for col_name in header_row:
        data_type = None
        data = data_column_row[count]


def get_col_value(col, col_index):
    data_type = None
    data_value = None
    if col:
        data_value = get_sql_data_type_of_value(col).value
        if (type(data_value) is int ) or (type(data_value) is float):
           data_value = get_col_best_value(col, col_index)
    else:
        data_col =  None
        data_value = get_col_best_value(col, col_index)

def get_col_best_value(col, col_index):
    ''' function will traverse the colum
        *in case if first value is None to find the type of column.
        *in case column is of type number then to find the largest number, to find which will be best datatype.
    '''
    data_col = excel_processing.get_column(col_index)
    li = list(filter(None, data_col))
    if li:
        li = sorted(li,reverse=True)

00
'''
    Get a row from excel sheet, this row could be used to determine the type of data stored in excel columns.
    It should not be the first row, as first row will contain columns.
'''
def get_row_for_datatypes(excel_sheet, row_index = 2):
    return excel_sheet.rows[row_index]

def iterate_row_for_values(row):
    count = 1
    for col in row:
        NoneType = type(None)


def get_sql_data_type_of_value(value):
    try:
        if type(value) is str:
            return 'VARCHAR'
        elif type(value) is int:
            return 'INTEGER'
        elif type(value) is float:
            return 'FLOAT'
        elif type(value) is datetime.datetime:
            return 'DATETIME'
    except:
        return None

if __name__ == '__main__':
    print(get_sql_data_type_of_value(datetime.datetime.now()))
