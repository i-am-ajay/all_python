from salary import query
from salary.connection import Connection
from salary.global_vars import get_pay_period

__author__ = 'gaa8664'
''' module provides functions to get data from Prodigious payslip table for a given payperiod'''


def get_employee_pro_sal(emp_code, year, month):
    pay_period = get_pay_period(month, year)
    connection = Connection.get_connection()
    cursor = Connection.get_cursor()
    cursor.execute(query.EMP_SAL,(emp_code, pay_period))   #9||01/04/2017||30/04/2017||0
    resultset = cursor.fetchall()
    return resultset

if __name__ == '__main__':
    get_employee_pro_sal('GAA4293','2017','04')

