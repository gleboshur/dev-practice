n, m = [int(el) for el in input().split()]
matrixA = [[int(num) for num in input().split()] for _ in range(n)]
input()
m, k = [int(el) for el in input().split()]
matrixB = [[int(num) for num in input().split()] for _ in range(m)]
matrixC = [[0 for _ in range(k)] for _ in range(n)]
print()


for _ in range(m):
    i = 1
    for j in range(m):
        print(matrixA[i][j], end=" ")
        print(matrixB[j][i])


# for row in matrixC:
#     print(*row)
