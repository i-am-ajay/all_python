__author__ = 'gaa8664'
import openpyxl


def foxsalary(file_name, sheet_name):
    get_sheet(file_name, sheet_name)

def get_sheet(file_name, sheet_name):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook[sheet_name]
    return sheet

if __name__ == '__main__':
    pass
    #sal_mapping(file_name='D:\Software\Software\HR Module\Salary\Fox Heads.xlsx', sheet_name='Sheet4')
