__author__ = 'gaa8664'

FOX_PROD_SALHEADS = {}
HEAD_SEQUENCE = {}
SEQUENCE_HEAD_MAP = {}
COMMON_HEAD_FOX_HEAD_MAP = {}

PAY_PERIOD = '9||01/{month}/{year}||30/{0}/{1}||0'

def get_pay_period(month, year):
    return '9||01/{month}/{year}||__/{month}/{year}||0'.format(month=month, year=year)


if __name__ == '__main__':
    print(get_pay_period(4,2016))