import random


def is_valid(s):
    return s.isdigit() and  1 <= int(s) <= 100


def play_again():
    while True:
        choice = input()
        if choice != '1' and choice != '0':
            print('Ошибка! Введите 1 (да) или 0 (нет):')
        else:
            return choice == '1'
    
while True:
    num = random.randint(1, 100)
    prompt = 'Введите число от 1 до 100:'
    attempts = 0

    print('Добро пожаловать в числовую угадайку!')
    print(prompt)

    while True:
        attempts += 1
        user_num = input()
        if is_valid(user_num):
            user_num = int(user_num)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if user_num < num:
            print('Ваше число меньше загаданного, попробуйте еще разок', prompt, sep='\n')
        elif user_num > num:
            print('Ваше число больше загаданного, попробуйте еще разок', prompt, sep='\n')
        else:
            print(f'Вы угадали, поздравляем! Сделано попыток: {attempts}')
            print('Хотите сыграть еще раз? (1 - да, 0 - нет):')
            break
    
    if play_again():
        continue
    else:
        print('Спасибо что играли в числовую угадайку. Еще увидимся...')
        break