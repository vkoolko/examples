
def find_digits(string: str):
    ''' Поиск целых чисел в строке
    :param string:  строка в которой надо найти числа
    :return: список получившихся целых чисел
    '''
    digits = []
    previous_is_digit = False
    for s in string:
        if s.isdigit():
            if previous_is_digit:
                index = len(digits) - 1
                digits[index] = digits[index] + s
            else:
                digits.append(s)
        previous_is_digit = s.isdigit()
    return [int(n) for n in digits]


if __name__ == '__main__':
    string = "switchport trunk allowed vlan 1,3,10,20,30,100:3434"
    digits = find_digits(string)
    print(digits)
