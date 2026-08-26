data={"Name":"Sneha",
      "Age":25,
      "salary":250000}
data["Name"]="Aditi"
print(data)
print(set(data))
data.pop("Age")
print(data)

for key in data:
    print(key)

for value in data.values():
    print(value)

for key , value in data.items():
    print(key,value)