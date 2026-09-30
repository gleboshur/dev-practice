n, m = [int(el) for el in input().split()]
symbols = [".", "*"]

for i in range(n):
    for j in range(m):
        print(symbols[0], end=" ")
        symbols.reverse()
    if m % 2 == 0:
        symbols.reverse()
    print()
