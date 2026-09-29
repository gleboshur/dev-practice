n = int(input())
numbers = [[i for i in range(1, n + 1)] for _ in range(n)]
print(*numbers, sep='\n')


# for i in range(n):
#     numbers.append([i for i in range(1, n + 1)])

# for row in numbers:
#     print(row)
    