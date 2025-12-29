"""
Генератор скользящего окна с суммой элементов
"""

def sliding_sum(data, k):
    if not isinstance(k, int):
        raise TypeError("k должно быть целым числом")
    
    if k <= 0:
        raise ValueError("k должно быть положительным числом")
    
    data_list = list(data)
    
    if k > len(data_list):
        raise ValueError(f"k ({k}) не может быть больше длины данных ({len(data_list)})")
    
    window_sum = sum(data_list[:k])
    yield window_sum
    
    for i in range(k, len(data_list)):
        window_sum = window_sum - data_list[i - k] + data_list[i]
        yield window_sum
