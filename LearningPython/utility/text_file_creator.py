import os.path
from utility.excel_processor import ExcelProcessor


def create_tab_delimited_file(file_name=''):
    dir_path = os.path.dirname(file_name)
    new_dir_path = os.path.join(dir_path,'txt_to_upload_july')
    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)
    excel_processor = ExcelProcessor(file_name)
    sheets_list = excel_processor.get_workbook_sheets()
    count = 0
    for sheet in sheets_list:
        file = str(sheet)+'.txt'
        file_path = os.path.join(new_dir_path,file)
        file = open(file_path,'w')
        worksheet = excel_processor.get_sheet(sheet)
        row_count = 0
        for row in worksheet:
            if row_count == 0:
                row_count +=1
                continue
            emcode = row[0].value
            amount = row[1].value
            if amount == 0 or amount == '' or amount is None:
                continue
            string = str(emcode)+'\t'+str(amount)+'\r\n'
            file.write(string)
        file.close()



if __name__ == '__main__':
    create_tab_delimited_file('D:/July/salary_workbook.xlsx')

