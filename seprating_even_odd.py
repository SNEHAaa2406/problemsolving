# Separate Even and Odd
# Create two lists:
# one containing even numbers
# one containing odd numbers

num=[78,6,5,96,2,45,0,15]
evem=[]
odd=[]
for i in num:
    if i%2==0:
        evem.append(i)
    else:
        odd.append(i)
print("Even list:",evem)
print("Odd list :",odd)

