def even_odd():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd()
print(result)