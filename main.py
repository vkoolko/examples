

if __name__ == '__main__':
    config = "switchport trunk allowed vlan 1,3,10,20,30,100:3434"
    digits = []
    previous_is_digit = False
    for s in config:
        if s.isdigit():
            if previous_is_digit:
                index = len(digits) - 1
                digits[index] = digits[index] + s
            else:
                digits.append(s)

        previous_is_digit = s.isdigit()

    print(digits)
