__author__ = 'gaa8664'
import openpyxl

'''
    Find employees whose salary created in Fox but missing in Prodigious and Employees whoes salary exists in Prod but missing in Fox for a salary month.
    * Get employee list from Fox excel list A.
    * Get employee list from Prodigious B.
    * Compare two lists and a apply A-B and B - A set operation
'''



def select_fox_emp_list(path, sheet):
    fox_salary_excel = openpyxl.load_workbook(path)
    get_salary_sheet = fox_salary_excel[sheet]
    #max_col = get_salary_sheet.