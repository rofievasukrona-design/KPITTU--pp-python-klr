a = 0
print(f"Если в списке есть число {a} то закончивать цикл и вывести число!")

for i in range(10):     
    if i == a:         
        break 
    
print("Число:", i)