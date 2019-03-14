__author__ = 'gaa8664'
import pymssql


class Connection:

    def __init__(self):
        self.connection = pymssql.connect(server = 'gditsn033\SQLPROD', database='ProdigiousDB', user='sa', password='sgrh@2016')

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()