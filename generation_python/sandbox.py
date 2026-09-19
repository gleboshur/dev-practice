num = input().split('-')
if len(num) == 3 or (len(num) == 4 and num[0] == '7'):
    if len(num[-3]) == 3 and len(num[-2]) == 3 and len(num[-1]) == 4  and num[-3].isdigit() and num[-2].isdigit() and num[-1].isdigit():
        print('YES')
    else:
        print('NO')
else:
    print('NO')