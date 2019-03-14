__author__ = 'gaa8664'
import pymssql

class DbConnection():
    conn = None

    def __init__(self):
        DbConnection.conn = pymssql.connect(server="gditsn033\SQLProd",database="ProdigiousDB", user="sa", password="sgrh@2016")

    @classmethod
    def get_connection(cls):
        if not cls.conn:
            DbConnection()
        return cls.conn

# Prodigious Connection
class Prod_Con():
    def __init__(self):
        self.prod_con = DbConnection.get_connection()

    def get_con(self):
        return self.prod_con

    def close_con(self):
        self.prod_con.close()


if __name__ == "__main__":
    con = Prod_Con()
    connection = con.get_con()
    print(connection)