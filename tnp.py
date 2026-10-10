#min max , zeros at last, even odd using function   

# zero at end
import array as arr
a=arr.array('i',(45,87,0,54,2,0,1,0))
new=[]
for i in a:
    if i !=0:
        new.append(i)
zeroes= a.count(0)
new=new+[0]*zeroes
    
print(new)