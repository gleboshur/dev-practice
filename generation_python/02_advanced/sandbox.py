n = int(input())
matrixA = [[int(num) for num in input().split()] for _ in range(n)]
matrixB = [[0 for _ in range(n)] for _ in range(n)]
matrixC = [[0 for _ in range(n)] for _ in range(n)]
m = int(input())
print()

for i in range(n):
    for j in range(n):
        matrixB[i][j] = matrixA[i][j]

for _ in range(m - 1):
    matrixC = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for q in range(n):
                matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
            
    for i in range(n):
        for j in range(n):
            matrixA[i][j] = matrixC[i][j]
    
for row in matrixC:
        print(*row)
    