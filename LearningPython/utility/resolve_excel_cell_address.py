__author__ = 'gaa8664'
from utility.alphabet_dict import alphabet_dict;


def get_cell_number(row_id, column_id):
    pass


def get_row_address(row_id):
    row_add = []
    while row_id > 0:
        rem = row_id % 26
        if rem == 0:
            row_add.append('Z')
            row_id = row_id // 26 - 1
        else:
            row_add.append(chr((rem - 1) + ord('A')))
            row_id = row_id // 26
    reversed(row_add)
    return ''.join(row_add)


if __name__ == '__main__':
    print(get_row_address(703))

