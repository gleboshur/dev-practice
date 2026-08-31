name = input()
flag = False
counter = 0
while name != "Левон":
    if name == "Александра":
        flag = True
    if flag:
        counter += 1
    name = input()
print(counter - 1)




