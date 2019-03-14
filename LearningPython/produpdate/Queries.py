__author__ = 'gaa8664'

# Queries to record the employee redesignation info.
''' Query to insert name who authorized redesignation
    @param1 : Emp Code
    @param2 : Authority Designation
'''
INS_AUTH_DES = """INSERT INTO EMPINFO (COMPANY, EMPLOYEE, INFO, IVALUE, RECNO)
                    VALUES ('9', %s,'Redesignation||Approved By Desig',%s,1)"""
''' Query to insert designation who authorized redesignation
    @param1 : Emp Code
    @param2 : Authority Name
'''
INS_AUTH_NAME = """INSERT INTO EMPINFO (COMPANY, EMPLOYEE, INFO, IVALUE, RECNO)
                    VALUES ('9', %s,'Redesignation||Approved By Name',%s,1)"""
'''Query to insert old designation
    @parma1: Emp Code
    @param2: Old Designation
'''
INS_REDES_FROM = """INSERT INTO EMPINFO (COMPANY, EMPLOYEE, INFO, IVALUE, RECNO)
                      VALUES ('9', %s,'Redesignation||Redesignation From',%s,1)"""
''' Query to insert new  designation
    @param1: Emp Code
    @param2: New Designation
'''
INS_REDES_TO = """INSERT INTO EMPINFO (COMPANY, EMPLOYEE, INFO, IVALUE, RECNO)
                      VALUES ('9', %s,'Redesignation||Redesignation To',%s,1)"""
''' Query to insert new date
    @param1: Emp Code
    @param2: Date
'''
INS_REDES_DATE = """INSERT INTO EMPINFO (COMPANY, EMPLOYEE, INFO, IVALUE, RECNO)
                        VALUES ('9', %s,'Redesignation||Redesignation Date','19/07/2011',1)"""


''' Query to find GAA Numbers of Employee with given designations
    @param1 : Designation
'''
GET_EMPCODES = """SELECT EMPLOYEE.EMPCODE,
                  EMPLOYEE.DESIGNATION,
                  EMPLOYEE.A
                  FROM EMPLOYEE(NOLOCK)
                  WHERE 1=1
	                AND EMPLOYEE.DESIGNATION IN (%s)
	                AND EMPLOYEE.STATUS = '1'
	              ORDER BY
	                EMPLOYEE.EMPCODE
	  --              AND EMPLOYEE.EMPCODE = 'GAA1050'"""

''' Query to update designation
    @param1 : Designation_code
    @param2 : Emp Code
'''
UPDATE_DES = """UPDATE EMPLOYEE
	            SET EMPLOYEE.DESIGNATION = %s
	            WHERE EMPCODE = %s"""

DELETE_ROWS = """
    SELECT * FROM LOANHISTORY(NOLOCK)
    WHERE 1=1
    AND ID = %d
"""

UPDATE_BANK_ACC = """
    UPDATE EMPBANK SET
      ACCOUNTNAME = %s,
      ACCOUNTNO = %s,
      BANKNAME = 'Syndiate Bank',
      COMPANY = 9
    WHERE 1=1
      AND EMPCODE = %s
"""
UPDATE_PAN = """
    UPDATE EMPLOYEE SET
      PANNO = %s
    WHERE 1=1
      AND EMPCODE = %s
"""

UPDATE_DOB= """
    UPDATE EMPLOYEE SET
      DOB = %s
    WHERE 1=1
      AND EMPCODE= %s
"""

UPDATE_DOJ= """
    UPDATE EMPLOYEE SET
      DOJ = %s
    WHERE 1=1
      AND EMPCODE= %s
"""

UPDATE_Designation = """
    UPDATE EMPLOYEE SET
      DESIGNATION = %s
    WHERE 1=1
      AND EMPCODE = %s
"""

UPDATE_DEPARTMENT = """
    UPDATE EMPLOYEE SET
      DEPARTMENT = %s
    WHERE 1=1
      AND EMPCODE = %s
"""

UPDATE_PF_START_DATE = """
    UPDATE EmployeePFDeclarationForm SET
      PFStartDate = %s
    WHERE 1=1
      AND EMPLOYEE = %s
"""