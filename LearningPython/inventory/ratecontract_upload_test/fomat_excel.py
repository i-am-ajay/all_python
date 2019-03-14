__author__ = 'gaa8664'
'''
    Program will read rate contract data from an excel sheet and will format it in desired format for comparison with database data.
'''
import openpyxl


class ExcelReader:

    def __init__(self, file_name, sheet_name):
        self.workbook_name = file_name
        self.workbook = openpyxl.load_workbook(file_name)
        self.sheet_name = self.workbook[sheet_name]
        self.new_sheet = self.workbook.create_sheet('new_sheet')

    # read excel
    def read_ratecontract_excel(self):
        sheet_name = self.sheet_name
        for row in sheet_name:
            self.process_excel_record(row[1].value,row[2].value)

    # Split store on the basis of comma and store in a list
    def process_excel_record(self, rc_no, stores):
        store_list = stores.split(',')
        self.add_data_in_excel(rc_no,store_list)

    def add_data_in_excel(self, rc_no, store_list):
        sheet = self.new_sheet
        for store in store_list:
            sheet.append([rc_no,store])

    def save_workbook(self):
        self.workbook.save(self.workbook_name)


if __name__ == '__main__':
    var = ExcelReader('C:\\Users\\gaa8664\\Downloads\\RC Color Code Store link.xlsx','RC')
    var.read_ratecontract_excel()
    var.save_workbook()