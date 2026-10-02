n, m = [int(el) for el in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]
cur_row = 0
cur_number = 1
i, j = 1, 0

for _ in range(5):
    while matrix[cur_row][j] == 0:
        matrix[cur_row][j] = cur_number
        cur_number += 1
        if j < m - 1:
            j += 1

    cur_col = j
    j -= 1

    while matrix[i][cur_col] == 0:
        matrix[i][cur_col] = cur_number
        cur_number += 1
        if i < n - 1:
            i += 1

    cur_row = i
    i -= 1

    while matrix[cur_row][j] == 0:
        matrix[cur_row][j] = cur_number
        cur_number += 1
        if j > 0:
            j -= 1

    cur_col = j

    while matrix[i][cur_col] == 0:
        matrix[i][cur_col] = cur_number
        cur_number += 1
        if i > 0:
            i -= 1

    cur_row = i


for row in matrix:
    print(*[str(i).ljust(2) for i in row])
