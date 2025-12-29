import csv

def process_csv(path):
    success_count = 0

    try:
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for line_number, row in enumerate(reader, start=1):
                try:
                    a = int(row[0])
                    b = float(row[1])

                    result = a + b
                    success_count += 1

                except (ValueError, IndexError) as e:
                    print(f"Строка {line_number}: ошибка формата -> {row}")

    except FileNotFoundError:
        print("Файл не найден")
        return

    print(f"Успешно обработано строк: {success_count}")
    
process_csv("C:\К1\К1\ЛР4\data.csv")
