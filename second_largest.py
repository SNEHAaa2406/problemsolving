arr=[10, 5, 20, 8, 15]
low=0
# arr.sort()
# print(arr)
# print(" Second Largest element is :" ,arr[-2])

n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
print(arr[-2])