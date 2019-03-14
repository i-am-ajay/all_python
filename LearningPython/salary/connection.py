__author__ = 'gaa8664'
import pymssql

class Connection:

    class DBConnection:
        def __init__(self):
            self.con = pymssql.connect(server='gditsn033\sqlprod', user='sa', password='sgrh@2016', database='ProdigiousDB')

    __connection = None # static or class variable
    __cursor = None

    def __init__(self):
        if not Connection.__connection:
            Connection.__connection = Connection.DBConnection().con

    def __enter__(self):
        self.cursor = Connection.__connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        #Connection.__connection.close()

    @staticmethod
    def connection_close():
        Connection.__connection.close()


    @staticmethod
    def get_connection():
        Connection()
        return Connection.__connection

    @classmethod
    def get_cursor(cls):
        if not cls.__cursor:
            cls.__cursor = Connection.__connection.cursor()
        return cls.__cursor

    @classmethod
    def close_cursor(cls):
        cls.__cursor.close()
