from salary.connection import Connection
from salary import query
__author__ = 'gaa8664'


class EmpProdSalary:

    @staticmethod
    def get_emp_salary(self, gaa_num, pay_period):
        with Connection() as cursor:
            cursor.execute(query.EMP_SAL,(gaa_num, pay_period))
            for row in cursor.fetchall():
                for col in row:
                    print(col)


if __name__ == '__main__':
    EmpProdSalary.get_emp_salary()
