#s = "radar"
s = "Iphone"
left, right = 0, len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("Не палиндром")
        break
    left += 1
    right -= 1

else:
    print("Палиндром")
