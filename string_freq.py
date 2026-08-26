# Character Frequency ⭐
word = "banana"
fre={}
for ch in word:
    if ch in fre:
        fre[ch]+=1
    else:
        fre[ch]=1
print(fre)
