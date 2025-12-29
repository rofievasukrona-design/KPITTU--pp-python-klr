#binary search

products=[]

products.sort(key=lambda x: x[0])

def binary_search(products, name):
    left, right = 0, len(products) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_name, mid_price = products[mid]

        if mid_name == name:
            return mid_price
        elif mid_name < name:
            left = mid +1
        else:
            right = mid - 1
    
    return None

print(binary_search(products, "Ананас"))
