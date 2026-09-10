s = input()
first_half = s[: (len(s) + 1) // 2]
second_half = s[(len(s) + 1) // 2 :]
print(second_half + first_half)
