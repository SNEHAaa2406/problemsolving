def sep(*args):
    pos=[]
    neg=[]
    for i in args:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)
    return pos,neg
print(sep(12,-4,-6,25))