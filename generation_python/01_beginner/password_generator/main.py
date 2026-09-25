import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


chars = ''

quantity = int(input('Введите количество паролей: '))
length = int(input('Введите длину одного пароля: '))

if input('Включать ли цифры? (д - да, н - нет) ') == 'д':
    chars += digits
if input('Включать ли прописные буквы? (д - да, н - нет) ') == 'д':
    chars += uppercase_letters
if input('Включать ли строчные буквы? (д - да, н - нет) ') == 'д':
    chars += lowercase_letters
if input('Включать ли символы !#$%&*+-=?@^_ ? (д - да, н - нет) ') == 'д':
    chars += punctuation
if input('Исключать ли неоднозначные символы il1Lo0O? (д - да, н - нет)') == 'д':
    for s in 'il1Lo0O':
        chars = chars.replace(s, '')

for _ in range(quantity):
    print(generate_password(length, chars))