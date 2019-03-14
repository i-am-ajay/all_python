__author__ = 'gaa8664'
from salary.arrear_cal import connection
from salary.arrear_cal import Query
import calendar as cl
from datetime import date
from dateutil import parser

'''
    This program is to find list of employee on monthly basis whose salary is less than the minimum wages for that month.
    To start we given beginning and ending month and year. A loop will run monthwise till the end date and will store data from Prodigious Salary history in
    local tables. There are two tables, empdetails(empcode, emp_name, designation, dept, category, status, seperation, type) and
    emp_sal_amount(id, empcode, amount, date).
'''

conn = connection.con
my_conn = connection.con_mysql
# to store empcode, whose details we have store in empdetails, so that we don't have to pull employee information each month iteration
emp_list = []
# monthly base amount, it is updated from base_amount_map and if current month in not in the map then base amount remain same as previous month
base_amount = 0.0
# map of minimum wages month wise
base_amount_map = {'20173':17604,'20174':17916, '20184':18332, '201810':18462}


'''
    * Find employee with salary less then minimum wage from prodigious
    * if this is first month employee is appearing then save employee details in empdetails table and append employee to emp_list
    * save employee salary and month in emp_sal_amount table
'''

def relevant_data(record):
    if record[1]:
        return True
    return False


def monthwise_emp_list(payperiod, min_amount, year_month ):
    global emp_list
    check_blocked = False
    continue_loop = True
    blocked_employee = False
    recordset = None
    while continue_loop:

        if payperiod == '9||01/03/2017||31/03/2017||0':
            continue_loop = False
            recordset = []
            import openpyxl
            workbook = openpyxl.load_workbook('E:\Salary\March 2017\Salary March 2017.xlsx')
            sheet = workbook.get_sheet_by_name('Mar 17')
            list_record = []
            count = 1
            for record in sheet:
                list_record.clear()
                if count == 1:
                    count += 1
                    print('{}:{}:{}:{}:{}:{}'.format(record[9].value,record[29].value,record[30].value,record[32].value,record[34].value,record[41].value))
                    continue
                #print('{}:{}:{}:{}:{}:{}'.format(record[9].value,record[29].value,record[30].value,record[32].value,record[34].value,record[41].value))
                list_record.append(record[29].value if record[29].value else 0)
                list_record.append(record[30].value if record[30].value else 0)
                list_record.append(record[32].value if record[32].value else 0)
                list_record.append(record[34].value if record[34].value else 0)
                list_record.append(record[41].value if record[41].value else 0)
                print(list_record)
                val = sum(list_record)
                if val < min_amount:
                    emp_sal_record = []
                    emp_sal_record.append(record[9].value)
                    emp_sal_record.append(val)
                    print(emp_sal_record)
                    recordset.append(emp_sal_record)

        else:
            if not check_blocked:
                blocked_employee = False
                recordset = run_execute_query(conn,Query.FIND_SALARY_MONTHWISE,(payperiod, min_amount))
                check_blocked = True
            else:
                blocked_employee = True
                recordset = run_execute_query(conn, Query.BLOCKED_EMPLOYEE_SALARY,(payperiod,min_amount,payperiod))
                recordset = list(filter(relevant_data, recordset))
                check_blocked = False
                continue_loop = False
        for record in recordset:
            if record[0].casefold() not in emp_list:
                print('{} not found'.format(record[0]))
                emp_detail = run_execute_query(conn,Query.FIND_EMP_DETAILS,record[0])
                run_update_query(my_conn,Query.SAVE_EMP_DETAIL, emp_detail[0])
                emp_list.append(record[0].casefold())
            cursor = my_conn.cursor()
            print(year_month)
            cursor.execute(Query.SAVE_EMP_SAL,( record[0], record[1], year_month, min_amount ))
            my_conn.commit()
            cursor.close()


# execute a query
def run_execute_query(con,query, query_params=None):
    cursor = con.cursor()
    cursor.execute(query,query_params)
    recordset = cursor.fetchall()
    cursor.close()
    return recordset


# update or insert query
def run_update_query(con,query, query_params):
    cursor = con.cursor()
    cursor.execute(query, query_params)
    cursor.close()

# upload employee list from the empdetails table everytime we run program
def list_of_emp():
    global emp_list
    recordset = run_execute_query(my_conn,Query.GET_EMP_LIST)
    emp_list = [x[0].casefold() for x in recordset]


# method will generate pay period and will set base amount for the month
def generate_parameters(year, month):
    global base_amount
    year_month = str(year)+str(month)
    pay_date = date(year,month,1)
    last_date = cl.monthrange(year,month)[1]
    if month < 10:
        payperiod = '9||01/0{0}/{1}||{2}/0{0}/{1}||0'.format(month,year,last_date)
    else:
        payperiod = '9||01/{0}/{1}||{2}/{0}/{1}||0'.format(month,year,last_date)
    try:
        base_amount = base_amount_map[year_month]
    except:
        pass

    return (payperiod, base_amount, pay_date)

# Generator to provide an iterator between the given time range
def month_range(b_day, e_day, b_year, e_year):
    while True:
        if b_year > e_year:
            break
        elif b_day > e_day and b_year == e_year:
            break
        else:
            yield (b_day,b_year)
            if b_day == 12:
                b_day = 1
                b_year += 1
            else:
                b_day += 1


if __name__ == '__main__':
    list_of_emp()
    for month,year in month_range(3,12,2017,2018):
        print(generate_parameters(year,month))
        monthwise_emp_list(*generate_parameters(year,month))

    #print(generate_parameters(2017,3))

    conn.commit()
    my_conn.commit()
    conn.close()
    my_conn.close()