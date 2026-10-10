import array as arr
a=arr.array('i',[78,1,52,2])
small=a[0]
for i in a :
    if i<small:
        small=i
print(small)