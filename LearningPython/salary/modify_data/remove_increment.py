from salary.connection import Connection
import salary.query as query

con = Connection.get_connection()
cursor = Connection.get_cursor()

''' get employees code, whose increment has to be removed.
'''
def get_valid_employee(from_date, to_date, param):
    cursor.execute(query.EMP_INC_DETAIL,(from_date,to_date,param))
    resultset = cursor.fetchall()
    return resultset

# method will remove given employee entries from INCTHISTORY, EMPSALTEMPLATE, SALHISTORY for selected month
def delete_increment_entries( emp, date,template ):
    cursor.execute(query.DELETE_EMP_SALTEMPLATE,(emp, date, template))

    cursor.execute(query.DELETE_SAL_DETAILS,(emp,date))

    cursor.execute(query.DELETE_EMP_INC_DETAIL,(emp,date,template))
    con.commit()


if __name__ == '__main__':
    data = get_valid_employee('2018-02-01', '2018-02-28', '%3%')
    count = 0
    for record in data:
        print(record)
        delete_increment_entries(record[0], record[1] , record[2])

    Connection.close_cursor()
    Connection.connection_close()

