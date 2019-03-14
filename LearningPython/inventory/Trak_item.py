__author__ = 'gaa8664'

from inventory.connection import Trak_connection

trak_connection = Trak_connection()
con = trak_connection.connection_trak

import openpyxl

def rate_INC_Itm(query):
    workbook = openpyxl.Workbook()
    sheet = workbook.create_sheet("INC_Itm")
    cursor = con.cursor()
    cursor.execute(query)
    record_set = cursor.fetchall()
    count = 0
    for record in record_set:
        count = count+1
        print("{0}{1}".format(count,record))
        sheet.append(list(record))
    workbook.save("e://test_file_inc_itm.xlsx")
    con.close()

if __name__ == "__main__":
    #rate_INC_Itm("SELECT HOSP_ParRef->INCI_Code,HOSP_UnitCost FROM INC_ItmHosp where HOSP_UnitCost > 0")
    rate_INC_Itm("SELECT TOP 50000 INCI_Code, INCI_Desc, INCI_UnitCost from SQLUser.INC_Itm where INCI_UnitCost <> 0")






