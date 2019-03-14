__author__ = 'gaa8664'


def calc_compound_interest(rate, principal, duration):
    years = range(duration)
    earnings = principal
    for x in years:
        earnings += earnings * rate/100

    return earnings

if __name__ == '__main__':
    print(calc_compound_interest(7.8, 700000, 30))