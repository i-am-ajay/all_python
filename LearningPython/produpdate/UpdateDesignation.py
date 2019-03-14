from produpdate import GlobalVars

__author__ = 'gaa8664'
from connection import Connection
from produpdate.Queries import *
from pprint import pprint


class DesUpdate:

    @staticmethod
    def get_records():
        with Connection() as cursor:
            cursor.execute(GET_EMPCODES,('Designation||120',))
            result_set = cursor.fetchall()
            pprint(result_set)
            print(len(result_set))
            for empcode, descode in result_set:
                print(empcode)
                DesUpdate.inser_redesignation_info(empcode, descode, cursor)
                DesUpdate.update_emp_designation(empcode, descode, cursor)
                cursor.connection.commit()


    # Insert a new entry in redesignation module of prodigious, to keep history of designation change
    @staticmethod
    def inser_redesignation_info( empcode, descode, cursor):
        cursor.execute(INS_AUTH_DES,(empcode,'Addl. Director Administration')) # insert designation of authority who allowed redesignation
        cursor.execute(INS_AUTH_NAME,(empcode, 'Col. M.S. Jaswal')) # name of authority
        cursor.execute(INS_REDES_FROM,(empcode,GlobalVars.EMP_DES_MAPPING[descode])) # old designation
        cursor.execute(INS_REDES_TO,(empcode,GlobalVars.EMP_NEW_DES[descode])) # new designation
        cursor.execute(INS_REDES_DATE,(empcode)) # date of redesignation

    # Update employee designation
    @staticmethod
    def update_emp_designation(empcode, descode, cursor):
        cursor.execute(UPDATE_DES, (GlobalVars.EMP_NEW_DES_CODE[descode], empcode))

if __name__ == '__main__':
    du = DesUpdate()
    du.get_records()
