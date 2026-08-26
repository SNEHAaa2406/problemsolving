# Search for a Key
# Take a key from the user and check whether it exists.
marks = {"Maths": 75, "Python": 82, "DBMS": 68}
find=input("Enter the key you want to find:")
if find in marks:
    print("It is found")
else:
    print("Not found!")