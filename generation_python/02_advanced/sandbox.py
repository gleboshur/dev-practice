student1, student2, student3 = [set([int(el) for el in input().split()]) for _ in range(3)]

res = (student1 & student2) - student3

print(*sorted(res, reverse=True))
