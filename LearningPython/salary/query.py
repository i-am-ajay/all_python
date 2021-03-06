__author__ = 'gaa8664'

EMP_SAL = "SELECT SUM(AMOUNT), Employee, SALHEAD FROM ProdigiousDB..PaySLIP(NOLOCK) WHERE Employee = %s  AND PayPeriod LIKE %s GROUP BY Employee, SALHEAD"
TEST_QUERY = 'SELECT TOP 10 * FROM PaySlip'
GROSS_SALRY = """
    SELECT
      EMPLOYEE,
      TYPE,
      Sum(Amount) AS Amount
    FROM
	  ProdigiousDB..PaySlip(NOLOCK)
    WHERE 1=1
	  AND EMPLOYEE = %s
	  AND PAYPERIOD LIKE %s
    GROUP BY
	  EMPLOYEE, TYPE
"""

UPDATE_LIC = '''
    Insert INTO EMPDECLARATION
(AMOUNT, COMPANY, DCLDATE, EMPLOYEE,
	HOLDDATE, INVESTMENTDATE,
	ISDOCNEEDED, ISSALARYBASED, POLICY,
	PolicyNo, PolicyOF, PrintOnPayslip, RebateAmount
	)
      VALUES
	( %s, 9, '2017-04-01', %s, '2030-03-31','2017-04-01',1,1,'LIC',%s,'SELF', 1,0)
'''

DISTINCT_EMP = '''
    SELECT
	DISTINCT PAYSLIP.EMPLOYEE
FROM
	ProdigiousDB..PAYSLIP(NOLOCK)
WHERE 1=1
	AND PAYSLIP.PAYPERIOD LIKE %s
'''

UPDATE_TEMPLATE_HEAD = '''
    UPDATE SALHISTORY
    SET AMOUNT = %s,
      SALHEAD = %s
    WHERE 1=1
      AND EMPLOYEE = %s
      AND FROMDATE = %s
'''

FIND_SALTEMPLATE_OF_EMP = '''
    SELECT
	    ET.SALTEMPLATE
	FROM ProdigiousDB..EMPSALTEMPLATE ET(NOLOCK)
    WHERE 1=1
        AND EMPLOYEE = %s
	    AND ET.FROMDATE = %s
'''

FIND_EMP_SALHISTORY_HEAD_ID = '''
    SELECT ID1
    FROM SALHISTORY(NOLOCK)
    WHERE 1=1
      AND EMPLOYEE = %s
      AND FROMDATE = %s
'''

LATEST_HEAD_AMOUNT = '''

'''

UPDATE_HEAD_AMOUNT = '''
    UPDATE AMOUNT
    FROM SALHISTORY
    WHERE 1=1
        AND EMPLOYEE = %s
        AND FROMDATE = %s
        AND ID = %s
'''
UPDATE_HEAD_AMOUNT_EMPWISE = '''
    UPDATE SALHISTORY
        SET AMOUNT = %d
    WHERE 1=1
        AND EMPLOYEE = %s
        AND FROMDATE = %s
        AND SALHEAD = %s
'''

UPDATE_EMP_AMOUNT_SALHISTORY = '''
    UPDATE SALHISTORY
    SET AMOUNT = %s
    WHERE 1=1
      AND FROMDATE = %s
      AND EMPLOYEE = %s
      AND Salhead = %s
'''

UPDATE_EMP_SALHEAD_SALHISTORY = '''
    UPDATE SALHISTORY
        SET SALHEAD = %s, AMOUNT = 0.0
        WHERE 1=1
          AND ID1 = %s
          AND FROMDATE = %s
          AND employee = %s
'''

SALARY_DETAILS_PAYSLIP = '''
    SELECT SALHEAD, AMOUNT
    FROM Payslip(NOLOCK)
    WHERE 1=1
      AND EMPLOYEE = %s
      AND Payperiod = %s
      AND SALHEAD IN ('9||MESS','9||OINC','9||VPF','9||OTHERSE')
      AND AMOUNT <> 0
'''

GET_HEAD_AMOUNT_FROM_PAYSLIP = '''
    SELECT
        AMOUNT
    FROM PAYSLIP(NOLOCK)
    WHERE 1=1
      AND EMPLOYEE = %s
      AND SALHEAD = %s
      AND Payperiod = %s
'''

GET_HEAD_LIST = '''
    SELECT
		SALHEAD
	FROM SALTEMPLATEHEAD(NOLOCK)
	WHERE 1=1
		AND SALTEMPLATEHEAD.SALTEMPLATE = %s
'''

GET_TEMPLATE_HEADS = '''
    SELECT
		SALHEAD
	FROM SALTEMPLATEHEAD(NOLOCK)
	WHERE 1=1
		AND SALTEMPLATEHEAD.SALTEMPLATE = %s
'''

