__author__ = 'gaa8664'

import pymssql

con = pymssql.connect(server="gditsn033\\sqlprod", user="sa",password="sgrh@2016", database="ProdigiousDB")

if __name__ == "__main__":
    con