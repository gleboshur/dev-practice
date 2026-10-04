n, m = [int(el) for el in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]



for row in matrix:
    print(*[str(i).ljust(2) for i in row])
