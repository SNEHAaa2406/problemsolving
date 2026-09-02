#reversing string using stack
s="sneha"
stack=[]
reverse=""
for ch in s:
    stack.append(ch)
while stack:
    reverse+=stack.pop()
print(reverse)