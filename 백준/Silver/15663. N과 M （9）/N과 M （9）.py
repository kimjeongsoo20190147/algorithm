from itertools import permutations

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
used = set()

for p in permutations(arr,k):
    if p not in used:
        used.add(p)
        print(" ".join(map(str,p)))