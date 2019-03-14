from salary.connection import Connection
from salary import query
from salary.global_vars import get_pay_period

__author__ = 'gaa8664'

def emp_gross_sal(empcode, month, year):
    pay_period = get_pay_period(month, year)
    prod = Connection.get_connection()
    cursor = Connection.get_cursor()
    cursor.execute(query.GROSS_SALRY,(empcode, pay_period))   #9||01/04/2017||30/04/2017||0
    resultset = cursor.fetchall()
    return resultset

def get_distinct_emp(month, year):
    pay_period = get_pay_period(month, year)
    prod = Connection.get_connection()
    cursor = Connection.get_cursor()
    cursor.execute(query.DISTINCT_EMP,(pay_period,))
    resultset = cursor.fetchall()
    return resultset

if __name__ == '__main__':
    result = emp_gross_sal('gaa8664','04','2017')
    for x in result:
        print(x)