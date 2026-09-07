num = int(input())
res = ""
while num != 0:
    res = str(num % 2) + res
    num //= 2
print(res)
