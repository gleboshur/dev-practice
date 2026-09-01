price = int(input())
counter = 0
while price >= 25:
    price -= 25
    counter += 1
while price >= 10:
    price -= 10
    counter += 1    
while price >= 5:
    price -= 5
    counter += 1
while price >= 1:
    price -= 1
    counter += 1
print(counter)





