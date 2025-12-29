#Команда 1
text = input("")
clean = "".join([ch.lower() for ch in text if ch.isalpha() or ch.isspace()])
res= clean.split()
print(clean)
print(res)