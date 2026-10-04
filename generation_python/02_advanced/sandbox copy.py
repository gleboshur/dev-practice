n, m = [int(el) for el in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]
cur_num = 1
i, j = 0, 0
up, down = 0, n - 1
left, right = 0, m - 1
direction = "right"

while cur_num <= n * m:
    matrix[i][j] = cur_num

    if direction == "right":
        if j < right:
            j += 1
        else:
            i += 1
            up += 1
            direction = "down"

    elif direction == "down":
        if i < down:
            i += 1
        else:
            j -= 1
            right -= 1
            direction = "left"

    elif direction == "left":
        if j > left:
            j -= 1
        else:
            i -= 1
            down -= 1
            direction = "up"

    elif direction == "up":
        if i > up:
            i -= 1
        else:
            j += 1
            left += 1
            direction = "right"

    cur_num += 1

for row in matrix:
    print(*[str(i).ljust(2) for i in row])
