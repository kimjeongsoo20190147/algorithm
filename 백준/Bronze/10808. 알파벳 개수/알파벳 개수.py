a='abcdefghijklmnopqrstuvwxyz'
b=[0]*len(a)
s=input()
for w in s:
    for i in range(len(a)):
        if w==a[i]:
            b[i]+=1
            break
print(*b)    