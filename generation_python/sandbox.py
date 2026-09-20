def print_symbol_counts(s):
    chars = list(s.lower())
    chars.sort()
    res = ''
    for el in chars:
        if el not in res:
            res += el
            print(f'{el}: {chars.count(el)}')
            
s = input()
print_symbol_counts(s)