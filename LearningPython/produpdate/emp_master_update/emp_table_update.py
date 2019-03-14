from produpdate import Queries

import openpyxl
from datetime import datetime

__author__ = 'gaa8664'

from connection.connections import Prod_Con

# get data from emp_master
connection = Prod_Con()


# UPLOAD METHODS
# update bank account number in EmployeeBank
def update_bank_account( empCode, account_name, account_number ):
    cursor = connection.get_con().cursor()
    val = cursor.execute(Queries.UPDATE_BANK_ACC,(account_name, account_number, empCode))
    print(val)


# update pan number in employee table
def update_pan_number(empcode, pan_no):
    cursor=connection.get_con().cursor()
    val = cursor.execute(Queries.UPDATE_PAN, (pan_no,empcode))


# update designation in employee table
def update_designation(empcode, designation):
    cursor=connection.get_con().cursor()
    val = cursor.execute(Queries.UPDATE_Designation, (designation,empcode))


# update employee DOJ in employee table
def update_doj(empcode, doj):
    #doj = datetime.strptime(doj,"%d/%m/%Y")
    cursor = connection.get_con().cursor()
    val = cursor.execute(Queries.UPDATE_DOJ, (doj,empcode))


# update employee DOB in employee table
def update_dob(empcode, dob):
   # dob = datetime.strptime(dob,"%d/%m/%Y")
    cursor = connection.get_con().cursor()
    val = cursor.execute(Queries.UPDATE_DOB, (dob, empcode))


#update department in Prodigious
def update_department(empcode, department):
    cursor = connection.get_con().cursor()
    val = cursor.execute(Queries.UPDATE_DEPARTMENT,(department, empcode))


#update pf start date
def update_pf_startdate(empcode, pf_startdate):
    cursor = connection.get_con().cursor()
    val = cursor.execute(Queries.UPDATE_PF_START_DATE,(pf_startdate,empcode))


# EXCEL DATA TRAVERSING METHODS. These methods will call upload methods
# To update bank account details
def bank_account_list(workbook, sheet_name):
    sheet = workbook[sheet_name]
    for record in sheet:
        print("Empcode : {0}".format(record[0].value))
        print("Name : {0}".format(record[1].value))
        print("Bank Acc : {0}".format(record[2].value))
        update_bank_account(record[0].value,record[1].value,record[2].value)


# To update different type of values in database based on choice. Choice will decide which sheet data will be updated in table and in which col.
def emp_list(workbook, sheet_name, choice):
    sheet = workbook[sheet_name]
    # if sheet has header
    contains_header = True
    for record in sheet:
        if contains_header:
            contains_header = False
            continue
        print("Empcdoe : {0}".format(record[0].value))
        print("{1} : {0}".format(record[1].value,choice))
        if choice is 'PAN':
            update_pan_number(record[0].value, record[1].value)

        elif choice is 'designation':
            update_designation(record[0].value, record[1].value)

        elif choice is 'doj':
            update_doj(record[0].value, record[1].value)

        elif choice is 'dob':
            update_dob(record[0].value, record[1].value)
        elif choice is 'department':
            update_department(record[0].value, record[1].value)
        elif choice is 'pf_start_date':
            update_pf_startdate(record[0].value, record[1].value)
    sheet = None


# MAIN METHOD
# method loads a workbook and call a method to upload relevant sheet in database, sheet traversing methods
def list_of_employees():
    excel = openpyxl.load_workbook("C:\\Users\\gaa8664\\Documents\\Employee Master Detail1.xlsx")
    # method will read emp data from excel and will upload the same in prodigious
    #bank_account_list(excel,'bank')

    ''' upload pan numbers in employee table from the excel sheet.
        Arguments
            1) workbook objects
            2) Sheet_name that has to be read from workbook
            3) Choice, to decide which method should be called,
                'PAN' - For Pan card upload method
                'designation' - For designation upload method
                'doj' - For date of joining upload method
                'dob' - For date of birth upload method
                'pf_start' - For updating PF start date

    '''
    emp_list(excel, 'pf start date', 'pf_start_date')
    connection.get_con().commit()
    connection.close_con()

if __name__ == "__main__":
    list_of_employees()
    #update_bank_account('Gaa8664','Ajay Chandel','91112180027412')


