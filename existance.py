# Search an Element
# Take a number from the user and check whether it exists in the list.
arr=[45,88,20,62,14,77,96]
user=int(input("Enter the number :"))
if user in arr:
    print("It exists.")
else:
    print("Number doesn't exists.")