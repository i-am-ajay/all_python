from salary import query

__author__ = 'gaa8664'
import openpyxl
from salary.connection import Connection
# A program to upload headwise amount for employees in SalHistory table in employee template.
# Any value uploaded from here will reflect in the template of employee and will be calculated in salary each month.

template_head = {}

''' Requirement : an excel file with four columns,
    Employee code.
    Amount to be uploaded
    Salary Head to be uploaded
    Date for which head has to be updated. i.e. Last date in FromDate column
'''


def get_emp_amount(file_name, sheet_name, salhead,con):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.get_sheet_by_name(sheet_name)
    count = 0
    counter = 0
    for row in sheet:
        counter += 1
        if count == 0:
            count += 1
            continue
        empcode = row[0].value
        amount = row[1].value
        fromdate = row[2].value
        print('{0} {1} {2}'.format(empcode,amount,fromdate))
        #rollback(empcode,fromdate)
        #get_salhead_details(empcode, fromdate)

        update_amount_database(empcode, amount, salhead, fromdate,con)
        if(counter > 130):
            break



def update_amount_database(empcode, amount, salhead, fromdate, con):
    cursor = con.cursor()
    cursor.execute(query.UPDATE_HEAD_AMOUNT_EMPWISE,(amount, empcode, fromdate, salhead))
    con.commit()

'''
    Gets template of employee based on the given date and fetches all the head of the template and stores it in a template map if template is not
    already in the map. Then update the sal head as per template in the sal history table.
'''
'''
def rollback(emp, fromdate):
    cursor = con.cursor();
    cursor.execute(query.FIND_SALTEMPLATE_OF_EMP,(emp,fromdate))
    recordset = cursor.fetchall()
    template = list(recordset[0])[0]
    list_of_heads = []
    try:
        list_of_heads = template_head[template]
    except:
        cursor.execute(query.GET_HEAD_LIST,template)
        record_set = cursor.fetchall()
        head_list = []
        for record in record_set:
            head_list.append(list(record)[0])
        template_head[template] = head_list
        list_of_heads = template_head[template]
    # Get ids those has to be updated.
    cursor.execute(query.FIND_EMP_SALHISTORY_HEAD_ID,(emp,fromdate))
    id_recordset = cursor.fetchall()
    if len(id_recordset) == len(list_of_heads):
        count = 0
        for id in id_recordset:
            i = list(id)[0]
            cursor.execute(query.UPDATE_EMP_SALHEAD_SALHISTORY,(list_of_heads[count],i,fromdate,emp))
            count += 1
        print("Done for emp {0} -> {1}".format(emp,fromdate))
        con.commit()
    else:
        print("Not valid detail - Emp {0} -> {1}".format(emp,fromdate))

'''

'''
    UPDATE AMOUNT head for all salary heads in sal history table for a particular employee for a particular date.
'''

'''
def rollback(emp, fromdate):
    cursor = con.cursor()
    #Get ids those has to be updated.
    cursor.execute(query.FIND_EMP_SALHISTORY_HEAD_ID,(emp,fromdate))
    id_recordset = cursor.fetchall()
    count = 0
    for id in id_recordset:
        i = list(id)[0]
        cursor.execute(query.UPDATE_EMP_AMOUNT_SALHISTORY,(i,fromdate,emp))
        print("Done for emp {0} -> {1}".format(emp,fromdate))
    con.commit()
'''
'''
# update CC head to 400 for given employee for given date
def rollback(emp, fromdate):
    cursor = con.cursor()
    cursor.execute(query.UPDATE_EMP_AMOUNT_SALHISTORY,(400, fromdate, emp, '9||CC'))
    print("{0} -> {1}".format(emp, fromdate))
    con.commit()
'''
'''
def rollback(emp, fromdate):
    salhead = '9||DLF'
    payperiod = '9||01/12/2018||31/12/2018||0'
    cursor = con.cursor()
    try:
        cursor.execute(query.GET_HEAD_AMOUNT_FROM_PAYSLIP,(emp, salhead, payperiod))
        amount = list(cursor.fetchone())[0]
        print("{0} -> {1}".format(emp, amount))
        cursor.execute(query.UPDATE_EMP_AMOUNT_SALHISTORY,(amount * -1,fromdate, emp, salhead))
    except:
        print("{0} salary is not generated".format(emp))
    con.commit()
'''


def get_salhead_details(emp,fromdate):
    payperiod = '9||01/12/2018||31/12/2018||0'
    cursor = con.cursor()
    try:
        print(emp)
        cursor.execute(query.SALARY_DETAILS_PAYSLIP,(emp,payperiod))
        recordset = cursor.fetchall()
        if recordset:
            print("{0}->{1}".format(emp," ".join(recordset)))
    except  Exception as ex:
        print("{0} -> {1}".format(emp,ex))



if __name__ == '__main__':
    con = Connection.get_connection()
    file_name = 'E:\Salary\Conveyance Subsidy Uploaded.xlsx'
    sheet_name = 'Conveyance Subsidy'
    get_emp_amount(file_name, sheet_name, '9||CC', con)
    con.close()
