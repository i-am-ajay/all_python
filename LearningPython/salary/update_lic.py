from salary import query
from salary.connection import Connection

__author__ = 'gaa8664'
import openpyxl

def get_connection():
    pass


def read_excel(file,sheet):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheet)
    count = 0
    for row in sheet:
        if count == 0:
            count += 1
            continue
        policy = row[0].value
        empcode = row[1].value
        amount = row[2].value
        update_database(amount,empcode,policy)
    Connection.close_cursor()
    Connection.connection_close()


def update_database(amount, empcode, policy):
    connection = Connection.get_connection()
    cursor = Connection.get_cursor()
    cursor.execute(query.UPDATE_LIC,(float(amount),empcode,policy))
    connection.commit()


if __name__ == '__main__':
    read_excel('D:/LIC_11.xlsx','Sheet2')
