# Problem 4: Find the Second Largest
# Given:
arr = [10, 25, 8, 40, 32]
# Find the second largest number.
# Expected:
# 32
# Try doing it without sort().
# This is an important DSA pattern.

largest = arr[0]
second_largest = arr[0]

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)