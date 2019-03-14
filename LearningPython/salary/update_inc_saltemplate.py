__author__ = 'gaa8664'
from salary.connection import Connection
from salary import query

# create static object for connection and cursor.
Connection.get_connection()
cursor = Connection.get_cursor()

# fetch data that needs to be updated
def get_resultset():
    cursor.execute(query.GET_EMPLOYEE_TEMPLATE,('2017-11-01','2017-11-30'))
    resultset = cursor.fetchall()
    return resultset

# display the fetched data
def show_data(resultset):
    #resultset = get_resultset()
    for row in resultset:
        print(row)
        print('{}->{}'.format(row[0], row[3]))

# update the template information
def update_template(resultset:''):
    con = Connection.get_connection()
    cursor.executemany(query.UPDATE_TEMPLATE_INC,resultset)
    con.commit()


def close():
    Connection.close_cursor()
    Connection.connection_close()


if __name__ == '__main__':
    resultset = get_resultset()
    show_data(resultset)
    update_template(resultset)
    close()