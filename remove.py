num=[54,45,8,1,2]
key=int(input("Enter the number you want to delete:"))
if key in num:
    num.remove(key)
    print(num)
else:
    print("Key is not present")