from loan_update import prod_con
from loan_update import Queries
import openpyxl


def loan_correction():
    sheet = get_employee_excel()
    con = None
    cursor = None
    for row in sheet:
        employee = row[0].value
        con = prod_con.get_con()
        cursor = con.cursor()
        cursor.execute(Queries.get_loan_detail,(employee,))
        result = cursor.fetchall()
        print('{} -> {}'.format(employee,len(result)))
        # Delete records from Loan History
        ''' #cursor1 = con.cursor()
        cursor.execute(Queries.delete_loan_record,(result[-1][0],))
        cursor.execute(Queries.delete_loan_record,(result[-2][0],))
        con.commit() '''

        # update loan history and loan
        '''print(result[0][1])
        cursor.execute(Queries.update_loan_history,result[0][1])
        cursor.execute(Queries.update_loan_detail,result[0][1])'''

    #con.commit()
    con.close()
    cursor.close()


def del_employee_record(id):
    pass


def get_employee_excel():
    workbook = openpyxl.load_workbook('D:\\Festival Loan Emp.xlsx')
    sheet = workbook.get_sheet_by_name('Sheet1')
    return sheet

if __name__ == '__main__':
    loan_correction()