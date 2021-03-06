__author__ = 'gaa8664'

FIND_SALARY_MONTHWISE = '''
SELECT
	EMPLOYEE,
    SUM(AMOUNT) AMOUNT
FROM
	PAYSLIP(NOLOCK)
WHERE 1=1
	AND PAYSLIP.PAYPERIOD = %s
	AND SALHEAD IN ('9||BASIC','9||HRA','9||CONALL','9||CC','9||DA')
GROUP BY
	EMPLOYEE
HAVING SUM(AMOUNT) < %d
'''

FIND_BLOCKED_EMPLOYEES = '''
	SELECT EMPLOYEE FROM PayrollStatus(NOLOCK)
	WHERE 1=1
	AND Payperiod = %
	AND (BLOCKDATE IS NOT NULL OR BLOCKDATE <> '')
'''

BLOCKED_EMPLOYEE_SALARY = '''
		SELECT
		PayrollStatus.EMPLOYEE,
		(
		SELECT SUM(AMOUNT) AMT FROM SALHISTORY(NOLOCK)
		WHERE 1=1
			AND EMPLOYEE = PayrollStatus.Employee
			AND SALHEAD IN ('9||BASIC','9||CONALL','9||DA','9||HRA','9||CC')
			AND FROMDATE <= (
				SELECT TOP 1 FROMDATE FROM ProdigiousDB..EMPSALTEMPLATE(NOLOCK)
				WHERE 1=1
				AND EMPSALTEMPLATE.EMPLOYEE = PayrollStatus.Employee
				AND EMPSALTEMPLATE.FROMDATE <= CONVERT(DATE,SUBSTRING(%s,16,10),103)
				ORDER BY FROMDATE DESC
		)
		HAVING SUM(AMOUNT) < %d
	 ) AS SAL_AMT
	FROM
		PayrollStatus(NOLOCK)
	WHERE 1=1
	 	AND (PayrollStatus.BLOCKDATE IS NOT NULL OR PayrollStatus.BLOCKDATE <> '')
		AND PayrollStatus.Payperiod = %s
'''

FIND_EMP_DETAILS = '''
    SELECT
        EMPCODE,
	    RTRIM(CONCAT(RTRIM(CONCAT(FIRSTNAME,' ',MIDDLENAME)),' ',LASTNAME)) NAME,
	    CommonCodes.Description DESIG,
	    DEPTTABLE.Description Dept,
	    SeperationTable.Description Seperation,
	    Employee.Status,
	    EMPINFO.IValue Category,
	    GRADETABLE.Description LEVEL,
		TypeTable.Description Type
	FROM
	    EMPLOYEE(NOLOCK)
    INNER JOIN
        COMMONCODES(NOLOCK) ON 1=1
	    AND EMPLOYEE.DESIGNATION = CommonCodes.ID
	    AND CommonCodes.TYPE = 'DESIGNATION'
	INNER JOIN
	    COMMONCODES DEPTTABLE(NOLOCK) ON 1=1
	    AND EMPLOYEE.DEPARTMENT = DEPTTABLE.ID
	    AND DEPTTABLE.TYPE = 'Department'
	LEFT JOIN
		COMMONCODES TypeTable (NOLOCK) ON 1=1
		AND EMPLOYEE.EMPTYPE = TypeTable.ID
		AND TypeTable.Type = 'Employee Type'
	LEFT JOIN
		COMMONCODES GRADETABLE (NOLOCK) ON 1=1
		AND EMPLOYEE.GRADE = GRADETABLE.ID
		AND GRADETABLE.TYPE = 'GRADE'
	LEFT JOIN
	    EMPINFO(NOLOCK) ON 1=1
	    AND EMPLOYEE.EMPCODE = EMPINFO.EMPLOYEE
	    AND EMPINFO.INFO = 'EMPLOYEE Category||EMPLOYEE Category'
	LEFT JOIN
		COMMONCODES SeperationTable(NOLOCK) ON 1=1
		AND EMPLOYEE.SEPERATIONTYPE = SeperationTable.ID
		AND SeperationTable.Type = 'Seperation Type'
    WHERE 1=1
        AND EMPCODE = %s
'''

GET_EMP_LIST ='''
    SELECT
        EMPCODE
    FROM
      EMPDETAILS
'''

GET_EMP_FULL_DETAILS ='''
	SELECT * FROM EMPDETAILS
	ORDER BY EMPCODE
'''

SAVE_EMP_DETAIL = '''
    INSERT INTO EMPDETAILS (EMPCODE, EMP_NAME, DESIGNATION, DEPT, SEPERATION, STATUS, CATEGORY,TYPE,LEVEL)
    VALUES
    (%s,%s,%s, %s, %s,%s,%s,%s,%s)
'''


SAVE_EMP_SAL = '''
    INSERT INTO EMP_SAL_AMOUNT ( EMPCODE, AMOUNT, DATE, MINIMUM_WAGE ) VALUES ( %s, %s, %s, %s )
'''

EMP_ARREAR_QUERY ='''
	SELECT * FROM
	empdetails
	INNER JOIN emp_sal_amount ON 1=1
		AND empdetails.empcode = emp_sal_amount.empcode
	ORDER BY empdetails.empcode,
'''

GET_EMP_FOR_ARREAR = '''
	SELECT EMPCODE FROM empdetails ORDER BY EMPCODE;
'''

EMP_SAL_ARREAR = '''
	SELECT * FROM emp_sal_amount
	WHERE 1=1 AND EMPCODE = %s;
'''

EMP_ARREAR_MONTH = '''
	SELECT DISTINCT DATE FROM emp_sal_amount ORDER BY DATE;
'''