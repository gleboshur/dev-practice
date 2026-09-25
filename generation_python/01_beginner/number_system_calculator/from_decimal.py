def from_decimal(num, base):
    res = ''
    characters = '0123456789ABCDEF'
    while num >= base:
        res += characters[num % base]
        num //= base
    res += characters[num]
    return res[::-1]


num = int(input('Введите число: '))
base = int(input('Введите основание системы счисления: '))

print(f'{num}_10 = {from_decimal(num, base)}_{base}')