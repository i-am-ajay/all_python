__author__ = 'gaa8664'
import pymssql

class Connections:

    prod_connection = None
    trak_connection = None
    cursor = None
    pass
    def __init__(self):
        pass

    @classmethod
    def get_prodigious_connection(cls):
        if not Connections.prod_connection :
            Connections.prod_connection = pymssql.connect(server = 'gditsn033\sqlprod', user = 'sa', password = 'sgrh@2016', database = 'ProdigiousDB')
            Connections.cursor = Connections.prod_connection.cursor()

        return Connections.cursor

    @classmethod
    def close_prod_connection(self):
        if not Connections.prod_connection:
            Connections.prod_connection.close()


