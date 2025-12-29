import csv

def read_csv(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding="utf-8", newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не найден")


def write_csv(filename, data, fieldnames=None, encoding='utf-8'):
    if not data:
        print("Нет данных для записи")
        return 0
    
    if fieldnames is None:
        fieldnames = list(data[0].keys())
    
    try:
        with open(filename, 'w', encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            return len(data)
    except Exception as e:
        raise Exception(f"Ошибка при записи файла: {e}")


def filter_rows(data, condition):
    try:
        filtered = [row for row in data if condition(row)]
        return filtered
    except Exception as e:
        raise ValueError(f"Ошибка при фильтрации данных: {e}")
