__author__ = 'gaa8664'
'''
    Program will modify the salary head amount of in Salhistory table for a given date.
    Input : Will be an excel sheet with Empcode, Amount, Salhead to be updated as columns.
    Output : Will update salary head in sal history table.
'''

import openpyxl
import pymssql
from sal_template.connections import db_con
from sal_template import queries


def db_conf():
    global con
    global cursor
    con = db_con.con
    cursor = con.cursor()


def get_employee_excel(excel_file, sheet_name, from_date, sal_head):
    db_conf()
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook[sheet_name]
    for row in sheet:
        emp = row[0].value
        amount = float(row[1].value)
        print("{} -> {}".format(emp, amount))
        sal_head = row[2].value
        # uncomment to update in database Salhistory table.
        # update_employee_template(emp, sal_head, amount, from_date)
        #break


def update_employee_template(emp, sal_head, amount, from_date):
    cursor.execute(queries.UPDATE_AMOUNT_TEMP,(amount,emp,sal_head,from_date))


if __name__ == "__main__":
    get_employee_excel("C:\\Users\\gaa8664\\Documents\\DNB_Fee.xlsx","Sheet1","2018-12-01","9||BASIC")
    con.commit()
    con.close()
