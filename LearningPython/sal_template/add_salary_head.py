from sal_template import queries
from sal_template.connections import db_con


__author__ = 'gaa8664'
'''
    Program to include a new salary head in the template.
    *** Parameters ***
    1) Template Code
    2) Salary Head code

    *** Logic ***
    1) Insert Head into SalTemplateHead table, against salary template.
    2) Find List of employees to whom this template is allocated and the date of template change for each employee.
    3) Insert the newly allocated head in the SalHistory table, insert head against the employee. This table stores heads mapping and heads amount for
        an employee.
'''
con = db_con.con
cursor = con.cursor()

# Get all employees with the given template with their latest template change date
def get_template_emps(temp_name):
    cursor.execute(queries.GET_EMP_WITH_NEWTEMP,(temp_name,))
    record_set = cursor.fetchall()
    # insert sal head in the template in latest change date.
    count = 0
    for record in record_set:
        if count > 100:
            break
        insert_into_salhistory(record)
        count += 1


def insert_into_salhistory(salary_record):
    empcode = salary_record[0]
    salary_head = '9||CC'
    from_date = salary_record[2]
    cursor.execute(queries.LATEST_TEMP_CHANGE_DATE,(salary_record[0],))
    record_set = cursor.fetchone()
    if salary_record[2] == str(record_set[0]):
        cursor.execute(queries.FIND_SALHEAD_ENTRY,(empcode,salary_head,from_date))
        if not cursor.fetchone():
            cursor.execute(queries.INSERT_HEAD_SALHISTORY,(salary_record[0],salary_record[2],salary_head))
        con.commit()
        print("Done for "+salary_record[0])

if __name__ == "__main__":
    get_template_emps('ClassWSC1')
    print("i am here")
