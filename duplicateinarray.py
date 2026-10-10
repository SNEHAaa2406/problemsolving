import array as arr
a=arr.array('i',[78,78,54,2,2,45,11])
new=[]
for i in a:
    if i not in new:
        new.append(i)
    else:
        pass
print(new)