from itertools import permutations

n = int(input())
product=[]

for i in range(1,n+1):
    product.append(i)


ans = list(permutations((product), n))

for num in ans:
    for _ in num:
        print(_, end=' ')
    print()