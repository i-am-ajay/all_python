__author__ = 'gaa8664'


def future_value(rate, installments, installment_amount, current_value=0, **time):
    fv = installment_amount*((1.00 + (0.01 * rate))**installments)
    return fv


if __name__ == '__main__':
    print(future_value(7.8, 30, 1500000))

