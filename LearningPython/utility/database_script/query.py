SELECT_EMP = '''
    SELECT TOP 1
      *
    FROM
      ProdigiousDB..EMPLOYEE(NOLOCK)
'''

SELECT_EMP_INFO = '''
    SELECT TOP 1
        *
    FROM
      ProdigiousDB..EMPINFO(NOLOCK)
'''

SELECT_COMMON_CODES = '''
      SELECT TOP 1
        *
      FROM ProdigiousDB..CommonCodes(NOLOCK)
'''