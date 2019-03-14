__author__ = 'gaa8664'

from utility.database_script import connections
from utility.database_script import query

datatype_map ={
            1 :'String',
            2 :'Byte[]',
            3 :'Integer',
            4 :'LocalDateTime',
            5 :'Double'
}
list_columns = []

def create_class_file(file_path,class_name,column_list,generator_name,generator_table_name ):
    first_line = True
    file = open(file_path+class_name+'.java','w')
    file.write('public class {}{}\r\n'.format(class_name,'{'))
    for column in column_list:
        if first_line:
            file.write('\t@Id\r')
            file.write('\t@GeneratedValue(generator = "{}")\r'.format(generator_name))
            file.write('\t@GenericGenerator(name="{}",strategy="enhanced-sequence",'
                       'parameters={}@org.hibernate.annotations.Parameter(name="sequence_name", value="{}"){})\r'.format(generator_name,'{',generator_table_name,'}'))
            first_line = False
        file.write('\t@Column\r')
        file.write('\tprotected {} {};\r\n'.format(column[1],column[0].casefold()))
    file.write('\r\n}')
    file.close()

def create_class(file_path, class_name, generator_name, generator_table_name):
    cursor = connections.Connections.get_prodigious_connection()
    recordset = cursor.execute(query.SELECT_COMMON_CODES)
    recordset = cursor.description
    for record in recordset:
        #print('{}->{}'.format(record[0],record[1]))
        #print('{}->{}'.format(record[0],datatype_map[record[1]]))
        list_columns.append([record[0],datatype_map[record[1]]])
    create_class_file(file_path,class_name, list_columns, generator_name, generator_table_name)


if __name__ == '__main__':
    create_class('e:\\','DeptCommonCodes','my_generator','emp_generator_table')