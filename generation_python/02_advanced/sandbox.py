n = int(input())
matrix = []
numbers = list(range(n))

for i in range(n):
    matrix.append(numbers[:i+1][::-1] + numbers[1:n-i])
    print(*matrix[i])
    