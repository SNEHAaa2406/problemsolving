grades = {
    "Sneha": 92,
    "Riya": 81,
    "Anaya": 67,
    "Priya": 45,
    "Aarav": 76,
    "Neha": 58,
    "Rahul": 95,
    "Isha": 73
}

result = {}

for name, marks in grades.items():

    if marks >= 90:
        result[name] = "A"

    elif 75 <= marks < 90:
        result[name] = "B"

    elif 60 <= marks < 75:
        result[name] = "C"

    else:
        result[name] = "D"

print(result)