from itertools import combinations

n, target = map(int, input().split())

nums = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    comb = combinations(nums,i)

    for x in comb:
        if sum(x) == target:
            ans += 1 

print(ans)