__author__ = 'gaa8664'
import openpyxl
from demographic import Query
from demographic import db_connection

workbook = openpyxl.Workbook();
sheet = workbook.create_sheet('Demo')
header_list = ['EmpCode','EmpName','Dept','Des','DOB','DOJ','GRADE','PANNo','Type','Category','Account No','PF','UAN','Aadhar Card No'];
sheet.append(header_list)

con = db_connection.get_connection()
cursor = con.cursor()
cursor.execute(Query.GET_EMP_LIST)
emp_list = cursor.fetchall()

for emp in emp_list:
    print(emp)
    demo_list = []
    # get emp demographic
    cursor.execute(Query.GET_EMP_DEMO,(emp,))
    emp_demo = cursor.fetchone()
    #get emp bank
    cursor.execute(Query.GET_EMP_BANK,(emp,))
    emp_bank = cursor.fetchone()
    #get emp pf
    cursor.execute(Query.GET_EMP_PF,(emp,))
    emp_pf = cursor.fetchone()
    if not emp_pf:
        emp_pf = ['']
    # get emp uan
    cursor.execute(Query.GET_EMP_UAN,(emp,))
    emp_uan = cursor.fetchone()
    if not emp_uan:
        emp_uan = ['']

    #get aadhar details
    cursor.execute(Query.GET_EMP_AADHAR,(emp,))
    emp_aadhar = cursor.fetchone()
    if not emp_aadhar:
        emp_aadhar = ['']
    print(emp_demo)
    demo_list +=(list(emp_demo))
    demo_list +=(list(emp_bank))
    demo_list +=(list(emp_pf))
    demo_list +=(list(emp_uan))
    demo_list +=(list(emp_aadhar))
    sheet.append(demo_list)
cursor.close()
workbook.save('e://demo.xlsx');



