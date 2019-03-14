__author__ = 'gaa8664'
get_loan_detail = '''SELECT ID, Employee, FromDate, PrincipalAmount, LoanType
                    From LoanHistory
                    WHERE 1=1
                      AND LoanType ='9||Festival'
                       AND FromDate >= '2017-04-01'
                       AND EMPLOYEE = %s
                       --AND AMOUNT = 1000.00
                    ORDER BY FromDate
                       '''

update_loan_detail = '''
    UPDATE Loan SET LASTMONTHSDUE = 1200, MONTHLYDue = 1200
    WHERE 1=1
	  AND Employee = %s
	  AND LOANTYPE = '9||Festival'
	  AND ISSUEDATE >= '2017-04-01'
	  AND LASTMONTHSDUE = 1000
'''
update_loan_history = '''
  UPDATE LOANHISTORY SET AMOUNT = 1200.00,BALANCEAMOUNT = 1200, PRINCIPALAMOUNT = 1200
  WHERE 1=1
	AND Employee = %s
	AND FROMDATE >= '2017-04-01'
	AND LOANTYPE = '9||Festival'
    AND AMOUNT = 1000
'''

delete_loan_record = '''
  DELETE FROM LOANHISTORY
    WHERE 1=1
    AND ID = %d
'''


