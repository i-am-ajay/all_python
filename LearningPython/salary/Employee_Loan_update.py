from salary import query
from salary.connection import Connection
__author__ = 'gaa8664'

'''
   A program to get employee loan details for the current month and update it accordingly
'''


# get employee loan informaton from loan table.
def get_loans(empcode, loan_date):
    count = 1
    loans_list = []
    with Connection() as cursor:
        cursor.execute(query.LOAN_INFO,(empcode,loan_date))
        for row in cursor.fetchall():
            loans_list.append(row)
            print("{0}.{1}".format(count,row))
            count += 1
        print('-'*300)
    return loans_list


# get selected loan details form loan history table
def get_loan_detail(loan):
    id_loan = []
    employee = loan[0]
    issue_date = loan[1]
    loandr = loan[5]
    print('{0}-> {2},{1}'.format(employee, issue_date, loandr))
    with Connection() as cursor1:
        cursor1.execute(query.LOAN_DETAILS,(employee, loandr))
        for record in cursor1.fetchall():
            id_loan.append(record[0])
            print(record)
        print("-"*300)
    return id_loan


def update_loan_date(year, month, day, emi_id_list, loandr, employee):
    with Connection() as cursor2:
        for emi_id in emi_id_list:
            value_list = []
            local_date = '-'.join([str(year), str(month), str(day)])
            #cursor2.execute(query.LOAN_SELECT,emi_id)
            cursor2.execute(query.UPDATE_LOAN_DATE, (local_date, loandr, employee, emi_id))
            '''for row in cursor2.fetchone():
                value_list.append(str(row))
            print("{}-{}->{}".format(local_date, emi_id, ','.join(value_list)))'''

            if month == 12:
                month = 1
                year += 1
            else:
                month += 1

        con = Connection.get_connection()
        con.commit()
        print('Updation Done')
        Connection.connection_close()

def update_loan_amount():
    pass


def loan_operations(employee, loan_date, year, month, date):
    loans_info = get_loans(employee, loan_date)
    choice = int(input('Enter your choice'))
    selected_loan = loans_info[choice-1]
    loan_emi_list = get_loan_detail(selected_loan)
    loandr = selected_loan[5]
    print("1.Update Loan")
    print("2.Exit")
    choice = int(input("Enter Choice"))
    if choice == 1:
        update_loan_date(year, month, date, loan_emi_list, loandr, employee)
    else:
        exit(1)


if __name__ == '__main__':
    '''
        date : date from which have to search loans
        year, month, day : since when to start loan emi.
    '''
    loan_operations('GAA3519', '2018-01-01', 2018, 2, 1)