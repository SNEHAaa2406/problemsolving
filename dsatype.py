# Find the element that appears only once when all other elements appear twice
import array as arr
a=arr.array('i',(78,78,54,54,2,11,11))
for i in a :
    if a.count(i)==1:
        print(i)