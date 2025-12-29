def max_sum(arr, k):
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k должно быть положительным целым числом")

    n = len(arr)
    if k > n:
        raise ValueError("k не может быть больше длины массива")

    current_sum = sum(arr[:k])
    best_sum = current_sum

    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum
