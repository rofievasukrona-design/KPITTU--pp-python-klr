items = []

sorted_by_price = sorted(items, key = lambda x: x[1])

sorted_by_name = sorted(items, key = lambda x: x[0])

print("По цене:", sorted_by_price)
print("По название:", sorted_by_name)

