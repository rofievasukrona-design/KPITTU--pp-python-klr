def sum_nested(a):
    total = 0
    for x in a:
        if isinstance(x, list):
            total += sum_nested(x)
        elif isinstance(x, (int, float)) and x > 0:
            total += x
    return total

b = [[], [[]], 1, [2]]
print(f"Результат: {sum_nested(b)}")