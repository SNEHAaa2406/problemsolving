nums = [1, 2, 1, 3, 2, 1]
freq={}
for i in range (len(nums)):
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)
for key,value in freq.items():
    print(key,":",value)