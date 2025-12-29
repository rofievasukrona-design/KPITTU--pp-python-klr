#Задача 1
a = [1, 3, 5, 5, 6, 1, 7, 6, 8, 9]

count = 0
prev = a[0]

for i in a[1:]:
    if prev < i:
        count += 1
    prev = i
    
print(count)