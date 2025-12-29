# main.py

def main():
    day_temps = []
    night_temps = []
    
    try:
        with open("data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                day_temps.append(int(parts[0]))
                night_temps.append(int(parts[1]))
    except FileNotFoundError:
        print("Ошибка: запустите generate_data.py")
        return
    
    n = len(day_temps)
    print(f"Загружено данных за {n} дней.\n")
    
    k = 7
    moving_averages = []
    
    current_sum = sum(day_temps[:k])
    moving_averages.append(current_sum / k)
    
    for i in range(1, n - k + 1):
        current_sum = current_sum - day_temps[i - 1] + day_temps[i + k - 1]
        moving_averages.append(current_sum / k)
        
    print(f"--- Анализ трендов ---")
    print(f"Средняя темп. первой недели: {moving_averages[0]:.2f}°C")
    print(f"Средняя темп. последней недели: {moving_averages[-1]:.2f}°C")
    
    if moving_averages[-1] > moving_averages[0]:
        print(">> Вывод: Наблюдается глобальное потепление (сезонный рост).")
    else:
        print(">> Вывод: Похолодание.")
        
    anomalies = []
    for i in range(n):
        diff = day_temps[i] - night_temps[i]
        if diff > 10:
            anomalies.append((i+1, diff)) 
            
    print(f"Найдено аномальных дней: {len(anomalies)}")
    if anomalies:
        print(f"Примеры (День: Разница): {anomalies[:3]}...")

    max_warming_streak = 0
    current_streak = 0
    
    for i in range(1, n):
        if day_temps[i] > day_temps[i-1]:
            current_streak += 1
        else:
            max_warming_streak = max(max_warming_streak, current_streak)
            current_streak = 0
            
    max_warming_streak = max(max_warming_streak, current_streak) 
    
    print(f"Самая длинная серия непрерывного роста температуры: {max_warming_streak} дней")

if __name__ == "__main__":
    main()