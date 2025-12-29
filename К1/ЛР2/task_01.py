#ЛР-1
a = int(input("a = "))
b = int(input("b = "))
start = min(a, b)
stop = max(a, b)
s = 0
for i in range(start, stop+1):
    if i % 2 == 0:
        continue
    s+=i
print(s)