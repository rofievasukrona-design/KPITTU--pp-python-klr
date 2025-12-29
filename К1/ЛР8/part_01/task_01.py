def analyze_temperatures(temps):
    print(f"Анализ списка: {temps}")
    
    if not temps:
        print("  Список пуст.")
        return
    
    # Задача 1: Средняя температура и количество дней выше средней
    average = sum(temps) / len(temps)
    count_above = 0 # счетчик дней выше средней температуры
    for t in temps:
        if t > average:
            count_above += 1
            
    print(f"  Средняя темп: {average:.2f}")
    print(f"  Дней выше средней: {count_above}")

    # Задача 2: Длиннейшая серия без минуса (Sliding Window)
    max_sequence = 0
    current_sequence = 0
    
    for t in temps:
        if t >= 0:
            current_sequence += 1
            if current_sequence > max_sequence:
                max_sequence = current_sequence
        else:
            current_sequence = 0
            
    print(f"  Самая длинная серия без 'минуса': {max_sequence}")
    print("-" * 30)

test_cases = [
    [2, 5, -1, 3, 0, 4, 6],
    [-5, -3, -1, -2],       
    [1, 2, 3, 4, 5],        
    [0]                     
]

for case in test_cases:
    analyze_temperatures(case)