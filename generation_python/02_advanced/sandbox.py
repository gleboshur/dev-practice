def longest(a1, a2):
    myset = sorted(set(a1) | set(a2))
    return ''.join(myset)

print(longest(a, b))