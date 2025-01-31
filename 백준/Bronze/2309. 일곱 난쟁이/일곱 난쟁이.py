from itertools import combinations

k = [int(input()) for _ in range(9)]
k.sort()

rst = list(combinations(k, 7))
i = 0
while i < len(rst):
    if sum(rst[i]) == 100:
        print(*rst[i], sep="\n")
        break 
    i += 1
