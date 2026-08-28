a = [45, 78, 12, 4, 5]

number = a[0]

for i in range(len(a)):
    if a[i] > number:
        number = a[i]

print("Largest number is:", number)