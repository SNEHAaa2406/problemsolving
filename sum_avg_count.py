l=[45,88,22,97,99,98,21,121]
sum=0
avg=0
count=0
for i in range((len(l))):
    sum=sum+l[i]
print("Sum of all elements is :",sum)
for i in l:
    count+=1
avg=sum / count
print("Average of list is :",avg)