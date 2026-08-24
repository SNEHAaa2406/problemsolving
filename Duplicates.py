# Find Duplicate Elements
# Print all elements that occur more than once.

num=[12,12,45,45,8,5,77,77]
new=[]
repeat=[]
for i in num:
    if i not in new:
        new.append(i)
    else:
        repeat.append(i)
print("List of reverse numbers is :",repeat)