num=[78,54,1,5,65,20,1]
key=int(input("Enter the key you want to find:"))
# for i in num:
#     if key==i:
#       print("Number found at index ",i)
#     else:
      # print("number not found")

found=False
for i in range(len(num)):
    if key==num[i]:
        print("Number found at index ",i)
        found=True
if found==False:
    print("Not found")