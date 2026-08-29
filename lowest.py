l=[45,88,22,23.99,98,21,121]
low=l[0]
for i in range (len(l)):
    if l[i]<low:
        low=l[i]
print("Lowest number is :",low)