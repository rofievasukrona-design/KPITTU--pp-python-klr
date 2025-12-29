#linear search

products=[
    ("Банан", 20), 
    ("Яблоко", 10), 
    ("Ананас", 30),
    ("Груша", 50)
]

def linear_search(products, name):
    for product, price in products:
        if product == name:
            return price
    return None

print(linear_search(products, "Ананас"))