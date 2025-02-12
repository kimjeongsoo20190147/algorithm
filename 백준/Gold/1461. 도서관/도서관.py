N,M=[*map(int,input().split())]
books=[*map(int,input().split())]
 
plus = []; minus = []; last = 0
for b in books:
    last = max(abs(b),last)
    if b>0:
        plus.append(b)
    else:
        minus.append(abs(b))

plus.sort(reverse = 1)
minus.sort(reverse = 1)
 
result = 0
for i in range(0, len(plus), M):
    result += plus[i]*2
for i in range(0, len(minus), M):
    result += minus[i]*2
print(result-last)