__author__ = 'gaa8664'

GET_TEMPLATE = '''
    SELECT
        SALHEAD
    FROM
        ProdigiousDB..SALTEMPLATEHEAD(NOLOCK)
    WHERE 1=1
        AND SALTEMPLATE = %s
'''

GET_EMP_WITH_NEWTEMP ='''
    SELECT
        EMPLOYEE,
        SALTEMPLATE SalTemp,
        (
             SELECT TOP 1
                FROMDATE
            FROM
                ProdigiousDB..EMPSALTEMPLATE TemplateDate(NOLOCK)
            WHERE 1=1
                AND TemplateDate.Employee = EMPSALTEMPLATE.EMPLOYEE
                AND TemplateDate.SALTEMPLATE = EMPSALTEMPLATE.SALTEMPLATE
            ORDER BY FROMDATE DESC
        ) FromDate
    FROM
      ProdigiousDB..EMPSALTEMPLATE(NOLOCK)
    WHERE 1=1
      AND SALTEMPLATE = %s
'''
LATEST_TEMP_CHANGE_DATE ='''
    SELECT
      TOP 1 FROMDATE
    FROM
      SALHISTORY(NOLOCK)
    WHERE 1=1
      AND SALHISTORY.EMPLOYEE = %s
      AND SALHISTORY.SALHEAD = '9||BASIC'
    ORDER BY FROMDATE DESC
'''
GET_LAST_DATE_TEMP_EMP ='''
    SELECT TOP 1
        FROMDATE
    FROM
      ProdigiousDB..EMPSALTEMPLATE(NOLOCK)
    WHERE 1=1
      AND SALTEMPLATE = %s
      AND EMPLOYEE = %s
    ORDER BY FROMDATE DESC
'''

GET_AMOUNT_OLDTEMP = '''
    SELECT TOP 1
	    AMOUNT,
	    ID1
    FROM
		ProdigiousDB..SALHISTORY(NOLOCK)
    WHERE 1=1
	    AND EMPLOYEE = %s
	    AND SALHEAD = %s
	    AND FROMDATE = %s
	ORDER BY ID1 DESC
'''

UPDATE_AMOUNT_NEWTEMP = '''
    UPDATE
        SALHISTORY
    SET
        AMOUNT = %d
    WHERE 1=1
        AND EMPLOYEE = %s
        AND SALHEAD = %s
        AND FROMDATE = %s
        AND ID1 = %d
'''
INSERT_HEAD_SALHISTORY = '''
    INSERT INTO SALHISTORY
      (Amount, Company, Employee, FromDate, Salhead)
      VALUES
      (0.0,9,%s,%s,%s)
'''

FIND_SALHEAD_ENTRY = '''
    SELECT TOP 1
        EMPLOYEE
    FROM SALHISTORY
    WHERE 1=1
      AND EMPLOYEE = %s
      AND SALHEAD = %s
      AND FROMDATE = %s
'''

UPDATE_AMOUNT_TEMP = '''
    UPDATE
      SALHISTORY
    SET AMOUNT = %d
    WHERE 1=1
      AND EMPLOYEE = %s
      AND SALHEAD = %s
      AND FROMDATE = %s
'''

'''
    SELECT TOP 1 FROMDATE
    FROM SALHISTORY(NOLOCK)
    WHERE 1=1
        AND EMPLOYEE = %s
        AND SALHEAD = '9||BASIC'
    ORDER BY FROMDATE DESC
'''

if __name__ == '__main__':
    pass