n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

diagonal = [matrix[i][i] for i in range(n)]

print(sum(diagonal))