def find_pair(prices, target):
    l, r=0, len(prices)-1
    while l<r:
        s=prices[l]+prices[r]
        if s==target: 
            return prices[l], prices[r]
        elif s< target: 
            l+=1
        else:
            r-=1

print(find_pair([0, 5, 10, 8, 0, 110],70))