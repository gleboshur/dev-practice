def to_decimal(num, base):
    power = len(num) - 1
    res = 0
    for digit in num:
        if digit.isalpha():
            digit = hex_char_to_int(digit)
        res += int(digit) * base**power
        power -= 1
    return res


def hex_char_to_int(chr):
    characters = 'ABCDEF'
    return characters.find(chr) + 10


num = input('Введите число: ')
base = int(input('Введите основание системы счисления: '))

print(f'{num}_{base} = {to_decimal(num, base)}_10')