import sys
input = lambda: sys.stdin.readline().rstrip()

def is_possible(k):
    global N, C, arr
    
    bef_idx = 0
    cnt = 1
    for idx in range(1,N):
        if arr[idx] - arr[bef_idx] >= k:
            bef_idx = idx
            cnt += 1
            
    return (cnt >= C)


N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

cur = -1
step = int(1e9) + 1

while step != 0:
    while cur + step <= int(1e9) and is_possible(cur+step):
        cur += step
    step //= 2
    
print(cur)
