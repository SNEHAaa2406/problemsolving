def large(*args):
    elem=args[0]
    for i in args:
        if i>elem:
            elem=i
    return elem
print(large(10,50,20,30))