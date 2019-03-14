__author__ = 'gaa8664'
import pymssql

__con = pymssql.connect(server = 'gditsn033\SQLPROD', database='ProdigiousDB', user='sa', password='sgrh@2016')

def get_con():
    return __con

if __name__ == '__main__':
    __con.close()
    print(__con)
