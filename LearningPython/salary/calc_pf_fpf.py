__author__ = 'gaa8664'


def calc_pf(basic, da=0, days = 31,month_in_days = 1):
    if days != 31 or days != 30:
        pf = ((basic + da)*3.67/100)/month_in_days
        pf = pf * days
    pf = (basic + da)*3.67/100
    return pf


def calc_fpf(basic, da = 0, days = 31, month_in_days=1):
    if days != 31 or days != 30:
        fpf = ((basic + da)*8.33/100)/month_in_days
        fpf = fpf * days
    fpf = (basic + da)*8.33/100
    return fpf

if __name__ == '__main__':
    print(calc_pf(8100))
    print(calc_fpf(8100))
