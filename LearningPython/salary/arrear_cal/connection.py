__author__ = 'gaa8664'
import pymssql
import pymysql

con = pymssql.connect(server="GDITSN033\SQLPROD",user="sa",password="sgrh@2016",database="ProdigiousDB")
con_mysql = pymysql.connect(host="127.0.0.1", user="root", password="admin", database="emp_arrear")

