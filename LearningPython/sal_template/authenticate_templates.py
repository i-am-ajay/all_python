__author__ = 'gaa8664'
from sal_template.connections import db_con
from sal_template import queries
# Compares old and new templates to find if the newly created templates are correct or not.


class AuthenticateTemplate:
    parameter_tuple = None
    def __init__(self):
        self.con = db_con.con
        self.cursor = self.con.cursor()

    def get_template_map(self, template_name, version):
        parameter_tuple = ''.join([template_name,str(version)]) if version != 0 else template_name
        new_template = self.execute_saltemp_query(parameter_tuple)
        new_template = [data[0] for data in new_template]
        version -= 1
        parameter_tuple = ''.join([template_name,str(version)]) if version != 0 else template_name
        old_template = self.execute_saltemp_query(parameter_tuple)
        old_template = [data[0] for data in old_template]
        new_template1 = new_template.copy()
        old_template1 = old_template.copy()
        for head in new_template:
            count = old_template.count(head)
            if count > 0:
                new_template1.remove(head)
                old_template1.remove(head)

        self.print_template(new_template1)
        print(template_name.center(50,'*'))
        self.print_template(old_template1)

    def print_template(self, template_code):
        from pprint import pprint
        pprint(template_code)

    def compare_templates(self,new_template, old_template):
        pass

    def execute_saltemp_query(self,parameter_tuple):
        self.cursor.execute(queries.GET_TEMPLATE,parameter_tuple)
        recordset = self.cursor.fetchall()
        return recordset

if __name__ == "__main__":
    auth_temp = AuthenticateTemplate()
    auth_temp.get_template_map('CST',1)


