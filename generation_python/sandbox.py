s = input()
if (
    9 <= len(s) <= 10
    and (s[0]+s[4:6]).isupper()
    and (s[0]+s[4:6]).isalpha()
    and s[6] == '_'
    and s[0] in 'АВЕКМНОРСТУХ'
    and s[4] in 'АВЕКМНОРСТУХ'
    and s[5] in 'АВЕКМНОРСТУХ'
    and (s[1:4]+s[7:]).isdigit()
):
    print('YES')
else:
    print('NO')
