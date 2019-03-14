__author__ = 'gaa8664'
import inventory.connection as connection
import inventory.query as query
import openpyxl

'''
    A program that will read data from the given query and will copy it to an excel file.
'''

data_workbook = None
data_sheet = None

def read_data_from_database(query, parameter_tuple, workbook_name, sheet_title):
    #cursor = connection.get_proddb_connection().cursor(as_dict=True) #Prodigious Connection
    cursor = connection.get_connection().cursor(as_dict=True) # Get prodigious container connection
    cursor.execute(query,parameter_tuple)
    records = cursor.fetchall()
    header_set = False
    for record in records:
        if not header_set:
            header_list = record.keys()
            create_excel(workbook_name,sheet_title, header_list)
            header_set = True
        row = record.values()
        add_data_to_excel(workbook_name,sheet_title,list(row) )


    cursor.close()
    #connection.close_proddb_connection() # Close Prodigious connection
    connection.close_connection() # Close ProdigiousContainer connection
    return header_list


def create_excel(workbook_name, sheet_title, header_list):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_title
    sheet.append(list(header_list))
    workbook.save(workbook_name)


def add_data_to_excel(workbook_name, sheet, data_row):
    global data_workbook
    global data_sheet
    if not data_workbook :
        data_workbook = openpyxl.load_workbook(workbook_name)
        data_sheet = data_workbook[sheet]
    print(data_row)
    data_sheet.append(data_row)



def populate_excel():
    pass

if __name__ == '__main__':
    global data_workbook
    workbook_name = 'E://title.xlsx'
    list_x = read_data_from_database(query.PO,('2017-01-01','2017-12-31'),'E://title.xlsx','test')
    data_workbook.save(workbook_name)




