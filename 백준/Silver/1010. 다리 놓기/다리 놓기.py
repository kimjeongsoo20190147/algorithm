from itertools import combinations
import math

n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    print(math.comb(b,a))