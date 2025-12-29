from collections import Counter 
 
text = """ 
Программа получает два числа!!! и формирует диапазон от меньшего к большему.?  
Она перебирает каждое значение, пропуская чётные через/ continue, и накапливает  сумму 
всех нечётных. Финальный результат!! выводится на экран. 
""" 
 
clean = "".join([ch.lower() for ch in text if ch.isalpha() or ch.isspace()]) 
 
words = clean.split() 
counts = Counter(words) 
 
top_10 = counts.most_common(10) 
 
long_words = Counter({w: c for w, c in counts.items() if len(w) > 6}) 
 
total = len(words)
percent = {w: round(c / total * 100, 2) for w, c in counts.items()} 
 
print("Очищенный текст и к нижнему регистру:", clean) 
print("Частотный словарь:", counts) 
print("10 самых частых слов:", top_10) 
print("Слова длиннее 6 символов:", long_words) 
print("Процентное соотношение слов:", percent)