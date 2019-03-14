__author__ = 'gaa8664'
from sal_template.connections import db_con
from sal_template import queries
'''
    Update a Salary head in new template by picking the amount of the salary head from old head.
    Parameters
    * Old Template
    * New Template
    * Salary Head

    Steps -
    1) Get all the active employees from New Template.
    2) Loop through the list of employees, get the amount of the salary head from the old template.
    3) Update the amount against new salary template head.
'''
cursor = db_con.con.cursor()


def get_emp_with_newTemplate(saltemplate, old_saltemplate, sal_head):
    global cursor
    cursor.execute(queries.GET_EMP_WITH_NEWTEMP,(saltemplate))
    recrodset = cursor.fetchall()
    count = 0
    for record in recrodset:
        emp = record[0]
        from_date = record[1]
        data_record = get_head_amount_oldtemplate(emp, old_saltemplate,sal_head)
        amount = data_record[0]
        id = data_record[1]
        new_hra = (amount*19)/100
        print('{0} {1} {2}'.format(emp, new_hra, id))
        count += 1
        #update_head_amount_newtemplate(emp,sal_head,from_date, new_hra,id)
    print('Total Records:'+str(count))


#returns amount
def get_head_amount_oldtemplate(emp, saltemp, sal_head):
    global cursor
    cursor.execute(queries.GET_LAST_DATE_TEMP_EMP,(saltemp,emp))
    template_date = cursor.fetchone()
    template_date = template_date[0]
    cursor.execute(queries.GET_AMOUNT_OLDTEMP,(emp, sal_head, template_date))
    amount_record = cursor.fetchone()
    cursor.execute(queries.GET_AMOUNT_OLDTEMP,(emp, '9||VPF', template_date))
    id_record = cursor.fetchone()
    print("{0}: Template:{1}, Date:{2}, Amount:{3}".format(emp,saltemp,template_date,amount_record[0]))
    return (amount_record[0],id_record[1])



def update_head_amount_newtemplate(emp, salhead, fromdate, amount,id):
    global cursor
    cursor.execute(queries.UPDATE_AMOUNT_NEWTEMP,(float(amount),emp,'9||HRA',fromdate,id))



def close_cursor_con():
    global cursor
    db_con.con.commit()
    cursor.close()
    db_con.con.close()

if __name__ == '__main__':
    get_emp_with_newTemplate('ClassWSR6','ClassWSR4A','9||VPF')
    #update_head_amount_newtemplate('GAA0470','9||HRA','2018-04-01',8037,1752618)
    close_cursor_con()

