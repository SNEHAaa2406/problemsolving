# Count how many times each number appears in a list

numbers = [2, 4, 2, 7, 4, 2, 9, 7, 4, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Number Frequency:")

for num, count in frequency.items():
    print(num, "->", count)