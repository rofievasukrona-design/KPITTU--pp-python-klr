from csv_utils import read_csv, write_csv, filter_rows

test_data = [
    {'name': 'Азиз', 'age': '25', 'city': 'Душанбе'},
    {'name': 'Рахима', 'age': '30', 'city': 'Худжанд'},
    {'name': 'Чамшед', 'age': '22', 'city': 'Истаравшан'},
    {'name': 'Рахмон', 'age': '28', 'city': 'Исфара'}
]
# Запись данных
print("Запись данных в test.csv...")
written = write_csv('test.csv', test_data)
print(f"Записано строк: {written}")
    
# Чтение данных
print("\nЧтение данных из test.csv...")
data = read_csv('test.csv')
print(f"Прочитано строк: {len(data)}")
for row in data:
    print(row)
    
print("\nФильтрация по возрасту > 25")
filtered = filter_rows(data, lambda row: int(row['age']) > 25)
print(f"Найдено строк: {len(filtered)}")
for row in filtered:
    print(row)
    

print("\nФильтрация по городу ")
filtered_city = filter_rows(data, lambda row: row['city'] == 'Турсунзода')
print(f"Найдено строк: {len(filtered_city)}")
for row in filtered_city:
    print(row)
