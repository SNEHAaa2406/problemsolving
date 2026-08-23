# Replace Negative Numbers
# Replace every negative number in a list with 0.

arr=[10,10,24,-4,-87,5,-8]
for i in range(len(arr)):
    if arr[i]<0:
        arr[i]=0
print(arr)