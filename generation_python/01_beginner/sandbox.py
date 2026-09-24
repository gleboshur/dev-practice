left = 0
right = int(input())
cnt = 0
while right - left > 0:
    right = (left + right) // 2
    cnt += 1
print(cnt)
