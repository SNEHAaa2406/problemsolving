# Find Duplicate Elements
# Use a dictionary to identify elements appearing more than once.
arr = [4, 2, 7, 2, 8, 4, 9, 7, 3]
new={}
for i in arr:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
for key,value in new.items():
    if value>1:
        print(key)