FIND_SALTEMPLATE_WITH_HEAD_COUNT = '''
    SELECT
	ET.SALTEMPLATE,
	(
		SELECT COUNT(*)
		FROM ProdigiousDB..SALTEMPLATEHEAD
		WHERE SALTEMPLATE = ET.SALTEMPLATE
	),
	(
		SELECT COUNT(*)
		FROM ProdigiousDB..SALHISTORY(NOLOCK)
		WHERE 1=1
			AND EMPLOYEE = %s
			AND FROMDATE = %s
	)
    FROM ProdigiousDB..EMPSALTEMPLATE ET(NOLOCK)
    WHERE 1=1
        AND EMPLOYEE = %s
	    AND ET.FROMDATE = %s

'''

LOAN_INFO = '''
    SELECT
      EMPLOYEE,
      ISSUEDATE,
      AMOUNT,
      MonthlyDue,
      LOANTYPE,
      ID,
      SANCTION
    FROM LOAN(NOLOCK)
    WHERE 1=1
      AND EMPLOYEE = %s
      AND ISSUEDATE >= %s
'''

LOAN_DETAILS = '''
    SELECT
        ID,
        EMPLOYEE,
        FROMDATE,
        AMOUNT,
        INTERESTPAY,
        PRINCIPALAMOUNT,
        LOANDR,
        LOANTYPE
    FROM
        LOANHISTORY
    WHERE 1=1
        AND EMPLOYEE = %s
        AND LOANDR = %d
'''

UPDATE_LOAN_DATE = '''
    UPDATE LOANHISTORY
    SET FROMDATE = %s
    WHERE 1=1
	  AND LOANDR = %d
	  AND EMPLOYEE = %s
	  AND ID = %d
'''

LOAN_SELECT = '''
    SELECT
      ID,
      LOANDR,
      EMPLOYEE,
      FROMDATE,
      AMOUNT
    FROM
      LOANHISTORY
    WHERE 1=1
      AND ID = %d
'''

GET_EMPLOYEE_TEMPLATE ='''
    SELECT
      ProdigiousContainer.dbo.find_sal_template(INCTHISTORY.EMPLOYEE,INCTHISTORY.FROMDATE) AS saltemplate,
      EMPLOYEE,
      FROMDATE,
	  ID
	FROM ProdigiousDB..INCTHISTORY(NOLOCK)
    WHERE 1=1
	  AND FROMDATE BETWEEN %s AND %s
	  AND TEMPLATE IS NULL
	ORDER BY FROMDATE ASC
'''

UPDATE_TEMPLATE_INC = '''
    UPDATE INCTHISTORY
    SET TEMPLATE = %s
    WHERE 1=1
      AND EMPLOYEE = %s
      AND FROMDATE = %s
      AND ID = %d
'''
# query to get employee codes from INCTHISTORY table based on passed information
EMP_INC_DETAIL = '''
    SELECT
	    EMPLOYEE,
	    FROMDATE,
	    TEMPLATE
    FROM
	    ProdigiousDB..INCTHISTORY(NOLOCK)
    WHERE 1=1
	    AND FROMDATE BETWEEN  %s AND %s
	    AND TEMPLATE NOT LIKE %s
	    AND REMARKS <> ''
'''
DELETE_EMP_INC_DETAIL = '''
    DELETE
    FROM ProdigiousDB..INCTHISTORY
    WHERE 1=1
       AND EMPLOYEE = %s
       AND FROMDATE = %s
       AND TEMPLATE = %s
'''
# get employee template based details from EMPSALTEMPLATE
GET_EMP_SAL_TEMPLATE = '''
    SELECT *
    FROM
      ProdigiousDB..EMPSALTEMPLATE(NOLOCK)
    WHERE 1=1
      AND EMPLOYEE = %s
      AND FROMDATE = %s
      AND SALTEMPLATE = %s
'''

DELETE_EMP_SALTEMPLATE = '''
    DELETE
    FROM
      ProdigiousDB..EMPSALTEMPLATE
    WHERE 1=1
      AND EMPLOYEE = %s
      AND FROMDATE = %s
      AND SALTEMPLATE = %s
'''

# get employee sal history details form SALHISTORY
GET_SAL_DETAILS = '''
    SELECT
        *
    FROM ProdigiousDB..SALHISTORY(NOLOCK)
    WHERE 1=1
        AND EMPLOYEE = %s
	    AND FROMDATE = %s
'''

DELETE_SAL_DETAILS = '''
    DELETE
    FROM ProdigiousDB..SALHISTORY
    WHERE 1=1
        AND EMPLOYEE = %s
	    AND FROMDATE = %s
'''

