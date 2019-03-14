__author__ = 'gaa8664'
import pymssql

connection = pymssql.connect(server="gditsn033\SQLProd", user="sa", password="sgrh@2016", database="ProdigiousDB")


def get_connection():
    return connection


def close_connection():
    connection.close()



