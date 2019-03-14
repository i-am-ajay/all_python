__author__ = 'gaa8664'

import pymssql
import psycopg2
import pyodbc

class Trak_connection:
    connection_trak = pyodbc.connect("dsn=TRAK; UID=test; PWD=test")


class Prodigious_connection:
    connection = pymssql.connect(server='gditsn033\sqlprod',user='sa', password='sgrh@2016',database='ProdigiousContainer')
    connection_db = pymssql.connect(server='gditsn033\sqlprod',user='sa', password='sgrh@2016',database='ProdigiousDB')

    @classmethod
    def get_connection(cls):
        return cls.connection

    @classmethod
    def get_proddb_connection(cls):
        return cls.connection_db

    @classmethod
    def close_connection(cls):
        cls.connection.close()

    @classmethod
    def close_proddb_connection(cls):
        cls.connection_db.close()

class Postgres_connection:
    connection = psycopg2.connect(dbname='Inventory', user='postgres', password='admin', host='localhost')

    @classmethod
    def get_connection(cls):
        return cls.connection

    @classmethod
    def close_connection(cls):
        cls.connection.close()

if __name__ == '__main__':
    #Postgres_connection.get_connection()
    #Postgres_connection.close_connection()

    obj = Trak_connection()
    con = obj.connection_trak
    cursor = con.cursor()
    cursor.execute("SELECT TOP 10 HOSP_ParRef->INCI_Code, HOSP_UnitCost FROM INC_ItmHosp where HOSP_UnitCost > 100000")
    recordset = cursor.fetchall()
    for row in recordset:
        print(row)

    con.close()

