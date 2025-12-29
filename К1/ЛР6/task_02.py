def max_sum(arr, k):
    if len(arr) < k:
        return []
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_start_index = 0
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i - k + 1
        
    return arr[max_start_index : max_start_index + k]

arr = [-5, -1, -2, -10]
k = 2
result = max_sum(arr, k)
print(f"Лучший подмассив : {result}")