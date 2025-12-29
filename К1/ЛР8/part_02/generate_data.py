# generate_data.py

import random 

days = 90
base_temp = 5 

data_entries = []

for day in range(days):
    trend = day * 0.2 
    noise = random.randint(-3, 3)
    
    day_temp = int(base_temp + trend + noise)
    
    night_drop = random.randint(5, 12)
    night_temp = day_temp - night_drop
    
    data_entries.append(f"{day_temp},{night_temp}")
    
with open("data.txt", "w") as f:
    for entry in data_entries:
        f.write(entry + "\n")